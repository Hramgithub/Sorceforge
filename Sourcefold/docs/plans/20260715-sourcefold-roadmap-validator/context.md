# Roadmap Validator Context

Sourcefold now has a local package-backed validator for
`docs/roadmap/roadmap.yaml`. The viewer can parse YAML in the browser, but
development validation must be reproducible from the repository.

## Design

The validator is Sourcefold-specific. It uses the locked `yaml` npm package for
parsing and checks semantic references:

- required top-level keys;
- indentation hygiene;
- status values;
- unique lane, node, edge, and checkpoint ids;
- node lane/status references;
- node linked-plan paths;
- edge endpoint/status references;
- checkpoint goal-plan references;
- `source_policy` file paths.

## Boundary

This is not a full schema framework. If Sourcefold later needs JSON Schema or a
broader validation layer, add an explicit validator package and record the
dependency decision.

## Tooling Rule Captured

The validator goal established the Sourcefold tooling hierarchy:

1. Prefer installed/package-backed tools with lockfiles or explicit config.
2. Prefer checked-in scripts/wrappers over manual repeated actions.
3. Treat manual actions as narrow repair/exploration steps that must leave
   durable evidence.
4. When tooling changes, update setup/docs/status with what changed, why it is
   needed, and how to reproduce it.

This is why the initial custom PowerShell parser was replaced by the locked
Node `yaml` package and a thin PowerShell wrapper.

## Verification

- `npm run validate:roadmap` passes on the current roadmap.
- `scripts/validate_roadmap.ps1` wrapper passes on the current roadmap.
- It reports 6 statuses, 5 lanes, 22 nodes, 24 edges, and 2 documentation
  checkpoints.
- `package-lock.json` pins `yaml` 2.9.0 for reproducible installs via `npm ci`.
- `SETUP.md` records what was installed, why, and how to reproduce it.
- `scripts/documentation_checkpoint.ps1` dry-run works with roadmap validation
  enabled.


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
