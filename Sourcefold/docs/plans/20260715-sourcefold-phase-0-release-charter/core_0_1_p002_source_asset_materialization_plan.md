## Core 0.1 P002 Source Asset Materialization

Lane: `C01TEP002ASSETMAT-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-MATERIALIZATION-001`

Status:
`p002_source_asset_materialization_completed_output_surface_only_no_blocker_clearance_no_mutation`.

Scope:

- Consume committed `C01TEP002ASSETMATAUTH-G1-VIRAL-001` and
  `C01TEP002ASSETREC-G1-VIRAL-001` artifacts by exact hash.
- Materialize only page `002` source asset surface copies into a new
  lane-owned output root.
- Preserve `stale_generator_hash_in_completion_artifact` as an authority risk.
- Keep `bridge_blocker_cleared=false`.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_source_asset_materialization_G1_VIRAL_001/`

Allowed materialized assets:

- `materialized_surface/page_002.png`
- `materialized_surface/1_SRAD-G1-VIRAL-002-R01__SRAD-G1-VIRAL-002-R01-C01.png`
- `materialized_surface/2_SRAD-G1-VIRAL-002-R02__SRAD-G1-VIRAL-002-R02-C01.png`

Boundaries:

- Do not write into historical `page_complete_review_p002_G1_VIRAL_001/review_assets/`.
- Do not clear bridge blocker, accept source/page status, run OCR/Tesseract,
  render or parse PDFs, mutate source/raw/accepted/page-status files, admit
  fixtures, assemble production, include page `021+`, push, promote, or trigger
  downstream execution.

Output hashes:

- Report:
  `82D51C020E5571C7FDB86040CC0E3469EC0CE26A1C4A49286B0135E13A39315F`
- Summary:
  `3962117A4EE8737788B0FE60ADB57C4BB9E5338ABDE03835E1B56BEBD732B038`
- Manifest:
  `8F32E3FBEB3B671857B65FCD769627B8545F471B4E5F8DDF062D4FDDFD62EFE6`
