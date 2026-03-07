# OpenAI Agents SDK Patterns — Best Practices for the OpenAI Agents SDK (Python)

A practical reference for building production-quality applications with the OpenAI Agents SDK (`openai-agents`). Covers the major SDK surfaces you actually need for agentic applications, with real code patterns rather than only hello-world examples.

---

## Setup and Initialization

```python
import os
from dotenv import load_dotenv
from agents import set_default_openai_key

load_dotenv()
set_default_openai_key(os.environ["OPENAI_API_KEY"])
```

### Install

```bash
pip install openai-agents openai python-dotenv
```

### Core imports you will actually use

```python
from agents import Agent, Runner, function_tool
```

**Model guidance (March 2026):**
```python
MODELS = {
    "best_general": "gpt-5",
    "faster_cheaper": "gpt-5-mini",
    "smallest": "gpt-5-nano",
}
```

---

## Pattern 1: Basic Agent (Single Turn)

```python
from agents import Agent, Runner

agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly and concisely.",
)

result = Runner.run_sync(
    agent,
    "What is the capital of France?",
)

print(result.final_output)
```

---

## Pattern 2: Instructions / System Behavior

```python
from agents import Agent, Runner

agent = Agent(
    name="VC Analyst",
    instructions=(
        "You are a senior VC analyst. Be specific, cite numbers, name companies. "
        "Return a structured answer with clear section headers."
    ),
)

result = Runner.run_sync(
    agent,
    "What is the AI agent market opportunity?",
)

print(result.final_output)
```

**Instructions best practices:**
- Put the persona in the first sentence: "You are a [specific expert]..."
- Define output format explicitly
- Add negative constraints: "Never claim market size without citing the source."
- Keep instructions tight enough to stay sharp

---

## Pattern 3: Multi-Turn Conversation

You have three main choices in the Agents SDK:

1. Pass `result.to_input_list()` back into the next run
2. Use a session so the SDK manages memory automatically
3. Use OpenAI server-managed continuation with `previous_response_id`

### Option A — manual carry-forward with `to_input_list()`

```python
from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="Reply clearly and briefly.",
)

result = Runner.run_sync(agent, "What's the biggest challenge in voice AI?")
result = Runner.run_sync(agent, result.to_input_list() + [{"role": "user", "content": "How does Decagon address that?"}])

print(result.final_output)
```

### Option B — session-managed memory

```python
from agents import Agent, Runner, SQLiteSession

agent = Agent(
    name="Assistant",
    instructions="Reply clearly and briefly.",
)

session = SQLiteSession("conversation_123")

print(Runner.run_sync(agent, "What's the biggest challenge in voice AI?", session=session).final_output)
print(Runner.run_sync(agent, "How does Decagon address that?", session=session).final_output)
```

**Key rule:** prefer sessions for chat-like or repeated CLI workflows. Use `to_input_list()` when you want explicit local transcript control.

---

## Pattern 4: Tools (Native Agent Loop)

The foundation of every agentic system. The SDK runs the tool loop for you.

### Define tools

```python
from agents import Agent, Runner, function_tool

@function_tool
def web_search(query: str, max_results: int = 5) -> str:
    \"\"\"Search the web for information.

    Args:
        query: The search query.
        max_results: Number of results to return.
    \"\"\"
    # Your implementation here
    return '{"results": []}'

@function_tool
def read_file(path: str) -> str:
    \"\"\"Read a local file by path.

    Args:
        path: Absolute file path.
    \"\"\"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()[:8000]
```

### Use the tools in an agent

```python
agent = Agent(
    name="Research Analyst",
    instructions="Research thoroughly, use tools when needed, then write a concise analysis.",
    tools=[web_search, read_file],
)

result = Runner.run_sync(
    agent,
    "Research the voice AI market",
    max_turns=50,
)

print(result.final_output)
```

### Why this is different from Anthropic-style raw loops

With the OpenAI Agents SDK, you usually do **not** manually:
- inspect raw tool-call blocks
- build `tool_result` messages yourself
- append assistant/user tool history by hand

The `Runner` handles tool calls, results, repeated turns, and stopping. You control it with agent config plus `max_turns`.

---

## Pattern 5: Streaming

Use when you want progressive output in chat UIs, terminals, or long-running analyses.

```python
import asyncio
from agents import Agent, Runner

agent = Agent(
    name="Analyst",
    instructions="Write a detailed market analysis.",
)

async def main():
    result = Runner.run_streamed(
        agent,
        "Analyze the AI agents market in depth.",
    )

    async for event in result.stream_events():
        print(event)

    print(result.final_output)

asyncio.run(main())
```

**When to use streaming:** chat interfaces, long analysis, visible progress. Skip it for pure back-end workflows where only the final result matters.

---

## Pattern 6: Structured Output via `output_type`

One of the most important OpenAI-native upgrades versus prompt-only JSON extraction.

```python
from pydantic import BaseModel
from agents import Agent, Runner

class CompanyVerdict(BaseModel):
    company: str
    founded: int | None = None
    raised_total: str | None = None
    verdict: str

agent = Agent(
    name="Extractor",
    instructions="Extract company information from the input.",
    output_type=CompanyVerdict,
)

result = Runner.run_sync(
    agent,
    "Analyze Stripe. Founded 2010. Verdict: buy.",
)

print(result.final_output)
print(result.final_output.verdict)
```

**When to use `output_type`:**
- default choice for reliable structured final outputs
- extraction tasks
- research reports with defined schemas
- downstream automation where typed objects are better than regex parsing

---

## Pattern 7: Sessions / Memory

The Agents SDK has first-class session memory, so you do not need to hand-roll transcript persistence for every app.

```python
from agents import Agent, Runner, SQLiteSession

agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
)

session = SQLiteSession("conversation_123")

result = Runner.run_sync(
    agent,
    "What city is the Golden Gate Bridge in?",
    session=session,
)
print(result.final_output)

result = Runner.run_sync(
    agent,
    "What state is it in?",
    session=session,
)
print(result.final_output)
```

**When to use sessions:** chat workflows, repeated CLI use, multi-step research across turns, human-in-the-loop tools.

**When not to use sessions:** when you want stateless one-shot runs or explicit full-transcript control.

---

## Pattern 8: Handoffs (Multi-Agent Orchestration)

OpenAI Agents SDK has native handoffs, so specialist-agent routing is part of the core model.

```python
from agents import Agent, Runner

refund_agent = Agent(
    name="Refund Agent",
    instructions="Handle refund questions.",
)

faq_agent = Agent(
    name="FAQ Agent",
    instructions="Handle FAQ questions.",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Route the user to the right specialist.",
    handoffs=[refund_agent, faq_agent],
)

result = Runner.run_sync(
    triage_agent,
    "I want my money back for order 123",
)

print(result.final_output)
print(result.last_agent.name)
```

**When to use handoffs:** different specialists should truly take over the conversation.

**When not to use handoffs:** when you just want one agent to call another for a subtask and return. In that case, use `agent.as_tool()` instead.

---

## Pattern 9: Agents as Tools

Sometimes you want specialization without full control transfer.

```python
from agents import Agent, Runner

math_agent = Agent(
    name="Math Agent",
    instructions="Solve quantitative questions carefully.",
)

research_agent = Agent(
    name="Research Agent",
    instructions="Research and synthesize clearly.",
    tools=[math_agent.as_tool(tool_name="solve_math")],
)

result = Runner.run_sync(
    research_agent,
    "Estimate TAM growth at 15% CAGR for 5 years starting from $2B.",
)

print(result.final_output)
```

**Use this when:** one agent should stay in charge but delegate subproblems to specialist sub-agents.

---

## Pattern 10: Hosted Tools

OpenAI Agents SDK supports hosted OpenAI-managed tools alongside your local function tools.

Common hosted tool categories include:
- web search
- file search
- code interpreter
- image generation
- hosted MCP tools

Use hosted tools when you want OpenAI to manage the runtime and tool protocol rather than implementing it yourself.

---

## Pattern 11: Guardrails and Approvals

You can add tool guardrails and require approvals for sensitive actions.

```python
from agents import Agent, Runner, function_tool

@function_tool
def delete_file(path: str) -> str:
    \"\"\"Delete a file by path.

    Args:
        path: File to delete.
    \"\"\"
    return f"Would delete {path}"

dangerous_tool = delete_file
dangerous_tool.needs_approval = True

agent = Agent(
    name="Ops Agent",
    instructions="Use tools carefully.",
    tools=[dangerous_tool],
)

result = Runner.run_sync(
    agent,
    "Delete temp.log",
)

if result.interruptions:
    state = result.to_state()
    for interruption in result.interruptions:
        state.approve(interruption)
    result = Runner.run_sync(agent, state)

print(result.final_output)
```

**When to use approvals:** file deletion, shell execution, production writes, external side effects, anything you would want a human to confirm.

---

## Pattern 12: Result Surfaces You Actually Need

The Agents SDK gives you several result surfaces; each answers a different question.

```python
result = Runner.run_sync(agent, "Research this market")

print(result.final_output)       # final answer / final structured object
print(result.to_input_list())    # replay-ready next-turn input
print(result.new_items)          # rich run items incl. tool calls/handoffs
print(result.last_agent)         # who should usually handle next turn
print(result.last_response_id)   # for Responses API continuation
print(result.raw_responses)      # low-level diagnostics
```

**Rule of thumb:**
- `final_output` → what to show the user
- `to_input_list()` → manual conversation carry-forward
- `new_items` → logs/debugging/UI
- `last_agent` → next-turn routing after handoffs

---

## Pattern 13: The Research Agent (Full Production Pattern)

A practical OpenAI-native production pattern:

```python
from dataclasses import dataclass, field
from typing import Any
from pydantic import BaseModel
from agents import Agent, Runner, function_tool

class ResearchReport(BaseModel):
    market: str
    summary: str
    sources: list[str]

@dataclass
class AgentResult:
    raw_text: str
    data: dict[str, Any] = field(default_factory=dict)
    tool_calls: int = 0

@function_tool
def web_search(query: str, max_results: int = 5) -> str:
    \"\"\"Search the web.

    Args:
        query: Search query.
        max_results: Number of results.
    \"\"\"
    return '{"results": []}'

def run_agent(system_prompt: str, user_prompt: str, model: str = "gpt-5") -> AgentResult:
    agent = Agent(
        name="Researcher",
        instructions=system_prompt,
        tools=[web_search],
        output_type=ResearchReport,
        model=model,
    )

    result = Runner.run_sync(
        agent,
        user_prompt,
        max_turns=50,
    )

    final_output = result.final_output
    raw_text = str(final_output) if final_output is not None else ""
    data = final_output.model_dump() if hasattr(final_output, "model_dump") else {}

    return AgentResult(
        raw_text=raw_text,
        data=data,
        tool_calls=sum(1 for item in result.new_items if item.__class__.__name__ == "ToolCallItem"),
    )
```

### Why this pattern is production-grade
- Native tool loop
- Typed final output
- Turn cap
- Tool calls visible in `new_items`
- Easy to add sessions, streaming, handoffs, approvals, or tracing later

---

## Pattern 14: Error Handling

```python
from agents import Agent, Runner
from openai import APIConnectionError, APIStatusError, APITimeoutError, RateLimitError

try:
    result = Runner.run_sync(agent, "Research the market", max_turns=50)

except RateLimitError as e:
    print(f"Rate limited: {e}")

except APIStatusError as e:
    print(f"API status error: {e.status_code} - {e}")

except APIConnectionError:
    print("Connection failed")

except APITimeoutError:
    print("Request timed out")

except Exception as e:
    print(f"Unexpected error: {e}")
```

**Common runtime issues:**
- hitting `max_turns` because instructions never converge
- oversized tool outputs because fetched pages are not truncated
- malformed local tool code
- approval interruptions not being resumed
- session strategy conflicts (for example mixing sessions with `previous_response_id` incorrectly)

---

## Model Selection Decision Tree

```text
What are you building?
│
├─ Interactive chat / real-time response needed?
│   └─ gpt-5-mini
│
├─ Agentic loop with research and tools?
│   └─ gpt-5
│
├─ Cost-sensitive extraction / classification?
│   └─ gpt-5-mini or gpt-5-nano
│
├─ Multi-agent orchestration with handoffs and approvals?
│   └─ gpt-5
│
└─ Very lightweight utility agent?
    └─ gpt-5-nano
```

---

## Common Mistakes and Fixes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Re-implementing the provider tool loop manually | Extra complexity, more bugs, worse state handling | Let `Runner` manage the loop |
| Not setting `max_turns` | Run can wander too long | Set an explicit turn cap |
| Returning giant tool outputs | Context bloat, slower runs, higher cost | Truncate tool output to ~8K chars |
| Using prompt-only JSON parsing when you need typed data | Fragile downstream code | Use `output_type` with Pydantic |
| Using handoffs when you only need subtask delegation | Unnecessary control transfer | Use `agent.as_tool()` |
| Forgetting to resume approval interruptions | Agent appears stuck | Call `to_state()`, approve/reject, then resume |
| Mixing sessions and server-managed continuation casually | Confusing state | Pick one conversation-memory strategy per workflow |
| Treating `new_items` like final user-visible content | Messy output | Show `final_output`, inspect `new_items` for diagnostics |

---

## Quick Reference Card

```python
from agents import Agent, Runner, function_tool

@function_tool
def search(query: str) -> str:
    \"\"\"Search the web.

    Args:
        query: Search query.
    \"\"\"
    return "results"

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    tools=[search],
)

# one-shot
result = Runner.run_sync(agent, "Hello")
print(result.final_output)

# with tools
result = Runner.run_sync(agent, "Search for voice AI news", max_turns=10)
print(result.final_output)

# structured output
# agent = Agent(name="Extractor", instructions="...", output_type=MySchema)

# session memory
# session = SQLiteSession("conversation_123")
# result = Runner.run_sync(agent, "Hello", session=session)

# next-turn carry-forward
# next_input = result.to_input_list() + [{"role": "user", "content": "Continue"}]
# result = Runner.run_sync(agent, next_input)
```
