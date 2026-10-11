# Terra Independent Critique — Gate 1 Step 8

Receipt status: immutable handoff

- Timestamp: `2026-07-15T22:07:06+03:00`
- Review kind: `process`
- Candidate implemented or materially designed by reviewer: `no`
- Verdict: `NOT OK — required revisions before Step 8 approval or Step 9`
- Elapsed active review time: `48 seconds` at receipt snapshot
- Token use: `37,196` at receipt snapshot

## Files Checked

- `gate_01_qualification_protocol.md` (Step 8, lines 948–1090)
- `plan.md`
- `context.md`
- `today_20260715_step_plan.md`
- `PROJECT_STATUS.md`
- `roadmap.yaml`

## Evidence and Findings

| Severity | Finding | Evidence | Required revision |
|---|---|---|---|
| Blocker | Parking can silently remove a discovered non-waivable defect from accepted scope. The predicate allows every required class to be `parked` (1074–1076), while the namespace says a parking record may narrow scope when approved (988). It does not require the approved scope decision to predate QA, prove the excluded unit is not required/previously in scope, bind its exact anchors and predecessor revisions, or force re-evaluation of coverage and acceptance roll-up. | Protocol 988, 1000, 1021, 1039–1041, 1074–1080. | Make parking ineligible for a non-waivable finding inside frozen accepted scope. Permit it only through a separately accepted scope revision with exact anchors/artifacts, rationale, authority, effective time, invalidation, and a mandatory rerun of QA coverage/roll-up. A stale finding may never be parked to restore acceptance. |
| Blocker | The future ledger cannot reproducibly prove complete QA coverage or an immutable finding disposition. It records individual findings but lacks required QA-scope/run ID, candidate/source-candidate revision, taxonomy/schema version, applicability/coverage result for each required class and scoped unit, finding revision/hash, disposition rationale, disposition actor/timestamp, and direct bounded-QA-authorization reference. Therefore an absent class can be mistaken for an untested class, and a later resolution/rejection/parking cannot be reconstructed deterministically. | Protocol 964–976, 1004–1024, 1070–1082. | Require these fields or linked immutable records, and make acceptance require a current coverage matrix showing every required class × frozen scope unit was assessed, explicitly not applicable under an accepted rule, or has a current disposition. |
| Major | The requested OCR-first classes are named, but two treatments are conditional without a controlled classification rule: `wrong_reading_order` is non-waivable only when meaning/traceability changes, and `structure_loss` only when structure carries meaning. That leaves room to downgrade ambiguous reading order or table/card/stat-block loss without reproducible evidence. Overlay/clipping is present but must likewise require an explicit classification outcome. | Protocol 1032–1041, 1059–1061. | Add a controlled, evidence-bound classification predicate for reading order, structural semantics, and overlay/clipping. Any unresolved ambiguity inside frozen scope remains non-waivable; tables, cards, and stat blocks must be separately represented in the coverage matrix. |

## Control-State Check

Consistent: Step 8 is `drafted; review pending`; Step 9 is blocked/not authorized; the protocol, context, status, and roadmap state that no Viral processing or candidate-derived observation is authorized. No source text, OCR output, QA result, waiver, or Accepted Source Text is accepted by this draft.

## Recommendation

Do not approve or commit Step 8, and do not start Step 9, until both blockers are remediated and independently re-reviewed. The current draft correctly preserves candidate quarantine, but it needs the parking and reproducibility controls above before it can safely govern later acceptance.

## Scope Attestation

No candidate PDF, candidate-derived artifact, OCR output, source text, page image, manifest, render, hash, extraction, or QA result was opened, inspected, processed, rendered, hashed, or otherwise touched during this review.
