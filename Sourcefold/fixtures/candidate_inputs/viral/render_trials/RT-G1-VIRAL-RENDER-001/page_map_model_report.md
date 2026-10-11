# Page Map Model Report - PMR-G1-VIRAL-001

Report id: `PMR-G1-VIRAL-001`

Status: `valid_for_review`

Created: 2026-07-17

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-PAGEMAP-001`

Schema/taxonomy: `provisional-page-map-model-v0`

Accepted protocol:

- Revision: `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- File blob: `4d494e83d8d63dd3778a3813b3ee529449cee51a`

Predecessor artifacts:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Visual sanity report: `VSR-G1-VIRAL-001`
- Visual sanity report SHA-256:
  `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`
- Page inventory report: `PIR-G1-VIRAL-001`
- Page inventory report SHA-256:
  `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA`

Method:

- Page-level modeling from `PIR-G1-VIRAL-001` and already-rendered PNG
  evidence only.
- No PDF was opened, parsed, rehashed, recounted, or inspected.
- No OCR, transcription, PDF text-layer extraction, exact text copying,
  reading-order assertion, coordinates, bounding boxes, anchors, stable region
  IDs, region registry, QA, benchmark scoring, fixture creation, source
  acceptance, translation, proofreading, or implementation work.

Boundary:

- This report is a non-accepting page-level planning/model artifact only.
- It is not a `doc_map`, `content_map`, `art_map`, `pre_ocr_map_bundle`, region
  registry, accepted source evidence, OCR routing decision, QA result,
  benchmark, fixture, source-profile acceptance, or implementation artifact.
- Labels are provisional planning hints. They may guide a later bounded map or
  OCR authorization request, but do not authorize or accept that downstream
  work.

Page-level model:

| Page | Image id | Image SHA-256 | Broad role | Coarse visual/layout class | Candidate layer focus | Map complexity | Later region mapping appears needed | Review state | Notes |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `IMG-G1-VIRAL-RENDER-001-P001` | `672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692` | cover/title | full-page art/title composition | visual/title separation | medium | yes | provisional | Page-level hint only; no text or regions asserted. |
| 2 | `IMG-G1-VIRAL-RENDER-001-P002` | `ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9` | credits/legal | centered text-heavy page | front matter/text block | low | maybe | provisional | Exact text and reading order were not inspected. |
| 3 | `IMG-G1-VIRAL-RENDER-001-P003` | `B6B5A48D498FDEFB050B67E7155E85502010799D05CC10317C9E179CEB97A6BF` | intro/title text | text-heavy with large heading/art | heading/text/art interaction | medium | yes | provisional | Candidate mixed structure; no region map created. |
| 4 | `IMG-G1-VIRAL-RENDER-001-P004` | `45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88` | warning/notice | in-page document graphic plus text | inset graphic/text separation | high | yes | provisional | Inset/tilted visual suggests future bounded region work. |
| 5 | `IMG-G1-VIRAL-RENDER-001-P005` | `0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE` | contents/table | structured contents/table-style list | table/list structure | high | yes | provisional | Table/list structure remains unaccepted. |
| 6 | `IMG-G1-VIRAL-RENDER-001-P006` | `B0BE1CC101217D0732B5C8D32F731C7A22C1F1C852F67B673F5E2F38AC2B46BF` | introduction | text plus large background image | mixed image/text | high | yes | provisional | Needs later separation before OCR routing claims. |
| 7 | `IMG-G1-VIRAL-RENDER-001-P007` | `0271A5FB9A672248ABBC771C2F1F064D58640CCB6D8692C7AF7AAE58A160BC41` | profile/social-card | portrait plus text/graphic blocks | profile-card layout | high | yes | provisional | No semantic RPG label accepted. |
| 8 | `IMG-G1-VIRAL-RENDER-001-P008` | `237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0` | profile/text | portrait/image plus text columns | image/text columns | high | yes | provisional | Reading order remains unknown. |
| 9 | `IMG-G1-VIRAL-RENDER-001-P009` | `3EC853C61DED9F5009F3FD567A03D499408C25EE385169DFE0EC82A2C47FC456` | profile spread | two-profile visual/text composition | multi-block profile layout | high | yes | provisional | Multi-block visual hint only. |
| 10 | `IMG-G1-VIRAL-RENDER-001-P010` | `A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7` | profile spread | portrait-heavy two-column-looking page | image/text columns | high | yes | provisional | No columns or order accepted. |
| 11 | `IMG-G1-VIRAL-RENDER-001-P011` | `697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6` | profile/text | portrait plus secondary image and text | mixed image/text | high | yes | provisional | Later bounded map may split visual/text zones. |
| 12 | `IMG-G1-VIRAL-RENDER-001-P012` | `D5040085668216E68E617A06B513DC09CE3797E4D3F6BC6AC7BF35B68BD08ED6` | text-heavy | mostly continuous text with section breaks | text block planning | medium | maybe | provisional | Exact text/order not inspected. |
| 13 | `IMG-G1-VIRAL-RENDER-001-P013` | `DC9BF562A4B3B7E43B38F29F484B64B13958330F449672D6A695B36E0D8F0935` | full-page art/photo | dominant image page | image-dominant handling | medium | yes | provisional | Future action may decide OCR exclusion or image handling. |
| 14 | `IMG-G1-VIRAL-RENDER-001-P014` | `24271ACED987DDF04850975ABE27D3B9BD4D48C74D81226E381D98D5E82948EA` | equipment/table-like | structured text/table-like page with image | table/image/text structure | high | yes | provisional | Table-like structure not accepted. |
| 15 | `IMG-G1-VIRAL-RENDER-001-P015` | `023836CD8DF8B77073F977E22F00CA87391F96855765D77B5C2826B0F00EDBBA` | timeline/history | split text plus photo panel | split image/text | high | yes | provisional | Future bounded map likely needed. |
| 16 | `IMG-G1-VIRAL-RENDER-001-P016` | `7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56` | timeline/history text | text-heavy page | text block planning | medium | maybe | provisional | No reading order or OCR readiness asserted. |
| 17 | `IMG-G1-VIRAL-RENDER-001-P017` | `1198CBB7D55877B31FEEA3E32CD95EABEB504A4610CA98D7CB2047C30142E08F` | section opener/location | large scenic image plus text | opener image/text | high | yes | provisional | Mixed opener should be handled by a later bounded map. |
| 18 | `IMG-G1-VIRAL-RENDER-001-P018` | `6E8F440CEB5F11A4081722ADF5CD65F74E622641884192390E9DA0CAE6C6BFD4` | location/background | text-heavy with multi-block structure | text/multi-block planning | medium | maybe | provisional | Coarse page-level structure only. |
| 19 | `IMG-G1-VIRAL-RENDER-001-P019` | `63BBB963A76F5C266E4A1B139FBCEFD2D390FB23B23CA391E8BAF12A4E9D3AC8` | location/background | portrait image plus text blocks | image/text blocks | high | yes | provisional | No accepted region registry created. |
| 20 | `IMG-G1-VIRAL-RENDER-001-P020` | `53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E` | location/background | text page with scenic image | text/image planning | medium | yes | provisional | Later action needed before OCR routing. |

Recommended next bounded work:

- If continuing toward OCR preparation, request a distinct bounded region-map
  authorization that explicitly decides whether it may create provisional
  region IDs, coordinates, and layer-specific records.
- If testing render parameters first, request a distinct render benchmark
  authorization instead.

Not accepted by this report:

- `doc_map`, `content_map`, `art_map`, `pre_ocr_map_bundle`, stable region IDs,
  anchors, coordinates, bounding boxes, reading order, OCR routing, benchmark
  scores, QA findings, fixture records, source evidence, source-profile
  acceptance, translation, proofreading, or implementation.

Invalidation:

- This report is stale if source path/hash, accepted protocol revision/blob,
  authorization record, `SPM-G1-VIRAL-001`, `RT-G1-VIRAL-RENDER-001`, render
  output manifest/hash, any page PNG/hash, `VSR-G1-VIRAL-001`, contact
  sheet/hash, `PIR-G1-VIRAL-001`, render config, schema/taxonomy, observation
  rules, tooling, reviewer identity, or authority model changes.
