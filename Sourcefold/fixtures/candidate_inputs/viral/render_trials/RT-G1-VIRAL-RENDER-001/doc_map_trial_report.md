# Trial Doc Map - DM-G1-VIRAL-001

Map id: `DM-G1-VIRAL-001`

Status: `valid_for_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-DOCMAP-001`

Schema: `doc_map.v0` from `MSID-G1-VIRAL-001`

Baseline commit: `8fff7fc5bd7e384374835bf9af6195aa91f6991a`

Purpose: create a non-accepting trial page/region registry for future
`content_map` and `art_map` trials.

Boundary: this is not accepted `doc_map`, source evidence, source-profile
acceptance, accepted anchors, accepted coordinates, accepted reading order, OCR
routing, QA, benchmark, fixture, translation, proofreading, renderer/profile
acceptance, implementation, or `pre_ocr_map_bundle`.

Method: derive trial page IDs and trial region ID ranges from already recorded
SPM/RT/VSR/PIR/PMR/PRM predecessors and `MSID-G1-VIRAL-001`. The PDF was not
opened, parsed, rehashed, recounted, or inspected. No OCR, transcription,
copied source text, or PDF text-layer extraction was performed.

## Predecessors

| Evidence | ID | SHA-256 / revision |
|---|---|---|
| Accepted protocol revision | `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a` | file blob `4d494e83d8d63dd3778a3813b3ee529449cee51a` |
| Baseline commit | `8fff7fc5bd7e384374835bf9af6195aa91f6991a` | commit |
| Map schema/identity packet | `MSID-G1-VIRAL-001` | `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024` |
| Selected-page manifest | `SPM-G1-VIRAL-001` | `73D6C817E54DDEFB89BA7109440E87F36B447F74C19044D154A0674AD41E3936` |
| Render output manifest | `RT-G1-VIRAL-RENDER-001` | `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC` |
| Visual sanity report | `VSR-G1-VIRAL-001` | `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439` |
| Page inventory report | `PIR-G1-VIRAL-001` | `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA` |
| Page map/model report | `PMR-G1-VIRAL-001` | `72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F` |
| Provisional region map report | `PRM-G1-VIRAL-001` | `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C` |

## Identity Rules Used

- Page IDs: `PG-G1-VIRAL-P001` through `PG-G1-VIRAL-P020`.
- Trial region IDs: `RG-G1-VIRAL-P{page:000}-R{region:000}`.
- PRM IDs are provenance only and are not canonical identity.
- Coordinate values remain inherited/provisional; this trial doc map records
  registry coverage, not accepted coordinates.

## Page Registry

| Page | Page id | Gross role candidate | Trial region id range | Region count | PRM provenance range | Review state |
|---:|---|---|---|---:|---|---|
| 1 | `PG-G1-VIRAL-P001` | `cover_or_landing` | `RG-G1-VIRAL-P001-R001`..`RG-G1-VIRAL-P001-R003` | 3 | `PRM-G1-VIRAL-001-P001-R01`..`R03` | `valid_for_review` |
| 2 | `PG-G1-VIRAL-P002` | `credits_legal_front_matter` | `RG-G1-VIRAL-P002-R001`..`RG-G1-VIRAL-P002-R002` | 2 | `PRM-G1-VIRAL-001-P002-R01`..`R02` | `valid_for_review` |
| 3 | `PG-G1-VIRAL-P003` | `front_matter_intro` | `RG-G1-VIRAL-P003-R001`..`RG-G1-VIRAL-P003-R002` | 2 | `PRM-G1-VIRAL-001-P003-R01`..`R02` | `valid_for_review` |
| 4 | `PG-G1-VIRAL-P004` | `inset_document_like` | `RG-G1-VIRAL-P004-R001`..`RG-G1-VIRAL-P004-R003` | 3 | `PRM-G1-VIRAL-001-P004-R01`..`R03` | `valid_for_review` |
| 5 | `PG-G1-VIRAL-P005` | `contents_table_like` | `RG-G1-VIRAL-P005-R001`..`RG-G1-VIRAL-P005-R003` | 3 | `PRM-G1-VIRAL-001-P005-R01`..`R03` | `valid_for_review` |
| 6 | `PG-G1-VIRAL-P006` | `chapter_or_intro_opener` | `RG-G1-VIRAL-P006-R001`..`RG-G1-VIRAL-P006-R003` | 3 | `PRM-G1-VIRAL-001-P006-R01`..`R03` | `valid_for_review` |
| 7 | `PG-G1-VIRAL-P007` | `profile_or_mixed_page` | `RG-G1-VIRAL-P007-R001`..`RG-G1-VIRAL-P007-R004` | 4 | `PRM-G1-VIRAL-001-P007-R01`..`R04` | `valid_for_review` |
| 8 | `PG-G1-VIRAL-P008` | `mixed_text_art_page` | `RG-G1-VIRAL-P008-R001`..`RG-G1-VIRAL-P008-R004` | 4 | `PRM-G1-VIRAL-001-P008-R01`..`R04` | `valid_for_review` |
| 9 | `PG-G1-VIRAL-P009` | `dual_profile_page` | `RG-G1-VIRAL-P009-R001`..`RG-G1-VIRAL-P009-R004` | 4 | `PRM-G1-VIRAL-001-P009-R01`..`R04` | `valid_for_review` |
| 10 | `PG-G1-VIRAL-P010` | `dual_profile_mixed_page` | `RG-G1-VIRAL-P010-R001`..`RG-G1-VIRAL-P010-R005` | 5 | `PRM-G1-VIRAL-001-P010-R01`..`R05` | `valid_for_review` |
| 11 | `PG-G1-VIRAL-P011` | `mixed_text_art_page` | `RG-G1-VIRAL-P011-R001`..`RG-G1-VIRAL-P011-R004` | 4 | `PRM-G1-VIRAL-001-P011-R01`..`R04` | `valid_for_review` |
| 12 | `PG-G1-VIRAL-P012` | `two_column_text_page` | `RG-G1-VIRAL-P012-R001`..`RG-G1-VIRAL-P012-R002` | 2 | `PRM-G1-VIRAL-001-P012-R01`..`R02` | `valid_for_review` |
| 13 | `PG-G1-VIRAL-P013` | `text_plus_dominant_art_page` | `RG-G1-VIRAL-P013-R001`..`RG-G1-VIRAL-P013-R002` | 2 | `PRM-G1-VIRAL-001-P013-R01`..`R02` | `valid_for_review` |
| 14 | `PG-G1-VIRAL-P014` | `mixed_list_art_page` | `RG-G1-VIRAL-P014-R001`..`RG-G1-VIRAL-P014-R003` | 3 | `PRM-G1-VIRAL-001-P014-R01`..`R03` | `valid_for_review` |
| 15 | `PG-G1-VIRAL-P015` | `timeline_or_list_mixed_page` | `RG-G1-VIRAL-P015-R001`..`RG-G1-VIRAL-P015-R003` | 3 | `PRM-G1-VIRAL-001-P015-R01`..`R03` | `valid_for_review` |
| 16 | `PG-G1-VIRAL-P016` | `two_column_text_page` | `RG-G1-VIRAL-P016-R001`..`RG-G1-VIRAL-P016-R002` | 2 | `PRM-G1-VIRAL-001-P016-R01`..`R02` | `valid_for_review` |
| 17 | `PG-G1-VIRAL-P017` | `section_opener_mixed_page` | `RG-G1-VIRAL-P017-R001`..`RG-G1-VIRAL-P017-R003` | 3 | `PRM-G1-VIRAL-001-P017-R01`..`R03` | `valid_for_review` |
| 18 | `PG-G1-VIRAL-P018` | `two_column_text_page` | `RG-G1-VIRAL-P018-R001`..`RG-G1-VIRAL-P018-R003` | 3 | `PRM-G1-VIRAL-001-P018-R01`..`R03` | `valid_for_review` |
| 19 | `PG-G1-VIRAL-P019` | `mixed_portrait_text_page` | `RG-G1-VIRAL-P019-R001`..`RG-G1-VIRAL-P019-R003` | 3 | `PRM-G1-VIRAL-001-P019-R01`..`R03` | `valid_for_review` |
| 20 | `PG-G1-VIRAL-P020` | `mixed_body_sidebar_page` | `RG-G1-VIRAL-P020-R001`..`RG-G1-VIRAL-P020-R004` | 4 | `PRM-G1-VIRAL-001-P020-R01`..`R04` | `valid_for_review` |

Total trial regions: 62.

## Payload Leakage Check

Result: `passed_for_trial_doc_map`

Checked boundaries:

- No OCR output.
- No copied source text.
- No PDF text-layer content or order.
- No translated/proofread text.
- No gold sample text.
- No accepted reading order.
- No accepted coordinates or anchors.
- No source-profile acceptance.
- No bundle freeze.

## Next Bounded Work

The next step may request `BA-G1-VIRAL-CONTENTMAP-001` to create a
non-accepting trial `content_map` referencing `DM-G1-VIRAL-001` and
`MSID-G1-VIRAL-001`. This report does not authorize that action.

## Invalidation

This report is stale if protocol revision/blob changes, baseline commit is
superseded, authorization changes, `MSID-G1-VIRAL-001` changes, any listed
predecessor identity/hash changes, page or region namespace changes, coordinate
basis changes, payload-leakage rules change, observation/review rules change,
or a later doc-map remediation supersedes this artifact.
