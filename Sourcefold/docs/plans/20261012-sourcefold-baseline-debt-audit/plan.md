# Goal plan: Sourcefold baseline debt and continuation audit

- Goal ID: `20261012-sourcefold-baseline-debt-audit`
- State: `paused` (2026-10-13: user switched to an idea-vs-implementation audit; packet v3 kept as reference)
- Objective: produce a read-only decision packet that explains the 13 failing
  tests of the standalone baseline, proposes a portable OCR runtime binding and
  a Python dependency declaration, and names one next bounded implementation
  task. Source: `docs/handoff/MODEL_HANDOFF_SPEC.md` §14.
- Baseline revision: `98c2404ca894546326fc2f5b03d6db932e8d92bf` (`main`,
  equal to `origin/main` at preflight).
- Role contract: `docs/governance/nri_goal_governance.md` (root).
- Policy orchestrator: main chat, `gpt-6-sol` / medium.
- Actual orchestrator: Claude Opus 5.5 (`claude-opus-5-5`), effort
  unavailable.
- Assignment state: `user-overridden`.
- Scoped override (user, 2026-10-12, this goal only): the independent critic
  is a separate Claude Opus 5.5 subagent instead of `gpt-6-astra`. The critic
  must not have designed or written the audit packet.

## User decisions (2026-10-12)

1. Task: the read-only baseline debt and continuation audit.
2. A goal bundle may be created.
3. pytest may be run for diagnosis.
4. Independent critic: Claude Opus 5.5.
5. Whether active producer scripts with `D:\NRI` paths may later change:
   delegated to the orchestrator as a recommendation inside the packet; no
   script is changed by this goal.
6. Python dependency format: reuse the KB Creator decision
   (`kb_creator/docs/plans/20261011-standalone-hardening/decisions.md` D4/D6).

## Steps

| Step | Owner | Effort | State |
|---|---|---:|---|
| S1 goal bundle and preflight | orchestrator | medium | completed |
| S2 isolated pytest run in a scratch clone; list failing node IDs | orchestrator | medium | completed |
| S3 per-failure trace: asserted path, expected/actual SHA-256, earliest mismatching predecessor, successor, classification | orchestrator | medium | completed |
| S4 Tesseract-dependent failure and runtime binding proposal | orchestrator | medium | completed |
| S5 Python dependency declaration proposal | orchestrator | medium | completed |
| S6 lane map and one next bounded implementation task | orchestrator | medium | completed |
| R1 independent critic review of the packet (v1) | Claude Opus 5.5 subagent (override) | high | completed: NOT OK (P1-1 scope) |
| S7 v2: full-scope identity scan and T1 rework | orchestrator | medium | completed |
| R1b critic re-review (v2) | same critic | high | completed: NOT OK (P1-A reverse TSV class) |
| S8 v3: reverse class, F9, T1b, nits | orchestrator | medium | completed |
| R1c critic re-review (v3) | same critic | high | completed: OK (P3 nits E–H applied) |

## Forbidden scope

- No OCR, render, PDF parsing, translation, proofreading, or production run.
- No change to fixtures, reports, manifests, receipts, expected hashes, tests,
  or producer scripts.
- No acceptance-state change; no fixture admission; no page 021+.
- Tests run only in an isolated scratch clone, never in this working tree.
- No commit or push without an explicit user request.

## Deliverables

- `audit.md`: the decision packet (failure table, classification, runtime
  binding proposal, dependency proposal, lane map, next task).
- `handoffs/R1-critic-review.md`, `handoffs/R1b-critic-rereview.md`,
  `handoffs/R1c-critic-rereview.md`: independent critic receipts.
- `evidence/`: reproducible audit scripts and their outputs.

## Definition of Done

- all 13 failures are listed by node ID with evidence paths and hashes;
- every classification is backed by a recomputed hash or a cited record;
- the full suite is not described as green;
- the runtime proposal fails closed on a missing or mismatched executable or
  language data;
- `git status` shows no change outside this goal folder and the status index
  row;
- the critic returns OK, or its blockers are fixed and re-reviewed.
