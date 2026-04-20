# FAQ and troubleshooting

## `venv` missing

**Symptom:** `AutoTag virtual environment not found`.

**Fix:** Run `./setup_autotag.sh` from `v5-workspace`.

## Wrong directory scanned

**Symptom:** Output reflects unexpected files.

**Fix:** Pass explicit target: `./autotag.sh /absolute/path/to/target`. Remember: **no args** scans the workspace root by design.

## CSV did not open

**Symptom:** Run succeeded but no app opened.

**Fix:** Use `./autotag.sh <path> <name> --no-open` and open CSV manually from `./output/<name>/`.

## verify_installation fails on missing optional artifacts

**Symptom:** Script reports missing `output/csv_test/...`.

**Fix:** Either run a small smoke scan once to generate artifacts, or treat that check as non-blocking (future improvement); core dirs should still exist: `scripts/`, `config/`, `data/`, `docs/`.

## Paths in older docs still show `/Users/steven/AutoTag`

**Symptom:** Confusing copy in legacy `docs/user_guide.md`.

**Fix:** Prefer this `docs/v2/` tree for V5 workspace. Legacy guide may be updated in a separate change.

## Playbook disagrees with markdown

**Symptom:** Command mismatch.

**Rule:** `docs/v2/*.md` wins. File an issue or patch `playbooks/v2/LINK_MAP.md` / HTML.
