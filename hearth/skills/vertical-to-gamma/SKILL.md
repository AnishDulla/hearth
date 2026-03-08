---
name: vertical-to-gamma
description: Convert vertical_research JSON outputs into concise 3-slide Gamma infographic content and create decks via Gamma Generate API v1.0. Use when asked to transform reports (full_report/opportunities/workflow/pains) into an executive summary deck with Problem -> Opportunities -> ROI structure, light citations, and reproducible payload artifacts.
---

# Vertical To Gamma

## Overview

Use this skill to convert `vertical_research/output` report folders into a concise 3-slide narrative and push it to Gamma via API.

## Workflow

1. Build payload from report data
- Run:
```bash
python skills/vertical-to-gamma/scripts/build_gamma_payload.py --vertical "home services"
```
- This writes:
  - `gamma_prompt.md`
  - `gamma_payload.json`
  - `gamma_source_map.json`

2. Create deck in Gamma
- Set API key:
```bash
export GAMMA_API_KEY="sk-gamma-..."
```
- Run:
```bash
python skills/vertical-to-gamma/scripts/create_gamma_deck.py --payload <path/to/gamma_payload.json>
```
- This writes:
  - `gamma_create_response.json`
  - `gamma_status_response.json` (when polling)
  - `gamma_deck_url.txt` (when available)
  - `run_log.md`

## Slide Contract

Always produce exactly 3 slides:

1. Current Pain Landscape
- 3-5 bullets on current workflow friction and why now.

2. Top 3 AI Opportunities
- One entry each for ranked opportunities with insertion point and buyer.

3. ROI Snapshot
- 3-5 KPI metrics and a pilot recommendation.

Use light citations (3-6 short cues total).

## Input Discovery Rules

`build_gamma_payload.py` resolves report folders in this order:

1. Explicit `--report-dir`
2. New naming style: `<vertical_slug>_<YYYYMMDD>` (and `_2`, `_3`, ...)
3. Legacy naming style: timestamped folders such as `20260306_191516_run`

Preferred source file is `full_report.json`. Fallback is merged data from `opportunities.json`, `workflow.json`, and `pains.json`.

## References

- For Gamma endpoint and supported request fields, load `references/gamma_api.md`.
