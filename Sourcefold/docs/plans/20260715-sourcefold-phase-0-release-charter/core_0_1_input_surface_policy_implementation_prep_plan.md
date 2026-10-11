# Core 0.1 Input Surface Policy Implementation Prep Plan

Status: `implemented_static_replay_validated`

Lane id: `C01TEISP-G1-VIRAL-001`

## Objective

Prepare a bounded Core 0.1 implementation slice that universalizes the
P017/P018 lesson without turning `full_page_region` into a blanket policy.
The slice must make OCR input surfaces explicit, route weak OCR outcomes by
diagnosis, and keep acceptance boundaries separate from candidate evidence.

## Scope

In scope:

- Define an `ocr_input_surface` contract for every Core 0.1 OCR run.
- Separate human-review crops, text-evidence crops, OCR-candidate crops, and
  full-page-derived regions.
- Define a router contract that starts with the frozen baseline profile when
  allowed, then routes P017/P018-like failures to full-page-derived geometry or
  another explicitly authorized OCR-safe surface.
- Add a mandatory result-evaluation step using both sequence similarity and
  token recall, compared with the observed P018 full-page geometry measurement:
  similarity `0.999466` and token recall `0.996067`. This comparison is
  diagnostic only; it must not become an automatic pass/fail, promotion, or
  acceptance threshold.
- Define failure behavior for partial candidate/hash/scoring artifacts.
- Prepare tests over existing evidence classes: P009/P010/P015 as baseline
  controls and P017/P018 as full-page-geometry controls.

Out of scope:

- New OCR execution.
- Rendering, PDF parsing, or PDF text-layer extraction.
- Page `021+`.
- Accepted text mutation.
- Semantic-map or page-status mutation.
- Source/profile/page-complete acceptance.
- Runtime implementation/start/execution beyond contract/code scaffolding.
- Translation/proofreading.
- Push.

## Implementation Boundary

The implementation slice that follows this plan is limited to schema/model,
router-decision logic, scorer report fields, and tests using static fixtures.
It must not invoke Tesseract, render pages, parse PDFs, read PDF text layers,
or write OCR artifacts outside test temporary directories. Runtime integration
requires a future bounded authorization naming exact files, commands, inputs,
outputs, and invalidation behavior.

## Proposed Contract

Each OCR attempt must declare an `ocr_input_surface` object:

| Field | Requirement |
|---|---|
| `surface_class` | One of `review_crop`, `text_evidence_crop`, `ocr_candidate_crop`, `full_page_region`. Unknown classes fail closed as `blocked_unsafe_surface`. |
| `artifact_role` | Human-review, text-evidence, OCR-candidate, or full-page-region role binding. |
| `ocr_allowed` | `false` by default for `review_crop` and `text_evidence_crop`; `true` only for explicitly authorized OCR-safe surfaces. |
| `source_artifact` | Hash-bound full-page image or crop artifact path. |
| `page_id` | Stable page id such as `P018`. |
| `regions` | Page-space geometry and prepared-region artifact paths. |
| `preprocessing_profile` | Named preprocessing tuple. |
| `ocr_engine_profile` | OCR engine, version/config, PSM/OEM. |
| `allowed_purpose` | `smoke_non_promotable`, `remediation`, `candidate_policy`, or `candidate_scoring_evidence`. `acceptance_evidence` is reserved for a future separate acceptance authority and is rejected in this lane. |
| `reference_policy` | Whether references are scorer-only, reference-risk, or prohibited. |
| `failure_behavior` | Partial artifacts are quarantined/incomplete/stale and cannot be scored or accepted without a new run id/hash manifest or explicit invalidation. |
| `authorization` | Required for `full_page_region`: bounded authorization id, page family, region policy, and negative reason why baseline routing is insufficient. |
| `observed_control_measurement` | Optional diagnostic comparison object; for this lane it records P018 `full_page_expanded_overlap_psm4`, similarity `0.999466`, token recall `0.996067`, and the `C01TEFG017018-G1-VIRAL-001` manifest hash `A754D100659FA7900677C7BBAF49ACC06F991A8E8C2A02DECE59506EF8C6DAC0`. |

## Router Design

1. Apply the surface eligibility gate before scoring. `review_crop` and
   `text_evidence_crop` are blocked unless explicitly marked
   `smoke_non_promotable`; smoke outputs cannot be promoted or used for
   candidate-policy review.
2. Try the baseline lane only when the input surface is explicitly allowed as
   `ocr_candidate_crop`.
3. Score baseline output with sequence similarity and token recall.
4. If the baseline reaches existing OK-level control thresholds, currently
   similarity `>= 0.997` and token recall `>= 0.993`, keep the result as
   candidate-only evidence and stop.
5. If token recall is high while sequence similarity is weak, inspect
   diagnostics for geometry/order failure signals. The committed static router
   keeps baseline OK at similarity `>= 0.997` and token recall `>= 0.993`,
   but uses a separate geometry-diagnosis floor of token recall `>= 0.97`
   when weak sequence and geometry/order flags are present:
   edge artifacts, column-order drift, text near crop boundaries, clipped
   review crops, or role-derived human-review assets.
6. Route geometry-like failures to a `full_page_region` candidate family only
   when a bounded `full_page_region_authorization_id`, `page_family`,
   `region_policy`, and `negative_reason_not_baseline` are present. Otherwise
   return `blocked_unsafe_surface` or `geometry_probe_required`.
7. Seal candidate text and hashes before reference scoring.
8. Score every candidate with both sequence similarity and token recall.
9. Compare best candidates to the P018 observed control measurement:
   similarity `0.999466` and token recall `0.996067`. The report must include
   `similarity_delta`, `token_recall_delta`, `structure_order_assessment`, and
   `completeness_assessment`. Numeric comparison to P018 must not auto-pass,
   auto-fail, promote, park, or accept a policy.
10. Produce a route decision: `baseline_ok`, `geometry_probe_required`,
   `candidate_policy_ready_for_review`, `park_candidate_policy`, or
   `blocked_incomplete_artifacts`. Unsafe or unauthorized inputs return
   `blocked_unsafe_surface`.

## Candidate Families

- `trim_mask_psm4`: existing baseline for suitable OCR-candidate crops.
- `expanded_overlap_columns_psm4`: full-page-derived two-column tight pages,
  observed in P018 candidate-only evidence.
- `bright_title_body_psm7_4_4`: full-page-derived title/body split pages,
  observed in P017 candidate-only evidence.
- Future families: table, card/sidebar, mixed art/text, and unknown block
  fallbacks.

## Test Plan

- P009/P010/P015: baseline controls should remain baseline-routed and must not
  require full-page geometry by default.
- P017/P018: complex/tight controls should route to full-page geometry when
  crop-derived results show high-recall / low-sequence-similarity failure.
- P009/P010/P015 negative controls must not auto-route to full-page geometry
  merely because a baseline candidate is imperfect.
- Unknown `surface_class` fails as `blocked_unsafe_surface`.
- Missing or hash-mismatched `source_artifact` fails closed.
- `review_crop` and `text_evidence_crop` cannot be promoted from
  `smoke_non_promotable`.
- `full_page_region` without a bounded authorization id, page family, region
  policy, and baseline-negative reason fails closed.
- Page `021+` fixtures fail closed.
- Attempts to invoke an OCR engine, render pages, parse PDFs, or write
  non-temp OCR artifacts fail the implementation-boundary tests.
- Partial artifact fixture: candidate text/hash exists but scoring/report is
  incomplete; route must be `blocked_incomplete_artifacts`.
- Reference policy fixture: references may be loaded only after candidate text
  hashes are sealed.
- Acceptance boundary fixture: even `0.999+` candidate metrics do not create
  source/profile/page-status/page-complete acceptance.
- P018 measurement fixture: candidates above or below P018 `0.999466` /
  `0.996067` do not auto-pass, auto-fail, promote, park, or accept; they only
  produce diagnostic deltas and assessments.

## Implementation Outline

- Added `scripts/ocr_input_surface_policy.py` with the static
  `ocr_input_surface` contract, route decisions, observed control measurement
  deltas, and fail-closed validation.
- Added `tests/test_ocr_input_surface_policy.py` with focused controls for
  P009/P010/P015 baseline routing, P017/P018 geometry routing, unsafe surface
  rejection, missing/hash-mismatched source artifacts, forbidden
  `acceptance_evidence`, reference-before-hash rejection, page `021+`
  rejection, partial artifacts, implementation-boundary no-execution behavior,
  and static 001-020 replay.
- Committed as `6507f386` and tuned in `a01da448`.

## Static Replay Result

The 001-020 replay consumes existing saved overview metrics only; it does not
run OCR, render pages, parse PDFs, write OCR artifacts, or mutate accepted
source/status material.

| Pages | Route |
|---|---|
| `001`-`008` | `not_run_ineligible` |
| `009`, `010`, `011`, `015` | `baseline_ok` |
| `012`, `013`, `016`, `017`, `018`, `020` | `geometry_probe_required` |
| `014`, `019` | `park_candidate_policy` |

The replay changed the design detail from a single high-recall geometry gate to
two thresholds: baseline OK remains similarity `>= 0.997` plus token recall
`>= 0.993`; geometry diagnosis may trigger at token recall `>= 0.97` when weak
sequence and geometry/order flags are present.

## Review Questions

1. Does the `ocr_input_surface` contract prevent review crops from silently
   becoming OCR-safe inputs?
2. Does the observed P018 measurement (`0.999466` similarity / `0.996067`
   token recall) stay diagnostic rather than becoming a hidden hard threshold?
3. Are the added fail-closed fixtures enough for the first router-contract
   tests?
4. Are failure behavior and quarantine rules strong enough for partial artifacts?
5. Is the implementation boundary narrow enough to avoid OCR/runtime execution,
   source/profile acceptance, and policy promotion?

## Next Step

Sol and Terra reviewed the draft before implementation. The accepted fixes are
folded into this plan and the first static implementation slice is complete.

Recommended next plan:

1. Add a bounded geometry-probe execution-prep lane for pages routed
   `geometry_probe_required`, starting with `012`, `013`, `016`, `017`, `018`,
   and `020`.
2. Keep `014` and `019` parked until a lower-recall failure family is named;
   do not force them into the P017/P018-like geometry route.
3. Define exact inputs, outputs, run ids, invalidation rules, and hash
   manifests for a future full-page-derived geometry probe.
4. Run Sol/Terra on that execution-prep scope before any OCR/runtime command.
5. Only after static authorization, execute a small probe batch and evaluate
   results against both sequence similarity and token recall with P018
   `0.999466` / `0.996067` as diagnostic control, not acceptance.
