# AutoTag V5 — Start here (truth docs)

This folder is the **V2 source of truth** for how AutoTag behaves in `v5-workspace`. Creative HTML playbooks live under `playbooks/v2/` and `playbooks/v3/`; they may dramatize and sequence ideas, but **commands, paths, and recovery steps are authoritative here**.

## Pick your lane

| You are… | Read next |
|-----------|-----------|
| Running scans today | [`operator.md`](./operator.md) |
| Extending scripts or wiring integrations | [`builder.md`](./builder.md) |
| Packaging offers, pricing, launches | [`seller.md`](./seller.md) |
| Choosing a revenue or ops pattern | [`uses-library.md`](./uses-library.md) |
| Something broke | [`faq-troubleshooting.md`](./faq-troubleshooting.md) |

## Workspace assumptions

- All commands assume your shell’s current directory is **`v5-workspace`** (the folder that contains `autotag.sh`, `config/`, `scripts/`, `venv/`).
- `REPO_ROOT` in scripts resolves to that directory automatically.
- Outputs land under `./output/<run_name>/` unless you changed `config/autotag_config.json`.

## Map to playbooks

- **V2 experience layer:** `../playbooks/v2/index.html` — dark “editorial operator” presentation.
- **V3 experience layer:** `../playbooks/v3/index.html` — warm “archival annex” presentation (same truths, different narrative skin).

Cross-reference index: `../playbooks/v2/LINK_MAP.md` and `../playbooks/v3/LINK_MAP.md`.
