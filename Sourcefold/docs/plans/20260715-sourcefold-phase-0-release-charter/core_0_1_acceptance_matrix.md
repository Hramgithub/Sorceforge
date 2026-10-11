# Core 0.1 Executable Acceptance Matrix

Status: draft skeleton updated by Gate 1 Step 9; no executable evidence created

This matrix is separate from the Phase 0 decision matrix. It maps the
OCR-first Core 0.1 release claim to evidence that must exist before a release
candidate can be frozen.

| ID | Step | Criterion | Evidence Artifact | Human Check | Failure Behavior | Status |
|---|---|---|---|---|---|---|
| AM-02-01 | 2 | PDF is immutable root evidence. | `source_pdf` manifest with hash and page count. | operator confirms source selection and rights/redaction status. | block intake | draft |
| AM-02-02 | 2 | Selected pages render one-to-one to page images. | `page_image_set`, renderer run record, page hashes. | page count/dimensions spot check. | block OCR | draft |
| AM-03-01 | 3 | Page layout conforms to bounded band/two-column profile. | `layout_profile`, per-page `layout_map`. | reviewer checks representative pages and exceptions. | block OCR acceptance | draft |
| AM-03-02 | 3 | Every text-bearing region is accounted for. | region inventory and exclusion findings. | reviewer confirms no missing regions. | block OCR acceptance | draft |
| AM-03-03 | 3 | Pre-OCR page/content/art maps use one shared page and region identity model. | `pre_ocr_map_bundle` with `doc_map`, `content_map`, `art_map`, shared IDs, and hashes. | reviewer checks cross-map references and missing/duplicate regions. | block map bundle acceptance | proposed |
| AM-03-04 | 3 | Roadmap references map state without embedding map payloads. | roadmap node `gate-01-pre-ocr-map-model` linked to canonical map evidence. | reviewer checks node status, checklist, linked plan, and no payload drift. | block documentation checkpoint | proposed |
| AM-04-01 | 4 | OCR method is frozen before full run. | `ocr_profile`, tool/version/config records, benchmark report. | user/orchestrator accepts benchmark thresholds. | block full OCR | draft |
| AM-04-02 | 4 | Gold benchmark passes predeclared thresholds. | gold transcription and benchmark report. | reviewer confirms threshold was not chosen after results. | block full OCR | draft |
| AM-04-03 | 4 | Complex/tight pages prove OCR input geometry independently before source/profile/page-status acceptance. Review `*-text-evidence.png` crops may be review assets or bounded smoke inputs only when the lane names that limit; P017/P018-like pages require full-page-derived regions or another independently generated OCR-safe geometry, candidate text/hash sealing before reference scoring, and no reference-text-map use during candidate generation. Static router evidence may route pages toward geometry probes, but cannot by itself execute OCR, promote policy, or accept source/profile/page-status/page-complete state. | independent OCR geometry probe report, sealed candidate hash manifest, reference-scoring report, negative evidence for rejected crop/segmentation routes, `ocr_input_surface` router replay report. | reviewer confirms the candidate was generated before reference scoring and did not use reference-guided repair; orchestrator confirms the router used saved metrics/metadata only. | block OCR/source-profile/page-status/page-complete acceptance for the affected page class; reference-guided output can only be support evidence | declared |
| AM-05-01 | 5 | OCR covers every declared region once. | `ocr_run`, raw outputs, region-to-OCR map. | reviewer samples low-confidence regions. | block reading order | draft |
| AM-05-02 | 5 | PDF text layer does not enter canonical text. | `pdf_text_comparison` and discrepancy findings only. | reviewer checks no text-layer predecessor edge exists. | block source acceptance | draft |
| AM-06-01 | 6 | Reading order is deterministic and complete. | `reading_order_map`, ordered block stream, order findings. | all pilot pages receive human order review. | block source acceptance | draft |
| AM-06-02 | 6 | Ambiguous order is resolved. | order finding closure records. | reviewer confirms no open ambiguity. | block source acceptance; non-waivable for 0.1 | draft |
| AM-07-01 | 7 | Source text traces to page-image evidence. | anchored source candidate and trace map. | reviewer checks sample and high-risk regions. | block accepted source | draft |
| AM-07-02 | 7 | Overlay/content QA covers all pilot pages. | overlay QA record, content findings, page acceptance ledger. | reviewer confirms omission/duplication/geometry checks. | block accepted source | draft |
| AM-07-03 | 7 | Unknown structures are preserved safely. | `unclassified_bounded_block` records with geometry/order/anchors. | reviewer confirms no semantic support is overclaimed. | block source acceptance until bounded fallback is accepted | draft |
| AM-07-04 | 7 | Page-complete readiness packets declare page block inventory, advisory coverage, reading order, anchors, context/exclusion decisions, OCR/text fidelity indicators from existing artifacts only, and open blockers before any page-complete acceptance is requested. | `page_map_readiness_packet`, page block inventory, advisory coverage summary, discrepancy disposition ledger. | reviewer checks the human-facing page packet; percentages are planning signals only. | block page-complete review request | draft |
| AM-07-05 | 7 | Page-complete review packets gate on semantic-map readiness before complete-ok routing. | canonical semantic-unit JSON artifact, Markdown projection, semantic validation, projection validation, inventory reconciliation, structural finding ledger. | reviewer inspects the packet only after validators suppress any non-waivable blocker. | block page-complete acceptance request; non-waivable for structure loss | declared |
| AM-08-01 | 8 | Translation covers all accepted source units. | translation unit manifest and source-to-RU trace map. | reviewer checks semantic high-risk units. | block RU draft acceptance | draft |
| AM-08-02 | 8 | Controlled data is preserved. | automated comparison for names, numbers, dice, tables, mechanics. | reviewer checks findings/waivers. | block RU draft acceptance | draft |
| AM-09-01 | 9 | Proofreading changes do not drift source meaning. | proofread change ledger and semantic-drift findings. | reviewer checks all high-risk changes. | block RU master acceptance | draft |
| AM-09-02 | 9 | RU master is accepted by exact revision/hash. | RU master acceptance record. | human acceptance. | block release freeze | draft |
| AM-10-01 | 10 | Candidate evidence is frozen and hash-bound. | frozen candidate manifest and full DAG. | release owner confirms exact candidate. | block release review | draft |
| AM-10-02 | 10 | Negative fixtures fail for expected reasons. | fixture results. | reviewer checks failure explanations. | block release approval | draft |
| AM-10-03 | 10 | Terra release review approves exact candidate. | independent Terra release handoff. | release owner confirms no post-freeze mutation. | release remains pending | draft |

## Gate 1 Protocol Criteria

These rows bind the Step 1-8 Gate 1 protocol work to future executable
fixtures. Step 9 declares criteria only; it does not create fixtures, execute
checks, accept evidence, or authorize candidate-derived work.

| ID | Gate 1 Step | Criterion | Future Evidence Artifact | Fixture Coverage | Failure Behavior | Status |
|---|---|---|---|---|---|---|
| AM-G1-01 | 1-3 | Protocol, authority, permission, decision, evidence, and finding states are accepted before candidate-derived work. | accepted protocol revision, authority record, permission ledger | `fixture-protocol-authority-lock`, `fixture-permission-state-missing`, `fixture-decision-state-missing`, `fixture-evidence-state-missing`, `fixture-finding-state-missing`, `fixture-unsupported-profile`, `fixture-bad-edge` | block bounded trial authorization | declared |
| AM-G1-02 | 4 | Candidate PDF intake cannot create selected pages, page count/hash claims, or rights conclusions without bounded authorization. | candidate intake record, selected-page manifest authorization | `fixture-unsupported-profile`, `fixture-unauthorized-intake-metadata`, `fixture-stale-intake-metadata` | block intake acceptance | declared |
| AM-G1-03 | 5 | Render benchmark output requires frozen render candidate manifest, comparison plan, output manifest lineage, and stale behavior. | render trial record, comparison plan, output manifest | `fixture-render-lineage-stale`, `fixture-stale-lineage` | block render evidence acceptance | declared |
| AM-G1-04 | 6 | Pre-OCR map bundle requires shared identity/geometry model and no OCR/PDF text-layer/translation payload. | `pre_ocr_map_bundle`, map schemas, map review ledger | `fixture-missing-region`, `fixture-column-order`, `fixture-map-payload-leakage`, `fixture-overlay-failure`, `fixture-unclassified-block`, `fixture-stale-lineage` | block map bundle acceptance | declared |
| AM-G1-05 | 7 | OCR benchmark requires frozen OCR candidate manifest, scoring/gold plan, output manifest lineage, and text-layer payload containment. | OCR trial record, candidate manifest, scoring plan, gold sample manifest | `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-stale-lineage` | block OCR evidence acceptance | declared |
| AM-G1-05A | 7 | OCR benchmark/remediation lanes must label the input surface class: review crop, text-evidence crop, OCR candidate crop, or full-page-derived region. A review/text-evidence crop lane cannot silently become OCR-safe policy for complex/tight pages; a full-page-derived geometry lane must seal candidates before reference scoring, and reference-guided repair must remain a non-independent evidence class. Static routing decisions such as `baseline_ok`, `geometry_probe_required`, `park_candidate_policy`, `blocked_unsafe_surface`, and `blocked_incomplete_artifacts` are routing evidence only. | input-surface policy record, static router contract, OCR geometry probe manifest, sealed candidate text hashes, reference-scoring report | `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-stale-lineage`, `fixture-column-order` | block OCR/source-profile/page-status/page-complete acceptance for the affected page class | declared |
| AM-G1-06 | 8 | QA acceptance requires current QA scope, coverage manifest, finding ledger, non-waivable blocker disposition, and no empty-ledger acceptance. | QA scope manifest, QA coverage manifest, finding ledger, acceptance record | `fixture-open-finding`, `fixture-missing-qa-coverage`, `fixture-empty-ledger`, `fixture-parking-bypass`, `fixture-invalid-waiver`, `fixture-stale-lineage`, `fixture-missing-region`, `fixture-column-order`, `fixture-overlay-failure`, `fixture-unclassified-block` | block Accepted Source Text | declared |
| AM-G1-07 | 9 | Fixture manifest declares expected pass/fail reason, target criteria, protocol revision, and non-waivable failure class before execution. | fixture manifest schema and fixture index | `fixture-positive-0.1`, `fixture-valid-human-acceptance`, `fixture-protocol-authority-lock`, `fixture-permission-state-missing`, `fixture-decision-state-missing`, `fixture-evidence-state-missing`, `fixture-finding-state-missing`, `fixture-unsupported-profile`, `fixture-bad-edge`, `fixture-unauthorized-intake-metadata`, `fixture-stale-intake-metadata`, `fixture-render-lineage-stale`, `fixture-stale-lineage`, `fixture-missing-region`, `fixture-column-order`, `fixture-map-payload-leakage`, `fixture-overlay-failure`, `fixture-unclassified-block`, `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-invalid-waiver`, `fixture-open-finding`, `fixture-missing-qa-coverage`, `fixture-parking-bypass`, `fixture-empty-ledger` | block fixture execution | declared |
| AM-G1-08 | 10 | Review checkpoint confirms all required fixture obligations are declared or explicitly parked before requesting review of the exact draft protocol revision; it cannot authorize a bounded candidate action by itself. | documentation checkpoint, roadmap state, review handoffs, exact draft revision under review | `fixture-valid-human-acceptance` | block Gate 1 exit; later candidate trials still require accepted protocol plus separate bounded action record | declared |
| AM-G1-09 | 8 | Page-complete readiness must remain separate from page-complete acceptance and may use only already-authorized artifacts for advisory coverage and fidelity indicators. | page readiness packet, page block inventory, advisory coverage summary, blocker ledger | `fixture-missing-region`, `fixture-column-order`, `fixture-overlay-failure`, `fixture-unclassified-block`, `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-missing-qa-coverage`, `fixture-stale-lineage` | block page-complete acceptance request | declared |
| AM-G1-10 | 8 | Semantic-map readiness is a first-class page-complete gate: canonical JSON, Markdown projection, inventory reconciliation, structural findings, and decision-option suppression must all be current before a complete-ok option exists. | semantic map artifact, projection artifact, report semantic validation fields, inventory reconciliation, structural finding ledger | `fixture-missing-region`, `fixture-column-order`, `fixture-unclassified-block`, `fixture-open-finding`, `fixture-missing-qa-coverage`, `fixture-stale-lineage`, `fixture-map-payload-leakage` | block page-complete acceptance request | declared |

## Core 0.1 Fixture Coverage Map

Every Core 0.1 matrix row is mapped to a declared fixture obligation or to a
future parked/blocking disposition. No row is passed by this mapping.

| Criterion | Fixture Coverage | Disposition |
|---|---|---|
| AM-02-01 | `fixture-positive-0.1`, `fixture-unsupported-profile` | declared |
| AM-02-02 | `fixture-positive-0.1`, `fixture-render-lineage-stale` | declared |
| AM-03-01 | `fixture-positive-0.1`, `fixture-column-order` | declared |
| AM-03-02 | `fixture-missing-region`, `fixture-unclassified-block` | declared |
| AM-03-03 | `fixture-missing-region`, `fixture-column-order`, `fixture-stale-lineage` | declared |
| AM-03-04 | `fixture-missing-region`, `fixture-unclassified-block` | declared |
| AM-04-01 | `fixture-render-lineage-stale`, `fixture-ocr-discrepancy` | declared |
| AM-04-02 | `fixture-ocr-discrepancy`, `fixture-stale-lineage` | declared |
| AM-04-03 | `fixture-ocr-discrepancy`, `fixture-column-order`, `fixture-text-layer-leakage`, `fixture-stale-lineage` | declared |
| AM-05-01 | `fixture-missing-region`, `fixture-ocr-discrepancy` | declared |
| AM-05-02 | `fixture-text-layer-leakage` | declared |
| AM-06-01 | `fixture-column-order`, `fixture-missing-region` | declared |
| AM-06-02 | `fixture-column-order`, `fixture-open-finding` | declared |
| AM-07-01 | `fixture-positive-0.1`, `fixture-stale-lineage` | declared |
| AM-07-02 | `fixture-overlay-failure`, `fixture-missing-qa-coverage`, `fixture-empty-ledger` | declared |
| AM-07-03 | `fixture-unclassified-block` | declared |
| AM-07-04 | `fixture-missing-region`, `fixture-column-order`, `fixture-overlay-failure`, `fixture-unclassified-block`, `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-missing-qa-coverage`, `fixture-stale-lineage` | declared |
| AM-07-05 | `fixture-missing-region`, `fixture-column-order`, `fixture-unclassified-block`, `fixture-open-finding`, `fixture-missing-qa-coverage`, `fixture-stale-lineage`, `fixture-map-payload-leakage` | declared |
| AM-08-01 | `fixture-positive-0.1`, `fixture-stale-lineage` | declared |
| AM-08-02 | `fixture-positive-0.1`, `fixture-open-finding` | declared |
| AM-09-01 | `fixture-positive-0.1`, `fixture-stale-lineage` | declared |
| AM-09-02 | `fixture-valid-human-acceptance`, `fixture-open-finding` | declared |
| AM-10-01 | `fixture-stale-lineage`, `fixture-valid-human-acceptance` | declared |
| AM-10-02 | `fixture-protocol-authority-lock`, `fixture-permission-state-missing`, `fixture-decision-state-missing`, `fixture-evidence-state-missing`, `fixture-finding-state-missing`, `fixture-unsupported-profile`, `fixture-bad-edge`, `fixture-unauthorized-intake-metadata`, `fixture-stale-intake-metadata`, `fixture-render-lineage-stale`, `fixture-stale-lineage`, `fixture-missing-region`, `fixture-column-order`, `fixture-map-payload-leakage`, `fixture-overlay-failure`, `fixture-unclassified-block`, `fixture-ocr-discrepancy`, `fixture-text-layer-leakage`, `fixture-invalid-waiver`, `fixture-open-finding`, `fixture-missing-qa-coverage`, `fixture-parking-bypass`, `fixture-empty-ledger` | declared |
| AM-10-03 | parked until Step 10; reason: independent Terra release review requires an exact frozen candidate; owner: `gpt-5.6-terra` in independent release-review role; later evidence task: Step 10 exact-candidate Terra release review handoff | parked |

Rows with `declared` disposition still require future executable evidence.
Rows with parked release-review fixture obligations must be revisited in Step
10 before any Gate 1 exit or release checkpoint.

Every fixture listed in a criterion row must list that exact criterion in the
canonical fixture index. Every criterion listed in a fixture declaration must
list that exact fixture in the corresponding criterion row. One-way mappings,
ranges, wildcard references, aliases, placeholders, and aggregate fixture sets
do not satisfy coverage.

## Step 9 Boundary

The matrix rows above are declared acceptance obligations. They are not passed,
failed, accepted, or released. Any future executable fixture result must bind
the exact protocol revision, fixture manifest revision, evidence predecessors,
and review authority before it can satisfy a criterion.
