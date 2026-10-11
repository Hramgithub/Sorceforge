# Sourcefold Roadmap Lab

This folder contains the shared roadmap pult for Sourcefold planning.

- `roadmap.yaml` is the canonical editable data file.
- `roadmap_viewer.html` is a standalone viewer for nodes, dependencies,
  statuses, comments, and linked plan paths.
- Markdown roadmaps under `Sourcefold/docs/plans/` are narrative/reference
  snapshots. They explain why the map exists, but they are not the live
  planning pult once a node, edge, status, or comment exists in `roadmap.yaml`.

Keep node ids and edge ids stable. Codex can read the YAML directly, so comments
and status changes made there become part of the next planning turn.

When the Markdown and YAML disagree, treat `roadmap.yaml` as the operational
source of truth and either update the YAML or add an explicit comment explaining
why the narrative document is intentionally different.

Detailed evidence payloads do not belong in roadmap YAML. For example, Gate 1
pre-OCR maps are tracked by node/status/checklist/link fields in the roadmap,
while future `doc_map`, `content_map`, `art_map`, and bundle payloads must live
in dedicated evidence artifacts.

Validate roadmap changes locally before commit:

```powershell
..\..\scripts\validate_roadmap.ps1
```

From the Sourcefold root, the equivalent package command is:

```powershell
npm run validate:roadmap
```

The validator is Sourcefold-specific and uses the locked `yaml` package to
parse the roadmap before checking contract cross-references.
