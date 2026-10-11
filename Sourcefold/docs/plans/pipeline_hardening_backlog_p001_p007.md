# Pipeline Hardening Backlog - P001/P002/P003/P004/P005/P006/P007

Scope: rules discovered while processing pages 001 through 007 that are not yet fully promoted into reusable Sourcefold pipeline validators or consumer gates.

Already universalized:

- `page_review_semantic_units.py`: semantic unit schema/taxonomy, heading levels, paragraph-boundary preservation, continuation links, OCR/text-evidence crop linkage, inventory/projection checks.
- `deferred_review_contract.py`: deferred visual anchors and action backlog boundaries.
- `artifact_lifecycle_validation.py`: held, stale, superseded, and current artifact lifecycle checks.
- `bounded_authorization_contract.py`: bounded authorization id, ledger presence, scope marker, and authority leakage checks.
- `pcrp_preflight_contract.py`: aggregate predecessor contract checks before PCRP.
- `human_review_gate_contract.py`: Sol OK, Terra OK, and explicit Bogdan decision gates.

## 1. Visual/Title Page-Complete Contract

Current state:

- Page 001 is accepted as page-complete based on visual/title anchors, not text extraction.
- The page-specific flow is `P001TR-G1-VIRAL-001` -> `PCRP-G1-VIRAL-P001-001` -> `P001PCA-G1-VIRAL-001`.
- Review anchors include full-page cover, title/logo area, and footer/rating/tagline/logo area.
- The local rule blocks OCR execution, source acceptance, and whole-Gate acceptance.

Missing universal rule:

- Add a shared `visual_title_page_contract` validator.
- Permit page-complete review without text extraction only for explicit visual/title page profiles.
- Require complete visual/title anchor coverage and reviewed readiness for every declared anchor.
- Require a negative capability matrix: no OCR/text extraction, no source acceptance, no fixture admission, no whole-Gate acceptance, and no downstream mutation.
- PCRP/page acceptance consumers must fail closed if a visual/title page lacks the contract or if the contract leaks text/OCR authority.

## 2. Source Reconstruction Evidence-Slice Contract

Current state:

- `G1RP-G1-VIRAL-001` packages seven reviewed source-reconstruction records.
- The accepted scope is narrow: four positive source-text records and three negative visual-exclusion records.
- Bogdan accepted the exact slice, but pages are not complete and whole Gate 1 is not accepted.
- Current behavior is enforced by dedicated Gate 1 source-reconstruction scripts/tests.

Missing universal rule:

- Add a shared `source_reconstruction_slice_contract` validator.
- Require exact record counts, record identities, predecessor hashes, and source-text vs visual-exclusion classification.
- Require the accepted scope to stay record-slice only unless a separate page-complete or whole-Gate acceptance exists.
- Require a rollup/preflight step before broader Gate use.
- Block page-complete, whole-Gate, translation, proofreading, implementation, and push leakage from source-reconstruction slice acceptance.

## 3. Context-Only Region Decision Contract

Current state:

- Page 004 uses a separate context-only decision for the full tilted inset `PRM-G1-VIRAL-001-P004-R01`.
- The confirmed context-only region must not compete with peer text crop records `R02` and `R03`.
- The local flow records Bogdan's explicit `page 004 context-only ok` decision and keeps page-complete acceptance false.
- Semantic inventory can represent `context_only`, but the standalone decision workflow is still page-specific.

Missing universal rule:

- Add a shared `context_only_region_decision` validator.
- Require explicit human decision, affected region id, peer represented records, overlap rationale, evidence references, and downstream limits.
- Context-only decisions must not mutate predecessor packets.
- Context-only decisions must not create page-complete acceptance, source acceptance, OCR acceptance, fixture admission, or whole-Gate acceptance.
- Page-map/PCRP consumers should distinguish confirmed context-only regions from unresolved missing text-bearing regions.

## 4. Human-Facing Structure/Display Label Normalization

Current state:

- Page 004 corrected human-facing `Draft structure/semantics` labels so body-only text blocks display as `text_body`, not `none`.
- The migration is review-asset/display-only and does not mutate predecessor evidence.
- The semantic unit taxonomy now catches nearby style/role problems, but the display migration itself remains local.

Missing universal rule:

- Add a shared `review_display_label_contract` validator.
- Require body-only text blocks to use human-readable display labels instead of `none`.
- Distinguish display-only normalization from predecessor evidence mutation.
- Block packets whose human-facing labels hide text body structure or make represented body text look absent.
- Add regression coverage for old review packets that need display normalization without changing their evidence lineage.

## 5. OCR Benchmark / Candidate Contract

Current state:

- Early OCR benchmark/remediation work used exact admitted zones from pages 001, 005, and 006.
- The flow distinguishes OCR candidate zones from `visual_qc` zones.
- It records raw text, TSV, logs, stderr captures, hashes, and remediation recommendations.
- It blocks PDF text-layer leakage and raw-output mutation.
- Later `text_extraction_contract` covers draft text layers, but not OCR benchmark/run/remediation matrix rules.

Missing universal rule:

- Add a shared `ocr_benchmark_candidate_contract` validator.
- Require exact admitted crop set, zone ids, page ids, crop hashes, OCR profile/config, raw-output hashes, and result lineage.
- Distinguish OCR candidate zones from visual-QC-only zones.
- Preserve benchmark threshold/result separation and prevent threshold changes after results.
- Block PDF text-layer leakage, unauthorized OCR reruns, raw-output mutation, and OCR acceptance leakage.
- Require remediation recommendations to remain review-only until separately authorized.

## 6. TOC / Page-Reference Row Contract

Current state:

- Page 005 introduced Contents-like structure with contents heading, entry rows, and page references.
- The semantic taxonomy includes `page_ref`, `list`, `list_item`, and `page_marker`.
- Page 005 also treats the margin page marker as visual/context-only.
- The current behavior is embedded in page-specific P005 semantic refresh/profile data.

Missing universal rule:

- Add a shared `toc_page_reference_contract` validator.
- Represent contents entries as stable rows/groups instead of flattened paragraph text.
- Preserve entry text and page reference values without treating page numbers as decorative noise.
- Distinguish page references inside TOC rows from margin page markers.
- Require projection checks that prove row count, entry labels, and page-ref units survive Markdown/JSON projections.

## 7. Legacy PCRP Compatibility Refresh Contract

Current state:

- Page 005 went through `PCRP-G1-VIRAL-P005-001/002/003` before the semantic compatibility refresh `PCRP-G1-VIRAL-P005-004`.
- Page 006 held `PCRP-G1-VIRAL-P006-001` and later superseded it with `PCRP-G1-VIRAL-P006-002`.
- Artifact lifecycle handles held/stale/superseded state, and semantic validation handles current structure.
- The specific compatibility-refresh rule is not yet a reusable contract.

Missing universal rule:

- Add a shared `legacy_pcrp_refresh_contract` validator.
- A legacy PCRP may be consumed only as a compatibility predecessor, not as current page-complete evidence.
- A refreshed PCRP must regenerate under current semantic, crop, inventory, lifecycle, authorization, and human-review contracts.
- Legacy text maps with known structural defects should become negative regression inputs, not accepted structure.
- Consumers must fail closed if a legacy PCRP is used directly for page acceptance without a current refresh packet.
