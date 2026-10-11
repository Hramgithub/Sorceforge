# Sol Prior-Work Evidence Analysis Handoff

Role: `gpt-5.6-sol`
Review kind: architecture/evidence analysis
Status: completed
Timestamp: 2026-07-15T03:27:53+03:00

## Scope

Read-only analysis of Sourcefold Phase 0 OCR-first notes and targeted prior
NRI evidence. The task was to determine what prior work can support before
locking Gate 1 Source Profile parameters.

## Result

Prior work supports the OCR-first architecture, but does not justify locking
`300 DPI`, `8-bit sRGB`, `PNG`, any OCR engine, or numeric OCR thresholds.
Those values must remain benchmark candidates until tested against the first
20 pages of the `Вирал` pilot.

## Evidence Signals

| Source | Signal | Sourcefold Use | Limitation |
|---|---|---|---|
| Sourcefold OCR profile notes | PDF -> page images -> OCR -> reviewed source text is the right authoritative chain. | Confirms OCR-first direction. | Product direction, not parameter evidence. |
| Sourcefold OCR-first roadmap and critique | Rendering, layout, OCR, order, content, and overlay must be separate gates. | Confirms staged control model. | Existing render values are proposals only. |
| Wormsign OCR stand receipt | Prior work needed page workbench, page assets, records, indexes, and metrics. | Supports durable page-level evidence packages. | No comparative render/OCR parameter metrics found. |
| Beyond scenario reports | Workflow separated page PNGs, PDF text/raw layers, OCR, page review, completeness, and image extraction. | Supports separate evidence layers and page review. | Not a Sourcefold acceptance model. |
| KeeperBook QA evidence | OCR defects can survive structural checks; conservative visual/source review is required. | Confirms independent text-fidelity QA. | No retained render/engine configuration. |

## Provisional Now

- OCR-first PDF profile.
- Immutable PDF as root evidence.
- Page images as working visual evidence.
- PDF text layer as comparison-only evidence.
- One-to-one PDF-page to page-image mapping.
- Canonical pixel hash plus ordinary file hash.
- Separate layout, OCR, order, content, structure, and overlay gates.
- Bounded one/two-column layout as the initial supported family.
- `unclassified_bounded_block` fallback only with complete text, geometry,
  order, and anchors.
- Human acceptance bound to exact artifact identity and hash.

## Evidence-Gated

- Exact DPI.
- RGB/grayscale, bit depth, and image container.
- Renderer and rasterization parameters.
- OCR engine, models, segmentation, preprocessing, and confidence policy.
- Final supported/deferred layout classes.
- Final RPG structure taxonomy.
- Numeric OCR and overlay thresholds.
- Whether one profile handles all 20 pilot pages without exceptions.

## Required Evidence-Pass Gates

1. Pilot intake: hash and freeze the `Вирал` PDF and pages 1-20.
2. Page inventory: classify every page and text-bearing region before samples.
3. Render qualification: compare candidate raster profiles on identical regions.
4. OCR qualification: compare engine/config candidates against predeclared gold
   transcription.
5. Layout/order qualification: review all 20 pages for missing, duplicated, or
   ambiguous regions.
6. Overlay qualification: review region coverage, OCR geometry, order sequence,
   and source-block trace overlays.
7. Profile lock: choose the least costly passing configuration and bind exact
   renderer/OCR/preprocessing identities.
8. Structure lock: publish supported, fallback, and rejected classes with
   evidence references.

## Recommendation

Demote `300-DPI, 8-bit sRGB PNG` from normative profile to benchmark candidate.
No numeric render/OCR parameter should be locked without benchmark evidence.

## Receipt

- Files changed: none by subagent.
- Verification: targeted reads only; no recursive CoC/Dune scan.
- Blocker: pilot PDF is not supplied yet.
- Token use reported by subagent: 81,608.
