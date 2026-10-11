# Core 0.1 P013 Seam Dedupe Diagnostic Plan

Status: `candidate_only_p013_seam_dedupe_diagnostic_completed`

Lane id: `C01TEP013SDD-G1-VIRAL-001`

Authorization id:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-SEAM-DEDUPE-DIAGNOSTIC-001`

## Objective

Run the first bounded failed-page loop attempt for P013 after the
`001`-`020` geometry probe showed high recall but very low sequence
similarity.

The diagnosis is an order/assembly failure rather than an OCR-recognition
failure: the `_G1_VIRAL_002` expanded P013 regions overlap at seams and
duplicate boundary text before scoring.

## Inputs

- Corrected geometry-probe output root
  `core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002`.
- Sealed P013 candidate
  `candidate_texts/full_page_triage_boxes_expanded_psm4/page_013_candidate.md`
  with SHA-256
  `6AA2ADCDB1CDE71741F057300DC8888543F315BC14CD65F02602D71145CA5412`.
- The five sealed P013 raw OCR text files under
  `raw_ocr/full_page_triage_boxes_expanded_psm4/p013/`.
- The `_G1_VIRAL_001` stale marker, used only to prove the first incomplete
  output root remains rejected.
- P013 reference text map only after candidate hashes are sealed, for scoring.

## Outputs

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001/`

Allowed files under that root:

- repaired candidate markdown files;
- normalized candidate text files;
- seam deletion ledgers;
- per-page rankings;
- JSON report;
- Markdown summary;
- manifest with output hashes.

The runner and tests may be added under `scripts/` and `tests/`.

## Execution Contract

- The runner must fail closed unless `--execute`, the exact authorization id,
  and the exact Bogdan decision text are supplied.
- The runner must refuse to overwrite an existing output directory.
- No OCR, render, PDF parsing, PDF text-layer extraction, or source/raw
  mutation is allowed in this lane.
- Dedupe parameters are fixed before scoring.
- Candidate text and hashes must be written before reference text is loaded.
- Deletions may remove only exact normalized token overlap at declared seams:
  `P013-B001` to `P013-B002`, `P013-B002` to `P013-B003`, and `P013-B004` to
  `P013-B005`.
- Every deletion ledger entry must cite seam id, source block pair, current
  source span, deleted text, match basis, and expanded page-space overlap.
- Fuzzy matching, reference-guided token insertion, spelling correction, and
  tuning after reference scoring are forbidden.

## Diagnostic Gate

This lane has no acceptance effect. A repaired P013 candidate is only a method
registry candidate if all of the following are true:

- sequence similarity is at least `0.997`;
- token recall is at least the current P013 floor `0.993939`;
- every deletion is explainable by exact overlap evidence;
- no accepted text, semantic map, page status, source/raw asset, runtime, or
  production output is mutated.

If similarity improves but remains below `0.997`, the attempt is still useful
diagnostic evidence but remains a failed-page loop stage.

## Boundaries

This lane is P013-only. It must not generalize the method selector, create a
production assembly folder, process pages `014`, `019`, or `021+`, promote any
candidate, accept source/profile/page-status/page-complete state, translate,
proofread, push, or start runtime integration.

The no-expansion geometry idea is parked as a possible later OCR lane only; it
is not an executable candidate in this seam-dedupe diagnostic.

## Run Result

`C01TEP013SDD-G1-VIRAL-001` completed under
`core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001`.

| Candidate | Similarity | Token recall | Diagnostic threshold met |
|---|---:|---:|---|
| `sealed_raw_v1_max_tail_prefix_exact_dedupe` | `0.25788` | `0.993939` | `False` |
| `sealed_raw_v2_window160_prefix_exact_dedupe` | `0.25788` | `0.993939` | `False` |

Interpretation: strict seam-boundary dedupe is safe but insufficient. The
runner found no exact suffix-to-prefix deletion at the declared seams, which
means the duplicate-looking text is not removable under this conservative
assembly-only contract. Similarity improved only from `0.242772` to `0.25788`
while token recall stayed at `0.993939`.

This stage remains failed diagnostic evidence. It does not enter the method
registry, does not create a selector rule, and does not create production
output. The next failed-page loop for P013 should ask Sol for a new bounded
proposal, likely around non-overlapping/no-expansion geometry or logical
region re-OCR, rather than another sealed raw dedupe-only attempt.
