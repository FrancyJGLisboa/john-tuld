#!/usr/bin/env python3
"""Build or verify the portable, single-skill skills.zip download."""

from __future__ import annotations

import argparse
import io
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "john-tuld"
IGNORED_PARTS = {"__pycache__", ".DS_Store", ".git"}


def package_files(root: Path) -> dict[str, bytes]:
    source = root / "skills" / SKILL_NAME
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Missing canonical skill: {source / 'SKILL.md'}")
    files = {}
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if IGNORED_PARTS.intersection(relative.parts) or path.suffix in {".pyc", ".pyo", ".zip"}:
            continue
        if path.is_symlink():
            raise ValueError(f"Skill archives cannot contain symlinks: {relative}")
        if path.is_file():
            files[f"{SKILL_NAME}/{relative.as_posix()}"] = path.read_bytes()
    for name in ("LICENSE", "VERSION"):
        files[f"{SKILL_NAME}/{name}"] = (root / name).read_bytes()
    manifests = [name for name in files if Path(name).name.lower() == "skill.md"]
    if manifests != [f"{SKILL_NAME}/SKILL.md"]:
        raise ValueError("Expected exactly one SKILL.md at the top of the skill folder")
    return files


def build_archive(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, contents in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, contents)
    return buffer.getvalue()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "skills.zip")
    parser.add_argument("--check", action="store_true", help="Fail if the ZIP is missing, damaged, or stale; write nothing.")
    args = parser.parse_args(argv)
    try:
        expected = package_files(ROOT)
        if args.check:
            with zipfile.ZipFile(args.output) as archive:
                names = archive.namelist()
                actual = {name: archive.read(name) for name in names}
                if len(names) != len(actual) or actual != expected:
                    raise ValueError("skills.zip is stale; run python3 scripts/build_skill_zip.py")
            print(f"Skill ZIP matches source ({len(expected)} files): PASS")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(build_archive(expected))
            print(f"Built {args.output} ({len(expected)} files, {args.output.stat().st_size} bytes)")
        return 0
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError) as error:
        print(f"Skill ZIP failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
