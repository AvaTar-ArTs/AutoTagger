# Changelog — n8n_workflows (Trend Pulse library)

## 2026-04-20 — Product scenarios (examples)

### Added

- `docs/v2/product-scenarios.md` — per-workflow example narratives and sample inputs (anchors match workflow slugs).

### Changed

- `docs/v2/00-start-here.md`, `workflow-library-v2.md` — link to product scenarios and V5 HTML product hub.

## 2026-04-20 — Real trees in AutoTagger + session export

### Added

- `docs/SESSION_EXPORT_REAL_TREES_AND_POLICY.md` — long-form handoff: commits, rsync, verification, `.gitignore` / `.cursorignore`, dual-repo alignment.

### Changed

- `README.md` — link to the session export from the V2 documentation section.

## 2026-04-20 — V2 documentation baseline

### Added

- `docs/v2/` — operator-facing truth docs: start here, import/credentials, env matrix, Trend Pulse pattern, full workflow index, link map.
- `docs/v3/` — Annex positioning note (how creative playbooks relate without duplicating JSON).
- Root `CHANGELOG.md` (this file) for the library outside the older per-folder notes.

### Changed

- `README.md` — V2 structure section, cross-link to AutoTagger V5 playbooks (`v5-workspace/playbooks/v2` / `v3`) where relevant for go-to-market narrative.

### Notes

- JSON workflow payloads live under `free/`, `premium/`, `workflows/*`, and `imports/` as **real directories in git** in the AutoTagger repo. Optional second checkout at `~/n8n_workflows` stays aligned via git or rsync, not symlinks.
