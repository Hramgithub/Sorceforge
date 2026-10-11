## Core 0.1 Bridge Page Authority Upgrade 003-004

Lane: `C01TEP003004AUTHUP-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-AUTHORITY-UPGRADE-003-004-001`

Status:
`reference_surface_authority_upgrade_recorded_future_strategy_only`.

Scope:

- Consume committed `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `50d4abac`.
- Nominate higher-authority reference surfaces for pages `003` and `004` for a
  future bounded comparison strategy.
- Keep page `004` context-only region `PRM-G1-VIRAL-001-P004-R01` non-peer and
  outside text reference surfaces.

Decision:

| Page | Nominated future reference surface |
|---|---|
| `003` | `P003A-G1-VIRAL-003` source-accepted records plus `P003PCA-G1-VIRAL-001` page-complete acceptance |
| `004` | `P004A-G1-VIRAL-004` source-accepted records plus `P004PCA-G1-VIRAL-001` page-complete acceptance |

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_authority_upgrade_003_004_G1_VIRAL_001/`

Allowed outputs:

- `authority_upgrade_003_004_report.json`
- `authority_upgrade_003_004_summary.md`
- `authority_upgrade_003_004_manifest.md`

Boundaries:

- Do not write replacement reference surfaces in this lane.
- Do not perform scoring execution, OCR/Tesseract, remediation, accepted text
  mutation, semantic/page-status mutation, source/raw mutation, bridge removal,
  promotion, fixture admission, production assembly, page `021+`, push,
  acceptance, or downstream execution.
- This lane does not confer promotion, acceptance, fresh-success, bridge-
  removal, or production authority.

Output hashes:

- Report:
  `134558C435879BB14FAAFE34F985E23075175BE49721412B9643D32DCD408A99`
- Summary:
  `690708980CBCB6F58000208B25F0AC75D2DC08619EA1BC41C867671D84D1B7AA`
- Manifest:
  `E920D4620C5AD61F95C558D33885A4566EEE21B6A2B66EC80ABA013AD498DB34`
