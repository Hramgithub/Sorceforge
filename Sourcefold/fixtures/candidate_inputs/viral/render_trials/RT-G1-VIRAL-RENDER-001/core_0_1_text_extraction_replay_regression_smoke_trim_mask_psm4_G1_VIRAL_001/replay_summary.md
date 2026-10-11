# Core 0.1 Text Extraction Replay Regression Smoke - C01TERSM-G1-VIRAL-001

Status: `candidate_only_replay_regression_smoke_completed`

Replay uses only frozen profile config `C01TEFPC-G1-VIRAL-001`.

| Page | Reference | Inputs | Similarity | Token recall |
|---|---|---:|---:|---:|
| `009` | `reference_ocr_verified_text_map` | `2` | `0.997902` | `0.996324` |
| `010` | `reference_ocr_verified_text_map` | `4` | `0.998867` | `0.995825` |
| `015` | `reference_text_map_not_ocr_verified` | `2` | `0.997252` | `0.993985` |

Boundary: candidate-only replay; no accepted/semantic/source/page-status mutation, no PDF/render/runtime/page 016+/page 021+/push.
