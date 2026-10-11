## Core 0.1 P002 Materialized Surface Review

Lane: `C01TEP002MATREVIEW-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-MATERIALIZED-SURFACE-REVIEW-001`

Status:
`p002_materialized_surface_review_completed_asset_recovery_blocker_cleared_no_ocr_no_acceptance`.

Scope:

- Consume committed `C01TEP002ASSETMAT-G1-VIRAL-001` report, summary, and
  manifest by exact hash.
- Verify the lane-owned materialized page `002` full-page image and two
  corrected crop refs by SHA-256.
- Clear only the page `002` asset-recovery blocker.
- Preserve `fresh_ocr_success=false` and move the next blocker to
  `needs_fresh_ocr_route_authorization`.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_materialized_surface_review_G1_VIRAL_001/`

Allowed outputs:

- `p002_materialized_surface_review_report.json`
- `p002_materialized_surface_review_summary.md`
- `p002_materialized_surface_review_manifest.md`

Boundaries:

- Do not run OCR/Tesseract, render or parse PDFs, accept text, mutate
  source/raw/accepted/page-status files, admit fixtures, assemble production,
  include page `021+`, push, promote, or trigger downstream execution.
- Do not treat source acceptance chain artifacts as fresh OCR truth.

Output hashes:

- Report:
  `0B047CF8B9FA2E7B77D3CB73C296F11070198F4C2EEB4B1585882EE91DFFFA1F`
- Summary:
  `8E293FB620CE6503D341FC4EB5F882FF6A98F807C04FEDD51FFE170E8E939AD7`
- Manifest:
  `CCBFD30FCCCAE5C0659C08817F1524CF3A3740FC87600D6956D6F20555AE6D7B`
