# Changelog — n8n_workflows (Trend Pulse library)

## 2026-04-20 — V2 documentation baseline

### Added

- `docs/v2/` — operator-facing truth docs: start here, import/credentials, env matrix, Trend Pulse pattern, full workflow index, link map.
- `docs/v3/` — Annex positioning note (how creative playbooks relate without duplicating JSON).
- Root `CHANGELOG.md` (this file) for the library outside the older per-folder notes.

### Changed

- `README.md` — V2 structure section, cross-link to AutoTagger V5 playbooks (`v5-workspace/playbooks/v2` / `v3`) where relevant for go-to-market narrative.

### Notes

- JSON workflow payloads live under `free/`, `premium/`, `workflows/*`, and `imports/` as **real directories in git** in the AutoTagger repo. Optional second checkout at `~/n8n_workflows` stays aligned via git or rsync, not symlinks.
