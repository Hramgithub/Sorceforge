# Acceptance Vocabulary

Status: draft for Phase 0 decision

## Terms

| Term | Meaning | Authority | Must Not Mean |
|---|---|---|---|
| `passed` | Automated or checklist validation completed without blocking findings for a declared criterion. | tool/check owner | Human acceptance or release approval. |
| `accepted` | A human/operator accepts an artifact for its stage with required evidence and no unresolved blocking findings. | stage acceptance owner | Merely generated, linted, or plausible. |
| `waived` | A specific finding is allowed to remain under an explicit rationale, scope, authority, and evidence record. | waiver authority | Ignored, hidden, or globally excused. |
| `conformant` | Artifact satisfies machine-checkable schema/contract constraints for its type and stage. | validator | Quality acceptance or semantic correctness. |
| `released` | A frozen candidate/evidence package is approved for the declared release claim. | release authority plus Terra release review | Current workspace state or latest successful run. |

## Additional Lifecycle Terms

| Term | Meaning |
|---|---|
| `open` | Finding or decision is unresolved and blocks any dependent acceptance if severity requires it. |
| `resolved` | Finding is corrected or dispositioned with evidence. |
| `rejected` | Proposed artifact, waiver, or decision is not allowed under the current charter. |
| `superseded` | Artifact revision was replaced by a newer revision. |
| `stale` | Artifact depends on changed/superseded predecessor and cannot be consumed as current. |
| `frozen` | Candidate set is immutable for release review. |
| `revalidated` | Artifact was checked again against unchanged identity/lineage requirements. |
| `readiness` | A routing signal that an artifact may be ready for a later bounded review or acceptance packet. |
| `coverage_summary` | A declared inventory/coverage overview for human planning and QA targeting. |
| `page_complete_candidate` | A page packet is ready to ask for page-complete review; no page is accepted yet. |
| `page_complete_accepted` | A separately authorized human/operator decision accepts one exact page as complete. |

## Stage Acceptance

| Stage | Accepted Artifact | Required Evidence |
|---|---|---|
| `reconstruct` | Accepted Source Text | source evidence manifest, anchors, findings/waivers, acceptance record |
| `translate` | Faithful RU Draft | accepted source predecessor, translation units, QA findings/waivers, terminology evidence |
| `proofread` | Proofread RU Master | faithful RU draft predecessor, semantic/language findings, final acceptance record |

## Proposed Authority Model

- Tools may mark checks as `passed` or `failed`.
- Validators may mark artifacts as `conformant` or `nonconformant`.
- The operator or assigned reviewer marks artifacts as `accepted`.
- Waiver authority must be explicit per finding severity.
- Release approval requires a frozen candidate and independent Terra release
  review.

## Hard Rules

- A downstream stage cannot consume an unaccepted predecessor.
- An artifact with open blocking findings cannot be accepted.
- A waiver cannot exist without scope, rationale, owner, and affected artifact.
- `released` cannot point at a mutable workspace.
- Human acceptance cannot override hash/lineage mismatch; it must create a new
  artifact or a recorded waiver where allowed.
- `readiness`, `coverage_summary`, and `page_complete_candidate` are not
  acceptance states and must not unlock downstream source, fixture, Gate,
  translation, proofreading, renderer/profile, implementation, or push work.
- Page-complete acceptance is page-scoped. It cannot accept another page, a
  whole Gate, fixtures, source profile parameters, translation, proofreading,
  renderer/profile behavior, or implementation without separate authority.

## Waiver Closure Semantics

Proposed rule:

- A valid waiver may close a specific finding for stage acceptance only when
  the finding type/severity is waiver-eligible.
- A valid waiver does not mean the criterion `passed`; it means the finding is
  visible and accepted as a bounded exception.
- A waived finding must remain visible in release evidence and limitations.
- A waiver can be revoked or invalidated by source/profile/schema changes.
- Release approval must state whether waived findings are inside or outside the
  release claim.

Pending decisions:

- Which severities are never waiver-eligible?
- Can proofreading language findings be waived, or must all language findings
  be resolved?
- Can semantic findings ever be waived for 0.1?
- Who is waiver authority for 0.1 fixtures versus real pilot material?
