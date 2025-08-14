from __future__ import annotations

from typing import Iterable, List


def is_exit(text: str) -> bool:
    lowered = text.strip().lower()
    return lowered in {"exit", "quit", ":q", "bye"}


def format_sources(sources: Iterable[dict]) -> str:
    formatted: List[str] = []
    for idx, s in enumerate(sources, start=1):
        src = s.get("source", "unknown")
        page = s.get("page")
        page_txt = f" p.{page}" if page is not None else ""
        formatted.append(f"[{idx}] {src}{page_txt}")
    return "\n".join(formatted)


