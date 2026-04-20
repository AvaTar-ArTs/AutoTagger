# n8n_workflows — workspace policy (AutoTagger + canonical repo)

## Do not remove — version instead

- **Do not delete** prior docs, playbooks, or workflow JSON history to “replace” them. Add a **new path or repo version** (for example `docs/v3/…`, a dated export, or a new branch in [n8n_workflows](https://github.com/AvaTar-ArTs/n8n_workflows)) and link forward from the old entry.
- Prefer **additive** changes: extend tables, add rows to link maps, append changelog sections.

## Two locations (intentional)

1. **Canonical full library (git repo):** `/Users/steven/n8n_workflows` → remote `AvaTar-ArTs/n8n_workflows`.
2. **AutoTagger mirror:** `AutoTagger/n8n_workflows/` tracks **markdown + library docs** in the AutoTagger repo; heavy trees may exist as **symlinks** to the canonical folder (see `LOCAL_BASE_NOTE.md`, `CANONICAL_HOME.md`).

## What may evolve freely

- **`.gitignore`** at the AutoTagger repo root may change over time to keep clones lean (outputs, large mirrors, local-only paths). That is normal hygiene and does not delete source history in git.

## Restoring symlinks (local only, not committed)

From `AutoTagger/n8n_workflows/`:

```bash
ln -sf /Users/steven/n8n_workflows/free free
ln -sf /Users/steven/n8n_workflows/premium premium
ln -sf /Users/steven/n8n_workflows/workflows workflows
ln -sf /Users/steven/n8n_workflows/imports imports
```
