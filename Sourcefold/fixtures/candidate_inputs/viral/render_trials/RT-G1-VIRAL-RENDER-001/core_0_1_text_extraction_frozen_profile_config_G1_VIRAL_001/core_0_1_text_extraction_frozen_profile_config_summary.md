# Core 0.1 Text Extraction Frozen Profile Config - C01TEFPC-G1-VIRAL-001

Status: `text_extraction_frozen_profile_config_recorded_no_ocr_execution`

This artifact records the reusable Core 0.1 text extraction candidate profile config.

It does not run OCR and does not create OCR/source/runtime acceptance.

## Profile

- Profile id: `trim_mask_psm4`.
- Preprocessing: `edge_mask_trim`.
- Tesseract: `-l eng --oem 1 --psm 4 txt tsv`.
- Allowed inputs: text-evidence crop PNGs for P009/P010/P015 replay.
- P015 reference label: `reference_text_map_not_ocr_verified`.

## Boundary

- OCR execution: `false`.
- Source/runtime profile acceptance: `false`.
- Accepted/semantic/page-status mutation: `false`.
- PDF/render/runtime/page 016+/page 021+/push: `false`.
