"""Tiny JSON-based translations. Add a language by dropping `<code>.json` next to this file."""

from __future__ import annotations

import json
from functools import cache
from pathlib import Path

_DIR = Path(__file__).parent


@cache
def languages() -> dict[str, str]:
    """Language code -> its own name, e.g. {"ru": "Русский"}."""
    return {p.stem: _load(p.stem).get("_name", p.stem) for p in sorted(_DIR.glob("*.json"))}


@cache
def _load(code: str) -> dict[str, str]:
    path = _DIR / f"{code}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def translator(code: str):
    """Return t(key) for `code`, falling back to English, then to the key itself."""
    primary, fallback = _load(code), _load("en")

    def t(key: str) -> str:
        return primary.get(key) or fallback.get(key) or key

    return t
