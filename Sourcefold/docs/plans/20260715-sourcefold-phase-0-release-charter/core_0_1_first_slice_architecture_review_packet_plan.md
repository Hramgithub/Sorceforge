# Core 0.1 First-Slice Architecture Review Packet Plan - C01FSARP-G1-VIRAL-001

Status: `prepared`

Scope: prepare `C01FSARP-G1-VIRAL-001`, a bounded first-slice
architecture review packet for `C01WP-01-phase-1-scaffold-contracts`, consuming
only `C01SPLPR-G1-VIRAL-001`.

This plan is not runtime implementation.

## Inputs

- Source-profile lock-or-parking receipt: `C01SPLPR-G1-VIRAL-001`.
- First-slice design prep recorded through `C01FSDP-G1-VIRAL-001`.
- Whole Gate 1 accepted scope from `G1WGADR-G1-VIRAL-001`: pages `001`-`020`
  plus `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups only.

## Packet Duties

- Prepare Sol architecture review targets for module boundary, artifact
  identity, lineage trace, and acceptance-matrix trace contracts.
- Prepare Terra critique targets for boundary wording, stale current-action
  drift, and negative capability leakage.
- Keep source-profile lock parked for design-prep only through `C01SPLPR`.
- Keep runtime implementation blocked.

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

- Focused pytest contract for `C01FSARP-G1-VIRAL-001`.
- Roadmap validator.
- `git diff --check -- Sourcefold`.
- Full `Sourcefold/tests` suite before commit.
