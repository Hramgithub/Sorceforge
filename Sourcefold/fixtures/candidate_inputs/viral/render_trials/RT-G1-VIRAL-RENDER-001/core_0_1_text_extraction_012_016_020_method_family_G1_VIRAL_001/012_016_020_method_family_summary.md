# P012/P016/P020 Method Family - C01TEMF012016020-G1-VIRAL-001

Status: `method_family_candidates_selected_static_evidence_only`

This dry-run generates bounded OCR candidates for pages `012`, `016`, and `020`, seals candidate hashes before reference scoring, and records static method entries for selector replay v3.

Selected pages v3: `009, 010, 011, 012, 013, 015, 016, 017, 018, 020`.
Production ready: `false`.
All pages first-pass success: `false`.

| Page | Entry | Candidate | Similarity | Token recall |
|---|---|---|---:|---:|
| `012` | `C01TEMF012016020-G1-VIRAL-001-P012` | `p012_full_columns_scale2_psm6` | `1.0` | `1.0` |
| `016` | `C01TEMF012016020-G1-VIRAL-001-P016` | `p016_expanded_bottom_conf60_scale2_psm6` | `0.99975` | `0.99802` |
| `020` | `C01TEMF012016020-G1-VIRAL-001-P020` | `p020_table_normalized_scale2_threshold180_psm6` | `0.99979` | `1.0` |

## Boundary Flags

- `ocr_execution_performed=true` and scoped only to pages `012`, `016`, `020` candidate generation.
- `candidate_generation_reference_text_used=false`.
- `reference_text_loaded_after_candidate_hashing=true`.
- `reference_token_insertion_performed=false`.
- `production_assembly_created=false`.
- `accepted_text_mutation_performed=false`.
- `semantic_text_mutation_performed=false`.
- `page_status_mutation_performed=false`.
- `source_or_raw_mutation_performed=false`.
- `page_021_plus_included=false`.
- `promotion_performed=false`.
- `acceptance_performed=false`.
- `downstream_execution_performed=false`.
