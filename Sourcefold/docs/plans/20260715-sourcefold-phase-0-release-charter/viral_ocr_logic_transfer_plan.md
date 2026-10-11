# Viral OCR Logic Transfer Plan

Plan id: `ORP-G1-VIRAL-001`

Status: `executed_for_review`

Authorization id: `BA-G1-VIRAL-REMEDIATE-001`

Created: 2026-07-18

Baseline commit: `684a6400d8ffb5b6f9d6db2e289069408dfd0bda`

Purpose: recreate the proven prior OCR evaluation logic inside Sourcefold
without carrying over old project filenames, script names, variable names,
config models, cache paths, or dependencies.

Boundary: this plan and its outputs are remediation evidence only. They are not
QA, fixture creation, source-profile acceptance, translation, proofreading,
renderer/profile acceptance, implementation, or Gate 1 advancement.

## Research Provenance

The logic was taken from a read-only review of the prior local OCR work under
`D:\NRI\translator`. These files are research references only; they are not
runtime dependencies, import targets, config parents, API names, cache roots, or
Sourcefold naming sources.

Reviewed references:

- `D:\NRI\translator\scripts\wormsign\wormsign_ocr_method_profiles_20260701.json`
  for method-routing precedent: disable weak default segmentation modes, prefer
  page/region-aware method matrices, use visual-only routing for image-first
  regions, and treat scores as triage.
- `D:\NRI\translator\scripts\wormsign\wormsign_pages_layout_method_loop_20260630.README.md`
  for evidence-shape precedent: method matrix, extracted blocks, TSV-backed
  geometry, output hashes, and review stand concepts.
- `D:\NRI\translator\docs\wormsign\OCR_Translation_Iteration_Run_Plan_20260702.md`
  for overlay QC and order/zone QC precedent: bbox/confidence flags, routing
  status, method disagreement, and visual review queue behavior.
- `D:\NRI\translator\docs\wormsign\OCR_Translation_Pipeline_Agent_Spec_20260701.md`
  for the non-acceptance model: OCR/overlay/order scores route review work but
  do not approve source, translation, or production.
- `D:\NRI\translator\docs\architecture\translator_pipeline_stage_reference.md`
  for boundary precedent: OCR and column/order reconstruction are opt-in
  evidence stages and must not become automatic source truth.

Sourcefold reproduction rules from that review:

- Recreate behavior in Sourcefold-native files and names.
- Do not import, execute, wrap, or reference old scripts as live tools.
- Do not copy old config models, variable names, wrapper commands, output
  directory conventions, or package vocabulary into Sourcefold runtime.
- Keep old references only here as audit trail for future research.
- If additional research is needed, use these references as starting points,
  then record any new influence here before applying it to Sourcefold.

## Working Principles

1. Use only current Sourcefold identities: `POMB-G1-VIRAL-001`,
   `GSM-G1-VIRAL-001`, `OCM-G1-VIRAL-001`, `OBR-G1-VIRAL-002`, and current
   rendered page PNGs.
2. Treat rendered page PNGs as the visual authority for this bounded step.
3. Treat OCR output as evidence, never as accepted source text.
4. Keep scoring as triage. A high score selects the first candidate to inspect;
   it does not approve text, layout, source profile, or Gate 1.
5. Separate OCR-capable zones from visual-QC zones. Decorative titles and page
   number columns may need routing evidence rather than forced OCR.
6. Preserve payload-light reports in roadmap/status files. Raw text and TSV
   stay under the remediation output directory with hashes.
7. Keep invalidation strict: any crop, tool, preprocessing, PSM, scoring, gold,
   or predecessor change stales the evidence.

## Sourcefold-Native Shape

The transfer becomes four local capabilities:

1. `route_samples`: split each admitted sample into one or more route zones.
   Routes are `ocr` or `visual_qc`.
2. `prepare_inputs`: create refined crop PNGs and deterministic input variants
   from already rendered page PNGs only.
3. `run_matrix`: execute a bounded Tesseract matrix over OCR zones only.
   Default tested PSM modes are `1`, `4`, `8`, and `11`; PSM `3` and `6` are
   disabled as default candidates.
4. `score_and_record`: compute normalized exact match, token recall, character
   error rate, overlay QC, order/zone QC, output hashes, route findings, and
   invalidation rules.

## Detailed Execution Plan

1. Record `BA-G1-VIRAL-REMEDIATE-001` with exact action, inputs, allowed
   outputs, limits, expiry, and invalidation behavior.
2. Create a checked-in Sourcefold script:
   `scripts/run_ocr_remediation_matrix.py`.
3. Define five current sample routes:
   `GS-G1-VIRAL-001` through `GS-G1-VIRAL-005`.
4. For `GS-G1-VIRAL-001`, split the decorative cover title into a visual-QC
   route for the large visual component and an OCR route for the machine-readable
   component.
5. For `GS-G1-VIRAL-002`, use a refined heading crop and OCR route.
6. For `GS-G1-VIRAL-003`, split content-entry words from page-number column
   evidence; OCR the words and route page numbers through visual QC because the
   current rendered digits are not reliable OCR targets.
7. For `GS-G1-VIRAL-004`, use a refined section-heading crop and OCR route.
8. For `GS-G1-VIRAL-005`, use a refined quote crop and OCR route.
9. For every OCR route, generate `original`, `enhanced_x2`, `binary_x3`, and
   `white_mask_x4` prepared inputs.
10. For every prepared OCR input, run Tesseract with OEM `1` and PSM modes
    `1`, `4`, `8`, and `11`, writing text, TSV, stderr, and command logs.
11. Score each OCR route by normalized exact match, token recall, character
    error rate, average confidence, overlay status, and order/zone status.
12. Select the best OCR candidate per OCR route for inspection.
13. Mark visual-QC routes as route passes only when they are explicit routing
    findings, not transcriptions.
14. Produce JSON evidence:
    `ocr_remediation_matrix_report.json`,
    `ocr_remediation_matrix_rows.json`, and
    `ocr_remediation_plan.json`.
15. Produce Markdown evidence:
    `ocr_remediation_output_manifest.md`.
16. Run validation checks: roadmap validator, diff whitespace check, and changed
    file scan for old-project naming/dependency leakage.
17. Ask Sol and Terra to review the final artifacts against lineage, leakage,
    non-acceptance wording, and the 5/5 route metric.
18. Commit only after checks and review pass.

## Success Metric

The target is `5/5 remediation_route_pass`, not `5/5 accepted source text`.

An OCR route passes only when:

- normalized expected text is present in normalized OCR output;
- token recall is `1.0`;
- raw output is unedited;
- text and TSV hashes are recorded;
- overlay/order QC is recorded.

A visual-QC route passes only when:

- it is declared before scoring;
- it is used for a component that current OCR cannot reliably resolve;
- it records the crop hash and route finding;
- it does not transcribe, approve, or promote source text.

## Expected Output Location

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_remediation_matrix_G1_VIRAL_001/`

## Non-Claims

- No PDF text-layer use.
- No PDF opening, parsing, rehashing, recounting, or inspection.
- No OCR outside the five admitted sample routes.
- No source acceptance.
- No Gate 1 advancement.
- No production or translation decision.
