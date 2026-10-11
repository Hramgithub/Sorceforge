# Sol Step 9 Remediation Confirmation

- Goal: `20260715-sourcefold-phase-0-release-charter`
- Step: Gate 1 Step 9, Fixture And Acceptance Updates
- Role/model/effort: Sol architect / `gpt-5.6-sol` / high
- Review kind: renewed architecture and gating confirmation; not release review
- Verdict: **NOT OK**
- Timestamp: `2026-07-15T23:30:41.5967424+03:00`
- Elapsed time: approximately 10 minutes
- Token use: goal counter snapshot `71,067` tokens at receipt creation; exact final
  goal total is available only after goal closure

## Scope And Result

Documentation-only confirmation against the previous Step 9 Sol blockers. The
review was limited to fixture identity, Gate 1/Core 0.1 coverage declarations,
negative-fixture contracts, `AM-G1-06`, and the Step 10 authorization boundary.

The remediation closes fixture alias drift in the Gate 1/Core 0.1 roadmap
scope, adds the missing protocol field, explicitly adds invalid-waiver and stale
lineage coverage to `AM-G1-06`, and keeps Step 10 and all candidate-derived work
blocked. It does not close the complete stable-mapping or exact negative-blocker
contracts. The renewed Step 9 verdict therefore remains **NOT OK**.

## Confirmation Matrix

| Confirmation | Result | Evidence And Reason |
|---|---|---|
| 1. Fixture IDs consistent across strategy, matrix, protocol, and roadmap for Gate 1/Core 0.1 | **CLOSED in bounded scope** | Gate 1 and Core 0.1 roadmap fixture references now resolve to IDs in the canonical strategy index; the matrix uses those canonical spellings; the protocol declares the strategy/matrix synchronization contract and contains no conflicting alias. |
| 2. Gate 1 Steps 1-8 and Core 0.1 rows have complete stable mappings or explicit parked/blocking disposition | **NOT CLOSED** | The visible tables contain rows, but the mappings are not contract-complete or bidirectionally consistent. Details are in Blockers B1 and B2. |
| 3. Every negative declaration binds a non-empty exact failure class, blocker, and criterion refs | **NOT CLOSED** | Fields are non-empty, but several blocker values are disjunctive or multi-target rather than one exact expected blocker; Core criteria assigned by the matrix are also absent from the corresponding canonical fixture declarations. Details are in Blockers B1 and B3. |
| 4. `AM-G1-06` explicitly includes invalid waiver and stale lineage | **CLOSED** | `AM-G1-06` names both `fixture-invalid-waiver` and `fixture-stale-lineage`. |
| 5. Step 10 and all operational/candidate actions remain blocked | **CLOSED** | The protocol, working plan, goal plan, project status, context, and roadmap keep renewed review pending, Step 10 blocked, and fixture creation/execution, protocol acceptance, Viral processing, and candidate-derived action unauthorized. |

## Blocking Findings

### B1. Canonical fixture declarations and Core coverage rows are not reciprocal

The canonical index is declared as the fixture-ID source and the protocol
requires exact `acceptance_criteria_refs`, but the Core coverage map assigns
criteria that the corresponding fixture declarations do not name.

Examples:

- `fixture-positive-0.1` declares the range-like token
  `AM-02-01..AM-10-03`, not the exact matrix IDs required by the protocol.
- `fixture-unsupported-profile` declares only `AM-G1-01` and `AM-G1-02`, while
  the Core coverage map also assigns it to `AM-02-01`.
- `fixture-render-lineage-stale`, `fixture-column-order`,
  `fixture-missing-region`, `fixture-stale-lineage`, and other negative
  fixtures are assigned to Core rows without those Core IDs appearing in their
  canonical `Criteria` cells.
- `AM-10-02` uses `all negative fixtures in the canonical fixture index`
  instead of a stable, explicit list of fixture IDs.
- `AM-10-03` says a release-review fixture obligation is parked until Step 10,
  but does not record the parked obligation's reason, owner, and exact later
  evidence task. Its disposition also combines `declared` and `parked` rather
  than selecting one controlled state.

This allows the matrix to claim fixture coverage that the fixture's own
declared contract does not authorize and prevents deterministic reciprocal
validation.

### B2. Several Gate 1 obligations have labels but no exact negative case

The Step 1-8 table is present, but some required behaviors are represented only
by a broad fixture whose declared failure class does not exercise the stated
obligation:

- Steps 1-3 require protocol, authority, permission, decision, evidence, and
  finding-state prerequisites; the mapped failures cover missing
  protocol/authority, unsupported profile, and invalid edge, but do not
  explicitly cover missing or invalid permission, decision, evidence, and
  finding states.
- Step 4 requires rejection of unauthorized or stale candidate metadata, but
  is mapped only to `fixture-unsupported-profile`, whose declared class is
  `unsupported_source_profile`.
- Step 6 requires map shared identity and rejection of OCR/PDF text-layer/
  translation payloads, but none of its mapped fixture declarations has an
  exact prohibited-map-payload failure class. The Gate 1 matrix further narrows
  `AM-G1-04` to only `fixture-missing-region` and
  `fixture-unclassified-block`, omitting the other IDs claimed by the strategy
  Step 6 row.

These are unresolved coverage obligations, not explicit parked/blocking
dispositions.

### B3. Some negative fixtures still lack one exact blocker

The protocol correctly added `expected_blocker`, but canonical declarations
still contain alternatives or multiple targets, including:

- `fixture-stale-lineage`: `block evidence or source acceptance`;
- `fixture-missing-region`: `block map/source acceptance`;
- `fixture-unclassified-block`: `block or preserve as bounded fallback`;
- `fixture-text-layer-leakage`: `block OCR/source evidence acceptance`.

An expected blocker must resolve to one exact controlled blocker for the named
fixture case. In particular, `block or preserve` is not a single expected
negative result.

## Concrete Remediation Specification

1. Make the canonical index the bidirectional coverage contract. For every
   fixture, enumerate every exact Gate 1 and Core criterion ID it covers. Do
   not use ranges, wildcards, `all fixtures`, aliases, or implicit coverage.
2. Make every matrix row reciprocal: each fixture listed on a criterion row
   must list that criterion in its canonical declaration. Add a documentation
   check that rejects either one-way mismatch.
3. Add exact declaration-only fixture obligations for the uncovered Gate 1
   cases: missing/invalid permission, decision, evidence, and finding states;
   unauthorized or stale intake metadata; and prohibited OCR/PDF text-layer/
   translation payload in a pre-OCR map. Alternatively, park each obligation
   with controlled state, reason, owner, and exact later evidence task.
4. Replace each multi-target or alternative expected blocker with one exact
   blocker. Split fixture declarations where one input is intended to prove
   different blockers. Split the unclassified case into a negative blocking
   fixture and, if required, a separate positive bounded-fallback fixture.
5. Replace `AM-10-02` aggregate wording with the exact canonical negative
   fixture IDs. For `AM-10-03`, record an explicit parked disposition with
   reason, owner `gpt-5.6-terra` in the independent release-review role, and
   the Step 10 exact-candidate release-review evidence task. This Sol handoff
   does not perform or substitute for that release review.
6. Synchronize the resulting exact IDs and controlled dispositions across
   `fixture_strategy.md`, `core_0_1_acceptance_matrix.md`, the Step 9 protocol
   contract, and the Gate 1/Core 0.1 roadmap nodes. Keep all fixtures declared
   and not created.
7. Keep Step 10, protocol acceptance, fixture creation/execution, Viral
   interaction, and every candidate-derived action blocked until renewed Sol
   and independent Terra review both approve the corrected Step 9 contracts.

## Remediation Acceptance Criteria

- Every fixture ID referenced by a Gate 1/Core 0.1 matrix or roadmap row
  resolves exactly once in the canonical index.
- Every matrix-to-fixture edge is reciprocal: the fixture declaration names
  the exact criterion, and the criterion row names the exact fixture.
- No criterion list uses a range, wildcard, aggregate phrase, placeholder,
  alias, or implicit fixture set.
- Gate 1 Steps 1-8 have exact fixture cases for each stated obligation, or an
  explicit controlled parked/blocking record with reason, owner, and later
  evidence task.
- Every Core row `AM-02-01` through `AM-10-03` has exact reciprocal fixture
  coverage or a complete parked/blocking disposition.
- Every negative fixture has one non-empty exact failure class, one non-empty
  exact blocker, and non-empty exact criterion references. A different failure
  class or blocker cannot satisfy the criterion.
- `AM-G1-06` continues to name both invalid-waiver and stale-lineage coverage.
- All rows remain declaration-only; no fixture, evidence, acceptance, release,
  protocol acceptance, bounded trial, or candidate action is created or
  authorized.
- Step 10 remains blocked pending matching renewed Sol/Terra approval.

## Assumptions And Risks

- Assumption: Step 9 is declaration-only governance work; fixture schemas,
  directories, manifests, inputs, expected outputs, and execution are future
  bounded work.
- Assumption: roadmap fixture lists may be scoped subsets, but every listed ID
  must resolve to the canonical index and may not use an alias.
- Risk: one-way criterion mappings can produce false coverage roll-ups even
  when fixture declarations do not claim the relevant criterion.
- Risk: disjunctive blockers let an unrelated failure satisfy a negative
  fixture and conceal which acceptance boundary was actually enforced.
- Risk: broad Step labels can appear complete while leaving permission,
  metadata, payload-containment, or release-review obligations untested and
  unparked.

## Verification And Evidence

- Previous blocker baseline:
  `handoffs/sol-step-9-fixture-acceptance-review-20260715.md`.
- Canonical declaration and exact-value invariant:
  `fixture_strategy.md` lines 14-40.
- Gate 1 obligation map:
  `fixture_strategy.md` lines 42-56.
- Gate 1 criterion mappings and `AM-G1-06`:
  `core_0_1_acceptance_matrix.md` lines 38-49.
- Core coverage mappings and parked release-review wording:
  `core_0_1_acceptance_matrix.md` lines 51-83.
- Protocol exact-field, no-placeholder, non-waivable, and authorization rules:
  `gate_01_qualification_protocol.md` lines 1205-1314.
- Protocol Step 10 state:
  `gate_01_qualification_protocol.md` lines 1322-1340.
- Working-plan Step 9/10 state:
  `today_20260715_step_plan.md` lines 37-38 and 76-82.
- Goal-plan Step 10 state: `plan.md` lines 129-131.
- Roadmap Gate 1/Core fixture IDs and renewed-review state:
  `roadmap.yaml` lines 122-130, 200-210, 345-348, 703-713, and 1561-1567.
- Project status and context retain renewed-review/no-authorization state:
  `Sourcefold/PROJECT_STATUS.md` lines 89-94 and `context.md` lines 437-466.

Verification was static documentation comparison only. No validation script,
fixture execution, release review, candidate action, or derived-artifact check
was performed.

## Files Checked Or Changed

Checked:

- `fixture_strategy.md`
- `core_0_1_acceptance_matrix.md`
- `gate_01_qualification_protocol.md`
- `plan.md`
- `context.md`
- `today_20260715_step_plan.md`
- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`
- `handoffs/sol-step-9-fixture-acceptance-review-20260715.md`

Changed:

- `handoffs/sol-step-9-remediation-confirmation-20260715.md` (this immutable
  receipt only)

## Blockers And Next Action

Blockers are B1-B3 above. The next action is a documentation-only correction
of the Step 9 contracts, followed by renewed Sol architecture confirmation and
independent Terra critique. Do not start Step 10.

No candidate PDF, Viral file, candidate-derived artifact, PDF-derived artifact,
OCR-derived artifact, or fixture artifact was opened, inspected, hashed,
rendered, extracted, processed, created, changed, or otherwise touched during
this review.
