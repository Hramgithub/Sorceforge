# Sol Step 8 QA Architecture Review Receipt

- Goal: `20260715-sourcefold-phase-0-release-charter`
- Packet: Gate 1 Step 8, QA and non-waivable findings
- Role: Sol architect, `gpt-5.6-sol`, high effort
- Review type: architecture/gating review, not release acceptance
- Verdict: **NOT OK**

## Scope And Assumptions

Reviewed only the documentation contract for Step 8. The review assumes that
Accepted Source Text is a separately identified and authorized reconstruction
output, that scope parking is an external decision rather than a finding
resolution, and that absence of a finding must be proved by QA coverage rather
than inferred from an empty ledger.

No candidate, PDF, page image, OCR output, text layer, map payload, benchmark
output, or other candidate-derived artifact was opened, inspected, hashed,
rendered, OCRed, extracted, compared, or otherwise touched. Step 9 was not
started.

## Dependency And Branch Trace

The safe sequence is:

`Step 7 committed -> Step 8 corrected -> Sol approval + independent Terra
approval -> Step 9 documentation updates -> exact protocol revision accepted
by user -> separately authorized bounded QA run -> current QA evidence ->
separate Accepted Source Text decision`.

Step 8 approval may unlock Step 9 drafting only. It must not accept the
protocol, authorize QA or candidate interaction, accept evidence, approve a
waiver, or create/accept Accepted Source Text. The present draft preserves the
candidate default-deny boundary and explicitly blocks Step 9 pending matching
Sol/Terra approval, but its finding and acceptance data contracts are not yet
safe enough to approve.

## Blocking Findings

1. **Finding semantics are conflated.** In
   `gate_01_qualification_protocol.md:978-1002`, overlapping finding traits
   (`blocking`, `non_waivable`), an external waiver request, an external parking
   decision, and evidence currentness (`stale`) are presented as namespaces;
   the finding status then also absorbs `waived`, `parked`, and `stale`.
   A finding can be blocking and non-waivable simultaneously, while waiver,
   parking, acceptance, and staleness have different authority and invalidation
   rules. This model permits ambiguous transitions and implicit unlocks.

2. **The ledger cannot yet prove lineage, disposition, or invalidation.** The
   fields at `gate_01_qualification_protocol.md:1004-1024` lack an explicit
   ledger/revision identity, protocol/schema/taxonomy versions, QA run and scope
   IDs, criterion ID, subject artifact identity, direct predecessor IDs,
   blocking effect, separate currentness, exercised disposition authority and
   decision timestamp, parking decision reference, waiver request/decision
   separation, and actual invalidation event/reason/time. `invalidation_rules`
   describe future behavior but do not record that invalidation occurred.

3. **Conditional non-waivable classes can be silently softened.** At
   `gate_01_qualification_protocol.md:1032-1043`, wrong reading order and
   structure loss are conditional without a mandatory classification rule, and
   ambiguous reading order/unresolved OCR ambiguity and required-scope coverage
   gaps are not explicit classes. `unsupported_region` may be parked, but the
   draft does not require proof that the parked region and all dependents are
   outside Accepted Source Text scope. These gaps allow a defect to disappear
   through classification or scope language rather than fix, evidence-backed
   rejection, or approved exclusion.

4. **The acceptance predicate can pass on missing evidence.** At
   `gate_01_qualification_protocol.md:1068-1082`, a required class may be
   declared `absent` without a coverage record, and parking is allowed without
   disjoint-scope/descendant proof. The predicate also omits explicit current
   QA authorization, accepted/non-stale QA evidence, QA scope/criterion
   coverage identity, schema/taxonomy/anchor versions, Accepted Source Text
   artifact identity, and the acceptance authority/decision record. Therefore
   an empty or incomplete ledger could appear to satisfy acceptance.

## Concrete Remediation Specification

1. Replace the current namespace/status table with orthogonal fields:
   `finding_lifecycle = open|resolved|rejected|superseded`,
   `currentness = current|stale`,
   `blocking_effect = blocking|non_blocking`, and
   `waiver_eligibility = waivable|non_waivable`. Keep waiver requests/decisions
   and parking decisions as separate records referenced by ID. Remove
   `waived`, `parked`, and `stale` from finding lifecycle. Acceptance/unlock
   effect must be derived only by the acceptance predicate, never stored as a
   finding status.

2. Extend every finding row with at least:
   `finding_ledger_id`, `ledger_revision`, `protocol_revision`,
   `finding_schema_version`, `taxonomy_version`, `qa_run_id`, `qa_scope_id`,
   `criterion_id`, exact subject artifact ID/revision/hash when authorized,
   `predecessor_ids`, anchor-model version, `blocking_effect`, currentness,
   detection actor/time/method, resolution kind, exercised decision actor/time
   and decision reference, separate `waiver_request_ref`,
   `waiver_decision_ref`, and `parking_record_ref`, `supersedes` plus
   `superseded_by`, and `invalidated_by`, `invalidation_reason`,
   `invalidated_at`, and propagation references. Enforce null waiver fields
   when `waiver_eligibility=non_waivable`.

3. Add explicit non-waivable classes for unresolved/ambiguous reading order,
   unresolved or unverifiable OCR/source content inside accepted scope, and
   missing required QA coverage. Give every conditional class a versioned rule
   reference and evidence-backed classification. A non-waivable finding may
   cease blocking only by a verified fix, evidence-backed rejection as invalid,
   or an approved external scope exclusion proving the affected scope and all
   dependents are absent from Accepted Source Text; it can never be waived.

4. Replace “class is absent” with a current, accepted QA coverage manifest that
   has one result for every required `scope x criterion`. Require the acceptance
   record to bind the exact Accepted Source Text artifact identity, protocol,
   bounded QA authorization, QA run/scope, coverage manifest, finding-ledger
   revision, schema/taxonomy/anchor versions, current predecessor set, accepted
   and non-stale QA evidence, and named acceptance authority. Parking may only
   narrow scope through a separate approved decision with descendant exclusion
   proof. No open blocking, stale unresolved, unsupported in-scope, or
   non-waivable finding may remain.

5. Retain the Step 8 result and next-action default deny. Keep Step 9 pending
   until the corrected exact revision receives matching Sol and Terra approval.
   This review does not supply that approval.

## Acceptance Criteria For Re-Review

- Finding lifecycle contains no waiver, parking, acceptance, unlock, or stale
  semantics.
- Waiver and parking records have independent identity, authority, scope,
  expiry/invalidation, and references from—not states on—the finding.
- A non-waivable finding cannot carry an accepted waiver reference under any
  valid row or transition.
- Every finding is bound to an exact QA run/scope/criterion, subject artifact,
  predecessor chain, anchors, ledger/schema/taxonomy revision, and authority
  event.
- Staleness is recorded as currentness plus an actual invalidation event and
  deterministically propagates to QA coverage and acceptance.
- Ambiguous order, unverifiable in-scope content, and missing coverage are
  explicit non-waivable blockers.
- An empty ledger or a missing scope/criterion row cannot prove absence or
  satisfy Accepted Source Text acceptance.
- Step 9 and all candidate/PDF/OCR-derived actions remain blocked until their
  separately stated approvals and authorizations exist.

## Evidence And Files

Checked:

- `gate_01_qualification_protocol.md` — control states, predicates, Step 8, and
  current next action; principal evidence at lines 78-235 and 948-1116.
- `plan.md` — packet ownership and Step 8 review/Step 9 blocked state.
- `context.md` — reconstruction dependency and Gate 1 boundaries. Note:
  lines 130-132 still describe Step 7 as draft and Step 8 as blocked, while the
  other assigned state files record Step 7 committed and Step 8 under review;
  this is conservative state drift, not an authorization, and should be synced
  by the orchestrator after remediation.
- `today_20260715_step_plan.md` — Step 8/9 dependency and stop condition,
  especially lines 27-75.
- `PROJECT_STATUS.md` — current Step 8 draft-only status and no-candidate-action
  boundary.
- `docs/roadmap/roadmap.yaml` — Gate 1 nodes, evidence checklist, dependency
  edges, and checkpoint blocker; especially lines 92-223, 328-374,
  1145-1164, and 1506-1512.

Changed:

- `handoffs/sol-step-8-qa-review-20260715.md` only.

Verification: documentation-only cross-check of state names, authority and
transition predicates, Step 8 row contracts, acceptance conditions, today-plan
dependency, project status, and roadmap blocker. No execution or
candidate-derived verification was performed or authorized.

## Blockers And Next Action

Blockers: the four findings above. Next action: orchestrator revises Step 8 and
syncs conservative context drift, then requests bounded Sol re-review and
independent Terra critique of the exact revision. Do not start Step 9.

- Elapsed active time at receipt creation: 110 seconds
- Token use at receipt creation: 67,601 tokens
- Timestamp: `2026-07-15T19:08:28.913Z`
