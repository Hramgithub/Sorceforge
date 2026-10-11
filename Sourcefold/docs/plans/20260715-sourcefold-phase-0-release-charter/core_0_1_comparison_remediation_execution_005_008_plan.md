## Core 0.1 Comparison Remediation Execution 005-008

Lane: `C01TEP005008REMEXEC-G1-VIRAL-001`

Authorization:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-COMPARISON-REMEDIATION-EXECUTION-005-008-001`

Status:
`comparison_only_remediation_execution_completed_candidate_only`.

Scope:

- Consume committed `C01TEP005008REMAUTH-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `4c438c4f`.
- Execute only comparison-remediation over existing candidate text for pages
  `005`, `006`, `007`, and `008`.
- Write lane-owned remediated candidate text and trace files for pages
  `005`-`008`.
- Seal remediated candidate hashes before loading reference comparison
  surfaces and computing diagnostic metrics.

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_comparison_remediation_execution_005_008_G1_VIRAL_001/`

Allowed outputs:

- `candidate_texts/page_005_comparison_remediated_candidate.md`
- `candidate_texts/page_006_comparison_remediated_candidate.md`
- `candidate_texts/page_007_comparison_remediated_candidate.md`
- `candidate_texts/page_008_comparison_remediated_candidate.md`
- `traces/page_005_comparison_remediation_trace.json`
- `traces/page_006_comparison_remediation_trace.json`
- `traces/page_007_comparison_remediation_trace.json`
- `traces/page_008_comparison_remediation_trace.json`
- `comparison_remediation_execution_005_008_report.json`
- `comparison_remediation_execution_005_008_summary.md`
- `comparison_remediation_execution_005_008_manifest.md`

Boundaries:

- Do not run OCR/Tesseract, render execution, PDF parsing, or fresh candidate
  OCR.
- Do not write replacement reference surfaces, mutate accepted/source/raw/
  semantic/page-status state, remove bridge lineage, promote pages, admit
  fixtures, assemble production, include page `021+`, push, accept, or trigger
  downstream execution.
- Diagnostic metrics are comparison-only evidence after candidate hash sealing;
  they are not fresh OCR success, bridge removal, acceptance, promotion, or
  production authority.

Output hashes:

- Runner:
  `F013292B767965A26644947D43E6C02DE8A73A36C5B486CC3748241080316E6E`
- Test:
  `D65058A0905DE049D643ED591509ADD3B5A4B71CED1716CBE469DBFEE7C0A61B`
- Report:
  `2514D091A1EF33029264897937AF3BA13B573F1DC9B3B199790D7A22E4B996F7`
- Summary:
  `16B14CDA8BBE7A9A56EC3119CE0669AC961F2B8F1FFE0268B36268B3D7B25042`
- Manifest:
  `3CAA8CFD24A48B17BE0BB593CF6ED2A46138FCE511BC3291FAF32E3AF16FBC29`
