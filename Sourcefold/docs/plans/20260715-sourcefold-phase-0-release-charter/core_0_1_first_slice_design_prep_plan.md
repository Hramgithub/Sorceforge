# Core 0.1 First-Slice Design Prep Plan

Status: `planned_for_bounded_execution`

Scope: prepare `C01FSDP-G1-VIRAL-001`, a bounded Core 0.1 first-slice design
prep packet for `C01WP-01-phase-1-scaffold-contracts` after
`C01IAR-G1-VIRAL-001`.

## Authorization

Bogdan authorized this in Telegram message `2501`:

`c01iar receipt ok; proceed to prepare Core 0.1 first-slice design prep for C01WP-01-phase-1-scaffold-contracts; no runtime implementation, no source-profile lock or acceptance beyond G1WGADR, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

## Inputs

- `C01IAR-G1-VIRAL-001` Core 0.1 implementation authorization receipt.
- `C01IAR-G1-VIRAL-001` report, summary, and manifest hashes.

## Outputs

- Fail-closed builder: `scripts/build_core_0_1_first_slice_design_prep.py`.
- Focused contract: `tests/test_core_0_1_first_slice_design_prep.py`.
- Design-prep packet, report, summary, and manifest under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_first_slice_design_prep_G1_VIRAL_001/`.
- Current status, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization as needed.

## Boundaries

- First-slice design prep only.
- Runtime implementation is not authorized and not created.
- Source-profile lock and source-profile acceptance beyond `G1WGADR` are not
  created.
- No OCR execution/remediation rerun, render/PDF/raw/source mutation,
  translation, proofreading, renderer/profile acceptance, push, or downstream
  action.
- No page `021+` processing or authorization.
- No new or broader fixture admission.

## Verification

- Focused pytest for `test_core_0_1_first_slice_design_prep.py`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite from repo root with local basetemp.
