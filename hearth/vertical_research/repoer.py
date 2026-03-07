from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel


def new_report_dir(base_dir: Path, command: str) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = base_dir / f"{stamp}_{command}"
    report_dir.mkdir(parents=True, exist_ok=True)
    return report_dir


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def render_markdown(title: str, payload: dict[str, Any], raw_text: str | None = None) -> str:
    lines: list[str] = [f"# {title}", ""]
    if raw_text:
        lines.extend(["## Narrative Synthesis", raw_text.strip(), ""])
    for key, value in payload.items():
        lines.append(f"## {key}")
        if isinstance(value, list):
            if not value:
                lines.append("- None")
            else:
                for idx, item in enumerate(value, start=1):
                    if isinstance(item, dict):
                        lines.append(f"### Item {idx}")
                        for k, v in item.items():
                            lines.append(f"- **{k}**: {v}")
                    else:
                        lines.append(f"- {item}")
        elif isinstance(value, dict):
            for k, v in value.items():
                lines.append(f"- **{k}**: {v}")
        else:
            lines.append(str(value))
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def save_markdown(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def save_model_outputs(
    report_dir: Path,
    name: str,
    model_output: BaseModel,
    raw_text: str | None = None,
) -> tuple[Path, Path]:
    payload = model_output.model_dump()
    json_path = report_dir / f"{name}.json"
    md_path = report_dir / f"{name}.md"
    save_json(json_path, payload)
    save_markdown(md_path, render_markdown(title=name, payload=payload, raw_text=raw_text))
    return json_path, md_path
