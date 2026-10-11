# Terra Step 1 Qualification Protocol Critique — 2026-07-15

Role/model: independent critic in the Terra remit; Codex GPT-5 runtime.  
Review kind: `process` (non-release, non-frozen planning candidate).  
Reviewer implementation/material design: **No**. I did not implement modules,
process the candidate PDF, or materially design the protocol.

## Scope Reviewed

Candidate: committed Step 1 shell at `52dca0c623d55e271e53e996f53ab3385ba7c338`:
`gate_01_qualification_protocol.md` (109 added lines). The working-tree copy
is modified and contains an uncommitted Step 2 draft; it was inspected only to
preserve the boundary and is not accepted state or part of this verdict.

Files checked:

- `Sourcefold/AGENTS.md`
- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/today_20260715_step_plan.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/phase_gate_component_hierarchy.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/acceptance_vocabulary.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/artifact_lineage_model.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`

Excluded: all CoC/Dune/translator material; the `Вирал` PDF was not opened,
rendered, OCRed, mapped, hashed, counted, or otherwise processed.

## Verdict

**Accept with required revisions.** The shell correctly declares its planning
scope and blocks the listed operational actions. It is a usable container, but
must not serve as an unlock control until the revisions below remove ambiguous
qualification, identity, and waiver paths.

## Critical Risks (ordered)

1. **High — `qualified` is an uncontracted unlock state.** The shell says it
   may unlock a named action and assigns it to “user/orchestrator after review,”
   while `acceptance_vocabulary.md` does not define that state and
   `roadmap.yaml` records the exact Gate 1 authority as unknown. This conflicts
   with `phase_gate_component_hierarchy.md`, where Gate 1 is
   `pending_approval` with `approver: user`.
2. **High — candidate-input quarantine is incomplete.** The hard-stop table
   blocks the main derivatives, but does not explicitly prohibit any new PDF
   inspection or candidate-derived metadata before Step 4. The protocol must
   distinguish citation of already recorded path/hash from opening, parsing,
   recounting, hashing, or creating any new candidate-derived record.
3. **High — evidence can acquire decision effect before identity is settled.**
   The evidence skeleton has a `record_id` and input hashes, but no binding of
   the record revision/hash, predecessor identities, action authorization, or
   mutation rule. `artifact_lineage_model.md` requires exact identity/lineage;
   `roadmap.yaml` still lists artifact identity and trace anchors as blockers.
4. **Medium — waiver and non-waivable boundaries are not yet hard stops.** The
   shell exposes `waived` while waiver policy and severity eligibility are
   unresolved. `acceptance_vocabulary.md` requires explicit scope, rationale,
   authority, and evidence; the hierarchy marks core violations non-waivable.
5. **Medium — protocol completion is not itself an explicit prerequisite.**
   The shell should state that no operational action is authorized until Steps
   2–10, the listed decision blockers, review, and checkpoint are complete;
   Gate 1 roll-up cannot bypass unresolved required descendants.

## Premature Unlock Risks

No PDF work or module implementation was observed or authorized by the
committed shell. The risk is semantic: a later reader could interpret a
`qualified` record, a provisional waiver, or a minimally populated evidence
record as permission for intake/render/map/OCR work before the complete
protocol and user authority decision exist.

## Missing Blockers / Hard Stops

- `decision-acceptance-authority`, canonical-format, artifact-identity,
  trace-anchor, and waiver-policy decisions remain explicit roadmap blockers.
- No candidate-derived artifact or metadata may be created before the later
  intake rule names the action, evidence, authority, and failure behavior.
- No waiver may unblock Gate 1 while waiver eligibility and authority are
  unresolved; identity mismatch, unauthorized candidate interaction, and open
  blocking findings must be non-waivable.
- A Gate/component/subcomponent cannot be accepted while required descendants
  remain draft, proposed, evidence-gated, or pending approval.

## Step 2 Disposition

**Revise; do not advance to Step 3 or treat Step 2 as accepted.** Retain the
current Step 2 content only as draft context. First patch the Step 1 control
language, then revise Step 2 to carry the same quarantine and identity limits.

## Recommended Minimal Patch List for Orchestrator

1. Make `qualified` explicitly non-authorizing until a complete protocol,
   named action record, and user approval exist; otherwise remove it from the
   Step 1 state table until Step 3 resolves authority.
2. Add an absolute candidate quarantine: only existing path/hash citations are
   allowed; all new inspection, metadata derivation, and derivative creation
   are blocked before the accepted Step 4 intake rule.
3. Add a protocol-level blocker list and completion predicate covering all
   Steps 2–10 plus the five unresolved roadmap decisions.
4. Expand the evidence skeleton with evidence-record identity/revision/hash,
   predecessor identities, authorized action and authority record, timestamp,
   and explicit stale/revalidation behavior.
5. State that no waiver may authorize a Gate 1 action until the waiver policy
   is accepted, and enumerate the non-waivable control failures above.

## Immutable Receipt

Evidence: Git confirms `52dca0c6` as the Step 1-shell commit; Git status shows
the target is currently modified only for the separate Step 2 draft. No release
claim was reviewed, so freeze evidence and release QA references are N/A.
This receipt binds only the committed Step 1 candidate. Any mutation of that
candidate, or adoption of the current Step 2 draft, invalidates this verdict
and requires a new independent review; it does not alter this receipt.

Blockers: the five roadmap decisions above, incomplete protocol sections, and
the required revisions. Recommendation: revise the shell, retain all
operational hard stops, then continue the planning sequence.

Timestamp: 2026-07-15T20:02:47+03:00  
Elapsed active review time: 113 seconds.  
Token use: 43,666 (goal meter at receipt timestamp).
