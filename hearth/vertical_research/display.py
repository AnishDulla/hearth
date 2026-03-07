from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_run_header(command: str, vertical: str, icp: str = "") -> None:
    console.print(
        Panel.fit(
            f"[bold]Command:[/bold] {command}\n[bold]Vertical:[/bold] {vertical}\n[bold]ICP:[/bold] {icp}",
            title="Vertical Research",
        )
    )


def show_module_result(module: str, tool_calls: int) -> None:
    console.print(f"[green]Completed[/green] {module} (tool calls: {tool_calls})")


def show_saved_paths(report_dir: Path, json_path: Path, md_path: Path) -> None:
    table = Table(title="Saved Outputs")
    table.add_column("Artifact")
    table.add_column("Path")
    table.add_row("Report directory", str(report_dir))
    table.add_row("JSON", str(json_path))
    table.add_row("Markdown", str(md_path))
    console.print(table)


def show_ask_output(result: BaseModel) -> None:
    payload = result.model_dump()
    console.print(Panel(payload.get("answer", ""), title="Synthesis Answer"))
