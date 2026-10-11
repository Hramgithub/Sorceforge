# Goal plan: Sourcefold model handoff

- Goal ID: `20261011-sourcefold-model-handoff`
- State: `active`
- Objective: prepare a concise but operationally complete handoff package for
  a new model such as Claude Opus 5.5, publish it in the standalone repository,
  and leave the project at a safe continuation boundary.
- Policy orchestrator: main chat, `gpt-6-sol` / medium.
- Actual orchestrator model/effort: unavailable.
- Assignment state: `platform-unverified`.
- Scoped override: none.

## Ownership

| Step | Owner | Effort | State |
|---|---|---:|---|
| A1 current-state, architecture, and repository-map analysis | `gpt-6-astra` architect | high | completed |
| I1 write summary, operational spec, and onboarding prompt | main-chat orchestrator | medium | completed |
| V1 verify paths, claims, counts, links, and current revision | main-chat orchestrator | medium | completed |
| Q1 bounded handoff QA | `gpt-6-luna` QA | medium | completed |
| R1 independent release review | `gpt-6-astra` critic | high | active |
| P1 commit and publish documentation | main-chat orchestrator | medium | pending |

The critic must not implement or materially design the handoff candidate.

## Deliverables

- `docs/handoff/MODEL_HANDOFF_SUMMARY.md`: quick project orientation.
- `docs/handoff/MODEL_HANDOFF_SPEC.md`: authoritative operational and
  architectural handoff.
- `docs/handoff/NEW_MODEL_PROMPT.md`: copy-ready prompt for the receiving model.
- updated project status and links to the handoff package.
- contributor receipts and a release record for the frozen documentation
  candidate.

## Required coverage

- product purpose, non-goals, and acceptance model;
- why the product exists and what has been done;
- completed phases and current Phase 0 / Gate 1 boundary;
- repository topology and important files by reading order;
- technology stack and why each part exists;
- immutable inputs, governed evidence, authorization, and lineage rules;
- current standalone runtime gaps and inherited failing-test evidence;
- safe bootstrap, forbidden assumptions, and recommended next task;
- explicit distinction between historical evidence, current verified state,
  and future work.

## Definition of Done

- a new model can identify the product, current state, source-of-truth order,
  repository structure, and safe next action without broad repository study;
- every current-state claim is tied to live repository evidence or clearly
  labeled historical evidence;
- no candidate input, Phase 0 evidence, or old bounded acceptance is promoted
  by wording;
- all repository-relative links resolve;
- QA passes and an independent critic approves the exact candidate;
- documentation is committed and remote `main` is verified at the published
  revision.
