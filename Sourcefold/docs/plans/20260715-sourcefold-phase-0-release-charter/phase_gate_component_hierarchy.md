# Phase/Gate/Component Hierarchy

Status: draft governed model

Purpose: make Sourcefold planning navigable and auditable at a stable
resolution:

```text
Phase -> Gate -> Component -> Subcomponent -> Parameter -> Evidence
```

This document details the current decision:

```text
Phase 0 -> Gate 01 -> Source Profile -> subcomponents -> parameters
```

It does not approve implementation. Gate 1 remains blocked until the user
accepts the decision record or parks unresolved parameters.

## Controlled Levels

| Level | Meaning | Current Example |
|---|---|---|
| Phase | Release lifecycle boundary. | `P0` Phase 0 release contract. |
| Gate | Auditable decision/exit point inside a phase. | `P0.G01` Source Profile gate. |
| Component | Product responsibility inside a gate. | `C-SOURCE_PROFILE`. |
| Subcomponent | Replaceable unit inside the component. | `SC-RENDER`, `SC-OCR`. |
| Parameter | Concrete value, rule, branch, or constraint. | `P-RESOLUTION_DPI`. |

## Record Fields

Every parameter record must carry these fields before it can be accepted:

| Field | Required Meaning |
|---|---|
| `hierarchy_id` | Stable semantic ID, e.g. `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-RESOLUTION_DPI`. |
| `parent_id` | Stable parent chain. |
| `decision_status` | `captured`, `proposed`, `evidence_gated`, `pending_approval`, `accepted`, `parked`, `rejected`, or `superseded`. |
| `evidence_status` | `missing`, `partial`, `satisfied`, or `stale`. |
| `candidate_value` | Current proposed value or candidate range. |
| `selected_value` | Final value after acceptance; blank until accepted. |
| `measurement_method` | How the value will be qualified or checked. |
| `decision_evidence` | Evidence required for the decision itself. |
| `runtime_evidence` | Evidence expected during execution. |
| `owner` | Role responsible for resolving the parameter. |
| `approver` | Role allowed to accept it. |
| `failure_behavior` | What happens when runtime evidence violates it. |
| `waiver_class` | Whether violations are waivable. |
| `roadmap_refs` | Linked roadmap nodes. |
| `acceptance_refs` | Linked acceptance matrix IDs. |
| `invalidation_conditions` | What reopens or stales the decision. |

Roll-up rule: a gate, component, or subcomponent cannot be `accepted` while any
required descendant is still `captured`, `proposed`, `evidence_gated`, or
`pending_approval`.

## Phase 0 / Gate 01 Summary

| Field | Value |
|---|---|
| `phase_id` | `P0` |
| `phase_name` | Release Charter And Contract Decisions |
| `gate_id` | `P0.G01` |
| `gate_name` | Lock OCR-first Source Profile |
| `component_id` | `P0.G01.C-SOURCE_PROFILE` |
| `roadmap_refs` | `phase-0`, `decision-source-profile-0.1` |
| `status` | `pending_approval` |
| `approver` | user |
| `primary_question` | What exactly is the first supported Sourcefold 0.1 input and acquisition chain? |
| `implementation_effect` | Blocks Core 0.1 implementation authorization until accepted or explicitly parked. |

## Gate 01 Components

| Subcomponent | Purpose | Current Status |
|---|---|---|
| `SC-INPUT` | Profile and input envelope. | pending approval |
| `SC-RENDER` | Page-image evidence and render qualification. | evidence-gated |
| `SC-MAP` | Pre-OCR doc/content/art map model and bundle authority. | proposed |
| `SC-PAGE_MAP_READINESS` | Reusable per-page readiness pipeline and profiles before page-complete review. | planned |
| `SC-OCR` | OCR authority and PDF text-layer branch. | pending approval |
| `SC-LAYOUT` | Supported geometry and reading-order boundary. | evidence-gated |
| `SC-STRUCTURE` | RPG structure boundary and fallback. | evidence-gated |
| `SC-CONTROL` | Profile identity, failure behavior, and invalidation. | proposed |

## Parameter Register

### `SC-INPUT`: Profile And Input Envelope

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-PROFILE_KIND` | `constrained_ocr_first_rpg_pdf` | pending approval | decision record | profile mismatch blocks intake; non-waivable |
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-ACTIVE_PROFILE_COUNT` | exactly one Core 0.1 source profile | proposed | release charter decision | additional profile blocks 0.1 claim |
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-DOCUMENT_COUNT` | one source PDF | proposed | `source_pdf` manifest | extra/missing source blocks intake |
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-MEDIA_TYPE` | PDF only | pending approval | positive fixture and intake validation | non-PDF rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-IMMUTABLE_ROOT` | hash-bound immutable root evidence | pending approval | source hash and identity record | mutation invalidates descendants |
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-ENCRYPTION` | unencrypted PDF | proposed | intake validation | encrypted source parked unless separately accepted |
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-PILOT_RANGE` | first 20 pages of `Вирал` candidate | evidence-gated | already recorded candidate PDF hash reference, exact `accepted_protocol`, distinct bounded selected-page-manifest authorization, selected-page manifest | cannot qualify before exact protocol acceptance plus bounded intake/manifest authorization |
| `P0.G01.C-SOURCE_PROFILE.SC-INPUT.P-RIGHTS_ATTESTATION` | operator confirms rights/redaction status | proposed | operator attestation | blocks pilot acceptance |

### `SC-RENDER`: Page-Image Evidence

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-RENDER_BEFORE_OCR` | page images required before OCR | pending approval | decision record and positive fixture | OCR from PDF directly is rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-COVERAGE` | every selected PDF page renders exactly once | proposed | page-image mapping | missing/duplicate page blocks OCR |
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-RENDERER_IDENTITY` | renderer and config pinned | evidence-gated | run record with version/config | renderer drift stales descendants |
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-CONTAINER_FORMAT` | benchmark candidates: PNG/TIFF/other lossless | evidence-gated | deterministic decode and tool compatibility | not accepted until benchmarked |
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-RESOLUTION_DPI` | benchmark candidates: 300/400/600 or pilot-driven range | evidence-gated | OCR/overlay comparison on identical regions | not accepted until benchmarked |
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-COLOR_MODE` | benchmark candidates: source-preserving color and OCR derivatives | evidence-gated | low-contrast/callout/background comparison | canonical visual and OCR derivative must remain distinct |
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-PREPROCESSING` | undecided; derived images only | evidence-gated | lineage from canonical image to derivative | silent preprocessing mutation rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-RENDER.P-IMAGE_IDENTITY` | stable page ID, dimensions, file hash, canonical pixel hash | proposed | `page_image_set` manifest | hash drift stales OCR/layout/order evidence |

### `SC-MAP`: Pre-OCR Map Model

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-MAP.P-MAP_ROLE` | pre-OCR maps are qualification evidence, not accepted source text | proposed | `pre_ocr_mapping_model.md` and Gate 1 protocol | map label cannot accept source content |
| `P0.G01.C-SOURCE_PROFILE.SC-MAP.P-MAP_PARTS` | `doc_map`, `content_map`, `art_map` in a `pre_ocr_map_bundle` | proposed | map model and future schema contract | missing required map part blocks map bundle acceptance |
| `P0.G01.C-SOURCE_PROFILE.SC-MAP.P-MAP_PAYLOAD_LOCATION` | roadmap links state only; map payloads live in dedicated evidence artifacts | proposed | roadmap node `gate-01-pre-ocr-map-model` | roadmap payload embedding rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-MAP.P-MAP_SCHEMA_FORMAT` | JSON Schema-backed artifacts; human YAML authoring remains open | evidence-gated | canonical format decision | unresolved schema blocks implementation |
| `P0.G01.C-SOURCE_PROFILE.SC-MAP.P-VISUALIZATION_SCOPE` | roadmap viewer shows dependency/status; detailed map viewer is later tooling | proposed | roadmap node and comments | map visualization cannot become source of truth |

### `SC-PAGE_MAP_READINESS`: Reusable Page Readiness Pipeline

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-PAGE_MAP_READINESS.P-PIPELINE_ROLE` | readiness/routing signal before page-complete review, not acceptance | planned | roadmap node `gate-01-page-map-readiness-pipeline` and `pre_ocr_mapping_model.md` | readiness cannot accept a page, fixture, or Gate |
| `P0.G01.C-SOURCE_PROFILE.SC-PAGE_MAP_READINESS.P-GENERIC_BUILDER` | one reusable builder with page-specific profiles | planned | future evidence class under bounded authorization | page-specific one-off behavior blocks reuse |
| `P0.G01.C-SOURCE_PROFILE.SC-PAGE_MAP_READINESS.P-PAGE_PROFILE` | every processed page has an explicit profile: expected blocks, content types, anchors, reading order, exclusions, blockers | planned | future page-profile evidence class, starting with page 002 pilot | missing/extra profile block blocks readiness |
| `P0.G01.C-SOURCE_PROFILE.SC-PAGE_MAP_READINESS.P-PILOT_PAGE` | page 002 only as first pilot/proving case | planned | future bounded authorization for page 002 pilot | any broader page run requires separate authorization |
| `P0.G01.C-SOURCE_PROFILE.SC-PAGE_MAP_READINESS.P-COVERAGE_METRICS` | advisory block/text/anchor/order coverage summaries | planned | future readiness evidence class | percentages cannot unlock page-complete acceptance |
| `P0.G01.C-SOURCE_PROFILE.SC-PAGE_MAP_READINESS.P-FIDELITY_INPUTS` | existing-authorized artifacts only | planned | future readiness evidence class and boundary criteria | OCR, render, PDF parsing, PDF text-layer extraction, or raw mutation blocks the packet |
| `P0.G01.C-SOURCE_PROFILE.SC-PAGE_MAP_READINESS.P-HUMAN_PACKET` | human-readable packet with decision impact and no internal QA burden | planned | future human-review packet class | packet cannot ask the user to verify hashes, test keys, or pytest output |

### `SC-OCR`: OCR Authority And PDF Text-Layer Branch

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-OCR_ROLE` | OCR is primary text acquisition | pending approval | decision record and benchmark plan | non-OCR canonical text path rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-OCR_ENGINE` | undecided; benchmark candidates only | evidence-gated | engine/version/model benchmark | no engine locked in Gate 1 |
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-OCR_CONFIG` | undecided; one locked config after qualification | evidence-gated | gold transcription benchmark | config drift stales OCR descendants |
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-PDF_TEXT_AVAILABILITY` | optional; absence permitted | pending approval | comparison manifest or explicit absence | absence cannot block OCR-first intake |
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-PDF_TEXT_CANONICAL_USE` | forbidden | pending approval | DAG validation | canonical text-layer predecessor blocks acceptance |
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-PDF_TEXT_ORDER_USE` | forbidden | pending approval | order/DAG validation | text-layer order cannot accept order |
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-DISAGREEMENT_POLICY` | OCR/PDF-text disagreement creates finding | proposed | finding closure record | silent substitution rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-OCR.P-CORRECTION_PROVENANCE` | reviewed correction creates new candidate revision | proposed | supersession record | silent mutation rejected |

### `SC-LAYOUT`: Supported Geometry And Order Boundary

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-LAYOUT.P-LAYOUT_MODEL` | ordered vertical bands | evidence-gated | layout examples and review | unsupported model parks/rejects profile |
| `P0.G01.C-SOURCE_PROFILE.SC-LAYOUT.P-BAND_TYPES` | full-width and two-column bands | evidence-gated | positive layout fixtures and `Вирал` inventory | missing band support blocks acceptance |
| `P0.G01.C-SOURCE_PROFILE.SC-LAYOUT.P-TWO_COLUMN_ORDER` | declared left/right order per band | evidence-gated | layout/order maps | unresolved order blocks source acceptance |
| `P0.G01.C-SOURCE_PROFILE.SC-LAYOUT.P-REGION_COVERAGE` | every text-bearing region included once or explicitly excluded | proposed | region inventory | missing/duplicate region non-waivable |
| `P0.G01.C-SOURCE_PROFILE.SC-LAYOUT.P-AMBIGUITY_POLICY` | ambiguous reading order blocks acceptance | pending approval | negative fixture | non-waivable for 0.1 |
| `P0.G01.C-SOURCE_PROFILE.SC-LAYOUT.P-UNSUPPORTED_FEATURES` | interleaved flow, 3+ body columns, overlapping flows, rotated body text | evidence-gated | negative fixtures | rejected or parked before OCR acceptance |

### `SC-STRUCTURE`: RPG Structure Boundary

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-STRUCTURE.P-BASELINE_STRUCTURES` | headings, paragraphs, emphasis, quotes, lists, simple tables | evidence-gated | prior-work taxonomy plus pilot examples | unsupported structure parked/rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-STRUCTURE.P-RPG_STRUCTURES` | boxed text, callouts, sidebars, stat blocks/cards, captions, headers/footers, page markers, anchored blocks | evidence-gated | prior scenario/log evidence and `Вирал` inventory | taxonomy not closed |
| `P0.G01.C-SOURCE_PROFILE.SC-STRUCTURE.P-UNKNOWN_FALLBACK` | `unclassified_bounded_block` | proposed | positive fallback fixture | allowed only with complete text/geometry/order/anchors |
| `P0.G01.C-SOURCE_PROFILE.SC-STRUCTURE.P-COMPLEX_TABLES` | unsupported unless separately accepted | proposed | negative fixture | parked/rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-STRUCTURE.P-MAPS_DIAGRAMS` | essential text only in maps/diagrams unsupported for 0.1 | proposed | negative fixture | parked/rejected |
| `P0.G01.C-SOURCE_PROFILE.SC-STRUCTURE.P-DEGRADATION_BOUNDARY` | handwriting, unreadable scans, severe degradation unsupported | evidence-gated | pilot/prior examples | rejected before accepted source |

### `SC-CONTROL`: Identity, Failure, And Invalidation

| Parameter ID | Candidate Value | Decision | Evidence | Failure/Waiver |
|---|---|---|---|---|
| `P0.G01.C-SOURCE_PROFILE.SC-CONTROL.P-PROFILE_REFERENCE` | exact `{profile_id, profile_version, profile_hash}` | proposed | schema/DAG validation | missing profile ref blocks acceptance |
| `P0.G01.C-SOURCE_PROFILE.SC-CONTROL.P-ROLLUP_STATUS` | parent accepted only when required children accepted or parked | proposed | validator rule | manual override invalid |
| `P0.G01.C-SOURCE_PROFILE.SC-CONTROL.P-VIOLATION_BEHAVIOR` | reject before OCR/source acceptance | proposed | negative fixtures | core violations non-waivable |
| `P0.G01.C-SOURCE_PROFILE.SC-CONTROL.P-INVALIDATION` | source, render, OCR, layout, structure, or identity change stales descendants | pending approval | decision record | mutation requires revalidation |
| `P0.G01.C-SOURCE_PROFILE.SC-CONTROL.P-IMPLEMENTATION_AUTHORIZATION` | blocked until Gate 1 accepted | pending approval | user decision and checkpoint | no module work from draft profile |

## Evidence-Pass Sequence

0. Qualification protocol: define parameter statuses, render/OCR candidates,
   gold-sample rules, required pages/regions, metrics, non-waivable failures,
   and parameter-register update rules.
1. Pilot intake: use the committed `Вирал` candidate PDF to create a
   selected-page manifest and bind pages 1-20 only after the exact protocol
   revision is `accepted_protocol` and a distinct bounded authorization names
   selected-page manifest creation as the exact action.
2. Pre-OCR map model qualification: decide whether `doc_map`, `content_map`,
   `art_map`, and `pre_ocr_map_bundle` are required Gate 1 evidence and which
   schema/identity rules control them.
3. Page inventory: classify each selected page and text-bearing region only
   under the relevant bounded authorization.
4. Page-map readiness pipeline: use a reusable builder plus page-specific
   profiles to prove per-page block inventory, advisory coverage, anchors,
   reading order, overlay/nesting declarations, and existing-artifact-only
   fidelity indicators before any page-complete review. Page 002 is the first
   pilot only.
5. Render qualification: compare candidate render profiles on identical regions
   only under the relevant bounded authorization.
6. OCR qualification: compare engine/config candidates against predeclared gold
   transcription only under the relevant bounded authorization.
7. Layout/order qualification: prove complete, non-ambiguous order for all
   pilot pages only under the relevant bounded authorization.
8. Overlay qualification: review region coverage, OCR geometry, order sequence,
   and source-block trace overlays only under the relevant bounded
   authorization.
9. Profile lock: bind exact accepted values into a versioned profile decision.
10. Structure lock: publish supported, fallback, and rejected classes with
   evidence references.

## Roadmap And Matrix Links

The live roadmap remains `Sourcefold/docs/roadmap/roadmap.yaml`.
This hierarchy is a detailed decision record for roadmap node
`decision-source-profile-0.1`. Today's protocol work is tracked in roadmap node
`gate-01-qualification-protocol`, and the pre-OCR map model is tracked in
roadmap node `gate-01-pre-ocr-map-model` so the viewer can show Gate 1
dependencies without embedding map payloads into `roadmap.yaml`. The reusable
page-map readiness pipeline is tracked in roadmap node
`gate-01-page-map-readiness-pipeline` so page-level readiness work is visible
as a Gate 1 dependency before page-complete review packets.

Acceptance matrix rows use stable IDs in
`core_0_1_acceptance_matrix.md`. Parameter records should reference matrix IDs
instead of row positions.

## Current Post-P020 Matrix Note

`G1FARP-G1-VIRAL-001` is the current fixture-admission / whole-Gate-acceptance
readiness prep packet. It consumes `G1SPDR-G1-VIRAL-001`, preserves the 5 Gate
review candidates, 2 existing Core 0.1 OCR parking outcomes, 2 evidence-only
rows, 2 blocked rows, and 1 page 021+ separate-BA row, then records fixture
admission readiness and whole Gate 1 acceptance readiness as
`not_ready_requires_future_decision`. It does not accept whole source profile,
accept whole Gate 1, admit fixtures, create fixture manifests, execute
OCR/remediation, or authorize page 021+.
`G1FARPREV-G1-VIRAL-001` accepts that packet only as readiness/blocker review,
and `G1FABRP-G1-VIRAL-001` is the fixture admission blocker resolution prep
packet. It creates no fixture admission, fixture manifest, page `021+`
authorization, blocker resolution, or whole Gate 1 acceptance.
`G1FABRPREV-G1-VIRAL-001` accepts `G1FABRP-G1-VIRAL-001` as blocker-resolution
prep only and selects unsupported/negative fixture policy as the next
decision-prep lane. `G1UNFPDP-G1-VIRAL-001` prepares that lane only.
`G1UNFPDPREV-G1-VIRAL-001` accepts the prep packet for policy-record
preparation, `G1UNFPR-G1-VIRAL-001` prepares the policy record candidate, and
`G1UNFPAR-G1-VIRAL-001` accepts the unsupported/negative fixture policy
decision only. `G1FSFDP-G1-VIRAL-001` prepares fixture strategy fit decision
material, and `G1FSFAR-G1-VIRAL-001` accepts the fixture strategy fit decision
only. `G1FARR-G1-VIRAL-001` refreshes fixture admission readiness only.
`G1FMP-G1-VIRAL-001` prepares future fixture manifest shape only, and
`G1FMR-G1-VIRAL-001` records that fixture manifest shape without admitting
fixtures. `G1FADP-G1-VIRAL-001` prepares fixture admission decision questions
only, `G1FADAR-G1-VIRAL-001` accepts fixture admission without accepting whole
Gate 1, `G1WGARR-G1-VIRAL-001` prepares whole Gate 1 acceptance readiness
recheck only, and `G1WGADR-G1-VIRAL-001` accepts whole Gate 1 only for pages
001-020 and the `G1FADAR` admitted fixture manifest groups. Page `021+` remains
separate. `C01IPP-G1-VIRAL-001` prepares Core 0.1 implementation planning only
from `G1WGADR`; it creates no implementation authorization receipt, runtime
implementation, OCR/render/PDF/raw/source mutation, translation, proofreading,
or push. `C01IAR-G1-VIRAL-001` prepares implementation authorization receipt
material only and keeps runtime implementation blocked pending future
first-slice prerequisites. `C01FSDP-G1-VIRAL-001` prepares first-slice design
surfaces only for `C01WP-01-phase-1-scaffold-contracts`; it creates no runtime
implementation or source-profile lock/acceptance. `C01SPLPR-G1-VIRAL-001`
records source-profile parking only for that design-prep boundary and does not
create a runtime source-profile lock. `C01FSARP-G1-VIRAL-001` prepares the
first-slice Sol/Terra architecture review packet only and does not create
runtime implementation or runtime source-profile lock/acceptance.
`C01AMTR-G1-VIRAL-001` prepares acceptance-matrix claim/evidence trace review
material only and does not create runtime implementation or runtime
source-profile lock/acceptance.
`C01RSPLP-G1-VIRAL-001` records runtime source-profile parking for C01WP-01
authorization-prep only and does not create runtime implementation or runtime
source-profile lock/acceptance.
`C01RSAP-G1-VIRAL-001` prepares first-slice runtime authorization decision
context for C01WP-01 only and does not create runtime authorization grant,
runtime start, runtime implementation, or runtime source-profile
lock/acceptance.
`C01RSAD-G1-VIRAL-001` records a non-executing first-slice runtime
authorization decision for C01WP-01 only and does not create runtime
start/execution, runtime implementation, or runtime source-profile
lock/acceptance.
`C01RSPLAD-G1-VIRAL-001` records a runtime source-profile
lock-or-acceptance decision for C01WP-01 only; it grants no runtime
source-profile lock/acceptance, keeps the runtime source profile parked, and
does not create runtime start/execution or implementation.
`C01TETD-G1-VIRAL-001` completes a Sol/Terra-reviewed points 1-5 readiness
chain toward a future text extraction smoke trial; point 6 remains blocked
until Bogdan is called, and no OCR/PDF parsing/text-layer extraction or actual
text extraction is performed.

## Open Decisions

- The `Вирал` PDF is present as a committed candidate input with pages 001-020
  page-complete accepted-only evidence, but it is not accepted as a fixture or
  as a locked source profile.
- Gate 1 Qualification Protocol is `accepted_protocol` for methodology only;
  candidate-derived actions still require distinct bounded authorizations.
- The exact page-image render profile is not accepted.
- The OCR engine/config is not accepted.
- Numeric OCR and overlay thresholds are not accepted.
- RPG taxonomy coverage is not accepted.
- Reading-order ambiguity is treated as non-waivable for 0.1 unless the user
  explicitly changes the policy.
