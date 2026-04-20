# V5 Workspace Overview

This `v5-workspace` is the unified and self-contained operating root.

## What is included

- Full copy of prior active implementation from `v4-workspace/`
- Consolidated snapshots in `_root-links/` for everything else:
  - `_root-links/reference/autotagger-lite`
  - `_root-links/reference/current`
  - `_root-links/legacy/v1-original-kb`
  - `_root-links/legacy/v2-engine`
  - `_root-links/legacy/v3-dev`
  - `_root-links/data/root-output`
  - `_root-links/docs/root-docs`

## Independence status

- `_root-links/` entries are local copied directories (not symlinks)
- `v5-workspace` can be moved/copied as a standalone workspace
- Current footprint is larger because `output` and legacy trees are now fully local

## How to use V5

- Run day-to-day work from `v5-workspace/`
- Keep new scripts/config/docs in `v5-workspace/` first
- Use `_root-links/` to access historical/reference/data snapshots without leaving V5 context

## Suggested next move

- Treat this as canonical and start migrating any remaining root-level logic into native V5 folders over time.
