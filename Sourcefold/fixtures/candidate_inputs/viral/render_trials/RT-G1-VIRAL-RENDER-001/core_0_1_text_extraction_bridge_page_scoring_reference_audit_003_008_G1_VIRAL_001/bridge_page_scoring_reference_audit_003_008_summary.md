# Bridge Page Scoring Reference Audit 003-008 - C01TEBRIDGESCOREAUD020-G1-VIRAL-001

Status: `bridge_page_scoring_reference_audit_completed`

This lane audits pinned comparison/reference surfaces for the remediation candidates on pages `003`-`008` only.
It does not run OCR, promote candidates, accept text, mutate source/raw/page-status assets, create production output, include page `021+`, push, or run downstream work.

| Page | Reference class | Similarity | Token recall | Promotable |
|---|---|---:|---:|---|
| `003` | `bounded_reference_comparison_surface_available_low_authority` | `0.06414` | `0.739464` | `false` |
| `004` | `bounded_reference_comparison_surface_available_low_authority` | `0.017315` | `0.666667` | `false` |
| `005` | `bounded_reference_comparison_surface_available_not_acceptance_truth` | `0.175287` | `0.765` | `false` |
| `006` | `bounded_reference_comparison_surface_available_not_acceptance_truth` | `0.060631` | `0.766892` | `false` |
| `007` | `bounded_reference_comparison_surface_available_not_acceptance_truth` | `0.081666` | `0.801047` | `false` |
| `008` | `bounded_reference_comparison_surface_available_not_acceptance_truth` | `0.20165` | `0.879518` | `false` |

All pages have pinned comparison surfaces, but none are treated as independent acceptance truth in this lane.
Fresh OCR success remains empty until a separately authorized scoring/promotion decision exists.
