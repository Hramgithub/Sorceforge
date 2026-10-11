# Core 0.1 P013 Structural Suppression Diagnostic Plan

Status: `candidate_only_p013_structural_suppression_diagnostic_completed`

Lane id: `C01TEP013SSP-G1-VIRAL-001`

Authorization id:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-SUPPRESSION-DIAGNOSTIC-001`

## Objective

Run the fourth P013 failed-page loop attempt after seam dedupe, no-expansion
geometry, and expanded lane-order diagnostics failed to reach threshold.

This lane starts from the sealed ELO best retained record set and tests whether
invariant structural suppression can remove duplicated/garbage OCR line records
without inserting, rewriting, or repairing text from the reference.

No OCR is executed.

## Inputs

Pinned inputs:

- ELO report:
  `C8EFBAF8F3FFB58E0FF8CCFA41869861B6AA6F92A0E8E6DAC6F111EDC91BD3FB`
- ELO manifest:
  `74C1985E1B8DB19375E5652E2674918F9C44202F1173EF1074C5A16D757F5C87`
- ELO raw mapped line records:
  `1DEB381148397F9014C22C3263858C360FF9BAA8C64199572AD024CB578A2863`
- ELO best retained trace:
  `CE27FBE19F08D9432D3D8C8C8F43FBC3E749DA05A54B995523B4BAFA0C860E94`
- ELO exact-collapse report:
  `DCCBF482AAE8DAC5EC7F569BAE84422ED5487EE2676442E77120345B82E8EB73`
- Source P013 ranking:
  `45A41E61A34C892328ABB69D988DD6947D33F32E9BFCE56771B6FCD36CEC4454`
- Five cached P013 raw TSV files from `_G1_VIRAL_002`, pinned in the runner.
- P013 reference text map, scorer-only after all candidate hashes are sealed:
  `7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67`
- Parent commit `796c7044`.

## Record Schema

Every retained line record gets stable derived fields before suppression:

- `record_id`: `<source_region>:<tsv_block>.<tsv_par>.<tsv_line>`;
- `source_order`: `<sealed_region_index_2_digits>.<sealed_line_index_3_digits>`;
- `tsv_line_key`: same stable TSV key as `record_id`;
- `page_bbox_half_open`: page-space `[x1,y1,x2,y2]` half-open box from ELO;
- `confidence`: word-level mean/min/list from the pinned raw TSV rows.

## Variants

All parameters are fixed before reference scoring.

- `p013_ssp_a0_elo_exact_collapse_baseline`: the sealed ELO best retained set.
- `p013_ssp_a_near_overlap_confidence`: starts from A0; builds connected
  components from same-lane records with min-area overlap ratio `>= 0.72`,
  y-center gap `<= 8` px, and normalized token Dice `>= 0.84`; keeps only the
  highest mean-confidence record when the confidence delta is greater than
  `1.0`, otherwise preserves all records in the component. Non-clique
  transitive components are preserved as ambiguous; the retained winner must
  have a direct qualifying edge to every suppressed record.
- `p013_ssp_b_noise_from_a0`: starts from A0; suppresses only low-confidence
  thin noise or punctuation fragments when a same-lane neighbor is within
  `36` px vertical edge gap. Low-confidence thin noise requires mean confidence
  `<= 50` and height `<= 14` px.
- `p013_ssp_c_floor_guarded_near_overlap_then_noise`: records the A-then-B
  combined probe in the suppression ledger, but the candidate output preserves
  the sealed A0 retained set unless a separately reviewed selector rule defines
  non-regression behavior. This keeps C from regressing below the ELO best
  baseline.

Variant B uses exact geometry formulas:

- vertical edge gap is `next.y1 - current.y2`, `current.y1 - next.y2`, or `0`
  when boxes overlap;
- horizontal edge gap is the same edge-vs-edge formula on x;
- punctuation fragments match the runner's fixed regex and must also have a
  same-lane neighbor within the vertical-gap threshold.

## Outputs

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001/`

Allowed files under that root:

- enriched ELO best records;
- retained-record traces;
- suppression ledgers;
- candidate text files;
- normalized candidate text files;
- per-page rankings;
- JSON report;
- Markdown summary;
- manifest with output hashes.

## Fail-Closed Gates

- The runner requires `--execute`, exact authorization id, and exact Bogdan
  decision text.
- It refuses to overwrite an existing output root.
- It must fail closed on any pinned input hash mismatch.
- Candidate text and hashes for all variants must be sealed before reference
  text is loaded. Reference hash verification happens in the scoring phase.
- A0 and floor-guarded C must fail closed if scoring drifts below the ELO best
  metrics.
- It must not execute OCR, render, parse PDFs, mutate source/raw assets, mutate
  accepted text, mutate semantic maps, mutate page status, create production
  output, update a selector or method registry, process page `021+`, translate,
  proofread, push, or start runtime integration.

## Diagnostic Gate

This lane is diagnostic only.

The A0 baseline and floor-guarded C candidate must preserve the current ELO
best metrics:
sequence similarity `0.433325` and token recall `0.993939`.

Method-registry candidacy requires the full diagnostic threshold:
sequence similarity at least `0.997` and token recall at least `0.993939`.

## Run Result

`C01TEP013SSP-G1-VIRAL-001` completed under
`core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001`.

No OCR was executed. All candidate text, normalized text, retained-record trace,
and suppression-ledger artifacts were written and hash-sealed before the P013
reference text was loaded for scoring.

| Candidate | Similarity | Token recall | Diagnostic threshold met |
|---|---:|---:|---|
| `p013_ssp_a_near_overlap_confidence` | `0.914027` | `0.993939` | `False` |
| `p013_ssp_b_noise_from_a0` | `0.436181` | `0.993939` | `False` |
| `p013_ssp_a0_elo_exact_collapse_baseline` | `0.433325` | `0.993939` | `False` |
| `p013_ssp_c_floor_guarded_near_overlap_then_noise` | `0.433325` | `0.993939` | `False` |

Interpretation: near-overlap confidence suppression is the strongest P013
diagnostic signal so far. It removes one same-lane near-overlap
lower-confidence duplicate, improving similarity by `0.480702` over ELO while
preserving token recall. It still remains below the `0.997` diagnostic
threshold, so it is not a method-registry winner or selector rule.
