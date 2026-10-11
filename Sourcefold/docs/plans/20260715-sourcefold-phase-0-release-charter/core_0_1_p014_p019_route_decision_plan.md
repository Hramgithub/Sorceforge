## Core 0.1 P014/P019 Route Decision

Lane: `C01TEP014019ROUTEDEC-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P014-P019-ROUTE-DECISION-001`

Status:
`p014_p019_route_decision_recorded_full_page_ocr_route_required_no_execution`.

Scope:

- Consume committed `C01TEBRIDGEAUD020-G1-VIRAL-001` and
  `C01TEBRIDGEREM020-G1-VIRAL-001` report/summary/manifest by exact hash.
- Hash-pin page-complete acceptance/review surfaces plus full-page images and
  text maps for pages `014` and `019`.
- Decide whether existing text-evidence smoke outputs can clear bridge lineage
  or count as fresh OCR success.
- Authorize only a future separate full-page OCR route for pages `014` and
  `019`.

Decision:

- Existing text-evidence smoke clears bridge: `false`.
- Existing text-evidence smoke creates fresh OCR success: `false`.
- Future full-page OCR route authorized: `true`.
- Future OCR input surface class: `full_page_region`.
- Text-evidence crops may be used as OCR input: `false`.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p014_p019_route_decision_G1_VIRAL_001/`

Allowed outputs:

- `p014_p019_route_decision_report.json`
- `p014_p019_route_decision_summary.md`
- `p014_p019_route_decision_manifest.md`

Boundaries:

- Do not run OCR/Tesseract, score candidates, render or parse PDFs, accept text,
  mutate source/raw/accepted/page-status files, admit fixtures, assemble
  production, include page `021+`, push, promote, or trigger downstream
  execution.

Output hashes:

- Report:
  `BC4D6569FE50C59374C0A1D54B3A23611D267D08B6759F8B5D726FEC8D989458`
- Summary:
  `5AF33BFEB0E3750597AF4A400849128CF2D429C2AD2BDA334D576F2D83DEF18E`
- Manifest:
  `77C243CD1FB4C1AB70EE7902BA005216477DFD6B5FDC6C2B7FBADB332F2E42C9`
