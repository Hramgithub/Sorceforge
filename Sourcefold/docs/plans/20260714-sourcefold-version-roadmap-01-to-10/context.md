# Context: Sourcefold Version Roadmap 0.1 To 1.0

Goal id: `20260714-sourcefold-version-roadmap-01-to-10`

Orchestrator: `gpt-5.5`, medium effort

Last updated: 2026-07-14

## Objective

Create a constructive version roadmap from Sourcefold Core 0.1 RC through
Sourcefold 1.0 production.

## Baseline

- Sourcefold has an initial documentation/schema scaffold.
- The current release roadmap recommends a contract-first path to
  Sourcefold Core 0.1 RC.
- First release boundary currently recommended: headless core lane,
  fixture-backed, one declared source profile, no `press`, no `bridge`, no KB,
  no UI, no Translator migration.

## Planning Question

How should Sourcefold grow from Core 0.1 RC into 1.0 production without
collapsing future capabilities into the first release or over-detailing one
module too early?

## Current Step

Version roadmap synthesized; awaiting user review.

## Handoffs

- Sol version architecture:
  `handoffs/sol-version-roadmap-20260714.md`, SHA-256
  `9C745C710D25F8C96ED09A5B20187340F3FD31737F25B89C744781E61F9FFB88`.
- Terra version critique:
  `handoffs/terra-version-roadmap-critique-20260714.md`, SHA-256
  `84319D4DA9906297D3DE4C8E727991F51C4745A62F8A3B63E0FAA1F0B39BC13C`.

## Synthesis

The version ladder should lead to Sourcefold Core 1.0 production, not a broad
platform. `press` and `bridge` are previewable optional tracks after Core is
supportable, but they are not mandatory for Core 1.0. KB and Translator
migration remain outside the 1.0 line.

## Blockers

None.

## Next Action

Review `version_roadmap.md` and decide whether to launch Phase 0.
