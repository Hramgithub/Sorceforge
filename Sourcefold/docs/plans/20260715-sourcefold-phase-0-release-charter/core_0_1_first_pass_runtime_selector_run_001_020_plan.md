# Core 0.1 First-Pass Runtime Selector Run 001-020 Plan

Lane: `C01TEFPSRUN020-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FIRST-PASS-RUNTIME-SELECTOR-RUN-001-020-001`

## Objective

Execute the bounded `001`-`020` runtime selector route authorized by
`C01TEFPSAUTH020-G1-VIRAL-001` and materialize a clean output surface for the
selected page results.

This is real runtime/output work, not another denial packet. It must still keep
the distinction between fresh OCR execution and page-complete bridge lineage.

## Boundaries

- Page set is exactly `001`-`020`.
- No page `021+`.
- No source/raw mutation.
- No accepted text, semantic map, or page-status mutation.
- No fixture admission.
- No whole Gate 1 acceptance.
- No translation, proofreading, push, or downstream execution.
- Failed and superseded variants must not enter the output surface.

## Expected Result

- Per-page output files are materialized for pages `001`-`020`.
- Runtime selected pages are `009`, `010`, `011`, `012`, `013`, `015`, `016`,
  `017`, `018`, and `020`.
- Fresh OCR is executed in this lane only for pages with an executable selected
  baseline route: `009`, `010`, `011`, and `015`.
- Hash-pinned selected candidate text is materialized for selected method
  entries whose candidate artifact already exists: `012`, `013`, `016`, `017`,
  `018`, and `020`.
- Page-complete bridge pages are materialized as bridge lineage records, not as
  fresh OCR success: `001`-`008`, `014`, and `019`.
- `runtime_execution_performed=true`.
- `runtime_output_surface_created=true`.
- `all_pages_materialized=true`.
- `all_pages_fresh_ocr_success=false` while bridge lineage remains.
- `production_ready=false` and `production_assembly_authorized=false` until a
  separate decision accepts this mixed runtime/bridge output surface.

## Required Guardrails

- Pin `C01TEFPSAUTH020`, `C01TEAUTH020`, selector replay v4, assembly readiness
  selected-page manifest, bridge entries, and every selected candidate text or
  acceptance report consumed for materialization.
- Fail closed on hash drift, output root overwrite, page-set drift, page `021+`,
  missing selected artifacts, or any output outside the lane output root.
- Generated tests must inspect actual page files, not only report flags.

## Status

Generated. `C01TEFPSRUN020-G1-VIRAL-001` materialized the bounded runtime
output surface for pages `001`-`020`.

- Output page files created: `20`.
- Runtime selected pages: `009`, `010`, `011`, `012`, `013`, `015`, `016`,
  `017`, `018`, and `020`.
- Bridge lineage pages: `001`-`008`, `014`, and `019`.
- `all_pages_materialized=true`.
- `all_pages_fresh_ocr_success=false`.
- `runtime_execution_performed=true`.
- `runtime_output_surface_created=true`.
- `production_ready=false`.
- `production_assembly_authorized=false`.
- `acceptance_performed=false`.
- No source/raw/accepted/page-status mutation, fixture admission, whole Gate 1
  acceptance, or page `021+` output was created.
