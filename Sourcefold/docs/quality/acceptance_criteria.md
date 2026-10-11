# Acceptance Criteria

Sourcefold accepts artifacts by stage. Signals can open findings, but acceptance
requires resolved findings and explicit evidence.

## Reconstruct

- Source pages or blocks are accounted for.
- Reading order is preserved.
- Headings, emphasis, quotes, lists, tables, cards, stat blocks, and page
  markers are preserved when traceability matters.
- Page-complete review cannot be requested from a readiness packet until the
  semantic map is valid, the Markdown projection is valid, page inventory is
  reconciled, and no non-waivable structural finding remains.
- Canonical semantic review evidence is JSON. Markdown text maps are
  human-facing projections and cannot override JSON validation or inventory
  reconciliation.
- Numbers, dates, dice notation, mechanics, names, and definitions are not
  silently changed.
- Uncertain readings are marked and tracked.
- Accepted Source Text has source evidence and an acceptance ledger.

## Page-Complete Review

- `semantic_map_ready` means the page's semantic-unit JSON artifact validates,
  its Markdown projection validates, and every observed/expected region is
  reconciled against semantic units before decision options are exposed.
- `semantic_map_blocked` means at least one non-waivable semantic, projection,
  or inventory finding exists; complete-ok and acceptance routing must be
  suppressed until a superseding packet resolves or explicitly reclassifies the
  finding.
- `semantic_unit_review_only` units may help a human inspect a packet, but they
  do not accept source text, OCR, page completeness, fixture admission, or Gate
  state.
- Structure loss is acceptance-relevant: collapsed headings, quotes, tables,
  cards, stat blocks, callouts, captions, page markers, or continuation links
  block page-complete acceptance even when the visible prose is present.
- Status and roadmap documents may store semantic map IDs, states, and hashes;
  semantic payloads stay in canonical artifacts.

## Translate

- RU draft preserves source meaning and logical relations.
- Rule modality, conditions, negations, and subjects of action are preserved.
- Tables, lists, stat blocks, formulas, numbers, dates, names, and definitions
  remain structurally and semantically intact.
- Terminology decisions record provenance and applicability.
- Translation findings are resolved or explicitly waived.

## Proofread

- Russian grammar, punctuation, agreement, and style are reader-ready.
- Edits do not change source meaning, mechanics, or data.
- Semantic findings and language findings share provenance.
- No unresolved proofreading findings remain before RU master acceptance.

## Press

- Press output is built from an accepted RU master.
- Rendering does not alter accepted text meaning.
- Layout defects are tracked separately from core text acceptance.

## Bridge

- Exports identify the accepted source artifact and destination contract.
- Transform assumptions and lossy mappings are documented.
- Bridge output cannot substitute for missing core acceptance.
