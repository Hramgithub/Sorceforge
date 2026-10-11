# Page 009 Crop Contract Packet - P009TR-G1-VIRAL-003

Status: `page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked`

Purpose: review whether page 009 now has a role-separated crop contract suitable as the bounded input contract for a later PCRP authorization.

Boundary: this packet creates no OCR run, no OCR output/evidence, no PCRP, no page-complete acceptance, no whole Gate 1 acceptance, no render/PDF/raw mutation, and no pages 010-020 processing.

## Observed Page 009

- Page type: two-profile visual/text composition.
- Existing evidence: rendered page image plus provisional region-map/page-map/page-inventory hints.
- Current result: page 009 crop-role contract ready for human review, not accepted.
- Supersedes: `P009TR-G1-VIRAL-002` for PCRP routing only; `_002` remains historical/readability-only evidence.
- Right lower grey block: complete/non-blocker.

## Review Blocks

- `P009-B001`: left portrait/image area, `source_region_box_px` plus `human_review_crop_box_px` only.
- `P009-B002`: right portrait/image area, `source_region_box_px` plus `human_review_crop_box_px` only.
- `P009-B003`: left profile text block with `source_region_box_px`, `human_review_crop_box_px`, `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`.
- `P009-B004`: right profile text block with `source_region_box_px`, `human_review_crop_box_px`, `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`.

## Routing Recommendation

- Previous `_002` route recommendation is superseded for PCRP purposes.
- Recommended next candidate: Bogdan review of `P009TR-G1-VIRAL-003`; only after that may a separate PCRP authorization be created.
- OCR benchmark remediation remains a separate later branch; no OCR is executed here.

Decision after review: `p009 crop contract ok` or `hold p009 crop contract: <reason>`.
