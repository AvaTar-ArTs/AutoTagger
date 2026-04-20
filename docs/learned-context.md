# Learned Context for AutoTagger Workspace

## Terminology we've established
- **AutoTag**: Intelligent 3-phase automation tool tagging & categorization system for AVATARARTS (rapid scan → intelligent organization → advanced intelligence with business value prediction)
- **Serena**: Oraios AI's MCP-powered coding agent with LSP-based symbolic tools (`find_symbol`, `get_symbols_overview`, `replace_symbol_body`, etc.), memories, modes, and project indexing
- **v4-workspace**: Current production implementation of AutoTag (with CSV export, auto-open, compatibility layers)

## Decisions we've made
- Use `v4-workspace/` as primary active directory for AutoTag development and usage
- Serena project "AutoTagger" is indexed with Python + Bash LSP support
- Serena MCP is set up for both `claude-code` (user scope) and `codex`
- Hooks and reminders recommended for Claude Code / Cursor to combat agent drift and ensure optimal use of symbolic tools
- Always run `./verify_installation.sh` after structural changes

## Patterns that work
- `serena setup <client>` for quick MCP registration
- `./autotag.sh <target_dir> [name]` for full analysis with CSV output
- Use Serena's symbolic tools (`replace_symbol_body`, `find_referencing_symbols`, etc.) instead of raw grep/read/edit when possible
- Maintain `docs/learned-context.md` for persistent decisions and terminology

## Open / to revisit
- Add recommended Serena hooks to `.claude/settings.json` for Claude Code (remind, activate, auto-approve, cleanup)
- Consider enhancing Phase 2/3 with more sophisticated LLM-based categorization (currently extension-based)
- Explore integration between AutoTag CSV outputs and Serena memories

Last updated: 2026-04-12
