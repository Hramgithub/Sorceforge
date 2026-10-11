# Core 0.1 Geometry Probe - 012/013/016/017/018/020 - C01TEGP012013016017018020-G1-VIRAL-001

Status: `candidate_only_geometry_probe_completed`

Candidate generation uses full-page PNG geometry and Tesseract only; reference text is scorer-only after candidate hashes are sealed.

| Page | Best candidate | Similarity | Token recall | Diagnostic threshold met | Similarity delta | Token recall delta |
|---|---|---:|---:|---|---:|---:|
| `012` | `full_page_triage_boxes_expanded_psm4` | `0.98769` | `0.998024` | `False` | `-0.011776` | `0.001957` |
| `013` | `full_page_triage_boxes_expanded_psm4` | `0.242772` | `0.993939` | `False` | `-0.756694` | `-0.002128` |
| `016` | `full_page_triage_boxes_expanded_psm4` | `0.98277` | `0.991089` | `False` | `-0.016696` | `-0.004978` |
| `017` | `full_page_bright_title_body_psm7_4_4` | `0.99923` | `0.997859` | `True` | `-0.000236` | `0.001792` |
| `018` | `full_page_expanded_overlap_psm4` | `0.999466` | `0.996067` | `True` | `0.0` | `0.0` |
| `020` | `full_page_triage_boxes_expanded_psm4` | `0.994304` | `0.998833` | `False` | `-0.005162` | `0.002766` |

Parked pages not included: `014`, `019`.

Boundary: candidate-only OCR probe; no reference-guided repair, no accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.
