# Plan: Sourcefold Version Roadmap 0.1 To 1.0

Goal id: `20260714-sourcefold-version-roadmap-01-to-10`

State: completed

Owner: `gpt-5.5` orchestrator, medium effort

## Objective

Dry run the Sourcefold product path from Core 0.1 RC to 1.0 production and
produce a constructive version roadmap with nested expectations for each
version.

## Role Ownership

| Role | Effort | Scope |
|---|---|---|
| `gpt-5.5` orchestrator | medium | Owns canonical roadmap synthesis, plan/context, stop/ask decisions, and user-facing recommendation. |
| Sol architect | high | Proposes version ladder, product capability sequencing, and dependency structure from 0.1 to 1.0. |
| Terra engineering critic | medium | Challenges version gates, release claims, scope creep, missing validation, and production-readiness assumptions. |

## Steps

| Step | Owner | Status | Evidence | Next action |
|---|---|---|---|---|
| V1 Read current roadmap baseline | Orchestrator | completed | Sourcefold status, release roadmap, boundary, module contracts, acceptance criteria. | Dispatch contributors. |
| V2 Version architecture proposal | Sol | completed | `handoffs/sol-version-roadmap-20260714.md`, SHA-256 `9C745C710D25F8C96ED09A5B20187340F3FD31737F25B89C744781E61F9FFB88`. | Use in synthesis. |
| V3 Version risk critique | Terra | completed | `handoffs/terra-version-roadmap-critique-20260714.md`, SHA-256 `84319D4DA9906297D3DE4C8E727991F51C4745A62F8A3B63E0FAA1F0B39BC13C`. | Use in synthesis. |
| V4 Orchestrator synthesis | Orchestrator | completed | `version_roadmap.md`, context updates. | Present roadmap. |
| V5 User review | User + Orchestrator | completed | Final response and durable `version_roadmap.md`. | Decide whether to accept the version ladder and launch Phase 0 in the next goal. |

## Definition Of Done

- Roadmap covers Sourcefold Core 0.1 through Sourcefold 1.0.
- Each version states purpose, expected capabilities, non-goals, entry
  dependencies, exit/release gate, evidence, and likely implementation goals.
- The roadmap distinguishes release candidates, internal milestones, and
  production claims.
- `press`, `bridge`, broader source profiles, and Translator migration are
  sequenced deliberately rather than smuggled into 0.1.
- Sol and Terra handoffs are captured as immutable receipts.
- The final answer names the recommended next action.

## Watchdog

Expected artifacts:

- `docs/plans/20260714-sourcefold-version-roadmap-01-to-10/handoffs/sol-version-roadmap-20260714.md`
- `docs/plans/20260714-sourcefold-version-roadmap-01-to-10/handoffs/terra-version-roadmap-critique-20260714.md`

If a contributor returns without the expected handoff, request checkpoint, then
restart or resume the same narrow contributor step and verify the artifact. The
orchestrator must not perform that contributor's assigned analysis after the
first missing artifact.

## Compact Task Packet: Sol Version Roadmap

Goal id: `20260714-sourcefold-version-roadmap-01-to-10`

Step id: `V2`

Role and effort: Sol analyst/architect, high.

Relevant paths:

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/roadmap.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`

Expected artifact:
`Sourcefold/docs/plans/20260714-sourcefold-version-roadmap-01-to-10/handoffs/sol-version-roadmap-20260714.md`.

Acceptance criteria: propose a constructive version ladder from 0.1 to 1.0 with
version purpose, expected capabilities, gates, non-goals, dependencies, and
release evidence. Stay product-level; do not implement code.

Forbidden scope: do not inspect or modify `CoC`, `Dune`, `Git`, `FoundryVTT`,
`.tools`, `.agents`, temp folders, or arbitrary `translator` files.

## Compact Task Packet: Terra Version Roadmap Critique

Goal id: `20260714-sourcefold-version-roadmap-01-to-10`

Step id: `V3`

Role and effort: Terra engineering critic, medium.

Relevant paths:

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/roadmap.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`

Expected artifact:
`Sourcefold/docs/plans/20260714-sourcefold-version-roadmap-01-to-10/handoffs/terra-version-roadmap-critique-20260714.md`.

Acceptance criteria: critique the 0.1-to-1.0 ladder for false production claims,
missing validation gates, version inflation, scope creep, sequencing mistakes,
and risks specific to `press`, `bridge`, source-profile expansion, and
Translator migration. Stay product-level; do not implement code.

Forbidden scope: do not inspect or modify `CoC`, `Dune`, `Git`, `FoundryVTT`,
`.tools`, `.agents`, temp folders, or arbitrary `translator` files.

## Orchestrator Synthesis

The canonical version roadmap should treat Sourcefold 1.0 as a bounded,
production-supportable Core release, not a feature-complete platform. The main
line is:

- `0.1`: Core invariant proven on one declared profile.
- `0.2`: profile declarations and repeatability beyond one pilot.
- `0.3`: quality-depth and adversarial/regression coverage.
- `0.4`: long-form recovery, rerun, supersession, and revalidation.
- `0.5`: supportable operator beta and packaging.
- `0.8`: production-readiness beta for Core.
- `0.9`: 1.0 release candidate freeze.
- `1.0`: production-stable Core.

`press` and `bridge` may have preview tracks after Core supportability is
established, but they are not required for Sourcefold Core 1.0. Knowledge base
work and Translator migration remain post-1.0 or separate-product scope unless
a later charter changes the boundary.
