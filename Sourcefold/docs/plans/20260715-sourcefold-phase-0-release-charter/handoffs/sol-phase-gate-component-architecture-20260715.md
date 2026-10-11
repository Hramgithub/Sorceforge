# Sol Phase/Gate/Component Architecture Handoff

Role: `gpt-5.6-sol`
Review kind: architecture
Status: completed
Timestamp: 2026-07-15T03:28:12+03:00

## Scope

Read-only architecture recommendation for a stable planning hierarchy focused
on Phase 0 / Gate 1 / Source Profile.

## Recommended Model

Use a five-level hierarchy:

```text
Phase -> Gate -> Component -> Subcomponent -> Parameter
```

For the immediate decision:

```text
Phase 0 -> Gate 01 -> Source Profile -> six subcomponents -> parameter decisions
```

Gate 1 remains `pending_approval`. It must not authorize implementation or
release until unresolved child parameters are accepted or parked.

## Required Record Shape

Each hierarchy record should support:

- hierarchy identity: `hierarchy_id`, `entity_type`, `parent_id`,
  phase/gate numbers, title;
- parameter contract: value, allowed values, units, required flag;
- decision state: status, owner, approver, rationale, decision record, date;
- evidence state: decision evidence, runtime evidence, artifact types;
- dependency state: requires, enables, verification gates, invalidation rules;
- control behavior: failure behavior, waiver class, branch behavior;
- external links: roadmap node refs, acceptance criterion refs, lineage refs;
- versioning: profile version/hash and supersession.

Decision status and evidence status must remain separate. A well-evidenced
proposal is not automatically accepted.

## Source Profile Subcomponents

| Subcomponent | Purpose |
|---|---|
| `SC-INPUT` | Profile and input envelope. |
| `SC-RENDER` | Page-image evidence. |
| `SC-OCR` | OCR authority and PDF text-layer branch. |
| `SC-LAYOUT` | Supported geometry and reading-order boundary. |
| `SC-STRUCTURE` | RPG structure boundary and fallback. |
| `SC-CONTROL` | Profile identity, failure behavior, invalidation. |

## Linkage Guidance

Roadmap node IDs must not double as parameter IDs. Use explicit references:

```yaml
hierarchy_ref: P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-RESOLUTION_DPI
roadmap_node_refs:
  - node_id: decision-source-profile-0.1
    relation: owns
acceptance_criterion_refs:
  - AM-02-02
```

Recommended relations are `owns`, `depends_on`, `enables`, and `verifies`.

## Acceptance Criteria For This Remediation

1. Every Gate 1 Source Profile rule has one stable parameter ID and parent
   chain.
2. Every required parameter has value, status, approver, evidence requirement,
   failure behavior, waiver class, and invalidation conditions.
3. The accepted Source Profile is versioned and hash-bound.
4. Every durable runtime artifact references that exact profile revision.
5. Every normative parameter maps to a decision record and either an acceptance
   criterion or explicit `decision_only` designation.
6. Every acceptance criterion has a stable ID and reverse parameter references.
7. Gate status is derived from child statuses.
8. Positive and negative fixtures cover all profile branches.
9. Validation rejects duplicate IDs, dangling references, invalid parentage,
   invalid statuses, and acceptance rows without evidence/failure behavior.
10. User approval, Sol architecture evidence, Terra critique, roadmap
    validation, and implementation authorization remain separate receipts.

## Receipt

- Files changed: none by subagent.
- Current decision: Source Profile and Gate 1 remain `pending_approval`.
- Blockers: prior-work taxonomy evidence is incomplete; technical values remain
  unaccepted; exact roadmap/acceptance references need reconciliation.
- Token use reported by subagent: 35,144.
