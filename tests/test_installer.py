from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "reality-compression"
INSTALLER = SKILL / "scripts" / "install.py"


class InstallerTests(unittest.TestCase):
    def run_installer(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(INSTALLER), *arguments],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_installs_for_both_runtimes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            codex_parent = root / "agents" / "skills"
            claude_parent = root / "claude" / "skills"
            result = self.run_installer(
                "--runtime",
                "all",
                "--source",
                str(SKILL),
                "--target-codex",
                str(codex_parent),
                "--target-claude",
                str(claude_parent),
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((codex_parent / "reality-compression" / "SKILL.md").is_file())
            self.assertTrue((claude_parent / "reality-compression" / "SKILL.md").is_file())

    def test_refuses_unintentional_overwrite_and_allows_force(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "skills"
            common = (
                "--runtime",
                "codex",
                "--source",
                str(SKILL),
                "--target-codex",
                str(target),
            )
            first = self.run_installer(*common)
            second = self.run_installer(*common)
            forced = self.run_installer(*common, "--force")
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("Existing installation", second.stderr)
            self.assertEqual(forced.returncode, 0, forced.stderr)

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "skills"
            result = self.run_installer(
                "--runtime",
                "codex",
                "--source",
                str(SKILL),
                "--target-codex",
                str(target),
                "--dry-run",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(target.exists())
            self.assertIn("Would install for codex", result.stdout)


if __name__ == "__main__":
    unittest.main()
