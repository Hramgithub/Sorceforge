# Sol Prior-Books Map Evidence Handoff

- Role: `gpt-5.6-sol`, prior-work evidence scout / architect, high effort.
- Review kind: targeted read-only evidence gathering; not Sourcefold design or release acceptance.
- Timestamp: `2026-07-15T19:23:05+03:00`.
- Scope: prior processed NRI scenarios/books; reports, plans, manifests, and status only. No raw PDFs or image inspection.

## Result

- Prior work supports three linked but distinct maps. It does **not** support one flat page taxonomy or inheritance of any legacy schema.
- The recurring evidence unit is: `document/page identity -> provisional page role -> bounded regions and reading order -> art/asset provenance and source placement -> QA/decision state`.
- `doc_map`, `content_map`, and `art_map` should remain provisional evidence claims before OCR. They must cross-reference one another, preserve unknown/mixed cases, and remain separate from later reader/press placement decisions.

## 1. Page Types Recorded Or Implied

- **Beyond the Edge of Darkness (37 pages):** cover/visual, credits/legal, contents, author note, overview/background, setup and hooks, timeline, title/transition, rules/cult material, stat block/effects, narrative investigation/location pages, handout/map visual pages, finale/endings, acknowledgements, and image credits. Its page map was structural and explicitly allowed output pagination to diverge from source pagination.
- **Keeper's Book (399 source pages; 330 included page markers):** chapter openers, normal rules/reference prose, complex tables, full-page map, forms/sheets, appendices/reference, diagrams, and an embedded scenario chapter excluded by a user-approved product boundary. Pages 45-47 were mixed form/table/narrative pages requiring region-specific reconstruction, not one page-wide OCR strategy.
- **Wormsign (32 pages):** cover/full visual, credits background, normal content, scenario opener, inline/side/full-width art pages, visual placeholders, sheets/cards, stat blocks, tables, and pregenerated-character full-page visuals later compacted for production flow.
- **Desertflower (19 pages, narrow corroborating check):** cover, credits, TOC, full-page art, title/epigraph, ordinary two-column narrative, quote-art, NPC/stat-card, and visual/empty pages. Fixed left/right OCR zones produced noise on visual and credits pages, proving page/region classification must precede OCR routing.
- Required implication: page role is multi-label. `mixed`, `unknown`, and secondary roles are first-class; a page cannot always be reduced to one enum.

## 2. Content Structures That Caused QA Work

- Reading order across two columns, sidebars, images, and transitions; Beyond retained page-level review history, and Desertflower required render plus column-OCR reconstruction on most body pages.
- Complex tables and grid semantics: percentage lookup matrices, transport/collision tables, phobias/manias, financial tables, weapons/skills, and appendix flow diagrams.
- Stat blocks and character/NPC cards: automatic detection missed known candidates; values and labels required source-semantic review even after formatting checks passed.
- Forms/sheets combining field labels, tables, narrative text, and decorative frames. Keeper's Book evidence used a hybrid strategy: structured text/table reconstruction plus retained image references for irreducible regions.
- Boxed text, callouts, sidebars, quotes, lists, footnotes, examples, captions, and mechanics/data tokens. Wormsign's release evidence tracked anchor kinds for callout, card, full art, image, sheet, stat block, table, and visual placeholder.
- Chapter/section boundaries, page markers, inclusions/exclusions, TOC/index links, and source-to-reader pagination. Keeper's Book boundary corrections and Beyond's stale page-map/build-version pair show these records must be artifact-versioned and supersedable.
- OCR defects survived structural success: Keeper's Book had 330 page markers, zero missing images, and a buildable output while deep QA still found 1,335 candidates. Structural completeness cannot substitute for content fidelity.

## 3. Art / Placement / Asset Data Actually Tracked

- Source page, extract/xref or page-render crop, file path, format, dimensions, hashes, page-use count, and extraction method.
- Source kind (`pdf_direct`, page-render crop, legacy/derived), asset form, crop kind, bounding box/full-page state, derivation links, and normalization policy.
- Semantic/production role: cover, credits background, scenario inline art, full-width/side illustration, map, handout, portrait/card, diagram, decoration/mask, or excluded evidence.
- Content risk: clean/no text, essential or contaminating text, raw/unreviewed, forbidden text overlap, and whether visual review was required/completed.
- Source relationship and placement: after heading, after quote, float with wrap, full-width, background, replace visual page, or compact after table; plus break policy and protected neighboring blocks.
- Decision state and reason: approved, candidate, needs review, raw evidence, excluded; exclusions were explicitly accounted for. Wormsign tracked 117 inventory assets, 16 placements, and 101 exclusions. Beyond kept 306 extracted objects while promoting only selected stable assets; Keeper's Book selected 19 of 400 extracts; Desertflower approved 7 and rejected 11 reviewed candidates.
- Provenance distinctions mattered: direct extract versus composite render crop; source illustration versus player handout; original source asset versus generated reconstruction; master PNG versus runtime JPEG derivative. These must not collapse into one `image_path` field.

## 4. Evidence-Informed Map Contracts

- **Common envelope:** bind every map to source PDF identity/hash, page count, map schema version, producer/method, timestamp, evidence references, and supersession state. Historical reports demonstrate that unbound mutable status becomes stale.
- **`doc_map` page record:** stable `page_id`, PDF index, printed label if any, section path/boundary claim, primary and secondary roles, text/art/mixed flags, provisional layout family (columns/bands/rotation), inclusion disposition plus reason, benchmark/review flags, assignment method/confidence, verification state, and evidence refs. Every PDF page remains accounted for even if excluded from a later product projection.
- **`content_map` region record:** stable `region_id`, `page_id`, normalized geometry, parent/child relationship, provisional structure type, text-bearing state, reading-order sequence or explicit graph edges, criticality (rules/numbers/names/handout text), handling branch, ambiguity/finding state, and evidence refs. `unclassified_bounded_block` must preserve geometry, order, and completeness obligations rather than act as permission to drop content.
- **`art_map` region/asset record:** distinguish visible art region from extractable PDF object; record page, geometry/full-page state, source asset/xref or render crop, hash/dimensions/format, semantic role, text-content risk, source anchor relationship, derivation lineage, review/decision state, and exclusion reason. Keep `source_placement` separate from optional `projection_placement`; legacy HTML/CSS placement is press evidence, not reconstruct authority.
- Cross-map references are required: content containing essential text can point to an art region; composite art can point to multiple extracted objects or a render crop; a mixed page can own multiple content and art regions.

## Dependencies And Branching

- Intake identity and one-to-one page inventory precede all maps. Page-role and region claims then select benchmark samples and OCR routing; they do not authorize OCR.
- Narrative one/two-column pages may use zoned OCR only after region/order declaration.
- Cover, full-art, map, visual, and sparse pages bypass normal column OCR but still require essential-text inventory and explicit handling.
- Credits and TOC may look tabular but have distinct semantics. Any generated TOC or redesigned credits block belongs to a later projection, while source entries/order remain reconstruction evidence.
- Tables, stat blocks, cards, forms, and sheets branch to structure-aware or manual reconstruction plus value-level QA.
- Images containing essential text, handouts, maps, and diagrams participate in both `content_map` and `art_map`.
- Direct image extraction and page-render crops are alternative evidence branches; masks, layers, and repeated background objects require composition/triage rather than automatic promotion.
- Unknown/mixed regions block silent completion and route to review; they do not force premature taxonomy expansion.

## Risks And Concrete Remediation

- **Taxonomy overfit:** use extensible labels, secondary roles, and unknown/mixed fallbacks; qualify categories against the pilot rather than freezing the observed CoC/Dune labels.
- **Source/output conflation:** separate source page/region role and source placement from reader/press projection. Beyond output pagination and Wormsign art compaction prove they diverge legitimately.
- **Fixed segmentation:** prohibit applying one/two-column zones to visual, credits, form, or mixed pages without page/region qualification.
- **PDF object equals illustration fallacy:** require visible-region-to-object/crop linkage and an accounted exclusion reason for every extracted candidate.
- **Structural green hides semantic defects:** make reading-order, critical-token/value, and human source review independent gates from marker/link/image-count checks.
- **Derived asset confusion:** require source kind and derivation lineage; generated/reconstructed player assets cannot be represented as original source evidence.
- **Stale evidence:** bind claims and decisions to artifact hashes/versions and mark later records as superseding earlier ones; do not infer current acceptance from an old QA file.
- **Legacy inheritance:** do not copy `translator_*` schemas, R-stage names, package paths, CSS classes, hardcoded OCR zones/PSM, image selection thresholds, one-column production choice, or approval vocabulary into Sourcefold without separate qualification.

## Assumptions

- Pre-OCR maps are reconnaissance artifacts and can contain human-assigned or tool-suggested provisional claims.
- Sourcefold Core 0.1 must preserve source semantics and traceability; Knowledge Base generation and press styling remain outside the normal core lane.
- No conclusion here qualifies DPI, color mode, container, OCR engine/config, numeric thresholds, or the final RPG taxonomy.

## Acceptance Criteria For A Future Map Specification

- Source hash/page count are bound, and every PDF page is represented exactly once in `doc_map`; no page is silently omitted.
- Every benchmark-page content-bearing region has geometry, provisional type, handling branch, reading-order relation, evidence reference, and verification state, or is explicitly `unclassified_bounded_block` with a review blocker.
- Every visible art region is linked to direct object(s), a composite/render crop, or an explicit unresolved state; every extracted candidate is included, excluded, or held for review with reason.
- Essential text inside images is dual-linked between content and art records.
- Source role/placement and projection role/placement are distinct fields.
- Human/tool assignment, confidence, verification, acceptance, supersession, and artifact identity are not conflated.
- Fixtures cover at least: cover, credits, TOC, full-art, normal two-column, mixed/sidebar, table, stat/card, handout/map, form/sheet, and appendix/reference pages.
- Map completion does not advance OCR, source acceptance, or release gates by itself.

## Evidence Checked

- Sourcefold assigned `plan.md`, `context.md`, `PROJECT_STATUS.md`, current `pre_ocr_mapping_model.md`, prior evidence index/handoff, and nested `AGENTS.md`.
- Beyond: `PLAN.md`; QA `page_mapping`, `completeness`, `source_text`, `final_acceptance`, `assets`, `source_images`, `extraction`, `statblocks`, `handouts`, and image-gap reports.
- Keeper's Book: plan/status; production, integration, deep-QA, batch manifest, blocking-page reconstruction, and image-intake reports.
- Wormsign: package plan/manifest; art manifest, art integration/layout QA, release QA/manifest, and post-production image QA.
- Desertflower corroboration: project status plus PDF intake/render, text/column-OCR/reconstruction, stat-block, image inventory/classification, layout-anchor, and art-integration QA reports.

## Receipt

- Scope result: completed; evidence supports layered, cross-linked, provisional maps and rejects flat inherited taxonomy.
- Files changed: this new immutable handoff receipt only.
- Verification/evidence: targeted `rg --files`, report/manifest reads, JSON field/count inspection; no raw PDFs/images opened and no processing commands run.
- Blockers: no pixel-level validation by scope; cleaned Wormsign package no longer retains the original live layout-anchor payload at the referenced historical path; heterogeneous reports are not a unified Sourcefold contract; `Вирал` remains unprocessed candidate input.
- Next action: orchestrator may integrate these evidence constraints into `pre_ocr_mapping_model.md`; a separate Terra critique and user decision are still required before design or release acceptance.
- Elapsed time: approximately 22 minutes.
- Token use: unavailable from this subagent runtime.
