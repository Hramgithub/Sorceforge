# Sourcefold Release Roadmap

Goal id: `20260714-sourcefold-release-roadmap`

Status: draft for user decision

Date: 2026-07-14

## Recommendation

Build Sourcefold toward **Sourcefold Core 0.1 RC**: a headless, operator-run,
fixture-backed product release that proves the full core lane:

```text
reconstruct -> translate -> proofread
```

The first release should prove text truth and accepted Russian master handling
for one declared source profile and supported structure subset. It should not
promise universal PDF/OCR support, publishing output, external integrations,
knowledge base generation, UI, or Translator compatibility.

The main risk is not that one module is under-detailed. The main risk is that
the product starts producing plausible artifacts before it can prove acceptance,
lineage, traceability, and release state.

## Release Definition

Sourcefold Core 0.1 RC is releasable when it can:

- accept immutable source evidence for one declared input profile;
- produce Accepted Source Text, Faithful RU Draft, and Proofread RU Master;
- keep artifact identity, hashes, lineage, trace anchors, findings, waivers,
  QA state, and acceptance evidence inspectable;
- reject invalid stage/type combinations and invalid predecessor states;
- reject acceptance with open findings or incomplete waiver evidence;
- preserve meaning, structure, mechanics, numbers, names, and source
  traceability inside the declared scope;
- rerun or revalidate retained fixtures without hidden state;
- freeze a candidate revision/evidence package for independent Terra release
  review.

## Non-Goals For First Release

- `press` rendering as a release blocker.
- `bridge` exports.
- Knowledge base generation or cross-book rule integration.
- General PDF/OCR reconstruction claims.
- Full UI, multi-user workflow, or destination catalogue.
- Translator compatibility, migration, package prompts, or historical plan
  adoption.

## Phase 0: Release Charter And Contract Decisions

Purpose: decide what the first release is allowed to mean before implementation
starts.

Deliverables:

- first-release charter: supported environment, input profile, language pair,
  canonical text/evidence formats, and exclusions;
- accepted decisions for artifact identity, lineage, trace anchors, valid DAG
  edges, waiver policy, acceptance authority, evidence vocabulary, and schema
  evolution;
- fixture strategy: one representative pilot plus focused positive/negative
  contract fixtures;
- release acceptance matrix mapping acceptance criteria to tests, operator
  checks, and human decisions.

Exit gate:

- every Terra scaffold decision has an accepted owner/resolution;
- `accepted`, `passed`, `waived`, `conformant`, and `released` have distinct
  meanings;
- implementation is bounded to a testable first release.

## Phase 1: Executable Contract And Evidence Spine

Purpose: make shared product invariants executable before module work.

Deliverables:

- schemas/records for artifacts, lineage, trace maps, findings, waivers,
  acceptance, terminology, runs, and release evidence;
- graph/evidence validator for stage/type/predecessor rules;
- immutable artifact naming and supersession policy;
- positive and negative fixture suite.

Exit gate:

- invalid acceptance states are rejected;
- invalid waivers are rejected;
- invalid stage/type/predecessor combinations are rejected;
- mutation or hash mismatch is detected;
- validator output is stable and explainable.

## Phase 2: Thin End-To-End Core Lane

Purpose: prove that all three core modules compose through the shared contracts.

Deliverables:

- minimal `reconstruct`, `translate`, and `proofread` interfaces;
- one artifact chain through Accepted Source Text, Faithful RU Draft, and
  Proofread RU Master;
- findings that can route work back to the current or earlier stage;
- explicit operator acceptance at every stage.

Exit gate:

- pilot produces all three artifacts and a valid evidence DAG;
- every downstream input is an accepted upstream artifact;
- material output claims trace back to source evidence;
- injected source, translation, and proofreading defects are caught and handled.

## Phase 3: Quality Completion On Supported Profile

Purpose: make the vertical slice satisfy quality semantics, not only interface
shape.

Deliverables:

- coverage for the declared structure subset: reading order, headings,
  emphasis, quotes, lists, tables, cards/stat blocks, page markers, uncertain
  readings, numbers, dates, dice, mechanics, names, definitions, modality,
  conditions, negations, terminology, and Russian language quality as
  applicable;
- restart, partial rerun, supersession, and revalidation behavior;
- regression and adversarial fixtures from the acceptance matrix.

Exit gate:

- every in-scope acceptance criterion has evidence or an explicit exclusion;
- no unresolved core finding remains in the accepted pilot chain;
- changed inputs create new lineage rather than silently reusing acceptance.

## Phase 4: Operator Product Hardening

Purpose: make the validated pipeline usable and diagnosable by someone other
than the implementer.

Deliverables:

- documented installation/invocation, configuration, input/output layout,
  review workflow, failure recovery, and limitations;
- clean credential/provider handling;
- actionable errors for contract, lineage, QA, and stage failures;
- schema versioning and migration/revalidation policy;
- smoke, integration, regression, and clean-environment checks.

Exit gate:

- a qualified operator can run the pilot from documented inputs;
- evidence can be located and explained;
- controlled failure/resume works;
- no undocumented state is required for audit or reproduction.

## Phase 5: Candidate Freeze And Release Review

Purpose: make a release decision against one frozen candidate, not a moving
workspace.

Deliverables:

- frozen revision or SHA-256 manifest set;
- release evidence package with tests, accepted pilot chain, known limitations,
  exclusions, and participation declaration;
- independent Terra high-effort `release` review.

Exit gate:

- no unresolved release-blocking finding;
- every claimed capability is backed by candidate-bound evidence;
- Terra recommends release for the exact frozen candidate;
- any candidate mutation invalidates the receipt and requires a new freeze.

## Recommended Next Goal

Start Phase 0 as the next bundled goal:

```text
20260714-sourcefold-phase-0-release-charter
```

Expected output:

- a release charter;
- contract decision log;
- accepted identity/lineage/anchor/waiver/acceptance vocabulary;
- first fixture strategy;
- release acceptance matrix.

Do not implement module code before Phase 0 is accepted.

## Open User Decisions

- Is the first release boundary accepted as headless Sourcefold Core 0.1 RC?
- Which source profile should the first release support?
- Should canonical text be structured Markdown and evidence be JSON, or should
  Phase 0 evaluate alternatives?
- Is human acceptance mandatory at every core stage in 0.1, with automation only
  constraining or recommending acceptance?
- Should `press` remain completely outside 0.1, or should a Markdown projection
  be allowed as a non-release-blocking demo artifact?
