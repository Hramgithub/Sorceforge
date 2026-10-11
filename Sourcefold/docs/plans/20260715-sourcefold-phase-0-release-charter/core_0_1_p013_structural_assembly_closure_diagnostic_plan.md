# Core 0.1 P013 Structural Assembly Closure Diagnostic Plan

Status: `draft_execution_prep_pending_sol_terra_review`

Lane id: `C01TEP013SAC-G1-VIRAL-001`

Authorization id:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-ASSEMBLY-CLOSURE-DIAGNOSTIC-001`

## Objective

Run the next P013 failed-page loop attempt after structural suppression improved
P013 to `0.914027` sequence similarity and `0.993939` token recall while still
failing the `0.997` similarity threshold.

This lane starts from the sealed SSP best retained record set and tests only
deterministic structural assembly deletion rules: low-confidence thin noise and
declared seam-fracture duplicates. It does not insert, replace, or repair OCR
tokens.

No OCR is executed.

## Inputs

Pinned SSP inputs:

- SSP report:
  `712446CC642C1499E9786630D9F0E136B526CC028875BF7E6D4BA4F3E1A89D9B`
- SSP summary:
  `0AD50E8AAE374BB02654EC25A90EE07823AB25F0E4C3EA37EA6AAA181FF92D4B`
- SSP manifest:
  `11E29CA99CBBC60B04A3466B9A665EEB9C6978F52867720D396C6A839641183E`
- SSP-A candidate:
  `F02D342C7FFA21FC396169294EF01713D36BB4555D3DDB54094472BC0F3EC36D`
- SSP-A normalized candidate:
  `909B81B4614346DBD0F0C74A012CD6935A2EA3A46AEA1847E46E7401B792B8E0`
- SSP-A retained records:
  `6C9703A0255BA3B97A5C3872C6AF7513FFACBDAE153CB899A3E5AA1CF303A9A2`
- SSP-A suppression ledger:
  `14FF15526D97CD2E9E6F5B39BA4FB857F83DA761AB027860174948A4778BC424`
- Source P013 ranking and all five cached P013 raw TSV files are pinned in the
  runner for confidence and geometry traceability.
- P013 reference text map, scorer-only after all candidate hashes are sealed:
  `7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67`
- Sourcefold predecessor commit for history only:
  `de0d759b9947383bf21bfe4af0bacae5f1eaff21`.

## Variants

All parameters are fixed before reference scoring.

- `p013_sac_a0_ssp_best_baseline`: exact SSP-A retained records. It must
  reproduce `0.914027` similarity and `0.993939` token recall.
- `p013_sac_b_noise_after_ssp`: starts from SSP-A and applies only the existing
  low-confidence thin noise / punctuation-fragment geometry rule.
- `p013_sac_c_declared_seam_fracture_after_ssp`: starts from SSP-A and applies
  only declared seam-fracture duplicate suppression.
- `p013_sac_d_noise_then_declared_seam_fracture`: applies B, then C.
- `p013_sac_e_paragraph_join_d`: uses the same retained record set as D, but
  assembles adjacent records in each source region with spaces. Record text is
  unchanged; this is a separator-only assembly probe.

## Declared Seam-Fracture Rule

The fixed seam list is:

- `P013-B004-TES` -> `P013-B005-TES`

A later seam fragment may be suppressed only when all structural predicates are
true:

- source-region pair is in the declared seam list;
- earlier `source_order` is lower than later `source_order`;
- earlier record is the lower boundary record of its source region;
- later record is the upper boundary record of its source region;
- records are in the same lane;
- min-area overlap ratio is at least `0.72`;
- smaller/larger area size ratio is at least `0.80`;
- y-center gap is at most `8` px;
- normalized token Dice is at least `0.90`;
- earlier normalized-token support is greater than or equal to the later
  support.
- later normalized tokens are contained in the earlier normalized-token sequence
  except for at most one bounded edge fragment drop where the earlier token has
  one or two leading characters more than the later token.

The rule does not match text literals. It does not repair spelling or insert
missing reference tokens.

## Outputs

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001/`

Allowed files under that root:

- retained-record traces;
- suppression ledgers;
- assembly traces;
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
- Candidate text, normalized text, retained trace, suppression ledger, and
  assembly trace for every variant must be written and hash-sealed before the
  P013 reference text map is loaded for scoring.
- A0 must fail closed if scoring drifts from the current SSP best metrics.
- It must not execute OCR, render, parse PDFs, use PDF text-layer extraction,
  perform image processing, mutate source/raw assets, mutate accepted text,
  mutate semantic maps, mutate page status, create production output, update a
  selector or method registry, process page `021+`, translate, proofread, push,
  or start runtime integration.
- OCR token repairs such as spelling correction remain explicitly out of scope.

## Diagnostic Gate

This lane is diagnostic only.

Method-registry candidacy requires the full diagnostic threshold:
sequence similarity at least `0.997` and token recall at least `0.993939`.

Beating the SSP best baseline alone is diagnostic evidence only. Selector and
production behavior remain unchanged until separately reviewed.

## Run Result

`C01TEP013SAC-G1-VIRAL-001` completed under
`core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001`.

No OCR was executed. All candidate text, normalized text, retained-record
trace, suppression-ledger, and assembly-trace artifacts were written and
hash-sealed before the P013 reference text was loaded for scoring.

| Candidate | Similarity | Token recall | Diagnostic threshold met |
|---|---:|---:|---|
| `p013_sac_d_noise_then_declared_seam_fracture` | `0.998915` | `0.993939` | `True` |
| `p013_sac_e_paragraph_join_d` | `0.998915` | `0.993939` | `True` |
| `p013_sac_c_declared_seam_fracture_after_ssp` | `0.99219` | `0.993939` | `False` |
| `p013_sac_b_noise_after_ssp` | `0.92015` | `0.993939` | `False` |
| `p013_sac_a0_ssp_best_baseline` | `0.914027` | `0.993939` | `False` |

Interpretation: combined low-confidence thin-noise suppression plus declared
seam-fracture duplicate suppression closes the P013 diagnostic gap without OCR
or token repair. This is method-registry candidate evidence only; selector and
production behavior remain unchanged until a separate reviewed step.
