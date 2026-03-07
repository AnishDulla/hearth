---
name: openai-agent-builder
description: Design, scaffold, and refine OpenAI Agents SDK implementations and agent instruction prompts for production use. Use when asked to build a new OpenAI agent, improve an existing agent architecture, add tools/guardrails/handoffs/sessions/structured outputs/streaming, or convert requirements into concrete Agent SDK code and prompt templates.
---

# OpenAI Agent Builder

## Overview

Use this skill to turn user goals into production-oriented OpenAI agent implementations.

Load references as needed:
- `references/OPENAI_AGENTS_SDK_PATTERNS.md` for SDK architecture and implementation patterns.
- `references/OPENAI_AGENT_PROMPT_PATTERNS.md` for one-shot prompt frameworks and prompt quality guidance.

## Workflow

1. Clarify the build target
- Capture domain, outcome, runtime constraints, and expected output format.
- Confirm whether the request is greenfield build, refactor, or targeted fix.

2. Choose architecture pattern
- Use the SDK reference to choose the minimal viable pattern:
  - basic agent
  - tools
  - structured output
  - sessions/memory
  - multi-agent handoffs
  - hosted tools
  - guardrails/approvals
- Prefer the simplest pattern that satisfies requirements.

3. Define agent contract
- Write precise `instructions` with boundaries, priorities, and stop conditions.
- Define output contract early (`output_type` schema when reliability matters).
- Decide what must be persisted between turns and where.

4. Build implementation
- Implement with the Agents SDK primitives from the references.
- Keep orchestration explicit and testable.
- Separate tool code, agent config, and output schema into distinct modules when project size warrants it.

5. Validate behavior
- Run at least one happy path and one failure/edge path.
- Verify the tool loop, structured outputs, and guardrails behave as intended.
- Check for common mistakes listed in the SDK reference.

6. Harden and hand off
- Document model choice rationale.
- Note operational risks and monitoring hooks.
- Provide next steps for scaling (sessions, retries, approvals, observability).

## Prompt Construction Rules

When writing or revising agent prompts:
- Follow the prompt-pattern reference schema for the matching agent type.
- Keep instructions explicit, operational, and testable.
- Prefer constraints over stylistic guidance.
- Encode required output shape and quality bar in prompt + schema together.

## Fast Reference Navigation

Use these commands to find patterns quickly inside the references:

```bash
rg '^## ' references/OPENAI_AGENTS_SDK_PATTERNS.md
rg '^## ' references/OPENAI_AGENT_PROMPT_PATTERNS.md
rg -n 'Pattern|Guardrails|Handoffs|Structured Output|Sessions|Common Mistakes' references/OPENAI_AGENTS_SDK_PATTERNS.md
rg -n '1-Shot Prompt Schema|Prompt Quality Framework|Critical Engineering Decisions' references/OPENAI_AGENT_PROMPT_PATTERNS.md
```

## Deliverable Checklist

Before finalizing an agent build:
- Architecture choice is stated and justified.
- `instructions` are concrete and bounded.
- Tool interfaces are explicit and minimal.
- Structured output is used when parsing/reliability matters.
- Memory/session handling is intentional.
- Failure handling and retries are addressed.
- A runnable entry point and quick verification path are provided.
