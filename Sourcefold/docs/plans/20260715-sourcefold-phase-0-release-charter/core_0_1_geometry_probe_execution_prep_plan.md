# Core 0.1 Geometry Probe Execution Prep Plan

Status: `candidate_only_geometry_probe_completed`

Lane id: `C01TEGP012013016017018020-G1-VIRAL-001`

Authorization id:
`BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-GEOMETRY-PROBE-012-013-016-017-018-020-001`

## Objective

Run the first bounded OCR geometry probe after the static input-surface router
identified pages `012`, `013`, `016`, `017`, `018`, and `020` as
`geometry_probe_required`.

The probe tests full-page-derived page-space regions rather than OCRing
existing `*-text-evidence.png` crops as source images.

## Inputs

- `C01TEISP-G1-VIRAL-001` static router result from commits `6507f386` and
  `a01da448`.
- Full-page review images from existing page-complete review packets:
  `page_012.png`, `page_013.png`, `page_016.png`, `page_017.png`,
  `page_018.png`, and `page_020.png`.
- Existing triage `crop_box_px` metadata for pages `012`, `013`, `016`, and
  `020`, used only as page-space geometry coordinates.
- Existing `C01TEFG017018-G1-VIRAL-001` full-page geometry region families for
  pages `017` and `018`, used as controls.
- Reference text maps are scorer-only and remain
  `reference_text_map_not_ocr_verified` unless a page has an OCR-verified
  reference artifact.

## Outputs

Allowed output root:

`fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002/`

Allowed files under that root:

- prepared full-page-derived regions;
- raw OCR txt/tsv/stdout/stderr files;
- candidate text files;
- per-page candidate rankings;
- JSON report;
- Markdown summary;
- manifest with output hashes.

The runner and tests may be added under `scripts/` and `tests/`.

The initial `_G1_VIRAL_001` output root is reserved for incomplete/stale
quarantine only after the first runner attempt stopped before report/manifest
completion because triage `crop_box_px` encoding was interpreted incorrectly.

## Execution Contract

- The runner must fail closed unless `--execute`, the exact authorization id,
  and the exact Bogdan decision text from Telegram message `2787` are supplied.
- The runner must refuse to overwrite an existing output directory.
- Candidate text and hashes must be written before reference text is loaded for
  scoring.
- The report must include sequence similarity, token recall,
  `similarity_delta`, and `token_recall_delta` against the P018 diagnostic
  control `0.999466` / `0.996067`.
- `014` and `019` remain parked; they are not in this execution lane.

## Boundaries

This lane may execute OCR only for pages `012`, `013`, `016`, `017`, `018`,
and `020` under the output root above. It must not render pages, parse PDFs,
read PDF text layers, mutate accepted text, mutate semantic maps, mutate page
status, mutate source/raw assets, create runtime integration, start runtime
workflows, accept source/profile/page-status/page-complete state, authorize page
`021+`, translate, proofread, push, or promote/park `C01TEFG017018`.

## Review Gate

Sol must check completeness of inputs, outputs, metrics, and dependency
lineage. Terra must check overreach, authorization boundaries, stale hashes,
and acceptance wording. OCR execution may proceed only if both reviews return
OK or all blockers are fixed.

## Run Result

`C01TEGP012013016017018020-G1-VIRAL-001` completed in corrected output root
`_G1_VIRAL_002`.

| Page | Best candidate | Similarity | Token recall | Diagnostic threshold met |
|---|---|---:|---:|---|
| `012` | `full_page_triage_boxes_expanded_psm4` | `0.98769` | `0.998024` | `False` |
| `013` | `full_page_triage_boxes_expanded_psm4` | `0.242772` | `0.993939` | `False` |
| `016` | `full_page_triage_boxes_expanded_psm4` | `0.98277` | `0.991089` | `False` |
| `017` | `full_page_bright_title_body_psm7_4_4` | `0.99923` | `0.997859` | `True` |
| `018` | `full_page_expanded_overlap_psm4` | `0.999466` | `0.996067` | `True` |
| `020` | `full_page_triage_boxes_expanded_psm4` | `0.994304` | `0.998833` | `False` |

Interpretation: the P017/P018 controls still validate the known full-page
geometry families. Pages `012`, `016`, and `020` show high completeness but
below-control structure/order; page `013` is a much stronger order/assembly
failure despite high token recall. This does not promote any candidate family
or create acceptance.

## Iterative Failure Loop

When a page fails the diagnostic threshold, the next step is not to keep
rerunning ad hoc OCR variants. The page enters a bounded improvement loop:

1. Classify the failure family from the report: order/assembly, high-recall
   structure drift, lower-recall coverage loss, unsafe surface, or stale/
   incomplete artifact.
2. Ask Sol to propose the next geometry/assembly/scoring change for that
   failure family, including exact inputs, outputs, and expected evidence.
3. Ask Terra to critique the proposed change for overreach, stale lineage,
   unsafe surfaces, acceptance leakage, and missing negative checks.
4. Implement one bounded candidate attempt only after the review gate is clean.
5. Run the attempt, score it with sequence similarity and token recall, and
   write report/summary/manifest.
6. Commit that stage, including the runner/test/docs/artifacts needed to
   restore history later.
7. Compare candidates by page and by page type. Keep failed candidates as
   evidence/history, but do not let them enter the selected production output.

The desired end state is a method registry by page type: for each page or page
family, Sourcefold knows the best available extraction method and why it won.
After all input pages have a selected method, a later production assembly lane
must run an automatic selector: either choose the known best method for each
page or run all authorized methods and select the best diagnostic result. The
production output folder must contain only the selected best page results and
the assembly manifest; failed or superseded candidates remain in evidence runs,
not in the production folder.

The acceptance loop for pages `001`-`020` is end-to-end:

1. Run the pipeline over all pages `001`-`020`.
2. Identify pages that fail the diagnostic/structural checks.
3. Improve the extraction method for the specific failed page or page family
   through the bounded Sol/Terra cycle above.
4. Commit each improvement stage so the evidence history is restorable.
5. Add the winning method to the selector/method registry.
6. Rerun the whole `001`-`020` pipeline from the same input set.
7. The target is a clean first-pass run: all twenty pages are extracted with
   their selected best method and assembled into the production output folder
   without manual intervention and without failed/superseded variants in that
   folder.
