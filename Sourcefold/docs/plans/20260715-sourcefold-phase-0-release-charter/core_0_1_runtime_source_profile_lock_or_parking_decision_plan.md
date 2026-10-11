# Core 0.1 Runtime Source-Profile Lock-or-Parking Decision Plan - C01RSPLP-G1-VIRAL-001

Status: `prepared`

Scope: prepare `C01RSPLP-G1-VIRAL-001`, a bounded runtime source-profile
lock-or-parking decision for `C01WP-01-phase-1-scaffold-contracts`, consuming
only `C01AMTR-G1-VIRAL-001`.

This plan is not runtime implementation.

## Inputs

- Acceptance-matrix trace review: `C01AMTR-G1-VIRAL-001`.
- Architecture review packet: `C01FSARP-G1-VIRAL-001`.
- Source-profile lock-or-parking receipt: `C01SPLPR-G1-VIRAL-001`.
- Whole Gate 1 accepted scope from `G1WGADR-G1-VIRAL-001`: pages `001`-`020`
  plus `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups only.

## Packet Duties

- Record the runtime source-profile disposition before first-slice runtime
  authorization prep.
- Park runtime source-profile lock/acceptance until a separate future runtime
  authorization decides whether a concrete runtime profile can be selected.
- Remove only the `runtime_source_profile_lock_or_runtime_parking_decision`
  blocker from the C01WP-01 prerequisite list.
- Preserve first-slice runtime authorization as a separate future decision.
- Keep page `021+`, OCR/render/PDF/raw/source mutation, translation,
  proofreading, and push blocked.

## Explicit Non-Goals

- No runtime implementation.
- No runtime source-profile lock or runtime source-profile acceptance.
- No source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- No OCR, render, PDF parsing/text-layer extraction, or OCR remediation.
- No source/OCR/render/PDF/raw mutation.
- No translation or proofreading.
- No page `021+` processing or authorization.
- No new or broader fixture admission.
- No push or downstream action.

## Required Checks

- Focused pytest contract for `C01RSPLP-G1-VIRAL-001`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite before commit.
