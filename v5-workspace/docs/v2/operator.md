# Operator runbook

## First-time setup

```bash
cd /path/to/AutoTagger/v5-workspace
./setup_autotag.sh
```

Creates `venv/` and validates core layout. If setup fails, see [faq-troubleshooting.md](./faq-troubleshooting.md).

## Run AutoTag

**Default (scan the workspace itself):**

```bash
./autotag.sh
```

**Explicit target directory:**

```bash
./autotag.sh /path/to/target [optional_output_name] [--no-open]
```

- With no arguments, the script uses `REPO_ROOT` as the target and timestamps the output name.
- `--no-open` skips auto-opening the CSV if your environment prefers it.

Compat runner:

```bash
./autotag_compat.sh
```

## Verify installation

```bash
./verify_installation.sh
```

Uses `AUTOTAG_ROOT` derived from the script location (portable).

## Where outputs go

- Base directory: `./output/<run_name>/` (see `config/autotag_config.json` → `paths.output_base`).
- Logs: `./logs/` when logging is enabled by downstream scripts.
- Knowledge DB path (if used): `./data/knowledge_base.db` per config.

## What “success” looks like

- Terminal completes without Python tracebacks.
- `./output/<run_name>/` contains expected artifacts (JSON phases, CSV where applicable).
- CSV opens in your spreadsheet app unless `--no-open` was passed.

## Truth vs playbook

If a playbook page shows a command, it must match this file. When in doubt, **this file wins**.
