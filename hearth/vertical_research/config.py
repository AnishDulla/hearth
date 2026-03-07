from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    model: str = os.getenv("VERTICAL_RESEARCH_MODEL", "gpt-5")
    max_turns: int = int(os.getenv("VERTICAL_RESEARCH_MAX_TURNS", "80"))
    synthesis_trigger_turn: int = int(os.getenv("VERTICAL_RESEARCH_SYNTHESIS_TURN", "72"))
    default_icp: str = os.getenv("VERTICAL_RESEARCH_DEFAULT_ICP", "$5M-$50M annual revenue")
    output_dir: Path = Path(os.getenv("VERTICAL_RESEARCH_OUTPUT_DIR", "vertical_research/output"))
    journal_path: Path = Path(os.getenv("VERTICAL_RESEARCH_JOURNAL", "vertical_research/reports/research_journal.md"))


def get_settings() -> Settings:
    settings = Settings()
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    settings.journal_path.parent.mkdir(parents=True, exist_ok=True)
    if not settings.journal_path.exists():
        settings.journal_path.write_text("# Research Journal\n\n", encoding="utf-8")
    return settings
