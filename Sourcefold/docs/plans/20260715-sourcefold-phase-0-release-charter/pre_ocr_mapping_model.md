# Pre-OCR Mapping Model

Status: draft proposal, evidence-gated; not approved for implementation

Purpose: define how Sourcefold should describe a PDF before OCR so the project
can reason about page types, content structures, and art placement without
pretending that text has already been reconstructed.

This document is part of Gate 1 planning. It does not authorize rendering, OCR,
translation, proofreading, map collection from `Вирал`, or real book processing.

## Working Concept

Before OCR, Sourcefold should produce a structural reconnaissance package:

```text
source_pdf
  -> selected_page_manifest
  -> page_image_set
  -> pre_ocr_map_bundle
       -> doc_map
       -> content_map
       -> art_map
  -> derived layout_map
  -> OCR qualification/run
```

The maps are evidence inputs for Gate 1 Qualification Protocol. They describe
what must be handled, sampled, excluded, or reviewed before OCR and later source
acceptance.

Terra critique blocks implementation until the Qualification Protocol, selected
page manifest, canonical formats, identity, authority, trace anchors, and
fixture rules permit this work.

## Map Layers

| Layer | Purpose | Pre-OCR Status |
|---|---|---|
| `doc_map` | Page-level structure, selected-page identity, and complete region registry. | Conceptual until exact protocol acceptance plus a distinct bounded map authorization; later required before benchmark samples. |
| `content_map` | Text-bearing or structurally meaningful regions referencing `doc_map.region_id`. | Provisional before OCR; confirmed or corrected after OCR/layout QA. |
| `art_map` | Visual/mixed/art regions referencing the same region registry. | Provisional before OCR; semantic art mapping parked for Core 0.1. |
| `pre_ocr_map_bundle` | Exact revision bundle containing the three maps and shared identity/geometry references. | Proposed architecture; canonical format not accepted. |

Maps must not be independent manually maintained inventories. They are
projections over one shared page/region identity layer.

## Shared Identity Fields

All maps and bundles should eventually carry:

- `source_pdf_id` and source hash;
- selected-page manifest reference;
- page image reference and hash when render-bound;
- stable page IDs and region IDs;
- normalized coordinates plus render-specific pixel projections;
- `map_version`, purpose, profile reference, and provenance;
- observation state: `observed`, `inferred`, `reviewed`, or `resolved`;
- confidence and review status;
- cross-map references;
- supersession and invalidation conditions.

Purpose must be explicit:

- `qualification`: Gate 1 evidence only; not accepted source evidence.
- `runtime`: later Core 0.1 processing evidence.
- `fixture_expected`: expected fixture map.

## Candidate `doc_map` Categories

The map should identify page/section roles such as:

- cover or landing page;
- table of contents;
- credits/legal/front matter;
- introduction;
- body/chapter content;
- handout/player-facing page;
- appendix/reference;
- index/back matter;
- map-heavy page;
- full-page art page;
- advertisement/promo or non-content page;
- unknown or mixed page.

Use orthogonal fields for page function, layout, and modifiers instead of
creating combined page classes such as `two_column_chapter_opener_with_art`.
`mixed`, `unknown`, and secondary roles must be first-class.

## Candidate `content_map` Categories

The map should identify content structures such as:

- headings and subheadings;
- body paragraphs;
- lists;
- tables;
- boxed text or callouts;
- sidebars;
- stat blocks;
- character/NPC cards;
- item/spell/clue cards;
- examples;
- captions;
- page headers/footers;
- page numbers/markers;
- rules/mechanics/data tokens;
- unknown bounded content block.

Pre-OCR `content_map` may identify structural candidates and OCR routing. It
must not contain OCR transcription, PDF text-layer text, or trusted RPG semantic
roles such as clue/NPC/location/spell/item. Those belong after OCR or to a
future KB direction.

## Candidate `art_map` Categories

The map should identify art/image regions such as:

- full-page art;
- full-bleed or background art;
- centered illustration;
- side illustration;
- inline illustration with text wrap;
- crop/detail art;
- map/diagram;
- portrait/card image;
- decorative ornament or divider;
- logo/icon;
- image containing essential text;
- art anchored to a section, heading, block, table, stat block, or page.

Pre-OCR `art_map` may identify visual regions, text interaction, overlap, and
handling. Subject/style semantics and press placement are parked outside Core
0.1 unless separately chartered. Source placement and later projection
placement must remain distinct.

## Evidence From Prior Work

Targeted prior-work evidence supports layered maps:

- Beyond used page mapping and QA reports that distinguished cover, credits,
  contents, body, stat blocks, handouts, maps/keys, appendix, and art-heavy
  pages.
- Keeper's Book evidence showed that structural success can coexist with
  substantial OCR defects; reading-order and semantic QA need independent gates.
- Wormsign evidence tracked source art, derived crops, placement, exclusions,
  and production decisions separately.
- Desertflower evidence showed fixed column OCR can create noise on visual or
  credits pages if page/region type is not known first.

These are evidence points only. Sourcefold must not inherit legacy stage names,
schemas, thresholds, CSS placement, package policies, or approval vocabulary.

## Proposed Gathering Sequence

No `Вирал` mapping starts until the exact protocol revision is
`accepted_protocol` and a distinct bounded authorization names the exact
candidate-derived action. Protocol acceptance alone never creates or confirms
intake, selected-page manifests, renders, map seeds, annotations, map bundles,
viewer evidence, or OCR inputs.

Future sequence after protocol acceptance and separate bounded authorizations:

1. Accepted protocol revision exists, but authorizes no candidate-derived
   action by itself.
2. A distinct bounded intake authorization may create or update only the named
   intake record fields.
3. A distinct bounded selected-page-manifest authorization may create or update
   only the named selected-page manifest.
4. A distinct bounded render authorization may create or update only the named
   render evidence when map collection is render-bound.
5. Accepted or version-bound provisional schema and identity interfaces define
   map layer, page, region, coordinate, and bundle identity before any map
   collection.
6. A distinct bounded map-collection/annotation authorization may create or
   update only the named `doc_map`, `content_map`, or `art_map` artifacts and
   must name observation rules, tools, reviewers, outputs, limits, expiry, and
   invalidation behavior.
7. Human/tool review checks only the pages/regions authorized by the
   map-collection/annotation action for text, art, mixed, unknown, overlap, and
   exclusions.
8. A distinct bounded map-bundle-freezing authorization may create or update
   only the named `pre_ocr_map_bundle` artifact from already existing map
   revisions. The collection/annotation authorization must not freeze the
   bundle.
9. OCR benchmarking or OCR run consumption may use map evidence only after the
   map bundle is current, reviewed, and explicitly admitted by its own
   downstream bounded authorization.

Automation may propose regions and labels only inside a bounded authorization.
Evidence must record tool identity, confidence, and human review state. PDF
text-layer availability may be noted only when authorized, but text-layer
content/order must not populate these maps.

## Proposed Storage And Format

- Canonical map evidence: JSON with JSON Schema.
- Bundle: `pre_ocr_map_bundle` referencing exact `doc_map`, `content_map`, and
  `art_map` revisions by hash.
- Human review/explanation: Markdown generated from or linked to JSON.
- Roadmap: YAML state, checklist, and links only; no map payload.
- Large maps may use per-page JSON shards with a canonical bundle index.
- Visualization: the current roadmap viewer shows dependency/status metadata
  for the map model only. A later map viewer may visualize page regions, but it
  must read from canonical map artifacts, not from roadmap YAML.

Candidate schema names:

- `common_map.schema.json`;
- `doc_map.schema.json`;
- `content_map.schema.json`;
- `art_map.schema.json`;
- `pre_ocr_map_bundle.schema.json`.

Actual paths remain pending the canonical-format and artifact-identity
decisions.

## Roadmap And Gate Alignment

- `phase-0`: owns contract decisions and acceptance semantics.
- `gate-01-source-profile`: owns Qualification Protocol and qualification map
  bundle decisions.
- `gate-01-pre-ocr-map-model`: tracks this model as a visible Gate 1
  dependency in the roadmap viewer.
- `decision-source-profile-0.1`: decides source boundaries and unsupported
  cases.
- `decision-canonical-formats`: chooses JSON/schema/canonicalization.
- `decision-artifact-identity`: defines map IDs, revisions, bundle identity,
  hashes, and supersession.
- `decision-trace-anchor-model`: defines shared page/region IDs and later block
  mappings.
- `core-0.1`: may later require a frozen map bundle in its evidence DAG.

Current roadmap dependency:

```text
phase-0
  -> gate-01-source-profile
  -> gate-01-qualification-protocol
  -> gate-01-pre-ocr-map-model
  -> decision-source-profile-0.1
```

This means the map model is a Gate 1 input to the source-profile decision. It
does not become a second roadmap, a second source of truth, or an authorization
to process the `Вирал` candidate.

Parameter alignment:

- `doc_map`: input envelope, pilot range, page coverage, image identity, profile
  reference, invalidation.
- `content_map`: layout parameters, structure taxonomy, fallback blocks, region
  coverage, ambiguity.
- `art_map`: mixed/visual region coverage, text-in-art handling, maps/diagrams
  boundary, unknown fallback.

## Page-Map Readiness Indicators

Page-map readiness is a review-routing signal, not page-complete acceptance.
It helps decide whether a later bounded page-complete review packet can be
prepared for a page. It does not accept source text, accept a page as complete,
admit fixtures, advance Gate 1, run OCR, extract a PDF text layer, mutate raw
OCR output, or authorize any candidate-derived action by itself.

Each future page-complete readiness packet should be reproducible from already
authorized artifacts and should declare, for every page under review:

- page identity: stable page id, source image reference, predecessor map/source
  evidence, and currentness state;
- block inventory: expected block count and one row per observed or expected
  block, including block id, region id when available, content type, geometry
  or anchor reference, reading-order position when known, and review state;
- content type: `text`, `title`, `art`, `inset`, `table`, `callout`,
  `page_marker`, `caption`, `mixed`, `unknown`, or an explicitly versioned
  extension;
- block role state: `in_scope_text`, `context_only`, `excluded`, `unknown`,
  `missing`, or `blocked`;
- source state: no source text, draft text, human-verified text, accepted
  source record, or not applicable;
- structure state: heading/title, paragraph/body, label/value, list, table,
  legal/footer, URL, art-only, text-in-art, inset/container, or unknown;
- advisory coverage summary for inventory, accepted in-scope text,
  context/exclusion decisions, and QA rows;
- blockers and open questions that prevent a later page-complete acceptance
  packet.

Coverage percentages are advisory only. A page with high percentage coverage
can still be blocked by one missing table cell, title, number, caption, page
marker, overlay, clipped text, duplicate region, stale anchor, or ambiguous
reading order. Page-complete acceptance must remain a later bounded decision
that proves exact required scope-unit x criterion coverage, not a percentage
threshold.

OCR/text fidelity indicators may be declared only from already-authorized,
already-existing artifacts. They may compare raw OCR output, normalized OCR
output, assisted draft text, human-verified text, and accepted source text only
when those artifacts already exist under their own bounded authorizations.
Readiness packets may record character counts, normalized character counts,
line counts, protected-token mismatches, URL/name/number mismatches, and a
human-readable discrepancy disposition. They must not run OCR, rerun OCR,
extract PDF text-layer payloads, edit raw OCR output, or create accepted source
text.

Semantic checks in readiness packets are limited to structural preservation and
source-traceability risks: heading level versus visual presentation, label/value
pairs, legal/footer roles, URLs, names, numbers, dice/mechanics tokens, tables,
captions, insets, art-only blocks, and unsupported semantic claims. A readiness
semantic label is not RPG/source truth and cannot become accepted semantics
without later evidence-bound source acceptance.

Semantic-map readiness uses three explicit states:

- `semantic_map_ready`: the canonical semantic-unit JSON validates under the
  versioned schema/taxonomy, its Markdown projection validates as a projection
  only, page inventory reconciliation is valid, and no non-waivable structural
  finding remains before page-complete decision options are rendered.
- `semantic_map_blocked`: semantic-unit validation, Markdown projection
  validation, or page inventory reconciliation has a non-waivable blocker such
  as `invalid_heading_level`, `collapsed_units`, `missing_expected_heading`,
  `quote_flattened`, `missing_expected_unit_type`,
  `table_structure_flattened`, `stat_block_flattened`,
  `callout_container_unresolved`, `style_is_block_role`, stale schema/taxonomy,
  missing/ambiguous reading order, unsupported/unknown region leakage, or
  broken lineage.
- `semantic_unit_review_only`: a unit is present to make human review explicit,
  but it is not accepted source text, not OCR verification, not PDF text-layer
  evidence, not fixture admission, not page-complete acceptance, and not Gate
  acceptance.

Canonical semantic-map evidence is JSON. Human Markdown maps must be generated
from that JSON and validated as projections. Long prose belongs in per-unit
fenced text blocks, not table cells. Status, roadmap, and checkpoint documents
may store IDs, states, and hashes only; they must not become a second semantic
payload store.

Any readiness or page-complete review packet with non-waivable semantic,
projection, or inventory findings must suppress complete-ok/acceptance routing
and expose only hold/blocker paths until a superseding packet is generated
under the current contract.

Overlay, reading-order, and recovery indicators must be explicit:

- every in-scope block needs a stable anchor or a current recovery blocker;
- reading order must be declared or marked ambiguous;
- overlapping or nested regions must state whether one is context-only,
  container-only, or a separate source block;
- duplicate text through an inset/container and child text blocks must be
  blocked unless the relationship is explicitly resolved;
- clipped, hidden, or visually occluded text remains a blocker until a later
  bounded action repairs or excludes it.

For page 002, the current readiness interpretation is: two required in-scope
text blocks are known, the credits block and the boxed legal/footer block; both
have accepted source records; no context-only block, missing text block, or
blocker is currently identified by the triage. Page 002 still requires a
separate page-complete review packet before any page-complete acceptance can be
considered.

## Open Questions

- Which categories are accepted Gate 1 requirements versus future taxonomy?
- What is the minimum pre-OCR evidence for a page/content/art classification?
- Which labels may be human-assigned, tool-suggested, or must be verified later?
- How should maps be visualized in the roadmap/viewer or a dedicated PDF map
  viewer?
- Which parts are Core 0.1 versus post-0.1 or press/KB parking?

## Current Guardrails

- Pre-OCR maps must not replace OCR, reading-order QA, content QA, or overlay
  QA.
- A map label is not acceptance. It is a claim needing evidence and later
  confirmation.
- The `Вирал` PDF remains a candidate input only until the Qualification
  Protocol defines intake and sampling rules.
- A semantic art/content label must not become source truth before OCR and
  trace anchors exist.
- Map completion cannot unlock Core 0.1 independently of Gate 1 roll-up rules.
