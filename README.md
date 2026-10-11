# Sorceforge repository

This repository contains **Sourcefold**, the product for reconstructing,
translating, and proofreading source publications. `Sorceforge` is the GitHub
repository slug supplied for this standalone extraction; it does not rename the
product.

The project intentionally remains under `Sourcefold/`. Its roadmap, evidence,
and validation contracts use canonical paths beginning with `Sourcefold/`, so
flattening the tree would break traceability and require a broad migration.

## Start here

```powershell
cd Sourcefold
npm ci
npm run validate:roadmap
python -B -m pytest -p no:cacheprovider
```

Read these files before changing the project:

- `Sourcefold/docs/handoff/MODEL_HANDOFF_SUMMARY.md` — quick orientation for a
  new model or maintainer;
- `Sourcefold/docs/handoff/MODEL_HANDOFF_SPEC.md` — operational handoff and
  safe continuation contract;
- `Sourcefold/AGENTS.md` — project rules and current gate constraints;
- `Sourcefold/README.md` — project structure and development entry points;
- `Sourcefold/PROJECT_STATUS.md` — current Phase 0 state;
- `Sourcefold/SETUP.md` — reproducible tooling and known environment gaps;
- `docs/governance/nri_goal_governance.md` — bundled-goal governance;
- `NRI_OCR_LAYOUT_RULES.md` — shared layout-preservation rules.

## Import boundary

The initial standalone snapshot was materialized from the tracked `Sourcefold/`
subtree of NRI commit `22fafc14942e925b2e5f088f3c7ab1cd8efe3003`.
Governed fixtures, candidate inputs, and bounded-run evidence are retained on
purpose. Local caches, dependency folders, credentials, browser profiles,
temporary logs, and unrelated NRI projects are not part of the repository.

Sourcefold is still in Phase 0. The presence of candidate evidence does not
mean that a whole-book workflow or production release has been accepted.
