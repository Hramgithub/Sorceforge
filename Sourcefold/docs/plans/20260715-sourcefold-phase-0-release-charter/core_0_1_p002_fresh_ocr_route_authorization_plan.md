## Core 0.1 P002 Fresh OCR Route Authorization

Lane: `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-ROUTE-AUTH-001`

Status:
`p002_fresh_ocr_route_authorized_no_execution`.

Scope:

- Consume committed `C01TEP002MATREVIEW-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Verify page `002` remains blocked only by
  `needs_fresh_ocr_route_authorization`.
- Authorize a future bounded fresh OCR candidate route from the lane-owned
  full-page image only.
- Keep corrected crop refs as comparison-only surfaces, not OCR inputs.

Result:

- Fresh OCR route authorized: `true`.
- Future OCR input surface class: `full_page_region`.
- Corrected crop refs authorized as OCR input: `false`.
- Corrected crop refs authorized for comparison only: `true`.
- Candidate hash must be sealed before reference scoring: `true`.
- OCR execution performed: `false`.
- Fresh OCR success: `false`.
- Bridge blocker cleared: `false`.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_route_authorization_G1_VIRAL_001/`

Allowed outputs:

- `p002_fresh_ocr_route_authorization_report.json`
- `p002_fresh_ocr_route_authorization_summary.md`
- `p002_fresh_ocr_route_authorization_manifest.md`

Boundaries:

- Do not run OCR/Tesseract, create candidate text, render or parse PDFs, accept
  text, mutate source/raw/accepted/page-status files, admit fixtures, assemble
  production, include page `021+`, push, promote, clear bridge lineage, mark
  fresh OCR success, or trigger downstream execution.

Output hashes:

- Report:
  `6EE1925A65367833898D0E17150687E341F411C1B7D6EDDD0219671593F6AC68`
- Summary:
  `096069AC2AE284A852448D0DE3B8347F9369FF89BC851850742D646D1583B741`
- Manifest:
  `C0AA3147BB065FB8F0EA4F88A5D86E84F0C5B06CB9F8EAAC41DD4417AD2C444D`
