# Decision Log

## 2026-07-27: Fixture Admission Blocker Resolution Prep

Status: prep recorded, no fixture admission.

Decision: Bogdan accepted `G1FARP-G1-VIRAL-001` as a readiness/blocker packet
only and authorized preparing fixture admission blocker resolution prep.

Result: `G1FARPREV-G1-VIRAL-001` records that review, and
`G1FABRP-G1-VIRAL-001` prepares questions for unsupported/negative fixture
policy, fixture strategy fit, whole Gate 1 dependency, and the page `021+`
boundary.

Boundaries: no blocker is resolved, no fixture is admitted, no fixture manifest
is created, page `021+` remains behind separate authorization, and whole Gate 1
remains unaccepted.

Follow-up: Bogdan replied `ок` after Sol/Terra cleanup and human-review
readiness. `G1FABRPREV-G1-VIRAL-001` records that as acceptance of
`G1FABRP-G1-VIRAL-001` as blocker-resolution prep only. Unsupported/negative
fixture policy remains the next candidate decision-prep lane.

`G1UNFPDP-G1-VIRAL-001` prepares that lane only: unsupported profile scope,
negative fixture obligations, invalidation conditions, and fixture-admission
dependency. `G1UNFPDPREV-G1-VIRAL-001` accepts that prep packet for policy
record preparation only.

`G1UNFPR-G1-VIRAL-001` prepares the unsupported/negative fixture policy record
candidate for human review. It contains candidate decisions for unsupported
profile scope, negative fixture obligations, invalidation conditions, and
fixture-admission dependency, but creates no policy decision or blocker
resolution. No fixture admission, fixture manifest, page `021+`, or whole Gate
1 acceptance is created.

Follow-up: Bogdan accepted `G1UNFPR-G1-VIRAL-001` with the exact bounded
decision phrase `g1unfpr candidate ok; proceed to prepare unsupported/negative
fixture policy acceptance record; no fixture admission, no whole Gate 1
acceptance, no page 021+, no push`. `G1UNFPAR-G1-VIRAL-001` records the
unsupported/negative fixture policy decision over exactly four questions:
unsupported profile scope, negative fixture obligations, invalidation
conditions, and fixture-admission dependency.

Boundaries after acceptance: only the unsupported/negative fixture policy
decision blocker is resolved. Fixture strategy fit, fixture admission readiness,
whole Gate 1 readiness, and page `021+` separate authorization remain blocked;
no fixture is admitted, no fixture manifest is created, whole Gate 1 is not
accepted, and no push is authorized.

Follow-up: `G1FSFDP-G1-VIRAL-001` prepares fixture strategy fit decision
material after the unsupported/negative fixture policy decision. It asks whether
the draft fixture strategy fits the accepted Core 0.1 boundary, whether pages
001-020 may act as future positive fixture seed material, whether negative
fixture obligations cover the accepted policy, whether invalidation conditions
should stale the fit, and whether admission must remain blocked until fit
acceptance plus readiness refresh.

Boundaries after prep: no fixture strategy fit decision is created, no fixture
is admitted, no fixture manifest is created, page `021+` remains separate, and
whole Gate 1 remains unaccepted.

Follow-up: Bogdan accepted `G1FSFDP-G1-VIRAL-001` with the exact bounded
decision phrase `g1fsfdp packet ok; proceed to prepare fixture strategy fit
acceptance record over strategy_scope_fit, positive_fixture_seed_fit,
negative_fixture_coverage_fit, invalidation_dependency_fit, and
admission_dependency; no fixture admission, no fixture manifest, no whole Gate
1 acceptance, no page 021+, no push`. `G1FSFAR-G1-VIRAL-001` records the
fixture strategy fit decision over exactly five questions: strategy scope fit,
positive fixture seed fit, negative fixture coverage fit, invalidation
dependency fit, and admission dependency.

Boundaries after acceptance: only the fixture strategy fit decision blocker is
resolved. Fixture admission readiness refresh, whole Gate 1 readiness recheck,
and page `021+` separate authorization remain blocked; no fixture is admitted,
no fixture manifest is created, whole Gate 1 is not accepted, and no push is
authorized.

Follow-up: Bogdan authorized `fixture_admission_readiness_refresh` with the
exact bounded phrase `proceed with fixture_admission_readiness_refresh; no
fixture admission, no fixture manifest, no whole Gate 1 acceptance, no page
021+, no push`. `G1FARR-G1-VIRAL-001` consumes `G1SP-G1-VIRAL-017`,
`G1FARP-G1-VIRAL-001`, `G1UNFPAR-G1-VIRAL-001`, and `G1FSFAR-G1-VIRAL-001` to
refresh fixture admission readiness after accepted policy and strategy fit
decisions.

Boundaries after refresh: only the fixture admission readiness refresh blocker
is resolved. Fixture manifest prep, fixture admission decision, whole Gate 1
readiness recheck, and page `021+` separate authorization remain blocked; no
fixture is admitted, no fixture manifest is created, whole Gate 1 is not
accepted, and no push is authorized.

Follow-up: Bogdan chose to proceed in order and authorized
`fixture_manifest_prep` with the exact bounded phrase
`proceed with fixture_manifest_prep; no fixture admission, no whole Gate 1
acceptance, no page 021+, no push, commit`. `G1FMP-G1-VIRAL-001` consumes
`G1FARR-G1-VIRAL-001` and prepares the future fixture manifest shape: one
positive page-complete seed group for pages 001-020 and four negative fixture
groups from the accepted unsupported/negative policy.

Boundaries after manifest prep: no actual fixture manifest is created, no
fixture is admitted, whole Gate 1 is not accepted, page `021+` remains behind
separate authorization, and no push is authorized. The next bounded decision is
human review of `G1FMP-G1-VIRAL-001` as manifest prep only.

Follow-up: Bogdan accepted `G1FMP-G1-VIRAL-001` with the exact bounded decision
phrase `g1fmp packet ok; proceed to prepare fixture manifest acceptance record;
no fixture admission, no whole Gate 1 acceptance, no page 021+, no push,
commit`.
`G1FMR-G1-VIRAL-001` records the fixture manifest shape: one positive
page-complete seed group for pages 001-020 and four negative fixture groups
from the accepted unsupported/negative policy.

Boundaries after manifest acceptance: only fixture manifest review is resolved.
No fixture is admitted, whole Gate 1 is not accepted, page `021+` remains
behind separate authorization, and no push is authorized. The next bounded
decision is fixture admission decision prep.

Follow-up: Bogdan authorized `fixture_admission_decision_prep` with the exact
bounded phrase `proceed with fixture_admission_decision_prep; no fixture
admission, no whole Gate 1 acceptance, no page 021+, no push, commit`.
`G1FADP-G1-VIRAL-001` consumes `G1FMR-G1-VIRAL-001` and prepares fixture
admission decision questions over positive fixture group admission scope,
negative fixture group admission scope, invalidation/lineage blockers,
admission decision boundary, and whole Gate 1 dependency.

Boundaries after fixture admission decision prep: no fixture admission decision
is created, no fixture is admitted, whole Gate 1 is not accepted, page `021+`
remains behind separate authorization, and no push is authorized. The next
bounded decision is human review of `G1FADP-G1-VIRAL-001` as decision-prep
only.

Follow-up: Bogdan accepted `G1FADP-G1-VIRAL-001` with the exact bounded phrase
`g1fadp packet ok; proceed to prepare fixture admission decision acceptance
record; no whole Gate 1 acceptance, no page 021+, no push`.
`G1FADAR-G1-VIRAL-001` records the fixture admission decision and admits the
fixture manifest groups: the positive pages 001-020 seed group plus the four
negative fixture groups.

Boundaries after fixture admission decision acceptance: only the fixture
admission decision blocker is resolved. Whole Gate 1 is not accepted, page
`021+` remains behind separate authorization, and no push is authorized. At
that checkpoint, the next bounded decision was whole Gate 1 acceptance
readiness recheck.

Follow-up: Bogdan replied `Ок делай` to the bounded proposal to prepare whole
Gate 1 acceptance readiness recheck with no whole Gate 1 acceptance, no page
`021+`, no source-profile acceptance, no OCR/render/PDF/raw mutation, no
translation/proofreading/implementation, no push, and commit.
`G1WGARR-G1-VIRAL-001` consumes `G1FADAR-G1-VIRAL-001` and prepares review
questions for the whole Gate 1 acceptance scope, page `021+` boundary,
acceptance-record boundary, and downstream boundary.

Boundaries after readiness recheck prep: whole Gate 1 remains unaccepted, whole
source-profile acceptance remains uncreated, page `021+` remains behind
separate authorization, no new or broader fixture admission is created, and no
push is authorized.

Follow-up: Bogdan accepted `G1WGARR-G1-VIRAL-001` with the exact bounded phrase
`g1wgarr packet ok; proceed to prepare whole Gate 1 acceptance decision record limited to pages 001-020 and G1FADAR admitted fixture manifest groups; no page 021+, no source-profile acceptance beyond this Gate 1 record, no OCR/render/PDF/raw mutation, no translation/proofreading/implementation, no push, commit`.
`G1WGADR-G1-VIRAL-001` records whole Gate 1 acceptance limited to pages 001-020
and the `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups.

Boundaries after whole Gate 1 acceptance: page `021+` remains behind separate
authorization, source-profile acceptance beyond this Gate 1 record remains
uncreated, no new or broader fixture admission is created, no downstream
execution is authorized, and no push is authorized.

## 2026-07-14: Create Sourcefold As A New Product

Status: accepted for scaffold.

Decision: Sourcefold is a new NRI product, not a rename or copy of
`translator`.

Rationale: the product boundary must start cleanly around source truth,
faithful Russian translation, and proofreading acceptance without inheriting
legacy publishing, package, or knowledge-base assumptions.

## 2026-07-14: Core Modules And Optional Lanes

Status: accepted for scaffold.

Decision: core modules are `reconstruct`, `translate`, and `proofread`.
Optional lanes are `press` and `bridge`. Knowledge base work is future separate
scope.

Rationale: a single modular product preserves provenance across stages while
keeping publication and integration downstream of accepted text.

## 2026-07-14: Adopt NRI Goal Governance

Status: accepted for scaffold.

Decision: Sourcefold uses project-local bundled goals under `docs/plans/` from
the first scaffold.

Rationale: context ownership, compact task packets, immutable handoffs, and
event-driven recovery are required before Sourcefold accumulates operational
history.

## 2026-07-15: Start Phase 0 As Charter-Only Goal

Status: accepted for planning.

Decision: Phase 0 starts as a release-charter and contract-decision goal. It
must not implement modules or run real book processing.

Rationale: Sourcefold must define first-release scope, acceptance vocabulary,
artifact lineage, trace anchors, waivers, fixtures, and release evidence before
producing plausible artifacts.


## 2026-07-17T17:21:29Z - doc-checkpoint-20260717T172129Z

- Gate 1 Qualification Protocol revision 5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a / file blob 4d494e83d8d63dd3778a3813b3ee529449cee51a is accepted as accepted_protocol for methodology only.
- Bounded authorization BA-G1-VIRAL-SPM-001 authorizes only selected-page manifest creation for Viral ordinal pages 1-20 using already recorded candidate identity; rendering, OCR, mapping, benchmarks, QA, fixtures, source acceptance, translation, proofreading, and implementation remain blocked.

## 2026-07-17T17:25:18Z - doc-checkpoint-20260717T172518Z

- Selected-page manifest SPM-G1-VIRAL-001 was created under BA-G1-VIRAL-SPM-001 for Viral ordinal pages 1-20 using already recorded candidate identity only.
- BA-G1-VIRAL-SPM-001 is scope-consumed and cannot authorize render, OCR, mapping, benchmarks, QA, fixtures, source acceptance, translation, proofreading, or implementation.

## 2026-07-17T17:47:29Z - doc-checkpoint-20260717T174729Z

- Bounded render authorization BA-G1-VIRAL-RENDER-001 was executed only for SPM-G1-VIRAL-001 ordinal pages 1-20 using PyMuPDF 1.27.2.3 at 300 DPI RGB PNG.

## 2026-07-27T21:50:00Z - doc-checkpoint-20260727T215000Z

- `G1SPRPDREV-G1-VIRAL-001` accepts `G1SPRPD-G1-VIRAL-001` as decision-prep only and authorizes preparing the next source-profile options packet.
- `G1SPDP-G1-VIRAL-001` prepares five future Gate 1 source-profile decision options for human review; it creates no source-profile acceptance, no parking decision, no fixture admission, no page 021+ authorization, no OCR/remediation execution, and no whole Gate 1 acceptance.
- Render trial RT-G1-VIRAL-RENDER-001 produced 20 PNG page images and output manifest SHA-256 622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC.
- BA-G1-VIRAL-RENDER-001 is scope-consumed and cannot authorize OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## 2026-07-27T22:15:00Z - doc-checkpoint-20260727T221500Z

- `G1SPDR-G1-VIRAL-001` records Bogdan's contextual approval of the immediately preceding `G1SPDP` proposal; the record preserves the assistant proposal and Bogdan's raw `ок` separately.
- The record accepts 5 selected rows as Gate review candidates only, parks 2 OCR methodology/debt rows for Core 0.1 with invalidation conditions, keeps 2 render/source-reconstruction rows evidence-only, keeps unsupported/negative fixtures and whole Gate 1 blocked, and keeps page 021+ behind separate bounded authorization.
- It does not accept whole source profile, admit fixtures, accept whole Gate 1, authorize/process page 021+, execute OCR/remediation, mutate source/OCR/render/PDF/raw assets, translate, proofread, implement, or push.

## 2026-07-27T22:45:00Z - doc-checkpoint-20260727T224500Z

- `G1FARP-G1-VIRAL-001` prepares fixture-admission / whole-Gate-acceptance readiness only from `G1SPDR-G1-VIRAL-001`.
- It preserves 5 Gate review candidate rows, 2 existing Core 0.1 OCR parking outcomes with invalidation conditions, 2 evidence-only rows, 2 blocked rows, and 1 page 021+ separate-BA row.
- Fixture admission readiness and whole Gate 1 acceptance readiness remain `not_ready_requires_future_decision`; unsupported/negative fixture policy remains `blocked_needs_future_decision`.
- It does not admit fixtures, create fixture manifests, accept whole Gate 1, accept whole source profile, authorize/process page 021+, execute OCR/remediation, mutate source/OCR/render/PDF/raw assets, translate, proofread, implement, push, or create downstream action.

## 2026-07-17T18:03:29Z - doc-checkpoint-20260717T180329Z

- Bounded visual sanity authorization BA-G1-VIRAL-VISUAL-001 produced VSR-G1-VIRAL-001 for RT-G1-VIRAL-RENDER-001 as non-accepting inventory evidence only.
- BA-G1-VIRAL-VISUAL-001 is scope-consumed and cannot authorize OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## 2026-07-17T18:26:26Z - doc-checkpoint-20260717T182626Z

- Bounded page inventory authorization BA-G1-VIRAL-PAGEINV-001 produced PIR-G1-VIRAL-001 for RT-G1-VIRAL-RENDER-001 as non-accepting page-level inventory evidence only.
- BA-G1-VIRAL-PAGEINV-001 is scope-consumed and cannot authorize OCR, map, region registry, anchors, reading order, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## 2026-07-17T20:55:30Z - doc-checkpoint-20260717T205530Z

- Bounded page-map/model authorization BA-G1-VIRAL-PAGEMAP-001 produced PMR-G1-VIRAL-001 for RT-G1-VIRAL-RENDER-001 as non-accepting page-level planning evidence only.
- BA-G1-VIRAL-PAGEMAP-001 is scope-consumed and cannot authorize doc_map, content_map, art_map, pre_ocr_map_bundle freezing, OCR, region registry, anchors, reading order, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## 2026-07-17T21:20:08Z - doc-checkpoint-20260717T212008Z

- Bounded region-map authorization BA-G1-VIRAL-REGIONMAP-001 produced PRM-G1-VIRAL-001 as non-accepting provisional annotation evidence only.
- BA-G1-VIRAL-REGIONMAP-001 is scope-consumed and cannot authorize pre_ocr_map_bundle freezing, OCR, accepted anchors, accepted reading order, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## 2026-07-18T04:48:21Z - doc-checkpoint-20260718T044821Z

- BA-G1-VIRAL-MAPBUNDLE-PREQ-001 produced MBR-G1-VIRAL-001 as non-accepting prerequisite review only; it does not create or freeze pre_ocr_map_bundle.
- A real pre_ocr_map_bundle freeze remains blocked until exact doc_map, content_map, art_map, schema, and shared identity predecessors exist.

## 2026-07-18T05:41:58Z - doc-checkpoint-20260718T054158Z

- BA-G1-VIRAL-MAPSCHEMA-001 produced MSID-G1-VIRAL-001 as non-accepting version-bound provisional schema/shared identity evidence only.
- MSID-G1-VIRAL-001 may support future separately authorized non-accepting map-layer trials, but cannot create map payloads or freeze pre_ocr_map_bundle by itself.

## 2026-07-18T05:45:17Z - doc-checkpoint-20260718T054517Z

- BA-G1-VIRAL-DOCMAP-001 produced DM-G1-VIRAL-001 as non-accepting trial doc-map registry evidence only.
- DM-G1-VIRAL-001 may support future separately authorized content_map/art_map trials, but cannot freeze pre_ocr_map_bundle or authorize OCR by itself.

## 2026-07-18T05:47:48Z - doc-checkpoint-20260718T054748Z

- BA-G1-VIRAL-CONTENTMAP-001 produced CM-G1-VIRAL-001 as non-accepting trial content-map evidence only.
- CM-G1-VIRAL-001 may support future separately authorized art-map/consistency/bundle steps, but cannot freeze pre_ocr_map_bundle or authorize OCR by itself.

## 2026-07-18T05:50:19Z - doc-checkpoint-20260718T055019Z

- BA-G1-VIRAL-ARTMAP-001 produced AM-G1-VIRAL-001 as non-accepting trial art-map evidence only.
- AM-G1-VIRAL-001 may support future separately authorized map consistency and bundle steps, but cannot freeze pre_ocr_map_bundle or authorize OCR by itself.

## 2026-07-18T05:52:34Z - doc-checkpoint-20260718T055234Z

- BA-G1-VIRAL-MAPCONSISTENCY-001 produced MCV-G1-VIRAL-001 as non-accepting cross-map consistency validation only.
- MCV-G1-VIRAL-001 may support a future separately authorized pre_ocr_map_bundle freeze, but cannot freeze the bundle or authorize OCR by itself.

## 2026-07-18T05:54:39Z - doc-checkpoint-20260718T055439Z

- BA-G1-VIRAL-MAPBUNDLE-001 produced POMB-G1-VIRAL-001 as frozen_for_review pre-OCR map bundle lineage only.
- POMB-G1-VIRAL-001 is not_admitted_for_ocr and cannot authorize OCR prep, OCR benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation by itself.

## 2026-07-18T05:57:01Z - doc-checkpoint-20260718T055701Z

- BA-G1-VIRAL-OCRPREP-001 produced OPR-G1-VIRAL-001 as OCR preparation evidence only.
- OPR-G1-VIRAL-001 cannot authorize OCR execution, benchmark scoring, gold text creation, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation by itself.

## 2026-07-18T05:59:44Z - doc-checkpoint-20260718T055944Z

- BA-G1-VIRAL-OCRBENCH-PREQ-001 produced OBR-G1-VIRAL-001 as OCR benchmark prerequisite review only.
- OCR benchmark execution is blocked until gold-sample creation and OCR candidate manifest/config are separately authorized and frozen.

## 2026-07-18T06:10:27Z - doc-checkpoint-20260718T061027Z

- BA-G1-VIRAL-GOLDSAMPLE-001 produced GSM-G1-VIRAL-001 as gold-sample evidence for review only, not accepted source text.
- BA-G1-VIRAL-OCRCANDIDATE-001 produced OCM-G1-VIRAL-001 with status blocked_missing_executable; OCR benchmark execution remains blocked until OCR engine provisioning/freeze occurs.

## 2026-07-18T07:09:17Z - doc-checkpoint-20260718T070917Z

- BA-G1-VIRAL-OCRCANDIDATE-002 refreshed OCM-G1-VIRAL-001 with local Tesseract executable/version/language-data identity and status candidate_config_frozen_for_review.
- OCM-G1-VIRAL-001 still cannot authorize OCR benchmark execution, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement by itself.

## 2026-07-18T07:51:38Z - doc-checkpoint-20260718T075138Z

- BA-G1-VIRAL-OCRBENCH-001 produced non-accepting benchmark evidence only: ORB-G1-VIRAL-001, OOM-G1-VIRAL-001, and OBR-G1-VIRAL-002.
- The first OCR benchmark result recommends remediation before Gate 1 review and cannot authorize QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement.

## 2026-07-18T12:03:41Z - doc-checkpoint-20260718T120341Z

- BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001 produced SRVO-G1-VIRAL-001 as visual/overlay review decisions only.
- SRVO-G1-VIRAL-001 closes the SRRB visual, overlay, and full-region replacement blockers for later human review, but candidate text remains not source-accepted and cannot authorize QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.

## 2026-07-18T12:20:03Z - doc-checkpoint-20260718T122003Z

- BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001 produced SRHP-G1-VIRAL-001 as a human-review package only.
- SRHP-G1-VIRAL-001 is ready for Bogdan human review, but it is not source acceptance and cannot authorize QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.

## 2026-07-18T13:36:56Z - doc-checkpoint-20260718T133656Z

- BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001 produced SRHR-G1-VIRAL-001 as Bogdan's page-by-page human source review record.
- SRHR-G1-VIRAL-001 records all seven numbered decisions: four candidate-text records source-review accepted and three visual-only exclusions accepted.
- R003 records the corrected full-crop resend before acceptance and preserves Bogdan's semantic heading hint as review metadata, not a source-text mutation.
- SRHR-G1-VIRAL-001 is source review acceptance only and cannot authorize QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.

## 2026-07-18T13:59:19Z - doc-checkpoint-20260718T135919Z

- BA-G1-VIRAL-SOURCE-RECON-QA-001 produced SRQA-G1-VIRAL-001 from exact SRHR-G1-VIRAL-001 report and accepted-text hashes.
- SRQA-G1-VIRAL-001 passes source reconstruction QA for four source-text records and three visual-only exclusions, with zero blocked records.
- SRQA-G1-VIRAL-001 preserves the R003 corrected-full-crop note and semantic heading hint as QA metadata.
- SRQA-G1-VIRAL-001 is QA acceptance for this source reconstruction slice only and cannot authorize fixtures, translation, proofreading, implementation, or Gate 1 advancement.

## 2026-07-18T14:27:41Z - doc-checkpoint-20260718T142741Z

- BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001 produced SRFA-G1-VIRAL-001 from exact SRQA-G1-VIRAL-001 report and summary hashes.
- SRFA-G1-VIRAL-001 admits four positive source-text fixtures and three negative visual-exclusion fixtures as stable downstream test inputs.
- SRFA-G1-VIRAL-001 preserves R003 corrected-full-crop metadata and Bogdan's semantic heading hint as fixture metadata.
- SRFA-G1-VIRAL-001 does not authorize translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement.

## 2026-07-18T14:51:18Z - doc-checkpoint-20260718T145118Z

- BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001 produced G1RP-G1-VIRAL-001 from exact SRFA-G1-VIRAL-001 report, fixtures, and summary hashes.
- G1RP-G1-VIRAL-001 packages all seven admitted source reconstruction fixtures for Gate 1 review: four positive source-text items and three negative visual-exclusion items.
- G1RP-G1-VIRAL-001 preserves R003 corrected-full-crop metadata and Bogdan's semantic heading hint as packet metadata.
- G1RP-G1-VIRAL-001 is review-packet readiness only and does not authorize Gate 1 advancement, translation, proofreading, renderer/profile acceptance, or implementation.

## 2026-07-18T15:00:16Z - doc-checkpoint-20260718T150016Z

- BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001 produced G1RDB-G1-VIRAL-001 from exact G1RP-G1-VIRAL-001 report, manifest, payload, and summary hashes.
- G1RDB-G1-VIRAL-001 prepares one numbered decision question for Bogdan with accept, hold, reject, and park answer shapes.
- G1RDB-G1-VIRAL-001 includes accepted protocol revision, G1RP/SRFA/SRQA lineage, and a non-waivable checklist.
- G1RDB-G1-VIRAL-001 requires Bogdan review and does not record a Gate 1 decision or advancement.

## 2026-07-18T15:28:14Z - doc-checkpoint-20260718T152814Z

- BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001 produced G1RD-G1-VIRAL-001 from exact G1RDB-G1-VIRAL-001 report, JSON, and Markdown hashes.
- G1RD-G1-VIRAL-001 records Bogdan's Telegram message 303 decision: "1 принято".
- G1RD-G1-VIRAL-001 accepts only the exact seven reviewed source reconstruction records from G1RP-G1-VIRAL-001; pages are not accepted as complete and whole Gate 1 is not accepted.
- G1RD-G1-VIRAL-001 does not authorize translation, proofreading, renderer/profile acceptance, implementation, push, OCR, PDF parsing, rendering, or raw OCR mutation.

## 2026-07-18T16:37:25Z - doc-checkpoint-20260718T163725Z

- BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001 produced G1SRER-G1-VIRAL-001 from exact G1RD-G1-VIRAL-001 report, record, Markdown, and summary hashes.
- G1SRER-G1-VIRAL-001 carries the seven-record Gate 1 source reconstruction evidence slice forward as status input without accepting pages 001/005/006 as complete.
- G1SRER-G1-VIRAL-001 preserves whole_gate_1_acceptance=false and requires explicit scope labeling when reused.
- G1SRER-G1-VIRAL-001 does not authorize translation, proofreading, renderer/profile acceptance, implementation, push, OCR, PDF parsing, rendering, or raw OCR mutation.

## 2026-07-18T17:44:35Z - doc-checkpoint-20260718T174435Z

- BA-G1-VIRAL-GATE-1-STATUS-PACKET-001 produced G1SP-G1-VIRAL-001 from exact G1SRER-G1-VIRAL-001 report, manifest, payload, and summary hashes.
- G1SP-G1-VIRAL-001 summarizes current Gate 1 state as one accepted/rolled-up seven-record source reconstruction slice plus pending broader work.
- G1SP-G1-VIRAL-001 preserves accepted_pages_as_complete=false, page_complete_acceptance=false, whole_gate_1_acceptance=false, and new_gate_1_advancement_created=false.
- G1SP-G1-VIRAL-001 does not authorize translation, proofreading, renderer/profile acceptance, implementation, push, OCR, PDF parsing, rendering, or raw OCR mutation.

## 2026-07-18T18:27:56Z - doc-checkpoint-20260718T182756Z

- BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001 produced SRNS-G1-VIRAL-002 from exact G1SP-G1-VIRAL-001 status hashes, PRM-G1-VIRAL-001 region hints, and existing page_002.png.
- SRNS-G1-VIRAL-002 creates two page-002 crop references for Bogdan review: PRM-G1-VIRAL-001-P002-R01 and PRM-G1-VIRAL-001-P002-R02.
- SRNS-G1-VIRAL-002 creates no candidate text and does not accept page 002, source text, QA, fixtures, or Gate 1.
- SRNS-G1-VIRAL-002 does not authorize OCR, PDF parsing/rendering, raw OCR mutation, translation, proofreading, renderer/profile acceptance, implementation, or push.

## 2026-07-18T19:55:40Z - doc-checkpoint-20260718T195540Z

- BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-001 produced SRAD-G1-VIRAL-002 from exact SRNS-G1-VIRAL-002 report and manifest hashes.
- SRAD-G1-VIRAL-002 records Bogdan's messages 351 and 356 as a route decision: both page-002 regions contain text, but manual transcription is blocked because the text is too long and the earlier corrected crop over-included the lower block.
- SRAD-G1-VIRAL-002 creates corrected split crop references and assisted draft text for Bogdan verification only.
- SRAD-G1-VIRAL-002 does not accept source text, page 002 as complete, QA, fixtures, Gate 1, OCR execution, PDF parsing/rendering, raw OCR mutation, translation, proofreading, renderer/profile acceptance, implementation, or push.

## 2026-07-18T20:25:35Z - doc-checkpoint-20260718T202535Z

- BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-HUMAN-VERIFY-001 produced SRADV-G1-VIRAL-002 from exact SRAD-G1-VIRAL-002 report, manifest, and assisted draft Markdown hashes.
- SRADV-G1-VIRAL-002 records Bogdan's Telegram message 377: 1 ok, 2 ok, headings ignored, text OK.
- SRADV-G1-VIRAL-002 verifies only the two assisted page-002 draft text records against corrected crops.
- SRADV-G1-VIRAL-002 does not accept source text, page 002 as complete, QA, fixtures, Gate 1, OCR execution, PDF parsing/rendering, raw OCR mutation, translation, proofreading, renderer/profile acceptance, implementation, or push.

## 2026-07-18T21:07:54Z - doc-checkpoint-20260718T210754Z

- Added page_002_qa_structure_evaluation_packet.md as Bogdan-facing evaluation material for the post-SRADV path.
- Packet SHA-256: F261CB0035BB588A5F347A0BE30C7E7E0E8910BE505E3C913357A539E93F11BA.
- Recommended path: SRADV QA, then page-002 structure/semantics, then structure QA, then a separate source acceptance decision if authorized.
- The proposed structure model separates semantic roles from heading levels and presentation flags such as bold, italic, underline, centered, small-caps, and font scale.
- The packet is planning/evaluation material only and does not accept source text, structure, QA, fixtures, page 002 as complete, whole Gate 1, renderer/profile behavior, implementation, or push.

## 2026-07-18T21:44:29Z - doc-checkpoint-20260718T214429Z

- BA-G1-VIRAL-P002-QA-STRUCTURE-SOURCE-AND-NEXT-REVIEW-001 produced `P002C-G1-VIRAL-002` from exact `SRADV-G1-VIRAL-002` report, manifest, and summary hashes.
- `P002C-G1-VIRAL-002` records `SRADQ-G1-VIRAL-002`, `SRSS-G1-VIRAL-002`, `SRSSQ-G1-VIRAL-002`, `SRSA-G1-VIRAL-002`, and `G1SRER-G1-VIRAL-002`.
- `SRSA-G1-VIRAL-002` accepts exactly two page-002 source reconstruction records as a narrow slice; page 002 is not accepted as complete and whole Gate 1 is not accepted.
- `SRCR-G1-VIRAL-003` prepares remediated page-003 draft visual transcription text, draft structure/semantics, and two crop references for Bogdan review only after Bogdan message `430` reported the initial crop cut text.
- `SRCRV-G1-VIRAL-003` records Bogdan message `437`: `1 ок`, `2 ок`; this verifies the remediated draft packet but does not accept source text.
- Report SHA-256: A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F.
- Manifest SHA-256: 8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6.
- Next review packet SHA-256: 81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF.
- No fixture admission, page-complete acceptance, whole-Gate acceptance, translation, proofreading, renderer/profile acceptance, implementation, or push is authorized.

## 2026-07-18T22:39:26Z - doc-checkpoint-20260718T223926Z

- BA-G1-VIRAL-P003-QA-SOURCE-ACCEPTANCE-001 produced `P003A-G1-VIRAL-003` from exact `P002C-G1-VIRAL-002` report, manifest, and next-review-packet hashes.
- `P003A-G1-VIRAL-003` records `SRCRQ-G1-VIRAL-003`, `SRCG-G1-VIRAL-003`, `SRSA-G1-VIRAL-003`, and `G1SRER-G1-VIRAL-003`.
- `SRSA-G1-VIRAL-003` accepts exactly two page-003 source reconstruction records as a narrow slice; page 003 is not accepted as complete and whole Gate 1 is not accepted.
- `SRCG-G1-VIRAL-003` now consumes predecessor global crop layout evidence `SRCG-GLOBAL-CROP-BOX-LAYOUT-001`: approved boxes, crop overlap, and too-small gutters are blockers.
- Report SHA-256: 9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B.
- Manifest SHA-256: F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87.
- Summary SHA-256: 860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2.
- No fixture admission, page-complete acceptance, whole-Gate acceptance, translation, proofreading, renderer/profile acceptance, implementation, or push is authorized.

## 2026-07-19T16:23:34Z - doc-checkpoint-20260719T162334Z

- BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004 produced `SRCR-G1-VIRAL-004` from exact `P003A-G1-VIRAL-003` report, manifest, and summary hashes.
- `SRCR-G1-VIRAL-004` prepares a page-004 review-only packet with draft text, structure/semantics, and two padded crop references for Bogdan numbered review.
- `PRM-G1-VIRAL-001-P004-R01` is context-only because it contains the title/body regions and would overlap peer crop records under `SRCG-GLOBAL-CROP-BOX-LAYOUT-001`.
- Crop layout guardrail passed for `SRCR-G1-VIRAL-004-R01` and `SRCR-G1-VIRAL-004-R02`; approved boxes, overlap, and too-small gutters remain blockers.
- Report SHA-256: C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A.
- Manifest SHA-256: 30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4.
- Human review packet SHA-256: 1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446.
- No source acceptance, QA acceptance, fixture admission, page-complete acceptance, whole-Gate acceptance, translation, proofreading, renderer/profile acceptance, implementation, or push is authorized.

## 2026-07-19T17:45:26Z - doc-checkpoint-20260719T174526Z

- BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004-HUMAN-VERIFY-001 recorded Bogdan Telegram message `523`: `1 ok / 2 ok`.
- `SRCRV-G1-VIRAL-004` verifies exactly the two draft page-004 review records from `SRCR-G1-VIRAL-004`.
- Verification report SHA-256: 95041F808A1C2F44A417245BF3E25318C9BDE36183CCE7C4E372DF9363812FBA.
- Verification manifest SHA-256: 21B3CE0135D4D8CF09C394C192D7976766DA9DA1E55DE5F9B3FE240380CC0AB0.
- Verification summary SHA-256: F342D7DA0CBB7245812B8B3291F2C5585D880DA67D6C24DCAFEC4FF8B86D9011.
- No source acceptance, QA acceptance, fixture admission, page-complete acceptance, whole-Gate acceptance, translation, proofreading, renderer/profile acceptance, implementation, or push is authorized.

## 2026-07-19T18:26:26Z - doc-checkpoint-20260719T182626Z

- BA-G1-VIRAL-P004-QA-SOURCE-ACCEPTANCE-001 consumed exact `SRCR-G1-VIRAL-004` and `SRCRV-G1-VIRAL-004` hashes.
- `P004A-G1-VIRAL-004` records `SRCRQ-G1-VIRAL-004`, `SRCG-G1-VIRAL-004`, `SRSA-G1-VIRAL-004`, and `G1SRER-G1-VIRAL-004`.
- Exactly two page-004 records are source accepted; accepted source reconstruction records roll up from 11 to 13.
- Acceptance report SHA-256: 0CCB4AA33481BDB0B95B02D32A0E49FB1A20FD9A957DB7DAE1ECB0B00307622E.
- Acceptance manifest SHA-256: 75C0C0BD96FF77E64D2F7C827D7D21B12F7EF15964E8EC9734F9428CCC064C06.
- Acceptance summary SHA-256: BF664162A899765C3B614F87002792D213D70DB82A7ED4142686AA439D50C64C.
- Page 004 is not accepted as complete; page 002/003 remain incomplete; whole Gate 1, fixture admission, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked.

## 2026-07-19T20:15:58Z - doc-checkpoint-20260719T201558Z

- BA-G1-VIRAL-PAGE-COMPLETENESS-TRIAGE-001 produced `PGCT-G1-VIRAL-001` as a page-completeness triage/status packet for selected pages 1-20.
- The packet classifies pages 002 and 003 as ready for later separate page-complete review packets, page 004 as held pending a context-only decision for the full tilted inset, pages 001/005/006 as incomplete, and pages 007-020 as unstarted for source-reconstruction acceptance.
- Triage report SHA-256: EFDEBCC6ABBE916086887572D400DA9AAF41257F910D55AAF4D337BE386F550F.
- Human-facing packet SHA-256: 7BF4017A17D40BFAF8A6FE478E41234E4B8BE0889C6067B3BE7F3C890E85BB9A.
- This is triage/status only; no page-complete acceptance, whole-Gate acceptance, fixture admission, source acceptance, translation, proofreading, renderer/profile acceptance, implementation, push, OCR, PDF parsing/rendering, or raw OCR mutation is authorized.
