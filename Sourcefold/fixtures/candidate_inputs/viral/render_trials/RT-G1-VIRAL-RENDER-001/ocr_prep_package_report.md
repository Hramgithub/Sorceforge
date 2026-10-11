# OCR Preparation Package - OPR-G1-VIRAL-001

Prep id: `OPR-G1-VIRAL-001`

Status: `ready_for_gold_and_ocr_authorization`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-OCRPREP-001`

Baseline commit: `6769c619b53cadd13f9e338024c045fb9750451b`

Purpose: prepare planning artifacts needed before any future bounded OCR
benchmark can be authorized.

Boundary: this is not OCR execution, OCR output, gold text, source evidence,
QA, benchmark result, fixture, source-profile acceptance, translation,
proofreading, renderer/profile acceptance, implementation, or Gate 1
acceptance.

Method: bind current render and map-bundle predecessors and define candidate,
scoring, gold-sample creation, and map-consumption admission constraints. The
PDF was not opened, parsed, rehashed, recounted, or inspected. No OCR,
transcription, copied text, PDF text-layer extraction, benchmark, QA, fixture,
source acceptance, translation, proofreading, or implementation work was
performed.

## Inputs

| Evidence | ID | SHA-256 |
|---|---|---|
| Pre-OCR map bundle | `POMB-G1-VIRAL-001` | `B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F` |
| Render output manifest | `RT-G1-VIRAL-RENDER-001` | `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC` |

## Map Consumption Admission

Admission id: `MCA-G1-VIRAL-001`

Status: `admitted_for_ocr_planning_only`

Allowed:

- OCR candidate and scoring plan may reference `POMB-G1-VIRAL-001` by exact
  bundle ID and hash.
- Future OCR benchmark authorization may name `POMB-G1-VIRAL-001` as a
  candidate map predecessor if its hash remains current.

Not allowed:

- OCR execution.
- OCR output creation.
- Gold text/sample answer creation.
- QA, benchmark scoring, source acceptance, translation, proofreading, or
  implementation.

## OCR Candidate Manifest Stub

Manifest id: `OCM-G1-VIRAL-001`

Status: `candidate_manifest_stub`

Candidate dimensions to bind before execution:

- OCR engine/service identity and exact version/model.
- Executable/API identity and local environment.
- Language/profile configuration.
- Page/region input selection from `POMB-G1-VIRAL-001`.
- Preprocessing policy.
- Layout/output mode.
- Output format and canonicalization.
- Confidence/coordinate reporting behavior.

No engine is accepted by this package.

## Scoring Plan Stub

Plan id: `OSP-G1-VIRAL-001`

Status: `scoring_plan_stub`

Required before benchmark:

- Exact gold-sample manifest ID and hash.
- Exact OCR candidate manifest ID and hash.
- Metrics for text accuracy, structure preservation, reading-order failures,
  missing/duplicate content, table/list handling, and map/region lineage.
- Non-waivable failure handling from the Gate 1 protocol.
- Stale evidence behavior for any OCR candidate/config/map/gold/scoring
  change.

No scoring threshold is accepted by this package.

## Gold-Sample Creation Plan

Plan id: `GSP-G1-VIRAL-001`

Status: `gold_sample_creation_plan_only`

The future gold-sample step must be separately authorized before any gold text,
sample answers, expected OCR output, or accepted source snippets are created.

Required future fields:

- Page/region IDs selected from `POMB-G1-VIRAL-001`.
- Human authority and review method.
- Source of gold text and explicit prohibition on PDF text-layer payload unless
  separately authorized by exact action.
- Hashing/canonicalization of gold samples.
- Non-waivable failure taxonomy linkage.
- Invalidation behavior.

## Next Bounded Work

The next step cannot run OCR yet. It must first request separate authorization
for gold sample creation and admitted OCR benchmark execution, or record that
the OCR benchmark remains blocked because gold samples and OCR candidate
identity are not yet created.

## Invalidation

This package is stale if protocol revision/blob changes, baseline commit is
superseded, authorization changes, POMB changes, render output manifest
changes, OCR engine identity/config policy changes, scoring policy changes,
gold-sample policy changes, map-consumption admission rules change,
reviewer/authority changes, or any predecessor remediation/supersession
occurs.
