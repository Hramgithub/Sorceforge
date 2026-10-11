# Core 0.1 First-Slice Runtime Authorization Prep Plan - C01RSAP-G1-VIRAL-001

Status: `planned_for_bounded_execution`

Scope: prepare `C01RSAP-G1-VIRAL-001`, a bounded Core 0.1 first-slice
runtime authorization prep packet for `C01WP-01-phase-1-scaffold-contracts`,
consuming only `C01RSPLP-G1-VIRAL-001` and Bogdan's `c01rsplp packet ok`.

This plan is not runtime authorization, runtime start, or runtime
implementation.

## Authorization

Bogdan authorized this in Telegram message `2566`:

`c01rsplp packet ok; proceed to prepare Core 0.1 first-slice runtime authorization prep for C01WP-01 from C01RSPLP; no runtime implementation, no runtime source-profile lock/acceptance, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

## Inputs

- Runtime source-profile lock-or-parking decision: `C01RSPLP-G1-VIRAL-001`.
- Acceptance-matrix trace review: `C01AMTR-G1-VIRAL-001`.
- Architecture review packet: `C01FSARP-G1-VIRAL-001`.
- Source-profile lock-or-parking receipt: `C01SPLPR-G1-VIRAL-001`.
- Whole Gate 1 accepted scope from `G1WGADR-G1-VIRAL-001`: pages `001`-`020`
  plus `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups only.

## Packet Duties

- Canonically map `C01RSAP-G1-VIRAL-001` to
  `core_0_1_first_slice_runtime_authorization_prep`.
- Record Bogdan's human review acceptance of `C01RSPLP-G1-VIRAL-001`.
- Prepare runtime authorization decision context only.
- Reference runtime source-profile parking without creating a runtime
  source-profile lock or acceptance.
- Remove only the consumed `human_review_c01rsplp_required` blocker.
- Preserve first-slice runtime authorization and runtime start as future
  separately authorized decisions.
- Keep page `021+`, OCR/render/PDF/raw/source mutation, translation,
  proofreading, new fixture admission, and push blocked.

## Explicit Non-Goals

- No runtime implementation.
- No runtime authorization grant.
- No runtime start.
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
- Focused pytest contract for `C01RSAP-G1-VIRAL-001`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite before commit.
