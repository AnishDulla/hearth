from __future__ import annotations

import sys
import typer

from vertical_research.config import get_settings
from vertical_research.display import console, show_ask_output, show_module_result, show_run_header, show_saved_paths
from vertical_research.repoer import new_report_dir, save_model_outputs

app = typer.Typer(add_completion=False, no_args_is_help=True)


def _ensure_supported_python() -> None:
    if sys.version_info < (3, 12):
        console.print(
            "[red]Python 3.12+ is required.[/red]\n"
            f"You are running: [yellow]{sys.version.split()[0]}[/yellow]\n"
            "Use the project launcher instead:\n"
            "  ./vertical-research run \"your vertical\""
        )
        raise SystemExit(1)


def _new_orchestrator(settings):
    _ensure_supported_python()
    from vertical_research.agent.orchestrator import VerticalResearchOrchestrator

    return VerticalResearchOrchestrator(settings=settings)


def _append_journal(*args, **kwargs):
    from vertical_research.memory import append_journal

    return append_journal(*args, **kwargs)


def _append_note(*args, **kwargs):
    from vertical_research.memory import append_note

    return append_note(*args, **kwargs)


def _read_journal(*args, **kwargs):
    from vertical_research.memory import read_journal

    return read_journal(*args, **kwargs)


@app.command()
def run(
    vertical: str = typer.Argument(..., help="Target vertical"),
    model: str | None = typer.Option(None, "--model", help="Override model"),
) -> None:
    settings = get_settings()
    icp = settings.default_icp
    show_run_header(command="run", vertical=vertical, icp=icp)
    orchestrator = _new_orchestrator(settings=settings)

    outcome = orchestrator.run_full(vertical=vertical, icp=icp, model=model)
    report_dir = new_report_dir(settings.output_dir, command="run")

    for module_result in outcome.module_results:
        show_module_result(module_result.name, module_result.tool_calls)
        save_model_outputs(
            report_dir,
            module_result.name,
            module_result.output,
            raw_text=module_result.raw_text,
        )

    json_path, md_path = save_model_outputs(
        report_dir,
        "full_report",
        outcome.report,
        raw_text=outcome.module_results[-1].raw_text if outcome.module_results else None,
    )
    show_saved_paths(report_dir, json_path, md_path)

    open_questions = outcome.report.confidence_notes.needs_interviews
    _append_journal(
        journal_path=settings.journal_path,
        vertical=vertical,
        icp=icp,
        report=outcome.report,
        open_questions=open_questions,
    )
    console.print(f"[cyan]Journal updated:[/cyan] {settings.journal_path}")


def _run_single(
    command: str,
    vertical: str,
    icp: str,
    runner,
    model: str | None,
) -> None:
    settings = get_settings()
    show_run_header(command=command, vertical=vertical, icp=icp)
    orchestrator = _new_orchestrator(settings=settings)
    result = runner(orchestrator, vertical, icp, model)

    report_dir = new_report_dir(settings.output_dir, command=command)
    json_path, md_path = save_model_outputs(
        report_dir,
        command,
        result.output,
        raw_text=result.raw_text,
    )
    show_module_result(result.name, result.tool_calls)
    show_saved_paths(report_dir, json_path, md_path)

    bullets = []
    payload = result.output.model_dump()
    for key in ("workflow_map", "pain_point_map", "technology_map", "top_ai_use_cases"):
        if key in payload and isinstance(payload[key], list):
            bullets.append(f"{key}: {len(payload[key])} items")
    _append_note(settings.journal_path, f"{command} | {vertical} | {icp}", bullets)


@app.command()
def workflow(
    vertical: str = typer.Argument(...),
    model: str | None = typer.Option(None, "--model"),
) -> None:
    icp = get_settings().default_icp
    _run_single("workflow", vertical, icp, lambda o, v, i, m: o.run_workflow(v, i, m), model)


@app.command()
def pains(
    vertical: str = typer.Argument(...),
    model: str | None = typer.Option(None, "--model"),
) -> None:
    icp = get_settings().default_icp
    _run_single("pains", vertical, icp, lambda o, v, i, m: o.run_pains(v, i, m), model)


@app.command()
def tech(
    vertical: str = typer.Argument(...),
    model: str | None = typer.Option(None, "--model"),
) -> None:
    icp = get_settings().default_icp
    _run_single("tech", vertical, icp, lambda o, v, i, m: o.run_tech(v, i, m), model)


@app.command()
def opportunities(
    vertical: str = typer.Argument(...),
    model: str | None = typer.Option(None, "--model"),
) -> None:
    icp = get_settings().default_icp
    _run_single("opportunities", vertical, icp, lambda o, v, i, m: o.run_opportunities(v, i, m), model)


@app.command()
def ask(
    question: str = typer.Argument(..., help="Question over prior research"),
    model: str | None = typer.Option(None, "--model"),
) -> None:
    settings = get_settings()
    orchestrator = _new_orchestrator(settings=settings)
    journal = _read_journal(settings.journal_path)
    result = orchestrator.ask(question=question, journal_context=journal, model=model)
    show_ask_output(result)

    report_dir = new_report_dir(settings.output_dir, command="ask")
    json_path, md_path = save_model_outputs(report_dir, "ask", result, raw_text=result.answer)
    show_saved_paths(report_dir, json_path, md_path)

    _append_note(settings.journal_path, "ask", [f"Q: {question}", f"A: {result.answer[:280]}"])


def main() -> None:
    _ensure_supported_python()
    app()


if __name__ == "__main__":
    main()
