# Core 0.1 Source-Profile Lock-or-Parking Receipt Plan

Status: `planned_for_bounded_execution`

Scope: prepare `C01SPLPR-G1-VIRAL-001`, a bounded single source-profile
lock-or-parking receipt for `C01WP-01-phase-1-scaffold-contracts` after
`C01FSDP-G1-VIRAL-001`.

## Authorization

Bogdan authorized this in Telegram message `2515`:

`c01fsdp packet ok; proceed to prepare single source-profile lock-or-parking receipt for C01WP-01 from C01FSDP; no runtime implementation, no source-profile lock or acceptance beyond this receipt, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

## Inputs

- `C01FSDP-G1-VIRAL-001` Core 0.1 first-slice design prep packet.
- `C01FSDP-G1-VIRAL-001` report, summary, and manifest hashes.

## Outputs

- Fail-closed builder: `scripts/build_core_0_1_source_profile_lock_or_parking_receipt.py`.
- Focused contract: `tests/test_core_0_1_source_profile_lock_or_parking_receipt.py`.
- Receipt, report, summary, and manifest under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_source_profile_lock_or_parking_receipt_G1_VIRAL_001/`.
- Current status, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization as needed.

## Boundaries

- Source-profile receipt material only.
- Source-profile parking is recorded only for the C01WP-01 design-prep boundary.
- Runtime source-profile lock and runtime source-profile acceptance are not
  created.
- Runtime implementation is not authorized and not created.
- No OCR execution/remediation rerun, render/PDF/raw/source mutation,
  translation, proofreading, renderer/profile acceptance, push, or downstream
  action.
- No page `021+` processing or authorization.
- No new or broader fixture admission.

## Verification

- Focused pytest for `test_core_0_1_source_profile_lock_or_parking_receipt.py`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite from repo root with local basetemp.
