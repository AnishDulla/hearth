from __future__ import annotations

import json
from typing import Any

from vertical_research.agent.prompts import tech_prompt
from vertical_research.agent.schemas import TechReport
from vertical_research.modules.base import BaseModule
from vertical_research.modules.vertical_profiles import get_vertical_focus


class TechMapperModule(BaseModule):
    name = "tech"
    display_name = "Tech Mapper"

    @property
    def instructions(self) -> str:
        return tech_prompt()

    @property
    def output_schema(self) -> type[TechReport]:
        return TechReport

    def build_input(self, vertical: str, icp: str, context: dict[str, Any] | None = None) -> str:
        prior = ""
        if context:
            prior = "\n\nPrior context (use but verify):\n" + json.dumps(context, indent=2)[:6000]
        vertical_focus = get_vertical_focus(vertical).tech
        focus = f"\n{vertical_focus}" if vertical_focus else ""
        return (
            f"Build a current-state technology map for vertical='{vertical}', ICP='{icp}'. "
            "Name software categories, likely vendors, jobs-to-be-done, and exact failure points requiring manual intervention."
            + focus
            + prior
        )
