# Core 0.1 Text Extraction Overview Replay - 001-020 - C01TEOR020-G1-VIRAL-001

Status: `candidate_only_001_020_overview_replay_completed`

This overview reuses only the frozen profile tuple from `C01TEFPC-G1-VIRAL-001`; it does not broaden the config allowed-pages policy.

| Page | Status | Reference | Inputs | Similarity | Token recall | Flags |
|---|---|---|---:|---:|---:|---|
| `001` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `no_eligible_text_evidence_crops_reference_pair` |
| `002` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `no_page_complete_review_assets_or_reference` |
| `003` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `no_eligible_text_evidence_crops_reference_pair` |
| `004` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `no_eligible_text_evidence_crops_reference_pair` |
| `005` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `reference_map_exists_but_no_text_evidence_crops` |
| `006` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `reference_map_exists_but_no_text_evidence_crops` |
| `007` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `reference_map_exists_but_no_text_evidence_crops` |
| `008` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `reference_map_exists_but_no_text_evidence_crops` |
| `009` | `run_completed` | `reference_ocr_verified_text_map` | `2` | `0.997902` | `0.996324` | `none` |
| `010` | `run_completed` | `reference_ocr_verified_text_map` | `4` | `0.998867` | `0.995825` | `none` |
| `011` | `run_completed` | `reference_ocr_verified_text_map` | `2` | `0.999701` | `1.0` | `none` |
| `012` | `run_completed` | `reference_text_map_not_ocr_verified` | `7` | `0.948997` | `0.990119` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |
| `013` | `run_completed` | `reference_text_map_not_ocr_verified` | `5` | `0.96853` | `0.978788` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |
| `014` | `run_completed` | `reference_text_map_not_ocr_verified` | `9` | `0.843214` | `0.961749` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |
| `015` | `run_completed` | `reference_text_map_not_ocr_verified` | `2` | `0.997252` | `0.993985` | `reference_not_ocr_verified` |
| `016` | `run_completed` | `reference_text_map_not_ocr_verified` | `4` | `0.894813` | `0.975248` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |
| `017` | `run_completed` | `reference_text_map_not_ocr_verified` | `2` | `0.67119` | `0.980728` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |
| `018` | `run_completed` | `reference_text_map_not_ocr_verified` | `2` | `0.298585` | `0.971485` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |
| `019` | `run_completed` | `reference_text_map_not_ocr_verified` | `2` | `0.670833` | `0.953232` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |
| `020` | `run_completed` | `reference_text_map_not_ocr_verified` | `2` | `0.895437` | `0.991832` | `weak_similarity, weak_token_recall, reference_not_ocr_verified` |

Weak thresholds: similarity `< 0.997`, token recall `< 0.993`.
Weak pages: `012, 013, 014, 016, 017, 018, 019, 020`.
Reference-risk pages: `012, 013, 014, 015, 016, 017, 018, 019, 020`.

Boundary: overview/report only; no remediation in this layer.
No accepted/semantic/source/page-status mutation, no PDF/render/runtime/page 021+/push.
