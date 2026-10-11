# Artifact Lineage Model

Status: draft for Phase 0 decision

## Artifact Types

| Type | Stage | Description |
|---|---|---|
| `source_pdf` | input | Immutable root PDF evidence. |
| `page_image_set` | reconstruct | Rendered page screenshots/images used as working visual evidence. |
| `layout_map` | reconstruct | Page regions, columns, bands, geometry, and provisional order. |
| `ocr_observation_set` | reconstruct | Raw/canonical OCR observations with coordinates, confidence, and tool identity. |
| `pdf_text_comparison` | reconstruct | Optional PDF text-layer comparison artifact; findings only. |
| `ordered_source_blocks` | reconstruct | OCR/layout blocks after reading-order reconstruction. |
| `source_text_candidate` | reconstruct | Candidate canonical source text before human acceptance. |
| `accepted_source_text` | reconstruct | Canonical source text accepted for translation. |
| `faithful_ru_draft` | translate | Russian draft preserving source meaning, structure, and data. |
| `proofread_ru_master` | proofread | Accepted Russian master for downstream optional lanes. |
| `finding_ledger` | any | Findings attached to artifact/stage/anchor. |
| `waiver_ledger` | any | Authorized unresolved findings. |
| `acceptance_record` | any | Human acceptance receipt for a stage artifact. |
| `trace_map` | any | Mapping between source anchors and derived anchors. |
| `overlay_qa_record` | reconstruct | Visual/content/order QA record binding page images to source blocks. |

## Identity Fields

Every durable artifact should have:

- `artifact_id`;
- `artifact_type`;
- `stage`;
- `schema_version`;
- `created_at`;
- `created_by`;
- `content_hash`;
- `hash_algorithm`;
- `canonicalization_method`;
- `predecessors`;
- `source_profile`;
- `run_id`;
- `config_id`;
- `tool_versions`;
- `status`;
- `supersedes` when applicable.

## DAG Rules

| From | To | Rule |
|---|---|---|
| `source_pdf` | `page_image_set` | renderer creates page images from immutable PDF. |
| `page_image_set` | `layout_map` | layout profile maps visual regions and columns. |
| `layout_map` | `ocr_observation_set` | OCR runs on declared page regions. |
| `source_pdf` | `pdf_text_comparison` | optional comparison-only branch; not canonical source text. |
| `ocr_observation_set` | `ordered_source_blocks` | reading-order reconstruction sequences OCR/layout blocks. |
| `ordered_source_blocks` | `source_text_candidate` | source candidate is normalized from ordered OCR blocks. |
| `source_text_candidate` | `accepted_source_text` | human acceptance binds exact candidate hash after QA/finding closure. |
| `accepted_source_text` | `faithful_ru_draft` | translate requires an accepted source predecessor. |
| `faithful_ru_draft` | `proofread_ru_master` | proofread requires an accepted faithful draft predecessor. |
| `proofread_ru_master` | `press`/`bridge` outputs | optional lanes may consume only accepted RU master. |

Invalid:

- draft from unaccepted source;
- accepted source text directly from PDF text layer;
- accepted source text without page-image evidence;
- accepted source text without reading-order QA;
- proofread master from stale draft;
- acceptance record whose artifact hash does not match current content;
- waiver attached to unknown finding or missing authority;
- release candidate with mutable or missing manifest.

## Trace Anchors

Proposed 0.1 anchor stack:

- `source_page_id`;
- `page_image_id`;
- `region_id`;
- `ocr_observation_id`;
- `reading_order_id`;
- `source_block_id`;
- `source_span` when available;
- `derived_block_id`;
- optional `text_hash` per block.

Anchors must be stable enough to survive translation/proofread reruns and
specific enough to route findings backward.

## Supersession

When a predecessor changes:

- descendant artifacts become `stale` until revalidated or regenerated;
- new artifacts receive new ids/hashes;
- previous accepted artifacts remain historical evidence but cannot be treated
  as current;
- acceptance records bind to exact artifact ids and hashes.

## Pending Identity Decisions

- Hash algorithm and canonicalization method.
- Artifact id format.
- Run/config/tool identity boundary.
- Whether trace maps are separate artifacts or embedded ledgers.
- How many predecessors each artifact type may have in 0.1.
