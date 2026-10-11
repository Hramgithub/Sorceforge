# Sol OCR-First 10-Step Roadmap Handoff

Agent: `gpt-5.6-sol` / architect

Timestamp: 2026-07-15T01:32:35+03:00

Mutations: none

Token use: 30,247 goal tokens

## Result

Sol recommends expanding `reconstruct` into six separately gated steps. OCR is
the primary acquisition path. The PDF text layer becomes comparison-only
evidence and must never be a direct predecessor of `accepted_source_text`.

## Dependency And Lineage Model

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

Optional, non-authoritative branch:

```text
source_pdf -> pdf_text_comparison -> findings only
```

## Ten-Step Roadmap Summary

1. Phase 0: lock the OCR-first release contract.
2. Deterministic PDF intake and page-image evidence.
3. Constrained two-column layout profile and region mapping.
4. OCR methodology and toolchain qualification.
5. Reproducible OCR acquisition.
6. Reading-order reconstruction and QA.
7. Content, structure, and overlay QA; accept source text.
8. Translation and Faithful RU Draft acceptance.
9. Proofreading and Proofread RU Master acceptance.
10. Core 0.1 RC freeze and independent release review.

## Recommended Normative 0.1 Source Profile

- Input must be one immutable, unencrypted PDF.
- Positive pilot should contain 8-20 consecutive selected pages; if the PDF is
  8-20 pages, the whole PDF should be processed.
- Every selected page is rendered with pinned renderer/configuration to a
  lossless 300-DPI, 8-bit sRGB PNG.
- Page images are canonical working visual evidence for reconstruction.
- OCR operates on page images or declared image regions and is primary.
- PDF text layer may be extracted only into a separate comparison artifact.
- PDF text layer must not populate canonical text, determine reading order,
  bypass OCR/image QA, or become a direct predecessor of accepted source text.
- Supported page layout uses ordered vertical bands. Each band is full-width or
  two non-overlapping left/right column regions.
- Bounded sidebars, cards, stat blocks, examples, and callouts must be wholly
  contained in one column or occupy an explicit full-width band with explicit
  order position.
- Unknown RPG structures may be preserved as `unclassified_bounded_block` only
  when complete text, geometry, order, and trace anchors are retained.

Unsupported cases:

- ambiguous interleaved column flow;
- three or more body columns;
- overlapping text flows;
- rotated body text;
- handwriting;
- severe degradation outside the qualified preprocessing boundary;
- complex non-rectangular or nested tables;
- essential semantic text embedded only in maps or diagrams.

## Required Remediation

- Replace text-layer/no-OCR recommendations in the charter.
- Add PDF, page-image, layout, OCR, reading-order, comparison,
  source-candidate, and overlay-QA record types to lineage.
- Add negative fixtures for missing regions, column order, OCR discrepancy,
  overlay failure, unclassified blocks, and text-layer leakage.
- Add a separate executable Core 0.1 acceptance matrix covering Steps 2-10.
- Preserve earlier handoffs as historical evidence, but supersede only their
  source-profile recommendation.

## Release Status

Not reviewed or approved for release. Independent Terra release review remains
mandatory for a future frozen candidate.
