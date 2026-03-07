from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from agents import Agent, Runner
from openai import APIConnectionError, APIStatusError, APITimeoutError, RateLimitError
from pydantic import BaseModel

from vertical_research.agent.prompts import MAX_TURNS
from vertical_research.agent.schemas import AskSynthesis, VerticalResearchReport
from vertical_research.agent.tools import fetch_page, read_file, web_search
from vertical_research.config import Settings
from vertical_research.memory import get_session
from vertical_research.modules.base import BaseModule, ModuleRunResult
from vertical_research.modules.opportunity_ranker import OpportunityRankerModule
from vertical_research.modules.pain_researcher import PainResearcherModule
from vertical_research.modules.tech_mapper import TechMapperModule
from vertical_research.modules.vertical_scan import VerticalScanModule
from vertical_research.modules.workflow_mapper import WorkflowMapperModule


@dataclass
class OrchestratorResult:
    report: VerticalResearchReport
    module_results: list[ModuleRunResult]


class VerticalResearchOrchestrator:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.workflow_module = WorkflowMapperModule()
        self.pain_module = PainResearcherModule()
        self.tech_module = TechMapperModule()
        self.opportunity_module = OpportunityRankerModule()
        self.vertical_module = VerticalScanModule()

    def _build_agent(self, module: BaseModule, model: str | None = None) -> Agent:
        return Agent(
            name=module.display_name,
            instructions=module.instructions,
            tools=[web_search, fetch_page, read_file],
            output_type=module.output_schema,
            model=model or self.settings.model,
        )

    def _tool_calls(self, result: Any) -> int:
        return sum(1 for item in result.new_items if item.__class__.__name__ == "ToolCallItem")

    def run_module(
        self,
        module: BaseModule,
        vertical: str,
        icp: str,
        context: dict[str, Any] | None = None,
        model: str | None = None,
    ) -> ModuleRunResult:
        agent = self._build_agent(module=module, model=model)
        user_input = module.build_input(vertical=vertical, icp=icp, context=context)
        session = get_session(command=module.name, vertical=vertical, icp=icp)
        notes: list[str] = []
        try:
            result = Runner.run_sync(agent, user_input, max_turns=self.settings.max_turns, session=session)
            final_output = result.final_output
            if isinstance(final_output, BaseModel):
                typed_output = final_output
            else:
                typed_output = module.output_schema.model_validate(final_output)
            raw_text = result.final_output_text if hasattr(result, "final_output_text") else str(typed_output)
            return ModuleRunResult(
                name=module.name,
                output=typed_output,
                raw_text=raw_text or str(final_output),
                tool_calls=self._tool_calls(result),
                notes=notes,
            )
        except RateLimitError as exc:
            raise RuntimeError(f"Rate limited while running {module.name}: {exc}") from exc
        except APIStatusError as exc:
            raise RuntimeError(f"API status error while running {module.name}: {exc.status_code} {exc}") from exc
        except (APITimeoutError, APIConnectionError) as exc:
            raise RuntimeError(f"Connectivity error while running {module.name}: {exc}") from exc
        except Exception as exc:  # noqa: BLE001
            if "max turn" not in str(exc).lower():
                raise
            notes.append(
                f"Reached turn cap ({self.settings.max_turns}); forcing synthesis with constrained follow-up run."
            )
            nudge = (
                "Stop additional research now. Produce the final structured output immediately, "
                "marking uncertain items in confidence_notes."
            )
            result = Runner.run_sync(agent, nudge, max_turns=8, session=session)
            final_output = result.final_output
            if isinstance(final_output, BaseModel):
                typed_output = final_output
            else:
                typed_output = module.output_schema.model_validate(final_output)
            raw_text = result.final_output_text if hasattr(result, "final_output_text") else str(typed_output)
            return ModuleRunResult(
                name=module.name,
                output=typed_output,
                raw_text=raw_text,
                tool_calls=self._tool_calls(result),
                notes=notes,
            )

    def run_full(self, vertical: str, icp: str, model: str | None = None) -> OrchestratorResult:
        workflow = self.run_module(self.workflow_module, vertical=vertical, icp=icp, model=model)
        pain = self.run_module(
            self.pain_module,
            vertical=vertical,
            icp=icp,
            context=workflow.output.model_dump(),
            model=model,
        )
        tech = self.run_module(
            self.tech_module,
            vertical=vertical,
            icp=icp,
            context={
                "workflow": workflow.output.model_dump(),
                "pain": pain.output.model_dump(),
            },
            model=model,
        )
        opportunities = self.run_module(
            self.opportunity_module,
            vertical=vertical,
            icp=icp,
            context={
                "workflow": workflow.output.model_dump(),
                "pain": pain.output.model_dump(),
                "tech": tech.output.model_dump(),
            },
            model=model,
        )

        synthesis_context = {
            "specialist_outputs": {
                "workflow": workflow.output.model_dump(),
                "pain": pain.output.model_dump(),
                "tech": tech.output.model_dump(),
                "opportunities": opportunities.output.model_dump(),
            },
            "synthesis_nudge": (
                f"If this run approaches turn {self.settings.synthesis_trigger_turn}, stop gathering evidence and synthesize now."
            ),
        }
        final_result = self.run_module(
            self.vertical_module,
            vertical=vertical,
            icp=icp,
            context=synthesis_context,
            model=model,
        )

        return OrchestratorResult(
            report=final_result.output,
            module_results=[workflow, pain, tech, opportunities, final_result],
        )

    def run_workflow(self, vertical: str, icp: str, model: str | None = None) -> ModuleRunResult:
        return self.run_module(self.workflow_module, vertical=vertical, icp=icp, model=model)

    def run_pains(self, vertical: str, icp: str, model: str | None = None) -> ModuleRunResult:
        return self.run_module(self.pain_module, vertical=vertical, icp=icp, model=model)

    def run_tech(self, vertical: str, icp: str, model: str | None = None) -> ModuleRunResult:
        return self.run_module(self.tech_module, vertical=vertical, icp=icp, model=model)

    def run_opportunities(self, vertical: str, icp: str, model: str | None = None) -> ModuleRunResult:
        context = {
            "instruction": "Use prior reports if available through read_file('vertical_research/reports/research_journal.md')."
        }
        return self.run_module(self.opportunity_module, vertical=vertical, icp=icp, context=context, model=model)

    def ask(self, question: str, journal_context: str, model: str | None = None) -> AskSynthesis:
        from vertical_research.agent.prompts import ask_prompt

        ask_agent = Agent(
            name="Vertical Research Synthesis",
            instructions=ask_prompt(),
            tools=[read_file],
            output_type=AskSynthesis,
            model=model or self.settings.model,
        )
        user_input = f"Question: {question}\n\nJournal context:\n{journal_context}"
        result = Runner.run_sync(
            ask_agent,
            user_input,
            session=get_session(command="ask"),
            max_turns=min(MAX_TURNS, 30),
        )
        return result.final_output
