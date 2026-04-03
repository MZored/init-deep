from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepoMetadataTests(unittest.TestCase):
    def test_gitattributes_only_marks_real_generated_outputs(self) -> None:
        text = (ROOT / ".gitattributes").read_text(encoding="utf-8")
        self.assertNotIn("adapters/* linguist-generated=true", text)
        self.assertIn("skills/init-deep/SKILL.md linguist-generated=true", text)
        self.assertIn("adapters/cursor.mdc linguist-generated=true", text)
        self.assertIn("adapters/cursor/commands/init-deep.md linguist-generated=true", text)
        self.assertIn("adapters/gemini/commands/init-deep.toml linguist-generated=true", text)
        self.assertIn("adapters/copilot/prompts/init-deep.prompt.md linguist-generated=true", text)
        self.assertIn("adapters/windsurf/init-deep.md linguist-generated=true", text)
        self.assertIn("adapters/cline/init-deep.md linguist-generated=true", text)

    def test_plugin_metadata_mentions_generated_platform_native_outputs(self) -> None:
        plugin = (ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        marketplace = (ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
        self.assertIn("platform-native", plugin)
        self.assertIn("platform-native", marketplace)
        self.assertIn("Windsurf", plugin)
        self.assertIn("Cline", plugin)
        self.assertIn("7 AI coding platforms", marketplace)


if __name__ == "__main__":
    unittest.main()
