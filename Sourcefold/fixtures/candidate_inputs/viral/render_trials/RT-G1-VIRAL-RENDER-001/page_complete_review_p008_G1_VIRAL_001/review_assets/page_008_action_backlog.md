# Page 008 Action Backlog

Package: `PCRP-G1-VIRAL-P008-001`

This log separates orchestration/tool work from scripts so the page-complete packet build remains inspectable.

| Order | Actor | Action | Purpose | Output / Boundary |
|---|---|---|---|---|
| 1 | `Codex` | Inspected existing roadmap/docs and P008 provisional map state. | Confirm P008 starts as its own full-page step after P007, before Gate 1. | P008-only plan; no P007/P008 mixing and no acceptance. |
| 2 | `Tool:view_image` | Viewed rendered page_008.png. | Identify text blocks, photo/art anchors, gray boxes, and paragraph/column flow. | Seven review blocks: five text blocks plus portrait and crystal art anchors. |
| 3 | `Codex` | Prepared inline P008 readable profile. | Transcribe visible text, preserve paragraphs, and classify art as anchors. | P008 spans use paragraph/continuation units; art has anchor metadata and zero source text. |
| 4 | `Script:build_page_complete_review.py` | Materialized PCRP-G1-VIRAL-P008-001. | Generate packet/report/summary/manifest, crops, OCR text map, semantic JSON/Markdown, and this backlog. | Review packet only; no page-complete acceptance, Gate 1 acceptance, fixture admission, source/OCR/render/PDF/raw mutation, translation, proofreading, implementation, or push. |
| 5 | `Script:pytest` | Ran focused page-complete review regression tests after P008 build. | Verify P008 profile gating, attachments, semantic map, text map, action backlog, and no acceptance leakage. | tests/test_page_complete_review.py passed: 79 tests. |
| 6 | `Script:pytest` | Ran full Sourcefold test suite after P008 build. | Check P008 did not regress existing Sourcefold page-review and acceptance contracts. | Full suite passed: 305 tests. |
| 7 | `Script:npm` | Ran roadmap validator after P008 docs/roadmap sync. | Verify roadmap graph and documentation checkpoints remain parseable and consistent. | Roadmap validator passed: 122 checkpoints. |
| 8 | `Tool:git` | Ran scoped working-tree diff-check on generated/code/docs files. | Confirm the packet is not entering review with whitespace issues. | Scoped diff-check clean. |
| 9 | `Sol/Terra` | Reviewed the first P008 packet candidate and returned blockers. | Catch review-layer risks before sending the packet as ready. | Blocked on Corrina paragraph continuation modeling and crop geometry for Marco/Corrina/crystal evidence. |
| 10 | `Codex + Script:build_page_complete_review.py` | Returned to build/fix stage and regenerated the P008 packet. | Preserve visible paragraph boundaries and align crop evidence with declared block coverage. | Corrina right column starts as a paragraph, crystal crop is clean art-only, gray-box/text crops include represented text, and Marco top crop excludes the next block. |

## Guardrails

- This backlog is review/process evidence only.
- It creates no page-complete acceptance, whole Gate 1 acceptance, fixture admission, source/OCR/render/PDF/raw mutation, translation, proofreading, implementation, or push.
