from __future__ import annotations

from textwrap import dedent

from .source import CanonicalSource


def _body(source: CanonicalSource) -> str:
    return source.raw.rstrip() + "\n"


def render_skill(source: CanonicalSource) -> str:
    return (
        "---\n"
        "name: init-deep\n"
        "description: Deeply analyze a codebase and generate multi-agent project documentation (AGENTS.md + CLAUDE.md + GEMINI.md + scoped docs). Only invoke when user explicitly types /init-deep.\n"
        'argument-hint: "[--create-new] [--max-depth=N] [--only=claude,codex] [--skip-cursor] [--dry-run] [--doctor] [--sync-check]"\n'
        "disable-model-invocation: true\n"
        "---\n\n"
        + _body(source)
    )


def render_cursor_rule() -> str:
    return dedent(
        """\
        ---
        description: "Offer init-deep only when the user explicitly asks to generate or refresh agent documentation."
        alwaysApply: false
        ---

        # init-deep helper

        - Offer `/init-deep` when the user explicitly asks for a deep documentation pass.
        - The full workflow lives in `.cursor/commands/init-deep.md`.
        - Do not auto-attach the full init-deep workflow to unrelated requests.
        """
    )


def render_cursor_command(source: CanonicalSource) -> str:
    return (
        "# /init-deep\n\n"
        "Use this command only when the user explicitly asks to initialize or refresh project agent documentation.\n\n"
        + _body(source)
    )


def render_copilot_instructions() -> str:
    return dedent(
        """\
        # init-deep repository guidance

        - Keep `.github/copilot-instructions.md` short and repository-wide.
        - Use `.github/prompts/init-deep.prompt.md` for the full init-deep workflow.
        - Treat generated `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` files as outputs, not hand-maintained sources.
        """
    )


def render_windsurf_output(source: CanonicalSource) -> str:
    return _body(source)


def render_cline_output(source: CanonicalSource) -> str:
    return _body(source)


def render_distribution(source: CanonicalSource) -> dict[str, str]:
    return {
        "skills/init-deep/SKILL.md": render_skill(source),
        "adapters/cursor.mdc": render_cursor_rule(),
        "adapters/cursor/commands/init-deep.md": render_cursor_command(source),
        "adapters/copilot.md": render_copilot_instructions(),
        "adapters/gemini/commands/init-deep.toml": 'description = "init-deep"\n\nprompt = """\n' + _body(source) + '"""\n',
        "adapters/copilot/prompts/init-deep.prompt.md": "# init-deep\n\n" + _body(source),
        "adapters/windsurf/init-deep.md": render_windsurf_output(source),
        "adapters/cline/init-deep.md": render_cline_output(source),
    }
