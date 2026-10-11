# Map Schema Identity Packet - MSID-G1-VIRAL-001

Packet id: `MSID-G1-VIRAL-001`

Status: `valid_for_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-MAPSCHEMA-001`

Baseline commit: `c3bda8a8b32a87f92f23e434b9ffd5999637bedf`

Purpose: define a version-bound provisional map schema and shared identity
contract for future Viral trial `doc_map`, `content_map`, `art_map`, and
`pre_ocr_map_bundle` artifacts.

Boundary: this packet is a non-accepting schema/identity contract only. It is
not `doc_map`, `content_map`, `art_map`, `pre_ocr_map_bundle`, accepted map
evidence, accepted anchors, accepted coordinates, accepted reading order, OCR
routing, source evidence, QA, benchmark, fixture, source-profile acceptance,
translation, proofreading, renderer/profile acceptance, or implementation.

Method: derive schema and identity rules from the accepted Gate 1 protocol,
`pre_ocr_mapping_model.md`, `MBR-G1-VIRAL-001`, and Sol/Terra-reviewed forward
plan constraints. The PDF was not opened, parsed, rehashed, recounted, or
inspected. No OCR, transcription, copied text, PDF text-layer extraction,
benchmark, QA, fixture, source acceptance, translation, proofreading, or
implementation work was performed.

## Predecessor References

| Evidence | ID | SHA-256 / revision |
|---|---|---|
| Accepted protocol revision | `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a` | file blob `4d494e83d8d63dd3778a3813b3ee529449cee51a` |
| Baseline commit | `c3bda8a8b32a87f92f23e434b9ffd5999637bedf` | commit |
| Forward 10-step plan | `viral_forward_10_step_plan.md` | `4DD8BB5C7778BF660A2FECC6EE32AD6CD6CD0E5978BF512A2655ECB3B41DD64A` |
| Map-bundle prerequisite review | `MBR-G1-VIRAL-001` | `630B42491016B1013FB853A64A7ACBA03B1A15D5787C07655C9AD8F2F8BADD8E` |
| Selected-page manifest | `SPM-G1-VIRAL-001` | `73D6C817E54DDEFB89BA7109440E87F36B447F74C19044D154A0674AD41E3936` |
| Render output manifest | `RT-G1-VIRAL-RENDER-001` | `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC` |
| Visual sanity report | `VSR-G1-VIRAL-001` | `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439` |
| Page inventory report | `PIR-G1-VIRAL-001` | `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA` |
| Page map/model report | `PMR-G1-VIRAL-001` | `72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F` |
| Provisional region map report | `PRM-G1-VIRAL-001` | `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C` |

The forward plan hash is bound to the reviewed ten-step direction recorded
before this packet.

## Schema Set

Schema set id: `MSID-G1-VIRAL-SCHEMASET-v0`

Status: `version_bound_provisional`

Schemas:

- `common_map.v0`: shared artifact header, lineage, page identity, region
  identity, coordinate basis, review state, and invalidation fields.
- `doc_map.v0`: page role, region registry, page/region coverage, predecessor
  references, and exclusion/unknown records.
- `content_map.v0`: structural content candidates referencing
  `doc_map.region_id`; no copied text, OCR text, PDF text-layer content,
  trusted semantic RPG roles, or accepted routing.
- `art_map.v0`: visual/mixed/art candidates referencing `doc_map.region_id`;
  text-in-art may be recorded only as flags/zones, not transcription or
  semantic text claims.
- `pre_ocr_map_bundle.v0`: bundle index referencing exact `doc_map`,
  `content_map`, `art_map`, schema set, hash values, predecessor IDs,
  validation result, review state, and invalidation rules.

This schema set may unblock trial map construction only after review. It cannot
accept candidate evidence, freeze a bundle, authorize OCR, or advance Gate 1.

## Canonical Serialization And Hashing

Canonical serialization profile: `sourcefold-map-json-canonical-v0`

Rules:

- Canonical artifact payloads use UTF-8 JSON without BOM.
- Object keys are sorted lexicographically at every level.
- Arrays preserve authored order where order is semantically declared.
- Numbers use decimal notation without insignificant trailing zeroes.
- `null` is allowed only for fields whose schema explicitly permits it.
- Hash input is the exact canonical JSON byte stream.
- Hash algorithm is SHA-256, uppercase hexadecimal in reports and ledgers.
- Human-readable Markdown reports may summarize canonical artifacts, but their
  hashes do not replace canonical JSON hashes when JSON exists.

For this packet, Markdown is the review artifact. Future map-layer trials must
either create canonical JSON artifacts or explicitly record that the trial is
Markdown-only and cannot be consumed by a bundle freeze.

## Identity Namespaces

Namespace root: `G1-VIRAL`

Page id pattern:

- `PG-G1-VIRAL-P001` through `PG-G1-VIRAL-P020` for ordinal pages 1-20.

Trial region id pattern:

- `RG-G1-VIRAL-P{page:000}-R{region:000}`

Map artifact id patterns:

- `DM-G1-VIRAL-001` for first trial `doc_map`.
- `CM-G1-VIRAL-001` for first trial `content_map`.
- `AM-G1-VIRAL-001` for first trial `art_map`.
- `POMB-G1-VIRAL-001` for first frozen `pre_ocr_map_bundle`, if later
  authorized.

PRM provisional IDs are provenance only. They must not become stable region IDs
by copying. A future `doc_map` may map each MSID trial region ID to one or more
PRM provenance IDs, but only as `source_provenance`, not canonical identity.

## Coordinate Basis

Coordinate model id: `MSID-G1-VIRAL-COORD-v0`

- Source page range: selected ordinal pages 1-20 only.
- Render coordinate space: PNG pixel coordinates, width 2550, height 3300, from
  `RT-G1-VIRAL-RENDER-001`.
- Normalized coordinate space: `[x/W, y/H, w/W, h/H]` with values in `[0,1]`.
- Coordinate status: `trial_provisional`.
- Accepted coordinates, anchors, reading order, OCR routing, and source truth
  are out of scope.
- Any future coordinate payload must record coordinate space, render
  predecessor, page ID, region ID, observation state, and uncertainty.

## Required Artifact Header Fields

Every future map-layer artifact under this packet must carry:

- `artifact_id`
- `artifact_type`
- `schema_id`
- `schema_version`
- `status`
- `purpose`
- `authorization_id`
- `created_at`
- `actor`
- `baseline_commit`
- `accepted_protocol_revision`
- `accepted_protocol_file_blob`
- `predecessor_ids`
- `predecessor_hashes`
- `canonicalization_profile`
- `identity_namespace`
- `coordinate_model_id`
- `review_state`
- `payload_leakage_check`
- `supersession_of`
- `invalidation_rules`

Allowed statuses for map-layer trials:

- `draft`
- `valid_for_review`
- `blocked`
- `stale`
- `superseded`

No status in this packet accepts source text, accepts map layers for production,
approves OCR, advances Gate 1, or accepts the source profile.

## Payload Leakage Rules

Forbidden in pre-OCR map-layer artifacts unless a later authorization changes
the boundary:

- OCR text or OCR output under test.
- PDF text-layer content or order.
- Copied exact source text.
- Translation or proofreading output.
- Gold text or sample answers.
- Accepted reading order.
- Accepted anchors or accepted coordinates.
- Source-profile acceptance.
- QA finding conclusions outside a dedicated QA/finding authorization.
- Fixture manifests or fixture execution results.

Allowed in future map-layer trials when separately authorized:

- Page IDs, image IDs, predecessor hashes.
- Trial region IDs.
- Coarse structural classes.
- Visual/mixed/text-in-art flags.
- Unknown/ambiguous/unsupported markers.
- Provisional coordinate boxes with coordinate space and uncertainty.
- PRM provenance IDs as non-canonical provenance only.

## Bundle Preconditions

`pre_ocr_map_bundle` freeze remains blocked until all of the following exist:

- Reviewed and current `MSID-G1-VIRAL-001` or superseding schema/identity
  packet.
- Exact current `DM-G1-VIRAL-001` or successor `doc_map` hash.
- Exact current `CM-G1-VIRAL-001` or successor `content_map` hash.
- Exact current `AM-G1-VIRAL-001` or successor `art_map` hash.
- Cross-map consistency validation record with no unresolved blocking leakage,
  missing-region, duplicate-region, stale-lineage, or schema failures.
- Fresh bounded `BA-G1-VIRAL-MAPBUNDLE-001` naming bundle freeze as the exact
  action.

## Invalidation

This packet is stale if protocol revision/blob changes, baseline commit is
superseded for this lineage, `MBR-G1-VIRAL-001` changes, any listed
predecessor identity/hash changes, canonical serialization rules change,
identity namespace changes, coordinate basis changes, schema names or required
fields change, payload-leakage rules change, Sol/Terra review changes, or
authority model changes.
