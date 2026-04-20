# Changelog — n8n_workflows (Trend Pulse library)

## 2026-04-20 — V2 documentation baseline

### Added

- `docs/v2/` — operator-facing truth docs: start here, import/credentials, env matrix, Trend Pulse pattern, full workflow index, link map.
- Root `CHANGELOG.md` (this file) for the library outside the older per-folder notes.

### Changed

- `README.md` — V2 structure section, cross-link to AutoTagger V5 playbooks (`v5-workspace/playbooks/v2` / `v3`) where relevant for go-to-market narrative.

### Notes

- JSON workflow payloads remain under `free/`, `premium/`, and `workflows/*` (local or symlinked to `~/n8n_workflows` depending on your setup). **V2 docs describe them; they are not duplicated here in git** when those directories are ignored or symlinked.
