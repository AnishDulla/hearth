from __future__ import annotations

from datetime import datetime
from hashlib import sha1
from pathlib import Path

from agents import SQLiteSession

from vertical_research.agent.schemas import VerticalResearchReport


def build_session_id(command: str, vertical: str = "", icp: str = "") -> str:
    raw = f"{command}|{vertical}|{icp}".encode("utf-8")
    digest = sha1(raw).hexdigest()[:12]
    return f"vertical_research_{command}_{digest}"


def get_session(command: str, vertical: str = "", icp: str = "") -> SQLiteSession:
    return SQLiteSession(build_session_id(command=command, vertical=vertical, icp=icp))


def append_journal(
    journal_path: Path,
    vertical: str,
    icp: str,
    report: VerticalResearchReport,
    open_questions: list[str] | None = None,
) -> None:
    open_questions = open_questions or []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    durable_findings = [stage.stage for stage in report.workflow_map[:5]]
    pain_signals = [pain.pain for pain in report.pain_point_map[:5]]
    tech_findings = [f"{t.category}: {', '.join(t.likely_vendors[:3])}" for t in report.technology_map[:5]]
    ai_candidates = [f"#{u.rank} {u.name}" for u in report.top_ai_use_cases[:5]]
    contradictions = report.confidence_notes.inferred_but_not_confirmed[:5]
    durable_lines = [f"- {item}" for item in durable_findings] or ["- None captured"]
    pain_lines = [f"- {item}" for item in pain_signals] or ["- None captured"]
    tech_lines = [f"- {item}" for item in tech_findings] or ["- None captured"]
    ai_lines = [f"- {item}" for item in ai_candidates] or ["- None captured"]
    question_lines = [f"- {item}" for item in open_questions] or ["- None"]
    contradiction_lines = [f"- {item}" for item in contradictions] or ["- None captured"]

    lines = [
        f"## {timestamp} | {vertical} | {icp}",
        "",
        "### Durable Findings",
        *durable_lines,
        "",
        "### Strongest Pain Signals",
        *pain_lines,
        "",
        "### Strongest Tech Stack Findings",
        *tech_lines,
        "",
        "### Candidate AI Use Cases",
        *ai_lines,
        "",
        "### Open Questions",
        *question_lines,
        "",
        "### Contradictions / Uncertain Claims",
        *contradiction_lines,
        "",
    ]
    with journal_path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def read_journal(journal_path: Path, max_chars: int = 32000) -> str:
    if not journal_path.exists():
        return "# Research Journal\n\nNo prior research available."
    content = journal_path.read_text(encoding="utf-8", errors="ignore")
    if len(content) <= max_chars:
        return content
    return content[-max_chars:]


def append_note(journal_path: Path, title: str, bullets: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [f"## {timestamp} | {title}", ""]
    lines.extend(f"- {bullet}" for bullet in bullets if bullet.strip())
    lines.append("")
    with journal_path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
