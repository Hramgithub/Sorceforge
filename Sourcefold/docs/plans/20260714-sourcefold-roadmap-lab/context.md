# Context: Sourcefold Roadmap Lab

Goal id: `20260714-sourcefold-roadmap-lab`

Orchestrator: `gpt-5.5`, medium effort

Last updated: 2026-07-14

## Objective

Create a shared visual roadmap tool that keeps Sourcefold roadmap identifiers
visible and inspectable in code.

## Baseline

- The initial Sourcefold scaffold exists.
- Release roadmap and version roadmap artifacts exist.
- The user wants a shared tool where roadmap nodes, edges, comments, statuses,
  and linked plans are visible and can later be edited directly as YAML.

## Current Step

Roadmap Lab created.

## Blockers

None.

## Next Action

Review the viewer and decide whether to evolve it into the canonical planning
pult before Phase 0 starts.

## Created Files

- `Sourcefold/docs/roadmap/roadmap.yaml`
- `Sourcefold/docs/roadmap/roadmap_viewer.html`
- `Sourcefold/docs/roadmap/README.md`

## Updated Behavior

- Viewer supports zoom levels.
- Each node now has detailed entry, exit, gate, and evidence fields.
- The detail panel exposes those fields alongside `node_id`, `status`,
  `linked_plan`, expectations, and comments.
- `roadmap.yaml` is explicitly marked as the operational source of truth;
  Markdown roadmap files are reference snapshots.
- Decision nodes and post-1.0 parking nodes are now part of the map.
- The viewer exposes readiness, owners, fixtures, and evidence checklist fields.

## Verification

- Viewer script passed `node --check`.
- Roadmap data exposes node ids, edge ids, statuses, comments, and linked plan
  paths.
- `roadmap.yaml` contains a `details` block for every node.
