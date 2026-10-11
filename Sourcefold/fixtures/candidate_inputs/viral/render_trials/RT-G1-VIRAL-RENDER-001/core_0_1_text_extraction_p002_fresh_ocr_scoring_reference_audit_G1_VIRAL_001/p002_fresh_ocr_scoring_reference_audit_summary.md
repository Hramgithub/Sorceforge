# P002 Fresh OCR Scoring Reference Audit - C01TEP002FRESHSCOREAUD-G1-VIRAL-001

Status: `p002_fresh_ocr_scoring_reference_audit_completed`

This lane audits pinned comparison/reference surfaces for the page `002` fresh OCR candidates only.
It does not run OCR, promote candidates, remove bridge lineage, accept text, mutate source/raw/page-status assets, create production output, include page `021+`, push, or run downstream work.

| Candidate | Reference | Similarity | Token recall | Promotable |
|---|---|---:|---:|---|
| `psm4` | `page_complete_review_packet` | `0.02311` | `0.067669` | `false` |
| `psm4` | `page_map_readiness_packet` | `0.016667` | `0.098214` | `false` |
| `psm4` | `page_complete_acceptance_record` | `0.00974` | `0.048387` | `false` |
| `psm6` | `page_complete_review_packet` | `0.012979` | `0.090226` | `false` |
| `psm6` | `page_map_readiness_packet` | `0.021204` | `0.125` | `false` |
| `psm6` | `page_complete_acceptance_record` | `0.013625` | `0.080645` | `false` |

All reference surfaces are comparison-only. None are treated as independent acceptance truth in this lane.
Fresh OCR success remains empty until a separately authorized scoring/remediation decision exists.
