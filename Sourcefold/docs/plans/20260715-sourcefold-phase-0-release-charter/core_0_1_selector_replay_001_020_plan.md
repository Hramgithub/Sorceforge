# Core 0.1 Static Selector Replay 001-020 Plan

Lane: `C01TESEL020-G1-VIRAL-001`

Authorization: `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SELECTOR-REPLAY-001-020-001`

## Objective

Create a static `001`-`020` selector replay/report that combines the old
`C01TEOR020-G1-VIRAL-001` overview evidence with the new P013 method-registry
candidate decision `C01TEP013MRS-G1-VIRAL-001-P013`.

This is a no-OCR, no-production replay over sealed artifacts. It proves which
pages can currently be selected and which pages remain blocked without copying
candidate text into a production folder.

## Required Routing

- `001`-`008`: `not_run_ineligible`.
- `009`, `010`, `011`, `015`: `selected_frozen_baseline` from
  `C01TEOR020-G1-VIRAL-001` hashes.
- `013`: `selected_p013_mrs_candidate` from
  `C01TEP013MRS-G1-VIRAL-001-P013`.
- `012`, `016`, `017`, `018`, `020`: `unresolved_needs_method_winner`.
- `014`, `019`: `parked_candidate_policy`.

## Boundary

- No OCR execution.
- No render execution.
- No PDF parsing or text-layer extraction.
- No reference-guided repair or reference-token insertion.
- No candidate text copy.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No selector runtime enablement or runtime selector integration.
- No production assembly or clean production output folder.
- No page `021+`.
- No translation/proofreading, push, promotion, acceptance, or downstream
  execution.

## Tests

- Fail closed without `--execute`, the exact authorization id, and exact human
  decision.
- Assert exact page routing for all twenty pages.
- Assert baseline-selected pages carry selected output hashes from
  `C01TEOR020-G1-VIRAL-001`.
- Assert P013 selects `C01TEP013MRS-G1-VIRAL-001-P013` and records the
  unselected equivalent plus failed variants.
- Assert unresolved and parked pages are not selected.
- Assert no failed or superseded candidate is selected.
- Assert all boundary flags remain false.
- Assert pinned input hashes match.

## Status

Generated `C01TESEL020-G1-VIRAL-001` under
`core_0_1_text_extraction_selector_replay_001_020_G1_VIRAL_001`.

Result:

- Selected pages: `009`, `010`, `011`, `013`, `015`.
- Not-run ineligible: `001`-`008`.
- Unresolved: `012`, `016`, `017`, `018`, `020`.
- Parked: `014`, `019`.
- Production ready: `false`.
- All pages first-pass success: `false`.
- Failed or superseded candidates selected: `false`.

Generated output hashes:

- Report:
  `5EF728BE91FA609C44591C104ACC21766F4F184217DF2E01FC151A3504BA75AF`
- Selections:
  `17EEE268DA1972CF89FFC643F1BCBEC35D56DE1D959C223D2E15E769D0A0372F`
- Summary:
  `583AD80F57D1ED68496F3D3872F59F796D00A811D409A514D8FA570792976210`
