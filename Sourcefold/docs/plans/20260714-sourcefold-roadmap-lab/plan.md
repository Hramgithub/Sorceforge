# Plan: Sourcefold Roadmap Lab

Goal id: `20260714-sourcefold-roadmap-lab`

State: completed

Owner: `gpt-5.5` orchestrator, medium effort

## Objective

Create a first shared roadmap viewer and canonical roadmap data file so the
user and Codex can discuss Sourcefold phases, dependencies, statuses, comments,
and linked plans through one inspectable artifact.

## Steps

| Step | Owner | Status | Evidence | Next action |
|---|---|---|---|---|
| L1 Read current roadmap baseline | Orchestrator | completed | Sourcefold status, release roadmap, version roadmap. | Create data/viewer. |
| L2 Create canonical roadmap data | Orchestrator | completed | `docs/roadmap/roadmap.yaml`. | Add nodes, edges, comments, linked plans. |
| L3 Create interactive viewer | Orchestrator | completed | `docs/roadmap/roadmap_viewer.html`. | Expose IDs, status, dependencies, comments. |
| L4 Verify local file set | Orchestrator | completed | File reads, scoped git status, Node syntax check for viewer script. | Report usage. |

## Definition Of Done

- `roadmap.yaml` contains node ids, edge ids, comments, statuses, and linked
  plan paths.
- `roadmap_viewer.html` renders the roadmap and exposes the same identifiers.
- The viewer is usable as a first collaborative pult, not a production app.
- No module implementation or Sourcefold processing starts.

Result: first Roadmap Lab iteration created.

## Notes

The viewer is allowed to be a first iteration. The canonical data model should
stay simple enough for direct YAML editing.

## Update: Zoom And Step Detail

Added after first review:

- zoom selector at 85%, 100%, 125%, 150%, and 200%;
- per-node `details` in `roadmap.yaml`;
- viewer sections for `What enters`, `What exits`, `Gate`, and `Evidence`;
- built-in detail fallback so the viewer still shows details when opened
  without loading the YAML file.

## Update: Canonical YAML And Decision Layer

Added after roadmap review:

- `source_policy` clarifies that `roadmap.yaml` is the operational source of
  truth and Markdown roadmaps are narrative/reference snapshots;
- decision nodes for 0.1 source profile, canonical formats, acceptance
  authority, artifact identity, trace anchors, and waiver policy;
- `readiness`, `owners`, `fixtures`, and `evidence_checklist` fields;
- parking lane for post-1.0 topics: broader OCR/source profiles, KB/RuleAtlas,
  UI/hosted service, Translator migration, and destination catalogue;
- viewer sections for readiness, owners, fixtures, and evidence checklist.
