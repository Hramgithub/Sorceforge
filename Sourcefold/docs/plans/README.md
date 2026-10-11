# Sourcefold Plans

Sourcefold goal bundles follow
`../../../docs/governance/nri_goal_governance.md`.

Each bundled goal uses:

```text
docs/plans/<goal-id>/
  plan.md
  context.md
  handoffs/
  release.md
```

`PROJECT_STATUS.md` is the project rollup. `plan.md` records steps and evidence.
`context.md` is the orchestrator-owned checkpoint. `handoffs/` contains
immutable contributor receipts.

Use goal ids in the form `YYYYMMDD-kebab-slug`.

## Documentation Checkpoint Command

When the user says `обнови документацию`, `зафиксируй документацию`,
`обнови статус`, or `зафиксируй статус`, treat it as a Sourcefold
documentation checkpoint request.

Use `scripts/documentation_checkpoint.ps1` from the Sourcefold root. Dry-run is
the default and must be used first when the expected update scope is unclear:

```powershell
.\scripts\documentation_checkpoint.ps1 `
  -GoalId 20260715-sourcefold-doc-checkpoint-command `
  -Summary "Checkpoint summary"
```

Apply mode writes the checkpoint:

```powershell
.\scripts\documentation_checkpoint.ps1 `
  -GoalId 20260715-sourcefold-doc-checkpoint-command `
  -Summary "Checkpoint summary" `
  -Completed "Updated plan/context" `
  -Next "Review pending decisions" `
  -RoadmapNode "phase-0" `
  -Apply
```

The script updates:

- `PROJECT_STATUS.md`;
- the selected goal `plan.md`;
- the selected goal `context.md`;
- `docs/roadmap/roadmap.yaml` as the canonical roadmap checkpoint ledger;
- `docs/architecture/decision_log.md` only when accepted decisions are supplied.

The script runs `scripts/validate_roadmap.ps1` before dry-run/apply and again
after apply. Use `-SkipRoadmapValidation` only for a narrow repair task where
the roadmap is already known to be temporarily invalid.

The script does not commit, push, change module contracts, or infer accepted
decisions. Roadmap node statuses still require explicit user/orchestrator input.

## Roadmap Validation

Validate the canonical roadmap before committing roadmap or checkpoint changes:

```powershell
.\scripts\validate_roadmap.ps1
```

Or run the package command directly:

```powershell
npm run validate:roadmap
```

The validator is Sourcefold-specific and package-backed through `package.json`
and `package-lock.json`. It uses the `yaml` package for parsing, then checks
required top-level keys, lanes, statuses, unique ids, node linked plans, edge
endpoints, checkpoint goal plans, and `source_policy` paths.

When a checkpoint installs or changes project tooling, update `SETUP.md` and
the relevant docs/status with what changed, why it is needed, and how to
reproduce it.
