# Roadmap Validator Plan

Goal id: `20260715-sourcefold-roadmap-validator`

## Objective

Add a local package-backed validator for `docs/roadmap/roadmap.yaml` and wire
it into the documentation checkpoint workflow.

## Scope

In scope:

- Sourcefold-specific roadmap YAML contract validation using the `yaml` package;
- node, edge, lane, status, linked-plan, and checkpoint reference checks;
- checkpoint-script integration;
- documentation updates.

Out of scope:

- generic schema framework adoption;
- pip dependency installation;
- roadmap status changes;
- module implementation.

## Steps

| Step | Status | Evidence |
|---|---|---|
| Inspect current roadmap YAML shape | completed | package parser selected |
| Add validator package/script | completed | `package.json`, `tools/roadmap-validator/validate-roadmap.mjs`, `scripts/validate_roadmap.ps1` |
| Wire checkpoint script to validator | completed | `scripts/documentation_checkpoint.ps1` |
| Document usage | completed | README/plans/quality/roadmap docs |
| Verify validator and checkpoint dry-run | completed | npm validator pass, wrapper pass, checkpoint dry-run output |

## Handoff Evidence

No subagent handoff is required for this narrow tooling update.


## Documentation Checkpoint: doc-checkpoint-20260714T214751Z

- Created: 2026-07-14T21:47:51Z
- Type: documentation
- Summary: Added package-backed roadmap validator.

Completed:
- Added Sourcefold package.json and package-lock.json with yaml dependency
- Added Node roadmap validator and PowerShell wrapper
- Wired documentation checkpoint script to roadmap validation

Next:
- Run npm run validate:roadmap before roadmap commits

Blockers:
- No blockers supplied.

Roadmap nodes:
- phase-0

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260714T215213Z

- Created: 2026-07-14T21:52:13Z
- Type: documentation
- Summary: Updated documentation before committing package-backed roadmap validator.

Completed:
- Added package-backed roadmap validator tooling
- Added Sourcefold setup documentation
- Codified reproducibility-first tooling and environment documentation rules

Next:
- Use npm ci and npm run validate:roadmap for roadmap validation

Blockers:
- No blockers supplied.

Roadmap nodes:
- phase-0

Accepted decisions:
- No accepted decisions supplied.
