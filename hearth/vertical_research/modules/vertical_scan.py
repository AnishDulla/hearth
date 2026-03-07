from __future__ import annotations

from typing import Any

from vertical_research.agent.prompts import main_orchestrator_prompt
from vertical_research.agent.schemas import VerticalResearchReport
from vertical_research.modules.base import BaseModule
from vertical_research.modules.vertical_profiles import get_vertical_focus


class VerticalScanModule(BaseModule):
    name = "vertical_scan"
    display_name = "Vertical Research"

    @property
    def instructions(self) -> str:
        return main_orchestrator_prompt()

    @property
    def output_schema(self) -> type[VerticalResearchReport]:
        return VerticalResearchReport

    def build_input(self, vertical: str, icp: str, context: dict[str, Any] | None = None) -> str:
        synthesis_focus = get_vertical_focus(vertical).synthesis
        focus = f"\n{synthesis_focus}" if synthesis_focus else ""
        return f"""
Research target:
- Vertical: {vertical}
- ICP: {icp}

Deliver a full operating-model reconstruction report in the required schema.
Prioritize concrete detail for firms in this exact ICP.
Use multiple independent sources and resolve contradictions explicitly.
{focus}
""".strip()
