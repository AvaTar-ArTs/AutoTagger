# AutoTag SaaS MVP Roadmap

## Objective

Ship a paid MVP in 4 phases while reusing existing V5 scanning logic.

## Phase 1: API wrapper + jobs

- Create API endpoint to trigger scans
- Queue jobs and track status (`queued`, `running`, `done`, `failed`)
- Persist output artifact references

## Phase 2: Minimal dashboard

- List workspaces and latest runs
- Show top metrics:
  - total tools
  - high-value tools
  - category breakdown
- Download CSV/JSON artifacts

## Phase 3: Billing and access

- Add authentication and org/workspace model
- Add plan gating (Starter/Pro/Agency)
- Connect billing provider (Stripe or Lemon Squeezy)

## Phase 4: Scheduled monitoring

- Add recurring run schedules
- Add “what changed” deltas
- Add weekly email summary

## MVP success criteria

- At least 5 paying users
- 70%+ weekly active rate among trial users
- Median time-to-first-value under 15 minutes

