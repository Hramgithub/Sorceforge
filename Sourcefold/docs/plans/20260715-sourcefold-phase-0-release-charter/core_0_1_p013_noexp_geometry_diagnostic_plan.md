# Core 0.1 P013 No-Expansion Geometry Diagnostic Plan

Status: `candidate_only_p013_noexp_geometry_diagnostic_completed`

Lane id: `C01TEP013GNO-G1-VIRAL-001`

Authorization id:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-NOEXP-GEOMETRY-DIAGNOSTIC-001`

## Objective

Run the next P013 failed-page loop after sealed raw seam-dedupe proved safe but
insufficient.

This lane tests whether P013 improves when OCR is run over deterministic,
non-overlapping, no-expansion page-space regions derived from the original
triage boxes.

## Inputs

- P013 full-page review PNG `page_013.png`.
- Original P013 triage boxes, interpreted as `x,y,width,height`.
- Prior P013 seam-dedupe diagnostic report from `C01TEP013SDD-G1-VIRAL-001`,
  used as comparison history only.
- P013 reference text map, scorer-only after candidate hashes are sealed.
- Parent commit `e8af6677`.

## Geometry Contract

Coordinates are half-open `x1,y1,x2,y2`.

The original triage boxes become:

- `P013-B001`: `[160,205,1260,645]`
- `P013-B002`: `[210,625,1270,965]`
- `P013-B003`: `[210,960,1270,1100]`
- `P013-B004`: `[1290,205,2410,905]`
- `P013-B005`: `[1335,905,2395,1095]`

For declared vertical conflicts, the earlier/top block yields by clipping its
bottom to the later block's top:

- `P013-B001` clips bottom from `645` to `625`.
- `P013-B002` clips bottom from `965` to `960`.
- `P013-B004` and `P013-B005` only touch at `y=905` under half-open semantics,
  so no clipping is applied.

No padding, expansion, deskew, denoise, morphology, or OCR parameter search is
allowed.

## Candidates

All candidates use the same fixed OCR outputs with `eng_oem1_psm4`:

- `p013_geo_noexp_5box_triage_order`: `B001 -> B002 -> B003 -> B004 -> B005`.
- `p013_geo_noexp_4unit_triage_logical_order`: `B001`, `B002`,
  `B003+B004`, `B005`; this is derived from sealed triage roles, not reference
  scoring.
- `p013_geo_noexp_4unit_column_order_control`: `B001`, `B002`,
  `B004+B003`, `B005`; fixed before scoring as a reading-order control.

## Outputs

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_noexp_geometry_diagnostic_G1_VIRAL_001/`

Allowed files under that root:

- lineage JSON with pre/post clipping boxes;
- prepared crop images;
- raw OCR txt/tsv/stdout/stderr;
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
- It fails if any post-clipping boxes overlap, exceed original boxes, use
  padding, or use expansion.
- It fails if any page other than P013 is processed.
- It must not mix previous `_G1_VIRAL_002` raw OCR text into candidates.
- Candidate text and hashes must be sealed before reference text is loaded.
- No method-registry entry, selector rule, production output, acceptance,
  accepted text, semantic map, page status, source/raw asset, runtime, page
  `021+`, translation, proofreading, or push is allowed.

## Diagnostic Gate

Beating the prior dedupe baseline `0.25788` similarity is diagnostic
improvement only.

A result can become a method-registry candidate only if it meets the current
diagnostic threshold: sequence similarity at least `0.997` and token recall at
least `0.993939`, with no boundary violation.

## Run Result

`C01TEP013GNO-G1-VIRAL-001` completed under
`core_0_1_text_extraction_p013_noexp_geometry_diagnostic_G1_VIRAL_001`.

| Candidate | Similarity | Token recall | Diagnostic threshold met |
|---|---:|---:|---|
| `p013_geo_noexp_5box_triage_order` | `0.251286` | `0.987879` | `False` |
| `p013_geo_noexp_4unit_triage_logical_order` | `0.251286` | `0.987879` | `False` |
| `p013_geo_noexp_4unit_column_order_control` | `0.251286` | `0.987879` | `False` |

Interpretation: no-expansion/non-overlap geometry is not the P013 repair path.
It underperforms the previous seam-dedupe baseline (`0.25788` / `0.993939`),
so it is neither a method-registry candidate nor a selector rule.

This is still useful failed-page loop evidence: P013 likely needs either a
better OCR geometry family than no-expansion triage boxes, or a different
post-OCR structure strategy that can handle OCR instability without reference
token insertion.
