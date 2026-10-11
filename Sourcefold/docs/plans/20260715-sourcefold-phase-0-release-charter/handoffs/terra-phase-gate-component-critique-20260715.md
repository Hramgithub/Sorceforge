# Terra Phase/Gate/Component Critique Handoff

Role: `gpt-5.6-terra`
Review kind: architecture critique
Status: completed
Timestamp: 2026-07-15T03:26:04+03:00
Independence: reviewer did not implement or materially design the candidate.

## Recommendation

Block Phase 1 implementation authorization. The OCR-first direction is sound,
but Phase 0 is still a non-frozen architecture candidate. Its hierarchy and key
parameters are not yet enforceable or evidence-backed.

## Blocking Concerns

| Severity | Finding |
|---|---|
| Critical | The hierarchy was narrative, not governed: phases, steps, gates, matrix rows, artifacts, and parameters lacked one authoritative mapping. |
| Critical | `300-DPI, 8-bit sRGB PNG` was premature as a normative profile. DPI alone does not establish OCR adequacy. |
| High | The `Вирал` first-20-page pilot is not available or hash-bound, so no representative-structure or fixed-threshold claim is defensible. |
| High | RPG taxonomy is evidence-dependent but not yet bound to a source/log inventory or gate. |
| High | OCR thresholds are ungrounded without a gold protocol, corpus, sampling, and measurement definitions. |
| High | Waiver semantics conflict: ambiguous reading order must remain non-waivable for 0.1. |

## Evidence-Gated Parameters

- Raster/rendering: DPI, color/bit-depth, renderer/version, antialiasing,
  color management, transparency, crop policy, effective text-size floor.
- Pilot: exact PDF revision/hash, page range, representativeness criteria, and
  mandatory/deferred structures.
- OCR: engine/model, language pack, segmentation/layout mode, preprocessing,
  confidence handling, correction provenance, rerun tolerance.
- Layout: region classes, geometry precision, column/band rules, headers/footers,
  ambiguity criteria.
- Quality: gold-set selection, CER/token definitions, critical-token set,
  thresholds, review coverage, sampling, severity/waiver eligibility.
- Taxonomy: RPG structures, `unclassified_bounded_block` conditions, exclusions.

## Required Phase 0 Output

A hierarchy table plus parameter register that records ID, status, proposed
value/range, evidence source, measurement method, owner, approval gate, and
mutation invalidation.

## Receipt

- Candidate state: non-frozen draft.
- Release verification: not applicable; no candidate manifest, freeze evidence,
  QA package, or immutable revision was presented.
- Declared exclusions: no OCR engine selection, parameter approval, taxonomy
  approval, pilot qualification, implementation, or file mutation performed.
- Severity: 2 critical, 4 high.
- Token use reported by subagent: 15,132.
