# Sol Step 1/2 Revision Approval Review

- Goal: `20260715-sourcefold-phase-0-release-charter`
- Step: revised Steps 1/2 approval review
- Role/model/effort: Sol architect, `gpt-5.6-sol`, high
- Timestamp: `2026-07-15T20:20:58+03:00`

## Verdict

**Not OK, blocker remains.**

## Blocking Finding

The protocol-acceptance dependency graph is still cyclic and its roadmap gate
is weaker than the protocol contract:

- `gate_01_qualification_protocol.md` requires all required Gate 1 descendants
  to leave `evidence_gated`/`pending_approval` before the protocol can become
  `accepted_protocol`.
- The same document requires `accepted_protocol` before a bounded trial can
  generate the render/OCR/map evidence needed to move those descendants out of
  evidence-gated states.
- `roadmap.yaml` still lists acceptance authority, canonical formats, artifact
  identity, and trace anchors as blockers of the protocol while its active edge
  chain places those decisions downstream of the protocol. It also says the
  protocol need only exist and be reviewed before candidate work, whereas the
  revised protocol requires exact protocol acceptance plus bounded trial
  authorization.

This is a semantic deadlock and premature-unlock ambiguity even though the
roadmap schema validator passes.

### Required remediation specification

1. Separate three predicates: protocol acceptance, bounded-trial authorization,
   and Gate 1/source-profile acceptance.
2. Protocol acceptance must require completed/reviewed Steps 2-10, exact
   authority and interface contracts (or explicitly version-bound provisional
   interfaces), and user acceptance of an exact protocol revision/hash; it must
   not require trial-produced evidence or resolved evidence-gated profile
   parameters.
3. Bounded-trial authorization must require `accepted_protocol`, accepted Step
   4 intake rules, and the existing exact action/input/output/limit/expiry/
   invalidation envelope.
4. Gate 1/source-profile acceptance, not protocol acceptance, must enforce that
   required descendants are accepted or validly parked and that accepted
   evidence is current.
5. Align `roadmap.yaml` blockers/edges/gate text with those three predicates so
   the graph is acyclic and candidate work cannot unlock from review alone.

Acceptance criterion: a reader can traverse draft protocol -> accepted protocol
-> authorized bounded trial -> accepted evidence -> Gate 1 decision without
requiring any downstream result to authorize its own evidence-producing action.

## Non-blocking Notes

- The revised state namespaces, shell-review/protocol-acceptance boundary,
  evidence identity/lineage/staleness fields, waiver non-unlock, Step 2 input
  limits, and absolute pre-Step-4 candidate quarantine are materially sound.
- Update the Step 3 plan wording that still names generic `qualified` and the
  stale context sentence saying Step 3 waits for revisions to be applied; these
  are clarity fixes after the blocker above is repaired.

## Exact Answer

**Can orchestrator commit revised Step 1/2 and start Step 3 as drafting only,
with Viral still quarantined? No, not in the current revised state.** Repair the
acceptance/trial/Gate-1 dependency split and roadmap gate wording first. Then a
documentation-only Step 3 draft is architecturally safe while Viral remains
fully quarantined.

## Receipt

- Scope/result: reviewed the current working-tree revised Step 1/2 control
  architecture; one blocking dependency defect remains.
- Target files reviewed:
  - `gate_01_qualification_protocol.md`
  - `today_20260715_step_plan.md`
  - `context.md`
  - `plan.md`
  - `Sourcefold/docs/roadmap/roadmap.yaml`
- Supporting files checked: NRI goal governance and the prior Sol/Terra Step 1
  review handoffs.
- Files changed: only this immutable handoff receipt.
- Verification/evidence: reviewed working-tree content and diff; traced roadmap
  node blockers and active edges; `git diff --check` passed with line-ending
  warnings only; `npm run validate:roadmap` passed (25 nodes, 24 edges, 13
  checkpoints), confirming schema validity but not resolving the semantic cycle.
- PDF confirmation: no PDF was opened, parsed, rendered, OCRed, mapped,
  re-hashed, counted, inspected, or otherwise processed.
- Blocker: cyclic protocol-acceptance/evidence dependency and inconsistent
  roadmap unlock wording.
- Next action: orchestrator applies the five-item remediation above, then seeks
  Sol/Terra confirmation before committing and beginning Step 3 drafting.
- Elapsed: approximately 12 minutes active review.
- Token use: unavailable.
