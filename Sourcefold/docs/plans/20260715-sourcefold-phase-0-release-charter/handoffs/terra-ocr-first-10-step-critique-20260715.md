# Terra OCR-First 10-Step Critique Handoff

Agent: `gpt-5.6-terra` / independent critic

Timestamp: 2026-07-15T01:30:26+03:00

Mutations: none

Token use: 25,234

## Receipt

- `review_kind`: architecture
- Candidate: non-frozen OCR-first 0.1 roadmap/Phase 0 charter.
- Independence: Terra did not implement or materially design the candidate.
- Recommendation: block implementation authorization pending the gates below.

## Blocking Concerns

- B0: source-profile contradiction. The earlier charter made text-layer
  extraction primary and deferred OCR; the corrected premise requires PDF
  input, page-image evidence, and OCR-primary reconstruction.
- B1: two-column gap. Multi-column reading order is common and must be a
  bounded supported case with independent reading-order QA.
- B2: missing explicit OCR assurance steps. Raster evidence, OCR methodology,
  content QA, reading-order QA, and overlay QA need separate gates.
- B3: unsupported RPG taxonomy claim. Structure coverage must be grounded in
  prior-book/pilot evidence and must not imply universal coverage.
- B4: sequence not auditable unless each user correction maps to a dedicated
  roadmap step.

## Required Gates Before Implementation

- Lock one immutable PDF pilot, exact page range, profile version, and declared
  representative structures including bounded two-column pages.
- Define page-image evidence contract: raster settings, naming, hashes,
  retention, and PDF-to-page mapping.
- Lock OCR methodology: engine/version, language models, configuration,
  preprocessing policy, correction provenance, and reproducibility record.
- Define reading-order rules and acceptance evidence for one/two-column
  layouts.
- Ground the RPG structure taxonomy in prior-book/pilot evidence.
- Define preservation fallback for unclassified structures.
- Define distinct content QA, reading-order QA, and overlay QA artifacts,
  severity rules, pass criteria, and human authority.
- Bind lineage from PDF to page images to OCR output to reconstructed source to
  translation to proofread master.
- Update the release matrix so each OCR-first claim has a fixture, human check,
  evidence artifact, failure behavior, and blocking severity.

## Release Review Note

No release verification is applicable yet. Future frozen candidates must be
invalidated by any mutation to the PDF, page images, OCR/configuration,
reconstructed source, or predecessor lineage.
