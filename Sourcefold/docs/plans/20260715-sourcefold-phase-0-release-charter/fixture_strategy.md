# Fixture Strategy

Status: draft updated by Gate 1 Step 9; no executable fixtures created

## Purpose

Fixtures prove that Sourcefold Core 0.1 enforces contracts before real book
processing begins.

## Canonical Fixture Index

This is the canonical fixture ID source for Gate 1 Step 9. Roadmap, matrix,
and protocol references must use these IDs exactly. Historical roadmap aliases
must be reconciled before they can count as fixture coverage.

| Fixture ID | Type | Gate Steps | Criteria | Expected Result | Expected Failure Class | Expected Blocker | Status |
|---|---|---|---|---|---|---|---|
| `fixture-positive-0.1` | positive | Core 0.1 lane | AM-02-01, AM-02-02, AM-03-01, AM-07-01, AM-08-01, AM-08-02, AM-09-01, AM-G1-07 | future pass after bounded execution | n/a | n/a | declared, not created |
| `fixture-valid-human-acceptance` | positive | 8,10 | AM-09-02, AM-10-01, AM-G1-07, AM-G1-08 | future pass after bounded execution | n/a | n/a | declared, not created |
| `fixture-protocol-authority-lock` | negative | 1,2,3 | AM-G1-01, AM-G1-07, AM-10-02 | blocked | `missing_protocol_or_authority` | block bounded trial authorization | declared, not created |
| `fixture-permission-state-missing` | negative | 1,2,3 | AM-G1-01, AM-G1-07, AM-10-02 | blocked | `missing_or_invalid_permission_state` | block bounded trial authorization | declared, not created |
| `fixture-decision-state-missing` | negative | 1,2,3 | AM-G1-01, AM-G1-07, AM-10-02 | blocked | `missing_or_invalid_decision_state` | block bounded trial authorization | declared, not created |
| `fixture-evidence-state-missing` | negative | 1,2,3 | AM-G1-01, AM-G1-07, AM-10-02 | blocked | `missing_or_invalid_evidence_state` | block bounded trial authorization | declared, not created |
| `fixture-finding-state-missing` | negative | 1,2,3 | AM-G1-01, AM-G1-07, AM-10-02 | blocked | `missing_or_invalid_finding_state` | block bounded trial authorization | declared, not created |
| `fixture-unsupported-profile` | negative | 1,2,4 | AM-G1-01, AM-G1-02, AM-02-01, AM-G1-07, AM-10-02 | blocked | `unsupported_source_profile` | block intake acceptance | declared, not created |
| `fixture-bad-edge` | negative | 1,2,3 | AM-G1-01, AM-G1-07, AM-10-02 | blocked | `invalid_stage_artifact_edge` | block bounded trial authorization | declared, not created |
| `fixture-unauthorized-intake-metadata` | negative | 4 | AM-G1-02, AM-G1-07, AM-10-02 | blocked | `unauthorized_intake_metadata` | block intake acceptance | declared, not created |
| `fixture-stale-intake-metadata` | negative | 4 | AM-G1-02, AM-G1-07, AM-10-02 | blocked | `stale_intake_metadata` | block intake acceptance | declared, not created |
| `fixture-render-lineage-stale` | negative | 5 | AM-G1-03, AM-02-02, AM-04-01, AM-G1-07, AM-10-02 | blocked | `stale_or_incomplete_render_lineage` | block render evidence acceptance | declared, not created |
| `fixture-stale-lineage` | negative | 5,6,7,8 | AM-G1-03, AM-G1-04, AM-G1-05, AM-G1-06, AM-03-03, AM-04-02, AM-07-01, AM-08-01, AM-09-01, AM-10-01, AM-G1-07, AM-10-02 | blocked | `stale_lineage` | block stale-lineage acceptance | declared, not created |
| `fixture-missing-region` | negative | 6,8 | AM-G1-04, AM-G1-06, AM-03-02, AM-03-03, AM-03-04, AM-05-01, AM-06-01, AM-G1-07, AM-10-02 | blocked | `missing_text_bearing_region` | block source acceptance | declared, not created |
| `fixture-column-order` | negative | 6,8 | AM-G1-04, AM-G1-06, AM-03-01, AM-03-03, AM-06-01, AM-06-02, AM-G1-07, AM-10-02 | blocked | `ambiguous_or_wrong_reading_order` | block source acceptance | declared, not created |
| `fixture-map-payload-leakage` | negative | 6 | AM-G1-04, AM-G1-07, AM-10-02 | blocked | `prohibited_map_payload` | block map bundle acceptance | declared, not created |
| `fixture-overlay-failure` | negative | 6,8 | AM-G1-04, AM-G1-06, AM-07-02, AM-G1-07, AM-10-02 | blocked | `overlay_or_clipping_risk` | block source acceptance | declared, not created |
| `fixture-unclassified-block` | negative | 6,8 | AM-G1-04, AM-G1-06, AM-03-02, AM-03-04, AM-07-03, AM-G1-07, AM-10-02 | blocked | `unsupported_or_unclassified_structure` | block source acceptance | declared, not created |
| `fixture-ocr-discrepancy` | negative | 7 | AM-G1-05, AM-04-01, AM-04-02, AM-05-01, AM-G1-07, AM-10-02 | blocked | `ocr_source_discrepancy` | block OCR evidence acceptance | declared, not created |
| `fixture-text-layer-leakage` | negative | 7 | AM-G1-05, AM-05-02, AM-G1-07, AM-10-02 | blocked | `pdf_text_layer_payload_leakage` | block OCR evidence acceptance | declared, not created |
| `fixture-invalid-waiver` | negative | 8 | AM-G1-06, AM-G1-07, AM-10-02 | blocked | `invalid_waiver` | block Accepted Source Text | declared, not created |
| `fixture-open-finding` | negative | 8 | AM-G1-06, AM-06-02, AM-08-02, AM-09-02, AM-G1-07, AM-10-02 | blocked | `open_blocking_finding` | block Accepted Source Text | declared, not created |
| `fixture-missing-qa-coverage` | negative | 8 | AM-G1-06, AM-07-02, AM-G1-07, AM-10-02 | blocked | `missing_qa_coverage` | block Accepted Source Text | declared, not created |
| `fixture-parking-bypass` | negative | 8 | AM-G1-06, AM-G1-07, AM-10-02 | blocked | `parking_bypasses_non_waivable` | block Accepted Source Text | declared, not created |
| `fixture-empty-ledger` | negative | 8 | AM-G1-06, AM-07-02, AM-G1-07, AM-10-02 | blocked | `empty_finding_ledger_without_coverage` | block Accepted Source Text | declared, not created |

Empty, wildcard, placeholder, missing, or non-existent fixture IDs, criteria,
failure classes, or blockers do not count as coverage. A negative fixture that
fails for any reason other than its exact expected failure class and blocker
does not satisfy the acceptance criterion.

## Gate 1 Step Coverage

Step 9 only maps fixture obligations to the Gate 1 protocol. It does not create
fixture directories, fixture manifests, source files, page images, OCR output,
QA ledgers, or expected results.

| Gate 1 Step | Fixture Obligation | Canonical Fixture IDs |
|---|---|---|
| Steps 1-3 protocol/authority | prove accepted protocol, authority, permission, decision, evidence, and finding-state prerequisites before candidate-derived work | `fixture-protocol-authority-lock`, `fixture-permission-state-missing`, `fixture-decision-state-missing`, `fixture-evidence-state-missing`, `fixture-finding-state-missing`, `fixture-unsupported-profile`, `fixture-bad-edge` |
| Step 4 candidate intake | prove intake rejects unsupported profile, unauthorized metadata, and stale metadata | `fixture-unsupported-profile`, `fixture-unauthorized-intake-metadata`, `fixture-stale-intake-metadata` |
| Step 5 render benchmark | prove render outputs require frozen candidate manifest, comparison plan, output lineage, and stale behavior | `fixture-render-lineage-stale`, `fixture-stale-lineage` |
| Step 6 pre-OCR map | prove doc/content/art maps share identity and cannot contain OCR/text-layer/translation payloads | `fixture-missing-region`, `fixture-column-order`, `fixture-map-payload-leakage`, `fixture-overlay-failure`, `fixture-unclassified-block`, `fixture-stale-lineage` |
| Step 7 OCR benchmark | prove OCR candidates require frozen manifest, gold sample, scoring plan, text-layer containment, and output lineage | `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-stale-lineage` |
| Step 8 QA findings | prove coverage manifest, finding ledger, non-waivable findings, waiver/parking boundaries, and acceptance predicate | `fixture-open-finding`, `fixture-missing-qa-coverage`, `fixture-empty-ledger`, `fixture-parking-bypass`, `fixture-invalid-waiver`, `fixture-stale-lineage` |
| Step 8 page-complete readiness | prove page readiness cannot substitute for page-complete acceptance, cannot use unauthorized OCR/PDF text-layer work, and cannot hide missing regions, ambiguous reading order, overlay/clipping, unclassified blocks, missing QA coverage, or stale lineage behind advisory percentages | `fixture-missing-region`, `fixture-column-order`, `fixture-overlay-failure`, `fixture-unclassified-block`, `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-missing-qa-coverage`, `fixture-stale-lineage` |
| Core reconstruct -> translate -> proofread | prove accepted source, RU draft, and RU master require exact predecessor lineage | `fixture-positive-0.1`, `fixture-valid-human-acceptance` |

## Provenance Requirements

Every fixture must record:

- fixture id, fixture type, and protocol revision under test;
- expected acceptance matrix criteria;
- fixture manifest schema version;
- source rights or redaction status;
- immutable input hashes when the fixture is authorized and created;
- expected artifact ids or id pattern;
- deterministic run inputs/configuration;
- expected findings and closure state;
- expected pass/fail reason.

Negative fixtures must also record the exact non-waivable failure class, the
expected blocker, and the acceptance criterion that must remain locked.

## Positive Fixture Requirements

The first positive fixture should include:

- one immutable PDF with 8-20 selected pages;
- page screenshots/images as working evidence;
- at least one bounded two-column page;
- headings;
- paragraphs;
- emphasis;
- list;
- simple table or structured block;
- boxed/callout/sidebar/stat-block-like RPG structure where available;
- terms/names/numbers that must not drift;
- at least one traceable translation unit;
- one proofreading correction that must not change source meaning.

## Fixture Format

Proposed:

```text
fixtures/core-0.1/<fixture-id>/
  source/
  expected/
  manifest.json
  README.md
```

No real book fixture is selected in this charter draft. Fixture selection
requires user approval and, for candidate-derived fixture work, a separate
bounded authorization naming the exact action. The committed `Вирал` candidate
PDF is not a fixture and must not be converted into one by Step 9.

## Step 9 Fixture Boundary

Step 9 may:

- declare fixture obligations;
- add missing negative fixture classes;
- map fixtures to Gate 1 steps and acceptance criteria;
- mark fixture creation as future bounded work.

Step 9 must not:

- create fixture directories under `fixtures/core-0.1`;
- copy, render, OCR, hash, inspect, or otherwise process `Вирал`;
- create expected OCR/source/QA/translation/proofreading outputs;
- mark any fixture as passed, failed, accepted, or released;
- accept the Gate 1 protocol or authorize a bounded trial.
