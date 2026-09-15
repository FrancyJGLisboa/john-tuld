#!/usr/bin/env python3
"""Validate the cross-runtime plugin package without external dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
SKILL = ROOT / "skills" / "john-tuld"


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Invalid JSON at {relative}: {error}") from error


def main() -> int:
    errors: list[str] = []

    if not (SKILL / "SKILL.md").is_file():
        errors.append("missing canonical skill: skills/john-tuld/SKILL.md")

    for relative in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        try:
            manifest = load_json(relative)
        except RuntimeError as error:
            errors.append(str(error))
            continue
        if manifest.get("name") != "john-tuld":
            errors.append(f"{relative}: name must be john-tuld")
        if manifest.get("version") != VERSION:
            errors.append(f"{relative}: version must match VERSION ({VERSION})")

    try:
        marketplace = load_json(".claude-plugin/marketplace.json")
    except RuntimeError as error:
        errors.append(str(error))
    else:
        entries = marketplace.get("plugins", [])
        if len(entries) != 1 or entries[0].get("name") != "john-tuld":
            errors.append("Claude marketplace must expose exactly john-tuld")
        elif entries[0].get("version") != VERSION:
            errors.append("Claude marketplace version must match VERSION")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Cross-runtime package {VERSION}: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
