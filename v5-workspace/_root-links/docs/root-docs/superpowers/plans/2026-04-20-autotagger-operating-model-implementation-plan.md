# AutoTagger Operating Model Implementation Plan

Date: 2026-04-20  
Based on: `docs/superpowers/specs/2026-04-20-autotagger-operating-model-design.md`

## Objective

Execute the approved operating model in a low-risk sequence that stabilizes the workspace first, then layers in intelligence and continuity automation.

## Success criteria

- Retention policy actively controls output growth.
- A single entrypoint can run core workflows predictably.
- Verification output clearly reports `ok | partial | failed`.
- Classification quality is measurable with baseline metrics.
- Learned context updates are automated and high-signal.

## Phase plan

## Phase 1 - Stabilize foundations (`A + C`)

### Work items

- Define canonical workspace roles and policy config schema.
- Implement policy validator for safe path operations.
- Add retention rules for generated artifacts (with dry-run).
- Build/standardize one orchestrator entrypoint for:
  - `scan`
  - `verify`
  - `report`
  - `archive`
- Enforce mandatory verification after structural operations.

### Deliverables

- Policy configuration file and validator module.
- Updated run script/entrypoint contract.
- Verification report format (human + machine-readable status).

### Validation

- Fixture-based tests for retention and archive safety.
- Contract tests for orchestrator commands and failure behavior.

## Phase 2 - Observability baseline

### Work items

- Add `workspace_state.json` generation (size/churn/freshness).
- Add run summary artifact with status + warnings.
- Capture baseline quality metrics for current classifier behavior.

### Deliverables

- Workspace telemetry artifact.
- First trend snapshot for output growth and classification confidence.

### Validation

- Snapshot tests for report structure.
- Regression checks for telemetry generation on multiple directories.

## Phase 3 - Intelligence expansion (`B`)

### Work items

- Wrap Phase 2/3 outputs with confidence + rationale fields.
- Add pluggable strategy interface:
  - baseline rule strategy (default)
  - advanced strategy (feature-flagged)
- Build golden-set evaluation harness.

### Deliverables

- Strategy abstraction and baseline implementation.
- Feature-flagged advanced path stub/integration point.
- Quality dashboard artifact (coverage/confidence/correction rate).

### Validation

- Golden-set regression must not degrade baseline beyond agreed threshold.
- Fallback behavior tested (advanced failure -> baseline partial success).

## Phase 4 - Context continuity (`D`)

### Work items

- Implement structured append workflow for `docs/learned-context.md`.
- Generate "what changed since last run" digest.
- Link run metadata to relevant outputs/reports.

### Deliverables

- Context sync module with idempotent update behavior.
- Delta digest artifact included in run summary.

### Validation

- Idempotency tests for repeated context sync operations.
- Guardrails to prevent noisy/duplicate updates.

## Cross-phase safeguards

- Keep all destructive actions behind dry-run previews first.
- Keep archival operations path-restricted and explicitly allowlisted.
- Treat context sync as warning-only; never block main analysis flow.
- Require verify step evidence before claiming completion of a phase.

## Recommended execution order

1. Implement Phase 1 with tests.
2. Add Phase 2 telemetry/reporting.
3. Introduce Phase 3 strategy layer behind flag.
4. Finalize Phase 4 context automation.

## Work breakdown by independent streams

- **Stream A (Policy):** retention, archive safety, role mapping.
- **Stream C (Orchestrator):** entrypoint contracts, verify/report flow.
- **Stream B (Intelligence):** confidence/rationale and strategy abstraction.
- **Stream D (Context):** learned-context sync and delta digest.

Parallelization note: A and C should progress together first; B and D start after A/C interfaces are stable.

## Exit checklist

- [ ] Policy config + validator merged
- [ ] Orchestrator command contract stable and documented
- [ ] Verification report includes status + warnings
- [ ] Baseline quality metrics captured
- [ ] Advanced strategy behind feature flag
- [ ] Context sync automated and idempotent
- [ ] End-to-end run demonstrates full pipeline with artifacts
