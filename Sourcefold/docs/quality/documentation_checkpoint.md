# Documentation Checkpoint

Sourcefold uses a script-backed checkpoint for project documentation/status
sync. The command is intentionally narrow: it records the current planning
state, but it does not make product decisions by itself.

## Trigger Phrases

- `обнови документацию`
- `зафиксируй документацию`
- `обнови статус`
- `зафиксируй статус`

## Required Behavior

1. Prefer reproducible package/tool setup over custom parsing or ad hoc logic.
2. Prefer checked-in scripts over manual status/documentation edits.
3. Run `scripts\validate_roadmap.ps1` before changing roadmap/checkpoint data.
4. Run `scripts/documentation_checkpoint.ps1` without `-Apply` first unless the
   update payload is already explicit.
5. Confirm the target files and selected goal id.
6. Run again with `-Apply` only after the payload is clear.
7. Report changed files and pending manual updates.
8. Commit only when the user explicitly asks for a commit.

`documentation_checkpoint.ps1` also runs `validate_roadmap.ps1` before dry-run,
before apply, and after apply unless `-SkipRoadmapValidation` is supplied for a
narrow repair task.

## Durable Targets

| Target | Purpose |
|---|---|
| `PROJECT_STATUS.md` | Human project rollup and checkpoint index. |
| `docs/plans/<goal-id>/plan.md` | Goal progress and evidence note. |
| `docs/plans/<goal-id>/context.md` | Orchestrator-owned continuation context. |
| `docs/roadmap/roadmap.yaml` | Canonical roadmap/checkpoint ledger. |
| `docs/architecture/decision_log.md` | Accepted decisions only. |

## Roadmap Validator

Use `scripts\validate_roadmap.ps1` for local validation of the canonical
roadmap. It uses the Sourcefold Node dev-tool package and the locked `yaml`
dependency, so validation does not depend on browser/CDN state.

This follows the Sourcefold tooling hierarchy:

1. package-backed, locked, reproducible tools;
2. checked-in wrappers/scripts that call those tools;
3. manual action only when neither is available, with evidence recorded.

When a checkpoint installs or changes tooling, update `SETUP.md` and the
relevant project docs/status with what changed, why it is needed, and how to
reproduce it on another machine.

The validator checks:

- required roadmap keys;
- indentation hygiene;
- lane, node, edge, status, and checkpoint id uniqueness;
- node lane/status references;
- edge endpoint/status references;
- linked plan and checkpoint goal-plan paths;
- `source_policy` paths.

## Non-Goals

- No automatic commits.
- No hidden roadmap status changes.
- No architecture expansion without explicit decision.
- No recursive workspace scans.
- No migration of legacy `translator` history or governance.
