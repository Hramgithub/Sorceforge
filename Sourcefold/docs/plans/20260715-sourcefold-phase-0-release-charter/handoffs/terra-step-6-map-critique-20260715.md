# Terra Step 6 Pre-OCR Map Critique

Review kind: process

Candidate state: non-frozen Step 6 draft

Implemented or materially designed candidate: no

Verdict: NOT OK

Blocking findings:

- Severity: blocker. `pre_ocr_mapping_model.md` says “After protocol acceptance” and then describes candidate-derived metadata intake/selected-page-manifest and seed `doc_map` creation, renders, visual annotation, and freezing map revisions. It omits the distinct, exact bounded authorization required by the protocol for each such action. This contradicts `gate_01_qualification_protocol.md`, which requires both the exact `accepted_protocol` revision and a bounded authorization that names the action, inputs, outputs, limits, expiry, and invalidation. The roadmap repeats the weaker “protocol acceptance before any Viral mapping” formulation. This wording could prematurely unlock inspection, mapping, annotation, or evidence creation.

Non-blocking notes:

- The Step 6 section of `gate_01_qualification_protocol.md` is otherwise well controlled: it keeps maps conceptual, forbids payload collection, excludes payloads and region inventories from roadmap YAML, binds later viewer use to canonical artifacts, and marks unauthorized/stale map evidence non-waivable.
- Current live status is consistent that Step 6 is review-pending and Step 7 is blocked. Historical checkpoint entries retain older wording, but they are not the active control state.

Exact answer:

- NOT OK to commit or proceed to Step 7 draft-only. First revise the mapping-model gathering sequence and the roadmap expectation so every candidate-derived intake, manifest, render, inspection, map, annotation, viewer-evidence, or bundle-freezing action requires the exact `accepted_protocol` revision plus its own distinct bounded authorization. Then obtain renewed independent review. Viral remains quarantined.

Files reviewed:

- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/pre_ocr_mapping_model.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/context.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/today_20260715_step_plan.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`
- `Sourcefold/PROJECT_STATUS.md`

Verification:

- No Viral PDF was touched, opened, parsed, rendered, OCRed, hashed, counted, inspected, mapped, annotated, or otherwise processed.
- No schema, map artifact, payload, region inventory, viewer evidence, or implementation artifact was created. This handoff is the only file written.

Evidence:

- Protocol Step 6 requires exact `accepted_protocol` plus distinct bounded map-qualification authorization, and separately prohibits payload collection in the draft.
- The mapping-model “Proposed Gathering Sequence” weakens that dual predicate to protocol acceptance alone; roadmap map-node wording has the same omission.

Recommendation: remediate the dual-authorization wording before committing; keep Step 7 draft-only blocked until renewed Sol/Terra review returns OK.

Elapsed time: 707 seconds

Token use: 98,120

Timestamp: 2026-07-15T18:37:45.959Z
