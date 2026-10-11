# Sourcefold

Sourcefold is a new NRI product for turning immutable source material into an
accepted Russian text master through three core contracts:

1. `reconstruct`: establish accepted source text from source evidence.
2. `translate`: create a faithful RU draft while preserving meaning, structure,
   and data.
3. `proofread`: accept the reader-ready RU master without changing source
   meaning or data.

Optional lanes consume accepted text:

- `press`: Markdown, HTML, and PDF projections.
- `bridge`: explicit exports and integrations.

Knowledge base generation is a separate future direction, not a normal
Sourcefold processing lane.

Sourcefold is stored as a nested directory in the standalone `Sorceforge`
repository because canonical roadmap and evidence paths begin with
`Sourcefold/`. Run project commands from this directory.

## Project contents

- `docs/architecture/`: product boundary, module contracts, role model, and
  decisions.
- `contracts/`: module and authorization contracts.
- `docs/quality/`: acceptance criteria for source, translation, proofreading,
  optional projections, and integration outputs.
- `docs/legacy/`: index of legacy `translator` evidence and what must not be
  inherited.
- `docs/plans/`: governed plans, context checkpoints, and handoff receipts.
- `docs/roadmap/`: canonical roadmap YAML and its reader.
- `fixtures/`: governed candidate inputs and bounded-run evidence. These are
  durable project artifacts, not disposable test output.
- `manifests/`: artifact manifest definitions.
- `scripts/`: validation, contract, reconstruction, and bounded probe tools.
- `tests/`: executable contract and pipeline checks.
- `tools/roadmap-validator/`: package-backed roadmap validator.
- `scripts/documentation_checkpoint.ps1`: dry-run/apply helper for keeping
  project status, goal plan/context, and roadmap checkpoint evidence in sync.
- `package.json` / `package-lock.json`: reproducible Node dev-tool package.
- `scripts/validate_roadmap.ps1`: Windows-friendly wrapper for the
  package-backed roadmap YAML validator.

## Development Tools

See `SETUP.md` for environment setup rationale and reproducibility notes.

Install locked tool dependencies from the Sourcefold root:

```powershell
npm ci
npm run validate:roadmap
python -B -m pytest -p no:cacheprovider
```

Validate the canonical roadmap:

```powershell
npm run validate:roadmap
```

On Windows, the equivalent wrapper is:

```powershell
.\scripts\validate_roadmap.ps1
```

Sourcefold is currently in Phase 0. Candidate evidence and probe results do not
establish a production-ready pipeline, whole-book acceptance, or permission to
process new source material.

## Model handoff

For a new model or maintainer, start with:

- `docs/handoff/MODEL_HANDOFF_SUMMARY.md`;
- `docs/handoff/MODEL_HANDOFF_SPEC.md`;
- `docs/handoff/NEW_MODEL_PROMPT.md`.

The handoff distinguishes the active global Phase 0/Gate 1 roadmap from exact
bounded acceptance records and documents the current standalone runtime/test
limitations.
