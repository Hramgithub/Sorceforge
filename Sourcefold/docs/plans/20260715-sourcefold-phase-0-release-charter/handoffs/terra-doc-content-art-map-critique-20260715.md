# Terra Doc/Content/Art Map Critique Handoff

Role: `gpt-5.6-terra`
Review kind: independent architecture critique
Status: completed
Timestamp: 2026-07-15T19:18:04+03:00
Independence: reviewer did not implement or materially design the candidate.

## Recommendation

Do not approve implementation of full pre-OCR `doc_map/content_map/art_map` as
initially proposed. Consider only a tightly limited, non-semantic intake or
page-image coverage record after Qualification Protocol approval.

## Findings

- High: pre-OCR maps derived from `Вирал` before an accepted Qualification
  Protocol would violate candidate quarantine.
- High: semantic labels in `content_map` or `art_map` could be mistaken for
  source truth before OCR, layout, reading-order QA, and trace anchors exist.
- High: semantic content/art mapping risks drifting into Knowledge Base or
  press concerns, both outside Core 0.1.
- Medium: map artifacts depend on unresolved canonical format, identity,
  acceptance authority, and trace-anchor contracts.
- Medium: `doc_map`, `content_map`, and `art_map` need controlled meanings to
  avoid becoming a parallel taxonomy.

## Required Sequencing

- Before protocol acceptance: no `Вирал`-derived maps.
- After protocol acceptance and candidate intake: a non-semantic,
  source-bound page/intake inventory may be evidence-gated.
- After render/OCR/layout/order qualification: content-oriented maps may be
  evaluated as derived evidence tied to accepted anchors.
- Art subject/style semantics should be parked outside Core 0.1 unless
  separately chartered.

## Minimum Acceptance Criteria

- Qualification Protocol explicitly permits map collection.
- Hash-bound candidate, rights attestation, selected-page manifest, and pilot
  scope exist.
- Each map type has declared purpose, scope, exclusions, vocabulary, owner,
  approver, evidence requirements, failure behavior, and invalidation.
- Canonical format, identity, lineage, and trace-anchor dependencies are
  resolved or parked.
- Positive and negative fixtures prove unsupported/ambiguous/non-text material
  is parked or rejected without false source claims.
- No map acceptance unlocks Core 0.1 outside existing Gate 1 roll-up rules.
