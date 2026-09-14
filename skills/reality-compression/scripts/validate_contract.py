#!/usr/bin/env python3
"""Check the package's structural and behavioral contract markers."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/gates.md",
    "references/comic-protocol.md",
    "references/examples.md",
    "references/runtime-installation.md",
)

REQUIRED_SKILL_MARKERS = (
    "name: reality-compression",
    "G1 Reality",
    "G10 Visual parity",
    "COMPLETE",
    "RENDER_PENDING",
    "BLOCKED",
    "ChatGPT with ImageGen",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    root = parser.parse_args().root.resolve()
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing file: {relative}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        content = skill_path.read_text(encoding="utf-8")
        for marker in REQUIRED_SKILL_MARKERS:
            if marker not in content:
                errors.append(f"SKILL.md missing contract marker: {marker}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Reality Compression skill contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
