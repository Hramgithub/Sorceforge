# Sol Step 9 Fixture And Acceptance Architecture Review

- Goal: `20260715-sourcefold-phase-0-release-charter`
- Step: Gate 1 Step 9, Fixture And Acceptance Updates
- Role/model/effort: Sol architect / `gpt-5.6-sol` / high
- Review kind: architecture and gating review; not release review
- Verdict: **NOT OK**
- Timestamp: `2026-07-15T23:23:23+03:00`
- Elapsed time: approximately 15 minutes
- Token use: unavailable to this role/runtime

## Scope And Result

Documentation-only review of the assigned Step 9 draft. The declaration-only
and quarantine boundaries are sound: acceptance rows are not marked passed,
accepted, or released; Step 10 remains blocked; and no protocol acceptance,
fixture execution, bounded trial, or candidate-derived action is authorized.

Approval is blocked by incomplete and inconsistent fixture-to-criterion
contracts. The current documents cannot yet prove unambiguous coverage of Gate
1 Steps 1-8 and the Core 0.1 acceptance claims.

## Blocking Findings

1. **Fixture identity is inconsistent across control surfaces.** Roadmap Gate 1
   references `fixture-map-missing-region` and
   `fixture-ambiguous-reading-order`, while `fixture_strategy.md` declares
   `fixture-missing-region` and `fixture-column-order`. Roadmap Core 0.1
   references `fixture-open-finding-acceptance-rejected`, while the strategy
   declares `fixture-open-finding`. This conflicts with the stable
   `fixture_id` obligation and makes coverage non-deterministic.

2. **Coverage is not complete or explicit enough.** The fixture strategy's
   Gate 1 coverage table starts at Step 4. `AM-G1-01` aggregates Steps 1-3 but
   its two named fixtures do not explicitly exercise the accepted-protocol,
   authority, permission, decision, evidence, and finding-state prerequisite.
   `AM-G1-03` uses the placeholder `render benchmark negative fixture to
   define` instead of a stable fixture ID. The Core 0.1 rows `AM-02-01` through
   `AM-10-03` have no explicit criterion-to-fixture mapping or explicit parked
   disposition; the broad positive-lane statement is insufficient to prove
   claim coverage.

3. **The negative-fixture contract is not mechanically unambiguous.** The
   protocol fixture field table requires `expected_failure_class` and
   `acceptance_criteria_refs` but omits `expected_blocker`, even though the
   protocol later makes all three mandatory. Existing fixture declarations do
   not bind each negative fixture to non-empty exact values for those fields.
   Consequently an underspecified declaration could be counted as coverage
   before its expected failure contract is reviewable.

## Remediation Specification

1. Establish one canonical fixture index in `fixture_strategy.md`. For every
   fixture, record one stable `fixture_id`, type, non-empty `gate_step_refs`,
   non-empty `acceptance_criteria_refs`, expected result, and—when negative—an
   exact `expected_failure_class`, `expected_blocker`, and applicable
   `non_waivable_rule_ref`. Make roadmap and matrix references use those exact
   IDs; do not rely on aliases unless an explicit alias-to-canonical-ID rule is
   declared.
2. Add a complete obligation map for Gate 1 Steps 1-8. Split aggregated or
   placeholder coverage where necessary so protocol/authority prerequisites,
   unauthorized intake, render lineage/staleness, map identity/prohibited
   payload, OCR lineage/text-layer containment, and QA coverage/ledger rules
   each have a stable fixture obligation or an explicit blocked/parked row.
3. Map every Core 0.1 acceptance criterion `AM-02-01` through `AM-10-03` to at
   least one declared fixture obligation, or record an explicit parked status,
   reason, owner, and later evidence task. Keep all rows declaration-only.
4. Add `expected_blocker` to the protocol fixture contract and state the
   invariant: empty, missing, wildcard, unresolved, or non-existent criterion
   refs do not count as coverage; a negative fixture failing for any reason
   other than its exact expected class/blocker does not satisfy acceptance.
5. Keep Step 10, protocol acceptance, fixture creation/execution, and all
   candidate-derived actions blocked until renewed Sol/Terra review approves
   the remediated Step 9 documentation.

## Remediation Acceptance Criteria

- One canonical fixture ID resolves identically in strategy, matrix, protocol,
  and roadmap references.
- Gate 1 Steps 1-8 and every Core 0.1 matrix row have explicit fixture coverage
  or explicit parked/blocking disposition.
- Every negative fixture declaration has non-empty exact failure class,
  blocker, and criterion references, and empty/ambiguous values are explicitly
  non-satisfying.
- No fixture is created, executable, passed, accepted, released, or used as
  authorization evidence.
- Step 10 remains `blocked`, and candidate quarantine remains default-deny.

## Assumptions, Risks, And Evidence

- Assumption: Step 9 is limited to obligation declarations; executable fixture
  schemas and artifacts are future bounded work.
- Primary risk: inconsistent IDs or placeholder coverage can produce false
  roll-up confidence and later allow an unrelated failure to masquerade as an
  expected negative result.
- Evidence: `gate_01_qualification_protocol.md` lines 1205-1308;
  `fixture_strategy.md` proposed fixture set, Gate 1 Step Coverage, Provenance
  Requirements, and Step 9 Fixture Boundary; `core_0_1_acceptance_matrix.md`
  Core and Gate 1 tables; `roadmap.yaml` Gate 1 and Core 0.1 fixture lists;
  `today_20260715_step_plan.md` Step 9/10 states; `PROJECT_STATUS.md`,
  `plan.md`, and `context.md` current Step 9 checkpoint state.

## Files Checked Or Changed

Checked:

- `gate_01_qualification_protocol.md`
- `fixture_strategy.md`
- `core_0_1_acceptance_matrix.md`
- `plan.md`
- `context.md`
- `today_20260715_step_plan.md`
- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`

Changed:

- `handoffs/sol-step-9-fixture-acceptance-review-20260715.md` (this immutable
  receipt only)

## Blockers And Next Action

Blockers are the three findings above. Next action: the orchestrator may revise
only the Step 9 documentation contracts, then request renewed Sol and Terra
review. Do not start Step 10.

No candidate PDF, candidate-derived artifact, OCR-derived artifact, or fixture
artifact was opened, inspected, hashed, rendered, extracted, processed,
created, or changed during this review.
