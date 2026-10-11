# Core 0.1 Assembly Authorization 001-020 Plan

Lane: `C01TEAUTH020-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ASSEMBLY-AUTHORIZATION-001-020-001`

## Objective

Create a report-only final assembly-authorization check after
`C01TEBRIDGE020-G1-VIRAL-001`.

This lane answers whether selector replay v4 is enough to create production
output. It is not a production builder and does not copy candidate text.

## Inputs

- `C01TEBRIDGE020-G1-VIRAL-001` report.
- `C01TEBRIDGE020-G1-VIRAL-001` summary.
- `C01TEBRIDGE020-G1-VIRAL-001` bridge entries.
- `C01TEBRIDGE020-G1-VIRAL-001` selector replay v4.

## Expected Outputs

Output root:
`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_assembly_authorization_001_020_G1_VIRAL_001/`

Required files:

- `assembly_authorization_001_020_report.json`
- `assembly_authorization_001_020_summary.md`
- `assembly_authorization_001_020_manifest.md`

## Boundaries

- Report-only authorization check.
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

- Selector replay v4 covers all pages `001`-`020`.
- `all_pages_static_evidence_covered=true`.
- `all_pages_first_pass_success=false`.
- Mixed static evidence plus accepted bridge is recognized explicitly.
- `production_ready=false`.
- `production_assembly_authorized=false`.
- `production_assembly_created=false`.
- `clean_production_output_folder_created=false`.

## Decision Rule

Production assembly is not authorized from mixed static evidence while
`all_pages_first_pass_success=false`.

The standard production route remains a fresh first-pass runtime selector
success for pages `001`-`020`. The only alternative route is a separate
explicit human exception decision for mixed static evidence production.

## Status

Generated. `C01TEAUTH020-G1-VIRAL-001` wrote a report-only final
assembly-authorization check.

- Selector replay v4 covers all pages `001`-`020`.
- `all_pages_static_evidence_covered=true`.
- `all_pages_first_pass_success=false`.
- Mixed static evidence plus accepted bridge is recorded explicitly.
- Production assembly from mixed static evidence is not authorized while
  `all_pages_first_pass_success=false`.
- `production_ready=false`.
- `production_assembly_authorized=false`.
- `production_assembly_created=false`.
- `clean_production_output_folder_created=false`.
