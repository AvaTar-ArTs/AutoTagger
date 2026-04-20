# V2 playbook ↔ truth doc link map

Convention: playbook pages are under `playbooks/v2/`. Truth docs are under `docs/v2/`.

| Playbook | Primary truth doc | Secondary |
|----------|-------------------|------------|
| `index.html` | `docs/v2/00-start-here.md` | all |
| `operator-v2x.html` | `docs/v2/operator.md` | `faq-troubleshooting.md` |
| `builder-v2x.html` | `docs/v2/builder.md` | `operator.md` |
| `seller-v2x.html` | `docs/v2/seller.md` | `uses-library.md` |
| `hybrid-v2x.html` | `docs/v2/00-start-here.md` | `uses-library.md` |
| `uses-catalog-v2.html` | `docs/v2/uses-library.md` | `seller.md` |

## Relative paths (from `playbooks/v2/`)

- To truth: `../../docs/v2/<file>.md`

## QA gate

Before marking V2 “done,” confirm every `href` to `../../docs/v2/` resolves on disk.
