# Builder guide

## Layout you need to know

| Path | Role |
|------|------|
| `scripts/autotag_main.py` | Orchestrates phases |
| `scripts/phase*.py` | Phase implementations |
| `config/autotag_config.json` | Paths, processing, categorization weights |
| `data/` | Local DB and datasets |
| `output/` | Run artifacts (gitignored at repo root; still used inside workspace) |

## Extending behavior

1. **New categorization signal** — update `config/autotag_config.json` and the phase that assigns categories (see `scripts/phase2_intelligent_organization.py`).
2. **New export shape** — trace CSV export from `autotag_main.py` and the phase that emits summaries.
3. **External trigger (n8n, CI)** — wrap `./autotag.sh` with environment variables; keep secrets out of the repo (`.env` is gitignored).

## Contract for integrations

- **Inputs:** `--target` directory must exist and be readable.
- **Outputs:** deterministic folder name if you pass `optional_output_name`; otherwise timestamped.
- **Failure:** non-zero exit from Python should propagate; capture logs from `./logs/` if present.

## Link to creative surfaces

- Operator narrative + visuals: `../playbooks/v2/builder-v2x.html`
- “Annex” experimental narrative: `../playbooks/v3/builder-annex.html`
