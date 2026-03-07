from __future__ import annotations

import json
from typing import Any

from vertical_research.agent.prompts import pain_prompt
from vertical_research.agent.schemas import PainReport
from vertical_research.modules.base import BaseModule
from vertical_research.modules.vertical_profiles import get_vertical_focus


class PainResearcherModule(BaseModule):
    name = "pains"
    display_name = "Pain Researcher"

    @property
    def instructions(self) -> str:
        return pain_prompt()

    @property
    def output_schema(self) -> type[PainReport]:
        return PainReport

    def build_input(self, vertical: str, icp: str, context: dict[str, Any] | None = None) -> str:
        prior = ""
        if context:
            prior = "\n\nPrior context (use but verify):\n" + json.dumps(context, indent=2)[:6000]
        vertical_focus = get_vertical_focus(vertical).pains
        focus = f"\n{vertical_focus}" if vertical_focus else ""
        return (
            f"Identify persistent high-value pain points for vertical='{vertical}', ICP='{icp}'. "
            "Explain causal roots, who feels each pain, workarounds, and why workarounds fail."
            + focus
            + prior
        )
