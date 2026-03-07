from __future__ import annotations

import json
from pathlib import Path

import httpx
from agents import function_tool
from bs4 import BeautifulSoup
from ddgs import DDGS

MAX_TOOL_CHARS = 9000
DEFAULT_TIMEOUT = 20.0


class SearchProvider:
    def search(self, query: str, max_results: int = 8) -> list[dict[str, str]]:
        with DDGS() as ddgs:
            rows = ddgs.text(query, max_results=max_results)
            results: list[dict[str, str]] = []
            for row in rows:
                results.append(
                    {
                        "title": str(row.get("title", "")).strip(),
                        "url": str(row.get("href", "")).strip(),
                        "snippet": str(row.get("body", "")).strip(),
                    }
                )
            return results


_provider = SearchProvider()


def _truncate(text: str, max_chars: int = MAX_TOOL_CHARS) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n[truncated for context-window safety]"


@function_tool
def web_search(query: str, max_results: int = 8) -> str:
    """Search the web for public sources.

    Args:
        query: Search query string.
        max_results: Maximum returned search results.
    """
    max_results = max(1, min(max_results, 15))
    results = _provider.search(query=query, max_results=max_results)
    payload = json.dumps({"query": query, "results": results}, indent=2)
    return _truncate(payload)


@function_tool
def fetch_page(url: str, max_chars: int = MAX_TOOL_CHARS) -> str:
    """Fetch and clean a webpage body.

    Args:
        url: Public URL.
        max_chars: Maximum returned chars.
    """
    try:
        with httpx.Client(timeout=DEFAULT_TIMEOUT, follow_redirects=True) as client:
            response = client.get(url, headers={"User-Agent": "vertical-research/1.0"})
            response.raise_for_status()
            content_type = response.headers.get("content-type", "")
            if "text/html" not in content_type and "application/xhtml+xml" not in content_type:
                return _truncate(response.text, max_chars=max_chars)

            soup = BeautifulSoup(response.text, "lxml")
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()
            text = "\n".join(line.strip() for line in soup.get_text("\n").splitlines() if line.strip())
            return _truncate(text, max_chars=max_chars)
    except Exception as exc:  # noqa: BLE001
        return f"fetch_page error for {url}: {exc}"


@function_tool
def read_file(path: str, max_chars: int = MAX_TOOL_CHARS) -> str:
    """Read a local file.

    Args:
        path: Relative or absolute path.
        max_chars: Maximum returned chars.
    """
    try:
        p = Path(path).expanduser().resolve()
        if not p.exists():
            return f"read_file error: file does not exist: {p}"
        if p.is_dir():
            return f"read_file error: path is a directory: {p}"
        data = p.read_text(encoding="utf-8", errors="ignore")
        return _truncate(data, max_chars=max_chars)
    except Exception as exc:  # noqa: BLE001
        return f"read_file error for {path}: {exc}"
