# Release record: Sourcefold model handoff

- Goal ID: `20261011-sourcefold-model-handoff`
- Release class: documentation-only model handoff
- Product acceptance effect: none
- Candidate baseline: `7c880d60320ba11c7a80f62fb804722cfac1548b`
- Reviewed candidate revision: `4d49307e18b238de10733ccbdaa05ff101574f86`
- Publication target: `origin/main`
- State: published and remotely verified

## Candidate contents

- `docs/handoff/MODEL_HANDOFF_SUMMARY.md`
- `docs/handoff/MODEL_HANDOFF_SPEC.md`
- `docs/handoff/NEW_MODEL_PROMPT.md`
- discovery links in root/project README and `PROJECT_STATUS.md`
- goal plan/context plus A1 architecture and Q1 QA receipts

No source PDF/image, governed fixture, historical report/manifest, producer,
validator, test, contract, roadmap state, authorization, or acceptance record
is changed by this release.

## Evidence

- A1 architecture receipt: `handoffs/A1-architecture-map.md`.
- Q1 bounded QA receipt: `handoffs/Q1-handoff-qa.md`, result **PASS**.
- R1 independent release receipt: `handoffs/R1-release-review.md`, exact
  candidate **APPROVED** with no findings or blockers.
- Baseline inventory independently recounted: 3987 tracked paths, 3981 under
  `Sourcefold/`.
- Local Markdown links checked: 23, missing: 0.
- Secret-pattern scan over changed documentation: no match.
- `git diff --check`: passed before candidate freeze.
- Clean `npm ci` plus `npm run validate:roadmap`: passed with 6 statuses,
  7 lanes, 26 nodes, 25 edges, and 254 documentation checkpoints.
- Generated ignored `Sourcefold/node_modules/` removed after validation.

The recorded Python full-suite result remains historical standalone-export
evidence: 989 passed, 27 skipped, 13 failed. It was not rerun or represented as
green for this documentation-only goal.

## Release boundary

This package transfers context and working constraints. It does not authorize
OCR, rendering, translation, proofreading, production assembly, a new source
package, repair of immutable lineage evidence, or a broader Gate decision.

The exact approved candidate was published by ordinary fast-forward on
2026-10-11. A fresh `ls-remote` verified `origin/main` at
`4d49307e18b238de10733ccbdaa05ff101574f86` immediately after publication.
This administrative successor adds the immutable R1 receipt and truthful goal
bookkeeping under the critic's explicit allowance; it does not mutate the
reviewed handoff documents or extend approval to product state.
