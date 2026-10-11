# Render Comparison Plan - RT-G1-VIRAL-RENDER-001

Comparison plan id: `CP-G1-VIRAL-RENDER-001`

Status: `frozen`

Frozen at: 2026-07-17T17:40:00Z

Selected-page predecessor: `SPM-G1-VIRAL-001`

Accepted protocol:

- Revision: `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- File blob: `4d494e83d8d63dd3778a3813b3ee529449cee51a`

Authorized scope:

- Ordinal pages 1-20 only.
- Page-level output identity checks only.
- No visual quality scoring, OCR-support scoring, layout classification, region
  declaration, map creation, QA finding, benchmark conclusion, source-profile
  acceptance, or renderer-parameter acceptance.

Report shape:

- Output manifest with one row per rendered page.
- Each row records page ordinal, selected-page manifest predecessor, render
  candidate ID, output path, output SHA-256, renderer/config predecessor, and
  stale/invalidation status.

Metrics:

- File existence.
- Output SHA-256 identity.
- Image width and height as renderer output metadata.
- No quality or correctness metric is accepted by this plan.

Non-waivable failures:

- Output created for a page outside ordinal pages 1-20.
- Output created without `BA-G1-VIRAL-RENDER-001`.
- Output row missing selected-page manifest, render candidate, comparison plan,
  output path, output hash, renderer/config, or invalidation reference.
- Any OCR, PDF text-layer extraction, map creation, benchmark conclusion, QA,
  fixture creation, source acceptance, translation, proofreading, or
  implementation occurs in the trial.

Invalidation:

- Stale if source path/hash, `SPM-G1-VIRAL-001`, accepted protocol
  revision/blob, bounded authorization, render candidate manifest, renderer
  config, output schema, or user authority changes.
