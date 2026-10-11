# Page Complete Review Packet - Page 006

Status: `blocked`

Boundary: this is a review packet only. It does not accept page 006 as complete, does not advance Gate 1, and does not admit fixtures.

## Readiness Input

- Input: `P006-READABLE-MAP-G1-VIRAL-001`.
- Scope: page-map readiness only, using existing artifacts.
- Coverage remains advisory; this packet asks for a separate human decision.

## Page 006 Review

- Expected blocks: 3
- Reviewed blocks: 3
- Ready blocks: 3 / 3
- Reading order: introduction_heading -> left_column_summary_overview_text -> right_column_overview_text
- table/unknown/missing: none identified by the readiness profile.
- Context-only regions: 2.
- Blockers: 2.
- Open questions: none.

## Review Attachments

- source_page_image: `review_assets/page_006.png`
- human_review_crop: `review_assets/1_P006-title__introduction_heading.png`
- human_review_crop: `review_assets/2_P006-left-column__summary_overview.png`
- human_review_crop: `review_assets/3_P006-right-column__overview_continuation.png`
- ocr_verified_text_map_markdown: `review_assets/page_006_ocr_verified_text_map.md`
- semantic_text_map_json: `review_assets/page_006_semantic_text_map.json`
- semantic_text_map_markdown: `review_assets/page_006_semantic_text_map.md`

## Blocks

### P006-B001 - introduction_heading

- Region: `PRM-G1-VIRAL-001-P006-R02`
- Status: `ready_for_page_complete_review`
- Characters: 12 raw / 12 normalized
- Lines: 1 total / 1 non-empty
- Protected tokens: 1 / 1
- Discrepancy: `none`
- Anchor crop: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_006.png`

### P006-B002 - left_column_summary_overview_text

- Region: `PRM-G1-VIRAL-001-P006-R03-L`
- Status: `ready_for_page_complete_review`
- Characters: 1226 raw / 1223 normalized
- Lines: 26 total / 23 non-empty
- Protected tokens: 5 / 5
- Discrepancy: `none`
- Anchor crop: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_006.png`

### P006-B003 - right_column_overview_text

- Region: `PRM-G1-VIRAL-001-P006-R03-R`
- Status: `ready_for_page_complete_review`
- Characters: 1534 raw / 1534 normalized
- Lines: 26 total / 26 non-empty
- Protected tokens: 5 / 5
- Discrepancy: `none`
- Anchor crop: `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_006.png`

## Blockers

- `P006-001-ATT-SEMANTIC-MAP-JSON`: `semantic_validation_blocker`
- `PCRP-G1-VIRAL-P006-001`: `text_map_semantics_and_formatting_blocker`

## Semantic Map Validation

- Semantic units validated: `True`
- Semantic validation: `blocked`
- Markdown projection: `valid`
- Inventory reconciliation: `valid`
- Structural findings: `1`

- `invalid_heading_level` / `SU-HEADING-002` / `blocker`: Only heading units may carry heading_level; quote/body/table/art units must keep it null.

## Post-Review State

- Status: `held_after_bogdan_review`
- Decision: `hold_page_006_text_map_semantics_messages_896_897`
- Reason: `text_map_semantics_and_formatting_blocker`
- Review crops: `ok_as_review_assets_only`
- Requires superseding packet: `PCRP-G1-VIRAL-P006-002`
- Negative regression input: `review_assets/page_006_ocr_verified_text_map.md`

## Decision Needed

Page 006 is blocked before any page-complete decision. A superseding review packet is required.

Reply shape:

```text
hold page 006: <reason>
```

This packet itself creates no acceptance.
