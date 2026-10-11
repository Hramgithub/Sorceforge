# Core 0.1 Assembly Readiness 001-020 Plan

Lane: `C01TEASM020-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ASSEMBLY-READINESS-001-020-001`

## Objective

Create a manifest-only, hash-reference-only assembly-readiness dry-run after
`C01TEMF012016020-G1-VIRAL-001`.

The builder consumes selector replay v3 and writes a selected-page manifest for
the static evidence currently selected inside pages `001`-`020`.

This is not a production assembly. It does not copy candidate text and does not
create a clean production output folder.

## Inputs

- `C01TEMF012016020-G1-VIRAL-001` report.
- `C01TEMF012016020-G1-VIRAL-001` summary.
- `C01TEMF012016020-G1-VIRAL-001` selector replay v3.
- `C01TEMF012016020-G1-VIRAL-001` method entries for `012`, `016`, and `020`.
- Hash-pinned selected output hashes for `009`, `010`, `011`, `012`, `013`,
  `015`, `016`, `017`, `018`, and `020`.

## Expected Outputs

Output root:
`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001/`

Required files:

- `assembly_readiness_001_020_report.json`
- `assembly_readiness_001_020_summary.md`
- `assembly_readiness_001_020_manifest.md`
- `assembly_manifest/selected_pages_manifest.json`

## Boundaries

- Manifest-only and hash-reference-only.
- No candidate text copy and no inline candidate text.
- No production assembly.
- No clean production output folder.
- No OCR execution.
- No render execution.
- No PDF parsing or text-layer extraction.
- No reference-token insertion.
- No accepted text, semantic map, page-status, source, or raw mutation.
- No selector runtime enablement or runtime selector integration.
- No runtime execution.
- No page `021+`.
- No promotion, acceptance, push, translation/proofreading, or downstream
  execution.

## Expected Result

- Selected manifest pages:
  `009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, and `020`.
- Not-run/ineligible pages remain:
  `001`, `002`, `003`, `004`, `005`, `006`, `007`, and `008`.
- Parked pages remain: `014` and `019`.
- Failed, weak, parked, or superseded candidates are not included in the
  selected manifest.
- `production_ready=false`.
- `all_pages_first_pass_success=false`.
- `production_assembly_created=false`.
- `clean_production_output_folder_created=false`.

## Reference Risk

Several selected pages still depend on `reference_text_map_not_ocr_verified`.
This lane records static evidence only. It does not accept source text, page
status, source profiles, or production readiness.

## Status

Generated. `C01TEASM020-G1-VIRAL-001` wrote a manifest-only selected-page
readiness report.

- Selected manifest pages:
  `009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, and `020`.
- Excluded/blocking pages:
  `001`, `002`, `003`, `004`, `005`, `006`, `007`, `008`, `014`, and `019`.
- Not-run/ineligible pages remain `001`-`008`.
- Parked pages remain `014` and `019`.
- No candidate text was copied or inlined.
- `production_ready=false`.
- `all_pages_first_pass_success=false`.
- `production_assembly_created=false`.
- `clean_production_output_folder_created=false`.
