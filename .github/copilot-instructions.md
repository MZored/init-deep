<!-- Derived from AGENTS.md by /init-deep. Keep in sync. -->
# init-deep

Multi-platform AI documentation generator. Python 3.11, no external deps.

## Commands

```bash
python3 scripts/build_init_deep.py       # Regenerate adapters from canonical source
python3 scripts/check_init_deep.py       # Validate sync
python3 -m unittest discover -s tests -v # Run tests
```

## Architecture

`source/init-deep/canonical.md` is the single source of truth. `tools/init_deep/renderers.py` generates platform-specific output. `scripts/build_init_deep.py` writes all artifacts to `skills/` and `adapters/`.

## Conventions

- Edit `source/init-deep/canonical.md` only; never hand-edit `skills/` or `adapters/`
- CI enforces sync: build then `git diff --exit-code`
- Pure stdlib Python, no external dependencies
- Each platform gets a dedicated `render_*()` function
- Tests read actual files, no mocks

## Pitfalls

- Gemini adapter is TOML, not Markdown
- Copilot instructions must be short; full prompt in `.github/prompts/`
- `managed_paths()` glob list must be updated when adding adapters
