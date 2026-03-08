# Gamma API Reference (for this skill)

This skill uses Gamma Generate API v1.0.

## Authentication

Send API key in header:
- `X-API-KEY: <GAMMA_API_KEY>`

## Base URL

- `https://public-api.gamma.app/v1.0`

## Endpoints used

1. Create generation
- `POST /generations`
- Required body fields:
  - `inputText` (string)
  - `textMode` (string)
- Useful body fields:
  - `format` (use `presentation`)
  - `cardSplit`
  - `textOptions`
  - `additionalInstructions`
  - `themeId`
  - `folderIds`

2. Check status
- `GET /generations/{generationId}`

## Typical values used by this skill

- `format: "presentation"`
- `textMode: "preserve"` (send pre-structured 3-slide content)
- `cardSplit: "inputTextBreaks"` (split cards on explicit separators)

## Notes

- `POST /generations` returns generation metadata including `generationId` and status.
- Poll `GET /generations/{generationId}` until terminal status.
- Save raw API responses to disk for debugging and reproducibility.
