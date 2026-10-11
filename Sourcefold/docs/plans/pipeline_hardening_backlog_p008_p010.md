# Pipeline Hardening Backlog - P008/P009/P010

Scope: rules discovered while processing pages 008, 009, and 010 that are not yet fully promoted into reusable Sourcefold pipeline validators or consumer gates.

Already universalized:

- `page_review_semantic_units.py`: semantic unit schema/taxonomy, heading levels, paragraph-boundary preservation, contiguous `reading_order`, OCR/text-evidence crop linkage, inventory/projection checks.
- `crop_order_validation.py`: logical crop reading order, asset/file-order collapse detection, continuation edges, and consumer helper for semantic/PCRP layers.
- `route_cursor_transition.py`: cursor/status transition validation for bounded route moves without acceptance leakage.
- `bounded_authorization_contract.py`: authorization id, ledger presence, scope marker, and authority leakage validation.
- `pcrp_preflight_contract.py`: aggregate PCRP preflight over required predecessor contracts and output capability boundaries.
- `human_review_gate_contract.py`: Sol/Terra OK plus explicit human package decision validation before next-layer movement.

## 1. Crop-Role Contract / Crop QA

Implementation status: promoted in `sourcefold_crop_role_contract.v1`.

Current state:

- P009/P010 triage builders consume the shared crop-role contract validator.
- Local fields include `source_region_box_px`, `human_review_crop_box_px`, `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`.
- Shared checks cover edge/gutter risks and visual pollution in text crops.

Universal rule:

- `Sourcefold/scripts/crop_role_contract.py` provides `sourcefold_crop_role_contract.v1`.
- Every represented text-like region must expose OCR/text-evidence crop roles.
- Human-review crops must not satisfy OCR/text evidence requirements.
- `source_region_box_px` must remain lineage only, not a downstream OCR boundary.
- Text evidence crops must fail closed on clipping, text near crop boundary, or visual/art/portrait pollution.

## 2. Split Source Region Rule

Implementation status: promoted into `sourcefold_crop_role_contract.v1` as `split_source_region_validation`.

Current state:

- P010 lower `R05` is modeled locally as two peer text blocks:
  - `P010-B005` lower-left Hyeon profile text.
  - `P010-B006` lower-right Maya profile text.
- Both blocks keep `source_region_id = PRM-G1-VIRAL-001-P010-R05` and declare `source_region_split`.
- The previous shared lower human crop was removed.

Universal rule:

- If one source region is split into multiple OCR/text surfaces, each split must be a peer block.
- Each peer block must have its own human-review, OCR-candidate, and text-evidence crop asset.
- Shared/context crops must not be promoted into OCR or reading order.
- Split blocks must declare `source_region_split` and preserve shared lineage to the source region.

## 3. Supersession / Stale Artifact Rule

Implementation status: promoted in `sourcefold_artifact_lifecycle.v1`.

Current state:

- P009 had a local artifact lifecycle:
  - `P009TR-G1-VIRAL-001` held for crop issues.
  - `P009TR-G1-VIRAL-002` preserved as readability-only and stale for PCRP.
  - `P009TR-G1-VIRAL-003` became the current crop contract.

Universal rule:

- `Sourcefold/scripts/artifact_lifecycle_validation.py` validates `held`, `stale`, `superseded`, and `current` state before consumer use.
- PCRP and semantic consumers must reject stale/readability-only predecessors.
- Superseding records must preserve prior evidence without retro-mutating old packets.

## 4. Text Extraction Packet Contract

Implementation status: promoted in `sourcefold_text_extraction_contract.v1`.

Current state:

- P009TXT and P010TXT builders consume the shared text-extraction contract.
- P010TXT now uses shared crop-order validation.
- The draft text layers remain bounded and create no OCR/source/semantic/PCRP/page acceptance.

Universal rule:

- `Sourcefold/scripts/text_extraction_contract.py` provides `sourcefold_text_extraction_contract.v1`.
- Text extraction artifacts must require accepted/current crop contract predecessor.
- Text extraction artifacts must require explicit text evidence crop ids for every extracted text block.
- Text extraction artifacts must require crop-order validation where text order can differ from asset/file order.
- Text extraction artifacts must require continuation metadata when text continues across crops or pages.
- Preserve the negative capability matrix: no OCR acceptance, source acceptance, semantic map, PCRP, page acceptance, or next-page processing unless separately authorized.

## 5. Semantic/PCRP Consumer Enforcement

Implementation status: promoted as `require_text_extraction_consumer_gate(...)`.

Current state:

- `require_passed_crop_order_validation(packet, consumer=...)` exists as a shared helper.
- `require_text_extraction_consumer_gate(packet, consumer=...)` requires passed text-extraction contract validation and, when present, passed crop-order validation for semantic/PCRP consumers.

Universal rule:

- Semantic-map builders must require passed text-extraction contract validation before consuming text extraction packets.
- PCRP builders must reject text extraction packets without required validation.
- Regression coverage proves semantic/PCRP consumers fail closed on missing, blocked, stale, or wrong-schema validation.

## 6. Deferred Visual Anchors / Action Backlog

Implementation status: promoted in `sourcefold_deferred_review_contract.v1`.

Current state:

- P008 separated deferred visual/art anchors and action backlog from page-complete text readiness.
- P008 could be page-complete accepted without treating deferred art replacement as text incompleteness.

Universal rule:

- `Sourcefold/scripts/deferred_review_contract.py` provides a shared deferred-anchor/action-backlog schema.
- Distinguish visual anchors, context-only regions, and text completeness blockers.
- Require deferred visual anchors to carry scope, deferred stage, evidence, and non-acceptance boundaries.
- Require action backlog items to be linked without turning into page acceptance or whole-Gate authorization.

## 7. Explicit Non-Blocker Annotations

Implementation status: promoted in `sourcefold_non_blocker_annotations.v1`.

Current state:

- P009 recorded `right lower grey block = complete/non-blocker` as a local reviewed decision.
- Similar human-reviewed non-blocker notes may recur on future pages.

Universal rule:

- `Sourcefold/scripts/non_blocker_annotations.py` provides a machine-readable non-blocker annotation format.
- Each annotation should include scope, reviewer decision, evidence reference, affected region/crop/unit ids, and downstream limits.
- Validators should distinguish reviewed non-blockers from unresolved blockers or silent omissions.

## 8. Route Cursor Transition

Implementation status: promoted in `sourcefold_route_cursor_transition.v1`.

Universal rule:

- `Sourcefold/scripts/route_cursor_transition.py` validates allowed cursor/status moves.
- A cursor transition must match the required next state when one is declared.
- A cursor transition must not create page-complete acceptance, whole-Gate acceptance, fixture admission, source acceptance, or PCRP authority.

## 9. Bounded Authorization Contract

Implementation status: promoted in `sourcefold_bounded_authorization.v1`.

Universal rule:

- `Sourcefold/scripts/bounded_authorization_contract.py` validates expected authorization id, ledger presence, and allowed scope markers.
- A bounded authorization check must fail closed on missing/wrong BA id or missing ledger entry.
- A bounded authorization check must not permit page-complete acceptance, whole-Gate acceptance, fixture admission, source acceptance, or PCRP authority unless the specific layer authorizes it.

## 10. PCRP Preflight Contract

Implementation status: promoted in `sourcefold_pcrp_preflight.v1`.

Universal rule:

- `Sourcefold/scripts/pcrp_preflight_contract.py` validates that all required predecessor contracts are present and passed before PCRP movement.
- PCRP preflight must fail closed on missing or blocked crop, text, authorization, lifecycle, or review-gate contracts.
- PCRP preflight must not create page-complete acceptance, whole-Gate acceptance, fixture admission, source acceptance, or OCR acceptance.

## 11. Human Review Gate Contract

Implementation status: promoted in `sourcefold_human_review_gate.v1`.

Universal rule:

- `Sourcefold/scripts/human_review_gate_contract.py` validates Sol OK, Terra OK, and Bogdan's explicit decision for the expected package.
- A human review gate must fail closed on non-OK Sol/Terra review, wrong package id, missing source message, or decision outside the allowed set.
- A review decision must not silently create page-complete acceptance unless a separate acceptance layer authorizes it.
