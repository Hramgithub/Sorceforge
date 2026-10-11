# Core 0.1 P002 Fresh OCR Scoring Reference Audit Plan

Lane: `C01TEP002FRESHSCOREAUD-G1-VIRAL-001`

Status: `completed`

## Scope

- Consume committed `C01TEP002FRESHOCR-G1-VIRAL-001` report/summary/manifest by exact hash.
- Consume page `002` PSM `4` and PSM `6` candidate texts by exact hash.
- Audit only pinned page `002` comparison/reference surfaces.
- Emit report, summary, and manifest under the lane-owned output folder.

## Boundaries

- No OCR/Tesseract execution.
- No fresh OCR success decision.
- No bridge removal.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No fixture admission, production assembly, page `021+`, push, promotion, acceptance, or downstream execution.

## Result

- Diagnostic comparison scoring performed: `true`.
- Candidate labels: `psm4`, `psm6`.
- Reference surfaces: page-complete review packet, page-map readiness packet, and historical page-complete acceptance record.
- All reference surfaces are comparison-only, not independent acceptance truth.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotable pages: `[]`.
- Next action: `separate_bounded_p002_candidate_scoring_or_remediation_decision`.

## Output Hashes

- `p002_fresh_ocr_scoring_reference_audit_report.json`: `0834F4A864105F6D15D243198F743158C9D91ECDAF5AAEA4A4281913DD481740`
- `p002_fresh_ocr_scoring_reference_audit_summary.md`: `3E42702616B3C4F1267559290F9D4BE303DC1A5CDC342C10ED11F8E32C396D7E`
- `p002_fresh_ocr_scoring_reference_audit_manifest.md`: `BF9B57598F7FAC66DEDFAF25D6CC1692C278AB9CA185BAC9DE06FD0AE4839FFB`
