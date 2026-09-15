from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_skill_zip.py"
SPEC = importlib.util.spec_from_file_location("build_skill_zip", BUILDER)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class SkillArchiveTests(unittest.TestCase):
    def test_committed_download_is_complete_and_current(self) -> None:
        result = subprocess.run([sys.executable, str(BUILDER), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(ROOT / "skills.zip") as archive:
            names = archive.namelist()
            self.assertEqual({Path(name).parts[0] for name in names}, {"john-tuld"})
            self.assertEqual([name for name in names if Path(name).name.lower() == "skill.md"], ["john-tuld/SKILL.md"])
            for name in ("LICENSE", "VERSION", "references/gates.md", "references/comic-protocol.md", "agents/openai.yaml"):
                self.assertIn(f"john-tuld/{name}", names)
            self.assertNotIn("..", {part for name in names for part in Path(name).parts})

    def test_check_rejects_stale_download_without_overwriting_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skills.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("john-tuld/SKILL.md", "outdated instructions")
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(BUILDER), "--output", str(path), "--check"], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("stale", result.stderr)
            self.assertEqual(path.read_bytes(), before)

    def test_local_junk_is_excluded_and_symlinks_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "john-tuld"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: john-tuld\n---\n")
            (root / "LICENSE").write_text("MIT")
            (root / "VERSION").write_text("test")
            (skill / "__pycache__").mkdir()
            (skill / "__pycache__" / "cache.pyc").write_bytes(b"cache")
            (skill / ".DS_Store").write_bytes(b"metadata")
            (skill / "old.zip").write_bytes(b"archive")
            files = builder.package_files(root)
            self.assertEqual(set(files), {"john-tuld/SKILL.md", "john-tuld/LICENSE", "john-tuld/VERSION"})
            (skill / "linked.txt").symlink_to(root / "LICENSE")
            with self.assertRaisesRegex(ValueError, "symlinks"):
                builder.package_files(root)


if __name__ == "__main__":
    unittest.main()
