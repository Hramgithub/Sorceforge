# Sol Doc/Content/Art Map Analysis Handoff

Role: `gpt-5.6-sol`
Review kind: taxonomy and prior-evidence analysis
Status: completed
Timestamp: 2026-07-15

## Result

Sol recommends three linked, revisioned maps for pre-OCR reconnaissance:
`doc_map`, `content_map`, and `art_map`. They remain `proposed` and
`evidence_gated`, not accepted design or release approval.

## Proposed Taxonomy

- `doc_map`: one record per selected PDF page.
  Candidate page functions: `cover`, `title`, `credits_legal`,
  `contents_index`, `section_opener`, `body`, `reference_heavy`,
  `handout_facsimile`, `map_diagram`, `art_plate`, `appendix_backmatter`,
  `advert_service`, `blank`, `mixed`, `unclassified`.
- `content_map`: text-bearing or potentially text-bearing regions.
  Candidate structures: `heading`, `paragraph`, `quote`, `list`,
  `simple_table`, `complex_table`, `boxed_text`, `callout`, `sidebar`,
  `stat_block`, `card`, `caption`, `footnote`, `header`, `footer`,
  `folio_page_marker`, `toc_index_entry`, `map_key_legend`, `handout_text`,
  `unclassified_bounded_block`.
- `art_map`: visually distinct source-art regions.
  Candidate kinds: `illustration`, `photograph`, `portrait`, `map`,
  `diagram_chart`, `handout_facsimile`, `logo_masthead`, `icon_glyph`,
  `ornament_border`, `background_texture`, `layout_fragment`, `unknown`.

## Key Controls

- Maps must share PDF/page/page-image identity, coordinates, map revision,
  profile reference, provenance, confidence, review state, cross-map IDs, and
  invalidation links.
- Pre-OCR maps may declare observations and provisional structure/order
  constraints. They must not contain OCR text or accepted semantic source truth.
- RPG semantic roles such as clue/NPC/location/spell/item are post-OCR
  annotations or later KB work, not trusted pre-OCR classes.
- Art/content overlap is expected; ownership must identify which region supplies
  OCR text to prevent duplicate acquisition.

## Evidence Note

Targeted Beyond evidence showed cover, credits, contents, transition, body,
stat-block, handout, map/key, appendix, and art-heavy pages, including retained
review states and order-sensitive placement. This supports map thinking but
does not accept a Sourcefold schema.

## Blockers

- Qualification Protocol missing.
- Render profile and taxonomy evidence remain unaccepted.
- No `Вирал` mapping may start from this handoff alone.
