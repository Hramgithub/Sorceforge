# Context: Sourcefold model handoff

- Goal ID: `20261011-sourcefold-model-handoff`
- State: `active`
- Repository: `https://github.com/Hramgithub/Sorceforge.git`
- Local root: `C:\_Hobby\_work\Sorceforge`
- Product root: `Sourcefold/`
- Baseline revision: `7c880d60320ba11c7a80f62fb804722cfac1548b`
- Branch: `main`; baseline matched `origin/main` at preflight.

## Accepted constraints

- Product identity is `Sourcefold`; `Sorceforge` is only the repository slug.
- Current state is Phase 0; Gate 1 Source Profile is the active product gate.
- Candidate inputs and bounded evidence are durable but are not accepted whole
  source, production readiness, or authorization for a new book run.
- The handoff may summarize historical evidence but must not rewrite immutable
  receipts or regenerate OCR evidence.
- Current standalone limitations and inherited test failures must remain
  visible rather than being repaired inside this documentation goal.

## Current step

R1 preparation: freeze the QA-passed documentation candidate, then obtain an
independent critic decision on its exact commit before publication.

## Completed evidence

- A1 architecture map:
  `handoffs/A1-architecture-map.md`.
- A1 verified the global-active versus scoped-acceptance distinction, baseline
  counts, implemented evidence boundary, technology/runtime gaps, source-of-
  truth precedence, and the recommended read-only continuation audit.
- I1 created `docs/handoff/MODEL_HANDOFF_SUMMARY.md`,
  `MODEL_HANDOFF_SPEC.md`, and `NEW_MODEL_PROMPT.md`, then linked the package
  from the root README, project README, and current project status.
- V1 independently recounted the baseline at 3987 tracked paths: 3981 under
  `Sourcefold/`; 193 docs, 186 scripts, 179 tests, 3408 fixtures, five
  contracts, one manifest schema, and one roadmap tool. The repository entry
  set is five root-level files plus root governance under `docs/`.
- V1 checked 23 repository-relative documentation links with zero missing,
  confirmed both bounded decision IDs in current evidence, and passed
  `git diff --check`.
- A clean `npm ci` followed by `npm run validate:roadmap` passed with 6
  statuses, 7 lanes, 26 nodes, 25 edges, and 254 documentation checkpoints.
  The generated ignored `Sourcefold/node_modules/` was removed afterwards.
- Q1 bounded QA passed with no P1/P2 defect. QA independently reconciled the
  inventory, recorded test totals, global-active versus scoped-acceptance
  boundary, first-pass/P002 distinction, technology limitations, links, and
  authority language. Main chat separately verified the worktree state that
  was unavailable in the QA mount.

## Next action

Freeze a release-candidate commit, ask the independent critic to review that
exact revision, and publish only after approval plus a fresh remote check.
