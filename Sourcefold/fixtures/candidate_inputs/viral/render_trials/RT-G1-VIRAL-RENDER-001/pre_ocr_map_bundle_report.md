# Pre-OCR Map Bundle - POMB-G1-VIRAL-001

Bundle id: `POMB-G1-VIRAL-001`

Status: `frozen_for_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-MAPBUNDLE-001`

Schema: `pre_ocr_map_bundle.v0` from `MSID-G1-VIRAL-001`

Baseline commit: `bb2b996d448df523e656386bc9a0f8f69dc96ab5`

Purpose: freeze exact current non-accepting pre-OCR map-layer evidence for
later admission review.

Boundary: this bundle is a lineage freeze only. It is not Gate 1 acceptance,
source-profile acceptance, OCR readiness, OCR authorization, QA, benchmark,
fixture, source evidence, translation, proofreading, renderer/profile
acceptance, or implementation.

Method: bind exact current MSID/DM/CM/AM/MCV hashes after
`MCV-G1-VIRAL-001` passed for bundle-freeze review. The PDF was not opened,
parsed, rehashed, recounted, or inspected. No OCR, transcription, copied text,
PDF text-layer extraction, benchmark, QA, fixture, source acceptance,
translation, proofreading, or implementation work was performed.

## Frozen Inputs

| Bundle part | ID | SHA-256 | Status |
|---|---|---|---|
| Schema/identity packet | `MSID-G1-VIRAL-001` | `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024` | `valid_for_review` |
| Trial doc map | `DM-G1-VIRAL-001` | `F10FFDF22393A467668396DB2C7861331B5E5BD11586DCF72B46FE95140717E6` | `valid_for_review` |
| Trial content map | `CM-G1-VIRAL-001` | `335699DB7AE60E87390D88D7A26AA22BA297F50F90B7868F7ED869C2F5AABE79` | `valid_for_review` |
| Trial art map | `AM-G1-VIRAL-001` | `77BD88C0522E17DF98603364677BC248450EC3E57996389881629E581197C544` | `valid_for_review` |
| Map consistency validation | `MCV-G1-VIRAL-001` | `B939CEB12187C47FCBE3FFB72032D50E2B13AD22261637D6652204F61144BCE3` | `passed_for_bundle_freeze_review` |

## Bundle Scope

Included:

- Exact map-layer artifact IDs and hashes.
- Exact schema/identity packet hash.
- Exact consistency validation hash.
- Downstream-use limitations.
- Invalidation rules.

Excluded:

- OCR output.
- Copied source text.
- PDF text-layer content or order.
- Gold sample text.
- Accepted reading order.
- Accepted coordinates or anchors.
- QA findings.
- Fixture manifests.
- Source evidence acceptance.
- Translation or proofreading output.

## Downstream Admission State

`not_admitted_for_ocr`

This bundle cannot be consumed by OCR preparation, OCR benchmark, QA, fixture
creation, source-profile acceptance, translation, proofreading, or
implementation until a later bounded admission/prep authorization explicitly
names `POMB-G1-VIRAL-001`, its hash, allowed use, and invalidation behavior.

## Verdict

`frozen_for_review`

This verdict freezes lineage for review only. It does not state that the map is
complete, correct, semantically accepted, OCR-ready, or sufficient for Gate 1
advancement.

## Next Bounded Work

The next step may request `BA-G1-VIRAL-OCRPREP-001` to prepare an OCR
candidate manifest, scoring plan, gold-sample creation plan, and
map-consumption admission record. This bundle does not authorize that action.

## Invalidation

This bundle is stale if protocol revision/blob changes, baseline commit is
superseded, authorization changes, MSID changes, any map-layer hash changes,
MCV changes, canonicalization/hash rules change, downstream admission rules
change, reviewer/authority changes, or any predecessor artifact is remediated
or superseded.
