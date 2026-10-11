# Prior Work Evidence Index

Status: draft evidence index, updated with Sol prior-work analysis

Purpose: collect real NRI prior-work signals before Sourcefold locks OCR-first
profile parameters. This index is evidence input, not a migration of CoC/Dune
pipelines into Sourcefold.

## Evidence Sources

| Source | Evidence Signal | Use For Sourcefold | Confidence | Limitation |
|---|---|---|---|---|
| Wormsign OCR translation stand memory | A dedicated full PDF OCR translation stand existed with page workbench, metrics, page JSON/MD, and assets. | OCR-first workflow and portable evidence bundle are realistic needs. | medium | Live stand path was not present during this check; memory summary only. |
| Beyond the Edge workflow memory | Workflow had `Pages/text_layer`, `Pages/text_raw`, `Pages/ocr`, image extraction, reports, and manual review pages. | Text layer and OCR should be separate evidence layers; review loop is required. | medium | Needs targeted live report pass before parameter decisions. |
| Beyond the Edge review pages memory | Pages `001, 003, 004, 010, 012, 015, 017, 022, 023, 028, 029, 034, 035` were flagged for manual review. | OCR/source reconstruction must support page-level review/finding ledger. | medium | Does not quantify OCR error rates. |
| KeeperBook deepqa memory | Deep QA separated safe mechanical OCR fixes from items requiring human/source review; residual OCR noise included `tilde_ocr` and `latin_inside_cyrillic`. | OCR content QA must be conservative and evidence-driven. | medium | Rulebook workflow differs from scenario intake. |
| User current input | First 0.1 pilot will be first 20 pages of the `Вирал` scenario. | Pilot choice narrows source-profile validation target. | high | File not supplied yet; page structure unknown. |
| Sol targeted prior-work analysis | Prior work supports OCR-first page-image evidence but not fixed render/OCR parameters. | Demote fixed render values to benchmark candidates. | high | Still no `Вирал` file or comparative benchmark. |

## Evidence-Gated Parameters

Do not accept these values without evidence from prior reports or the `Вирал`
pilot:

| Parameter Area | Examples | Evidence Needed |
|---|---|---|
| Page rendering | DPI, color mode, image format, compression/losslessness, renderer. | Compare OCR/overlay performance and reproducibility on representative pages. |
| OCR engine/config | engine, language model, preprocessing, segmentation mode. | Benchmark on gold transcription and high-risk page regions. |
| Layout profile | one/two columns, bands, sidebars, boxed regions, headers/footers. | Prior-book taxonomy plus `Вирал` page sampling. |
| Structure taxonomy | stat blocks, cards, callouts, boxed text, captions, tables, lists, mechanics. | Prior processed book examples and pilot examples. |
| Reading-order QA | order model, ambiguity rules, non-waivable cases. | Two-column and mixed-region examples. |
| Overlay QA | geometry tolerance, coverage threshold, review artifact format. | Page-image/OCR overlay experiments. |
| Content QA | critical token classes, CER/recall thresholds, human review rules. | Gold samples and historical OCR defect classes. |

## Provisional Rules

These are safe as planning defaults:

- PDF is immutable root input.
- Page images are working visual evidence.
- OCR is primary text acquisition.
- PDF text layer is comparison-only evidence.
- One-to-one PDF-page to page-image mapping is required.
- Page-image identity should include file hash and canonical pixel hash.
- Human acceptance is required for Accepted Source Text.
- 8-20 page `Вирал` pilot is the initial candidate, pending file intake.

## Not Yet Accepted

- 300-DPI, 8-bit sRGB PNG as final render profile.
- Exact OCR engine/toolchain.
- Final RPG structure taxonomy.
- Final overlay geometry tolerance.
- Final OCR quality thresholds.

## Required Next Evidence Pass

Before Gate 1 Source Profile can be accepted:

1. Freeze the `Вирал` pilot input by PDF hash and selected page range.
2. Inventory all 20 pages for layout and RPG structure classes.
3. Predeclare gold transcription coverage and critical-token classes.
4. Compare render candidates on identical regions; do not prefer 300 DPI by
   default.
5. Compare OCR engine/config candidates against the same benchmark.
6. Record which profile values are accepted, rejected, parked, or superseded.
