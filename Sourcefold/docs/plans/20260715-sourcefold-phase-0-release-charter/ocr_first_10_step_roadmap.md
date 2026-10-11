# OCR-First 10-Step Roadmap

Status: draft pending user decision

This roadmap expands Sourcefold Core 0.1 into ten auditable gates. The first
six gates belong to `reconstruct`; OCR is primary acquisition, and the PDF text
layer is comparison-only evidence.

## Dependency Model

```text
immutable source_pdf
  -> page_image_set
  -> layout_map
  -> ocr_observation_set
  -> ordered_source_blocks
  -> source_text_candidate
  -> content + structure + overlay QA
  -> accepted_source_text
  -> faithful_ru_draft
  -> proofread_ru_master
  -> frozen Core 0.1 candidate
  -> independent Terra release review
```

Optional non-authoritative branch:

```text
source_pdf -> pdf_text_comparison -> findings only
```

## 0.1 Source Profile Draft

Sourcefold Core 0.1 supports one OCR-first PDF profile:

- input is one immutable, unencrypted PDF;
- the positive pilot contains 8-20 consecutive selected pages; when the PDF is
  8-20 pages, the whole PDF should be processed;
- every selected page is rendered with pinned renderer/configuration to stable
  page images with page ids, PDF-page mapping, dimensions, file hashes, and
  canonical pixel hashes;
- `300 DPI`, `8-bit sRGB`, and `PNG` remain benchmark candidates until the
  `Вирал` pilot and prior-work evidence qualify them;
- page images are canonical working visual evidence for reconstruction;
- OCR operates on page images or declared image regions and is primary;
- PDF text layer may be extracted only as a separate comparison artifact;
- PDF text layer must not populate canonical text, determine reading order,
  bypass OCR/image QA, or become a direct predecessor of accepted source text;
- supported pages use ordered vertical bands: each band is full-width or two
  non-overlapping left/right column regions;
- bounded sidebars, cards, stat blocks, examples, and callouts must be wholly
  contained in one column or occupy an explicit full-width band with explicit
  order position;
- unknown RPG structures may be preserved as `unclassified_bounded_block` only
  when complete text, geometry, reading order, and trace anchors are retained.

Unsupported in 0.1:

- ambiguous interleaved column flow;
- three or more body columns;
- overlapping text flows;
- rotated body text;
- handwriting;
- severe degradation outside the qualified preprocessing boundary;
- complex non-rectangular or nested tables;
- essential semantic text embedded only in maps or diagrams.

## Step 1: Lock The OCR-First Release Contract

Goal: replace obsolete text-layer/no-OCR assumptions with one constrained
OCR-first profile and close prerequisite decisions.

Expected artifacts:

- revised release charter;
- source-profile decision record;
- acceptance vocabulary and authorities;
- expanded lineage/DAG contract;
- waiver policy;
- fixture strategy;
- Core 0.1 acceptance-matrix skeleton;
- implementation authorization receipt.

Entry gate: current Phase 0 and captured user corrections exist.

Exit gate: profile, pilot criteria, artifact identity, non-waivable findings,
canonical formats, and authorities are accepted; roadmap validation passes; the
user authorizes implementation.

Not done yet: tool installation, schemas, modules, OCR execution, book
processing.

## Step 2: Deterministic PDF Intake And Page-Image Evidence

Goal: turn immutable PDF pages into canonical working visual evidence.

Expected artifacts:

- `source_pdf` manifest;
- selected-page manifest;
- `page_image_set`;
- renderer run record;
- PDF/page/image hashes;
- page-count and dimensions report.

Entry gate: Phase 0 authorization and approved rights-cleared pilot PDF.

Exit gate: every selected PDF page maps one-to-one to a lossless image with
stable page id, dimensions, canonical pixel hash, renderer/config identity, and
reproducible order. No missing or extra pages.

Not done yet: layout interpretation, OCR, reading order, text reconstruction.

## Step 3: Constrained Two-Column Layout Profile And Region Mapping

Goal: account for all text-bearing page regions and express provisional order
without relying on OCR text.

Expected artifacts:

- versioned `layout_profile`;
- per-page `layout_map`;
- bands, columns, regions, bounding polygons;
- region classes;
- provisional order indexes;
- conformity findings;
- profile-negative fixtures.

Entry gate: accepted `page_image_set`.

Exit gate: every text-bearing region is included exactly once or explicitly
excluded with reason; all pages conform to the locked band/two-column model;
unsupported or ambiguous layouts fail before OCR acceptance.

Not done yet: OCR accuracy, final reading order, semantic block
classification, accepted source text.

## Step 4: OCR Methodology And Toolchain Qualification

Goal: select and freeze a reproducible OCR method before running the full
pilot.

Expected artifacts:

- representative gold transcription;
- benchmark protocol and report;
- preprocessing/cropping experiment results;
- engine/model/language versions;
- canonical OCR observation schema;
- `ocr_profile`;
- lockfile/configuration;
- setup/reproduction instructions.

Entry gate: representative regions from Step 3, including dense prose, bounded
RPG structure, and table/list/sidebar samples.

Exit gate: predeclared benchmark passes. Initial threshold proposal: gold set
covers at least three pages or 20% of the pilot, aggregate raw CER <= 2%,
critical-token recall for numbers/dice/headings/names >= 99.5%, and zero
omitted declared regions. Thresholds must be set before seeing final results.

Not done yet: full-pilot OCR, canonical reading order, manual correction,
source acceptance.

## Step 5: Reproducible OCR Acquisition

Goal: OCR every declared page region and retain enough evidence to reproduce
and diagnose the run.

Expected artifacts:

- `ocr_run` manifest;
- canonical per-token/per-line observations with coordinates and confidence;
- raw engine outputs;
- region-to-OCR mappings;
- preprocessing records;
- optional `pdf_text_comparison`;
- OCR findings ledger.

Entry gate: qualified and frozen OCR profile.

Exit gate: every declared text-bearing region has exactly one current OCR
result or a blocking finding; tool/model/config identities and hashes are
complete; rerun behavior is verified; PDF-layer text has not entered canonical
text automatically.

Not done yet: accepted reading order, normalized Markdown, content correction,
semantic acceptance.

## Step 6: Reading-Order Reconstruction And QA

Goal: produce a deterministic block sequence from layout and OCR evidence.

Expected artifacts:

- `reading_order_map`;
- ordered block stream;
- many-to-many region/block mappings;
- order findings;
- regenerable reading-order overlays;
- order-QA acceptance record.

Entry gate: complete layout and OCR artifacts.

Exit gate: every OCR block occurs exactly once; there are no cycles, gaps,
duplicates, or cross-column jumps; all pilot pages receive human order review;
all ambiguous-order findings are resolved. Reading-order ambiguity is
non-waivable for 0.1.

Not done yet: full textual fidelity, final structure taxonomy, translation,
accepted source text.

## Step 7: Content, Structure, And Overlay QA; Accept Source Text

Goal: produce and human-accept canonical source Markdown.

Expected artifacts:

- anchored `source_text_candidate`;
- trace map;
- structure assignments;
- `unclassified_bounded_block` records;
- content findings;
- overlay-QA record;
- exact-hash acceptance record;
- `accepted_source_text`.

Entry gate: reading-order QA passed.

Exit gate:

- 100% of text-bearing regions trace to source blocks;
- every source block traces back to page-image evidence;
- all pages receive omission, duplication, geometry, and content overlay review;
- headings, emphasis, lists, tables, names, numbers, dates, dice expressions,
  mechanics, and bounded RPG blocks are controlled;
- no open blocking findings remain;
- permitted waivers are valid and scoped;
- a human accepts the exact artifact revision and hash.

Not done yet: cross-book taxonomy completion, translation, proofreading,
broad-layout support. OCR overlays remain generated/non-committed; durable QA
records identify inputs, configuration, page coverage, findings, and reviewer.

## Step 8: Translation And Faithful RU Draft Acceptance

Goal: translate the accepted source while preserving meaning, structure,
anchors, and mechanical data.

Expected artifacts:

- translation units;
- source-to-RU trace map;
- terminology decisions;
- translation findings;
- `faithful_ru_draft`;
- acceptance record.

Entry gate: current, non-stale `accepted_source_text`.

Exit gate: translation-unit coverage is 100%; anchors and supported structures
remain intact; names, numbers, dice, tables, and mechanics pass comparison; no
blocking semantic findings remain; human acceptance binds to exact RU draft
hash.

Not done yet: final stylistic proofreading, RU master, rendering, release.

## Step 9: Proofreading And Proofread RU Master Acceptance

Goal: produce the accepted Russian master without semantic drift.

Expected artifacts:

- proofread candidate;
- change ledger;
- semantic-drift and structure findings;
- `proofread_ru_master`;
- acceptance record.

Entry gate: accepted current Faithful RU Draft.

Exit gate: every proofreading change is attributable; source meaning and
controlled data remain intact; no blocking findings remain; exact master
revision is human-accepted.

Not done yet: candidate freeze, release promotion, `press`, `bridge`.

## Step 10: Core 0.1 RC Freeze And Independent Release Review

Goal: assemble and evaluate one frozen reproducible Core 0.1 release candidate.

Expected artifacts:

- candidate manifest;
- exact artifact/revision/hash DAG;
- tool/config inventory;
- fixture results;
- final acceptance matrix;
- reproducibility report;
- frozen evidence package;
- independent Terra release handoff;
- release decision.

Entry gate: current accepted source text, RU draft, and RU master with no stale
descendants.

Exit gate: all matrix rows pass; negative fixtures fail for expected reasons;
candidate evidence is immutable and candidate-bound; independent Terra
recommends release; named release authority promotes exact frozen candidate. If
Terra is unavailable, acceptance remains pending.

Not done yet: production/1.0 claims, generalized OCR, UI, hosted workflows,
`press`, `bridge`, knowledge-base generation, complete RPG taxonomy.

## QA Ownership Map

| Concern | Owning Step | Supporting Steps |
|---|---:|---|
| OCR methodology | 4 | 5, 10 |
| OCR/rendering/tooling | 2, 4, 5 | 10 |
| Reading-order model | 3 | 6 |
| Reading-order QA | 6 | 7, 10 |
| Content fidelity QA | 7 | 4, 8, 9 |
| Overlay QA | 7 | 6 |
| RPG structure preservation | 7 | 3, 8, 9 |
| Release evidence/reproducibility | 10 | all prior steps |

## Principal Branches And Controls

- Unsupported page profile: reject before OCR acceptance; profile violations
  are not waivable in 0.1.
- Missing PDF text layer: permitted and produces no failure.
- PDF-layer/OCR disagreement: create a finding; page-image evidence controls
  resolution.
- Low OCR confidence: reviewed correction creates a new candidate revision; no
  silent mutation.
- Unknown RPG structure: preserve as `unclassified_bounded_block` only if text,
  geometry, and order are unambiguous; otherwise block.
- Ambiguous reading order or missing region: non-waivable blocking finding.
- Changed predecessor: descendants become `stale`; old acceptance records do
  not transfer.
- Valid waiver: finding-scoped and visible; cannot cover profile violations,
  content omission, ambiguous order, broken lineage, or release-evidence
  failure.
