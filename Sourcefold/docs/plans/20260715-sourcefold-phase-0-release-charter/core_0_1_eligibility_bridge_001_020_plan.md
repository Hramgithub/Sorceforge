# Core 0.1 Eligibility Bridge 001-020 Plan

Lane: `C01TEBRIDGE020-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ELIGIBILITY-BRIDGE-001-020-001`

## Objective

Create a dry-run policy bridge for pages `001`-`008`, `014`, and `019` after
`C01TEASM020-G1-VIRAL-001`.

This lane checks whether older page-complete acceptance artifacts can be
hash-pinned into the current static selector surface without pretending they
were produced by the new first-pass OCR selector.

## Inputs

- `C01TEASM020-G1-VIRAL-001` assembly-readiness report.
- `C01TEASM020-G1-VIRAL-001` selected-page manifest.
- Page-complete acceptance reports for pages `001`-`008`, `014`, and `019`.

## Expected Outputs

Output root:
`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_eligibility_bridge_001_020_G1_VIRAL_001/`

Required files:

- `eligibility_bridge_001_020_report.json`
- `eligibility_bridge_001_020_summary.md`
- `eligibility_bridge_001_020_manifest.md`
- `bridge_entries/accepted_page_complete_bridge_entries.json`
- `selector_replay_v4/selector_replay_v4_selections.json`

## Boundaries

- Static bridge/report only.
- No OCR execution.
- No render execution.
- No PDF parsing or text-layer extraction.
- No reference-token insertion.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No selector runtime enablement or runtime selector integration.
- No runtime execution.
- No production assembly or clean production output folder.
- No page `021+`.
- No promotion, acceptance, push, translation/proofreading, or downstream
  execution.

## Expected Result

- Pages `001`-`008` classify as `accepted_page_complete_bridge` when their
  page-complete-only acceptance reports are hash-pinned.
- Pages `014` and `019` classify as
  `parked_overview_but_page_complete_accepted_bridge` when their acceptance
  artifacts are hash-pinned.
- Selector replay v4 covers all pages `001`-`020` with static evidence.
- `all_pages_static_evidence_covered=true`.
- `all_pages_first_pass_success=false`, because the coverage includes imports
  from prior accepted lanes, not a fresh first-pass OCR selector run.
- `production_ready=false`.
- `production_assembly_created=false`.
- `clean_production_output_folder_created=false`.

## Status

Generated. `C01TEBRIDGE020-G1-VIRAL-001` verified hash-pinned page-complete
acceptance reports for all bridge pages.

- `001`-`008`: `accepted_page_complete_bridge`.
- `014` and `019`: `parked_overview_but_page_complete_accepted_bridge`.
- Selector replay v4 covers all pages `001`-`020` with static evidence.
- `all_pages_static_evidence_covered=true`.
- `all_pages_first_pass_success=false`.
- `production_ready=false`.
- `production_assembly_created=false`.
- `clean_production_output_folder_created=false`.
