# Core 0.1 Implementation Authorization Receipt Plan

Status: `planned_for_bounded_execution`

Scope: prepare `C01IAR-G1-VIRAL-001`, a bounded Core 0.1 implementation
authorization receipt after `C01IPP-G1-VIRAL-001`.

## Authorization

Bogdan authorized this in Telegram message `2485`:

`c01ipp packet ok; proceed to prepare Core 0.1 implementation authorization receipt from C01IPP; no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no source-profile acceptance beyond G1WGADR, no push, commit`

## Inputs

- `C01IPP-G1-VIRAL-001` Core 0.1 implementation planning prep packet.
- `C01IPP-G1-VIRAL-001` report, summary, and manifest hashes.

## Outputs

- Fail-closed builder: `scripts/build_core_0_1_implementation_authorization_receipt.py`.
- Focused contract: `tests/test_core_0_1_implementation_authorization_receipt.py`.
- Receipt, report, summary, and manifest under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_implementation_authorization_receipt_G1_VIRAL_001/`.
- Current status, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization as needed.

## Boundaries

- Implementation authorization receipt material only.
- Runtime implementation is not authorized and not created.
- First-slice design prep and first-slice runtime start are not authorized.
- No OCR execution/remediation rerun, render/PDF/raw/source mutation,
  translation, proofreading, renderer/profile acceptance, push, or downstream
  action.
- No page `021+` processing or authorization.
- No source-profile acceptance beyond `G1WGADR-G1-VIRAL-001`.
- No new or broader fixture admission.

## Verification

- Focused pytest for `test_core_0_1_implementation_authorization_receipt.py`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite from repo root with local basetemp.
