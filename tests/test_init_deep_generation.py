from pathlib import Path
import unittest

from tools.init_deep.source import load_canonical_source
from tools.init_deep.renderers import render_distribution

ROOT = Path(__file__).resolve().parents[1]


class CanonicalSourceTests(unittest.TestCase):
    def test_canonical_source_declares_new_modes(self) -> None:
        source = load_canonical_source(ROOT / "source/init-deep/canonical.md")
        self.assertIn("--dry-run", source.flags)
        self.assertIn("--doctor", source.flags)
        self.assertIn("--sync-check", source.flags)

    def test_canonical_source_preserves_current_workflow_depth(self) -> None:
        source = load_canonical_source(ROOT / "source/init-deep/canonical.md")
        self.assertIn("## Phase 1: Discovery + Analysis (Concurrent)", source.raw)
        self.assertIn("Track ALL phases with TodoWrite.", source.raw)

    def test_distribution_declares_platform_native_outputs(self) -> None:
        source = load_canonical_source(ROOT / "source/init-deep/canonical.md")
        outputs = render_distribution(source)
        self.assertIn("skills/init-deep/SKILL.md", outputs)
        self.assertTrue(outputs["skills/init-deep/SKILL.md"].startswith("---\n"))
        self.assertIn("disable-model-invocation: true", outputs["skills/init-deep/SKILL.md"])
        self.assertIn("adapters/cursor/commands/init-deep.md", outputs)
        self.assertIn("adapters/gemini/commands/init-deep.toml", outputs)
        self.assertIn("adapters/copilot/prompts/init-deep.prompt.md", outputs)
        self.assertIn("adapters/windsurf/init-deep.md", outputs)
        self.assertIn("adapters/cline/init-deep.md", outputs)


class GeneratedArtifactTests(unittest.TestCase):
    def test_rendered_artifacts_match_checked_in_files(self) -> None:
        source = load_canonical_source(ROOT / "source/init-deep/canonical.md")
        outputs = render_distribution(source)
        for relative_path in (
            "skills/init-deep/SKILL.md",
            "adapters/cursor.mdc",
            "adapters/cursor/commands/init-deep.md",
            "adapters/copilot.md",
            "adapters/windsurf/init-deep.md",
            "adapters/cline/init-deep.md",
        ):
            actual = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertEqual(outputs[relative_path], actual, relative_path)

    def test_cursor_rule_is_not_auto_attached(self) -> None:
        source = load_canonical_source(ROOT / "source/init-deep/canonical.md")
        outputs = render_distribution(source)
        rule = outputs["adapters/cursor.mdc"]
        self.assertIn("alwaysApply: false", rule)
        self.assertNotIn('"**/*"', rule)


if __name__ == "__main__":
    unittest.main()
