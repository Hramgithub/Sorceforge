# C01TEP003004COMPSTRAT-G1-VIRAL-001 Summary

Status: `comparison_scoring_prep_strategy_recorded_no_execution`

This lane records a comparison/scoring-prep strategy only for pages `003` and
`004`. It consumes committed `C01TEP003004AUTHUP-G1-VIRAL-001` from commit
`de58ee23` by exact declared output hashes. It does not execute scoring, run
OCR/Tesseract, perform remediation, write replacement reference surfaces, mutate
accepted/source/raw/semantic/page-status state, remove bridge lineage, promote
pages, assemble production, include page `021+`, push, or trigger downstream
execution.

## Strategy

A separately authorized future bounded scoring lane may compare the existing
bridge remediation candidate texts for pages `003`/`004` against the nominated
source-accepted/page-complete-backed comparison inputs. Those inputs remain
future bounded comparison inputs only; they do not become acceptance,
promotion, fresh-success, bridge-removal, or production authority in this lane.

| Page | Candidate input | Future reference assembly order |
|---|---|---|
| `003` | existing `page_003_full_page_psm6_candidate.md` | `SRSA-G1-VIRAL-003-R01 -> SRSA-G1-VIRAL-003-R02` |
| `004` | existing `page_004_full_page_psm6_candidate.md` | `SRSA-G1-VIRAL-004-R01 -> SRSA-G1-VIRAL-004-R02` |

For page `004`, `PRM-G1-VIRAL-001-P004-R01` remains context-only and excluded
from future text-reference assembly.

## Future Contract

- Normalize with NFKC, LF line endings, trimmed line edges, collapsed repeated
  whitespace, and preserved paragraph breaks.
- Preserve case and punctuation sensitivity.
- Use `sequence_similarity_ratio` and `token_recall`.
- Future threshold policy: existing Core 0.1 baseline thresholds,
  `sequence_similarity_ratio >= 0.997` and `token_recall >= 0.993`, unless a
  later Sol/Terra gate changes them.
- Bucket discrepancies as OCR noise/garbage, missing reference token, extra
  candidate token, order drift, case/punctuation drift, context-only leakage,
  or unsafe reference dependency.

## Boundary

No scoring execution or remediation is authorized by this packet. Any future
scoring or remediation requires a separate reviewed authorization and must not
infer fresh OCR success, promotion, bridge removal, acceptance, or production
from this strategy alone.
