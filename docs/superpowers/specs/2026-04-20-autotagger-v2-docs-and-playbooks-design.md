# AutoTagger V2 Documentation + Playbooks Design

Date: 2026-04-20  
Status: Implemented baseline (V2 truth + V2/V3 playbooks + hub links); iterate in follow-up PRs  
Scope: V2 documentation system for `v5-workspace` across markdown truth docs and creative HTML playbooks

## 1) Goal

Create a significantly more creative and usable documentation experience while preserving operational accuracy.

This design establishes a two-surface model:
- **Truth surface (Markdown):** precise operational guidance and source-of-truth procedures.
- **Experience surface (HTML playbooks):** creative narrative, decision pathways, monetization framing, and visual storytelling.

Both surfaces must stay aligned through an explicit link map and QA gates.

## 2) Non-Goals

- No rewrite of core AutoTag runtime/scripts in this phase.
- No migration to a generator/static-site framework in this phase.
- No redesign of legacy `v1` playbooks beyond archival labeling and linking.

## 3) Audience and Outcomes

Primary audiences:
- **Operator:** needs runbooks, failure recovery, and verification paths.
- **Builder:** needs extension patterns and integration workflows.
- **Seller:** needs packaging, offers, launch paths, and proof strategy.

Expected outcomes:
- Faster orientation for first-time users.
- Higher confidence for operators executing live runs.
- Better conversion from “tool usage” to “revenue use cases.”
- Reduced drift between “creative docs” and “technical truth.”

## 4) Information Architecture

## 4.1 Markdown truth surface (V2)

Add:
- `v5-workspace/docs/v2/00-start-here.md`
- `v5-workspace/docs/v2/operator.md`
- `v5-workspace/docs/v2/builder.md`
- `v5-workspace/docs/v2/seller.md`
- `v5-workspace/docs/v2/uses-library.md`
- `v5-workspace/docs/v2/faq-troubleshooting.md`
- `v5-workspace/docs/v2/changelog-v2.md`
- `v5-workspace/docs/v2/_templates/` (starter templates for future pages)

Role:
- Canonical commands, constraints, assumptions, and troubleshooting.
- Exact file paths and script references.
- Minimal persuasive language, maximum clarity.

## 4.2 HTML experience surface (Playbooks V2)

Add:
- `v5-workspace/playbooks/v2/index.html`
- `v5-workspace/playbooks/v2/operator-v2x.html`
- `v5-workspace/playbooks/v2/builder-v2x.html`
- `v5-workspace/playbooks/v2/seller-v2x.html`
- `v5-workspace/playbooks/v2/hybrid-v2x.html`
- `v5-workspace/playbooks/v2/uses-catalog-v2.html`
- `v5-workspace/playbooks/v2/LINK_MAP.md`

Role:
- High-creative presentation, persona flows, monetization framing, and scenario storytelling.
- “Choose-your-path” interaction from the V2 index.
- Inline bridges to truth docs for exact execution.

## 4.3 Versioning strategy

- Preserve existing playbooks as prior generation; do not overwrite.
- Introduce V2 as a separate namespace under `playbooks/v2` and `docs/v2`.
- Changelog entries must clearly distinguish “legacy,” “v2 new,” and “v2 updated.”

## 5) Frontend Design Direction (for V2 playbooks)

This section applies `frontend-design` principles while respecting existing codebase patterns.

## 5.1 Context mode

Current repo indicates a **partial system**:
- Existing static HTML/CSS pages and established tone in v5 playbooks.
- No strict component framework requirement for this phase.

Decision:
- Reuse existing page architecture where useful.
- Apply stronger visual thesis and interaction design to V2 pages only.

## 5.2 Visual thesis

“Editorial operator intelligence”: dark, intentional, high-contrast layouts with selective accent color, command-centric typography pairing, and concise narrative blocks that feel premium but operational.

## 5.3 Content plan

Per page sequence:
1. Context framing (who this page is for)
2. Decision fork (what path to take)
3. Core workflow blocks (what to do now)
4. Use-case amplification (how to extract more value/revenue)
5. Action and verification (what success looks like)

## 5.4 Interaction plan

For V2 pages:
- One deliberate entrance sequence for hero and first decision blocks.
- One hover/reveal pattern for decision cards and use-case cards.
- One lightweight scroll-linked section emphasis for long-form readability.

Guardrails:
- Accessibility first (focus states, contrast, semantic sections).
- Motion supports hierarchy; no ornamental-only animation.

## 6) Creative “Uses” System

Create a reusable “uses catalog” pattern that maps each use case to:
- Trigger condition
- Required inputs
- Workflow path
- Output artifact
- Monetization angle (if commercial)
- Risk and mitigation notes

Use-case categories:
- Automation operations
- Content repurposing
- Lead generation
- SaaS packaging
- Service/agency delivery
- Internal knowledge ops

Each category should include at least one fast-start path and one advanced path.

## 7) Quality Workflow (writing-skills-inspired)

Adopt a practical RED/GREEN/REFACTOR loop for docs:

- **RED (baseline audit):** identify current doc failures (ambiguity, stale routes, weak cross-links).
- **GREEN (minimal fix set):** produce V2 docs/playbooks that directly address those failures.
- **REFACTOR (loophole closure):** remove ambiguity, strengthen links, and tighten decision paths.

Mandatory QA gates before completion:
1. Placeholder scan (`TODO`, `TBD`, unfinished sections)
2. Contradiction scan (HTML claims vs markdown truth docs)
3. Scope scan (no accidental platform rebuild in this phase)
4. Ambiguity scan (single interpretation for critical steps)
5. Link integrity check (all cross-links resolvable)

## 8) Data Flow and Link Contracts

Primary flow:
`playbooks/v2/*.html` -> references -> `docs/v2/*.md`

Contract:
- Any command/script assertion in HTML must point to a markdown truth section.
- Any monetization recommendation in markdown should link to at least one example playbook pattern.
- `LINK_MAP.md` is the explicit contract index and maintenance surface.

## 9) Error Handling and Maintenance

Failure modes:
- Drift between creative and truth surfaces
- Broken links
- Version confusion (legacy vs v2)
- Overly verbose pages that hide core actions

Mitigations:
- “Source of truth” badges in markdown pages.
- “Validated against docs/v2” markers in playbooks.
- Changelog discipline for every V2 file touch.
- Keep each page purpose-specific; avoid mixed intent pages.

## 10) Testing and Verification

Testing approach:
- Manual narrative walkthrough per persona (Operator/Builder/Seller).
- Link checks for all V2 pages and docs.
- Run litmus checks for frontend quality:
  - clear first-screen purpose
  - one-page-one-job sections
  - readable contrasts and focus states
  - no prompt/AI leakage in user-facing copy

Acceptance criteria:
- New user can choose a path in under 60 seconds.
- Operator can find exact run path without opening legacy docs.
- Seller can extract at least 3 clear offer/use-case pathways from V2.
- No unresolved placeholders or contradictory statements.

## 11) Rollout Plan

Phase A (foundation):
- Create V2 folder structures, hub pages, and truth skeleton docs.

Phase B (content depth):
- Fill operator/builder/seller flows and uses catalog.

Phase C (quality hardening):
- Run QA gates, link map completion, and changelog updates.

Phase D (handoff):
- Final review and transition to implementation planning.

## 12) Risks and Trade-Offs

Trade-off chosen:
- Two-surface model introduces maintenance overhead, but greatly improves creativity without sacrificing technical clarity.

Key risk:
- Content drift over time.

Control:
- Enforced link contracts + changelog discipline + QA gates.

## 13) Deliverables from this design

1. V2 markdown documentation tree (`docs/v2`)
2. V2 HTML playbook tree (`playbooks/v2`)
3. Cross-link contract (`playbooks/v2/LINK_MAP.md`)
4. V2 changelog artifacts (`docs/v2/changelog-v2.md` + updates to `v5-workspace/CHANGELOG.md`)
5. Quality checklist integrated into doc workflow

## 14) Open Assumptions (explicit)

- V2 remains static HTML + markdown in this phase (no generator migration).
- Existing V1 assets remain available as archival references.
- This design does not require new runtime dependencies for docs delivery.
