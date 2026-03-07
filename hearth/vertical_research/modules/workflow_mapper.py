from __future__ import annotations

import json
from typing import Any

from vertical_research.agent.prompts import workflow_prompt
from vertical_research.agent.schemas import WorkflowReport
from vertical_research.modules.base import BaseModule
from vertical_research.modules.vertical_profiles import get_vertical_focus


class WorkflowMapperModule(BaseModule):
    name = "workflow"
    display_name = "Workflow Mapper"

    @property
    def instructions(self) -> str:
        return workflow_prompt()

    @property
    def output_schema(self) -> type[WorkflowReport]:
        return WorkflowReport

    def build_input(self, vertical: str, icp: str, context: dict[str, Any] | None = None) -> str:
        prior = ""
        if context:
            prior = "\n\nPrior context (use but verify):\n" + json.dumps(context, indent=2)[:6000]
        vertical_focus = get_vertical_focus(vertical).workflow
        focus = f"\n{vertical_focus}" if vertical_focus else ""
        return (
            f"Map current-state workflows for vertical='{vertical}', ICP='{icp}'. "
            "Output stage-by-stage operational detail with owners, tools, handoffs, manual work, and stage pain."
            + focus
            + prior
        )
