# Core 0.1 Runtime Source-Profile Lock-or-Acceptance Decision Plan - C01RSPLAD-G1-VIRAL-001

Status: `planned_for_bounded_execution`

Scope: prepare `C01RSPLAD-G1-VIRAL-001`, a bounded Core 0.1 runtime
source-profile lock-or-acceptance decision record for
`C01WP-01-phase-1-scaffold-contracts`, consuming only `C01RSAD-G1-VIRAL-001`
and Bogdan's `c01rsad packet ok`.

This plan records that no runtime source-profile lock or acceptance is granted
without concrete runtime profile evidence. It is not runtime implementation,
runtime start, OCR execution, render execution, or source mutation.

## Authorization

Bogdan authorized this in Telegram message `2573`:

`c01rsad packet ok; proceed to prepare Core 0.1 runtime source-profile lock-or-acceptance decision for C01WP-01 from C01RSAD; no runtime implementation, no runtime start/execution, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

## Inputs

- First-slice runtime authorization decision: `C01RSAD-G1-VIRAL-001`.
- First-slice runtime authorization prep: `C01RSAP-G1-VIRAL-001`.
- Runtime source-profile parking decision: `C01RSPLP-G1-VIRAL-001`.
- Acceptance-matrix trace review: `C01AMTR-G1-VIRAL-001`.
- Architecture review packet: `C01FSARP-G1-VIRAL-001`.
- Source-profile lock-or-parking receipt: `C01SPLPR-G1-VIRAL-001`.
- Whole Gate 1 accepted scope from `G1WGADR-G1-VIRAL-001`: pages `001`-`020`
  plus `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups only.

## Packet Duties

- Canonically map `C01RSPLAD-G1-VIRAL-001` to
  `core_0_1_runtime_source_profile_lock_or_acceptance_decision`.
- Record Bogdan's human review acceptance of `C01RSAD-G1-VIRAL-001`.
- Record the runtime source-profile lock-or-acceptance decision for
  `C01WP-01-phase-1-scaffold-contracts`.
- Resolve the separate authorization blocker by recording that no runtime
  source-profile lock or acceptance is granted.
- Preserve runtime implementation and runtime start/execution as blocked.
- Keep page `021+`, OCR/render/PDF/raw/source mutation, translation,
  proofreading, new fixture admission, and push blocked.

## Explicit Non-Goals

- No runtime implementation.
- No runtime start or execution.
- No runtime source-profile lock or runtime source-profile acceptance.
- No source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- No OCR, render, PDF parsing/text-layer extraction, or OCR remediation.
- No source/OCR/render/PDF/raw mutation.
- No translation or proofreading.
- No page `021+` processing or authorization.
- No new or broader fixture admission.
- No push or downstream action.

## Required Checks

- Sol/Terra scope gate before implementation and after fixes if blockers are
  found.
- Focused pytest contract for `C01RSPLAD-G1-VIRAL-001`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite before commit.
