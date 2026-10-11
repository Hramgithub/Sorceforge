# Plan: Sourcefold Release Roadmap

Goal id: `20260714-sourcefold-release-roadmap`

State: completed

Owner: `gpt-5.5` orchestrator, medium effort

## Objective

Define a high-level, end-to-end roadmap from the current Sourcefold scaffold to
a releasable product, without prematurely diving into one module or starting
real book processing.

## Role Ownership

| Role | Effort | Scope |
|---|---|---|
| `gpt-5.5` orchestrator | medium | Owns canonical roadmap synthesis, plan/context, stop/ask decisions, and user-facing recommendation. |
| Sol architect | high | Propose product architecture phases, gates, dependencies, and release shape. |
| Terra engineering critic | medium | Critique the roadmap for engineering risk, missing gates, accidental scope creep, and release readiness gaps. |

## Steps

| Step | Owner | Status | Evidence | Next action |
|---|---|---|---|---|
| R1 Read current Sourcefold state | Orchestrator | completed | `PROJECT_STATUS.md`, scaffold plan/context, Terra scaffold handoff, product boundary, module contracts, NRI governance. | Dispatch roadmap contributors. |
| R2 Architecture roadmap proposal | Sol | completed | `handoffs/sol-roadmap-architecture-20260714.md`, SHA-256 `B0092EA96740DF45FC2238E833463CD2EAA8EBADE8846515DA40E94D18EAC628`. | Use in synthesis. |
| R3 Engineering risk critique | Terra | completed | `handoffs/terra-roadmap-risk-critique-20260714.md`, SHA-256 `759002D8DA17894D94C082AA58560D2511F51A70E47B96ED086DA00D93F9C868`. | Use in synthesis. |
| R4 Orchestrator synthesis | Orchestrator | completed | `roadmap.md`, plan/context updates. | Present recommendation. |
| R5 User decision point | User + Orchestrator | completed | Roadmap prepared for user decision. | Decide whether to launch Phase 0 or revise roadmap in the next goal. |

## Definition Of Done

- Roadmap covers the path from current scaffold to first release candidate.
- The plan separates product release gates from module implementation details.
- Terra scaffold findings are placed as early gates, not postponed into
  implementation.
- Optional lanes (`press`, `bridge`) remain downstream and non-blocking for the
  core product unless release scope explicitly includes them.
- Knowledge base work remains outside ordinary release scope.
- Sol and Terra handoffs are captured as immutable receipts.
- The final answer identifies the recommended next goal and unresolved user
  decisions.

## Watchdog

Expected artifacts:

- `docs/plans/20260714-sourcefold-release-roadmap/handoffs/sol-roadmap-architecture-20260714.md`
- `docs/plans/20260714-sourcefold-release-roadmap/handoffs/terra-roadmap-risk-critique-20260714.md`

If an expected handoff is absent after the contributor returns, request a
checkpoint, then restart or resume the same narrow contributor step and verify
the artifact. The orchestrator must not perform that contributor's assigned
critique after the first missing artifact.

## Orchestrator Synthesis

Recommended path: contract-first release roadmap with a bounded, headless
Sourcefold Core 0.1 RC.

The first releasable product should prove the complete core lane
`reconstruct -> translate -> proofread` for one declared source profile and
supported structure subset. It should not include `press`, `bridge`, knowledge
base generation, broad PDF/OCR support, UI, or Translator compatibility.

Phase sequence:

1. Phase 0: Release charter and contract decisions.
2. Phase 1: Executable contract and evidence spine.
3. Phase 2: Thin end-to-end core lane.
4. Phase 3: Quality completion on the supported profile.
5. Phase 4: Operator product hardening.
6. Phase 5: Candidate freeze and independent Terra release review.

Critical next decision: authorize Phase 0 as the next goal, or revise the
release boundary before any implementation planning.

## Compact Task Packet: Sol Roadmap Architecture

Goal id: `20260714-sourcefold-release-roadmap`

Step id: `R2`

Role and effort: Sol analyst/architect, high.

Relevant paths:

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`
- `Sourcefold/manifests/artifact_manifest.schema.json`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/context.md`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/handoffs/terra-engineering-critique-20260714.md`

Expected artifact:
`Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/handoffs/sol-roadmap-architecture-20260714.md`.

Acceptance criteria: propose a high-level product roadmap from scaffold to first
release candidate, with phases, gates, dependencies, and release definition.
Stay product-level; do not implement code or rewrite canonical context.

Forbidden scope: do not inspect or modify `CoC`, `Dune`, `Git`, `FoundryVTT`,
`.tools`, `.agents`, temp folders, or arbitrary `translator` files.

## Compact Task Packet: Terra Roadmap Risk Critique

Goal id: `20260714-sourcefold-release-roadmap`

Step id: `R3`

Role and effort: Terra engineering critic, medium.

Relevant paths:

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`
- `Sourcefold/manifests/artifact_manifest.schema.json`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/context.md`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/handoffs/terra-engineering-critique-20260714.md`

Expected artifact:
`Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/handoffs/terra-roadmap-risk-critique-20260714.md`.

Acceptance criteria: critique likely roadmap risks, missing gates, false
sequencing, accidental scope creep, and release-readiness gaps. Stay
product-level; do not implement code or rewrite canonical context.

Forbidden scope: do not inspect or modify `CoC`, `Dune`, `Git`, `FoundryVTT`,
`.tools`, `.agents`, temp folders, or arbitrary `translator` files.
