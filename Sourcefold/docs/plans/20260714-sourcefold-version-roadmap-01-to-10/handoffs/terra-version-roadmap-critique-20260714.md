# Terra Version Roadmap Critique — V3

## Receipt

- **Goal id:** `20260714-sourcefold-version-roadmap-01-to-10`
- **Step id:** `V3`
- **Role / model / effort:** Engineering critic / Terra / medium
- **Timestamp:** `2026-07-14T23:37:48+03:00`
- **Scope:** Critique the prospective path from Sourcefold Core 0.1 RC through
  Sourcefold 1.0 against the assigned product boundary, module contracts, and
  acceptance criteria. No code, canonical planning/status, or product files
  were changed.

## Files Checked

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/roadmap.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`

## Critical Critique Of The Version Ladder

The defensible ladder is capability maturity of one governed core lane, not a
calendar of increasingly broad product labels. The proposed 0.1 RC boundary is
sound only if it is interpreted as one declared input profile and structure
subset, one repeatable pilot chain, and explicit human acceptance. It is not
evidence that Sourcefold can process arbitrary PDFs, books, layouts, providers,
or publishing destinations.

Primary risks of false confidence:

1. **A three-module happy path can be mistaken for production.** A pilot proves
   composition, not reliability. Production claims require adversarial and
   regression fixtures, restart/revalidation behaviour, changed-input lineage,
   and clean-operator evidence across the declared profile.
2. **The quality list is wider than a thin slice.** The acceptance criteria span
   complex structures, uncertain OCR, mechanics, modality, negation,
   terminology provenance, and Russian editorial quality. A release may exclude
   a feature only when the charter names the exclusion and tests enforce that
   it is rejected rather than silently degraded.
3. **Acceptance semantics can collapse into workflow labels.** `accepted`,
   `passed`, `waived`, `conformant`, and `released` must remain separately
   modeled. Otherwise an automated check, a waived finding, or a downstream
   render can be misrepresented as human acceptance of text truth.
4. **Lineage integrity is the first production dependency.** Hashing alone is
   inadequate unless artifact identity, supersession, trace anchors, valid DAG
   edges, release evidence, and mutation invalidation are executable and
   inspectable. A regenerated artifact must never inherit acceptance implicitly.
5. **Optional lanes invite scope substitution.** `press` can make an unaccepted
   master look finished; `bridge` can normalize loss into a destination; KB and
   Translator migration can create an apparent ecosystem before Core has a
   stable contract. None proves missing core acceptance.

The permitted review set did not include the referenced
`version_roadmap.md`. Consequently, no specific proposed version labels,
dates, or per-version scope have been validated; this receipt critiques only
the governing roadmap and limits supplied in scope.

## Recommended Minimum Production Boundary

Call Sourcefold **1.0 production** only when the core lane, for explicitly
declared source profiles and structure subsets, is operator-repeatable and
candidate-auditable:

- immutable source evidence produces accepted Source Text, Faithful RU Draft,
  and Proofread RU Master through enforced stage/type/predecessor rules;
- all accepted artifacts expose identity, hashes, trace anchors, lineage,
  tool/model versions, findings, waivers, QA state, and explicit acceptance;
- acceptance rejects unresolved findings and malformed or unauthorized waiver
  evidence, and downstream work consumes accepted upstream artifacts only;
- representative, negative, adversarial, regression, restart, partial-rerun,
  supersession, and revalidation checks pass for every in-scope criterion;
- a qualified independent operator reproduces the pilot from documented inputs
  in a clean environment, diagnoses controlled failures, and resumes without
  undocumented state;
- a frozen candidate package binds every claim and known limitation to evidence
  and receives an independent Terra high-effort release review.

This is a production boundary for Core, not a promise of universal document
reconstruction or a general publishing/knowledge platform.

## Non-Goals Until After 1.0

- `press` as a release dependency, layout repair path, or source of text
  acceptance;
- `bridge` destinations, catalogue breadth, or lossy export normalization;
- knowledge-base generation, cross-book rule systems, and unified reference
  behavior;
- Translator compatibility, migration, runtime namespace, package prompts,
  history, or file-structure adoption;
- general PDF/OCR, arbitrary language pairs, arbitrary source layouts, UI,
  multi-user workflow, hosted service operation, or provider-specific promises
  not proven by the production charter;
- version labels whose sole difference is a demo, a new integration, or a
  cosmetic output format without independently accepted core evidence.

## Validation Gates By Release Band

| Release band | Required gate | Must not be claimed |
|---|---|---|
| 0.1 RC | One declared profile; executable contracts; valid core pilot DAG; injected defects caught; explicit per-stage acceptance; frozen reviewable candidate. | General reconstruction, autonomous acceptance, publishing, integrations, or migration. |
| 0.2–0.x | Each added profile/structure is explicitly chartered; rejection behavior, adversarial/regression fixtures, and revalidation evidence cover it; clean operator run remains repeatable. | That coverage extends to unchartered profiles or that optional lanes cure core defects. |
| 1.0 candidate | All in-scope criteria have evidence; restart/partial rerun/supersession controls work; docs and failure recovery are independently exercised; limitations are candidate-bound. | “Production” based on cumulative feature count, successful demos, or an implementer-only run. |
| 1.0 production | Exact frozen candidate passes all core gates and independent Terra high-effort release review; mutation invalidates the receipt. | A final release decision from this critique or a blanket claim beyond the stated charter. |

## Version-Inflation Warnings

- Do not treat each new artifact format, model/provider, or document sample as
  a minor version without evidence that it preserves the same acceptance and
  lineage semantics.
- Do not use 1.0 to mean “feature-complete.” It should mean a bounded Core
  promise is durable, reproducible, auditable, and supportable.
- Do not bundle expansion of source-profile coverage with `press`, `bridge`,
  KB, or Translator work; independent axes conceal which claim has actually
  been validated.
- Avoid release-band advancement when a prior gate is waived for schedule
  reasons. A waiver must be narrow, authorized, evidenced, and visible in the
  candidate limitation set; it is not silent debt retirement.

## Changed Files

- Added this immutable handoff receipt only:
  `Sourcefold/docs/plans/20260714-sourcefold-version-roadmap-01-to-10/handoffs/terra-version-roadmap-critique-20260714.md`.

## Blockers

- The actual prospective `version_roadmap.md` was referenced by project status
  but was outside the explicitly permitted inspection paths. Review of precise
  version-by-version commitments remains pending until that document is placed
  in scope.
- Phase 0 decisions remain unresolved: supported profile, canonical formats,
  identity/lineage/trace semantics, waiver authority, acceptance authority,
  and acceptance vocabulary.

## Next Action

Have the orchestrator compare the actual version ladder against this minimum
boundary, remove or defer any optional-lane and migration commitments, then
route the resulting 1.0 candidate definition to independent Terra high-effort
release review when a frozen candidate exists. This is not a release decision.

## Token Use

Unavailable: exact telemetry is not exposed to this delegated review.
