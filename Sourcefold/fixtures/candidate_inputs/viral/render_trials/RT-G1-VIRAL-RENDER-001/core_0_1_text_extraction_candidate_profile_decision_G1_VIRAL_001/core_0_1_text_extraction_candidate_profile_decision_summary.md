# Core 0.1 Text Extraction Candidate Profile Decision - C01TECPD-G1-VIRAL-001

Status: `text_extraction_candidate_profile_decision_recorded_candidate_profile_frozen`

`trim_mask_psm4` is frozen as a Core 0.1 text extraction candidate profile for future config/replay work only.

This is not OCR acceptance, source-profile acceptance, accepted text, semantic acceptance, page-status mutation, runtime profile lock, or runtime implementation authorization.

## Candidate Profile

- Candidate: `trim_mask_psm4`.
- Preprocessing variant: `edge_mask_trim`.
- Tesseract PSM: `4`.
- Tesseract OEM: `1`.
- Language: `eng`.
- Scope: `Core_0_1_text_extraction_candidate_profile_only`.

## Evidence Ladder

| Evidence | Page | Role | Reference | Similarity | Token recall |
|---|---:|---|---|---:|---:|
| `C01TESRM-G1-VIRAL-001` | `009` | `remediation_selection` | `reference_ocr_verified_text_map` | `0.9993` | `0.996324` |
| `C01TESP010-G1-VIRAL-001` | `010` | `same_profile_generalization` | `reference_ocr_verified_text_map` | `0.998867` | `0.995825` |
| `C01TESP015-G1-VIRAL-001` | `015` | `same_profile_ladder_evidence` | `reference_text_map_not_ocr_verified` | `0.997252` | `0.993985` |

## Decision

- Candidate profile decision recorded: `true`.
- Candidate profile freeze granted: `true`.
- Decision outcome: `freeze_trim_mask_psm4_as_candidate_profile_for_future_config_and_replay_only`.
- Minimum ladder similarity: `0.997252`.
- Minimum ladder token recall: `0.993985`.

## Boundary

- OCR execution in this layer: `false`.
- Render/PDF/text-layer extraction: `false`.
- Source/raw/accepted/semantic/page-status mutation: `false`.
- Source-profile acceptance: `false`.
- Runtime source-profile lock/acceptance: `false`.
- Runtime implementation/start/execution: `false`.
- Page 016+/021+ processing: `false`.
- Push: `false`.

## Remaining Blockers

- `frozen_profile_config_requires_separate_authorization`
- `replay_regression_smoke_requires_separate_authorization`
- `runtime_integration_design_requires_separate_authorization`
- `runtime_source_profile_lock_requires_separate_authorization`
- `accepted_text_or_semantic_mutation_requires_separate_authorization`
- `page_021_plus_remains_separate_bounded_lane_if_selected`
- `push_requires_separate_authorization`
