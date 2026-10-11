# Gate 1 Qualification Protocol

Status: `accepted_protocol`; exact revision accepted for methodology only; candidate-derived actions require distinct bounded authorization records

Goal id: `20260715-sourcefold-phase-0-release-charter`

Roadmap node: `gate-01-qualification-protocol`

## Purpose

This protocol defines how Gate 1 may qualify the first Sourcefold Core 0.1
source profile before any candidate PDF is processed.

It is a methodological control document. It does not accept the `Вирал`
candidate PDF, does not authorize rendering/OCR/mapping/benchmark work, and
does not approve Core 0.1 implementation.

## Review Boundary

Step 1 shell review is not protocol acceptance.

Sol and Terra reviewed the Step 1 shell and returned `accept with required
revisions`. That verdict means the shell is a usable planning container only.
It does not accept the protocol, accept any parameter, waive any finding,
authorize any candidate interaction, or unlock Step 3 as resolved work.

Operational work requires two later records: an accepted protocol revision and
a separate bounded trial authorization record that names the exact action,
admitted inputs, allowed outputs, limits, authority, expiry, and invalidation
behavior.

## Current Scope

In scope:

- Gate 1 input package rules;
- qualification statuses and authority boundaries;
- candidate PDF intake rules before processing;
- render benchmark protocol;
- pre-OCR `doc_map`, `content_map`, `art_map`, and bundle qualification;
- OCR benchmark protocol;
- QA and non-waivable finding classes;
- fixture and acceptance-matrix updates;
- review and checkpoint rules.

Out of scope:

- rendering, OCR, mapping, translation, proofreading, or benchmarking of
  `Вирал`;
- accepting `Вирал` as a fixture;
- locking renderer, DPI, image format, OCR engine/config, thresholds, or map
  schema as final values;
- implementing `reconstruct`, `translate`, `proofread`, `press`, or `bridge`.

## Hard Stops

The following actions remain blocked until the relevant predicate below is met.
Review alone is never sufficient.

| Action | Current State | Required Before Action | Named Output Evidence | Invalidation Rule |
|---|---|---|---|---|
| Create selected-page manifest from `Вирал` | completed by `SPM-G1-VIRAL-001`; authorization `BA-G1-VIRAL-SPM-001` scope consumed | exact `accepted_protocol` revision, accepted Step 4 intake rule, accepted or version-bound provisional identity interface, accepted selection policy, and distinct bounded authorization naming manifest creation as the exact action | `selected_page_manifest` | source path/hash, selection policy, manifest schema, protocol revision, or authorization changes stale the manifest |
| Render `Вирал` pages | completed by `RT-G1-VIRAL-RENDER-001`; authorization `BA-G1-VIRAL-RENDER-001` scope consumed | exact `accepted_protocol` revision, accepted render benchmark protocol, selected-page manifest, renderer identity rule, and distinct bounded render authorization naming rendering as the exact action | `page_image_set` trial evidence | source, selected pages, renderer/config, DPI/color/container, or preprocessing changes stale render evidence |
| Benchmark render candidates | blocked | exact `accepted_protocol` revision, render benchmark protocol, comparison regions, metrics, failure behavior, and distinct bounded render-benchmark authorization naming benchmark execution as the exact action | `render_benchmark_report` | benchmark input, metric, threshold, or renderer/config changes stale the report |
| Create `doc_map`, `content_map`, or `art_map` from `Вирал` | blocked | exact `accepted_protocol` revision, map qualification rules, source/page identity model, allowed annotation procedure, and distinct bounded map authorization naming map creation as the exact action | `pre_ocr_map_bundle` trial evidence | source/page identity, schema, annotation rules, or map tool changes stale map evidence |
| OCR `Вирал` pages | blocked | exact `accepted_protocol` revision, OCR benchmark protocol, approved render trial evidence, gold-sample policy, and distinct bounded OCR authorization naming OCR as the exact action | `ocr_trial_output` | render evidence, OCR engine/model/config, or gold policy changes stale OCR evidence |
| Benchmark OCR candidates | blocked | exact `accepted_protocol` revision, OCR benchmark protocol, gold samples, metrics, failure behavior, and distinct bounded OCR-benchmark authorization naming benchmark execution as the exact action | `ocr_benchmark_report` | OCR input/config, metric, threshold, or gold sample changes stale the report |
| Accept Source Profile parameters | blocked | exact `accepted_protocol` revision, accepted evidence records, authority assignment, roll-up proof, blocker closure, and no required descendant left unresolved | source-profile decision record | any predecessor evidence or authority change stales affected parameter decisions |

Candidate quarantine is absolute until both predicates are true for the exact
candidate-derived action: the exact protocol revision is `accepted_protocol`,
and a distinct bounded authorization names that action, inputs, outputs,
limits, expiry, and invalidation behavior. The protocol may cite already
recorded candidate path/hash/status, but must not open, parse, re-count,
re-hash, render, OCR, map, inspect, or derive any new candidate metadata from
the PDF.

## OCR Input Surface Policy

OCR evidence must name its input surface class before execution:

- `review_crop`: a human-review or text-evidence crop prepared for inspection
  and page-review traceability.
- `text_evidence_crop`: a review-package crop with text-evidence role; it is
  not OCR-safe by default.
- `ocr_candidate_crop`: a crop explicitly authorized as an OCR input surface.
- `full_page_region`: a region derived from the immutable full-page render in
  page-space coordinates.

Review crops are not automatically OCR-safe. They may be used for bounded smoke
tests only when the authorization names that limitation. For complex/tight pages
matching the P017/P018 evidence class, poor sequence similarity with high token
support is a geometry warning, not permission to repair from reference text.
For P017/P018-like pages, independent routes must use full-page-derived
regions, or another separately authorized OCR-safe geometry, before any
source/profile/page-status acceptance. `C01TEFG017018-G1-VIRAL-001` remains
candidate-only until a separate promote-or-park decision.

Reference-guided repair is a separate support-evidence class. It may compare
OCR support against reference text maps marked
`reference_text_map_not_ocr_verified`, but it must not be reported as
independent OCR validation, source-profile acceptance, accepted source text,
page-status mutation, page-complete acceptance, or runtime source-profile lock.

Independent geometry probes must persist candidate text and hashes before
loading reference text for scoring. Reference maps may be used for scoring only
after candidate generation is sealed.

If a geometry probe writes candidate text or hash artifacts but fails before a
complete scoring/report manifest is produced, those artifacts remain
quarantined candidate-only evidence. They must be marked incomplete or stale,
must not be scored or accepted, and any rerun must use a new run id/hash
manifest or an explicit invalidation record.

`C01TEISP-G1-VIRAL-001` is now implemented as a static contract/router slice
in commits `6507f386` and `a01da448`. It consumes declared surface metadata and
saved score summaries only. It may return `baseline_ok`,
`geometry_probe_required`, `candidate_policy_ready_for_review`,
`park_candidate_policy`, `blocked_unsafe_surface`, or
`blocked_incomplete_artifacts`, but those decisions do not execute OCR, mutate
accepted text/status, promote `C01TEFG017018`, park `C01TEFG017018`, or create
source/profile/page-status/page-complete acceptance.

## Control State Model

State names are separated by purpose. They must not be collapsed into one
generic `qualification state`.

### Protocol Status

| State | Meaning | Unlocks |
|---|---|---|
| `draft_shell` | Container exists, not reviewed. | drafting only |
| `reviewed_revisions_required` | Shell reviewed and found usable with required revisions. | revision work only |
| `draft_protocol` | Protocol sections are drafted but not accepted. | review preparation only |
| `review_ready` | Draft is ready for user/Sol/Terra review. | review only |
| `accepted_protocol` | Exact protocol revision/hash is accepted. | may support bounded authorization records |
| `superseded_protocol` | Newer protocol revision replaces this one. | no new work |

### Permission Status

| State | Meaning | Unlocks |
|---|---|---|
| `prohibited` | Action is blocked by default. | nothing |
| `draft_request` | A proposed bounded action exists, not reviewed. | nothing |
| `review_pending` | A bounded action request is under review. | nothing |
| `authorized_trial` | Exact action/input/output/limits are approved by authority. | only the named trial |
| `expired` | Authorization reached its expiry or scope limit. | nothing |
| `revoked` | Authorization was cancelled or invalidated. | nothing |

### Decision Status

| State | Meaning | Unlocks |
|---|---|---|
| `captured` | Candidate value recorded for discussion. | nothing |
| `proposed` | Candidate value is proposed, not evidence-proven. | nothing |
| `evidence_gated` | Evidence is required before decision. | nothing |
| `pending_approval` | Evidence exists but authority has not accepted it. | nothing |
| `accepted` | Exact value is accepted for the stated scope. | only declared dependents |
| `parked` | Explicitly out of current scope. | may unblock dependents that do not need it |
| `rejected` | Not permitted in current scope. | nothing |
| `superseded` | Replaced by a newer decision. | nothing |

### Evidence Status

| State | Meaning | Unlocks |
|---|---|---|
| `missing` | Required evidence does not exist. | nothing |
| `draft` | Evidence exists but is not reviewed. | nothing |
| `valid_for_review` | Evidence can be reviewed under current identity/lineage rules. | review only |
| `accepted_evidence` | Evidence is accepted for a named criterion. | may support a decision |
| `stale` | Evidence invalidated by changed predecessor/config/schema. | nothing |
| `rejected_evidence` | Evidence failed a criterion or identity rule. | nothing |

### Finding And Waiver Status

| State | Meaning | Unlocks |
|---|---|---|
| `open_finding` | Finding is unresolved. | nothing |
| `resolved_finding` | Finding is closed by fix, evidence, or rejection. | may support review |
| `waiver_requested` | Waiver proposed but not accepted. | nothing |
| `accepted_waiver` | Waiver accepted under an accepted waiver policy. | only the named finding if eligible |
| `non_waivable` | Finding class cannot be waived for Core 0.1. | nothing |

No waiver may authorize a Gate 1 action until the waiver policy is accepted.
Identity mismatch, unauthorized candidate interaction, missing lineage, stale
evidence, and open blocking findings are non-waivable control failures for this
protocol draft.

## Transition Rules

| Transition | Requirement |
|---|---|
| `draft_shell -> reviewed_revisions_required` | Sol/Terra review handoffs exist and are recorded. |
| `reviewed_revisions_required -> draft_protocol` | Required revisions are applied and checkpointed. |
| `draft_protocol -> review_ready` | Steps 2-10 have explicit sections or blockers, validation has passed, and Step 10 records a next-step decision. |
| `review_ready -> accepted_protocol` | User accepts an exact protocol revision/hash after review; no trial-produced evidence is required for this transition. |
| `prohibited -> authorized_trial` | Accepted protocol, named action record, user authority, accepted intake/interface prerequisites, exact inputs/outputs/limits, expiry, and invalidation rules. |
| any evidence state -> `stale` | Any predecessor identity, tool/config, schema, metric, threshold, or authority rule changes. |

## Evidence Package Skeleton

Every Gate 1 qualification record should carry:

| Field | Requirement |
|---|---|
| `record_id` | Stable ID for the qualification record. |
| `record_version` | Monotonic version or revision label for this exact record. |
| `record_hash` | Content hash after canonicalization rules exist; `pending-canonicalization` until then. |
| `roadmap_node` | Related roadmap node, usually `gate-01-qualification-protocol` or a child decision node. |
| `hierarchy_ref` | Exact Gate/component/subcomponent/parameter ID from `phase_gate_component_hierarchy.md`. |
| `criterion_id` | One criterion per result; use multiple records rather than ambiguous arrays. |
| `input_artifacts` | Exact artifact IDs, paths, types, schema versions, and hashes for evidence used. |
| `predecessor_ids` | Parent records/artifacts whose mutation stales this record. |
| `authorized_action_id` | Required if the record was produced by any bounded trial. |
| `tool_identity` | Tool, version, model/config, environment, and command profile when a tool is involved. |
| `measurement_method` | How the observation was produced or reviewed. |
| `observed_result` | Measured or reviewed result tied to the criterion. |
| `protocol_status` | Protocol state namespace value, when relevant. |
| `permission_status` | Permission state namespace value, when relevant. |
| `decision_status` | Decision state namespace value, when relevant. |
| `evidence_status` | Evidence state namespace value, when relevant. |
| `finding_waiver_status` | Finding/waiver state namespace value, when relevant. |
| `actor` | Who produced the record. |
| `accepted_by` | Required for accepted protocol, accepted decision, accepted evidence, parked/rejected decisions, or accepted waiver. |
| `timestamp` | Creation and decision timestamp. |
| `invalidation_rules` | What changes make this evidence stale and how staleness propagates. |
| `findings` | Open/resolved findings linked to evidence. |
| `waiver_refs` | Waiver records, if and only if an accepted waiver policy allows them. |
| `supersedes` | Prior record IDs superseded by this record. |

## Acceptance And Authorization Predicates

These predicates are intentionally separate to avoid cyclic dependencies.

### Protocol Acceptance Predicate

The protocol may become `accepted_protocol` only when:

- Steps 2-10 have explicit sections or explicit blockers.
- The authority model for accepting the protocol revision is named.
- Canonical format, artifact identity, trace-anchor, and waiver interfaces are
  either accepted or explicitly version-bound as provisional interfaces for the
  first bounded trial.
- The protocol defines the bounded trial authorization template.
- Sol/Terra review evidence is recorded for the exact revision under review.
- The user accepts the exact protocol revision/hash.

Protocol acceptance must not require trial-produced render/OCR/map evidence,
resolved evidence-gated source-profile parameters, accepted candidate evidence,
or Gate 1/source-profile acceptance.

### Bounded Trial Authorization Predicate

A candidate-derived action may move from `prohibited` to `authorized_trial`
only when:

- the protocol is `accepted_protocol`;
- the relevant intake/interface prerequisites for that action are accepted or
  version-bound as provisional;
- the authorization names exactly one action, admitted inputs, allowed outputs,
  limits, expiry, authority, and invalidation behavior;
- the action can produce only the named evidence artifacts;
- candidate quarantine exceptions are limited to that exact authorization.

### Gate 1 / Source Profile Acceptance Predicate

Gate 1/source-profile acceptance is later than protocol acceptance and later
than bounded trial evidence. It requires:

- required Gate 1 descendants are `accepted`, validly `parked`, or `rejected`
  with accepted failure behavior;
- required evidence is `accepted_evidence` and not `stale`;
- open blocking findings are resolved or rejected;
- waiver use, if any, is allowed by an accepted waiver policy;
- roll-up proof shows no required child remains `captured`, `proposed`,
  `evidence_gated`, `pending_approval`, or blocked without accepted parking.

Completion of a drafting step is not acceptance of the protocol. Only an exact
protocol revision/hash plus user acceptance can move this document to
`accepted_protocol`.

## Gate 1 Input Package

Gate 1 may reason only from the following input package. Anything outside this
package is either ignored or must be added through a later checkpoint.

| Input | Current Artifact | Status | Allowed Use | Not Allowed |
|---|---|---|---|---|
| Product boundary | `product_boundary.md`, `PROJECT_STATUS.md`, Sourcefold `AGENTS.md` | available | constrain Core/optional/future scope | expand Core 0.1 beyond `reconstruct -> translate -> proofread` |
| NRI governance | `../docs/governance/nri_goal_governance.md`, Sourcefold `AGENTS.md` | available | enforce goal, handoff, checkpoint, and watchdog rules | replace Sourcefold governance with Translator precedent |
| User OCR-first direction | `user_ocr_profile_notes.md`, `context.md`, roadmap comments | captured | shape questions for the first source-profile candidate | lock renderer/OCR/config/thresholds without evidence |
| Phase 0 decision drafts | `release_charter.md`, `acceptance_vocabulary.md`, `artifact_lineage_model.md`, `fixture_strategy.md`, `release_acceptance_matrix.md` | draft | identify decisions that Gate 1 must satisfy | treat draft decisions as accepted values |
| Gate hierarchy | `phase_gate_component_hierarchy.md` | draft governed model | provide subcomponent/parameter IDs and roll-up rules | skip parameter-level evidence |
| Today plan | `today_20260715_step_plan.md` | completed original ten-step bootstrap; retained as historical cursor for bounded continuation | document the completed Gate 1 protocol bootstrap and point continuation work back to the global Gate 1 roadmap | override roadmap, accepted protocol text, or bounded authorizations |
| Pre-OCR mapping model | `pre_ocr_mapping_model.md` | draft proposal | define map-related questions and blockers | authorize map collection from `Вирал` |
| Prior-work evidence | `prior_work_evidence_index.md` and recorded Sol handoffs | draft evidence index | inform taxonomy and risk expectations | substitute for `Вирал` qualification evidence |
| Step 1 review handoffs | Sol and Terra Step 1 handoffs | recorded | constrain revisions and blocker state | serve as protocol acceptance |
| Candidate PDF | `fixtures/candidate_inputs/viral/Call_of_Cthulhu_Viral.pdf` plus candidate README/hash | present-unqualified | prove a durable candidate exists through already recorded references only | open, inspect, re-hash, count pages, render, OCR, map, benchmark, or accept it |
| Roadmap state | `docs/roadmap/roadmap.yaml` and viewer | active planning control | show dependencies, status, blockers, linked plans | store map payloads or evidence payloads |

## Input Admission Rules

An input may enter Gate 1 only if it has:

| Requirement | Rule |
|---|---|
| Stable path | The artifact path is durable inside `Sourcefold/` or an explicitly named NRI governance path. |
| Role | The artifact says whether it is governance, draft decision, evidence, candidate input, handoff, or status. |
| Status | The artifact has a current state such as `available`, `draft`, `present-unqualified`, `active`, or `accepted`. |
| Scope boundary | The artifact states what it can and cannot authorize. |
| Traceability | The artifact can be referenced from roadmap, plan/context, or parameter records. |
| Invalidation trigger | The artifact says what kind of change makes dependent decisions stale, or it is marked as pending that rule. |
| Authorization boundary | The artifact says whether it can inform planning, support review, or authorize a bounded action. Draft artifacts authorize planning only. |

## Candidate PDF Boundary

The `Вирал` PDF is part of the Gate 1 input package only as a quarantined
candidate input. Before the exact protocol revision is `accepted_protocol` and
a bounded trial authorization names the exact candidate-derived action, the
protocol may refer to its committed location and previously recorded hash, but
must not derive any new metadata or artifact from it.

Allowed before exact protocol acceptance plus bounded authorization:

- cite the candidate path;
- cite the already recorded candidate hash from existing status/context;
- state that the candidate exists and is unqualified;
- define what future intake evidence must contain.

Blocked before exact protocol acceptance plus bounded authorization:

- opening the PDF for any reason;
- parsing PDF metadata;
- re-hashing or re-counting the PDF;
- opening the PDF for page/content inspection;
- rendering pages;
- creating screenshots/images;
- extracting or comparing text;
- creating selected-page manifests;
- creating `doc_map`, `content_map`, or `art_map` records.

## Step 2 Result

The Gate 1 input package is now drafted as a control list. It permits planning
and protocol writing only. Operational work remains blocked until later
sections define authority, candidate intake, render benchmark, map
qualification, OCR benchmark, and QA rules. This Step 2 draft has been revised
to preserve candidate quarantine and identity/authorization boundaries, but it
still requires user/orchestrator review before it can be treated as resolved.

## Authority And States

Status: confirmed and committed.

This section assigns draft authorities to the separate state namespaces above.
It does not accept the protocol, authorize candidate work, accept Gate 1, or
change the `Вирал` quarantine.

### Authority Roles

| Role | Scope |
|---|---|
| `orchestrator` | Drafts protocol text, integrates reviews, records checkpoints, and blocks unsafe transitions. |
| `user` | Accepts protocol revisions, scope-expanding decisions, bounded trial authorization, and any final Gate 1/source-profile acceptance. |
| `sol_architect` | Reviews architecture, dependency graph, evidence interfaces, and deadlock/cycle risks. |
| `terra_critic` | Reviews premature unlocks, missing blockers, waiver risks, and release/process safety. |
| `validator` | Marks machine-checkable schema/contract results as conformant/nonconformant when validators exist. |
| `tool_runner` | Produces tool/run observations only after bounded trial authorization exists. |
| `stage_reviewer` | Reviews evidence and findings for a named stage after evidence exists. |

### Protocol Status Authority

| State | May Set | Required Evidence | Notes |
|---|---|---|---|
| `draft_shell` | orchestrator | created protocol shell | drafting only |
| `reviewed_revisions_required` | orchestrator after Sol/Terra handoffs | review receipts | cannot unlock Step 3 as accepted work |
| `draft_protocol` | orchestrator | applied revisions and checkpoint | drafting/review prep only |
| `review_ready` | orchestrator | Steps 2-10 drafted or explicitly blocked; validation passed | review only |
| `accepted_protocol` | user | exact protocol revision/hash, Sol/Terra review, accepted/provisional interfaces | may support bounded trial requests |
| `superseded_protocol` | orchestrator or user | successor revision/hash | no new work from superseded revision |

### Permission Status Authority

| State | May Set | Required Evidence | Notes |
|---|---|---|---|
| `prohibited` | default/system rule | protocol default-deny policy | starting state for all candidate-derived actions |
| `draft_request` | orchestrator | proposed action/input/output/limit/invalidation envelope | no work authorized |
| `review_pending` | orchestrator | request routed for user/Sol/Terra review as needed | no work authorized |
| `authorized_trial` | user | accepted protocol, accepted/provisional interfaces, exact bounded action record | only named trial may run |
| `expired` | orchestrator or validator | expiry/limit reached | no further work |
| `revoked` | user or orchestrator for safety | invalidation, scope breach, or user stop | no further work |

### Decision Status Authority

| State | May Set | Required Evidence | Notes |
|---|---|---|---|
| `captured` | orchestrator | user note, handoff, or source document reference | discussion only |
| `proposed` | orchestrator or Sol | rationale and affected parameter IDs | not accepted |
| `evidence_gated` | orchestrator, Sol, or Terra | named evidence needed | blocks dependent acceptance |
| `pending_approval` | orchestrator | evidence exists and review package is ready | user decision still required |
| `accepted` | user | accepted evidence, no blocking findings, exact scope | only declared dependents may consume |
| `parked` | user for required items; orchestrator only for proven non-required items | rationale, dependency impact, and roll-up eligibility | cannot hide required blockers |
| `rejected` | user for required items; orchestrator only for invalid non-required proposals | rationale, failure behavior, and dependency impact | may close impossible non-required branch |
| `superseded` | orchestrator | successor decision ID | historical only |

### Evidence Status Authority

| State | May Set | Required Evidence | Notes |
|---|---|---|---|
| `missing` | orchestrator or validator | expected artifact absent | blocks dependent review |
| `draft` | orchestrator or tool_runner | artifact exists, not reviewed | no acceptance effect |
| `valid_for_review` | validator or orchestrator | identity/lineage fields present and not stale | review only |
| `accepted_evidence` | stage_reviewer or user as named | criterion/result record, current lineage, closed blockers | may support decision acceptance |
| `stale` | validator, orchestrator, or stage_reviewer | predecessor/config/schema/authority changed | cannot be consumed |
| `rejected_evidence` | stage_reviewer or validator | failed criterion or identity rule | cannot support acceptance |

### Finding And Waiver Authority

| State | May Set | Required Evidence | Notes |
|---|---|---|---|
| `open_finding` | stage_reviewer, validator, or orchestrator | finding record with severity and affected artifact/criterion | blocks if severity requires |
| `resolved_finding` | stage_reviewer or validator | fix, rejection, or accepted evidence | may support review |
| `waiver_requested` | orchestrator or stage_reviewer | request with scope/rationale/evidence | no unlock |
| `accepted_waiver` | user or named waiver authority after policy acceptance | accepted waiver policy, eligible severity, exact finding | only named finding if eligible |
| `non_waivable` | protocol, user, or Terra critic | policy/control rule | cannot be waived |

### Step 3 Draft Rules

- A draft authority assignment never overrides default-deny candidate
  quarantine.
- `accepted_protocol`, `authorized_trial`, `accepted`, `accepted_evidence`, and
  `accepted_waiver` require explicit evidence records; chat text alone is not
  sufficient.
- The user may delegate a narrow authority later, but delegation must be
  recorded with scope, expiry, and affected state namespace.
- Sol/Terra review may recommend or block transitions but does not replace user
  acceptance where user authority is required.
- If authority conflicts, the safer/lower-unlock state wins until the conflict
  is resolved.
- Any `parked` or `rejected` transition that changes required scope, exit-gate
  coverage, or Gate 1/source-profile roll-up eligibility requires an explicit
  user decision record. The orchestrator may only propose that transition.
- `stage_reviewer` authority must be recorded with actor, stage, state
  namespace, scope, expiry, and participation constraints before that role may
  accept/reject evidence or resolve findings.

## Step 3 Result

Authority/state rules were confirmed by Sol/Terra and committed. They do not
accept the protocol and do not authorize any candidate-derived action. The
current safe action is renewed review of the remediated Step 5 render benchmark
rules.

## Candidate PDF Intake Rules

Status: confirmed and committed as `e98bfdd1`.

This section defines what a future candidate PDF intake record must contain.
It does not authorize opening, parsing, re-hashing, page counting, rendering,
OCR, mapping, metadata extraction, selected-page manifest creation, or any
other candidate-derived action.

### Intake Boundary

Candidate intake is a control record, not PDF processing. Until the protocol is
accepted and a bounded trial authorization names an exact intake action, the
only allowed references to the `Вирал` candidate remain the already recorded
path/hash/status in existing committed artifacts.

| Intake Question | Draft Rule |
|---|---|
| What is admitted? | One candidate source PDF path already committed under `fixtures/candidate_inputs/viral/`. |
| What is not admitted? | Page images, OCR output, metadata dumps, page counts, page manifests, maps, screenshots, or derived text. |
| Can intake verify the PDF now? | No. Verification is a future bounded action. |
| Can intake create a selected-page manifest now? | No. Manifest creation is a separate future action requiring the exact `accepted_protocol` revision and a distinct bounded authorization for selected-page manifest creation. |
| Can intake compare or inspect PDF contents? | No. Comparison/inspection is candidate-derived work. |
| Can intake cite existing records? | Yes, only existing path/hash/status already recorded before this Step 4 draft. |

### Future Intake Record Requirement Matrix

When authorized later, a candidate intake record should carry only fields
permitted by the exact authorization. Conditional fields use explicit absent
states and must never trigger implicit observation work.

| Field | Cardinality | Source/Authority | Allowed Absent State |
|---|---|---|---|
| `intake_record_id` | mandatory | record creator under bounded authorization | none |
| `protocol_revision` | mandatory | exact `accepted_protocol` revision/hash | none |
| `authorization_id` | mandatory | exact bounded trial authorization ID | none |
| `candidate_path` | mandatory | already recorded candidate path under `fixtures/candidate_inputs/viral/` | none |
| `source_pdf_artifact_id` | mandatory when identity interface is accepted; provisional otherwise | accepted identity rules or version-bound provisional identity interface | `provisional_identity_pending` |
| `provisional_candidate_id` | conditional | version-bound provisional identity interface | `not_required` |
| `content_hash` | conditional | only if the authorization explicitly permits hashing | `not_authorized` or `not_observed` |
| `hash_algorithm` | conditional | accepted hash rule or version-bound provisional hash interface | `not_authorized` or `not_required` |
| `observed_page_count` | conditional | only if the authorization explicitly permits page counting | `not_authorized` or `not_observed` |
| `rights_attestation` | conditional | operator/user attestation if required by authorization | `not_required` |
| `permission_status` | mandatory, non-unlocking | authorization ledger | `prohibited`, `authorized_trial`, `expired`, or `revoked` |
| `evidence_status` | mandatory, non-unlocking | validator/orchestrator evidence namespace | `missing`, `draft`, `valid_for_review`, `accepted_evidence`, `stale`, or `rejected_evidence` |
| `decision_status` | mandatory, non-unlocking | decision namespace | `proposed`, `pending_approval`, `accepted`, `parked`, `rejected`, or `superseded` |
| `allowed_next_actions` | mandatory | bounded authorization record | defaults to none; cannot grant permission by itself |
| `invalidation_rules` | mandatory | bounded authorization record | none |
| `created_by` | mandatory | actor who executed the authorized intake action | none |
| `created_at` | mandatory | timestamp of authorized intake record creation | none |

`permission_status`, `evidence_status`, and `decision_status` are separate
namespaces. No value in an intake record can unlock a later action unless that
later action also has the exact `accepted_protocol` revision and its own
bounded authorization.

### Intake Authorization Preconditions

Before any intake action can be authorized:

- protocol status is `accepted_protocol` for the exact revision;
- Step 4 intake rules are accepted for the exact protocol revision;
- artifact identity/hash interfaces are accepted or version-bound provisional
  with named version, scope, and expiry;
- the user approves the exact bounded intake action;
- the action names permitted observations, outputs, limits, expiry, and
  invalidation behavior;
- the action explicitly states whether hashing, page counting, or rights
  attestation is permitted.
- selected-page manifest creation is not part of candidate intake unless it is
  named as a distinct bounded action with its own authorization.

### Non-Waivable Intake Failures

The following failures cannot be waived in this draft:

- candidate file path is outside the admitted candidate-input location;
- candidate file was modified without a new intake authorization;
- intake action exceeds its permitted observations;
- any PDF opening/parsing/hash/page-count operation occurs before authorization;
- intake record lacks protocol revision or authorization ID;
- intake record hash or identity conflicts with accepted or version-bound
  provisional identity/hash rules;
- a selected-page manifest is created without the exact `accepted_protocol`
  revision and a distinct bounded selected-page-manifest authorization.

## Step 4 Result

Candidate PDF intake rules were remediated after Sol review, confirmed by
renewed Sol/Terra review, approved under the user-delegated approval rule, and
committed as `e98bfdd1 Draft Gate 1 candidate intake rules`. No intake action
is authorized. The `Вирал` candidate remains quarantined, and Step 5 remains
draft-only until it receives its own review and approval.

## Render Benchmark Protocol

Status: confirmed and committed as `15cbe4a2`.

This section defines what future render benchmark rules must compare before
Sourcefold accepts page-image parameters. It does not authorize opening,
rendering, screenshotting, page selection, page-image creation, image
inspection, OCR, mapping, or benchmark execution for `Вирал` or any other
candidate PDF.

### Render Benchmark Boundary

Render benchmarking is a future bounded trial. Step 5 may define candidate
dimensions, metrics, and failure classes without candidate-derived evidence.
Any future render trial requires:

- exact `accepted_protocol` revision;
- accepted Step 4 candidate intake rules and any required intake record;
- selected-page manifest created under its own distinct bounded authorization;
- accepted or version-bound provisional renderer identity interface;
- frozen `render_candidate_manifest` with stable candidate IDs before
  execution;
- frozen `comparison_plan_id` before render authorization and execution;
- distinct bounded render-benchmark authorization naming inputs, outputs,
  limits, comparison plan, candidate manifest, expiry, authority, and
  invalidation behavior.

### Render Candidate Dimensions

No value in this table is accepted by this draft. The table names dimensions
that a future benchmark protocol must either compare, justify as irrelevant, or
park by explicit decision.

| Dimension | Candidate Space To Define Later | Why It Matters |
|---|---|---|
| `renderer_engine` | Poppler, MuPDF, Acrobat/export, or another pinned renderer | reading order/overlay evidence depends on reproducible page images |
| `renderer_version` | exact executable/library version and build/source | renderer upgrades can alter glyphs, transparency, and crop behavior |
| `page_box` | media/crop/bleed/trim/art box handling | wrong box can hide margins, captions, or full-page art |
| `resolution_dpi` | evidence-tested DPI ladder, not a preselected value | small glyphs, tables, maps, and captions may require more than one DPI |
| `color_space` | grayscale, RGB, or other justified mode | art overlays, colored rules, and contrast can affect QA and OCR |
| `bit_depth` | 8-bit, 16-bit, or renderer-native choice | low depth can lose faint text or subtle overlays |
| `image_container` | justified container and compression classes, with lossless-only policy accepted only by separate evidence decision | compression/container affects reproducibility, file size, QA, and downstream OCR |
| `alpha_transparency` | preserve, flatten to background, or reject | transparent overlays can create missing/ghosted content |
| `rotation_orientation` | honor PDF rotation, normalize, or record both | wrong orientation breaks map/region anchors |
| `anti_aliasing` | renderer default, disabled, or pinned settings | glyph edge quality changes OCR and visual QA |
| `preprocessing_policy` | none, crop, deskew, denoise, contrast, split columns, or prohibited | preprocessing can improve OCR but can also change evidence |
| `render_candidate_manifest` | stable candidate IDs binding renderer, version/build, complete config, and invalidation rules | benchmark outputs must be unambiguous across renderer/config variants |
| `comparison_plan` | pre-execution plan identity, metrics, regions/checks, thresholds/scoring, failure rules, and invalidation | benchmark criteria must not be chosen after seeing output |
| `output_identity` | page-image IDs, hashes, candidate IDs, selected-page entries, source-page identity, predecessor IDs | page images must be traceable and invalidatable |

### Future Render Candidate Manifest

Before a render benchmark can be authorized, a frozen
`render_candidate_manifest` must exist. It must be version/hash-bound and must
assign a stable candidate ID to every renderer/config variant under test.

Each candidate row must bind:

- `render_candidate_id`;
- renderer engine, exact version, build/source, and executable/library
  identity;
- complete render config for every candidate dimension under test;
- selected-page-manifest dependency;
- source-page identity dependency;
- permitted output container/compression policy;
- invalidation rules for renderer, config, selected pages, source identity,
  and comparison plan changes.

### Future Comparison Plan

Before a render benchmark can be authorized or executed, a frozen
`comparison_plan_id` must exist. It must be version/hash-bound and must define
the allowed comparison without relying on observations from unauthorized page
inspection.

The plan must include:

- selected-page manifest reference;
- authorized pages, page-level checks, or region IDs;
- the separately authorized observation source for any region declaration;
- visual and OCR-support metrics;
- thresholds or scoring method;
- non-waivable failure rules;
- report shape and invalidation rules.

Region declaration must rely only on observations separately authorized by the
selected-page-manifest action. If no region observation is authorized, the plan
may use page-level checks only.

### Required Future Render Trial Record

When authorized later, a render trial record must carry:

| Field | Requirement |
|---|---|
| `render_trial_id` | stable ID for the bounded render trial |
| `protocol_revision` | exact `accepted_protocol` revision/hash |
| `authorization_id` | distinct bounded render-benchmark authorization |
| `source_intake_record_id` | accepted/current candidate intake record if required |
| `selected_page_manifest_id` | current selected-page manifest created by its own authorization |
| `render_candidate_manifest_id` | frozen manifest binding stable candidate IDs to renderer identity and full configs |
| `comparison_plan_id` | frozen pre-execution comparison plan bound to authorization and trial |
| `renderer_identity` | accepted or version-bound provisional renderer identity for each candidate |
| `render_config` | full config for every candidate dimension under test, referenced through candidate IDs |
| `output_manifest` | one row per output binding exact `comparison_plan_id`, render candidate ID, selected-page entry, source-page identity, page-image ID/path/hash when hashing is authorized, and predecessor IDs |
| `comparison_regions` | declared visual regions or page-level checks from the frozen comparison plan |
| `metrics` | visual/OCR-support metrics from the frozen comparison plan |
| `findings` | missing text/art, clipping, overlays, transparency, rotation, or reproducibility failures |
| `invalidation_rules` | what changes stale the trial evidence |

### Non-Waivable Render Benchmark Failures

The following failures cannot be waived in this draft:

- render trial occurs without exact `accepted_protocol` plus bounded render
  authorization;
- selected-page manifest is missing, stale, or not created under its own
  authorization;
- `render_candidate_manifest` is missing, stale, not frozen before execution,
  or lacks stable candidate IDs;
- `comparison_plan_id` is missing, stale, not frozen before render
  authorization/execution, or is not bound to the trial/report;
- renderer identity or render config is not recorded;
- output manifest rows do not bind exact `comparison_plan_id`, render
  candidate ID, selected-page entry, source-page identity, output identity/hash
  when authorized, and predecessor IDs, or they bind a mismatched comparison
  plan;
- preprocessing changes page content without a recorded policy and finding;
- output hides, clips, rotates, duplicates, or silently drops visible source
  content;
- benchmark metrics or comparison regions are selected after seeing the trial
  output.

## Step 5 Result

Render benchmark protocol rules were remediated after Sol review, confirmed by
renewed Sol/Terra review, and committed as
`15cbe4a2 Draft Gate 1 render benchmark protocol`. No render trial, page
selection, image output, OCR, map, benchmark, or candidate-derived observation
is authorized. The next safe action is Step 6 pre-OCR map qualification
drafting.

## Pre-OCR Map Qualification

Status: confirmed and committed as `7d98dc66`.

This section defines how `doc_map`, `content_map`, `art_map`, and
`pre_ocr_map_bundle` may qualify as future Gate 1 evidence. It does not
authorize opening, rendering, screenshotting, page selection, page-image
creation, image inspection, OCR, mapping, annotation, benchmark execution, or
any candidate-derived observation for `Вирал` or any other candidate PDF.

### Map Qualification Boundary

Pre-OCR maps are future reconnaissance evidence. Step 6 may define map layers,
required schemas, identity contracts, review states, and visualization
boundaries without collecting any map payload.

Any future map collection, annotation, or map qualification trial requires:

- exact `accepted_protocol` revision;
- accepted Step 4 candidate intake rules and any required intake record;
- selected-page manifest created under its own distinct bounded authorization;
- accepted Step 5 render benchmark protocol and any required current render
  evidence;
- accepted or version-bound provisional map schema and identity interfaces;
- a distinct map-collection/annotation authorization separate from intake,
  selected-page-manifest creation, rendering, map-bundle freezing, OCR, and
  bundle consumption;
- distinct bounded map-qualification authorization naming inputs, outputs,
  limits, page/region observation rules, tool identity, reviewer authority,
  expiry, and invalidation behavior.
- a distinct map-bundle-freezing authorization before creating or updating
  `pre_ocr_map_bundle`; collection/annotation authorization cannot freeze the
  bundle.

### Map Layer Contracts

The three map projections share one page/region identity layer. They must not
be independent inventories that can drift apart.

| Layer | Draft Qualification Role | Must Reference | Must Not Contain |
|---|---|---|---|
| `doc_map` | page-level roles, selected-page identity, and region registry | source candidate, selected-page manifest, page IDs, region IDs, map purpose | OCR text, accepted source text, translation text |
| `content_map` | text-bearing or structurally meaningful region candidates | `doc_map.region_id`, page IDs, structure taxonomy, review status | OCR transcription, trusted semantic RPG roles, translated content |
| `art_map` | visual/mixed/art regions and text interaction candidates | `doc_map.region_id`, page IDs, art taxonomy, anchor candidates | press placement decisions, generated crops, semantic art interpretation unless separately chartered |
| `pre_ocr_map_bundle` | frozen revision bundle for Gate 1 evidence | exact map revisions, schema versions, hashes when authorized, predecessor IDs | unresolved independent map versions or payloads outside canonical artifacts |

### Required Future Map Bundle Record

When authorized later, a map qualification record must extend the mandatory
Evidence Package Skeleton and carry:

| Field | Requirement |
|---|---|
| `map_qualification_id` | stable ID for the bounded map qualification trial |
| `protocol_revision` | exact `accepted_protocol` revision/hash |
| `authorization_id` | distinct bounded map-qualification authorization |
| `source_pdf_artifact_id` | exact candidate source identity from accepted or version-bound provisional identity rules |
| `source_intake_record_id` | current intake record if required by the map authorization |
| `selected_page_manifest_id` | current selected-page manifest created by its own authorization |
| `page_image_set_id` | current render evidence if map collection is render-bound |
| `map_schema_set_id` | accepted or version-bound provisional schema set for all map layers |
| `shared_identity_model_id` | page/region identity, coordinate, and anchor model |
| `doc_map_id` | exact `doc_map` revision, schema version, hash when authorized, and predecessor IDs |
| `content_map_id` | exact `content_map` revision, schema version, hash when authorized, and predecessor IDs |
| `art_map_id` | exact `art_map` revision, schema version, hash when authorized, and predecessor IDs |
| `pre_ocr_map_bundle_id` | exact bundle revision binding all map layers, schemas, hashes when authorized, and predecessor IDs |
| `bundle_freezing_authorization_id` | distinct bounded authorization that created or updated the bundle, or `not_created` when no bundle is produced |
| `tool_identity` | tool name/version/config if any automated proposal or visualization-assisted review is used |
| `actor_and_reviewer` | actor, reviewer authority, review scope, and participation constraints |
| `created_at` | timestamp of map record creation |
| `reviewed_at` | timestamp of review or explicit `not_reviewed` absent state |
| `review_matrix` | human/tool review states and unresolved unknown/mixed regions |
| `visualization_policy` | whether a viewer may display map payloads and from which canonical artifacts |
| `supersession_of` | predecessor map qualification IDs or `none` |
| `invalidation_rules` | what changes stale map evidence or dependent decisions |

The map record plus the inherited Evidence Package Skeleton must close the
evidence DAG. Changes to source identity, intake record, selected-page
manifest, render evidence, schema set, shared identity model, map tool/config,
review authority, authorization, or any predecessor map revision stale the
affected map bundle unless an explicit supersession record replaces it.

### Map Review States

Map records must separate observation state from acceptance state:

| State Field | Allowed Values | Meaning |
|---|---|---|
| `observation_state` | `unobserved`, `observed`, `inferred`, `reviewed`, `resolved` | confidence in the region/page observation |
| `classification_state` | `candidate`, `ambiguous`, `mixed`, `unsupported`, `accepted_for_trial`, `rejected_for_trial` | whether the label can support a bounded trial |
| `evidence_status` | standard evidence namespace | whether the artifact can support review/decision |

No map state can accept source text, approve OCR output, or authorize a later
trial without a separate bounded authorization.

### Visualization Boundary

Roadmap YAML may store only map status, blockers, links, and comments. It must
not store map payloads, coordinates, extracted text, image crops, or region
inventories.

A future map viewer may visualize page/region data only from canonical map
artifacts and only after a bounded action authorizes the relevant artifacts.
Viewer screenshots are not canonical evidence unless separately admitted by an
accepted artifact-identity rule.

### Non-Waivable Map Qualification Failures

The following failures cannot be waived in this draft:

- map collection or annotation occurs without exact `accepted_protocol` plus
  bounded map-qualification authorization;
- selected-page manifest creation, render evidence creation, map collection,
  annotation, map bundle freezing, and OCR/map consumption are combined into
  one implicit protocol-acceptance action or one collection/annotation
  authorization instead of separate bounded authorizations;
- map payload is stored in roadmap YAML or status rollups;
- `doc_map`, `content_map`, and `art_map` use incompatible page/region
  identity models;
- map record omits source/intake identity, predecessor IDs, schema versions,
  map revision/hash data when hashing is authorized, tool/actor/reviewer
  provenance, timestamps, supersession, or invalidation rules;
- region coordinates lack coordinate space, page identity, or render/source
  dependency;
- OCR text, PDF text-layer text, or translated text is placed in pre-OCR map
  payloads;
- art crops, press placement, or generated visual assets are treated as source
  art evidence without separate authorization;
- unknown, mixed, overlapped, or unsupported regions are silently coerced into
  supported categories;
- map evidence is consumed after schema, selected-page manifest, render
  evidence, identity model, or authorization changes make it stale.

## Step 6 Result

Pre-OCR map qualification rules were remediated after Sol/Terra review,
confirmed by renewed Sol/Terra review, and committed as
`7d98dc66 Draft Gate 1 pre-OCR map qualification`. No map collection,
annotation, page-image use, OCR, render, benchmark, bundle freezing, or
candidate-derived observation is authorized. The next safe action is Step 7 OCR
benchmark protocol drafting.

## OCR Benchmark Protocol

Status: confirmed and committed.

This section defines how future OCR candidates may be benchmarked before
Sourcefold accepts OCR engine/config parameters. It does not authorize OCR
execution, PDF text-layer extraction, page-image inspection, gold-sample
creation, text comparison, map consumption, or any candidate-derived
observation for `Вирал` or any other candidate PDF.

### OCR Benchmark Boundary

OCR benchmarking is a future bounded trial. Step 7 may define candidate
dimensions, gold-sample policy, metrics, and failure behavior without
candidate-derived evidence.

Any future OCR trial requires:

- exact `accepted_protocol` revision;
- accepted Step 4 candidate intake rules and any required intake record;
- current selected-page manifest created under its own distinct bounded
  authorization;
- current render evidence created under its own distinct bounded authorization;
- current map evidence only if separately admitted by its own bounded
  authorization;
- accepted or version-bound provisional OCR engine/config identity interface;
- frozen OCR candidate manifest before execution;
- frozen gold-sample and scoring plan before execution;
- distinct bounded OCR-benchmark authorization naming inputs, outputs, limits,
  gold samples, metrics, expiry, authority, and invalidation behavior.

PDF text-layer content/order is not canonical source text and must not populate
gold samples, OCR output, map evidence, accepted source evidence,
`output_manifest`, `ocr_benchmark_report`, findings payloads, persisted
comparison evidence, or any other output artifact. It may be used only by a
separately authorized comparison operation under a later accepted policy. Such
a policy may persist only derived metrics/findings that carry explicit
text-layer provenance and non-canonical status; it must not persist or copy
text-layer content/order payloads.

### OCR Candidate Dimensions

No value in this table is accepted by this draft. The table names dimensions
that a future benchmark protocol must either compare, justify as irrelevant, or
park by explicit decision.

| Dimension | Candidate Space To Define Later | Why It Matters |
|---|---|---|
| `ocr_engine` | OCR engine/service identity and version | output quality and reproducibility depend on engine/model |
| `ocr_model` | language/model/version or service profile | mixed RPG pages may need model-specific handling |
| `language_profile` | English-only, multilingual, domain dictionary, or other justified profile | wrong language/profile can distort names, tables, and terminology |
| `page_input` | accepted page-image evidence and selected-page entries | OCR inputs must be traceable to render evidence |
| `region_input` | page-level, region-level, column-level, or map-guided input | reading order and structured content depend on input granularity |
| `preprocessing_policy` | none, inherited render preprocessing, OCR-specific preprocessing, or prohibited | preprocessing can improve OCR but can alter evidence |
| `layout_mode` | plain text, layout blocks, hOCR/ALTO/JSON, table-aware, or other structured output | reconstruct needs structure and order, not just text |
| `dictionary_terms` | none, candidate glossary, scenario glossary, or prohibited | dictionaries can help names but may introduce false corrections |
| `output_format` | structured OCR observations, text blocks, confidence data, and coordinates | downstream QA needs lineage, confidence, and anchors |
| `confidence_policy` | engine confidence, reviewer confidence, or unsupported | low confidence drives review/finding behavior |

### Future OCR Candidate Manifest

Before an OCR benchmark can be authorized, a frozen
`ocr_candidate_manifest` must exist. It must be version/hash-bound and must
assign a stable candidate ID to every OCR engine/config variant under test.

Each candidate row must bind:

- `ocr_candidate_id`;
- OCR engine/service, exact version/model/profile, and executable/API identity;
- complete OCR config for every candidate dimension under test;
- accepted page-image input references;
- optional map evidence references only if separately authorized;
- output format/schema;
- invalidation rules for engine, model, config, render input, map input, and
  scoring plan changes.

### Future Gold-Sample And Scoring Plan

Before an OCR benchmark can be authorized or executed, a frozen
`ocr_scoring_plan_id` must exist. It must be version/hash-bound and must define
gold samples, metrics, scoring, and failure behavior before seeing OCR output.

The plan must include:

- selected-page manifest and page-image input references;
- authorized page, region, or block IDs;
- gold-sample source and reviewer authority;
- permitted transcription/editing procedure for gold samples;
- metrics for character accuracy, word accuracy, reading order, table/list
  structure, headings, emphasis, page markers, and structured RPG blocks where
  applicable;
- thresholds or scoring method;
- non-waivable failure rules;
- report shape and invalidation rules.

Gold samples must be created only by a distinct bounded authorization. They
must never be populated from PDF text-layer content, OCR output under test, or
translation/proofreading artifacts.

### Required Future OCR Trial Record

When authorized later, an OCR trial record must carry:

| Field | Requirement |
|---|---|
| `ocr_trial_id` | stable ID for the bounded OCR trial |
| `protocol_revision` | exact `accepted_protocol` revision/hash |
| `authorization_id` | distinct bounded OCR-benchmark authorization |
| `source_intake_record_id` | accepted/current candidate intake record if required |
| `selected_page_manifest_id` | current selected-page manifest |
| `page_image_set_id` | current render evidence used as OCR input |
| `pre_ocr_map_bundle_id` | current map bundle only if separately authorized for OCR use |
| `ocr_candidate_manifest_id` | exact revision/hash of the frozen manifest binding OCR candidate IDs to engine/config variants |
| `ocr_scoring_plan_id` | exact revision/hash of the frozen gold-sample/scoring plan |
| `gold_sample_manifest_id` | exact gold-sample manifest revision/hash, sample IDs, predecessor IDs, creation authorization, actor/reviewer, and invalidation rules |
| `gold_sample_creation_authorization_id` | distinct bounded authorization that created or revised the gold samples |
| `map_consumption_authorization_id` | distinct bounded map-consumption authorization, or explicit `not_used` |
| `output_manifest` | one row per output binding OCR candidate ID, OCR candidate manifest revision/hash, scoring plan revision/hash, gold-sample manifest revision/hash, map-consumption authorization or `not_used`, input page/region/block ID, output identity/hash when authorized, and predecessor IDs |
| `findings` | accuracy, order, structure, omission, hallucination, substitution, table/list, and unsupported-region failures |
| `invalidation_rules` | what changes stale OCR trial evidence |

The trial and every output row must stale deterministically when source intake,
selected-page manifest, render evidence, map evidence, map-consumption
authorization, gold-sample manifest, OCR candidate manifest, OCR engine/config,
scoring plan, OCR authorization, or any predecessor identity changes.

### Non-Waivable OCR Benchmark Failures

The following failures cannot be waived in this draft:

- OCR trial occurs without exact `accepted_protocol` plus bounded OCR
  authorization;
- gold samples are missing, stale, not frozen before execution, or derived from
  PDF text-layer content, OCR output under test, translation, or proofreading;
- OCR candidate manifest is missing, stale, or lacks stable candidate IDs;
- OCR output rows lack predecessor identity, scoring plan ID, input identity,
  or output identity/hash when hashing is authorized;
- OCR output rows do not bind exact OCR candidate manifest revision/hash,
  scoring plan revision/hash, gold-sample manifest revision/hash,
  map-consumption authorization or `not_used`, and predecessor IDs;
- PDF text-layer content/order payload appears in any gold sample, OCR output,
  map evidence, accepted source evidence, output manifest, benchmark report,
  finding payload, persisted comparison evidence, or other output artifact;
- derived text-layer comparison metrics/findings lack explicit text-layer
  provenance or non-canonical status;
- benchmark metrics, gold samples, or scoring thresholds are chosen after
  seeing OCR output;
- OCR output silently drops, duplicates, reorders, substitutes, invents, or
  normalizes protected source content;
- PDF text-layer content/order is treated as canonical source evidence or is
  copied into benchmark output artifacts;
- unsupported layouts or regions are silently coerced into supported output.

## Step 7 Result

OCR benchmark protocol rules were remediated after Sol review, confirmed by
renewed Sol/Terra review, and committed as
`1b30b776 Draft Gate 1 OCR benchmark protocol`. No OCR trial, gold-sample
creation, PDF text-layer extraction, page-image inspection, map consumption,
text comparison, or candidate-derived observation is authorized.

## QA And Non-Waivable Findings

Status: confirmed and committed as `c22e4ebb`.

This section defines the future QA finding model that must exist before any
OCR-derived source candidate can be promoted toward Accepted Source Text. It
does not authorize QA execution, page-image inspection, OCR review, comparison
against `Вирал`, source reconstruction, translation, proofreading, waiver
approval, or any candidate-derived observation.

### QA Boundary

QA and non-waivable findings are future bounded review work. Step 8 may define
finding classes, ledger shape, waiver boundaries, stale behavior, and
acceptance predicates without reviewing candidate content.

Any future QA run requires:

- exact `accepted_protocol` revision;
- accepted/current candidate intake record if required;
- current selected-page manifest, render evidence, pre-OCR map evidence, OCR
  benchmark evidence, and source-candidate evidence only when each has been
  created and admitted by its own bounded authorization;
- frozen QA scope naming pages, regions, source blocks, artifacts, reviewer
  authority, limits, expiry, and stop conditions;
- accepted or version-bound provisional finding ledger schema;
- accepted or version-bound provisional anchor identity model;
- distinct bounded QA authorization naming inputs, outputs, allowed actions,
  review roles, and invalidation behavior.

### Finding Semantics

Findings must use orthogonal fields. Waiver, parking, acceptance, unlock, and
staleness are not finding lifecycle states.

| Field | Allowed Values | Meaning |
|---|---|---|
| `finding_lifecycle` | `open`, `resolved`, `rejected`, `superseded` | whether the finding itself remains active |
| `currentness` | `current`, `stale` | whether predecessor evidence still matches the finding |
| `blocking_effect` | `blocking`, `non_blocking` | whether the finding blocks acceptance while current and unresolved |
| `waiver_eligibility` | `waivable`, `non_waivable` | whether accepted waiver policy may ever apply |
| `resolution_kind` | `none`, `verified_fix`, `evidence_rejection`, `superseded` | how a finding stopped blocking, if it did |

External records must remain separate and can only be referenced by ID:

| Record | Requirement |
|---|---|
| `waiver_request` | separate request record; cannot unlock anything |
| `waiver_decision` | separate accepted/denied decision under accepted waiver policy and authority |
| `scope_revision` | separate accepted scope change that may exclude future units from accepted scope |
| `parking_record` | explanation record linked to a scope revision; not a finding state |
| `acceptance_record` | separate user-visible decision; derived from current QA evidence, never from finding status alone |

Valid finding rows must enforce:

- `waiver_eligibility=non_waivable` requires null `waiver_request_ref` and null
  `waiver_decision_ref`;
- a stale finding cannot be resolved, rejected, waived, parked, or used for
  acceptance until re-reviewed against current evidence;
- acceptance/unlock effect is derived only by the QA acceptance predicate;
- parking cannot be applied to a finding inside frozen accepted scope.

### Required Future QA Scope And Coverage Records

Future QA must create immutable scope and coverage records before absence of a
finding can be claimed.

`qa_scope_manifest` must carry:

| Field | Requirement |
|---|---|
| `qa_scope_id` | stable QA scope ID |
| `scope_revision` | exact revision/hash when hashing is authorized |
| `protocol_revision` | exact `accepted_protocol` revision/hash |
| `bounded_qa_authorization_id` | distinct QA authorization |
| `source_candidate_id` | exact candidate/source-candidate artifact identity and revision |
| `accepted_scope_units` | frozen page, region, block, table, card, stat-block, art/text overlay, and artifact units under review |
| `criterion_taxonomy_version` | exact taxonomy version defining required criteria |
| `anchor_model_version` | exact anchor identity model version |
| `predecessor_ids` | exact source/render/map/OCR/gold/source-candidate predecessors |
| `scope_revision_refs` | approved external scope changes, if any |
| `invalidation_rules` | what changes stale the scope |

`qa_coverage_manifest` must carry one row for every required
`accepted_scope_unit x criterion_id` pair:

| Field | Requirement |
|---|---|
| `coverage_manifest_id` | stable coverage manifest ID and revision/hash when authorized |
| `qa_run_id` | bounded QA run identity |
| `qa_scope_id` | exact scope revision under review |
| `scope_unit_id` | exact page/region/block/table/card/stat/artifact unit |
| `criterion_id` | exact taxonomy criterion |
| `applicability_result` | `assessed`, `not_applicable_by_rule`, or `excluded_by_scope_revision` |
| `classification_rule_id` | required for conditional or not-applicable outcomes |
| `finding_refs` | current finding IDs linked to this row, or explicit empty list after assessment |
| `evidence_refs` | exact evidence IDs/revisions/hashes when authorized |
| `review_actor_time` | reviewer/tool role and timestamp |
| `currentness` | `current` or `stale` plus invalidation event if stale |

An empty finding ledger cannot prove absence. Missing coverage for any required
scope unit or criterion is itself a non-waivable finding.

### Required Future Finding Ledger Fields

When authorized later, every finding ledger row must carry:

| Field | Requirement |
|---|---|
| `finding_ledger_id` | stable ledger ID |
| `ledger_revision` | exact ledger revision/hash when authorized |
| `protocol_revision` | exact `accepted_protocol` revision/hash |
| `finding_schema_version` | exact schema version |
| `taxonomy_version` | exact finding taxonomy version |
| `qa_run_id` | bounded QA run identity |
| `qa_scope_id` | exact QA scope revision |
| `criterion_id` | exact taxonomy criterion that produced the finding |
| `finding_id` | stable unique finding ID |
| `stage` | `reconstruct`, `translate`, `proofread`, or `gate_01_qa` |
| `finding_class` | controlled class from the accepted QA taxonomy |
| `severity` | controlled severity; must not replace non-waivable classification |
| `waiver_eligibility` | `waivable` or `non_waivable` plus rule reference |
| `blocking_effect` | `blocking` or `non_blocking` |
| `finding_lifecycle` | `open`, `resolved`, `rejected`, or `superseded` |
| `currentness` | `current` or `stale` |
| `source_scope` | page, region, block, table, card, stat block, overlay, artifact, or cross-artifact scope |
| `subject_artifact_id` | exact subject artifact ID/revision/hash when authorized |
| `predecessor_ids` | exact predecessor artifact IDs |
| `anchor_model_version` | exact anchor model version |
| `anchor_refs` | exact accepted/current anchor IDs or explicit `missing_anchor` finding |
| `evidence_refs` | exact evidence artifact IDs, revisions, hashes when authorized, and predecessor IDs |
| `detected_by` | reviewer/tool role, method, and timestamp |
| `decision_actor_time_ref` | actor, timestamp, authority, and decision reference for resolution/rejection/supersession |
| `resolution_kind` | `none`, `verified_fix`, `evidence_rejection`, or `superseded` |
| `resolution_refs` | evidence proving fix, evidence-backed rejection, or supersession |
| `waiver_request_ref` | null unless waivable class and request exists |
| `waiver_decision_ref` | null unless waivable class and accepted/denied decision exists |
| `parking_scope_revision_ref` | external accepted scope revision ID if excluded from future scope |
| `supersedes` | previous finding IDs if replaced |
| `superseded_by` | later finding ID if replaced |
| `invalidated_by` | invalidation event ID if stale |
| `invalidation_reason` | why the finding became stale |
| `invalidated_at` | timestamp when staleness was recorded |
| `propagation_refs` | records invalidating coverage, QA result, or acceptance |

### Parking And Waiver Boundary

Parking is not a finding disposition and cannot make a non-waivable defect
acceptable inside frozen accepted scope.

Parking is allowed only through a separate accepted `scope_revision` that:

- predates the acceptance decision that consumes it;
- names exact scope units, anchors, artifacts, predecessor revisions, and
  affected descendants;
- proves the excluded unit and all dependent text/structure/artifacts are not
  part of Accepted Source Text;
- records rationale, authority, effective time, expiry or review trigger, and
  invalidation rules;
- forces a new QA coverage manifest and acceptance roll-up for the revised
  scope.

A stale finding may never be parked to restore acceptance. A non-waivable
finding inside frozen accepted scope may stop blocking only by verified fix,
evidence-backed rejection as invalid, or an external scope revision proving the
affected scope and all dependents are outside Accepted Source Text.

### Finding Class Matrix

This draft names classes; it does not assert that any candidate contains them.

| Class | Example Risk | Default 0.1 Treatment |
|---|---|---|
| `missing_content` | source text, table cell, list item, caption, page marker, or stat value omitted | non-waivable |
| `duplicate_content` | duplicated paragraph, list item, table row, or page marker | non-waivable |
| `wrong_reading_order` | columns, sidebars, captions, tables, or boxed text placed in wrong sequence | non-waivable inside accepted scope |
| `ambiguous_reading_order` | order cannot be proven from current evidence | non-waivable until resolved or excluded by scope revision |
| `substitution_or_hallucination` | invented or substituted names, numbers, rules, stats, dice, dates, references | non-waivable |
| `protected_data_change` | numbers, units, dice notation, page refs, headings, labels, proper names altered | non-waivable |
| `structure_loss` | heading/list/table/card/stat block/callout structure flattened or misclassified | non-waivable inside accepted scope |
| `paragraph_boundary_loss` | two or more visible source paragraphs collapsed into one body paragraph/continuation unit, or paragraph breaks preserved only in prose instead of semantic unit structure | non-waivable inside accepted scope |
| `anchor_mismatch` | source block points to wrong page/region/artifact predecessor | non-waivable |
| `overlay_or_clipping_risk` | text/art overlap, clipped text, hidden text, unreadable overlay in source evidence | non-waivable until classified by evidence-bound rule |
| `unsupported_region` | region/content type outside accepted profile | non-waivable inside accepted scope |
| `unverifiable_in_scope_content` | in-scope content cannot be verified against current evidence | non-waivable |
| `missing_qa_coverage` | required scope unit or criterion lacks current coverage row | non-waivable |
| `stale_lineage` | finding or QA result relies on superseded evidence | non-waivable |
| `waiver_policy_gap` | waiver requested before waiver policy/authority is accepted | non-waivable |
| `review_gap` | required reviewer, role, or evidence is missing | non-waivable |

Reading-order, structural-semantics, and overlay/clipping classification must
use versioned `classification_rule_id` values and evidence-backed outcomes.
Unresolved ambiguity inside accepted scope remains non-waivable. Tables, cards,
stat blocks, callouts, captions, sidebars, overlays, and page markers must be
represented as separate coverage criteria where present in the accepted scope.

### Page-Complete Semantic Map Gate

Page-complete review is allowed to expose a complete-ok/acceptance option only
after semantic structural criteria pass as first-class gates. The contract uses
the following review vocabulary:

| State | Meaning | Routing |
|---|---|---|
| `semantic_map_ready` | Canonical semantic-unit JSON validates, Markdown projection validates, page inventory reconciliation validates, and no non-waivable structural finding remains. | A page-complete review packet may expose complete-ok routing if all other page-complete gates also pass. |
| `semantic_map_blocked` | Semantic-unit validation, Markdown projection validation, or inventory reconciliation has a non-waivable blocker. | Complete-ok and acceptance routing must be suppressed; only hold/blocker/supersession routing may remain. |
| `semantic_unit_review_only` | Semantic units exist to make human review inspectable and traceable. | Review evidence only; no source/OCR/PDF/render/fixture/page/Gate acceptance. |

For page-complete packets, canonical semantic-map JSON is the authority.
Markdown is a human projection only and must not become a parallel source of
semantic truth. The packet/report must run semantic validation, Markdown
projection validation, and page-inventory reconciliation before status,
manifest hash recording, blocker roll-up, and decision-option filtering.

The following page-complete semantic failures inherit non-waivable treatment
from the finding matrix: collapsed multi-unit regions, missing expected
headings, flattened quotes, paragraph-boundary loss, invalid heading levels,
block-role leakage into display style, table/card/stat/callout/sidebar topology
loss, missing page markers or captions where expected, unsupported in-scope
regions, missing or broken lineage, duplicate units, non-contiguous reading
order, and semantic payload leakage into status/roadmap documents.

Semantic body text must preserve visible source paragraph boundaries. The
preferred representation is one semantic `paragraph` or `continuation` unit per
source paragraph, with `continues_from`/`continues_to` used only when the same
paragraph crosses a column or page boundary. A `paragraph` or `continuation`
unit containing an embedded blank-line paragraph boundary is blocked by
`paragraph_boundary_flattened` (`SU-PARA-001`) unless a separately reviewed
contract records explicit paragraph-boundary metadata instead.

### Non-Waivable QA Failures

The following failures cannot be waived in this draft:

- QA run occurs without exact `accepted_protocol` and distinct bounded QA
  authorization;
- QA accepts evidence with missing, stale, or mismatched predecessor identity;
- finding ledger lacks required fields, exact evidence references, anchor
  references, reviewer authority, status, or invalidation rules;
- non-waivable finding is marked waived, passed, accepted, or released;
- open, stale, unsupported, or unresolved blocking findings are ignored during
  source acceptance;
- waiver exists before accepted waiver policy and authority, or waiver attempts
  to unlock a non-waivable class;
- missing content, duplicate content, wrong order, hallucination,
  substitution, protected data change, anchor mismatch, stale lineage, or
  unsupported region is silently normalized as acceptable output;
- QA result is produced after source/render/map/OCR/gold/anchor/ledger schema
  changes without deterministic stale behavior;
- finding payload copies prohibited PDF text-layer content/order;
- page-complete review exposes complete-ok/acceptance routing while
  `semantic_map_blocked`, projection validation blocked, inventory
  reconciliation blocked, or any non-waivable structural finding remains;
- roadmap/status/checkpoint documents store semantic map payloads instead of
  artifact IDs, states, and hashes;
- Accepted Source Text is created without a current QA ledger and explicit
  blocking-finding disposition;
- an empty ledger or missing coverage manifest is used to prove absence of
  findings;
- parking is used as a finding status, waiver substitute, stale-finding repair,
  or non-waivable bypass.

### QA Acceptance Predicate

Future Accepted Source Text requires all of the following:

- exact Accepted Source Text artifact identity is named;
- exact `accepted_protocol`, bounded QA authorization, QA run, QA scope,
  coverage manifest, finding ledger revision, schema/taxonomy/anchor versions,
  and current predecessor set are named;
- QA coverage manifest has one current row for every required
  `accepted_scope_unit x criterion_id` pair;
- every coverage row is assessed, explicitly not applicable by an accepted
  classification rule, or excluded by an accepted external scope revision;
- QA ledger exists and is current for the accepted scope;
- every current finding is resolved by verified fix, rejected with reviewer
  evidence, or superseded by a current finding; no stale unresolved finding is
  accepted;
- no open blocking, stale unresolved, unsupported in-scope, missing-coverage,
  unverifiable in-scope, ambiguous-order, or non-waivable finding remains
  inside accepted scope;
- any waiver is linked to accepted waiver policy, allowed waivable class,
  authority, evidence, expiry/scope, and user-visible decision record;
- no waiver reference exists for `waiver_eligibility=non_waivable`;
- any scope exclusion is backed by accepted scope revision, descendant
  exclusion proof, rerun QA coverage, and acceptance roll-up;
- acceptance record names the actor/authority and decision timestamp.

## Step 8 Result

QA and non-waivable finding rules were confirmed by renewed Sol/Terra review
and committed as `c22e4ebb Draft Gate 1 QA findings policy`. No QA run,
finding ledger, waiver decision, Accepted Source Text, OCR review, page-image
inspection, PDF text-layer extraction, text comparison, or candidate-derived
observation is authorized. The next safe action is Step 10 review/checkpoint
as draft-only governance work.

## Fixture And Acceptance Updates

Status: confirmed by Sol/Terra and committed as `7b0c2f41`.

This section syncs future fixture obligations and Core 0.1 acceptance criteria
with the Gate 1 protocol. It does not create executable fixtures, fixture
directories, fixture manifests, expected outputs, QA evidence, source text, OCR
evidence, translation output, proofreading output, or release evidence.

### Step 9 Boundary

Step 9 may update:

- `fixture_strategy.md` fixture obligations;
- `core_0_1_acceptance_matrix.md` declared criteria;
- roadmap/status references to fixture and acceptance readiness.

Step 9 must not:

- copy, render, OCR, hash, inspect, or otherwise process `Вирал`;
- create `fixtures/core-0.1` fixture packages;
- mark fixture rows as passed, failed, accepted, released, or executable;
- accept the Gate 1 protocol;
- authorize any bounded trial or candidate-derived action;
- create or accept source, translation, proofread, QA, or release artifacts.

### Fixture Obligation Rules

Future fixtures must be declared before execution and must bind:

| Field | Requirement |
|---|---|
| `fixture_id` | stable ID |
| `fixture_type` | `positive` or `negative` |
| `protocol_revision_under_test` | exact accepted protocol revision |
| `fixture_manifest_schema_version` | exact fixture manifest schema version |
| `acceptance_criteria_refs` | exact acceptance matrix IDs |
| `gate_step_refs` | Gate 1 steps covered |
| `expected_result` | expected pass/fail/blocked result |
| `expected_failure_class` | required for negative fixtures |
| `expected_blocker` | required for negative fixtures |
| `non_waivable_rule_ref` | required when a non-waivable failure is expected |
| `input_identity_refs` | source fixture inputs only after fixture creation is authorized |
| `expected_artifact_patterns` | expected IDs or artifact classes, not real output payloads |
| `review_authority` | role allowed to accept fixture result later |
| `invalidation_rules` | what changes stale the fixture expectation |

Negative fixtures must prove that the system rejects invalid states for the
expected reason. A negative fixture that fails for a different reason does not
satisfy acceptance.

Empty, wildcard, placeholder, unresolved, or non-existent fixture IDs,
criterion references, failure classes, or blockers do not count as fixture
coverage.

### Fixture Coverage Requirements

The declared future fixture set must cover:

- unsupported profile and invalid stage/type edges;
- candidate intake boundary and unauthorized metadata claims;
- render candidate manifest, comparison plan, output lineage, and stale render
  evidence;
- pre-OCR map shared identity, missing regions, incompatible map records, and
  no OCR/PDF text-layer/translation payload in maps;
- OCR candidate manifest, scoring plan, gold sample identity, text-layer
  payload containment, output manifest lineage, and stale OCR evidence;
- QA scope, coverage manifest, finding ledger, non-waivable findings,
  invalid waiver, parking bypass, missing coverage, and empty-ledger rejection;
- positive Core 0.1 lane only after Gate 1 protocol acceptance and separately
  authorized bounded execution.

### Acceptance Matrix Sync Rules

Acceptance matrix rows declared by Step 9 are obligations, not passed checks.
Every declared row must include:

- stable criterion ID;
- Gate 1 step or Core lane reference;
- future evidence artifact class;
- fixture coverage expectation;
- failure behavior;
- current status `declared`, `draft`, `blocked`, or `parked`.

Step 9 may mark a criterion as `declared`. It must not mark any criterion as
`passed`, `accepted`, `released`, or `waived`.

### Non-Waivable Step 9 Failures

The following failures cannot be waived in this draft:

- fixture is executed or created before fixture creation is authorized;
- `Вирал` is converted into a fixture without separate user approval and
  bounded task authorization;
- acceptance matrix marks a criterion passed/accepted/released without
  executable evidence;
- negative fixture lacks expected failure class, expected blocker, or linked
  acceptance criterion;
- future fixture result lacks exact protocol revision, fixture manifest
  revision, predecessor identity, expected result, actual result, and reviewer
  authority;
- fixture or acceptance row is used to authorize candidate-derived action.

## Step 9 Result

Fixture and acceptance updates are confirmed by renewed Sol/Terra review and
committed as `7b0c2f41`. No fixtures, fixture manifests, expected outputs, QA
run, acceptance result, protocol acceptance, `Вирал` processing, or
candidate-derived action is authorized. The next safe action is Step 10
review/checkpoint as draft-only governance work.

## Step 10 Review And Checkpoint

Status: `review_ready` for review only.

Step 10 records validation, critique collection, roadmap/status synchronization
needs, and the next-step decision. It does not accept this protocol, authorize
any bounded trial, create fixture packages, run QA, process `Вирал`, create a
selected-page manifest, or authorize any candidate-derived action.

### Step 10 Inputs

| Input | Status | Use | Boundary |
|---|---|---|---|
| Roadmap validation | passed locally on 2026-07-17 | prove current `roadmap.yaml` is syntactically valid | does not prove governance readiness |
| Protocol consistency review | completed by OpenClaw/Averroes | identify missing Step 10 section, status namespace mismatch, and review-ready criteria drift | does not accept the protocol |
| Roadmap/status review | completed by OpenClaw/Zeno | identify stale status labels and checkpoint readiness gaps | does not pass the checkpoint |
| Safety/authority review | completed by OpenClaw/Newton | identify weaker authorization shorthand in adjacent documents | does not authorize candidate-derived action |
| Sol architecture review | completed by OpenClaw/Sol | identify remaining review-ready blockers and status drift | does not accept the protocol |
| Terra independent critique | completed by OpenClaw/Terra | identify premature-unlock risks and weaker hard-stop wording | does not authorize candidate-derived action |
| Pre-Step-10 checkpoint commit | `4a41673b` | preserve the state before Step 10 cleanup | not a rollback or acceptance record |

### Step 10 Findings

| Finding | Disposition |
|---|---|
| Step 10 was listed as next action but had no explicit protocol section. | Closed by adding this Step 10 section. |
| Header used plain `draft` instead of the protocol status namespace. | Closed by moving the top-level status to `review_ready` for review only. |
| `review_ready` requirements were split across transition rules and authority table. | Closed by making validation and next-step decision explicit in the transition rule and checkpoint. |
| Step 10 wording could be read as authorizing the first narrow `Вирал` action. | Closed by stating Step 10 can only request review of the exact draft revision. |
| Adjacent docs used weaker shorthand such as protocol accepted/defined without a distinct bounded authorization. | Closed by requiring exact `accepted_protocol` plus distinct bounded authorization in live control surfaces. |
| Hard-stop table relied on the quarantine paragraph for some row-level prerequisites. | Closed by adding exact `accepted_protocol` plus distinct bounded authorization to every candidate-derived row. |

### Step 10 Decision

The protocol is `review_ready` for user, Sol, and Terra review of this exact
draft revision only. This state is not protocol acceptance and does not create
permission to run a bounded trial.

No candidate-derived action is authorized by Step 10 or by `review_ready`. Any
later `Вирал` action requires the exact protocol revision to be accepted as
`accepted_protocol` and a separate bounded authorization naming that exact
action, inputs, outputs, limits, authority, expiry, and invalidation behavior.

## Protocol Acceptance Record

Record id: `PA-G1-QP-20260717-001`

Status: `accepted_protocol`

Accepted by: user authority, after OpenClaw/Sol and OpenClaw/Terra read-only
review.

Accepted exact revision:

- Commit: `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- File: `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`
- File blob: `4d494e83d8d63dd3778a3813b3ee529449cee51a`

Acceptance meaning:

- The Gate 1 Qualification Protocol is accepted as the governing methodology
  for Gate 1 qualification work.
- Protocol acceptance does not accept the `Вирал` candidate as fixture,
  source evidence, accepted source, or source-profile evidence.
- Protocol acceptance does not authorize candidate-derived action by itself.
- Protocol acceptance does not lock render, OCR, map, QA, fixture, source
  profile, translation, proofreading, or implementation parameters.
- Protocol acceptance may support later bounded authorization records, each of
  which must name exactly one action, admitted inputs, allowed outputs, limits,
  authority, expiry, and invalidation behavior.

Version-bound provisional interfaces for the first bounded trial:

- artifact identity references may use the already recorded candidate path and
  SHA-256 from `fixtures/candidate_inputs/viral/README.md`;
- trace anchors may use ordinal selected-page entries only, without page images,
  OCR text, PDF text-layer payload, layout maps, or content extraction;
- waiver and non-waivable finding interfaces remain as declared by this
  protocol and cannot unlock the trial.

## Bounded Trial Authorization Record

Record id: `BA-G1-VIRAL-SPM-001`

Status: `expired`; scope consumed by `SPM-G1-VIRAL-001`

Ledger: `bounded_trial_authorizations.md`

Exact action: create one selected-page manifest for the `Вирал` candidate.

Admitted inputs:

- candidate identity already recorded in
  `fixtures/candidate_inputs/viral/README.md`;
- local candidate copy path
  `fixtures/candidate_inputs/viral/Call_of_Cthulhu_Viral.pdf`;
- recorded SHA-256
  `0A80B6F389821B87553D26746D2BE171B4482BA9BBC6E3EB3FEC26274EDBED05`;
- selection policy: ordinal pages 1-20 only.

Allowed output: one `selected_page_manifest` record that binds the selected
ordinal page range, candidate identity, accepted protocol revision/blob, this
authorization ID, actor, timestamp, and invalidation rules.

Produced output:

- `fixtures/candidate_inputs/viral/selected_page_manifest_pages_1_20.md`
- Manifest id: `SPM-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- no rendering, OCR, mapping, PDF text-layer extraction, metadata refresh,
  recounting, rehashing, benchmark execution, QA, fixture creation, source
  acceptance, translation, proofreading, or implementation;
- no page images, extracted text, layout maps, screenshots, benchmark results,
  QA findings, fixtures, or accepted source artifacts may be produced;
- no downstream action is authorized by the manifest's existence.

Expiry: after the first selected-page manifest revision is created, or at
2026-07-18T20:30:00+03:00, whichever comes first.

Invalidation: source path/hash, selection policy, manifest schema, accepted
protocol revision/blob, authorization record, or user authority changes stale
the manifest.

## Step 1 Result

This shell exists so the team can review the shape of the protocol before
filling in the remaining sections. It intentionally keeps operational actions
blocked.

## Next Sections To Fill

| Today Step | Section To Add | Status |
|---|---|---|
| 2 | Gate 1 input package | revised draft |
| 3 | Authority and states | drafted |
| 4 | Candidate PDF intake rules | confirmed and committed |
| 5 | Render benchmark protocol | confirmed and committed |
| 6 | Pre-OCR map qualification | confirmed and committed |
| 7 | OCR benchmark protocol | confirmed and committed |
| 8 | QA and non-waivable findings | confirmed and committed |
| 9 | Fixture and acceptance updates | confirmed and committed |
| 10 | Review and checkpoint | accepted_protocol plus first bounded authorization |

## Current Next Action

`C01TETD-G1-VIRAL-001` is the current Core 0.1 text extraction trial readiness
cursor after `C01RSPLAD-G1-VIRAL-001`. It completes points 1-5 using Sol/Terra
review instead of human review, then stops before point 6. Point 6 requires
calling Bogdan before any actual OCR, render, PDF parsing/text-layer
extraction, text extraction, runtime start/execution, runtime implementation,
page `021+` processing, source/OCR/render/PDF/raw mutation, translation,
proofreading, push, or downstream execution.
