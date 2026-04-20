# Uses library (patterns)

Each pattern lists **trigger → inputs → steps → outputs → risks**.

## U1 — Automation inventory

- **Trigger:** Unknown number of scripts across a large tree.
- **Inputs:** Target directory path.
- **Steps:** `./autotag.sh <path> inventory_<date>`
- **Outputs:** Phase JSON + CSV summary.
- **Risks:** Sensitive paths in CSV; scrub before sharing externally.

## U2 — Value triage before refactor

- **Trigger:** Planning consolidation of legacy automation folders.
- **Inputs:** Two candidate roots; run twice.
- **Steps:** Compare CSV `predicted_business_value` and `integration_potential_*`.
- **Outputs:** Ranked list of keep/merge/retire candidates.
- **Risks:** Business value is heuristic; validate with owner interviews.

## U3 — Lead magnet bundle

- **Trigger:** Marketing wants “automation report” for a niche.
- **Inputs:** Public-safe sample directory (no secrets).
- **Steps:** Run scan → export highlights → wrap in playbook HTML PDF export (manual print-to-PDF).
- **Outputs:** Branded artifact for Gumroad.
- **Risks:** Overclaiming AI precision; label scores as estimates.

## U4 — n8n / scheduled hygiene

- **Trigger:** Weekly catalog of internal `~/scripts` or team drive.
- **Inputs:** Cron or n8n Execute Command to `autotag.sh` with explicit path.
- **Outputs:** Timestamped folder under `./output/`.
- **Risks:** Long runs on huge trees; schedule off-peak; add disk checks.

## U5 — Internal knowledge ops

- **Trigger:** Link scan results to Notion database rows (external to AutoTag).
- **Inputs:** CSV from AutoTag + import mapping.
- **Steps:** Manual or n8n import; key on `path` + `name`.
- **Outputs:** Searchable internal catalog.
- **Risks:** Drift if directory moves; store stable IDs if possible.

For richer storytelling, see `../playbooks/v2/uses-catalog-v2.html` and `../playbooks/v3/uses-wunderkammer.html`.
