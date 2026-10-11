## Core 0.1 P002 Fresh OCR Candidate

Lane: `C01TEP002FRESHOCR-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-CANDIDATE-001`

Status:
`p002_fresh_ocr_candidate_executed_candidate_only_no_scoring_no_promotion`.

Scope:

- Consume committed `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Run Tesseract only on the lane-owned page `002` full-page image.
- Keep corrected crop refs as comparison-only surfaces, not OCR input.
- Seal candidate text hashes without loading any reference-scoring surface.

Result:

- OCR execution performed: `true`.
- Tesseract-invoked pages: `["002"]`.
- PSM values: `[4, 6]`.
- Candidate count: `2`.
- Reference scoring performed: `false`.
- Fresh OCR success: `false`.
- Bridge blocker cleared: `false`.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_candidate_G1_VIRAL_001/`

Allowed outputs:

- `candidate_texts/page_002_full_page_psm4_candidate.md`
- `candidate_texts/page_002_full_page_psm6_candidate.md`
- `ocr_metadata/page_002_full_page_psm4_ocr_metadata.json`
- `ocr_metadata/page_002_full_page_psm6_ocr_metadata.json`
- `p002_fresh_ocr_candidate_report.json`
- `p002_fresh_ocr_candidate_summary.md`
- `p002_fresh_ocr_candidate_manifest.md`

Boundaries:

- Do not use corrected crop refs as OCR input.
- Do not score references, accept text, mutate source/raw/accepted/page-status
  files, admit fixtures, assemble production, include page `021+`, push,
  promote, clear bridge lineage, mark fresh OCR success, or trigger downstream
  execution.

Output hashes:

- Report:
  `5686F161296BD696E8F97B00DB9560F2374E6FAC74B4DA223490FF2ECFC473D2`
- Summary:
  `4AE2AE00372FADB5E523982A438ABDDAD69F5CB6EA8EB5F706A2D87FA399A3A5`
- Manifest:
  `FEE45C27C759FCCBD67DF2CC44B8F65D4249644FCC3DA9A289612FBDC721B155`
