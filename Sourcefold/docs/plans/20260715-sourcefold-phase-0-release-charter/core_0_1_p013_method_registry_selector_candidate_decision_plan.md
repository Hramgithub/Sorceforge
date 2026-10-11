# Core 0.1 P013 Method-Registry Selector Candidate Decision Plan

Status: `p013_method_registry_candidate_decision_recorded`

Lane: `C01TEP013MRS-G1-VIRAL-001`

Authorization: `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-REGISTRY-SELECTOR-001`

## Purpose

Record the P013 SAC winner as a method-registry candidate decision artifact
without enabling selector behavior or creating production output.

This is a P013-only decision record over sealed diagnostic evidence. It does
not copy candidate text into a clean production folder and does not mutate
accepted text, semantic maps, page status, source assets, raw assets, runtime
selector code, method registry runtime files, or page `021+`.

## Inputs

Pinned SAC lane: `C01TEP013SAC-G1-VIRAL-001`

- Report:
  `E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4`
- Summary:
  `353CA98438634BA64347B9FE8F545D3BFE3A8E8FAC002677A2A9D0073A065898`
- Manifest:
  `46343B13144DFBD3C074F7E369A4DDE97F4D2F6540F60341120B5E3DE7CF7212`
- Rankings:
  `613455DDA093EC5F7E01E4F993481D344AB37643257BF5259AC546D5A557D47A`
- Selected candidate text:
  `E24D29CE34A61755E9B92214007EFEB8FEADC4B77D4C35468ACF64DDF9D41DE4`
- Selected normalized candidate:
  `69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D`
- Selected retained trace:
  `4B0628DE7BC5EF395DAAB107F6B6448A230C2E08FA24C0B4005F37FE90389A19`
- Selected suppression ledger:
  `4A54B31E63C66AE28939FAF9A9A63A8F131F19B2E1AD2E0BBA61B29DD96B5F03`
- Selected assembly trace:
  `EC9A97A032A1562C25839AFCD46B15792A6498AAC3FB3D5B14A7B0FEC471C62D`

The reference dependency remains `reference_text_map_not_ocr_verified`; this
winner is scored against a reference map, not independently accepted OCR truth.

## Selected Candidate

Selected: `p013_sac_d_noise_then_declared_seam_fracture`

Metrics:

- Sequence similarity: `0.998915`
- Token recall: `0.993939`
- Threshold: `>=0.997 / >=0.993939`

Tie note:

- `p013_sac_e_paragraph_join_d` has the same normalized hash and metrics.
- `D` is selected because it uses simpler `line_join`; `E` is a separator-only
  equivalent and remains evidence-only.

## Required Outputs

Output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_method_registry_selector_G1_VIRAL_001/`

Files:

- `method_registry_entries/page_013.json`
- `selector_dry_run/page_013_selection.json`
- `p013_method_registry_selector_report.json`
- `p013_method_registry_selector_summary.md`
- `p013_method_registry_selector_manifest.md`

## Required False Flags

Every report, registry entry, and dry-run artifact must keep these effects
false when present:

- `selector_rule_created=false`
- `selector_enabled=false`
- `runtime_selector_integration=false`
- `runtime_implementation_created=false`
- `production_assembly_created=false`
- `accepted_text_mutation_performed=false`
- `semantic_text_mutation_performed=false`
- `page_status_mutation_performed=false`
- `source_or_raw_mutation_performed=false`
- `page_001_020_runtime_loop_created=false`
- `page_021_plus_included=false`

## Tests

Focused test target:

`pytest tests/test_core_0_1_text_extraction_p013_method_registry_selector.py`

The tests cover fail-closed authorization, pinned SAC hashes, selected
candidate schema, D/E tie handling, static selector dry-run boundaries,
negative capabilities, and output manifest coverage.

## Result

Generated `C01TEP013MRS-G1-VIRAL-001` under
`core_0_1_text_extraction_p013_method_registry_selector_G1_VIRAL_001`.

Selected entry:

- `C01TEP013MRS-G1-VIRAL-001-P013`
- `p013_sac_d_noise_then_declared_seam_fracture`
- Similarity/token recall: `0.998915 / 0.993939`

Output hashes:

- `method_registry_entries/page_013.json`:
  `B09BF185510557CDAF3E757D381A416E2DEE52A8430B93E8293A348ACD6A56EC`
- `selector_dry_run/page_013_selection.json`:
  `A439914FC0AE585DF52A69CA6F6BEDA3B7E19644B0B28D5550517192B57432D7`
- `p013_method_registry_selector_report.json`:
  `988FA33843EE0E35F70562E227BE7FA613CD7715982AC5FEA4BE4D3F9847B520`
- `p013_method_registry_selector_summary.md`:
  `ADDD20D6C2761623AC56BD30C1B45170717D1C94617D46AE464F17995F7C1A62`

Post-run checks:

- Focused P013 MRS tests: `5 passed`
- Roadmap validator: `222` checkpoints, passed
- `git diff --check -- Sourcefold`: clean

## Next Packets

Allowed next packets only if separately reviewed and authorized:

- `p013_selector_integration_prep_if_separately_authorized`
- `core_0_1_first_pass_001_020_selector_loop_prep_if_separately_authorized`
