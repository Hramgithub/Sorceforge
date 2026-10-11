# OCR Remediation Review Report - ORR-G1-VIRAL-001

Status: `remediation_evidence_only`; review state: `valid_for_review`

Authorization: `BA-G1-VIRAL-REMEDIATION-REVIEW-001`

Boundary: this report reviews `ORM-G1-VIRAL-001` remediation evidence only. It is not source acceptance, Gate 1 advancement, QA completion, fixture acceptance, translation, proofreading, renderer/profile acceptance, implementation, or a human source review.

`BA-G1-VIRAL-REMEDIATE-001` is `expired`; its scope was consumed by `ORM-G1-VIRAL-001` and does not authorize new OCR, PDF parsing, QA, fixtures, source acceptance, translation, proofreading, or Gate 1 advancement.

## Aggregate

- Samples: `5`
- Remediation-route pass: `5/5`
- OCR normalized-exact zones: `5`
- Visual-QC route zones: `2`
- Source acceptance: `false`
- Gate 1 advancement: `false`
- Approved by score: `false`

## OCR Route Findings

| Sample | Zone | Finding | Selected config | Token recall | CER | Overlay QC | Order QC |
|---|---|---|---|---:|---:|---|---|
| `GS-G1-VIRAL-001` | `z02` | `ocr_normalized_exact` | `white_mask_x4__psm4` | `1.0` | `0.0` | `bad_geometry` | `auto_qc_pass` |
| `GS-G1-VIRAL-002` | `z01` | `ocr_normalized_exact` | `original__psm11` | `1.0` | `0.375` | `needs_visual_review` | `auto_qc_pass` |
| `GS-G1-VIRAL-003` | `z01` | `ocr_normalized_exact` | `binary_x3__psm11` | `1.0` | `0.6207` | `likely_visual_page` | `auto_qc_pass` |
| `GS-G1-VIRAL-004` | `z01` | `ocr_normalized_exact` | `original__psm11` | `1.0` | `0.0` | `bad_geometry` | `auto_qc_pass` |
| `GS-G1-VIRAL-005` | `z01` | `ocr_normalized_exact` | `enhanced_x2__psm1` | `1.0` | `0.0` | `ok` | `auto_qc_pass` |

## Visual-QC Route Findings

| Sample | Zone | Finding | Label |
|---|---|---|---|
| `GS-G1-VIRAL-001` | `z01` | `visual_qc_route_pass` | `cover_title_visual_component` |
| `GS-G1-VIRAL-003` | `z02` | `visual_qc_route_pass` | `contents_page_numbers` |

## Review Decision

- `ORM-G1-VIRAL-001` is suitable as remediation evidence for a later Gate 1 rollup.
- The matrix does not authorize source reconstruction approval or human proofreading.
- Visual-QC route findings are routing evidence only; they are not transcription or text acceptance.
- Overlay/QC caveats remain part of the review package and must be carried into any later human-readable reconstruction review.
- Bogdan should be asked to review only after a separate source reconstruction package contains readable text aligned to page images/regions.

## Invalidation

This review stales if ORM output hashes, crop hashes, gold samples, OCR candidate identity, POMB/GSM/OCM/OBR predecessors, scoring rules, route rules, script revision, reviewer authority, or any upstream evidence changes.
