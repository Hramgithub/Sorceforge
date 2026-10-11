## Core 0.1 Bridge Page Scoring Decision 003-008

Lane: `C01TEBRIDGESCOREDEC020-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-SCORING-DECISION-003-008-001`

Status:
`bridge_page_scoring_decision_recorded_remediation_strategy_no_scoring_no_promotion`.

Scope:

- Consume committed `C01TEBRIDGESCOREAUTH020-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `9ea4f8ed`.
- Record a decision over existing audited metrics only for pages `003`-`008`.
- Route pages `003`/`004` to authority upgrade because their comparison surfaces
  are low-authority OCR block text.
- Route pages `005`-`008` only to a future comparison-based remediation
  strategy because their OCR-verified text-map surfaces are comparison-only,
  not independent acceptance truth.

Decision:

| Page | Reference class | Route |
|---|---|---|
| `003` | low-authority comparison surface | `authority_upgrade_required` |
| `004` | low-authority comparison surface | `authority_upgrade_required` |
| `005` | OCR-verified text-map comparison surface, not independent acceptance truth | `remediation_strategy_required_comparison_only` |
| `006` | OCR-verified text-map comparison surface, not independent acceptance truth | `remediation_strategy_required_comparison_only` |
| `007` | OCR-verified text-map comparison surface, not independent acceptance truth | `remediation_strategy_required_comparison_only` |
| `008` | OCR-verified text-map comparison surface, not independent acceptance truth | `remediation_strategy_required_comparison_only` |

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_scoring_decision_003_008_G1_VIRAL_001/`

Allowed outputs:

- `bridge_page_scoring_decision_003_008_report.json`
- `bridge_page_scoring_decision_003_008_summary.md`
- `bridge_page_scoring_decision_003_008_manifest.md`

Boundaries:

- Do not perform new scoring execution in this lane.
- Do not run OCR/Tesseract, render or parse PDFs, accept text, mutate
  source/raw/accepted/page-status files, admit fixtures, assemble production,
  include page `021+`, push, promote, remove bridge lineage, mark fresh OCR
  success, or trigger downstream execution.
- Comparison-only evidence cannot become acceptance truth or promotion
  authority in this lane.

Output hashes:

- Report:
  `05945273CB5F34C2E30F7DD9609E00AD4B218C1F72FF86FC9BE34FF97FC765DA`
- Summary:
  `B9AC740820AC6F539A8E5C4D9940F8E2238A459D849484A631BD010AD0048334`
- Manifest:
  `D2177682602EC011A084AA17E66A52A767AF8088FE7BA105AE97CB6EDFEC9E25`
