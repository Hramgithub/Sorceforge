# Visual Sanity Report - RT-G1-VIRAL-RENDER-001

Report id: `VSR-G1-VIRAL-001`

Status: `valid_for_review`

Created: 2026-07-17

Authorization id: `BA-G1-VIRAL-VISUAL-001`

Inputs:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Contact sheet:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/visual_sanity_contact_sheet.png`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`

Boundary:

- This is a visual sanity and page inventory report only.
- No OCR, transcription, PDF text-layer extraction, mapping, benchmark scoring,
  QA finding, fixture creation, source acceptance, translation, proofreading,
  renderer/profile acceptance, or implementation was performed.
- Broad page-kind labels below are non-authoritative inventory hints, not
  source structure, map regions, QA classes, or acceptance evidence.

Summary:

- Expected outputs present: 20.
- Visual outputs reviewed: 20.
- Missing or unreadable image files: none observed.
- Gross blank/corrupt render outputs: none observed.
- Gross page rotation/orientation problem: none observed.
- Output dimensions observed in the render manifest/contact sheet: 2550x3300
  for pages 1-20.
- Gross page-boundary clipping: none observed at contact-sheet scale.

Page Inventory:

| Page | Broad visual kind | Gross sanity note |
|---:|---|---|
| 1 | cover/title-style page | present; portrait; no gross blank/corrupt output |
| 2 | credits/legal-style page | present; portrait; text-heavy page rendered |
| 3 | intro/title-style text page | present; portrait; text page rendered |
| 4 | warning/notice-style graphic page | present; portrait; tilted in-page graphic appears intentional |
| 5 | contents/table-style page | present; portrait; structured list/table page rendered |
| 6 | introduction text page with background image | present; portrait; text/image composition rendered |
| 7 | profile/social-card-style page with portrait | present; portrait; image/text composition rendered |
| 8 | character/profile text page with portrait and image | present; portrait; text/image composition rendered |
| 9 | two-column profile page with portraits | present; portrait; text/image composition rendered |
| 10 | profile page with portraits | present; portrait; text/image composition rendered |
| 11 | profile/text page with portrait and image | present; portrait; text/image composition rendered |
| 12 | text-heavy page | present; portrait; text-heavy layout rendered |
| 13 | full-page dark photo/illustration page | present; portrait; image rendered |
| 14 | equipment/table-like text page with small image | present; portrait; text/table-like layout rendered |
| 15 | timeline/history split page with photo | present; portrait; text/image composition rendered |
| 16 | text-heavy timeline/history page | present; portrait; text-heavy layout rendered |
| 17 | section opener with large scenic image and text | present; portrait; image/text composition rendered |
| 18 | location/background text page | present; portrait; text-heavy layout rendered |
| 19 | location/background text page with portrait image | present; portrait; text/image composition rendered |
| 20 | location/background text page with scenic image | present; portrait; text/image composition rendered |

Not Accepted By This Report:

- OCR readiness.
- Reading order.
- Region map or anchors.
- Text correctness.
- Render quality score.
- Renderer/DPI/color/container parameters.
- Source profile acceptance.

Invalidation:

- Stale if `SPM-G1-VIRAL-001`, `RT-G1-VIRAL-RENDER-001`, render output
  manifest, contact sheet, accepted protocol revision/blob, visual
  authorization, render config, visual report schema, or user authority changes.
