# Terra Roadmap Risk Critique Receipt

- Goal id: `20260714-sourcefold-release-roadmap`
- Step id: `R3`
- Role / model / effort: Terra engineering critic / `gpt-5.6-terra` / medium
- Timestamp: `2026-07-14T23:15:53+03:00`
- Elapsed time: approximately 5 minutes
- Token use: unavailable (exact telemetry was not exposed)

## Scope

Read-only engineering critique of the route from Sourcefold's documentation and
schema scaffold to a first releasable product. This receipt challenges roadmap
assumptions and identifies decisions and gates required before implementation.
No code, migration, real-book processing, canonical plan/context/status edit,
or release decision was performed.

## Result

The scaffold is a valid planning baseline, but it is not yet an implementable
product contract. A roadmap that starts building the three core modules before
locking acceptance semantics, lineage, and evidence validation will create
plausible-looking outputs that cannot demonstrate the product's central claim:
that an accepted RU master preserves traceable source truth. Treat those items
as a single contract-design milestone, not as later QA polish.

## Files Checked

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`
- `Sourcefold/manifests/artifact_manifest.schema.json`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/context.md`
- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/handoffs/terra-engineering-critique-20260714.md`
- `docs/governance/nri_goal_governance.md`

## Critical Risks

1. **Acceptance is structurally unenforceable.** The schema permits an
   `accepted` artifact with `qa: not_run`, `open_findings`, no acceptance
   actor/time/evidence, and finding references still marked `open`. This
   directly conflicts with the contracts and acceptance criteria. If module
   implementation begins now, every producer and consumer will have to invent
   its own interpretation, making later convergence a migration.

2. **Lineage cannot prove a core-stage claim.** `inputs` and `outputs` are
   file paths with optional hashes, not typed upstream artifact references or
   traceability anchors. The roadmap must decide how a proofread RU master
   proves derivation from a particular accepted source text, including
   many-to-many mapping for reorganized prose, tables, cards, and stat blocks.
   A file hash alone does not supply that semantic relation.

3. **The governed DAG is not executable.** The schema accepts every declared
   artifact type at every producing stage and names no required accepted
   predecessor. A command can therefore emit a `proofread_ru_master` without a
   faithful draft, while still passing JSON syntax checks. Valid
   stage/type/predecessor rules need an explicit validation specification;
   JSON Schema alone may be insufficient for cross-manifest graph validation.

4. **Evidence objects are referenced but undefined.** Ledgers, terminology
   provenance, uncertain readings, findings, waiver rationale, and acceptance
   evidence are required by prose but lack stable identifiers, minimal fields,
   storage location, and referential-integrity rules. A rushed pilot will
   otherwise bind the external API to whatever one book happened to need.

5. **“Release” remains overloaded.** Stage acceptance, press/bridge destination
   conformance, a reusable-product release candidate, and NRI release approval
   are separate states. The roadmap must not use accepted core text or a
   successful rendered sample as evidence that Sourcefold itself is releasable.
   Per governance, a frozen candidate additionally requires an independent
   Terra `release` review; this R3 critique is not that review.

6. **A broad first pilot will conceal an unbounded product.** The stated
   reconstruction criteria include complex structures and optional press/
   bridge lanes. Choosing a full rulebook, PDFs with heavy layout damage, or
   multiple source classes as the first implementation target will conflate OCR
   quality, structural parsing, translation workflow, proofing, rendering, and
   integration. A single successful artifact would not establish product
   repeatability.

## Sequencing Warnings

1. Decide the shared contract before module code: identity model; valid
   stage/artifact pairs; accepted predecessor rule; evidence and finding IDs;
   traceability-anchor granularity; waiver authority and lifecycle; and the
   distinction among QA, stage acceptance, destination conformance, and release.
2. Convert those decisions into a versioned contract plus validator behavior
   and adversarial fixtures. Include invalid acceptance, open/waived findings,
   wrong predecessor, changed input hash, missing anchor, and valid happy-path
   cases. Do not make a real-book pilot the first validator.
3. Implement only the thin core path against fixtures: reconstruct -> translate
   -> proofread, with manifests, evidence references, lineage validation, and
   deterministic rejection of invalid transitions.
4. Run one deliberately bounded pilot only after the thin path is proven.
   Capture operational gaps as new requirements; do not silently generalize
   the core contract from exceptions.
5. Freeze a candidate only after repeatability evidence, documented known
   limitations, and candidate QA. Then obtain the separate independent Terra
   release review required by governance.

## Missing Gates

- **Contract decision gate:** named owner records the six shared decisions in
  canonical roadmap artifacts before implementation authorization.
- **Machine-validation gate:** schema plus graph/evidence validator has passing
  and failing fixtures for every core transition; JSON parsing is not enough.
- **Traceability gate:** a reviewer can navigate an accepted output claim back
  to a bounded source anchor and its evidence, including at least one complex
  structure supported by the initial scope.
- **Repeatability gate:** the same fixture set reruns without untracked manual
  changes and produces inspectable lineage/evidence.
- **Pilot-scope gate:** one source class, one input shape, language pair,
  supported structure subset, and explicit unsupported cases are declared.
- **Candidate-freeze gate:** release candidate revision or SHA-256 manifest,
  QA evidence, intentional exclusions, and participant declaration exist
  before an independent `release` review is requested.

## Scope-Creep Warnings

- Do not start `press` or `bridge` in the first product release. They are
  optional lanes and will multiply contracts before core acceptance is proven.
- Do not include knowledge-base generation, cross-book rule integration, or a
  compatibility/migration layer for `translator`; all are explicitly outside
  ordinary Sourcefold processing.
- Do not promise general PDF/OCR reconstruction. The first release should name
  its supported source class and structural subset instead of inheriting every
  layout type listed as a long-term quality criterion.
- Do not build a full UI, multi-user workflow, or destination catalogue before
  the artifact/evidence validator establishes the core product invariant.

## Recommended Minimal Release Boundary

A first releasable Sourcefold should be a fixture-backed, headless core-lane
reference implementation for one declared source class and a narrow supported
structure subset. It should accept immutable source evidence, produce and
validate the three core artifact states (`accepted_source_text`,
`faithful_ru_draft`, `proofread_ru_master`), preserve typed lineage and bounded
traceability anchors, require explicit findings/waivers/acceptance evidence,
and reject invalid state transitions. One small bounded pilot may demonstrate
the same flow, but it must not broaden the supported claim. `press`, `bridge`,
knowledge bases, cross-book systems, and legacy migration stay excluded.

This boundary is intentionally a product-contract release, not a promise of
universal document reconstruction or final publishing output.

## Changed Files

- `Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/handoffs/terra-roadmap-risk-critique-20260714.md` (new immutable handoff receipt)

## Verification / Evidence

- All assigned artifacts were read; no forbidden project trees were inspected.
- Product boundary, module flow, acceptance criteria, project status, and the
  earlier Terra critique consistently identify acceptance semantics, lineage,
  valid stage/artifact pairs, waiver evidence, and shared vocabulary as pending
  implementation prerequisites.
- The manifest was inspected as JSON Schema text; its allowed state
  combinations demonstrate the listed enforcement gaps. No implementation or
  schema validation run was performed because this is a roadmap critique.

## Blockers

No blocker prevents roadmap drafting. Implementation should remain gated until
the contract-decision gate is explicitly resolved by the orchestrator and the
architecture owner.

## Next Action

The orchestrator should turn the six contract decisions and the minimal release
boundary into the canonical roadmap's first implementation milestone, assign
architecture ownership, and request a separate implementation specification
before any module build begins.
