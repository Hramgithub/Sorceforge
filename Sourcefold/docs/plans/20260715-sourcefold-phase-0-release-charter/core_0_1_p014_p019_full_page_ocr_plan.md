## Core 0.1 P014/P019 Full-Page OCR

Lane: `C01TEP014019FPOCR-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P014-P019-FULL-PAGE-OCR-001`

Status:
`p014_p019_full_page_ocr_completed_candidate_only_no_promotion`.

Scope:

- Consume committed `C01TEP014019ROUTEDEC-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Hash-pin full-page image and text-map comparison surfaces for pages `014` and
  `019`.
- Run Tesseract only on authorized full-page-region input surfaces for pages
  `014` and `019`.
- Seal candidate text hashes before loading comparison text maps for diagnostic
  metrics.

Result:

- Page `014` selected PSM `4` with similarity `0.157291` and token recall
  `0.885572`.
- Page `019` selected PSM `4` with similarity `0.072989` and token recall
  `0.9225`.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotion performed: `false`.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p014_p019_full_page_ocr_G1_VIRAL_001/`

Allowed outputs:

- `candidate_texts/page_014_full_page_psm4_candidate.md`
- `candidate_texts/page_014_full_page_psm6_candidate.md`
- `candidate_texts/page_019_full_page_psm4_candidate.md`
- `candidate_texts/page_019_full_page_psm6_candidate.md`
- `ocr_metadata/page_014_full_page_psm4_ocr_metadata.json`
- `ocr_metadata/page_014_full_page_psm6_ocr_metadata.json`
- `ocr_metadata/page_019_full_page_psm4_ocr_metadata.json`
- `ocr_metadata/page_019_full_page_psm6_ocr_metadata.json`
- `p014_p019_full_page_ocr_report.json`
- `p014_p019_full_page_ocr_summary.md`
- `p014_p019_full_page_ocr_manifest.md`

Boundaries:

- Do not use text-evidence crops as OCR input.
- Do not accept text, mutate source/raw/accepted/page-status files, admit
  fixtures, assemble production, include page `021+`, push, promote, clear
  bridge lineage, mark fresh OCR success, or trigger downstream execution.

Output hashes:

- Report:
  `0238FFA8B0D91FAE6047E426AA59BA606668EAB589B14FD112AE5615A4877F32`
- Summary:
  `4250181B5F35A1A8809A965190F0831B7F58FCAC73C3974A9BED18BF216B0E19`
- Manifest:
  `EB1DA1D11FAF85315363F7EE8213F34F381603719898A9EB2E353D6F36D4175B`
