# Page Inventory Report - PIR-G1-VIRAL-001

Report id: `PIR-G1-VIRAL-001`

Status: `valid_for_review`

Created: 2026-07-17

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-PAGEINV-001`

Accepted protocol:

- Revision: `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- File blob: `4d494e83d8d63dd3778a3813b3ee529449cee51a`

Predecessor artifacts:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/render_output_manifest.md`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Visual sanity report: `VSR-G1-VIRAL-001`
- Visual sanity report SHA-256:
  `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Contact sheet:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/visual_sanity_contact_sheet.png`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`

Method:

- Visual review of already-rendered PNG outputs and the derived contact sheet
  only.
- No PDF was opened, parsed, rehashed, recounted, or inspected.
- Page-level observations only; no coordinates, regions, anchors, reading
  order, map payload, OCR routing, QA, benchmark scoring, source-profile
  acceptance, translation, proofreading, or implementation work.

Boundary:

- This report is non-accepting inventory evidence only.
- Labels are non-authoritative visual hints for planning the next bounded
  action. They are not source structure, map regions, QA classes, OCR routing
  decisions, reading-order decisions, fixture evidence, or acceptance evidence.
- The report does not create `doc_map`, `content_map`, `art_map`,
  `pre_ocr_map_bundle`, region registry, anchors, stable region IDs, accepted
  source text, accepted source evidence, or accepted source-profile parameters.

Page inventory:

| Page ordinal | Image id | Image path | Image SHA-256 | Presence | Gross state | Broad page kind | Coarse layout hint | future_map_needed | Reason / uncertainty |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `IMG-G1-VIRAL-RENDER-001-P001` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_001.png` | `672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692` | present | portrait; not gross blank/corrupt/clipped | cover/title | full-page art/title composition | yes | Likely needs later visual/text separation if mapping is authorized. |
| 2 | `IMG-G1-VIRAL-RENDER-001-P002` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_002.png` | `ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9` | present | portrait; not gross blank/corrupt/clipped | credits/legal | centered text-heavy page | maybe | Coarse role only; exact text and reading order were not inspected. |
| 3 | `IMG-G1-VIRAL-RENDER-001-P003` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_003.png` | `B6B5A48D498FDEFB050B67E7155E85502010799D05CC10317C9E179CEB97A6BF` | present | portrait; not gross blank/corrupt/clipped | intro/title text | text-heavy with large heading/art | yes | Mixed heading/text/art may need later page map if authorized. |
| 4 | `IMG-G1-VIRAL-RENDER-001-P004` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_004.png` | `45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88` | present | portrait; not gross blank/corrupt/clipped | warning/notice | in-page document graphic plus text | yes | Tilted/inset graphic suggests later region handling may be needed. |
| 5 | `IMG-G1-VIRAL-RENDER-001-P005` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_005.png` | `0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE` | present | portrait; not gross blank/corrupt/clipped | contents/table | structured contents/table-style list | yes | Table-style structure should not be inferred without a later map action. |
| 6 | `IMG-G1-VIRAL-RENDER-001-P006` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_006.png` | `B0BE1CC101217D0732B5C8D32F731C7A22C1F1C852F67B673F5E2F38AC2B46BF` | present | portrait; not gross blank/corrupt/clipped | introduction | text plus large background image | yes | Mixed image/text composition likely needs later map separation. |
| 7 | `IMG-G1-VIRAL-RENDER-001-P007` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_007.png` | `0271A5FB9A672248ABBC771C2F1F064D58640CCB6D8692C7AF7AAE58A160BC41` | present | portrait; not gross blank/corrupt/clipped | profile/social-card | portrait plus text/graphic blocks | yes | Profile-like composition is only a broad visual hint. |
| 8 | `IMG-G1-VIRAL-RENDER-001-P008` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_008.png` | `237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0` | present | portrait; not gross blank/corrupt/clipped | profile/text | portrait/image plus text columns | yes | Later map may be needed for text/image separation. |
| 9 | `IMG-G1-VIRAL-RENDER-001-P009` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_009.png` | `3EC853C61DED9F5009F3FD567A03D499408C25EE385169DFE0EC82A2C47FC456` | present | portrait; not gross blank/corrupt/clipped | profile spread | two-profile visual/text composition | yes | Multi-block composition likely needs later mapping if authorized. |
| 10 | `IMG-G1-VIRAL-RENDER-001-P010` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_010.png` | `A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7` | present | portrait; not gross blank/corrupt/clipped | profile spread | portrait-heavy two-column-looking page | yes | Layout hint is non-authoritative and not a reading-order claim. |
| 11 | `IMG-G1-VIRAL-RENDER-001-P011` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_011.png` | `697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6` | present | portrait; not gross blank/corrupt/clipped | profile/text | portrait plus secondary image and text | yes | Mixed visual/text blocks may need later map action. |
| 12 | `IMG-G1-VIRAL-RENDER-001-P012` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_012.png` | `D5040085668216E68E617A06B513DC09CE3797E4D3F6BC6AC7BF35B68BD08ED6` | present | portrait; not gross blank/corrupt/clipped | text-heavy | mostly continuous text with section breaks | maybe | Later OCR/map decision depends on separately authorized evidence. |
| 13 | `IMG-G1-VIRAL-RENDER-001-P013` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_013.png` | `DC9BF562A4B3B7E43B38F29F484B64B13958330F449672D6A695B36E0D8F0935` | present | portrait; not gross blank/corrupt/clipped | full-page art/photo | dominant image page | yes | Image-dominant page likely needs distinct handling later. |
| 14 | `IMG-G1-VIRAL-RENDER-001-P014` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_014.png` | `24271ACED987DDF04850975ABE27D3B9BD4D48C74D81226E381D98D5E82948EA` | present | portrait; not gross blank/corrupt/clipped | equipment/table-like | structured text/table-like page with image | yes | Structured/table-like page likely needs map rules before OCR. |
| 15 | `IMG-G1-VIRAL-RENDER-001-P015` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_015.png` | `023836CD8DF8B77073F977E22F00CA87391F96855765D77B5C2826B0F00EDBBA` | present | portrait; not gross blank/corrupt/clipped | timeline/history | split text plus photo panel | yes | Split visual/text composition may need later map action. |
| 16 | `IMG-G1-VIRAL-RENDER-001-P016` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_016.png` | `7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56` | present | portrait; not gross blank/corrupt/clipped | timeline/history text | text-heavy page | maybe | Page-level hint only; no reading order or OCR readiness asserted. |
| 17 | `IMG-G1-VIRAL-RENDER-001-P017` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_017.png` | `1198CBB7D55877B31FEEA3E32CD95EABEB504A4610CA98D7CB2047C30142E08F` | present | portrait; not gross blank/corrupt/clipped | section opener/location | large scenic image plus text | yes | Mixed opener composition may need later mapping if authorized. |
| 18 | `IMG-G1-VIRAL-RENDER-001-P018` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_018.png` | `6E8F440CEB5F11A4081722ADF5CD65F74E622641884192390E9DA0CAE6C6BFD4` | present | portrait; not gross blank/corrupt/clipped | location/background | text-heavy with multi-block structure | maybe | Coarse structure only; no map or anchors created. |
| 19 | `IMG-G1-VIRAL-RENDER-001-P019` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_019.png` | `63BBB963A76F5C266E4A1B139FBCEFD2D390FB23B23CA391E8BAF12A4E9D3AC8` | present | portrait; not gross blank/corrupt/clipped | location/background | portrait image plus text blocks | yes | Mixed image/text blocks may need later page mapping. |
| 20 | `IMG-G1-VIRAL-RENDER-001-P020` | `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_020.png` | `53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E` | present | portrait; not gross blank/corrupt/clipped | location/background | text page with scenic image | yes | Later action needed before any map/OCR routing claim. |

Not accepted by this report:

- OCR, transcription, PDF text-layer extraction, copied text, or exact text.
- Reading order, region boxes, coordinates, anchors, stable region IDs, or map
  payloads.
- `doc_map`, `content_map`, `art_map`, or `pre_ocr_map_bundle`.
- OCR readiness, OCR routing, benchmark scores, render quality scores, QA
  findings, fixture manifests, accepted source text, source evidence,
  source-profile acceptance, translation, proofreading, or implementation.

Invalidation:

- This inventory is stale if source path/hash, `SPM-G1-VIRAL-001`,
  `RT-G1-VIRAL-RENDER-001`, render output manifest/hash, page PNG files,
  contact sheet/hash, `VSR-G1-VIRAL-001`, accepted protocol revision/blob,
  authorization record, render config, inventory schema/taxonomy, or user
  authority changes.
- If stale, it cannot feed map, OCR, benchmark, QA, fixture, source-profile,
  source-acceptance, translation, proofreading, or implementation work until
  refreshed under a fresh bounded authorization.
