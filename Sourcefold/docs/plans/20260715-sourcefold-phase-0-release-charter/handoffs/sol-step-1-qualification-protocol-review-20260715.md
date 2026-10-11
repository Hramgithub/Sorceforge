# Sourcefold Step 1 Qualification Protocol Shell Review

Role/model: Sol architect, `gpt-5.6-sol`, high reasoning effort.

Timestamp: 2026-07-15T20:02:05+03:00 (2026-07-15T17:02:05Z).

## Scope Reviewed

Authoritative review target: `gate_01_qualification_protocol.md` at commit
`52dca0c6`, Step 1 only. The uncommitted Step 2 additions in the same file were
read only to test whether the shell constrains later drafting; they are not
accepted by this review. Supporting contracts checked: Sourcefold `AGENTS.md`,
`PROJECT_STATUS.md`, `today_20260715_step_plan.md`,
`phase_gate_component_hierarchy.md`, `acceptance_vocabulary.md`,
`artifact_lineage_model.md`, and relevant nodes/edges in
`docs/roadmap/roadmap.yaml`. No PDF was opened, rendered, OCRed, mapped, or
otherwise processed. No module or runtime design was reviewed.

## Verdict

**Accept with required revisions.** The Step 1 shell is structurally sound as
a default-deny container: it states purpose and scope, keeps candidate work
blocked, enumerates later protocol sections, and introduces an evidence-record
location. It is safe to contain Step 2 drafting, but its state and dependency
contracts are not yet safe enough to govern Step 3 authority decisions or any
operational authorization.

## Architecture Findings, Ordered by Severity

### High - State namespaces are conflated and `qualified` can be misread as permission

The shell places `draft`, `qualified`, `accepted`, `parked`, `rejected`,
`stale`, and `waived` in one table and then constrains `decision_state` to that
set (`gate_01_qualification_protocol.md@52dca0c6`, Qualification States and
Evidence Package Skeleton). This conflicts with the existing contracts:

- `phase_gate_component_hierarchy.md:31-56` separates `decision_status` from
  `evidence_status`;
- `acceptance_vocabulary.md:5-25,35-51` separates check results, artifact
  acceptance, finding/waiver disposition, staleness, and release;
- `acceptance_vocabulary.md:53-64` makes a waiver finding-specific, not a
  general parameter decision state.

The shell's definition of `qualified` means “evidence is sufficient to test a
narrow action,” which is an action-permission state, not a qualification result.
If retained, it could authorize candidate processing through terminology rather
than through an explicit bounded action record.

Required contract: separate at least `protocol_status`, `permission_status`,
`decision_status`, `evidence_status`, and `finding/waiver_status`. A trial may
run only from a version/hash-bound authorization naming the action, inputs,
outputs, limits, authority, and invalidation conditions.

### High - The protocol's completion dependencies are cyclic or underspecified

The roadmap marks acceptance authority, canonical formats, artifact identity,
and trace anchors as blockers of `gate-01-qualification-protocol`
(`roadmap.yaml:178-198`). Its active edge chain instead places the protocol
before map qualification, Source Profile, formats, authority, identity, and
anchors (`roadmap.yaml:1069-1123`). The shell also defers authority reconciliation
to a later section. If `blockers` means a hard prerequisite for protocol
completion, the protocol cannot complete without decisions that the roadmap
places downstream of it.

Required contract: distinguish dependencies needed to draft the container from
dependencies required for final protocol acceptance and from dependencies
required to authorize the first trial. The completion graph must be acyclic;
co-developed provisional interfaces must be labeled as such and bound to exact
accepted decision revisions at the Step 10 checkpoint.

### High - The evidence skeleton cannot yet satisfy parameter or lineage contracts

The skeleton's path/hash and tool fields are useful but insufficient. It does
not bind one record deterministically to the hierarchy fields required by
`phase_gate_component_hierarchy.md:31-52`, nor to durable artifact identity and
supersession in `artifact_lineage_model.md:25-44,89-97`. An array of
`parameter_ids` can also obscure which criterion/result supports which
parameter, weakening the no-skip roll-up rule.

Required contract: each qualification result must either contain or reference
one stable parameter record, stable evidence artifact identities/hashes,
criteria and observations, the measurement method, separate decision/evidence
states, actor/authority and timestamp, findings/waivers, predecessor/supersession
links, and invalidation propagation.

### Medium - Hard-stop prerequisites are not yet a complete branch contract

The Hard Stops table is correctly default-deny, but prose prerequisites are not
enough to prevent inconsistent branches. In particular, render and OCR
benchmarks are combined despite different predecessors; “approved render
evidence” is undefined; selected-page-manifest creation lacks an explicit
protocol-acceptance/source-identity/selection-policy envelope; and map creation
does not identify whether each map projection consumes source identity,
page-image identity, or both. These can remain placeholders in Step 1, but each
action row needs a stable prerequisite set and named evidence output before the
row can transition from blocked.

### Medium - Shell acceptance and protocol acceptance are not distinguished

“Explicitly accepted” currently has no object boundary. This review accepts the
container shape with revisions; it does not accept the protocol, any parameter,
the candidate, or any action. Without separate `shell_review` and
`protocol_acceptance` records, the current Step 2 draft status “Steps 1-2
completed” could be interpreted more strongly than intended.

## Missing Dependencies or Fields in the Step 1 Shell

- Protocol identity: protocol version/revision, content hash, status,
  supersedes, and the exact acceptance record.
- Subject binding: `hierarchy_id`/parameter-record reference, parent/gate, and
  one criterion-to-result mapping per affected parameter.
- Evidence binding: artifact ID/type/stage/schema version/content hash,
  predecessor IDs, canonicalization/hash method, run/config/tool identities.
- Evaluation: criterion ID, measurement method, observed result, evidence
  status, failure severity, and non-waivable/waiver class.
- Authority/audit: owner, approver or waiver authority, actor, decision time,
  rationale, finding/waiver references, roadmap and acceptance-matrix refs.
- Permission envelope: named action, exact admitted inputs, allowed outputs,
  limits, expiry, prerequisites, and revocation/invalidation triggers.
- Transition/roll-up rules: permitted state transitions, stale propagation,
  and proof that unresolved required descendants cannot unlock a parent.
- Branch prerequisites: separate manifest, render trial, render benchmark, map,
  OCR trial, OCR benchmark, and parameter-acceptance paths.

## Can Step 1 Safely Gate Step 2?

**Yes, for Step 2 drafting only.** Step 2 is non-operational, and the committed
shell's hard stops prevent PDF-derived artifacts. Continue only under these
conditions:

1. The protocol remains `draft`; shell review is not protocol acceptance.
2. Step 2 inputs may inform planning but cannot authorize candidate processing
   or parameter acceptance.
3. The status should say “Step 1 shell reviewed; Step 2 drafted; protocol not
   accepted,” not imply operational completion.
4. The state-namespace and acceptance-boundary revisions below are completed
   before Step 3 is treated as resolved.

## Recommended Minimal Patch List for Orchestrator

1. Replace the single Qualification States table with separate state namespaces
   and a small transition table; rename the action-permission meaning of
   `qualified` to an explicit bounded trial-authorization state.
2. Add a Shell Review vs Protocol Acceptance section. State that shell review
   unlocks drafting only and that only a hash-bound protocol acceptance record
   can authorize a named trial.
3. Expand the Evidence Package Skeleton with the missing identity, hierarchy,
   criterion/result, authority, lineage, finding/waiver, and supersession fields;
   prefer references to canonical parameter/artifact records over duplicated
   free text.
4. Split the Hard Stops benchmark row into render and OCR branches and give
   every action a stable prerequisite set, named output evidence, and explicit
   invalidation rule.
5. Reconcile roadmap blocker semantics so protocol drafting, protocol
   acceptance, and first-trial authorization form an acyclic dependency graph.
6. Normalize the current draft status wording so “drafted/completed step” cannot
   be confused with accepted protocol or permission to process `Вирал`.

## Assumptions and Acceptance Criteria

Assumptions: commit `52dca0c6` is the accepted Step 1 baseline; all cited Phase
0 contracts remain draft unless explicitly marked otherwise; the uncommitted
Step 2 content is context only; and acceptance of this handoff is not a release
decision.

The remediation is sufficient when: state dimensions are non-overlapping and
match the vocabulary/hierarchy contracts; shell review cannot unlock an
operational action; every hard-stop transition has exact prerequisites and
evidence outputs; qualification records are identity/lineage complete; parent
roll-up cannot skip unresolved parameters; the roadmap completion graph is
acyclic; and no candidate-derived work is permitted before a bounded,
hash-bound authorization exists.

## Handoff Receipt

- Result: Step 1 container accepted with required revisions; Step 2 drafting is
  conditionally safe; Step 3 and all operational work remain blocked pending
  the specified contract repairs.
- Files checked: the authoritative target at `52dca0c6`, its current working
  copy/diff, and the seven Sourcefold supporting files listed in Scope Reviewed.
- Files changed: only this handoff receipt.
- Verification/evidence: compared `git show 52dca0c6:<target>` with the current
  target diff; traced hierarchy, vocabulary, lineage, roadmap nodes, and active
  edges; confirmed the review did not access the candidate PDF.
- Blockers: state/permission semantics, evidence-record completeness, and
  roadmap dependency semantics are unresolved; no final Terra release review
  is in scope.
- Next action: orchestrator applies the six minimal documentation patches, then
  proceeds with Step 3 authority/state drafting and requests the planned Terra
  critique.
- Elapsed/token snapshot before receipt write: 90 seconds active goal time;
  35,298 goal tokens used. Final orchestration totals may be higher.
