# Bridge Contract

Purpose: export accepted Sourcefold artifacts to explicit external systems.

## Inputs

- Accepted upstream artifact.
- Destination contract and transform configuration.
- Compatibility assumptions and version metadata.

## Outputs

- Exported artifact or package.
- Export manifest.
- Lossy mapping or compatibility findings.

## Boundary

Bridge is optional. It does not create source, translation, proofreading, or
release acceptance by itself.

## Acceptance Gate

Bridge output is accepted only when the destination contract is satisfied and
lossy transformations are documented.
