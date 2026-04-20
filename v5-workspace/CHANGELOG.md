# Changelog

All notable changes to `v5-workspace` are documented in this file.

## 2026-04-20

### Added

- **Trend Pulse product hub** under `playbooks/products/` (`index.html` + one HTML page per n8n workflow) with IO summaries, worked examples, and links into `n8n_workflows/`.
- **`scripts/generate_trend_pulse_product_pages.py`** — regenerates product HTML and `n8n_workflows/docs/v2/product-scenarios.md` from a single manifest.
- **V2 truth docs** under `docs/v2/` (`00-start-here`, operator/builder/seller, uses library, FAQ, changelog, `_templates/`).
- **V3 Annex notes** under `docs/v3/` (`00-annex.md`, `changelog-v3.md`) describing the narrative layer vs canonical V2 markdown.
- **Playbooks V2** under `playbooks/v2/` (hub + persona decks + uses catalog + `LINK_MAP.md`) — editorial dark theme, truth-linked.
- **Playbooks V3** under `playbooks/v3/` (“Archival annex” creative skin: specimen cards + Wunderkammer uses) + `LINK_MAP.md`.
- `playbooks/index.html` — sections **D**–**F** linking V2, V3, and Trend Pulse product pages + scenarios doc.
- `playbooks/` — separate HTML variants: operator (×2), sales landing (×2), hybrid (×2), plus `playbooks/index.html` as a table of contents.
- Created `v5-workspace` as the new unified workspace root.
- Added `V5_OVERVIEW.md` with operating guidance and consolidation notes.
- Added `_root-links/` structure with local snapshots for:
  - `reference/autotagger-lite`
  - `reference/current`
  - `legacy/v1-original-kb`
  - `legacy/v2-engine`
  - `legacy/v3-dev`
  - `data/root-output`
  - `docs/root-docs`

### Changed

- Consolidation mode changed from symlink-based references to fully local copied directories to make `v5-workspace` independent.
- Updated `V5_OVERVIEW.md` to explicitly reflect standalone/self-contained status.
- Updated run scripts (`autotag.sh`, `autotag_compat.sh`, `setup_autotag.sh`, `verify_installation.sh`) to avoid hardcoded absolute paths and use workspace-relative execution.
- Updated `config/autotag_config.json` paths to be portable and repo-local.
- Expanded playbook assets with additional variants and a browsable `playbooks/index.html`.

### Notes

- `v5-workspace` current size after consolidation is approximately `204M`.
- Independence was verified by replacing all external symlinks under `_root-links/`.
