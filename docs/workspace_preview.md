# AutoTagger Workspace Preview

This is a quick, high-signal preview of the main workspace areas:
`autotagger-lite`, `current`, `docs`, `v6`, `output`, `v1-original-kb`, `v2-engine`, `v3-dev`, `v4-workspace`.

## At a glance

- `autotagger-lite`: `16K`, `2 files` - minimal lite variant (`README`, `scan.py`)
- `current`: `16K`, `3 files` - compact active script entrypoint area
- `docs`: lightweight central docs (`learned-context`, `superpowers`, previews)
- `v6`: SaaS track — overview, strategy, roadmap, landing HTML (versioned at repo root)
- `output`: `151M`, `127 files` - generated artifacts and exports (largest data payload)
- `v1-original-kb`: `11M`, `38 files` - original KB generation
- `v2-engine`: `15M`, `81 files` - expanded engine with backups
- `v3-dev`: `7M`, `38 files` - dev iteration snapshot
- `v4-workspace`: `21M`, `527 files` - current full workspace (scripts/tools/data/output/venv)

## Suggested organization buckets

- **Active runtime/workspace:** `v4-workspace`, `current`
- **Reference implementation:** `autotagger-lite`
- **Documentation:** `docs`, **`v6/`** (SaaS positioning + MVP notes)
- **Generated outputs:** `output`, `v4-workspace/output`
- **Legacy versions / historical KB snapshots:** `v1-original-kb`, `v2-engine`, `v3-dev`

## Directory preview details

### `autotagger-lite`

- Main contents: `README.md`, `scan.py`
- File types: `.md(1)`, `.py(1)`
- Notes: ultra-small starter/portable variant.

### `current`

- Main contents: `autotagger.py`, `init.sh`, `main.py`
- File types: `.py(2)`, `.sh(1)`
- Notes: small active script set, likely quick-run workflow.

### `docs`

- Main contents: `learned-context.md`, `workspace_preview.md`, `superpowers/`.
- Notes: project-wide specs/plans; not the V6 SaaS bundle (see **`v6/`**).

### `v6`

- Main contents: `README.md`, `V6_SAAS_OVERVIEW.md`, `saas/*.md`, `saas_landing_v1.html`.
- Notes: **canonical tracked** SaaS track. Heavy experiments may still live in gitignored `v6-workspace/`.

### `output`

- Size/profile: `151M`, `127 files`
- Top file types: `.json(44)`, `.csv(31)`, `.md(28)`, `.html(23)`, `.db(1)`
- Largest files:
  - `autotagger.db` (`127.79 MB`)
  - `documents_autotag_20260121_040637.csv` (`11.96 MB`)
  - `all_scan_20260208_204731.csv` (`3.08 MB`)
  - `all_scan_20260208_204919.csv` (`3.08 MB`)
- Notes: primary artifact accumulation zone; best archive/retention target.

### `v1-original-kb`

- Size/profile: `11M`, `38 files`
- Top file types: `.md(15)`, `.py(14)`, `.sh(6)`, `.csv(2)`, `.db(1)`
- Largest files:
  - `test_relations.csv` (`6.04 MB`)
  - `knowledge_base.db` (`4.25 MB`)
- Notes: first-generation KB baseline.

### `v2-engine`

- Size/profile: `15M`, `81 files`
- Top file types: `.md(45)`, `.py(15)`, `.sh(13)`, `.csv(6)`, `.db(2)`
- Notable folder: `backups/`
- Largest files:
  - `test_relations.csv` (`6.04 MB`)
  - `backups/20260116_222742/test_relations.csv` (`6.04 MB`)
  - `knowledge_base.db` (`0.94 MB`)
- Notes: richest historical documentation + duplicated backup payloads.

### `v3-dev`

- Size/profile: `7M`, `38 files`
- Top file types: `.md(17)`, `.py(12)`, `.sh(6)`, `.csv(2)`, `.db(1)`
- Largest files:
  - `test_relations.csv` (`6.04 MB`)
  - `knowledge_base.db` (`0.62 MB`)
- Notes: intermediate dev snapshot, leaner than v2.

### `v4-workspace`

- Size/profile: `21M`, `527 files`
- Top file types: `.py(395)`, `[no-ext](38)`, `.md(34)`, `.json(18)`, `.txt(12)`
- Key top-level folders:
  - `config`, `data`, `docs`, `legacy`, `logs`, `output`, `reports`, `scripts`, `tools`
- Largest files:
  - `output/nocTurneMeLoDieS_music_collection/...phase1.json` (`6.83 MB`)
  - `output/documents_analysis/...phase1.json` (`3.15 MB`)
  - `output/pythons_activation_analysis/...phase1.json` (`2.18 MB`)
  - `output/avatarts_full_analysis/...phase1.json` (`1.80 MB`)
- Notes: most likely canonical working area moving forward.

## Practical next sort/cleanup pass

- Define one canonical runtime root (recommended: `v4-workspace`)
- Move older versions (`v1`-`v3`) under a single `/archive` namespace
- Add retention rules for `output` CSV/HTML/JSON timestamp batches
- Exclude large generated outputs and DB files from day-to-day scanning where possible
