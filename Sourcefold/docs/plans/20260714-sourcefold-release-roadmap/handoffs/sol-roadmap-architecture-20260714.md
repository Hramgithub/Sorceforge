# Sol Release Roadmap Architecture Receipt

- Goal id: `20260714-sourcefold-release-roadmap`
- Step id: `R2`
- Role / model / effort: Sol analyst and architect / `gpt-5.6-sol` / high
- Timestamp: `2026-07-14T23:16:11+03:00`
- Elapsed time: approximately 12 minutes
- Token use: unavailable (exact telemetry was not exposed)

## Scope

Produce a high-level product roadmap from the accepted Sourcefold scaffold to
the first releasable Sourcefold candidate. The analysis covers product
boundaries, dependency order, branch and feedback behavior, durable data
contracts, release gates, risks, assumptions, and evidence required for a
release decision.

This was architecture-only work. No code was implemented; no source material
was processed; no legacy Translator plan or history was migrated; and no
canonical plan, context, project status, or release file was edited.

## Result

The recommended path is a contract-first, thin vertical release of the complete
core lane: `reconstruct -> translate -> proofread`. The first candidate should
prove that one declared source profile can move through all three stages with
artifact-level lineage, traceability, governed findings and waivers, explicit
human acceptance, and reproducible operator evidence.

Implementation should not start by completing one module in isolation. It
should first close the cross-cutting contract decisions identified by the
scaffold critique, then establish one validation/evidence spine shared by all
stages, and only then build the three core stages as successively accepted
capabilities. `press`, `bridge`, knowledge-base generation, and legacy
Translator compatibility are not part of the first release candidate.

## Files Checked

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`
- `Sourcefold/manifests/artifact_manifest.schema.json`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/context.md`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/handoffs/terra-engineering-critique-20260714.md`
- `docs/governance/nri_goal_governance.md`

The active goal plan was not inspected because it was not among the explicitly
authorized inspection paths. `PROJECT_STATUS.md` supplied the assigned goal
state and purpose.

## Recommended First Release Definition

Define the first release candidate as **Sourcefold Core 0.1 RC**, an
operator-run, versioned product that:

1. supports one explicitly declared, representative source-input profile;
2. runs the complete core lane and produces an Accepted Source Text, Faithful
   RU Draft, and Proofread RU Master;
3. makes each artifact immutable after creation and links it to immutable input
   identities, producing stage, run configuration, tool/model versions, QA
   evidence, and acceptance evidence;
4. preserves the source meaning, structure, mechanics, numbers, names, and
   traceability semantics required by the current acceptance criteria;
5. rejects invalid stage/type combinations, invalid predecessor states, open
   findings at acceptance, and incomplete waivers;
6. supports governed feedback to the producing or earlier stage without
   overwriting previously accepted evidence;
7. can be installed or invoked from a clean supported environment using
   documented commands and can revalidate a retained run without hidden state;
8. freezes a candidate revision and evidence manifest for independent Terra
   `release` review at high effort.

The RC is not a promise of broad document-format support, unattended semantic
acceptance, press-ready layout, destination export, knowledge-base generation,
or compatibility with Translator. Those are later product increments.

The release charter should choose the exact runtime and input profile before
implementation. A reasonable default is a local, command-driven workflow with
canonical structured Markdown plus machine-readable JSON evidence, but that is
an assumption to approve rather than an existing Sourcefold decision.

## Architectural Contracts To Close First

The current manifest is a useful vocabulary scaffold, but it cannot enforce the
prose contracts. Before stage implementation, define these shared contracts:

- **Artifact identity:** stable `artifact_id` plus mandatory content hash and
  manifest/schema version. A new content hash creates a new artifact identity
  or revision; accepted content is never modified in place.
- **Typed lineage:** each derived artifact references an upstream artifact id,
  artifact type, manifest hash, and acceptance record, not only a file path.
- **Valid DAG edges:** an explicit matrix of producer stage, output artifact
  type, and required accepted predecessor type. This is enforced by schema
  conditionals and/or a graph validator.
- **Trace anchors:** stable source/page/block/table-cell/card or stat-block
  anchors and a many-to-many mapping representation sufficient to trace
  translation and proofreading changes back to source evidence.
- **Finding record:** common id, category, severity, stage, affected anchors,
  evidence, status, resolution, and actor/time fields.
- **Waiver record:** authority, rationale, supporting evidence, scope, review
  or expiry policy, and the acceptance effect. Waiver is not synonymous with a
  passed QA signal.
- **Acceptance record:** artifact-scoped decision, actor, authority, time,
  rationale, evidence references, and policy version. Stage acceptance remains
  distinct from QA status, destination conformance, and product release.
- **Run record:** input identities, configuration, tool/model/provider
  versions, prompts or procedure versions where material, and generated
  artifact references. Secrets are referenced operationally, never persisted.
- **Terminology evidence:** decision id, chosen Russian term, source evidence,
  applicability, alternatives, and affected anchors/artifacts.
- **Release manifest:** frozen candidate revision or immutable manifest set,
  supported profile, exclusions, QA evidence, and independent release receipt.

These are shared product contracts, not internal details of a single module.

## Proposed Roadmap

### Phase 0 — Release Charter And Decision Closure

Purpose: turn the pending scaffold questions into explicit, versioned product
decisions before runtime work begins.

Deliverables:

- first-release scope, supported environment, source-input profile, canonical
  text/evidence formats, and intentional exclusions;
- decisions for identity, lineage, trace-anchor granularity, waiver authority,
  evidence vocabulary, stage/type pairs, predecessor rules, and schema
  evolution;
- one end-to-end representative pilot corpus and focused positive/negative
  contract fixtures;
- release acceptance matrix mapping current prose criteria to executable tests,
  operator checks, and human decisions.

Exit gate:

- every pending decision from the initial scaffold critique has an owner and an
  accepted resolution;
- no term named `accepted`, `passed`, `waived`, `conformant`, or `released` has
  overlapping authority;
- the release definition and supported profile are bounded enough to test.

### Phase 1 — Executable Contract And Evidence Spine

Purpose: implement the shared rules that all core stages depend upon before
implementing stage-specific transformations.

Deliverables:

- versioned schemas/records for artifacts, lineage, trace maps, findings,
  waivers, acceptance, terminology, runs, and release evidence;
- a validator for local schema rules and cross-artifact DAG rules;
- immutable artifact storage/naming policy and supersession behavior;
- fixture suite covering valid flows and forbidden states.

Exit gate:

- an artifact cannot be accepted with `not_run` or open-findings QA;
- a waiver without the required authority, rationale, scope, and evidence is
  rejected;
- every artifact type has one valid producer and declared predecessor rules;
- rejected, draft, or superseded upstream artifacts cannot satisfy downstream
  acceptance;
- mutation or hash mismatch is detected;
- positive and negative fixtures produce explainable, stable validator output.

### Phase 2 — Thin End-To-End Core Lane

Purpose: establish the smallest working product flow across all three core
modules instead of optimizing one stage before learning whether the contracts
compose.

Deliverables:

- bounded `reconstruct`, `translate`, and `proofread` stage interfaces using the
  shared contracts;
- one representative artifact progressing through all three stages;
- findings that can route work to the current stage or an earlier stage;
- explicit operator acceptance at every stage; no stage self-certifies semantic
  quality merely because checks ran.

Exit gate:

- the pilot produces all three named core artifacts and a valid evidence DAG;
- all downstream inputs are accepted upstream artifacts;
- every material output unit is traceable to source evidence;
- a deliberately injected source, translation, and proofreading defect is
  caught, routed, resolved or validly waived, and preserved in history;
- optional lanes are neither invoked nor required to claim core completion.

### Phase 3 — Quality Completion On The Supported Profile

Purpose: make the vertical slice satisfy the full accepted quality semantics,
not merely the happy-path interfaces.

Deliverables:

- coverage for reading order, headings, emphasis, quotes, lists, tables, cards,
  stat blocks, page markers, uncertain readings, numbers, dates, dice notation,
  mechanics, names, definitions, modality, conditions, negations, and Russian
  language quality where those features occur in the supported profile;
- terminology provenance and semantic/language finding separation;
- restart, partial rerun, supersession, and revalidation behavior;
- adversarial and regression fixtures derived from the release acceptance
  matrix.

Exit gate:

- every in-scope acceptance criterion has passing evidence or an explicit,
  release-visible exclusion;
- no unresolved core finding remains in the accepted pilot chain;
- rerunning a changed input creates a new lineage branch and does not silently
  reuse acceptance;
- model or tool variability is recorded as new run/artifact evidence rather
  than hidden behind a prior acceptance state.

### Phase 4 — Operator Product Hardening

Purpose: convert a validated pipeline into a product another qualified operator
can run and diagnose.

Deliverables:

- documented installation/invocation, configuration, supported environment,
  input/output layout, review workflow, failure recovery, and limitations;
- clean handling of credentials and provider failures;
- actionable errors for contract, lineage, QA, and stage failures;
- versioning and migration policy for schemas and retained manifests;
- smoke, integration, regression, and clean-environment acceptance procedures.

Exit gate:

- a qualified operator who did not build the candidate can execute the pilot
  from documented inputs, locate evidence, resume after a controlled failure,
  and explain why each artifact is or is not accepted;
- retained artifacts revalidate against their declared schema/policy versions;
- the product emits no undocumented state required to reproduce or audit the
  run;
- all release-blocking tests pass on the declared supported environment.

### Phase 5 — Candidate Freeze And Independent Release Gate

Purpose: freeze evidence and obtain the independent decision required by NRI
governance.

Deliverables:

- frozen candidate revision or SHA-256 manifest set and freeze timestamp;
- release evidence package with test results, accepted pilot chain, known
  limitations, intentional exclusions, and participation declaration;
- independent `gpt-5.6-terra` high-effort `release` review by a critic who did
  not implement or materially design the candidate.

Exit gate:

- no unresolved release-blocking finding;
- every claimed capability is backed by candidate-bound evidence;
- Terra recommends release for the exact frozen candidate;
- any candidate mutation invalidates the receipt and triggers a new freeze and
  release review.

Sol's roadmap is architecture input, not a release approval.

## Dependency And Branching Model

Critical dependency chain:

```text
release charter and semantic decisions
  -> executable shared contracts and validators
  -> reconstruct accepted artifact capability
  -> translate accepted artifact capability
  -> proofread accepted artifact capability
  -> end-to-end quality completion
  -> operator hardening
  -> candidate freeze
  -> independent Terra release review
```

Cross-cutting fixture, documentation, and security work can proceed alongside
stage work only after its controlling contract is stable. Stage work may be
developed in parallel at interface level, but an accepted downstream artifact
cannot exist before its required predecessor is accepted.

Required branches:

- a reconstruct finding returns to source evidence interpretation or
  reconstruction and supersedes affected descendants after correction;
- a translation finding returns to translation unless it exposes a source-text
  defect, in which case it returns to reconstruct and invalidates descendants;
- a proofreading finding returns to proofreading unless it exposes semantic or
  source drift, in which case it returns to translate or reconstruct;
- a waiver branch may continue only under the approved waiver policy and must
  remain visible to downstream acceptance and release review;
- a contract/schema change either preserves declared backward validation or
  creates a new version with explicit migration/revalidation behavior;
- a release-review finding reopens the appropriate phase; a changed candidate
  must be refrozen and independently reviewed again.

## Acceptance Criteria For The Roadmap

The roadmap is ready for orchestration when:

- the orchestrator can assign each phase without inventing missing upstream
  decisions;
- each phase has candidate-bound evidence and an objective exit gate;
- core module dependencies and backward QA routes are explicit;
- data exchanged across stages has stable identities, lineage, anchors, and
  acceptance semantics;
- release scope is bounded to the core product and one supported profile;
- optional lanes and legacy material cannot satisfy or dilute a core gate;
- final release authority remains with an independent Terra `release` review.

## Risks And Assumptions

### Principal Risks

1. **Release ambiguity:** runtime, input class, canonical artifact format, and
   supported operating environment are not yet declared. Without Phase 0,
   implementation can be locally successful but not releasable.
2. **False acceptance:** the current schema permits contradictory QA and
   acceptance states. Human authority and machine preconditions must both be
   explicit.
3. **Unprovable lineage:** path-only references cannot prove derivation or
   detect stale downstream acceptance.
4. **Traceability cost explosion:** anchor granularity that is too coarse fails
   auditability; granularity that is too fine can dominate implementation and
   review effort. The supported source profile must drive the minimum.
5. **Model/provider variability:** semantic output may not be byte-stable.
   Reproducibility must mean explicit inputs, versions, configuration, identity,
   and history—not a false promise of identical stochastic output.
6. **Fixture optimism:** one happy-path document can conceal failures in tables,
   stat blocks, ambiguity, and many-to-many mappings. Focused adversarial
   fixtures are required in addition to the pilot.
7. **Scope creep:** `press`, `bridge`, knowledge bases, broad format support,
   and Translator compatibility can delay proof of the core promise.
8. **Schema lock-in:** root `additionalProperties: false` is useful for control
   but requires an explicit evolution/extension policy before optional lanes or
   new evidence fields emerge.
9. **Release independence:** Sol materially designed this roadmap and therefore
   must not act as the final release reviewer for the resulting candidate.

### Working Assumptions Requiring Orchestrator Approval

- Core 0.1 RC contains `reconstruct`, `translate`, and `proofread` only.
- Acceptance is an explicit human decision constrained by machine validation;
  automation may recommend but does not confer semantic acceptance.
- The first release supports one declared source profile rather than arbitrary
  PDFs and document structures.
- Structured Markdown is the likely canonical text carrier and JSON the likely
  evidence carrier, but Phase 0 must ratify or replace this choice.
- The first release is a local operator workflow on one declared NRI-supported
  environment; broader platform support is a later claim.
- Existing Translator code, plans, history, prompts, and runtime contracts are
  neither migrated nor accepted as compatibility requirements.

## Verification / Evidence

- The product boundary consistently identifies the three core modules and keeps
  `press` and `bridge` optional.
- The module contract defines an accepted-artifact DAG with backward QA routes;
  the roadmap preserves both properties.
- The acceptance criteria supply the semantic and structural quality matrix
  used in Phases 2 and 3.
- The current manifest vocabulary covers stages and artifact types but does not
  enforce valid combinations, predecessor acceptance, internally consistent
  QA/acceptance, artifact-level lineage, or waiver evidence. Phase 0 and Phase
  1 directly remediate those gaps.
- The initial context and Terra critique independently identify the same
  pre-implementation decisions addressed by the contract-first sequence.
- NRI governance requires candidate freeze and independent Terra `release`
  review; Phase 5 keeps release state separate from stage acceptance.
- Only the authorized evidence paths were read. No code or unrelated project
  area was inspected.

## Changed Files

- `Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/handoffs/sol-roadmap-architecture-20260714.md`
  (new immutable handoff receipt)

No canonical plan, context, project status, release file, code, schema, or
legacy artifact was changed.

## Blockers

None to completing this architecture handoff.

Implementation should remain gated until Phase 0 resolves the supported input
profile and environment, artifact identity/lineage, trace anchors, stage/type
and predecessor rules, waiver authority, evidence vocabulary, acceptance
authority, and schema evolution policy.

## Next Action

The orchestrator should incorporate this roadmap into the canonical goal state,
choose owners for Phase 0 decisions, and commission a bounded contract decision
specification. After those decisions are accepted, an engineering owner can
specify the executable validation/evidence spine; Sol should not approve the
final candidate, and independent Terra `release` review remains mandatory.
