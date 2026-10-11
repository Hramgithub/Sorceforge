# Press Contract

Purpose: render reader-facing projections from an accepted RU master.

## Inputs

- Proofread RU Master.
- Press profile and rendering configuration.
- Asset manifest, if assets are used.

## Outputs

- Markdown, HTML, PDF, or other declared projection.
- Rendering manifest.
- Layout QA findings.

## Boundary

Press is optional and downstream. It cannot fix or hide unresolved
reconstruction, translation, or proofreading findings.

## Acceptance Gate

Press output is accepted only as a projection of an accepted RU master and must
record any rendering-specific deviations.
