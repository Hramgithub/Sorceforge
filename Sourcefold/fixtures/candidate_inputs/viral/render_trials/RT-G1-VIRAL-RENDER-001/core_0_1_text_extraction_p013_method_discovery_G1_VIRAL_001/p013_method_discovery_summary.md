# P013 Cold-Start Method Discovery - C01TEP013DISC-G1-VIRAL-001

Status: `p013_method_discovered_without_mrs_registry_input`

This discovery does not use the prior P013 MRS registry entry. It ranks available P013 diagnostic method-family artifacts and creates a fresh discovered entry for dry-run selector use.

Discovered entry: `C01TEP013DISC-G1-VIRAL-001-P013`.
Selected lane: `C01TEP013SAC-G1-VIRAL-001`.
Selected candidate: `p013_sac_d_noise_then_declared_seam_fracture`.
Selection rule: `highest_threshold_met_method_registry_candidate_then_similarity_then_token_recall_then_line_join_tie_break_then_candidate_id`.
Similarity: `0.998915`.
Token recall: `0.993939`.

## Ranking

| Rank | Lane | Candidate | Similarity | Token recall | Threshold | Registry candidate |
|---:|---|---|---:|---:|---|---|
| 1 | `C01TEP013SAC-G1-VIRAL-001` | `p013_sac_d_noise_then_declared_seam_fracture` | `0.998915` | `0.993939` | `True` | `True` |
| 2 | `C01TEP013SAC-G1-VIRAL-001` | `p013_sac_e_paragraph_join_d` | `0.998915` | `0.993939` | `True` | `True` |
| 3 | `C01TEP013SAC-G1-VIRAL-001` | `p013_sac_c_declared_seam_fracture_after_ssp` | `0.99219` | `0.993939` | `False` | `False` |
| 4 | `C01TEP013SAC-G1-VIRAL-001` | `p013_sac_b_noise_after_ssp` | `0.92015` | `0.993939` | `False` | `False` |
| 5 | `C01TEP013SAC-G1-VIRAL-001` | `p013_sac_a0_ssp_best_baseline` | `0.914027` | `0.993939` | `False` | `False` |
| 6 | `C01TEP013SSP-G1-VIRAL-001` | `p013_ssp_a_near_overlap_confidence` | `0.914027` | `0.993939` | `False` | `False` |
| 7 | `C01TEP013SSP-G1-VIRAL-001` | `p013_ssp_b_noise_from_a0` | `0.436181` | `0.993939` | `False` | `False` |
| 8 | `C01TEP013SSP-G1-VIRAL-001` | `p013_ssp_c_floor_guarded_near_overlap_then_noise` | `0.433325` | `0.993939` | `False` | `False` |
| 9 | `C01TEP013SSP-G1-VIRAL-001` | `p013_ssp_a0_elo_exact_collapse_baseline` | `0.433325` | `0.993939` | `False` | `False` |
| 10 | `C01TEP013ELO-G1-VIRAL-001` | `p013_expanded_lane_order_lane_then_y_exact_collapse` | `0.433325` | `0.993939` | `False` | `False` |
| 11 | `C01TEP013SDD-G1-VIRAL-001` | `sealed_raw_v2_window160_prefix_exact_dedupe` | `0.25788` | `0.993939` | `False` | `False` |
| 12 | `C01TEP013SDD-G1-VIRAL-001` | `sealed_raw_v1_max_tail_prefix_exact_dedupe` | `0.25788` | `0.993939` | `False` | `False` |
| 13 | `C01TEP013GNO-G1-VIRAL-001` | `p013_geo_noexp_5box_triage_order` | `0.251286` | `0.987879` | `False` | `False` |
| 14 | `C01TEP013GNO-G1-VIRAL-001` | `p013_geo_noexp_4unit_triage_logical_order` | `0.251286` | `0.987879` | `False` | `False` |
| 15 | `C01TEP013GNO-G1-VIRAL-001` | `p013_geo_noexp_4unit_column_order_control` | `0.251286` | `0.987879` | `False` | `False` |
| 16 | `C01TEP013ELO-G1-VIRAL-001` | `p013_expanded_lane_order_source_region_baseline` | `0.242772` | `0.993939` | `False` | `False` |
| 17 | `C01TEP013ELO-G1-VIRAL-001` | `p013_expanded_lane_order_lane_then_y` | `0.242772` | `0.993939` | `False` | `False` |
| 18 | `C01TEP013ELO-G1-VIRAL-001` | `p013_expanded_lane_order_band_then_lane` | `0.08596` | `0.993939` | `False` | `False` |

## Boundary Flags

- `mrs_registry_input_used=false`.
- `ocr_execution_performed=false`.
- `production_assembly_created=false`.
- `accepted_text_mutation_performed=false`.
- `page_001_020_runtime_loop_created=false`.
- `page_021_plus_included=false`.
- `promotion_performed=false`.
- `acceptance_performed=false`.
- `downstream_execution_performed=false`.

Boundary: no OCR/render/PDF/text-layer execution, no reference-token insertion, no accepted/semantic/page-status/source/raw mutation, no runtime selector integration, no production assembly, no page 001-020 runtime loop, no page 021+, no promotion, no acceptance, and no downstream execution.
