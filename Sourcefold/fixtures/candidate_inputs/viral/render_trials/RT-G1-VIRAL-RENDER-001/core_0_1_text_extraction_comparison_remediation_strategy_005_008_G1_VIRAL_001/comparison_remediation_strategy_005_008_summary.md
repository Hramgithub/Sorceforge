# C01TEP005008REMSTRAT-G1-VIRAL-001 Summary

Status: `comparison_only_remediation_strategy_recorded_no_execution`

This lane records a comparison-only remediation strategy for pages `005`-`008`.
It consumes committed `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` from commit
`50d4abac` by exact declared output hashes and treats committed
`C01TEP003004COMPSTRAT-G1-VIRAL-001` from commit `6b336843` as an adjacent
boundary for pages `003`/`004`, not as part of this page scope.

It does not execute remediation, scoring, OCR/Tesseract, render execution, PDF
parsing, accepted/source/raw/semantic/page-status mutation, replacement
reference writes, bridge removal, promotion, fixture admission, production
assembly, page `021+`, push, or downstream execution.

## Strategy

Pages `005`-`008` keep the route
`remediation_strategy_required_comparison_only`. Their OCR-verified text-map
surfaces may support future bounded diagnostic comparison, but they remain
comparison-only evidence and do not become independent acceptance truth or
promotion authority in this lane.

| Page | Existing similarity | Existing token recall | Future strategy focus |
|---|---:|---:|---|
| `005` | `0.175287` | `0.765` | sequence/order repair, missing tokens, line or column order drift |
| `006` | `0.060631` | `0.766892` | large sequence gap, missing tokens, layout order failure |
| `007` | `0.081666` | `0.801047` | article continuation order, paragraph boundary flattening |
| `008` | `0.20165` | `0.879518` | residual missing tokens, noise or order drift |

Future remediation families are limited to separately authorized work over
existing candidate-policy inputs: full-page-region geometry variants, column
and lane-order reassembly, paragraph/line-join reassembly, candidate-floor
guarded noise suppression, and separately authorized PSM profile selection. No
future lane may insert reference tokens into candidates.

## Future Contract

- Normalize with NFKC, LF line endings, trimmed line edges, collapsed repeated
  whitespace, and preserved paragraph breaks.
- Preserve case and punctuation sensitivity.
- Seal candidate and reference hashes before any future scoring.
- Use `sequence_similarity_ratio` and `token_recall`.
- Future threshold policy: existing Core 0.1 baseline thresholds,
  `sequence_similarity_ratio >= 0.997` and `token_recall >= 0.993`, unless a
  later Sol/Terra gate changes them.
- Treat future comparison scores as diagnostic quality evidence only until a
  separate fresh-success decision is reviewed.

## Boundary

No remediation execution or scoring is authorized by this packet. Any future
execution, scoring, fresh OCR success decision, bridge removal, runtime selector
refresh, production assembly, acceptance, or promotion requires a separate
reviewed authorization.
