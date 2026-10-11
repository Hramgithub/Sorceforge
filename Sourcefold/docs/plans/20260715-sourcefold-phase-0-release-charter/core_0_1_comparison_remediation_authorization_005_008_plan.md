## Core 0.1 Comparison Remediation Authorization 005-008

Lane: `C01TEP005008REMAUTH-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-COMPARISON-REMEDIATION-AUTHORIZATION-005-008-001`

Status:
`comparison_only_remediation_authorized_no_execution`.

Scope:

- Consume committed `C01TEP005008REMSTRAT-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `8704802c`.
- Authorize only a future bounded comparison-only remediation execution for
  pages `005`, `006`, `007`, and `008`.
- Preserve OCR-verified text-map surfaces as diagnostic comparison inputs only,
  not acceptance truth or promotion authority.
- Add fail-closed builder and pytest coverage for exact authorization,
  predecessor hashes, page scope, output tree shape, and boundary flags.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_comparison_remediation_authorization_005_008_G1_VIRAL_001/`

Allowed outputs:

- `comparison_remediation_authorization_005_008_report.json`
- `comparison_remediation_authorization_005_008_summary.md`
- `comparison_remediation_authorization_005_008_manifest.md`

Boundaries:

- Do not execute remediation, scoring, OCR/Tesseract, render/PDF parsing, or
  candidate generation in this lane.
- Do not write replacement reference surfaces, mutate accepted/source/raw/
  semantic/page-status state, remove bridge lineage, promote pages, admit
  fixtures, assemble production, include page `021+`, push, accept, or trigger
  downstream execution.
- Any future remediation execution, scoring, fresh-success decision, bridge
  removal, runtime selector refresh, production assembly, acceptance, or
  promotion requires separate reviewed authorization.

Output hashes:

- Builder:
  `E9EC319D057958A76E3F77FFB4F0F6B143AA0B592A18D44E6FFA4166A47BA17B`
- Test:
  `DCBF9850BF639454E70609745DA5AEAC717BB06342E57CB569627506495ABE00`
- Report:
  `2616AE83F41A1F78911F5A8652EE8AF0CA01F20A2155E28F568082CF3D98E38B`
- Summary:
  `07D7F438F9E881B18D3CC2A7EAD1B2EAB6667ED128DABF87106A25E409F9728E`
- Manifest:
  `53A182226919CDCA4CC347EC48D65A48C1F959BF57DF0A1D9667DB480FE4C898`
