# Core 0.1 P015 Same-Profile OCR Smoke

Smoke id: `C01TESP015-G1-VIRAL-001`

Status: `candidate_only_p015_same_profile_smoke_completed`

Boundary: P015-only candidate evidence over read-only text-evidence crop PNGs.

Source selected profile: `C01TESRM-G1-VIRAL-001` / `trim_mask_psm4`.
Prior same-profile smoke: `C01TESP010-G1-VIRAL-001`.
Reference text map: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p015_G1_VIRAL_001/review_assets/page_015_text_map.md`.
Variant: `edge_mask_trim`.
PSM: `4`.
Similarity against P015 text map: `0.997252`.
Token recall: `0.993985`.

Preserved limits:

- No P015 source/review/reference/accepted-text overwrite.
- No semantic text or page-status mutation.
- No page 016+ or 021+ processing or authorization.
- No PDF parsing/text-layer extraction.
- No render execution.
- No runtime implementation/start.
- No translation/proofreading/push.
