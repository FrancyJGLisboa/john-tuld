#!/usr/bin/env python3
"""Install Reality Compression from this checkout or directly from GitHub."""

from __future__ import annotations

import argparse
import io
import os
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


SKILL_NAME = "reality-compression"
ARCHIVE_URL = (
    "https://github.com/FrancyJGLisboa/reality-compression/"
    "archive/refs/heads/main.zip"
)
MAX_ARCHIVE_BYTES = 20 * 1024 * 1024
REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/gates.md",
    "references/comic-protocol.md",
    "scripts/validate_contract.py",
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--runtime",
        choices=("all", "codex", "claude"),
        default="all",
        help="Runtime to install for. Defaults to both local runtimes.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        help="Local skill directory. Primarily useful for development and tests.",
    )
    parser.add_argument(
        "--target-codex",
        type=Path,
        help="Override the Codex skills parent directory.",
    )
    parser.add_argument(
        "--target-claude",
        type=Path,
        help="Override the Claude skills parent directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installation after staging and validation.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and show destinations without writing them.",
    )
    return parser.parse_args(argv)


def validate_source(source: Path) -> None:
    missing = [relative for relative in REQUIRED_FILES if not (source / relative).is_file()]
    if missing:
        raise RuntimeError("Invalid skill package; missing: " + ", ".join(missing))

    frontmatter = (source / "SKILL.md").read_text(encoding="utf-8")[:2048]
    if "name: reality-compression" not in frontmatter:
        raise RuntimeError("Invalid SKILL.md: expected name: reality-compression")


def local_source() -> Path | None:
    try:
        script_path = Path(__file__).resolve()
    except NameError:
        return None
    candidate = script_path.parents[1]
    return candidate if (candidate / "SKILL.md").is_file() else None


def download_source(work_dir: Path) -> Path:
    request = urllib.request.Request(
        ARCHIVE_URL,
        headers={"User-Agent": "reality-compression-installer/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read(MAX_ARCHIVE_BYTES + 1)
    if len(payload) > MAX_ARCHIVE_BYTES:
        raise RuntimeError("Downloaded archive exceeds the 20 MiB safety limit")

    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        marker_suffix = f"/skills/{SKILL_NAME}/SKILL.md"
        markers = [name for name in archive.namelist() if name.endswith(marker_suffix)]
        if len(markers) != 1:
            raise RuntimeError("Archive does not contain one canonical Reality Compression skill")

        prefix = markers[0][: -len("SKILL.md")]
        source = work_dir / SKILL_NAME
        source.mkdir()
        for member in archive.infolist():
            if member.is_dir() or not member.filename.startswith(prefix):
                continue
            relative_text = member.filename[len(prefix) :]
            relative = Path(relative_text)
            if not relative_text or relative.is_absolute() or ".." in relative.parts:
                raise RuntimeError(f"Unsafe archive member: {member.filename}")
            destination = source / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as incoming, destination.open("wb") as outgoing:
                shutil.copyfileobj(incoming, outgoing)
            if member.external_attr >> 16 & 0o111:
                destination.chmod(destination.stat().st_mode | 0o755)
    return source


def destinations(args: argparse.Namespace) -> list[tuple[str, Path]]:
    selected = ("codex", "claude") if args.runtime == "all" else (args.runtime,)
    defaults = {
        "codex": Path.home() / ".agents" / "skills",
        "claude": Path.home() / ".claude" / "skills",
    }
    overrides = {
        "codex": args.target_codex,
        "claude": args.target_claude,
    }
    return [
        (runtime, (overrides[runtime] or defaults[runtime]).expanduser().resolve())
        for runtime in selected
    ]


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def install_one(source: Path, parent: Path, force: bool) -> Path:
    parent.mkdir(parents=True, exist_ok=True)
    destination = parent / SKILL_NAME
    stage_root = Path(tempfile.mkdtemp(prefix=f".{SKILL_NAME}-stage-", dir=parent))
    staged = stage_root / SKILL_NAME
    backup = parent / f".{SKILL_NAME}-backup-{os.getpid()}"

    try:
        shutil.copytree(
            source,
            staged,
            ignore=shutil.ignore_patterns(".git", "*.zip", "__pycache__", "*.pyc"),
        )
        validate_source(staged)

        had_existing = destination.exists() or destination.is_symlink()
        if had_existing:
            if not force:
                raise RuntimeError(f"Destination exists: {destination}. Re-run with --force to update it.")
            if backup.exists() or backup.is_symlink():
                remove_path(backup)
            os.replace(destination, backup)

        try:
            os.replace(staged, destination)
        except Exception:
            if had_existing and backup.exists():
                os.replace(backup, destination)
            raise

        if backup.exists() or backup.is_symlink():
            remove_path(backup)
        return destination
    finally:
        if stage_root.exists():
            shutil.rmtree(stage_root)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    temporary_download = None
    try:
        if args.source:
            source = args.source.expanduser().resolve()
        else:
            source = local_source()
            if source is None:
                temporary_download = tempfile.TemporaryDirectory(prefix="reality-compression-download-")
                source = download_source(Path(temporary_download.name))

        validate_source(source)
        targets = destinations(args)

        conflicts = [
            parent / SKILL_NAME
            for _, parent in targets
            if (parent / SKILL_NAME).exists() or (parent / SKILL_NAME).is_symlink()
        ]
        if conflicts and not args.force:
            rendered = ", ".join(str(path) for path in conflicts)
            raise RuntimeError(f"Existing installation(s): {rendered}. Re-run with --force to update.")

        if args.dry_run:
            for runtime, parent in targets:
                print(f"Would install for {runtime}: {parent / SKILL_NAME}")
            return 0

        for runtime, parent in targets:
            installed = install_one(source, parent, args.force)
            print(f"Installed for {runtime}: {installed}")
        print("Invoke with $reality-compression in Codex or /reality-compression in Claude Code.")
        return 0
    except (OSError, RuntimeError, urllib.error.URLError, zipfile.BadZipFile) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1
    finally:
        if temporary_download is not None:
            temporary_download.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
