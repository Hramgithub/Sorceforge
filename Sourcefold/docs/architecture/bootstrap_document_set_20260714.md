# Sourcefold Bootstrap Document Set

Date: 2026-07-14

Status: proposal after Terra critique. This document defines what should be
created for the first Sourcefold scaffold. It does not mean the old `translator`
implementation has been migrated.

## Product Boundary

Sourcefold is one modular product, not three standalone products.

Core modules:

- `reconstruct`: OCR, PDF/native text extraction, layout recovery, source
  evidence and accepted source text.
- `translate`: translation units, terminology, LLM translation, structure/data
  preservation checks and faithful RU draft.
- `proofread`: semantic proofreading, Russian-language polish, issue ledger and
  accepted RU master.

Optional lanes:

- `press`: reader Markdown, HTML and PDF projections from accepted text.
- `bridge`: explicit export/integration lane.

Out of ordinary scope:

- Knowledge Base generation and cross-book rule integration. This remains a
  future/separate product direction, currently referred to as `RuleAtlas`.

## NRI Governance

Sourcefold inherits the NRI-wide operational standard from
`docs/governance/nri_goal_governance.md`. It is the first clean product to adopt
that standard from its scaffold; it does not inherit Translator governance or
historical package structure.

## Create From Scratch

These files should be created as Sourcefold-native documents, not copied from
`translator`:

```text
Sourcefold/
  AGENTS.md
  README.md
  PROJECT_STATUS.md
  .gitignore

  docs/
    architecture/
      product_boundary.md
      module_contracts.md
      role_model.md
      decision_log.md
    plans/
      README.md
    quality/
      acceptance_criteria.md
    legacy/
      translator_evidence_index.md

  contracts/
    reconstruct.md
    translate.md
    proofread.md
    press.md
    bridge.md

  manifests/
    artifact_manifest.schema.json

  fixtures/
    README.md
```

The first scaffold must explain boundaries and contracts. It must not pretend
that the legacy implementation has already been migrated.

## Adapt From Existing Context

Adapt these ideas from root `AGENTS.md` and `translator`, but rewrite them for
Sourcefold:

- immutable `Source/` and original PDFs/images;
- preservation of source layout semantics: headings, emphasis, quotes, lists,
  tables, cards/statblocks and page markers;
- traceability and provenance for source, units, translation, proofreading and
  release artifacts;
- no secrets, credentials, auth files or local environment state in commits;
- Obsidian-compatible readable Markdown where Markdown is emitted;
- structured parsers and existing reproducible tools over ad hoc text edits;
- status and context updates for multi-step goals;
- NRI-governance goal bundles, compact task packets, immutable contributor
  handoffs, and an orchestrator-owned `PROJECT_STATUS.md` rollup;
- role model: `gpt-5.5` orchestrator, Terra engineering assistant or
  independent reviewer, Sol analyst/architect, `gpt-5.4` bounded executor/QA;
- final release review by an independent Terra instance that did not own the
  implementation under review;
- artifact manifests with input/output hashes, producing stage, tool/model
  version, QA status and acceptance status.

## Source Documents To Mine

Use these current `translator` documents as source material, not as files to
copy verbatim:

| Source document | What Sourcefold should take | What must stay legacy |
|---|---|---|
| `translator/docs/architecture/translator_charter_20260713.md` | Mission, primary deliverable, canonical layers, quality model, stop rule. This should become Sourcefold `product_boundary.md` and `acceptance_criteria.md`. | The `Translator` name and any implication that Keeper/HTML/PDF are primary deliverables. |
| `translator/docs/architecture/translator_concept_review_20260713.md` | User thesis: three core stages, publishing as downstream, KB as separate future product, Viral failure lesson. This should become the rationale section for Sourcefold architecture. | Incident-specific Viral framing except as evidence in `legacy/translator_evidence_index.md`. |
| `translator/docs/architecture/product_naming_review_20260714.md` | Working name `Sourcefold`, one modular product decision, `reconstruct/translate/proofread`, optional `press/bridge`, future `RuleAtlas`. | Any public naming confidence; trademark/package/domain checks remain open. |
| `docs/governance/nri_goal_governance.md` | NRI-wide goal bundle, context ownership, handoff, recovery, critic, and release rules. Sourcefold references this standard instead of copying it. | None; this is the governing NRI standard. |
| `translator/docs/architecture/translator_role_model.md` | Historical role-boundary evidence only. | Its file structure and any Translator-specific operational assumptions. |
| `translator/README.md` | Operational examples, known reusable concepts, stage names worth evaluating, docs index patterns. | Current command surface and old file layout. These are implementation evidence, not Sourcefold contracts. |
| `translator/docs/architecture/README.md` | Architecture index pattern and legacy/current distinction. | Old explorer/version list except as historical references. |
| `translator/PROJECT_STATUS.md` | Historical lessons, accepted decisions, known failure classes and completed hardening ideas. | The file itself, backlog, package state, run history and current implementation status. |

The extraction rule is:

1. Pull principles into Sourcefold docs.
2. Pull contracts only after rewriting them in Sourcefold terms.
3. Pull code or commands only after a separate migration review.
4. Link legacy evidence instead of copying historical operational state.

## Keep As Legacy Evidence Only

Do not copy these into the first Sourcefold scaffold:

- old `translator/PROJECT_STATUS.md` history;
- historical reform plans, package logs, QA reports, browser profiles, OCR
  overlays and temporary generated artifacts;
- old file taxonomy if it mixes core text quality, publishing and KB work;
- project-specific configs, prompts or scripts tied to Viral, Wormsign,
  Desertflower, Bless, Mothers Love or a fixed output path;
- glossary/terminology decisions without provenance and applicability status;
- any script that assumes old `translator` paths as the runtime namespace.

Instead, reference them from:

```text
Sourcefold/docs/legacy/translator_evidence_index.md
```

Each legacy reference should record path, commit/revision when available, what
is useful, and what must not be inherited.

## Terra Critique Incorporated

Terra's main warning: the bootstrap package must not import the old project
shape by accident.

Accepted risks:

- Sourcefold may silently become `translator` with a new name if old publishing,
  KB and package history are copied wholesale.
- Contracts can become too abstract unless the first vertical slice uses a real
  fixture and expected output.
- `press` and `bridge` can accidentally become mandatory dependencies unless
  contracts explicitly keep them optional.
- `translate` and `proofread` can drift apart unless terminology decisions and
  semantic findings have one shared provenance model.
- Legacy links can decay unless they record stable paths and applicability.

## Recommended First Scaffold Commit

The first commit should contain documentation and schemas only:

1. Product boundary.
2. Core module contracts.
3. Role model.
4. Acceptance criteria.
5. Artifact manifest schema draft.
6. Legacy evidence index.
7. Empty fixtures README explaining how the first test fixture will be selected.

Do not migrate code in the same commit. Code migration should start only after
the module contracts and acceptance criteria are accepted.
