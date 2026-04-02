from .source import CanonicalSource


def render_skill(source: CanonicalSource) -> str:
    body = source.raw.rstrip() + "\n"
    return (
        "---\n"
        "name: init-deep\n"
        "description: Deeply analyze a codebase and generate multi-agent project documentation (AGENTS.md + CLAUDE.md + GEMINI.md + scoped docs). Only invoke when user explicitly types /init-deep.\n"
        'argument-hint: "[--create-new] [--max-depth=N] [--only=claude,codex] [--skip-cursor] [--dry-run] [--doctor] [--sync-check]"\n'
        "disable-model-invocation: true\n"
        "---\n\n"
        + body
    )


def render_distribution(source: CanonicalSource) -> dict[str, str]:
    body = source.raw.rstrip() + "\n"
    return {
        "skills/init-deep/SKILL.md": render_skill(source),
        "adapters/cursor/commands/init-deep.md": "# /init-deep\n\n" + body,
        "adapters/gemini/commands/init-deep.toml": 'description = "init-deep"\n\nprompt = """\n' + body + '"""\n',
        "adapters/copilot/prompts/init-deep.prompt.md": "# init-deep\n\n" + body,
        "adapters/windsurf/init-deep.md": body,
        "adapters/cline/init-deep.md": body,
    }
