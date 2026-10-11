## Core 0.1 Comparison Remediation Strategy 005-008

Lane: `C01TEP005008REMSTRAT-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-COMPARISON-REMEDIATION-STRATEGY-005-008-001`

Status:
`comparison_only_remediation_strategy_recorded_no_execution`.

Scope:

- Consume committed `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` report, summary,
  and manifest by exact hash from commit `50d4abac`.
- Treat committed `C01TEP003004COMPSTRAT-G1-VIRAL-001` from commit `6b336843`
  as the adjacent boundary for pages `003`/`004`, not as part of this page
  scope.
- Define comparison-only remediation strategy for pages `005`, `006`, `007`,
  and `008`.
- Define future remediation families, normalization, metric names, thresholds,
  hash-sealing requirements, and non-authorizing route constraints.

Decision:

| Page | Existing similarity | Existing token recall | Route |
|---|---:|---:|---|
| `005` | `0.175287` | `0.765` | `remediation_strategy_required_comparison_only` |
| `006` | `0.060631` | `0.766892` | `remediation_strategy_required_comparison_only` |
| `007` | `0.081666` | `0.801047` | `remediation_strategy_required_comparison_only` |
| `008` | `0.20165` | `0.879518` | `remediation_strategy_required_comparison_only` |

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_comparison_remediation_strategy_005_008_G1_VIRAL_001/`

Allowed outputs:

- `comparison_remediation_strategy_005_008_report.json`
- `comparison_remediation_strategy_005_008_summary.md`
- `comparison_remediation_strategy_005_008_manifest.md`

Boundaries:

- Do not execute remediation or scoring in this lane.
- Do not run OCR/Tesseract, perform render/PDF parsing, write replacement
  reference surfaces, mutate accepted/source/raw/semantic/page-status state,
  remove bridge lineage, promote pages, admit fixtures, assemble production,
  include page `021+`, push, accept, or trigger downstream execution.
- OCR-verified text-map surfaces for pages `005`-`008` are future bounded
  diagnostic comparison inputs only; they are not acceptance, promotion,
  fresh-success, bridge-removal, or production authority.
- Any future remediation execution, scoring, fresh-success decision, bridge
  removal, runtime selector refresh, production assembly, acceptance, or
  promotion requires separate reviewed authorization.

Output hashes:

- Report: `FFCEED1AF265E241A3C549DA7CE06B0631B6E02D9F4441FDB31188B708D6C843`
- Summary: `70BF51FDA3E5B5C10AABBE1A3D0778B7FB83E6D54E3336EF4C61E27013D019F0`
- Manifest: `66351A7B8D6CF27501605F24E823827310B3114521C904FFDC06A1CA7A128925`
