# Sol Step 5 Render Benchmark Review

Verdict: NOT OK

Blocking findings:
- The `image_container` candidate space permits only PNG, TIFF, or another lossless candidate. That silently accepts a lossless-only policy while container choice is still evidence-gated. Remediation: make the candidate dimension neutral across justified container/compression classes, or reference a separately accepted lossless-only evidence policy; do not settle that policy in this draft.
- The future trial contract has one `renderer_identity`, one `render_config`, and an `output_manifest`, but it does not require an immutable per-candidate binding from each output to the exact renderer engine/version/build, complete config, selected-page-manifest entry, and source-page identity. A multi-renderer/config benchmark could therefore produce ambiguous lineage and invalidation. Remediation: require a predeclared `render_candidate_manifest` with stable candidate IDs and require every output-manifest row to bind candidate ID, selected-page entry/source page, output identity/hash, and predecessor IDs.
- The non-waivable rule rejects post-hoc metrics or comparison regions, but the authorization predicate and record contract do not require a separately identified, frozen pre-execution comparison plan. Fields written into the trial record after execution cannot prove they were predeclared. Remediation: require a version/hash-bound `comparison_plan_id` before render authorization and execution, containing authorized pages/regions or page-level checks, metrics, thresholds/scoring, failure rules, and invalidation; bind the authorization, trial, outputs, and report to that plan. Region declaration must rely only on observations separately authorized by the selected-page-manifest action.
- Live labels are not consistent with the required stop state. `roadmap.yaml` has Step 5 `draft-review-needed` but Step 6 `missing`; the protocol and today-plan tables label Step 6 `pending`, and the protocol still labels Step 4 as renewed-review-pending. Remediation: make current control surfaces state Step 5 `draft-review-needed` and Step 6 `blocked` pending accepted Step 5 review/approval, and retire the stale Step 4 label. Historical checkpoints may remain unchanged.

Non-blocking notes:
- The draft correctly limits Step 5 to governance/specification work and explicitly forbids opening, rendering, inspecting, selecting pages from, OCRing, mapping, benchmarking, or otherwise deriving observations from Viral.
- The future-action boundary correctly requires the exact `accepted_protocol`, accepted Step 4 intake rules, a selected-page manifest created under its own authorization, a renderer-identity interface, and a distinct bounded render authorization.
- Renderer, DPI, color, bit-depth, preprocessing, page-box, transparency, rotation, and anti-aliasing are presented as dimensions rather than accepted values. The hidden/clipped/rotated/duplicated/silently dropped-content failure class is correctly non-waivable.

Exact answer:
- No. The Step 5 Render Benchmark Protocol draft is not yet OK to commit, and the orchestrator must not proceed to Step 6, even draft-only, until the four blocking contract/status remediations above receive renewed review. Viral remains fully quarantined; this review authorizes no candidate-derived action and is not a release decision.

Files reviewed:
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/context.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/today_20260715_step_plan.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`
- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/handoffs/sol-step-4-remediation-confirmation-20260715.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/handoffs/terra-step-4-remediation-confirmation-20260715.md`

Verification:
- Scope/result: architecture review of the Step 5 render benchmark draft only; result is NOT OK pending the four listed remediations.
- Changed file: this handoff only.
- Evidence: traced authorization dependencies, candidate dimensions, future record contracts, non-waivable failures, and live labels across the assigned Sourcefold files; scoped `git diff --check` found no whitespace errors, with line-ending warnings only.
- No PDF was touched: I did not open, parse, render, OCR, hash, count pages, inspect, map, or otherwise process the Viral PDF. No candidate-derived metadata or artifact was created.
- Blockers: neutral container policy; unambiguous per-candidate/output lineage; frozen pre-execution comparison-plan identity; consistent Step 5/Step 6 live labels.
- Next action: orchestrator remediates only these Step 5 contract and live-label issues, keeps Step 6 blocked, and requests renewed Sol/Terra review before commit or continuation.
- Elapsed time: approximately 13 minutes at receipt preparation.
- Token use: unavailable; no exact runtime token meter was exposed.
- Timestamp: `2026-07-15T21:11:37.0129614+03:00`.
