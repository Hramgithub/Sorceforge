# Core 0.1 P012/P016/P020 Method Family Plan

Lane: `C01TEMF012016020-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-012-016-020-METHOD-FAMILY-001`

## Objective

Create a bounded method-family dry-run for the remaining unresolved pages
`012`, `016`, and `020` after `C01TEUNRES020-G1-VIRAL-001`.

The builder generates fixed OCR candidates from full-page PNG geometry,
hash-seals candidate text before reference scoring, records static method
entries only for threshold-passing candidates, and creates selector replay v3.

This is not a production assembly and not runtime selector integration.

## Method Families

- `012`: full-column scale2 PSM6 OCR over left and right text columns.
- `016`: expanded bottom geometry plus TSV confidence filtering at `60`.
- `020`: scale2 threshold-180 PSM6 OCR plus source-derived Roll/Rumor table
  normalization.

## Boundaries

- OCR execution is allowed only for bounded candidate generation on pages
  `012`, `016`, and `020`.
- Candidate hashes are sealed before reference text is loaded for scoring.
- No reference-token insertion.
- No render execution.
- No PDF parsing or text-layer extraction.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No selector runtime enablement or runtime selector integration.
- No production assembly or clean production output folder.
- No page `021+`.
- No promotion, acceptance, push, translation/proofreading, or downstream
  execution.

## Expected Result

- Input unresolved pages: `012`, `016`, `020`.
- New static method entries: `012`, `016`, `020` if all three method-family
  candidates meet threshold.
- Selector replay v3 selected pages:
  `009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, `020`.
- Parked pages remain: `014`, `019`.
- Pages `001`-`008` remain not-run/ineligible.
- Production ready remains `false`.
- All pages first-pass success remains `false` until a separate production
  assembly layer is reviewed.

## Status

Generated. `C01TEMF012016020-G1-VIRAL-001` selected static method entries for
all three input pages:

- `012`: `p012_full_columns_scale2_psm6` at similarity/token recall `1.0/1.0`.
- `016`: `p016_expanded_bottom_conf60_scale2_psm6` at `0.99975/0.99802`.
- `020`: `p020_table_normalized_scale2_threshold180_psm6` at `0.99979/1.0`.

Selector replay v3 selects
`009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, and `020`.
Pages `001`-`008` remain not-run/ineligible; pages `014` and `019` remain
parked. Production remains blocked:
`production_ready=false` and `all_pages_first_pass_success=false`.
