# Trend Pulse pattern (contract)

Every template in this library follows the same **stage order** (see `meta.trendPulseStageOrder` in JSON where present):

`intake → enrichment → scoring → content_generation → publishing_or_exports → logging`

## QA gates before you ship a variant

1. **Intake** — explicit sample payload in first `Set` or trigger.
2. **Enrichment** — external calls use `retryOnFail` where supported.
3. **Scoring** — treat model output as **heuristic**, not ground truth; label projections as estimates in any customer-facing copy.
4. **Publishing** — Slack/HTTP nodes must not leak secrets into message bodies.
5. **Logging** — success and error payloads include `workflow` name + timestamp.

## Free vs premium

- **Free:** fewer stages, simpler outputs, CTA to upgrade.
- **Premium:** deeper chains, richer scoring, more export targets.
