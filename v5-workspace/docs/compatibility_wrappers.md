Compatibility Wrappers (Add-Only)

Purpose
- Provide a working runtime path without editing or overwriting original files.
- Keep originals intact while enabling tests and execution under current repo paths.

Added Files
- `scripts/phase1_rapid_scan_compat.py`: Fixes the f-string syntax error in Phase 1 without editing the original.
- `scripts/phase2_intelligent_organization.py`: Minimal Phase 2 implementation (missing in repo).
- `scripts/phase3_advanced_intelligence.py`: Minimal Phase 3 implementation (missing in repo).
- `scripts/autotag_main_compat.py`: Uses repo-relative paths and the compat phase scripts.
- `autotag_compat.sh`: Shell runner for the compat pipeline.

Usage
- Run the compat pipeline:
  `./autotag_compat.sh /path/to/target my_run_name --no-open`

Notes
- Original files remain unchanged.
- If you want in-place fixes instead, confirm and I will apply targeted corrections.
