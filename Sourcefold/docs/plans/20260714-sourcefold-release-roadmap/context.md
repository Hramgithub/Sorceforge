# Context: Sourcefold Release Roadmap

Goal id: `20260714-sourcefold-release-roadmap`

Orchestrator: `gpt-5.5`, medium effort

Last updated: 2026-07-14

## Objective

Create a high-level roadmap from the current Sourcefold scaffold to first
releasable product.

## Current Baseline

- Initial Sourcefold scaffold exists and was committed.
- Sourcefold is a new product, not a `translator` rename or copy.
- Core lane: `reconstruct`, `translate`, `proofread`.
- Optional lanes: `press`, `bridge`.
- Knowledge base is future separate scope.
- No real book processing has started.

## Known Pre-Implementation Gates

From Terra scaffold critique:

- acceptance-state enforcement and waiver evidence;
- artifact-level lineage and traceability anchors;
- valid stage/artifact pairs and accepted predecessor requirements;
- separation of stage acceptance, destination conformance, and release approval;
- common identifiers and formats for ledgers, provenance, and findings.

## Current Step

Roadmap synthesized; awaiting user decision in the main chat.

## Handoffs

- Sol architecture receipt:
  `handoffs/sol-roadmap-architecture-20260714.md`, SHA-256
  `B0092EA96740DF45FC2238E833463CD2EAA8EBADE8846515DA40E94D18EAC628`.
- Terra risk critique receipt:
  `handoffs/terra-roadmap-risk-critique-20260714.md`, SHA-256
  `759002D8DA17894D94C082AA58560D2511F51A70E47B96ED086DA00D93F9C868`.

## Roadmap Synthesis

The recommended release path is contract-first and core-only:

1. Release charter and contract decisions.
2. Executable contract and evidence spine.
3. Thin end-to-end `reconstruct -> translate -> proofread` flow.
4. Quality completion for the supported source profile.
5. Operator hardening.
6. Candidate freeze and independent Terra release review.

First release boundary: headless Sourcefold Core 0.1 RC for one declared source
profile and supported structure subset. Exclude `press`, `bridge`, knowledge
base generation, broad PDF/OCR promises, UI, and Translator compatibility.

## Blockers

None.

## Next Action

Ask the user whether to launch Phase 0 as the next bundled goal or revise the
release boundary first.
