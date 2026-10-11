# A1 Sourcefold architecture and current-state map

- Goal: `20261011-sourcefold-model-handoff`; step: `A1`.
- Role: `nri-architect`; assigned model/effort `gpt-6-astra` / high; independently verified runtime model/effort unavailable.
- Orchestrator policy owner: main chat, `gpt-6-sol` / medium. Ownership remains there.
- Assignment state: `platform-unverified`; scoped override: none.
- Scope: read-only product, architecture, current state, dependencies, precedence, inherited gaps and handoff recommendations. Sole write: this immutable receipt.
- Baseline: `7c880d60320ba11c7a80f62fb804722cfac1548b`, independently observed at local HEAD; repository `C:/_Hobby/_work/Sorceforge`, product `Sourcefold/`.
- Result: completed architecture analysis. No implementation or final release decision.
- Timestamp: `2026-10-11T20:30:00Z` (drafting time, approximate to minute). Elapsed approximately 5 minutes; exact time/token metering unavailable.

## 1. Product definition and actual implementation boundary

Sourcefold's intended deliverable is an accepted Russian text master whose source meaning, layout structure and data survive three distinct contracts:

`immutable source evidence -> reconstruct -> Accepted Source Text -> translate -> Faithful RU Draft -> proofread -> Proofread RU Master`.

`press` optionally projects the accepted master to Markdown/HTML/PDF; `bridge` optionally exports accepted artifacts to declared external systems. Neither can repair or hide an unaccepted predecessor. KB generation, cross-book rules integration and RuleAtlas are future separate directions. `translator` is historical lessons/reference material; it is not the implementation namespace, runtime dependency or current governance inherited by this product.

Authority: `Sourcefold/docs/architecture/product_boundary.md`, `module_contracts.md`, the five Markdown contracts under `Sourcefold/contracts/`, and `Sourcefold/docs/quality/acceptance_criteria.md`.

Current implementation is an extensive Phase 0 source-qualification and reconstruction evidence workbench: bounded Python producers/validators, semantic/page contracts, OCR probes, candidate comparison, human review/admission/decision records and a planning validator. It is not merely an empty documentation scaffold, but neither is it a delivered general-purpose reconstruct/translate/proofread engine. The module contracts state target inputs/outputs and acceptance rules; their existence does not establish completed runtime implementations. No completed Sourcefold whole-book Russian master or deployed translation/proofreading service is evidenced by the inspected current state.

The architecture is a governed artifact DAG with revision/supersession and backward remediation, not a one-way wizard. Normal execution is individual scripts with explicit authorization and exact evidence inputs; the inspected package metadata provides only a roadmap-validation npm command, not a universal book-processing CLI.

## 2. What has actually happened

### Completed foundations

The Active Goals table in `PROJECT_STATUS.md` lists six completed foundation goals: initial scaffold; high-level release roadmap; version ladder 0.1-to-1.0; YAML roadmap viewer; documentation checkpoint helper; package-backed roadmap validator. The original ten-step Phase 0 bootstrap is recorded complete, but the Phase 0 release-charter goal remains active.

The governed Viral source PDF and selected-page evidence were admitted into progressively bounded fixture/reconstruction workflows. Real rendering/OCR probes, semantic reconstruction, page-complete review and accepted page records exist. Current input/evidence preservation is intentional, including failed attempts and quarantined/superseded runs.

### Qualification, OCR and selector history

Use `TRIAL = Sourcefold/fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/` below; this is an abbreviation for paths in this receipt, not a new directory.

1. Page/region geometry, readable semantic maps and page-complete review became separate evidence types. Human-review crops were discovered to be unsafe as automatic OCR inputs, especially for complex P017/P018 layouts.
2. `scripts/ocr_input_surface_policy.py` implements a static contract/router: review crops versus candidate crops/full-page regions; explicit authority for full-page regions; page 021+ rejection; candidate/reference separation; quarantine of incomplete artifacts; distinct sequence-similarity and token-recall diagnostics. P018 control numbers are observations, not universal acceptance thresholds.
3. P013 diagnostic iterations tested seam dedupe, non-overlap geometry, lane ordering, structural suppression and closure. Later candidate discovery/selector records reference sealed best candidates. P012/P016/P020 method-family probes and P017/P018 geometry probes supplied other candidate records.
4. Static selector replay progressed to all-20-page evidence coverage by bridging accepted page-complete records for pages without fresh OCR success. That coverage did not authorize production assembly.
5. `TRIAL/core_0_1_text_extraction_first_pass_runtime_selector_run_001_020_G1_VIRAL_001/first_pass_runtime_selector_run_001_020_report.json` records actual materialized output for all twenty pages, fresh OCR execution on only `009`, `010`, `011`, `015`, ten bridge-lineage pages (`001`-`008`, `014`, `019`), and remaining selected candidates reused by hash. It explicitly records `all_pages_fresh_ocr_success=false`, `production_ready=false`, `production_assembly_authorized=false`.
6. Later bridge-remediation/reference-authority lanes separated P003/P004 higher-authority comparisons, P005-P008 comparison-only remediation, and poor P014/P019 full-page OCR diagnostics. These lanes must not be summarized as source acceptance merely because comparison inputs or metrics improved.
7. Latest detailed P002 sequence materialized/reviewed a source surface, ran fresh OCR, audited reference authority, applied bounded human-verified remediation, and recorded `C01TEP002FRESHPASS-G1-VIRAL-001`. Its report at `TRIAL/core_0_1_text_extraction_p002_fresh_ocr_pass_decision_G1_VIRAL_001/p002_fresh_ocr_pass_decision_report.json` records `fresh_ocr_success_pages=["002"]`, `bridge_removed_for_pages=["002"]`, `promotable_pages=["002"]`. This is a scoped decision after remediation, not proof of autonomous first-pass OCR, general promotion, source acceptance or production assembly. Do not alter the earlier first-pass report to fold in later progress.

### Standalone export

Sourcefold was extracted from NRI `22fafc14942e925b2e5f088f3c7ab1cd8efe3003`, preserving nested `Sourcefold/`. Export review approved exact initial commit `c557381c119ec03d420a0121784a5e111ebd94e8` and administrative successor `161aec0a474ad5160a6a44a063e662f8ea182bad`. The current `7c880d6` commit records publication. Local history confirms that sequence. The assigned handoff baseline matched origin at main-chat preflight; A1 did not contact the remote and does not claim a new remote observation.

The export release was acceptance of a source/evidence snapshot with documented limitations, not a green full test suite, portable OCR runtime or product release.

## 3. Current Phase/Gate state: retain both levels

Live roadmap node values:

| Layer | Recorded state |
| --- | --- |
| Phase 0 release charter | `active` |
| Gate 1 Source Profile | `active` |
| Gate 1 qualification protocol | `active` |
| Gate 1 page-map readiness pipeline | `active` |
| Gate 1 pre-OCR map model | `proposed` |
| Source profile/canonical format/acceptance authority/artifact identity/trace anchors/waiver decisions | `active` |
| Core 0.1 RC | `planned` |
| Later Core beta/production stages | `proposed` |
| Press 0.6/Bridge 0.7 previews and broader OCR/KB parking | `deferred` |

Important exception to simplistic wording: `TRIAL/gate_1_whole_gate_acceptance_decision_G1_VIRAL_001/gate_1_whole_gate_acceptance_decision_summary.md` explicitly records `G1WGADR-G1-VIRAL-001`, **bounded whole Gate 1 acceptance for pages 001-020 and the G1FADAR admitted groups (one positive, four negative)**. It does not accept wider source-profile scope or authorize page 021+, OCR/render/source mutation, translation/proofreading or implementation.

Thus both statements must appear together: global Phase 0/Gate 1 planning remains active, while named page/fixture/Gate acceptance records exist within their finite scope. Saying either "Gate 1 is finished globally" or "Gate 1/fixtures have never been accepted" loses evidence. Whether the global roadmap should later be reconciled to a more refined scope is a separate canonical-state decision, not permission to change it during handoff analysis.

Do not treat old human decision phrases embedded in scripts/records as current executable authorization. New actions require the applicable exact action, admitted inputs, outputs, limits, authority, expiry/invalidation and review gates. Repositories can preserve historic authority without transferring permission to rerun it.

## 4. Architecture, contracts and truth boundaries

| Layer | Representative paths | Responsibility and failure boundary |
| --- | --- | --- |
| Policy/orchestration | root `AGENTS.md`, `docs/governance/nri_goal_governance.md`; `Sourcefold/AGENTS.md` | Main chat owns canonical plan/context/status, integration and user decisions. Contributors own only scoped receipts. Current role policy supersedes old model labels in historical plans/roadmap. Independent critic reviews the exact frozen candidate. |
| Product contract | `docs/architecture/product_boundary.md`, `module_contracts.md`; `contracts/*.md` | Accepted predecessors and explicit preservation/QA; optional press/bridge never bypass core acceptance. |
| Artifact schema | `manifests/artifact_manifest.schema.json` | Draft schema v0.1.0 records stage/type/input/output/tool/model/QA/acceptance metadata. File-ref SHA is optional in this generic schema, so schema conformance alone cannot prove complete lineage; stricter bounded producer contracts enforce exact hashes. |
| Qualification/decision model | Phase-0 `release_charter.md`, `phase_gate_component_hierarchy.md`, `gate_01_qualification_protocol.md`, `core_0_1_acceptance_matrix.md`, `acceptance_vocabulary.md`, `artifact_lineage_model.md` | `Phase -> Gate -> Component -> Subcomponent -> Parameter -> Evidence`. Some documents remain draft/proposed; do not describe their entire future design as accepted implementation. |
| Authorization/lifecycle/route | `scripts/bounded_authorization_contract.py`, `artifact_lifecycle_validation.py`, `route_cursor_transition.py`, `human_review_gate_contract.py` | Exact ledger-bound action and permitted transitions; stale/held/superseded evidence cannot be silently consumed as current; route/readiness cannot leak source/page/Gate acceptance authority. |
| Semantic/page reconstruction | `scripts/semantic_segmentation_contract.py`, `page_map_readiness.py`, `source_reconstruction_crop_guardrails.py`, page-specific builders/reviewers | JSON semantic payload is canonical; Markdown is a human projection. Regions/inventory/order/layout structures must reconcile before page-complete decisions. Non-waivable structure loss blocks acceptance. |
| OCR/candidate diagnosis | `scripts/ocr_input_surface_policy.py`, scoped `build_*`/`run_*` tools | Surface identity and geometry are explicit; candidate hashes precede reference scoring. Similarity/recall are diagnostic; reference-guided repair has declared support lineage. |
| Human/operator acceptance | `accept_*`, `record_*` scripts and sealed reports | Page complete, fixture admission, whole Gate scope and source-profile scope are different decisions. Acceptance names exact evidence and has no transitive widening. |
| Planning/checkpoints | `docs/roadmap/roadmap.yaml`, validator/viewer; `scripts/documentation_checkpoint.ps1` | YAML is the live planning authority; viewer is a reader. Checkpoint command defaults dry-run, `-Apply` changes canonical docs and is not a harmless inspection command. |

All script paths in the table are product-relative. The general data path is immutable PDF/page images -> geometry/layout/semantic inventory -> OCR observations -> ordered source candidates -> exact QA/human decision -> accepted artifact, with failed alternatives and supersession preserved. Source PDF text-layer comparison, diagnostic reference text, review PNGs and candidate metrics cannot masquerade as independent accepted source text.

Use distinct vocabulary: `passed` is a check result; `conformant` is machine-contract compliance; `accepted` is scoped human/operator acceptance; `released` binds an independently reviewed frozen candidate. `ready`, `coverage_summary`, `promotable` and materialized output do not imply these stronger states.

## 5. Repository map and count provenance

At baseline `7c880d6`, native Git enumeration verified **3987 tracked files**: 3981 under Sourcefold plus six root policy/entry files. Product inventory includes **193 docs**, **186 scripts**, **179 test files**, **3408 fixture files**, **five module contracts**, **one artifact manifest schema**, **one roadmap-validator tool**, plus eight top-level project files. These are baseline file counts, not test counts or new goal-file counts.

The original NRI boundary was 3974 Sourcefold paths; the export added seven goal documentation/receipt files under Sourcefold and six root files. All 3408 fixture paths were retained, 3404 under the single governed Viral render-trial root. Failed attempts and overlay-named evidence remain durable governed files. No cleanup should be inferred from their volume or generated appearance.

Recommended reading order for a new model:

1. Root README/AGENTS, `Sourcefold/AGENTS.md`, current `docs/governance/nri_goal_governance.md`, and root `NRI_OCR_LAYOUT_RULES.md`.
2. New model handoff summary, then `Sourcefold/README.md`, `SETUP.md` and the top current status checkpoint.
3. `Sourcefold/docs/architecture/product_boundary.md` and `module_contracts.md`; read only the module/acceptance contract relevant to the task.
4. `Sourcefold/docs/roadmap/roadmap.yaml` for node/dependency state; Phase-0 `plan.md`/`context.md`, hierarchy, qualification protocol and acceptance matrix for the chosen bounded lane.
5. Exact current lane plan plus report/manifest/predecessor references under the Viral TRIAL root; inspect relevant scripts/tests after identifying this boundary.
6. `Sourcefold/docs/plans/20261011-sourcefold-standalone-export/{context,release}.md` and Q1/R1 receipts for imported byte identity and known runtime/test limitations.

Do not start by rereading the thousand-line historical status/decision log end to end. The status has multiple historical "next" recommendations that later lanes supersede. Locate the latest relevant lane and exact predecessor first.

## 6. Source-of-truth precedence

1. Current direct user/task constraints and active root/project policy govern what is authorized; the main chat owns interpretation and integration.
2. The active goal's plan/context defines the current task and role ownership; published Git revision identifies what bytes are being described.
3. Exact accepted lane records, schemas, manifests, pinned payloads and implementation define evidence/acceptance for their specific scope. A stale prose sentence cannot overwrite a concrete bounded decision, and a label cannot defeat mismatching hashes.
4. Roadmap YAML governs planning-node state/dependencies; project status is a rollup/index, not an acceptance ledger. The Phase/Gate summary and scoped evidence can have different granularity and must both be reported.
5. Product/module documents explain intended contracts; identify draft versus accepted versus implemented sections.
6. Historical checkpoints, prior reviewer/model labels, generated `current_head` fields and old PIDs are provenance. They are not current branch/remote/process/authority truth. Viewer/Markdown projections do not override YAML/semantic JSON.

Where precedence surfaces disagree, preserve both facts and flag the narrow reconciliation required. Do not invent acceptance, patch historic receipts or infer a running process.

## 7. Technologies and inherited limitations

| Technology | Why used | Current limitation |
| --- | --- | --- |
| Python standard library | Explicit scripts, file/JSON/hash identity, subprocess execution, sealed report and predecessor checks | Many tools are bounded lane-specific producers, not a generalized production engine. |
| pytest | Contract negatives, exact evidence lineage, bounded output and authorization regressions | Python development dependencies are not locked; tests are not all green. |
| Pillow | Image dimensions, crop geometry, preprocessing and image-aware tests | A suitable local interpreter/dependency set must be discovered, not copied from a workstation. |
| Tesseract English OCR | Controlled OCR candidates with explicit OEM/PSM/profile and txt/TSV artifacts | Active historical tools/configs hardcode `D:\NRI\.tools\tesseract\tesseract.exe`. A reviewed runtime-discovery/rebinding contract is needed before future authorized execution. |
| Node/npm + locked `yaml@2.9.0` | Real YAML parsing, roadmap structure/reference validation | Run from nested Sourcefold directory; npm package is private dev tooling, not a product service. |
| PowerShell | Windows wrappers and documentation checkpoint integration | Checkpoint apply writes canonical state; do not use it as automatic validation. |
| HTML/JS viewer + js-yaml CDN | Interactive reader of roadmap | Fetches sibling YAML and jsDelivr js-yaml 4.1.0; not a fully offline viewer and not acceptance evidence. |
| Git / long-path support | Snapshot provenance, byte preservation, 299-character destination paths | The import preserved measured source-checkout bytes, not universally identical source Git blob bytes; NRI autocrlf explains some historical line-ending differences. |

Recorded export verification (not rerun by A1): roadmap passed with 6 statuses, 7 lanes, 26 nodes, 25 edges, 254 checkpoints; focused suite 37 passed/1 skipped; full collection 1029, outcome **989 passed, 27 skipped, 13 failed**. Twelve failures are stale evidence-lineage SHA assertions reported reproduced in the NRI source; one requires the historic Tesseract path. Q1/R1 did not claim independent re-execution of the full Python failure reproduction. Exact bytes/tests/evidence were independently compared; runtime failure attribution remains the recorded V1 result.

Do not call this a passing full suite or fresh runtime proof. Do not repair these failures by editing immutable expected hashes, blessing stale predecessors, running OCR with old authorization, or synthesizing outputs to make tests pass. The import may be correctly accepted within scope while implementation/evidence debt remains.

Current local baseline is `7c880d6`. The export's `161aec0` publication/release references are historical exact events, not proof that that SHA is still branch tip. Export context also retains old phrases such as no remote mutation and stale pre-remediation role matrix: completed evidence and exact Git history supersede those snapshots for current-state descriptions.

## 8. Dangerous handoff claims to avoid

- "Documentation-only scaffold": inaccurate given scripts, real probes and evidence. "Completed general-purpose pipeline": unsupported by the current Phase 0 state.
- "No pages/fixtures/Gate accepted": contradicted by exact scoped records. "Gate 1 completed globally": contradicted by active roadmap nodes and the record's narrow boundaries.
- "All 20 pages freshly OCRed": contradicted by mixed bridge/candidate/four-page-fresh first-pass report. "P002 1.0 score proves independent OCR": omits human-backed remediation and separate pass decision.
- "Tests passed": hides 13 inherited failures and skipped coverage. "Import release approves books/source": confuses artifact types and acceptance scope.
- Old role names in roadmap, acceptance vocabulary or historical status are current policy: false; use root governance/current AGENTS and retain historic attribution.
- `Sorceforge` is a product/package/schema rename: false; it is only the remote/directory slug. Keep Sourcefold paths and `@nri/sourcefold-devtools` identity.
- Current `PROJECT_STATUS` Decisions/Next Actions or fixture README's old "not admitted" wording can be used without checking later bounded decisions: false; these append-only historical sections contain superseded recommendations.

## 9. Safest next task and concrete handoff specification

Finish this documentation handoff without execution or evidence remediation. For a receiving model's next implementation decision, recommend a separately scoped **read-only baseline debt/continuation audit**: enumerate the exact 12 failing lineage assertions and one runtime dependency, identify each earliest mismatching predecessor and whether it reflects historical supersession, line-ending identity or actual code defect; read current page/lane successor decisions; propose a bounded fix/runtime-binding specification. Do not launch a new book, repeat OCR or continue the old P013 loop by default.

Acceptance for that proposed audit: every failing assertion has exact test/path/expected/actual/source-of-authority evidence; no historical payload is rewritten; the intended future lane, prerequisites and output root are named; any runtime rebinding has a source/tool identity and authorization plan; remaining skipped coverage is explicit. Main chat selects and authorizes the next implementation scope. This is a recommendation, not authority granted by A1.

Recommended three-document outline:

- `MODEL_HANDOFF_SUMMARY.md`: product/non-goals; what exists versus planned; Phase 0 + scoped Gate acceptance; current standalone baseline; 13-failure/runtime caveat; six-link reading path; safest next task.
- `MODEL_HANDOFF_SPEC.md`: evidence precedence; core/optional DAG; implemented contract map; significant completed lane chronology and current page boundary; repository counts; artifact/authorization/acceptance distinctions; technology purposes; exact recorded verification limitations; safe commands/cwd; forbidden assumptions and remediation criteria.
- `NEW_MODEL_PROMPT.md`: operate in Sorceforge/Sourcefold, read the summary/spec and assigned current plan, retain main-chat ownership/current role policy, state exact revision and requested scope, preserve all source/evidence, do not infer OCR/release authority, return a bounded actionable result with explicit verified/recorded/pending distinctions. The prompt must not fabricate a platform model switch or override canonical ownership merely because the receiving model is named.

Handoff acceptance criteria: all local links resolve; counts name their baseline; current, historical and proposed claims are visibly distinct; `G1WGADR` and P002 exceptions are preserved alongside global gate state; test totals reconcile; no claim of new runtime or user acceptance; independent critic reviews the frozen documents after bounded factual QA.

## Verification, files and blockers

Read root/project AGENTS and current governance; assigned handoff plan/context; current root/project README, SETUP/status; product/module architecture, decision-log excerpts, all five module contracts, artifact manifest schema; roadmap node excerpts; Phase-0 plan/context, acceptance vocabulary/lineage/quality material; representative authorization/lifecycle/route/semantic/OCR code and script/test inventories; exact whole-Gate, first-pass and P002 lane summaries/reports; export context/plan/release and Q1/R1 receipts.

Native Git read-only history and baseline enumeration required an elevated retry after normal access returned permission denied; the retry succeeded and confirmed HEAD/history/counts. No remote request, fetch, commit, push, OCR, render, full test execution, dependency installation or evidence regeneration was performed. Only this receipt was changed; other agents' edits were preserved.

Blockers: none to the handoff. Product-runtime portability, inherited lineage failures and unresolved global acceptance decisions remain explicit future work. A1 is not the final release reviewer. Token use unavailable.
