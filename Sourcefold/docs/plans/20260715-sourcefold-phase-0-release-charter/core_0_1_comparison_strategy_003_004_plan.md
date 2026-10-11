## Core 0.1 Comparison Strategy 003-004

Lane: `C01TEP003004COMPSTRAT-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-COMPARISON-STRATEGY-003-004-001`

Status:
`comparison_scoring_prep_strategy_recorded_no_execution`.

Scope:

- Consume committed `C01TEP003004AUTHUP-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `de58ee23`.
- Define comparison/scoring-prep strategy only for pages `003` and `004`.
- Define future normalization, reference assembly order, metric names,
  thresholds, discrepancy buckets, and non-authorizing remediation
  considerations.

Decision:

| Page | Future candidate input | Future reference assembly |
|---|---|---|
| `003` | Existing bridge remediation PSM6 candidate | `SRSA-G1-VIRAL-003-R01 -> SRSA-G1-VIRAL-003-R02` |
| `004` | Existing bridge remediation PSM6 candidate | `SRSA-G1-VIRAL-004-R01 -> SRSA-G1-VIRAL-004-R02` |

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_comparison_strategy_003_004_G1_VIRAL_001/`

Allowed outputs:

- `comparison_strategy_003_004_report.json`
- `comparison_strategy_003_004_summary.md`
- `comparison_strategy_003_004_manifest.md`

Boundaries:

- Do not execute scoring in this lane.
- Do not run OCR/Tesseract, perform remediation, write replacement reference
  surfaces, mutate accepted/source/raw/semantic/page-status state, remove bridge
  lineage, promote pages, admit fixtures, assemble production, include page
  `021+`, push, accept, or trigger downstream execution.
- Source-accepted/page-complete-backed surfaces are future bounded comparison
  inputs only, not acceptance, promotion, fresh-success, bridge-removal, or
  production authority.
- Page `004` context-only region `PRM-G1-VIRAL-001-P004-R01` remains non-peer
  and excluded from future text-reference assembly.

Output hashes:

- Report:
  `E3BD3DB59AC70E4D24998DDD74B41730E286EFA1A56C953757058FE018883213`
- Summary:
  `B97A8C997525071A047FF1B9885B547DBEBEF9BC0D3ACC04B3677D6902F4C462`
- Manifest:
  `A958BBE246E6BD213A6C77C16739A34C305665E300D11BDA12FA010931245266`
