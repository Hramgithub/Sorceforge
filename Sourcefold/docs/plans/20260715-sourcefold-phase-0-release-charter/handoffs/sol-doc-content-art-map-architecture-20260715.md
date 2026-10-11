# Sol Doc/Content/Art Map Architecture Handoff

Role: `gpt-5.6-sol`
Review kind: architecture
Status: completed
Timestamp: 2026-07-15T19:19:46+03:00

## Result

Sol recommends three immutable map artifacts sharing one identity/geometry
layer and packaged as a versioned `pre_ocr_map_bundle`.

## Architecture

- `doc_map`: document/page topology and complete region registry.
- `content_map`: text-bearing and structurally meaningful regions.
- `art_map`: visual, decorative, mixed-media, and text-in-art regions.
- `layout_map`: remains a derived operational projection; it is not renamed to
  `content_map`.
- Downstream artifacts reference the exact bundle hash, not loose current files.
- Map purpose must be explicit: `qualification`, `runtime`, or
  `fixture_expected`.

## Lifecycle

- Step 1: accept protocol and map contracts.
- Step 2: create selected-page manifest and seed/render-bound `doc_map`.
- Step 3: create/review `content_map`, `art_map`, and the first frozen
  pre-OCR bundle; derive `layout_map`.
- Step 4: use map risk classes to select gold regions and OCR routes.
- Steps 5-7: consume/reconcile the frozen bundle; map corrections create
  superseding revisions and stale affected descendants.
- Steps 8-10: maps become read-only evidence and release lineage inputs.

## Format Recommendation

- Canonical map evidence: JSON with JSON Schema.
- Human review/explanation: Markdown generated from or linked to JSON.
- Roadmap: YAML state and references only, not map payload.
- Large maps may be per-page JSON shards with a canonical bundle index.

## Visualization

Roadmap viewer should show badges/counts/links only. A separate document
explorer should render page navigation, layer toggles, normalized-coordinate
overlays, region details, revision comparison, and lineage links. The
visualization is not editable source of truth.

## Blockers

Qualification Protocol, canonical formats, artifact identity/canonicalization,
acceptance authority, and explicit art/mixed-region matrix rows remain
unresolved.
