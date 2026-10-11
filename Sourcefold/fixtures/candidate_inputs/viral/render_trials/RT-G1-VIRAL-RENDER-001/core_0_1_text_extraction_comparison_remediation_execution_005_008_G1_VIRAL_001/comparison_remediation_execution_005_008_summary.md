# C01TEP005008REMEXEC-G1-VIRAL-001 Summary

Status: `comparison_only_remediation_execution_completed_candidate_only`

This lane materializes comparison-only remediated candidate outputs for pages `005`-`008` from existing candidate text.
It does not run OCR/Tesseract, render, parse PDF, mutate source/raw/accepted/page-status state, remove bridge lineage, promote, accept, assemble production, include page `021+`, push, or trigger downstream execution.

| Page | Similarity after remediation | Token recall after remediation | Threshold met |
|---|---:|---:|---|
| `005` | `0.20237` | `0.75122` | `false` |
| `006` | `0.110164` | `0.753205` | `false` |
| `007` | `0.230706` | `0.781095` | `false` |
| `008` | `0.09293` | `0.857143` | `false` |

Fresh OCR success, bridge removal, promotion, acceptance, and production remain false until a separate reviewed decision lane.
