# Core 0.1 Bridge Page Scoring Reference Audit 003-008 Plan

Lane: `C01TEBRIDGESCOREAUD020-G1-VIRAL-001`

Status: `bridge_page_scoring_reference_audit_completed`

## Purpose

Audit whether the `C01TEBRIDGEREM020-G1-VIRAL-001` fresh OCR candidate texts
for pages `003`-`008` have pinned comparison/reference surfaces that can support
a later bounded scoring or promotion decision.

This lane is diagnostic comparison only. It does not authorize fresh OCR
success, bridge removal, acceptance, production assembly, fixture admission, or
source/raw/page-status mutation.

## Scope

- Consume hash-pinned `C01TEBRIDGEREM020-G1-VIRAL-001` report, summary, and
  manifest.
- Consume hash-pinned candidate text files for pages `003`, `004`, `005`,
  `006`, `007`, and `008`.
- Consume exact pinned comparison/reference surfaces for pages `003`-`008`.
- Record diagnostic similarity/token-recall metrics only after candidate hashes
  are verified.
- Classify all reference surfaces as bounded comparison surfaces, not
  independent acceptance truth.

## Out Of Scope

- Pages `001`, `002`, `014`, `019`, and `021+`.
- OCR execution or Tesseract invocation.
- Render execution, PDF parsing, or PDF text-layer extraction.
- Accepted text, semantic-map, source/raw, or page-status mutation.
- Fixture admission, production assembly, promotion, push, or downstream work.

## Result

- All pages `003`-`008` have pinned comparison/reference surfaces.
- Pages `003` and `004` use lower-authority page-complete OCR block text
  comparison surfaces.
- Pages `005`-`008` use bounded page-complete OCR-verified text map comparison
  surfaces.
- No page is promotable in this lane.
- Fresh OCR success pages remain empty.
