from __future__ import annotations

import json
from typing import Any

from vertical_research.agent.prompts import opportunities_prompt
from vertical_research.agent.schemas import OpportunitiesReport
from vertical_research.modules.base import BaseModule
from vertical_research.modules.vertical_profiles import get_vertical_focus


class OpportunityRankerModule(BaseModule):
    name = "opportunities"
    display_name = "Opportunity Ranker"

    @property
    def instructions(self) -> str:
        return opportunities_prompt()

    @property
    def output_schema(self) -> type[OpportunitiesReport]:
        return OpportunitiesReport

    def _format_context(self, context: dict[str, Any] | None) -> str:
        if not context:
            return ""

        parts: list[str] = []

        pain_map: list[dict[str, Any]] = []
        workflow_map: list[dict[str, Any]] = []
        technology_map: list[dict[str, Any]] = []

        if isinstance(context.get("pain"), dict):
            pain_map = context["pain"].get("pain_point_map", []) or []
        elif isinstance(context.get("pain_point_map"), list):
            pain_map = context.get("pain_point_map", []) or []

        if isinstance(context.get("workflow"), dict):
            workflow_map = context["workflow"].get("workflow_map", []) or []
        elif isinstance(context.get("workflow_map"), list):
            workflow_map = context.get("workflow_map", []) or []

        if isinstance(context.get("tech"), dict):
            technology_map = context["tech"].get("technology_map", []) or []
        elif isinstance(context.get("technology_map"), list):
            technology_map = context.get("technology_map", []) or []

        if pain_map:
            parts.append("Top recurring pains (prioritize these unless disproven):")
            for pain in pain_map[:8]:
                pain_text = pain.get("pain", "").strip()
                where = pain.get("where_in_workflow", "").strip()
                severity = pain.get("severity", "").strip()
                frequency = pain.get("frequency", "").strip()
                impact = pain.get("economic_impact", "").strip()
                if pain_text:
                    parts.append(
                        f"- {pain_text} | where: {where or 'unknown'} | severity: {severity or 'unknown'} | "
                        f"frequency: {frequency or 'unknown'} | impact: {impact or 'unknown'}"
                    )

        if workflow_map:
            parts.append("\nWorkflow bottlenecks:")
            for stage in workflow_map[:6]:
                stage_name = stage.get("stage", "").strip()
                pains = stage.get("pain_points", []) or []
                owners = stage.get("owner_roles", []) or []
                if stage_name:
                    parts.append(
                        f"- {stage_name} | owners: {', '.join(owners[:3]) or 'unknown'} | "
                        f"pain points: {', '.join(pains[:2]) or 'none listed'}"
                    )

        if technology_map:
            parts.append("\nCurrent software failure points:")
            for category in technology_map[:6]:
                name = category.get("category", "").strip()
                breaks = category.get("where_it_breaks", "").strip()
                vendors = category.get("likely_vendors", []) or []
                if name:
                    parts.append(
                        f"- {name} | vendors: {', '.join(vendors[:3]) or 'unknown'} | "
                        f"breaks: {breaks or 'not specified'}"
                    )

        feasibility_lines: list[str] = []
        if technology_map:
            feasibility_lines.append("- Integration touchpoints should align to existing categories/vendors above.")
            feasibility_lines.append(
                "- Prefer opportunities that can be layered onto current systems without replacing core platforms."
            )
        if pain_map:
            high_frequency_count = sum(
                1 for pain in pain_map if str(pain.get("frequency", "")).strip() in {"daily", "weekly"}
            )
            high_severity_count = sum(
                1 for pain in pain_map if str(pain.get("severity", "")).strip() == "high"
            )
            feasibility_lines.append(
                f"- Data/dependency risk baseline: {high_frequency_count} high-frequency pains, "
                f"{high_severity_count} high-severity pains in current evidence."
            )
        if feasibility_lines:
            parts.append("\nFeasibility context (for adoption scoring):")
            parts.extend(feasibility_lines)

        if not parts:
            return "\n\nPrior context (use but verify):\n" + json.dumps(context, indent=2)[:4000]

        return "\n\nPrior evidence digest:\n" + "\n".join(parts)

    def build_input(self, vertical: str, icp: str, context: dict[str, Any] | None = None) -> str:
        prior = self._format_context(context)
        vertical_focus = get_vertical_focus(vertical).opportunities
        focus = f"\n{vertical_focus}" if vertical_focus else ""
        return (
            f"Rank exactly 3 AI use cases for vertical='{vertical}', ICP='{icp}'. "
            "Use ROI logic grounded in process pain, frequency, impact, adoption feasibility, and buyer clarity."
            + focus
            + prior
        )
