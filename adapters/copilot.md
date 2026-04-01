# /init-deep — Deep Project Initialization

Analyze codebase deeply. Generate documentation that works across 7 AI coding agents.

## Generated Files

| File | Read by | Purpose |
|------|---------|---------|
| `AGENTS.md` | OpenAI Codex | Universal agent instructions (canonical) |
| `CLAUDE.md` | Claude Code | Claude context, derived from AGENTS.md |
| `GEMINI.md` | Google Gemini CLI | Gemini context, derived from AGENTS.md |
| `.github/copilot-instructions.md` | GitHub Copilot | Copilot-specific context |
| `.windsurfrules` | Windsurf | Windsurf context (flat file) |
| `.clinerules` | Cline | Cline context (flat file) |
| `.claude/rules/*.md` | Claude Code | Scoped module docs with `paths:` frontmatter |
| `.cursor/rules/*.mdc` | Cursor | Scoped module docs with `globs:` frontmatter |

**Key principle:** `AGENTS.md` is the canonical source. All other files are derived from it.

## Usage

```
/init-deep                      # Update existing + create new where warranted
/init-deep --create-new         # Remove all -> regenerate from scratch
/init-deep --max-depth=2        # Limit directory depth (default: 3)
/init-deep --skip-cursor        # Skip .cursor/rules/ generation
/init-deep --skip-gemini        # Skip GEMINI.md generation
/init-deep --skip-copilot       # Skip .github/copilot-instructions.md
/init-deep --skip-windsurf      # Skip .windsurfrules
/init-deep --skip-cline         # Skip .clinerules
/init-deep --only=claude,codex  # Generate only specified formats
```

## Workflow

**Phase 1: Discovery** — Concurrent analysis of project structure, entry points, conventions, anti-patterns, build/CI, and test patterns. Scales dynamically based on project size.

**Phase 2: Scoring** — Each directory scored on file count, code ratio, module boundary, large files, distinct domain, and unique conventions. Score >12 = scoped docs generated.

**Phase 3: Generate** — Root files first (AGENTS.md canonical, others derived), then scoped files for high-scoring directories. Existing files updated, new files created.

**Phase 4: Review** — Cross-file sync verification, deduplication, trim to size limits, verify commands work. Final report lists all generated files.

## Root File Content

Root AGENTS.md/CLAUDE.md/GEMINI.md follow this structure (50-150 lines each):
- Overview (project + tech stack)
- Setup (install commands)
- Commands (dev/test/lint/build/deploy)
- Architecture (data flow, structure tree, key files)
- Conventions (project-specific deviations only)
- Known Pitfalls (non-obvious gotchas)

## Scoped File Rules

- 20-60 lines max each
- Never repeat content from root docs
- Only include sections with actual content
- Focus on what's unique to the module

## Keeping Files in Sync

AGENTS.md is the canonical source. Run `/init-deep` again after editing it to update all derived files.
