# Core 0.1 Acceptance-Matrix Trace Review Plan - C01AMTR-G1-VIRAL-001

Status: `prepared`

Scope: prepare `C01AMTR-G1-VIRAL-001`, a bounded claim/evidence trace review
for `C01WP-01-phase-1-scaffold-contracts`, consuming only
`C01FSARP-G1-VIRAL-001`.

This plan is not runtime implementation.

## Inputs

- First-slice architecture review packet: `C01FSARP-G1-VIRAL-001`.
- Source-profile lock-or-parking receipt: `C01SPLPR-G1-VIRAL-001`.
- Whole Gate 1 accepted scope from `G1WGADR-G1-VIRAL-001`: pages `001`-`020`
  plus `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups only.

## Packet Duties

- Map C01WP-01 acceptance-matrix claims to existing bounded evidence.
- Preserve runtime source-profile lock/parking as a separate future decision.
- Preserve first-slice runtime authorization as a separate future decision.
- Keep page `021+`, OCR/render/PDF/raw/source mutation, translation,
  proofreading, and push blocked.

## Explicit Non-Goals

- No runtime implementation.
- No runtime source-profile lock or source-profile acceptance beyond
  `C01SPLPR-G1-VIRAL-001`.
- No OCR, render, PDF parsing/text-layer extraction, or OCR remediation.
- No source/OCR/render/PDF/raw mutation.
- No translation or proofreading.
- No page `021+` processing or authorization.
- No new or broader fixture admission.
- No push or downstream action.

## Required Checks

- Focused pytest contract for `C01AMTR-G1-VIRAL-001`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite before commit.
