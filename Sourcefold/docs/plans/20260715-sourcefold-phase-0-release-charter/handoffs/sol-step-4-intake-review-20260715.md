# Sol Step 4 Candidate PDF Intake Review

- Goal id: `20260715-sourcefold-phase-0-release-charter`
- Step id: `4-candidate-pdf-intake-rules`
- Role/model/effort: Sol architect / `gpt-5.6-sol` / high
- Review kind: architecture; not a release decision
- Timestamp: `2026-07-15T20:57:29.4892341+03:00`
- Elapsed time: 136 seconds at receipt preparation
- Token use: 62,060 at receipt preparation

## Verdict

**Not OK, blocker remains.**

The draft preserves default-deny intent, but its contracts are not yet internally
consistent enough to commit or to unlock Step 5 drafting.

## Assumptions

- Existing Viral path/hash/status references are prior records only and were not
  reverified in this review.
- “Start Step 5” means drafting render benchmark rules only, with no PDF access,
  manifest creation, rendering, benchmark execution, or derived observations.
- Version-bound provisional interfaces remain intentionally allowed for the
  first bounded trial.

## Blocking Findings

1. **The selected-page-manifest gate is weaker than the governing authorization
   predicate.** The Hard Stops row requires an accepted Step 4 rule, identity
   rule, selection policy, and generic user authorization, but does not require
   an `accepted_protocol` revision plus a separate bounded trial authorization.
   This conflicts with the Intake Boundary and Bounded Trial Authorization
   Predicate. The nearby statement that quarantine is absolute “before Step 4”
   also implies that Step 4 alone could end quarantine.

2. **The first intake record can deadlock under an allowed provisional
   interface.** Intake authorization permits identity/hash interfaces to be
   accepted or version-bound provisional, while `source_pdf_artifact_id` must
   be assigned by accepted identity rules and the conflict failure names only
   accepted identity rules. A provisionally authorized intake therefore has no
   conforming artifact-ID branch.

3. **Field cardinality conflicts with observation authorization.** The record
   says it should carry `content_hash`, but an authorization may explicitly
   deny hashing. Unlike page count and rights attestation, the hash field has no
   conditional/absent-state rule. The contract must either require hashing in
   every intake authorization or define conditional omission such as
   `not_authorized`/`not_observed`; it must not cause an implicit hash operation.

4. **Step 4 reintroduces an ungoverned mixed state namespace.**
   `quarantine_status` combines candidate classification, permission, record,
   evidence, and decision concepts (`present-unqualified`,
   `intake_authorized`, `intake_recorded`, `stale`, `rejected`) without named
   authority or transitions. This duplicates the Step 3 namespaces and leaves
   unclear whether a value can unlock downstream work.

5. **Canonical working state is contradictory.** The protocol header still says
   Step 3 review is pending and Step 4 is blocked; `context.md` repeats stale
   Step 3/4 state beside the current Step 4 state. Roadmap
   `qualification_protocol: confirmed-committed` is also ambiguous while the
   protocol node remains planned and unaccepted. A commit would preserve
   conflicting control state.

## Concrete Remediation Specification

- Make every candidate-derived action, including selected-page-manifest
  creation, require the exact `accepted_protocol` revision and a distinct
  bounded authorization naming that one action, inputs, outputs, limits,
  expiry, and invalidation. State that quarantine persists until those two
  predicates are both true for the exact action.
- Replace the intake field list with a requirement matrix: mandatory,
  conditional, source, and allowed absent-state. Align artifact identity and
  hash algorithm fields with both accepted and version-bound provisional
  interfaces. Do not infer or derive any unlisted observation.
- Either make hashing mandatory and require it explicitly in the intake
  authorization, or make `content_hash` conditional. Apply the same explicit
  rule to page count and rights attestation.
- Remove `quarantine_status` or define a dedicated, non-unlocking intake-record
  namespace with authority and transitions. Keep authorization in permission
  state, evidence validity in evidence state, and rejection in decision/finding
  state. `allowed_next_actions` must default to none and cannot itself grant
  permission.
- Synchronize the protocol header, live context, plan/checklist wording, and
  roadmap labels so “drafted/reviewed/committed” cannot be read as
  `accepted_protocol`.

## Acceptance Criteria

- No Step 4 path permits opening, parsing, hashing, page counting, metadata
  extraction, manifest creation, inspection, rendering, OCR, mapping, or
  benchmarking before exact protocol acceptance plus exact bounded
  authorization.
- A valid intake record can be constructed under either accepted or explicitly
  version-bound provisional identity/hash interfaces without silently deriving
  unauthorized fields.
- Every intake state and transition has one namespace, authority, evidence, and
  non-unlocking behavior; later work always needs separate authorization.
- Canonical status artifacts agree that Step 4 is reviewed only after matching
  Sol/Terra decisions, the protocol remains unaccepted, and Viral remains
  quarantined.
- `Sourcefold/scripts/validate_roadmap.ps1` and scoped `git diff --check` pass
  after remediation.

## Non-Blocking Notes

- The separation of protocol acceptance, bounded trial authorization, and Gate
  1/source-profile acceptance avoids the earlier evidence-cycle deadlock.
- Step 5 can be drafted safely without intake evidence once these blockers are
  remediated and Step 4 receives the required matching review; Step 5 drafting
  must not execute a benchmark or touch Viral.
- The current roadmap validator passed, and scoped `git diff --check` reported
  only line-ending conversion warnings.

## Exact Answer

**No. The orchestrator should not commit the current Step 4 draft or start Step
5 yet. After the blocking contract/state corrections receive matching Sol and
Terra OK, the orchestrator may commit Step 4 and start Step 5 render benchmark
rules as drafting only, with Viral still quarantined.**

## Files And Evidence

Reviewed target files:

- `gate_01_qualification_protocol.md`
- `today_20260715_step_plan.md`
- `context.md`
- `plan.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`

Governing references checked:

- `Sourcefold/AGENTS.md`
- `docs/governance/nri_goal_governance.md`
- `Sourcefold/PROJECT_STATUS.md`

Changed files:

- `handoffs/sol-step-4-intake-review-20260715.md` only

Verification/evidence:

- Compared the five targets with committed Step 3 baseline `85b0b765`.
- Ran `Sourcefold/scripts/validate_roadmap.ps1`: passed.
- Ran scoped `git diff --check 85b0b765 -- <five target files>`: no whitespace
  errors; line-ending warnings only.
- No PDF was opened, rendered, OCRed, mapped, parsed, hashed, counted, inspected,
  or otherwise processed. No Viral-derived metadata or artifact was created.

Blockers: findings 1-5 above.

Next action: orchestrator remediates only the listed Step 4 contracts and stale
state labels, then requests renewed Sol/Terra review before commit or Step 5.
