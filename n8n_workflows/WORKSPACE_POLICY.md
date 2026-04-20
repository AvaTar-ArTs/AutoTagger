# n8n_workflows — workspace policy (AutoTagger + optional second repo)

## Do not remove — version instead

- **Do not delete** prior docs or workflow JSON history to “replace” them. Add a **new path or repo version** (for example `docs/v3/…`, a dated export, or a new branch in [n8n_workflows](https://github.com/AvaTar-ArTs/n8n_workflows)) and link forward from the old entry.
- Prefer **additive** changes: extend tables, add rows to link maps, append changelog sections.

## Two copies (no symlinks)

1. **AutoTagger repo:** `AutoTagger/n8n_workflows/` — **real directories only**, tracked in `AvaTar-ArTs/AutoTagger`.
2. **Standalone repo (optional):** `/Users/steven/n8n_workflows` — same project as `AvaTar-ArTs/n8n_workflows`. Keep them aligned with **git merge / cherry-pick / rsync + commit**, not symlinks.

## What may evolve freely

- **`.gitignore`** at the AutoTagger repo root may change over time to keep clones lean (outputs, large mirrors, local-only paths). That is normal hygiene and does not delete source history in git.
