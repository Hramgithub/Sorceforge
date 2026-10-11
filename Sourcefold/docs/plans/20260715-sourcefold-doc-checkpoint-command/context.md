# Documentation Checkpoint Command Context

Sourcefold now has a script-backed documentation checkpoint command.

## Current Contract

The user may say `РѕР±РЅРѕРІРё РґРѕРєСѓРјРµРЅС‚Р°С†РёСЋ`, `Р·Р°С„РёРєСЃРёСЂСѓР№ РґРѕРєСѓРјРµРЅС‚Р°С†РёСЋ`,
`РѕР±РЅРѕРІРё СЃС‚Р°С‚СѓСЃ`, or `Р·Р°С„РёРєСЃРёСЂСѓР№ СЃС‚Р°С‚СѓСЃ`.

The orchestrator should use `scripts/documentation_checkpoint.ps1`.

Default behavior is dry-run. `-Apply` appends durable checkpoint evidence to:

- `PROJECT_STATUS.md`;
- the selected goal `plan.md`;
- the selected goal `context.md`;
- `docs/roadmap/roadmap.yaml`;
- `docs/architecture/decision_log.md` only when `-Decision` is supplied.

## Important Boundaries

- The script does not commit.
- The script does not infer accepted decisions.
- The script does not automatically change roadmap node statuses.
- `roadmap.yaml` remains the canonical roadmap/checkpoint data file.

## Verification

- PowerShell parser validation passed.
- Dry-run output lists target files, goal id, checkpoint id, payload counts, and
  roadmap nodes.
- Apply mode wrote the first checkpoint evidence to project rollup, goal
  plan/context, and `roadmap.yaml`.


## Documentation Checkpoint: doc-checkpoint-20260714T213650Z

- Created: 2026-07-14T21:36:50Z
- Type: documentation
- Summary: Added script-backed documentation checkpoint command.

Completed:
- Added scripts/documentation_checkpoint.ps1

Next:
- Use dry-run before future documentation/status checkpoints

Blockers:
- No blockers supplied.

Roadmap nodes:
- phase-0

Accepted decisions:
- No accepted decisions supplied.
