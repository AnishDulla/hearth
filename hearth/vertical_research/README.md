# vertical_research

`vertical_research` is a Python CLI agentic system built on the OpenAI Agents SDK for one product mission: investment-grade vertical operating-model reconstruction.

Primary target use case:
- Vertical: plaintiff-side personal injury law firms
- ICP: firms doing roughly `$5M-$50M` annual revenue (default, configurable via env)

## What It Produces

For each run, it reconstructs:
1. current workflow/process reality
2. recurring pain points and root causes
3. current technology stack categories and likely vendors
4. top 3 highest-ROI AI opportunities

Outputs are saved as both JSON and Markdown in timestamped folders.

## Architecture

One main Vertical Research Agent product with internal specialists:
- `Workflow Mapper`
- `Pain Researcher`
- `Tech Mapper`
- `Opportunity Ranker`

The orchestrator runs specialists, then synthesizes with the main agent into a strict final schema.

## Setup

1. Python 3.12+
2. Install dependencies:

```bash
pip install -r vertical_research/requirements.txt
```

3. Set environment variables in `.env`:

```bash
OPENAI_API_KEY=your_key_here
VERTICAL_RESEARCH_MODEL=gpt-5
VERTICAL_RESEARCH_MAX_TURNS=80
VERTICAL_RESEARCH_SYNTHESIS_TURN=72
VERTICAL_RESEARCH_DEFAULT_ICP=$5M-$50M annual revenue
```

4. Run commands:

```bash
./vertical-research run "PI law firms"
./vertical-research workflow "PI law firms"
./vertical-research pains "PI law firms"
./vertical-research tech "PI law firms"
./vertical-research opportunities "PI law firms"
./vertical-research ask "Which buyer role is most likely to sponsor intake automation first?"
```

Optional shell alias:

```bash
alias vertical-research='./vertical-research'
vertical-research run "PI law firms"
```

## Commands

- `./vertical-research run "vertical"`
  - full pipeline + full schema report
- `./vertical-research workflow "vertical"`
  - workflow reconstruction only
- `./vertical-research pains "vertical"`
  - pain/root-cause analysis only
- `./vertical-research tech "vertical"`
  - technology map only
- `./vertical-research opportunities "vertical"`
  - top-3 AI use case ranking only
- `./vertical-research ask "question"`
  - synthesis over accumulated memory in `research_journal.md`

## Output Locations

- Timestamped outputs:
  - vertical commands: `vertical_research/output/<vertical>_<YYYYMMDD>/`
  - repeated same-day runs append numeric suffix: `<vertical>_<YYYYMMDD>_2`
  - `ask` command: `vertical_research/output/ask_<YYYYMMDD>/`
  - `<command>.json`
  - `<command>.md`
- Durable memory journal: `vertical_research/reports/research_journal.md`

## Notes

- Uses OpenAI Agents SDK primitives: `Agent`, `Runner`, `function_tool`, structured `output_type`, and `SQLiteSession` memory.
- Tool outputs are truncated to protect context windows.
- Turn caps and synthesis-turn instructions are included to avoid run-away loops.
