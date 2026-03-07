# Agent Prompt Patterns — 1-Shot OpenAI Agents SDK Agent Creation

A catalog of prompt schemas for building different types of agentic systems with the OpenAI Agents SDK. Each pattern produces a working CLI agent in a single well-structured prompt.

---

## The Meta-Pattern: What Every Agent Prompt Needs

Before the specific patterns, understand the 6 variables that define any OpenAI-powered agent:

```text
1. PERSONA        → who the agent acts as (analyst, engineer, PM, lawyer...)
2. TOOLS          → what external actions it can take (search, fetch, read files, call APIs...)
3. LOOP BEHAVIOR  → max turns, when to stop, approval/guardrail behavior
4. OUTPUT SCHEMA  → what structured data it must produce (Pydantic model, JSON fields, markdown sections)
5. CLI INTERFACE  → commands, arguments, flags, how the user invokes it
6. MEMORY         → what persists between sessions (journal, cache, session, knowledge base)
```

The quality of a 1-shot agent prompt is determined by how precisely you specify all 6. Vague on any one → the agent works but is shallow or unpredictable.

---

## Quick Start: Choose Your Agent Type

| Use Case | Pattern | Best For |
|----------|---------|----------|
| **Market research / due diligence** | Research Agent | VCs, analysts, competitive intelligence |
| **Feature planning / PRD writing** | PM Agent | Product teams, user research |
| **Competitor tracking** | CI Agent | Strategy, sales, competitive monitoring |
| **Code security review** | Technical Audit | Security teams, architecture reviews |
| **Understanding customer voice** | Customer Research | Product, support, GTM teams |
| **Sales call prep** | Sales Intelligence | Enterprise sales, account research |
| **Any new domain** | Universal Template | Build custom agents with confidence |

---

## Pattern 1: The Research Agent (OpenAI Version)

**Best for:** Market research, competitive intelligence, due diligence, technology landscape analysis

### The 1-Shot Prompt Schema

```text
Build a Python CLI research agent called [NAME] using the OpenAI Agents SDK.

PERSONA: [senior analyst persona — be specific about their expertise]
e.g. "a senior VC analyst at a top-tier fund who writes investment committee memos"

TOOLS (implement these primarily as OpenAI function_tool tools):
- web_search(query, max_results=8) → uses DuckDuckGo (ddgs package), returns [{title, url, snippet}]
  OR swap to the OpenAI hosted WebSearchTool if you want OpenAI-managed search
- fetch_page(url, max_chars=8000) → uses httpx + BeautifulSoup4, returns cleaned text

AGENTIC LOOP (use the SDK's native Runner loop — NO LangChain):
- MAX_TURNS = 80
- SYNTHESIS_TRIGGER_TURN = 72 (inject a wrap-up nudge near this point)
- Use Runner.run()/Runner.run_sync() for normal execution
- The SDK handles tool-call / tool-result chaining internally
- If a run nears the turn cap, add a user note telling the agent to stop researching and write the analysis
- Always save result.final_output_text (or stringified final_output) regardless of structured parsing success

SYSTEM PROMPT STRUCTURE for each research module:
1. Analyst persona + research protocol
2. Phased search strategy (4 phases: industry → competitive → investment → opportunity)
3. Stopping condition: "stop after 15-25 data points, write analysis"
4. 8-section research framework: [industry overview, TAM/SAM/SOM, incumbents,
   AI disruption map, startup landscape, investment activity, buildable opportunity, founder profile]
5. Exact structured output schema with all field names specified

OUTPUT:
- reports/TIMESTAMP/[module].json (full structured data + raw_analysis field)
- reports/TIMESTAMP/[module].md (raw narrative first, then structured sections)
- research_journal.md (auto-updated with 5-8 bullet extractions per run)

CLI (Typer):
- [name] diligence "market name"     → VC-grade deep dive on any market
- [name] ask "question"              → synthesis across all prior reports (no new web research unless explicitly requested)
- [name] journal                     → show accumulated research bullets
- Common flags: --output-dir, --model, --no-save

TECH STACK: Python 3.12+, openai-agents, openai, typer[all], rich, httpx, beautifulsoup4, lxml, ddgs, python-dotenv, pydantic
```

### Key Design Insight for Research Agents

The schema in the instructions acts as a **research checklist**. When the agent knows it must populate `incumbents[].weakness`, it specifically searches for incumbent weaknesses. The output format drives the input behavior.

---

## Pattern 2: The PM Agent

**Best for:** Product discovery, feature prioritization, PRD generation, user research synthesis, roadmap planning

### The 1-Shot Prompt Schema

```text
Build a Python CLI PM intelligence agent called [NAME] using the OpenAI Agents SDK.

PERSONA: "a Principal PM at a top-tier product org who thinks in terms of user outcomes,
jobs-to-be-done, and measurable impact. You write PRDs that engineering teams can execute
without asking clarifying questions."

TOOLS:
- web_search(query) → DuckDuckGo search via function_tool
- fetch_page(url) → httpx + BeautifulSoup via function_tool
- read_file(path) → reads local files (user research notes, transcripts, analytics exports)

COMMANDS:
- [name] discover "product area"       → research what users actually want in this area
- [name] prd "feature name"            → generate a full PRD from research
- [name] prioritize "problem list"     → stack-rank a set of problems by impact/effort
- [name] compete "your product"        → competitive teardown of similar products
- [name] ask "question"                → synthesis across all prior PM research

SYSTEM PROMPT STRUCTURE for each module:
1. PM persona — focus on user outcomes, not feature lists
2. Research phases:
   Phase 1 — Jobs to be done: "[product area] user problems frustrations 2025"
   Phase 2 — Competitive: "[product area] competitor product decisions teardown"
   Phase 3 — Signals: "[product area] reddit complaints forum feedback user voice"
   Phase 4 — Opportunity: "what [product area] products are NOT doing well"
3. Stopping condition: "after 10-15 user pain signals with evidence, write the PRD"

OUTPUT SCHEMA for `prd` command:
{
  "feature": "name",
  "problem_statement": "what user pain this solves",
  "jobs_to_be_done": ["I want to...", "so that..."],
  "user_stories": [{"persona": "...", "story": "As a... I want... So that..."}],
  "success_metrics": [{"metric": "...", "target": "...", "measurement": "..."}],
  "out_of_scope": ["explicitly excluded"],
  "open_questions": ["unanswered design questions"],
  "competitive_reference": [{"product": "...", "how_they_solve_it": "..."}]
}

MEMORY:
- pm_journal.md: accumulates user pain signals across sessions
- Each `discover` run → extract 5-8 "users say..." bullets with source
- `ask` synthesizes across all accumulated user research
```

---

## Pattern 3: The Competitive Intelligence Agent

**Best for:** Ongoing competitor monitoring, pricing changes, feature launches, funding events

### The 1-Shot Prompt Schema

```text
Build a Python CLI competitive intelligence agent called [NAME] using the OpenAI Agents SDK.

PERSONA: "a competitive intelligence analyst who tracks what competitors are actually doing
— not their marketing, but their product changes, pricing, hiring signals, and customer
sentiment. You think like a chess player: what does their move mean for us?"

TOOLS:
- web_search(query) → DuckDuckGo via function_tool
- fetch_page(url) → httpx + BeautifulSoup via function_tool
- check_sitemap(domain) → fetches sitemap.xml to find new pages (signals product launches)

COMMANDS:
- [name] monitor "CompanyA CompanyB CompanyC"  → research all named competitors
- [name] track "company" --since "2025-01-01"  → what changed since a date
- [name] pricing "company"                     → deep dive on pricing/packaging
- [name] hiring "company"                      → infer product direction from job posts
- [name] ask "question"                        → synthesize across all competitive research

SYSTEM PROMPT STRUCTURE:
1. Intelligence analyst persona — focus on what moves mean, not just what they are
2. Search phases:
   Phase 1 — Recent moves: "[company] product update launch 2025 site:techcrunch.com"
   Phase 2 — Customer reaction: "[company] review 2025 G2 Trustpilot Reddit"
   Phase 3 — Hiring signals: "[company] jobs hiring site:linkedin.com machine learning OR AI"
   Phase 4 — Strategic inference: "[company] partnership acquisition 2025"
3. For each finding: ask "what does this signal about their strategic direction?"

OUTPUT SCHEMA:
{
  "company": "name",
  "period_analyzed": "date range",
  "key_moves": [{"move": "...", "what_it_signals": "...", "threat_level": "high/medium/low"}],
  "pricing_changes": [{"change": "...", "our_implication": "..."}],
  "hiring_signals": [{"role": "...", "inference": "what this means they're building"}],
  "customer_sentiment_shift": "positive/negative/neutral + evidence",
  "recommended_response": ["action we should take"]
}

MEMORY:
- competitor_journal.md per competitor — tracks moves over time
- `ask` answers: "how has [company]'s strategy shifted over the last 3 months?"
```

---

## Pattern 4: The Code Review / Technical Audit Agent

**Best for:** Security audits, architecture reviews, dependency analysis, technical debt mapping

### The 1-Shot Prompt Schema

```text
Build a Python CLI technical audit agent called [NAME] using the OpenAI Agents SDK.

PERSONA: "a senior staff engineer and security-conscious architect who reviews code the
way a hostile acquirer's technical due diligence team would — looking for structural
problems, security exposure, scaling constraints, and hidden technical debt."

TOOLS:
- read_file(path) → reads local source files
- search_codebase(pattern, directory) → grep-like search across local files
- web_search(query) → looks up CVEs, known vulnerabilities, library issues
- fetch_page(url) → reads documentation or vulnerability databases

COMMANDS:
- [name] audit "path/to/repo"           → full technical audit of a codebase
- [name] security "path/to/repo"        → security-focused scan
- [name] deps "requirements.txt"        → dependency vulnerability analysis
- [name] architecture "path/to/repo"    → architectural pattern analysis
- [name] ask "question about the code"  → synthesize across audit findings

NOTE: This agent reads LOCAL files, not the web, as its primary data source.
The run should inspect files first, then web_search for specific CVEs/issues it discovers.

SYSTEM PROMPT STRUCTURE:
1. Staff engineer + security mindset persona
2. File reading phases:
   Phase 1 — Entry points: read main.py, app.py, index.ts (understand what the system does)
   Phase 2 — Security surface: find all places user input is processed, DB queries, auth
   Phase 3 — Dependencies: read requirements.txt or package.json, search for known CVEs
   Phase 4 — Architecture patterns: look for anti-patterns, coupling issues, scaling constraints
3. Stopping condition: "after reading 15-20 files and identifying all major risk areas"

OUTPUT SCHEMA:
{
  "overall_risk": "critical/high/medium/low",
  "security_findings": [{"severity": "...", "location": "file:line", "issue": "...", "fix": "..."}],
  "architecture_issues": [{"issue": "...", "impact": "...", "effort_to_fix": "..."}],
  "dependency_risks": [{"package": "...", "version": "...", "cve": "...", "recommendation": "..."}],
  "technical_debt_map": [{"area": "...", "debt_level": "...", "description": "..."}],
  "immediate_actions": ["prioritized list of things to fix this week"]
}
```

---

## Pattern 5: The Customer Research Agent

**Best for:** Understanding what customers actually say, synthesizing support tickets, NPS analysis, VOC programs

### The 1-Shot Prompt Schema

```text
Build a Python CLI customer intelligence agent called [NAME] using the OpenAI Agents SDK.

PERSONA: "a Head of Customer Research who finds the signal in the noise of customer
feedback — identifying the real underlying job-to-be-done behind complaints, the
patterns that predict churn, and the segments that love the product most."

TOOLS:
- web_search(query) → DuckDuckGo (public reviews, forums)
- fetch_page(url) → reads review sites, forums, social media
- read_file(path) → reads local CSV/JSON exports of support tickets, NPS data

COMMANDS:
- [name] reviews "product name"          → scrape + analyze public reviews
- [name] sentiment "product name"        → track sentiment trends
- [name] churn-signals "product name"    → find what dissatisfied customers say
- [name] love-signals "product name"     → find what loyal customers say
- [name] ask "question"                  → synthesize across all customer research

SEARCH STRATEGY:
Phase 1 — Find real customer voice:
  "[product] review site:g2.com OR site:trustpilot.com OR site:capterra.com"
  "[product] reddit honest review 2025"
  "[product] cancelling subscription why"

Phase 2 — Find the patterns:
  "[product] negative feedback complaints"
  "[product] feature request most upvoted"
  "[product] what I wish [product] had"

OUTPUT SCHEMA:
{
  "product": "name",
  "overall_sentiment": "positive/mixed/negative",
  "top_loves": [{"theme": "...", "frequency": "...", "representative_quote": "..."}],
  "top_frustrations": [{"theme": "...", "frequency": "...", "representative_quote": "..."}],
  "churn_risk_signals": ["specific things people say before leaving"],
  "segment_insights": [{"segment": "...", "what_they_care_about": "..."}],
  "product_gaps": ["things customers want that don't exist"]
}
```

---

## Pattern 6: The Sales Intelligence Agent

**Best for:** Account research before sales calls, ICP refinement, lead qualification, deal intelligence

### The 1-Shot Prompt Schema

```text
Build a Python CLI sales intelligence agent called [NAME] using the OpenAI Agents SDK.

PERSONA: "an elite enterprise sales researcher who preps AEs for calls by finding the
exact pain, the internal champion profile, the budget signals, and the competitive
situation — in under 10 minutes of research per account."

TOOLS:
- web_search(query) → DuckDuckGo
- fetch_page(url) → company pages, news, LinkedIn

COMMANDS:
- [name] account "Company Name"          → full account research brief
- [name] champion "Company" "title"      → research a specific buyer persona
- [name] trigger "Company"               → find buying triggers (funding, leadership, layoffs)
- [name] icp "your product description"  → identify ideal customer profile signals
- [name] ask "question about account"    → synthesize across account research

SEARCH STRATEGY for account research:
Phase 1 — Company context:
  "[Company] funding round 2024 2025"
  "[Company] tech stack engineering blog"
  "[Company] headcount growth hiring 2025"

Phase 2 — Pain signals:
  "[Company] problems challenges 2025 Reddit OR HN"
  "[Company] competitors why switched"
  "[Company] job postings [relevant role]"

Phase 3 — Trigger events:
  "[Company] new CTO OR CIO OR VP Engineering 2025"
  "[Company] layoffs OR restructuring 2025"
  "[Company] acquisition 2024 2025"

OUTPUT SCHEMA:
{
  "company": "name",
  "research_date": "...",
  "executive_summary": "3-sentence brief for AE to read 5 minutes before call",
  "pain_hypothesis": "what we believe their biggest relevant problem is",
  "likely_champion": {"title": "...", "why_they_care": "...", "likely_objection": "..."},
  "trigger_events": [{"event": "...", "date": "...", "relevance_to_us": "..."}],
  "competitive_situation": "who else are they evaluating and why",
  "opening_questions": ["3 questions to open the discovery call"],
  "red_flags": ["reasons this might not be a good fit"]
}
```

---

## Pattern 7: The Universal Agent Template

If you want to build ANY agent type, fill in this template and give it to your code generator / coding agent:

```markdown
Build a Python CLI agentic system called [NAME] using the OpenAI Agents SDK.

## Stack
Python 3.12+, openai-agents, openai, typer[all], rich, httpx, beautifulsoup4, lxml, ddgs, python-dotenv, pydantic

## Architecture
Follow this exact pattern:
- [name]/
  - config.py       → OPENAI_API_KEY, DEFAULT_MODEL, MAX_TURNS=80
  - main.py         → Typer CLI with all commands
  - memory.py       → research_journal.md + `ask` command synthesis
  - agent/
    - core.py       → Agent definitions + Runner helpers
    - tools.py      → function_tool handlers
    - prompts.py    → system prompts per module
    - schemas.py    → Pydantic output schemas
  - modules/
    - base.py       → BaseModule ABC (instructions, input builder, metadata)
    - [module].py   → one file per command
  - output/
    - reporter.py   → save .json + .md to reports/TIMESTAMP/
    - display.py    → Rich terminal output

## Agentic Run Pattern (core.py)
```python
from agents import Agent, Runner, RunConfig

agent = Agent(
    name="[NAME]",
    instructions=system_prompt,
    tools=TOOLS,
    output_type=OutputSchema,  # or omit for plain-text final output
)

result = Runner.run_sync(
    agent,
    user_prompt,
    run_config=RunConfig(
        model=model,
        workflow_name="[NAME] workflow",
    ),
    max_turns=MAX_TURNS,
)

final_output = result.final_output
raw_items = result.new_items
next_turn_input = result.to_input_list()
```

## Tools Needed
[LIST YOUR TOOLS HERE — web_search, fetch_page, read_file, etc.]

## Commands
[name] [command1] [required_arg]    → [what it does]
[name] [command2] "query"           → [what it does]
[name] ask "question"               → synthesize across all prior runs (default: no fresh web research unless requested)
[name] journal                      → show accumulated insights

## Persona (instructions)
"You are a [specific expert type] who [specific expertise].
You think in terms of [how they frame problems].
You produce outputs that [who uses them and how]."

## Research Strategy (instructions continued)
Phase 1 — [Discovery phase name] (X-Y searches):
  "[target] [aspect1] [year]"
  "[target] [aspect2] report"
Phase 2 — [Investigation phase] (X-Y searches):
  ...
Phase 3 — [Competitive/context phase] (X-Y searches):
  ...
Phase 4 — [Opportunity/synthesis phase] (X-Y searches):
  ...
Stopping condition: "After [N] good data points covering [key angles], stop and write."

## Output Schema
{
  "module": "[name]",
  "[field1]": "[type and description]",
  "[field2]": {"nested": "structure"},
  "[field_list]": [{"item_field": "...", "item_field2": "..."}],
  "sources": ["<url>"]
}

## Memory
After each run: extract 5-8 key bullets from final output → append to [name]_journal.md
`ask` command: load journal + all .md reports → single synthesis run
```

---

## Prompt Quality Framework

### ✅ What Works

**Schema-First Style:** Lead with the output schema. The agent works backward from "what must I populate" to "what must I search for."

**Persona-First Style:** Lead with who the agent is. Expert personas produce better reasoning and more appropriate tone.

**Failure-Mode-First Style:** Tell the agent what NOT to do. Prevents the most common agent failure modes.

### ❌ What Doesn't Work

**Capability-First Style:** Telling the model what it *can* do rather than what it *should produce* leads to shallow outputs.

### Variables That Most Impact Quality

Ranked by impact on output quality:

| Variable | Low Quality | High Quality |
|----------|------------|--------------|
| **Stopping condition** | "research until done" | "stop after 15-25 data points covering [specific angles]" |
| **Schema specificity** | `"findings": [...]` | `"findings": [{"company": "...", "raised": "$Xm", "traction": "ARR or customers", "gap": "..."}]` |
| **Persona specificity** | "expert analyst" | "senior VC partner who has invested in 40+ enterprise SaaS companies" |
| **Phase structure** | "search relevant things" | "Phase 1: industry (4-6 searches). Phase 2: competitive (4-6 searches). Phase 3: investment signals (3-4 searches)" |
| **Negative constraints** | none | "never assert without citing source. never say 'significant' without a number" |
| **Output ordering** | "produce a report" | "narrative analysis FIRST (4-8 paragraphs), then structured block" |

---

## Critical Engineering Decisions

Every production agent needs these 8 engineering decisions baked in. Include this block verbatim:

### 1. Let the SDK Own the Tool Loop
```python
result = Runner.run_sync(
    agent,
    user_prompt,
    max_turns=80,
)
```
Do not re-implement a raw provider loop unless you specifically need lower-level control than the Agents SDK provides.

### 2. Use `output_type` or Structured Outputs for Reliability
```python
class Report(BaseModel):
    company: str
    verdict: str
    sources: list[str]

agent = Agent(
    name="Researcher",
    instructions="...",
    output_type=Report,
)
```

### 3. Always Save Narrative + Structured Output
- Save a markdown report with the narrative analysis first
- Save a JSON file with the parsed structured output
- If structured parsing fails, still save the narrative and any raw response text

### 4. The Synthesis vs Research Split
`ask` command should default to synthesis over accumulated reports/journal/context. Do not automatically re-run full web research unless the user asks for fresh research.

### 5. Module Abstraction
All research types extend `BaseModule(ABC)` with properties like: `name`, `display_name`, `instructions`, `build_input()`, `metadata`. One file per command.

### 6. Context Window Management
- Truncate fetched pages before returning them from tools: `content[:8000]`
- Prefer sessions / `to_input_list()` / `previous_response_id` instead of blindly resending everything
- If prompt size grows too much, trim older tool outputs or summarize them into the journal

### 7. Turn Cap + Wrap-Up Nudge
- `MAX_TURNS = 80` (hard cap)
- `SYNTHESIS_TRIGGER_TURN = 72` (inject nudge to wrap up)
- Handle `MaxTurnsExceeded` cleanly and save partial results

### 8. Use `ddgs`, not `duckduckgo-search`
```python
# requirements.txt
ddgs>=0.1.0

from ddgs import DDGS
```

---

## Technology Stack Decisions

### Agent Backbone: OpenAI Agents SDK
Choose the Agents SDK when you want native agent orchestration, tools, handoffs, sessions, tracing, and structured final outputs without building the orchestration loop yourself.

### Web Search: `ddgs` or OpenAI Hosted Web Search
Use `ddgs` when you want a fully local/custom web tool with no extra hosted dependency. Use the hosted OpenAI web search tool when you want OpenAI-managed search inside the agent runtime.

### HTTP Client: `httpx` vs. `requests`
Use `httpx` for native async support. Upgrade to Playwright if targets need JavaScript rendering.

### HTML Parsing: `beautifulsoup4` + `lxml`
Simple and fast. For text extraction only, use `trafilatura` instead.

### CLI Framework: `typer[all]`
Type annotations → auto CLI. Minimal boilerplate. Commands are plain Python functions.

### Terminal UI: `rich`
The de-facto standard. No serious alternative.

### Model Selection: `gpt-5` family by default
Use a GPT-5 family model for most agents. Use a smaller/faster model when latency or cost matters more than reasoning depth.

### Package Management: `pip` + `requirements.txt`
For CLI tools, stick with pip. Use `uv pip` for faster installs. Graduate to `poetry` when publishing to PyPI.

---

## The Single Most Important Principle

**The instructions are the product.**

The CLI, tools, runner, and output layer are all infrastructure. The instructions — specifically the phased search strategy and the output schema — are what determine whether the agent produces investment-grade output or a surface-level summary.

When an agent produces shallow output, the fix is almost never in the code. It's in the instructions: tighter search phases, more specific schema fields, stronger stopping conditions, more precise negative constraints.

Build the infrastructure once. Iterate on prompts continuously.

---

## How to Use This Document

1. **Choose your agent type** from the Quick Start table
2. **Copy the specific pattern** for that type
3. **Fill in the Universal Template** with your specifics (persona, tools, commands, schema)
4. **Add the Engineering Decisions block** — all 8 decisions, copy-paste
5. **Give the complete prompt to your code generator / coding agent** with the instruction: "Build this agent following the pattern exactly"

The prompt should produce a working CLI agent in a single shot.
