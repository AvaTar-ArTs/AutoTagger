# AutoTagger Operating Model Design

Date: 2026-04-20  
Status: Approved for planning

## Goal

Create a stable operating model for AutoTagger that goes beyond one-time sorting and enables:

- controlled workspace growth,
- reliable repeatable execution,
- measurable intelligence quality improvements,
- durable project memory and context continuity.

## Scope

This design covers a combined roadmap across:

- `A`: prevent future clutter automatically (retention/archiving),
- `B`: improve analysis quality (Phase 2/3 intelligence),
- `C`: improve speed/repeatability (one-command workflows + verification),
- `D`: improve knowledge continuity (docs/memory/context automation).

Recommended sequencing: `A + C` first, then heavier `B + D`.

## Architecture

Use a 4-lane operating model with strict execution order:

1. **Lane A - Hygiene and retention**
   - Canonical folder roles (`active`, `archive`, `generated`, `reference`)
   - Retention/rotation policy for timestamped artifacts
   - Safe archival boundaries and exclusions
2. **Lane C - Execution reliability**
   - Single command entrypoint for routine operations
   - Mandatory verification after structural changes
   - Deterministic output and report contracts
3. **Lane B - Intelligence quality**
   - Upgrade classification logic with confidence and rationale
   - Keep baseline strategy; add advanced strategy behind a flag
   - Track quality metrics over time
4. **Lane D - Knowledge continuity**
   - Structured updates to learned context docs
   - Delta digests between runs
   - Run metadata linkage to generated reports

## Components

### 1) `workspace-policy` (Lane A)

Responsibilities:

- Define and validate canonical workspace roles.
- Enforce retention/archival rules for generated artifacts.
- Publish `workspace_state.json` summary (size, churn, freshness).

Constraints:

- Unsafe paths and conflicting policies are blocking errors.

### 2) `run-orchestrator` (Lane C)

Responsibilities:

- Provide one stable entrypoint for `scan`, `verify`, `report`, `archive`.
- Normalize naming and destination paths for outputs.
- Fail fast on prerequisites and always run verification on structural work.

Constraints:

- Command contracts are explicit and testable.

### 3) `intelligence-evaluator` (Lane B)

Responsibilities:

- Wrap Phase 2/3 classification with confidence and rationale fields.
- Support pluggable strategies (baseline first, advanced optional).
- Publish quality metrics (coverage, confidence distribution, correction rate).

Constraints:

- On evaluator failure, degrade to baseline and continue as partial success.

### 4) `context-sync` (Lane D)

Responsibilities:

- Append meaningful decisions and run deltas to `docs/learned-context.md`.
- Link runs to output/report artifacts.
- Emit short "what changed since last run" digest.

Constraints:

- Sync failures are non-blocking, but must be visible in verification output.

## End-to-end data flow

`scan input -> run-orchestrator -> workspace-policy checks -> analysis/classification -> output + metrics -> context-sync -> verification report`

## Error handling model

- **Blocking:** policy violations, invalid/unsafe path operations, conflicting retention rules.
- **Degradable/partial:** intelligence evaluator issues (fallback strategy).
- **Non-blocking with warnings:** context sync write/format issues.
- Each run emits both:
  - machine status: `ok | partial | failed`
  - human summary: concise execution and issue digest.

## Testing strategy

- **Policy tests (A):** retention matching, archive safety, exclusion behavior.
- **Orchestrator tests (C):** command contract tests across success/failure paths.
- **Intelligence tests (B):** golden-set regression + confidence bounds.
- **Context tests (D):** append safety, idempotency, structure validation.

## Rollout stages

### Stage 1 - Stabilize (`A + C`)

- Implement policy layer and orchestrator command contracts.
- Make verification gate mandatory after structural actions.

### Stage 2 - Observe

- Add run summaries and quality metrics collection.
- Establish trend baselines.

### Stage 3 - Intelligence expansion (`B`)

- Add advanced classifier strategy behind feature flag.
- Compare against baseline using tracked quality metrics.

### Stage 4 - Continuity automation (`D`)

- Automate context-sync and delta digest generation.
- Ensure contextual memory updates become routine artifacts.

## Definition of done

- Output growth is controlled by explicit retention policy.
- Core workflows run through one stable entrypoint.
- Classification quality is measurable and improving release-to-release.
- Learned context updates happen automatically after meaningful runs.

## Non-goals

- Full rewrite of existing AutoTag internals.
- Immediate dependency on LLM-only categorization.
- Large-scale repo restructuring unrelated to A/B/C/D roadmap.

## Risks and mitigations

- **Risk:** premature intelligence complexity before stabilization.  
  **Mitigation:** enforce A+C gates before B+D expansion.

- **Risk:** policy rules accidentally archive needed artifacts.  
  **Mitigation:** dry-run mode + explicit allow/deny lists + archive previews.

- **Risk:** context automation introduces noisy or low-value updates.  
  **Mitigation:** only persist high-signal deltas and decision-level changes.
