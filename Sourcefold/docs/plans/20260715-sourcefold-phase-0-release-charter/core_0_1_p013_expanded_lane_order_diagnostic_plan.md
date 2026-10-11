# Core 0.1 P013 Expanded Lane-Order Diagnostic Plan

Status: `candidate_only_p013_expanded_lane_order_diagnostic_completed`

Lane id: `C01TEP013ELO-G1-VIRAL-001`

Authorization id:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-EXPANDED-LANE-ORDER-DIAGNOSTIC-001`

## Objective

Run the third P013 failed-page loop attempt after seam dedupe and
no-expansion geometry both failed.

This lane tests whether P013 is a layout ordering problem over already
recognized expanded-geometry OCR content. It executes no OCR.

## Inputs

- Cached P013 `full_page_triage_boxes_expanded_psm4` ranking, candidate text,
  raw OCR txt, raw OCR TSV, and prepared crop PNGs from corrected `_G1_VIRAL_002`.
- Region `page_space_box` values from the cached ranking.
- P013 reference text map, scorer-only after candidate hashes are sealed.
- Parent commit `460cb459`.

## Coordinate Contract

TSV `left`/`top` coordinates are prepared-crop coordinates, not page-space
coordinates. The cached expanded region generator added a white border of
`24` px around each crop.

Every TSV line box must therefore be mapped with:

- `page_x = region_page_space_left + tsv_x - 24`
- `page_y = region_page_space_top + tsv_y - 24`

The runner must use `region_results[].page_space_box` from the sealed ranking,
not original triage `crop_box_px`, for this transform.

## Algorithm

All parameters are fixed before reference scoring:

- prepared border: `24` px;
- lane split: `x < 1200` is left lane, otherwise right lane;
- band tolerance: `18` px on page-space y-center;
- ordering modes:
  - `source_region_order`;
  - `lane_then_y`;
  - `band_then_lane`;
  - `lane_then_y` with exact duplicate collapse.

Text units are TSV OCR line records. Reconstructing text from TSV words is the
defined preserved OCR unit for this lane; no reference token insertion,
spelling correction, fuzzy dedupe, or accepted text repair is allowed.

Duplicate collapse is allowed only in the dedicated fixed variant, and only
when normalized full line text is identical, lane id is identical, and
page-space bounding-box IoU is at least `0.85`. Otherwise repeated phrases
must remain.

## Outputs

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001/`

Allowed files under that root:

- raw mapped line records;
- line-order traces;
- duplicate-collapse reports;
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
- It must not execute OCR, render, parse PDFs, mutate source/raw assets, mutate
  accepted text, mutate semantic maps, mutate page status, create production
  output, update a selector or method registry, process page `021+`, translate,
  proofread, push, or start runtime integration.
- Candidate text and hashes must be sealed before reference text is loaded.
- All input hashes must be pinned, including TSVs and prepared crop PNGs.

## Diagnostic Gate

This lane is diagnostic only.

Diagnostic improvement requires sequence similarity greater than the best
failed P013 baseline `0.25788` and token recall at least `0.993939`.

Method-registry candidacy requires the full diagnostic threshold:
sequence similarity at least `0.997` and token recall at least `0.993939`.

## Run Result

`C01TEP013ELO-G1-VIRAL-001` completed under
`core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001`.

| Candidate | Similarity | Token recall | Diagnostic threshold met |
|---|---:|---:|---|
| `p013_expanded_lane_order_lane_then_y_exact_collapse` | `0.433325` | `0.993939` | `False` |
| `p013_expanded_lane_order_source_region_baseline` | `0.242772` | `0.993939` | `False` |
| `p013_expanded_lane_order_lane_then_y` | `0.242772` | `0.993939` | `False` |
| `p013_expanded_lane_order_band_then_lane` | `0.08596` | `0.993939` | `False` |

Interpretation: lane-aware ordering with exact duplicate collapse is the first
P013 loop stage that materially improves structure without recall loss, moving
similarity from the prior best failed baseline `0.25788` to `0.433325` while
holding token recall at `0.993939`. It still does not meet the `0.997`
diagnostic threshold, so it remains diagnostic evidence only and is not a
method-registry winner or selector rule.
