# V6 SaaS Overview

V6 is the **SaaS-oriented** track for AutoTag. **Versioned docs** live at the **repository root** (`V6.md`, `V6_SAAS_OVERVIEW.md`, `saas/*.md`, `saas_landing_v1.html`). The optional folder `v6-workspace/` is a **local sandbox** (gitignored) for experiments and heavy mirrors—not the source of truth for these files.

## Should this be a SaaS?

Yes, if you position it as:

- **Workspace Intelligence Platform** for agencies/operators
- Not just a local script, but a system that delivers recurring value:
  - scheduled scans
  - trend tracking
  - team dashboards
  - client-ready reports

## Best SaaS positioning

- **Primary ICP:** agencies, automation consultants, operations teams
- **Core pain:** tool sprawl, no visibility, no scoring/prioritization
- **Outcome sold:** clarity + prioritized action, not “file scanning”

## Suggested SaaS tiers

- **Starter ($19-$39/mo):** single workspace, manual runs, CSV/JSON export
- **Pro ($79-$149/mo):** multi-workspace, scheduled scans, trend dashboards
- **Agency ($299+/mo):** multi-client reporting, white-label exports, team seats

## V6 package (this folder)

- [`saas/SAAS_PRODUCT_STRATEGY.md`](./saas/SAAS_PRODUCT_STRATEGY.md)
- [`saas/SAAS_MVP_ROADMAP.md`](./saas/SAAS_MVP_ROADMAP.md)
- [`saas_landing_v1.html`](./saas_landing_v1.html)

## Immediate next build move

Start with an MVP that wraps existing V5 logic behind:

1. API job trigger
2. run status + artifacts store
3. basic dashboard
4. billing gate

