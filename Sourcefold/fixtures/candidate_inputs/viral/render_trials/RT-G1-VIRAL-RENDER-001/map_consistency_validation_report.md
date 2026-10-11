# Map Consistency Validation - MCV-G1-VIRAL-001

Validation id: `MCV-G1-VIRAL-001`

Status: `passed_for_bundle_freeze_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-MAPCONSISTENCY-001`

Baseline commit: `5db5b26ec76f62e459e7d947d36a99dea86f1354`

Purpose: validate current non-accepting trial `doc_map`, `content_map`, and
`art_map` artifacts before any later bundle-freezing authorization.

Boundary: this is not `pre_ocr_map_bundle`, Gate 1 acceptance, OCR readiness,
source evidence, QA, benchmark, fixture, source-profile acceptance,
translation, proofreading, renderer/profile acceptance, or implementation.

Method: compare current map-layer hashes, MSID linkage, region reference
coverage, overlap policy, and explicit payload leakage claims in the existing
trial reports. No map artifact was modified. The PDF was not opened, parsed,
rehashed, recounted, or inspected. No OCR, transcription, copied text, PDF
text-layer extraction, benchmark, QA, fixture, source acceptance, translation,
proofreading, or implementation work was performed.

## Inputs

| Evidence | ID | SHA-256 |
|---|---|---|
| Map schema/identity packet | `MSID-G1-VIRAL-001` | `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024` |
| Trial doc map | `DM-G1-VIRAL-001` | `F10FFDF22393A467668396DB2C7861331B5E5BD11586DCF72B46FE95140717E6` |
| Trial content map | `CM-G1-VIRAL-001` | `335699DB7AE60E87390D88D7A26AA22BA297F50F90B7868F7ED869C2F5AABE79` |
| Trial art map | `AM-G1-VIRAL-001` | `77BD88C0522E17DF98603364677BC248450EC3E57996389881629E581197C544` |

## Validation Matrix

| Check | Result | Evidence |
|---|---|---|
| Current map hashes recorded | pass | Input table binds exact MSID/DM/CM/AM hashes. |
| Shared page ID namespace | pass | All maps reference `PG-G1-VIRAL-P001`..`PG-G1-VIRAL-P020` through DM/MSID. |
| Shared trial region namespace | pass | CM/AM references use `RG-G1-VIRAL-P{page}-R{region}` from DM/MSID. |
| Doc region registry coverage | pass | DM records 62 trial regions across pages 1-20. |
| Content references within doc registry | pass | CM records 45 references, all inside DM ranges. |
| Art/mixed references within doc registry | pass | AM records 22 references, all inside DM ranges. |
| Union coverage | pass | Content/art union covers 62 of 62 DM trial regions. |
| Intentional overlap policy | pass | Five mixed/inset/sidebar regions are referenced by both CM and AM as mixed candidates, not duplicates. |
| Missing/duplicate blocking regions | pass | No unclassified DM trial region remains outside content/art union; no duplicate identity namespace detected. |
| Payload leakage | pass | DM/CM/AM explicitly prohibit OCR output, copied text, PDF text-layer content, translation, gold text, accepted reading order, accepted coordinates, source truth, and bundle freeze. |
| Roadmap/status payload containment | pass | Roadmap/status updates carry IDs/status/hash only, not region tables or coordinates. |

## Mixed Overlap Notes

The following mixed regions are intentionally cross-referenced by content and
art layers for later review:

- `RG-G1-VIRAL-P001-R003`
- `RG-G1-VIRAL-P002-R002`
- `RG-G1-VIRAL-P004-R001`
- `RG-G1-VIRAL-P007-R003`
- `RG-G1-VIRAL-P020-R004`

These are not accepted reading-order, OCR-routing, or source-truth decisions.

## Verdict

`passed_for_bundle_freeze_review`

This verdict means only that the current non-accepting trial map set can be
offered to a future bounded `BA-G1-VIRAL-MAPBUNDLE-001` review. It does not
freeze `pre_ocr_map_bundle`, accept Gate 1, authorize OCR, authorize QA, create
fixtures, or accept source evidence.

## Next Bounded Work

The next step may request `BA-G1-VIRAL-MAPBUNDLE-001` to freeze a
non-accepting `pre_ocr_map_bundle` from exact current MSID/DM/CM/AM/MCV hashes.
This report does not authorize that action.

## Invalidation

This report is stale if protocol revision/blob changes, baseline commit is
superseded, authorization changes, MSID changes, any validated map-layer hash
changes, validation rule changes, overlap policy changes, payload-leakage rules
change, reviewer/authority changes, or any remediation/supersession of the
validated maps occurs.
