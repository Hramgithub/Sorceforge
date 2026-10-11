# Core 0.1 Weak Page Diagnostics + P018 Remediation - C01TEWDR-G1-VIRAL-001

Status: `candidate_only_weak_diagnostics_p018_remediation_completed`

## Diagnostics

| Page | Similarity | Token recall | Flags |
|---|---:|---:|---|
| `012` | `0.948997` | `0.990119` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |
| `013` | `0.96853` | `0.978788` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |
| `014` | `0.843214` | `0.961749` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |
| `016` | `0.894813` | `0.975248` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |
| `017` | `0.67119` | `0.980728` | `sequence_order_or_layout_issue, token_recall_issue, high_recall_low_sequence_alignment, reference_not_ocr_verified` |
| `018` | `0.298585` | `0.971485` | `sequence_order_or_layout_issue, token_recall_issue, high_recall_low_sequence_alignment, reference_not_ocr_verified` |
| `019` | `0.670833` | `0.953232` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |
| `020` | `0.895437` | `0.991832` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |

## P018 Remediation Probe

Best candidate: `wide_edge_mask_trim_psm4_normal`
P018 similarity: `0.814888`
P018 token recall: `0.976401`

## Mini Replay

| Page | Similarity | Token recall | Flags |
|---|---:|---:|---|
| `017` | `0.825557` | `0.987152` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |
| `019` | `0.534684` | `0.971114` | `sequence_order_or_layout_issue, token_recall_issue, high_recall_low_sequence_alignment, reference_not_ocr_verified` |
| `014` | `0.766091` | `0.965847` | `sequence_order_or_layout_issue, token_recall_issue, reference_not_ocr_verified` |

Boundary: diagnostic/remediation evidence only; no accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.
