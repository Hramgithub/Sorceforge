# Today Step Plan - 2026-07-15

Status: completed original daily plan; bounded continuation active under the global Gate 1 roadmap

Purpose: move Phase 0 / Gate 1 from broad planning toward an accepted
Qualification Protocol without processing the `Вирал` candidate PDF.

This document is the working plan for today. It does not replace
`roadmap.yaml`, `phase_gate_component_hierarchy.md`, or
`pre_ocr_mapping_model.md`. It tells the orchestrator what to do next, in what
order, and what durable artifact must exist after each step.

Current cursor as of 2026-07-18: the original 2026-07-15 ten-step daily plan is
complete as the Gate 1 Qualification Protocol bootstrap. Current work is no
longer a new daily plan; it is a bounded continuation inside the global Gate 1
roadmap, using exact `BA-G1-VIRAL-*` authorizations and committed evidence
artifacts.

Latest continuation state: `PGCT-G1-VIRAL-001` is the page-completeness triage
packet after `P004A-G1-VIRAL-004`. Accepted source reconstruction records are
still 13. No page is accepted as complete, whole Gate 1 remains unaccepted, and
fixtures, translation, proofreading, renderer/profile acceptance,
implementation, and push remain pending. The next human decision should choose
which later page-complete review packet to prepare, with pages 002/003 ready,
page 004 held pending a context-only decision, pages 001/005/006 incomplete,
and pages 007-020 parked until later source-reconstruction slices.
The next planned bounded layer is a universal `page_map` readiness pipeline
pilot, not a page-002-only script: page 002 is the first proving case for a
generic readiness builder plus page-specific profiles. The layer is tracked as
roadmap node `gate-01-page-map-readiness-pipeline` and hierarchy subcomponent
`SC-PAGE_MAP_READINESS`. That pilot still must not create page-complete
acceptance, Gate acceptance, fixtures, OCR/render/PDF work, raw artifact
mutation, translation, proofreading, implementation, or push.

## Operating Rules

- Do not render, OCR, map, translate, proofread, or benchmark `Вирал` unless
  the exact Gate 1 Qualification Protocol revision is accepted and a distinct
  bounded authorization explicitly permits the narrow action. The current
  `P002C-G1-VIRAL-002` now uses remediated page-003 crop boxes and a draft
  visual transcription text layer after Bogdan reported crop cut-off; that
  draft is not source-accepted.
- Keep roadmap YAML as planning/control state only.
- Keep future map payloads in dedicated evidence artifacts, not in roadmap YAML.
- Every step must produce a named artifact, checkpoint note, or explicit
  blocker.
- If a step expects a subagent handoff and the handoff is missing, request a
  checkpoint, then restart/resume the narrow step before the orchestrator takes
  over.

## Ten Steps

| Step | Name | Goal | Expected Output | Format | Owner | Status |
|---|---|---|---|---|---|---|
| 1 | Qualification Protocol shell | Create the governing document for Gate 1 qualification. | `gate_01_qualification_protocol.md` with scope, statuses, allowed/not-allowed actions, and evidence table. | Markdown | Orchestrator | confirmed and committed |
| 2 | Gate 1 input package | Define exact inputs Gate 1 may consume before processing. | Input package section covering product boundary, user OCR-first direction, prior evidence, candidate PDF, authority, identity, fixtures. | Markdown table | Orchestrator | confirmed and committed |
| 3 | Authority and states | Define who can mark protocol, permission, decision, evidence, and finding/waiver states. | State authority table aligned with `acceptance_vocabulary.md` and protocol predicates. | Markdown table | Orchestrator + Terra critique | confirmed and committed |
| 4 | Candidate PDF intake rules | Define what may be recorded about `Вирал` before rendering/OCR. | Intake rules for path, already-recorded hash/page-count references only, rights note, selected-page manifest boundary. | Markdown + manifest placeholder rules | Orchestrator + Sol/Terra review | confirmed and committed |
| 5 | Render benchmark protocol | Define how page-image render candidates will be compared. | Candidate dimensions, render candidate manifest, comparison plan, output lineage, and failure behavior. | Markdown table | Sol architecture review + Terra critique | confirmed and committed |
| 6 | Pre-OCR map qualification | Decide how `doc_map`, `content_map`, `art_map`, and `pre_ocr_map_bundle` enter Gate 1. | Map evidence requirements, schema blockers, bundle-freezing authorization, visualization boundary. | Markdown table linked to `SC-MAP` | Sol + Terra | confirmed and committed |
| 7 | OCR benchmark protocol | Define how OCR engine/config candidates will be tested. | Candidate manifest, gold-sample policy, scoring plan, metrics, failure behavior, no PDF text-layer canonical use. | Markdown table | Sol architecture review + Terra critique | confirmed and committed |
| 8 | QA and non-waivable findings | Define content/order/overlay checks before Accepted Source Text. | Findings matrix for omissions, duplicates, ambiguous order, unsupported structures, silent substitutions. | Markdown matrix | Sol architecture review + Terra critique | confirmed and committed |
| 9 | Fixture and acceptance updates | Sync fixtures and acceptance matrix with the protocol. | Updates or explicit backlog rows in `fixture_strategy.md` and `core_0_1_acceptance_matrix.md`. | Markdown diffs | Orchestrator + Sol/Terra review | confirmed and committed |
| 10 | Review and checkpoint | Run validation, collect critique, and decide whether the exact draft revision is ready for user/Sol/Terra review or remains blocked. | Documentation checkpoint, roadmap status update, next-step decision. | Script checkpoint + roadmap YAML | Orchestrator + user decision | accepted_protocol plus first bounded authorization |

## Step Dependencies

```text
1 Protocol shell
  -> 2 Gate 1 input package
  -> 3 Authority and states
  -> 4 Candidate PDF intake rules
  -> 5 Render benchmark protocol
  -> 6 Pre-OCR map qualification
  -> 7 OCR benchmark protocol
  -> 8 QA and non-waivable findings
  -> 9 Fixture and acceptance updates
  -> 10 Review and checkpoint
```

## Today's Stop Conditions

Stop and ask before continuing if:

- the plan would require processing `Вирал`;
- the protocol needs a user authority decision not already recorded;
- Sol and Terra recommendations conflict on the same gate condition;
- roadmap dependencies would become non-linear enough to obscure the main
  chain;
- a proposed step creates implementation work instead of Phase 0 governance.

## Next Action

OpenClaw Step 10 read-only review found blockers: the protocol lacked an
explicit Step 10 section, top-level protocol status was outside its state
namespace, validation/checkpoint criteria were not recorded in Step 10, and
adjacent docs used weaker authorization shorthand. Sol/Terra review then found
remaining roadmap, matrix, and hard-stop-table drift. Those blockers have been
remediated, Step 10 reached `review_ready`, and the user then accepted exact
revision `5ee1760f` / file blob `4d494e83` as `accepted_protocol` for
methodology only. `BA-G1-VIRAL-SPM-001` created `SPM-G1-VIRAL-001`, a
selected-page manifest for ordinal pages 1-20, and is now scope-consumed. Do
not create fixtures, run QA, render, OCR, map, benchmark, translate, proofread,
implement, or create any other candidate-derived artifact.
After separate Sol/Terra read-only review, `BA-G1-VIRAL-RENDER-001` rendered
ordinal pages 1-20 into `RT-G1-VIRAL-RENDER-001` as render trial evidence
only. OCR, map, benchmark, QA, fixture, source acceptance, translation,
proofreading, renderer/profile acceptance, and implementation remain blocked.
`BA-G1-VIRAL-VISUAL-001` then produced `VSR-G1-VIRAL-001` as non-accepting
visual sanity/page-inventory evidence only.
`BA-G1-VIRAL-PAGEINV-001` then produced `PIR-G1-VIRAL-001` as non-accepting
page-level inventory evidence only. It does not create a map, OCR routing
decision, QA result, benchmark, fixture, source evidence, source-profile
acceptance, translation, proofreading, renderer/profile acceptance, or
implementation authorization.
`BA-G1-VIRAL-PAGEMAP-001` then produced `PMR-G1-VIRAL-001` as non-accepting
page-level map/model planning evidence only. It does not create `doc_map`,
`content_map`, `art_map`, `pre_ocr_map_bundle`, region IDs, coordinates,
anchors, reading order, OCR routing, QA, benchmark, source acceptance,
translation, proofreading, renderer/profile acceptance, or implementation
authorization.
`BA-G1-VIRAL-REGIONMAP-001` then produced `PRM-G1-VIRAL-001` as
non-accepting provisional region annotation evidence only. It contains
provisional region IDs and approximate pixel/normalized boxes for pages 1-20,
but does not create accepted anchors, reading order, OCR routing, QA,
benchmark, source acceptance, translation, proofreading, renderer/profile
acceptance, implementation, or a frozen `pre_ocr_map_bundle`.

Step 5 render benchmark protocol was confirmed by Sol/Terra, approved by user
rule, and committed as `15cbe4a2`. Step 6 pre-OCR map qualification was
confirmed by Sol/Terra and committed as `7d98dc66`. Step 7 OCR benchmark
protocol was drafted for review only. Terra returned OK; Sol found two
blockers, the local remediation received renewed Sol/Terra OK under the
user-delegated rule, and Step 7 was committed as `1b30b776`. Step 8 QA and
non-waivable findings was drafted for Sol/Terra review; both reviewers found
blockers, and the local remediation received renewed Sol/Terra OK under the
user-delegated rule, and Step 8 was committed as `c22e4ebb`. Step 9 fixture
and acceptance updates was drafted for Sol/Terra review; both reviewers found
fixture-linkage blockers. Terra confirmed the first remediation, while Sol
found remaining reciprocity and exact-blocker issues. The second remediation
received Sol/Terra OK under the user-delegated rule, and Step 9 was committed
as `7b0c2f41`. Step 10 review/checkpoint is complete for protocol acceptance;
the completed candidate trials are `BA-G1-VIRAL-SPM-001` /
`SPM-G1-VIRAL-001`, `BA-G1-VIRAL-RENDER-001` /
`RT-G1-VIRAL-RENDER-001`, `BA-G1-VIRAL-VISUAL-001` /
`VSR-G1-VIRAL-001`, and `BA-G1-VIRAL-PAGEINV-001` /
`PIR-G1-VIRAL-001`, and `BA-G1-VIRAL-PAGEMAP-001` /
`PMR-G1-VIRAL-001`, and `BA-G1-VIRAL-REGIONMAP-001` /
`PRM-G1-VIRAL-001`, all scope-consumed.
