# User OCR-First Profile Notes

Status: orchestrator-captured user input

These notes capture user corrections to the first Phase 0 source-profile draft.
They are evidence for revising the release charter, not final accepted
implementation decisions by themselves.

## Captured Corrections

1. Input is always PDF.
2. The first acquisition step should create page screenshots/images.
3. Page screenshots/images are the working visual evidence for OCR, overlay,
   ordering, and review.
4. PDF text layers are often unreliable in real RPG PDFs.
5. OCR should be treated as the primary text acquisition route.
6. PDF text layer may be auxiliary evidence or comparison signal, not the
   primary source of truth.
7. Most PDFs should be expected to contain two-column layout.
8. The source profile must clarify what "two-column supported" means instead
   of assuming simple single-column flow.
9. RPG structures are broader than the first draft list.
10. Structure taxonomy should be informed by prior processed books and should
    not be treated as complete until that evidence pass is done.
11. A small 8-20 page pilot is feasible because many candidate PDFs are small.
12. OCR methodology, tooling, content QA, reading-order QA, overlay QA, and
    review controls are required product work, but should be staged rather than
    hand-waved into a single reconstruct step.

## Immediate Implication

The 0.1 source profile should move from:

```text
constrained born-digital text-layer PDF
```

to:

```text
constrained OCR-first RPG PDF profile
```

where the durable acquisition chain begins:

```text
PDF -> page image set -> OCR candidate text -> reviewed Accepted Source Text
```

## Open Questions

- Which OCR engine/toolchain is allowed for 0.1?
- Should page screenshots be raster images only, or include page geometry JSON?
- What counts as enough evidence to prove two-column reading order?
- Which RPG structures are mandatory for the first pilot?
- Which structures are explicitly excluded from 0.1?
- Which prior processed books should be sampled to build the structure
  taxonomy?
