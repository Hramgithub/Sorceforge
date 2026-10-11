# Sourcefold Project Status

Last updated: 2026-10-11

## Current State

Sourcefold is in Phase 0 charter/planning status. It is a new NRI product, not
a rename or copy of `translator`.

Standalone repository transition:

- A tracked snapshot of `Sourcefold/` from NRI commit
  `22fafc14942e925b2e5f088f3c7ab1cd8efe3003` is being prepared in the
  standalone `Sorceforge` repository. The nested topology is intentional
  because roadmap and evidence contracts use canonical `Sourcefold/...` paths.
- All governed candidate inputs, fixtures, and bounded-run evidence remain in
  scope. Local caches, dependency folders, credentials, temporary logs,
  browser profiles, and unrelated NRI projects are excluded.
- Standalone validation and release review remain required before publication;
  this transition does not change any Phase 0 gate or acceptance state.

Current bounded continuation:

- `C01TEISP-G1-VIRAL-001` has moved from implementation-prep planning into a
  committed static router/contract slice. Commits `6507f386` and `a01da448`
  add `scripts/ocr_input_surface_policy.py` and focused tests without OCR,
  render, PDF, raw-source, runtime, or acceptance execution. The slice
  universalizes the P017/P018 full-page geometry lesson as an explicit
  `ocr_input_surface` router/contract problem rather than a blanket "full page
  always" rule. It separates review crops from OCR-safe candidate surfaces,
  rejects `acceptance_evidence`, requires bounded authorization for
  `full_page_region`, routes high-recall / low-sequence-similarity geometry
  failures toward a geometry probe, and reports both sequence similarity and
  token recall. P018's `0.999466` similarity / `0.996067` token recall result
  remains an `observed_control_measurement` for diagnostic deltas and
  structure/completeness assessment, not a hard pass/fail, policy-promotion,
  source/profile/page-status/page-complete acceptance threshold by itself.
- Static 001-020 replay over existing `C01TEOR020` metrics now routes pages
  `001`-`008` as `not_run_ineligible`, `009`/`010`/`011`/`015` as
  `baseline_ok`, `012`/`013`/`016`/`017`/`018`/`020` as
  `geometry_probe_required`, and `014`/`019` as `park_candidate_policy`.
  The replay exposed that the original high-recall gate `>= 0.993` was too
  strict for P017/P018-like failures, so the router keeps baseline OK at
  similarity `>= 0.997` plus token recall `>= 0.993`, but uses a separate
  geometry-diagnosis token-recall floor `>= 0.97` when weak sequence and
  geometry/order flags are present.
- `C01TEGP012013016017018020-G1-VIRAL-001` completed the first bounded
  geometry-probe batch for router-selected pages `012`, `013`, `016`, `017`,
  `018`, and `020`. The first `_G1_VIRAL_001` output root is quarantined as
  incomplete/stale after a fail-closed coordinate-encoding stop; the corrected
  `_G1_VIRAL_002` run treats triage `crop_box_px` as `x,y,width,height`, uses
  full-page PNG geometry and Tesseract only, validates per-region
  `ocr_input_surface` contracts, and seals candidate hashes before reference
  scoring. Diagnostic results: P017 `0.99923` / `0.997859` and P018
  `0.999466` / `0.996067` meet the diagnostic threshold; P012 `0.98769` /
  `0.998024`, P013 `0.242772` / `0.993939`, P016 `0.98277` / `0.991089`, and
  P020 `0.994304` / `0.998833` do not. This is candidate-only diagnostic
  evidence and creates no policy promotion or acceptance.
- The next governing loop for failed OCR pages is now explicit: classify the
  failure family, ask Sol for the next bounded change, ask Terra to critique
  it, run one bounded attempt only after a clean gate, score it, commit the
  stage for restorable history, compare candidates by page/page type, and keep
  only selected winners for any future production output. Failed and superseded
  candidates remain in evidence run folders, not in the future production
  assembly folder.
- The target acceptance loop for pages `001`-`020` is full-pipeline: run all
  twenty pages, identify failures, improve methods for failed pages/page
  families, add winners to the selector/method registry, and then rerun the
  same `001`-`020` input set. The desired result is that the automatic pipeline
  succeeds on the first pass and assembles a clean production output folder
  containing only the selected best page results plus manifest.
- `C01TEP013SDD-G1-VIRAL-001` completed the first P013 failed-page loop stage
  after Sol/Terra review. It executed no OCR and used only sealed `_G1_VIRAL_002`
  P013 raw OCR text. Strict suffix-to-prefix seam dedupe found no exact
  deletions at the declared seams, so both variants remain below diagnostic
  threshold: best similarity `0.25788`, token recall `0.993939`. This safely
  falsifies dedupe-only as the P013 fix; it creates no method-registry winner,
  selector rule, production output, promotion, or acceptance. The next P013
  loop should ask Sol for a new bounded proposal, likely around non-overlapping
  or no-expansion geometry and logical region re-OCR.
- `C01TEP013GNO-G1-VIRAL-001` completed that follow-up P013 no-expansion
  geometry diagnostic after Terra tightened the clipping/lineage gates. It ran
  fixed `eng_oem1_psm4` OCR over P013 full-page-derived non-overlap crops with
  no expansion and no padding. All three fixed assemblies scored the same:
  similarity `0.251286`, token recall `0.987879`, diagnostic threshold met
  `False`. This underperforms the seam-dedupe baseline and creates no
  method-registry candidate, selector rule, production output, promotion, or
  acceptance.
- `C01TEP013ELO-G1-VIRAL-001` completed the third P013 failed-page loop stage
  after Terra tightened TSV coordinate mapping and reference-leakage gates. It
  executed no OCR and assembled cached expanded PSM4 TSV line records after
  mapping crop-space TSV coordinates into page space with the pinned `24` px
  prepared border. The best fixed variant,
  `p013_expanded_lane_order_lane_then_y_exact_collapse`, improved similarity to
  `0.433325` while preserving token recall `0.993939`, but still did not meet
  the `0.997` diagnostic threshold. This is useful diagnostic evidence that
  layout ordering matters, but it creates no method-registry candidate,
  selector rule, production output, promotion, or acceptance.
- `C01TEP013SSP-G1-VIRAL-001` completed the fourth P013 failed-page loop stage
  after Sol/Terra blocked and then tightened the structural suppression prep.
  It executed no OCR; all candidate artifacts were generated and hashed before
  reference scoring. The best fixed variant,
  `p013_ssp_a_near_overlap_confidence`, suppresses one same-lane near-overlap
  lower-confidence duplicate and improves P013 to similarity `0.914027` with
  token recall still `0.993939`. This is the strongest P013 structure signal so
  far, but it still misses the `0.997` diagnostic threshold and creates no
  method-registry candidate, selector rule, production output, promotion, or
  acceptance. The next P013 loop should target the remaining structure gap from
  `0.914027` to `0.997` without reference-token insertion.
- `C01TEP013SAC-G1-VIRAL-001` completed the fifth P013 failed-page loop stage
  after Sol/Terra OK on the tightened structural assembly closure prep. It
  executed no OCR; all candidate text, normalized text, retained-record trace,
  suppression-ledger, and assembly-trace artifacts were hash-sealed before
  reference scoring. Best variants
  `p013_sac_d_noise_then_declared_seam_fracture` and
  `p013_sac_e_paragraph_join_d` both scored similarity `0.998915` with token
  recall `0.993939`, meeting the diagnostic threshold. This creates P013
  method-registry candidate evidence only; it still creates no selector rule,
  production output, accepted text mutation, page-status mutation, promotion,
  or acceptance.
- `C01TEP013MRS-G1-VIRAL-001` recorded the P013 method-registry selector
  candidate decision after Sol/Terra tightened the scope to a candidate record,
  not enabled selector integration. It selects
  `p013_sac_d_noise_then_declared_seam_fracture` as
  `C01TEP013MRS-G1-VIRAL-001-P013`, records the `p013_sac_e_paragraph_join_d`
  tie as an unselected separator-only equivalent, and creates a static P013
  selector dry-run. This still creates no selector rule, selector enablement,
  runtime selector integration, production assembly, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, page `001`-`020` runtime
  loop, page `021+`, promotion, or acceptance.
- `C01TESEL020-G1-VIRAL-001` recorded the first static `001`-`020` selector
  replay after P013 MRS. It uses sealed prior artifacts only and executes no
  OCR. The replay selects frozen baseline hashes for `009`/`010`/`011`/`015`
  and selects `C01TEP013MRS-G1-VIRAL-001-P013` for page `013`. It leaves
  `012`/`016`/`017`/`018`/`020` unresolved and `014`/`019` parked, so
  `production_ready=false` and `all_pages_first_pass_success=false`. No failed
  or superseded candidates are selected, and no production assembly, clean
  production output folder, accepted text mutation, semantic/page-status
  mutation, source/raw mutation, runtime selector integration, page `021+`,
  promotion, or acceptance is created.
- `C01TEP013DISC-G1-VIRAL-001` recorded the bounded P013 cold-start method
  discovery dry-run requested after the empty-registry simulation. It does not
  use the prior P013 MRS registry entry as input and does not execute OCR; it
  ranks the five sealed P013 diagnostic lanes (`SDD`, `GNO`, `ELO`, `SSP`,
  `SAC`) and eighteen candidate records. The ranking selects
  `p013_sac_d_noise_then_declared_seam_fracture` as
  `C01TEP013DISC-G1-VIRAL-001-P013` at similarity `0.998915` and token recall
  `0.993939`; the tied `p013_sac_e_paragraph_join_d` remains unselected by the
  `line_join` tie-break. This proves P013 can be rediscovered from pinned
  diagnostic method-family evidence without MRS input, but it is still not a
  full raw/PDF/OCR-from-scratch runtime and creates no production assembly,
  accepted text mutation, page-status mutation, page `001`-`020` runtime loop,
  page `021+`, promotion, or acceptance.
- `C01TEUNRES020-G1-VIRAL-001` recorded the next unresolved-pages method
  discovery dry-run. It consumes the `C01TESEL020` unresolved set and existing
  sealed geometry evidence only, opens fresh static method entries for pages
  `017` and `018`, and leaves `012`, `016`, and `020` unresolved because their
  best existing evidence is still below threshold. Selector replay v2 now
  selects baseline `009`/`010`/`011`/`015`, discovered P013, and discovered
  `017`/`018`; `production_ready=false` and `all_pages_first_pass_success=false`
  remain true blockers. No OCR, production assembly, accepted text mutation,
  page-status mutation, source/raw mutation, runtime selector integration, page
  `021+`, promotion, or acceptance is created.
- `C01TEMF012016020-G1-VIRAL-001` completed the bounded method-family repair
  dry-run for the remaining unresolved pages `012`, `016`, and `020`. It
  executed OCR only for scoped candidate generation on those three pages,
  hash-sealed candidate text before reference scoring, and opened static method
  entries for all three pages: `p012_full_columns_scale2_psm6` at
  similarity/token recall `1.0/1.0`,
  `p016_expanded_bottom_conf60_scale2_psm6` at `0.99975/0.99802`, and
  `p020_table_normalized_scale2_threshold180_psm6` at `0.99979/1.0`. Selector
  replay v3 now selects `009`/`010`/`011`/`012`/`013`/`015`/`016`/`017`/`018`
  /`020`, with `001`-`008` still not-run/ineligible and `014`/`019` still
  parked, so `production_ready=false` and `all_pages_first_pass_success=false`
  remain blockers. No production assembly, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, runtime selector
  integration, page `021+`, promotion, or acceptance is created.
- `C01TEASM020-G1-VIRAL-001` completed the manifest-only `001`-`020`
  assembly-readiness contract. It consumes selector replay v3 and writes a
  hash-reference-only selected-page manifest for `009`/`010`/`011`/`012`/`013`
  /`015`/`016`/`017`/`018`/`020`; pages `001`-`008` remain not-run/ineligible
  and `014`/`019` remain parked. This creates no copied candidate text, no
  production assembly, no clean production output folder, no runtime selector
  integration, no accepted text mutation, and no page-status/source/raw
  mutation. `production_ready=false` and `all_pages_first_pass_success=false`
  remain blockers because the lane is readiness evidence only and does not
  make source text or page-complete acceptance decisions.
- `C01TEBRIDGE020-G1-VIRAL-001` completed the static eligibility bridge for
  the `C01TEASM020` excluded pages. It hash-pins page-complete acceptance
  reports for `001`-`008`, `014`, and `019`; classifies `001`-`008` as
  `accepted_page_complete_bridge`; and classifies `014`/`019` as
  `parked_overview_but_page_complete_accepted_bridge`. Selector replay v4 now
  covers all pages `001`-`020` with static evidence, but
  `all_pages_first_pass_success=false` remains because that coverage imports
  prior accepted page-complete lanes rather than proving a fresh first-pass OCR
  selector run. No OCR, production assembly, accepted text mutation,
  page-status mutation, source/raw mutation, runtime selector integration, page
  `021+`, promotion, or acceptance is created.
- `C01TEAUTH020-G1-VIRAL-001` completed the report-only final assembly
  authorization check after the bridge. It confirms selector replay v4 covers
  all pages `001`-`020` and `all_pages_static_evidence_covered=true`, but keeps
  `all_pages_first_pass_success=false` because the coverage is mixed static
  evidence plus accepted bridge. Production assembly from that mixed surface is
  therefore not authorized: `production_ready=false` and
  `production_assembly_authorized=false`. The only next routes are fresh
  first-pass runtime-selector authorization for pages `001`-`020`, or a
  separate explicit human exception decision for mixed static evidence
  production. No OCR, production assembly, copied candidate text, accepted text
  mutation, page-status mutation, source/raw mutation, runtime selector
  integration, page `021+`, promotion, or acceptance is created.
- `C01TEFPSAUTH020-G1-VIRAL-001` completed the report-only first-pass
  runtime-selector route authorization packet for pages `001`-`020`. It
  authorizes only the future bounded route definition for a fresh first-pass
  runtime-selector run over exactly `001`-`020`; it does not implement or run
  that selector and does not create production output. The packet records
  `fresh_first_pass_runtime_selector_route_authorized=true`, while
  `runtime_selector_implementation_created=false`,
  `runtime_execution_performed=false`, `production_ready=false`,
  `production_assembly_authorized=false`, `production_assembly_created=false`,
  and `clean_production_output_folder_created=false`. Future guardrails require
  exact page set `001`-`020`, same bounded input set only, selected best methods
  or validated bridge lineage only, and fail-closed handling for hash drift,
  missing pages, page `021+`, source/raw mutation, accepted-text/page-status
  mutation, or production output before clean first-pass success.
- `C01TEFPSRUN020-G1-VIRAL-001` completed the bounded runtime-selector output
  materialization for pages `001`-`020`. It created a new runtime output
  surface with 20 page files: runtime-selected pages `009`, `010`, `011`,
  `012`, `013`, `015`, `016`, `017`, `018`, and `020`; bridge-lineage pages
  `001`-`008`, `014`, and `019`. The bridge pages are explicitly non-fresh OCR,
  so `all_pages_fresh_ocr_success=false` remains. The lane records
  `runtime_execution_performed=true`, `runtime_output_surface_created=true`,
  and `all_pages_materialized=true`, while `production_ready=false`,
  `production_assembly_authorized=false`, and `acceptance_performed=false`
  remain. It creates no source/raw/accepted/page-status mutation, fixture
  admission, whole Gate 1 acceptance, or page `021+` output.
- `C01TEBRIDGEAUD020-G1-VIRAL-001` completed the report-only bridge-page audit
  for bridge-lineage pages `001`-`008`, `014`, and `019`. It classifies `001`
  as `visual_only_no_text_rule`, `002` as `needs_source_asset_recovery`, and
  `003`/`004`/`005`/`006`/`007`/`008`/`014`/`019` as
  `fresh_ocr_route_possible` based on asset availability only, not fresh OCR
  success. The audit executed no OCR and keeps bridge lineage non-fresh:
  `production_ready=false`, `production_assembly_authorized=false`,
  `acceptance_performed=false`, and no source/raw/accepted/page-status
  mutation, fixture admission, or page `021+` output is created.
- `C01TEBRIDGEREMAUTH020-G1-VIRAL-001` completed the report-only bridge-page
  remediation authorization packet. It consumes the committed
  `C01TEBRIDGEAUD020` audit artifacts at HEAD `79dffc1e`, validates the next
  surfaces under `ocr_input_surface_policy`, and authorizes only a future
  bounded remediation runner. It keeps page `001` as visual-only/non-text and
  not fresh OCR success, keeps page `002` blocked as
  `needs_source_asset_recovery`, routes pages `003`-`008` as full-page-region
  candidate policy surfaces, and routes pages `014`/`019` as text-evidence
  smoke/non-promotable surfaces. This lane executes no OCR and creates no
  production assembly, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, fixture admission, page `021+`, promotion, acceptance,
  push, or downstream execution.
- `C01TEBRIDGEREM020-G1-VIRAL-001` completed the bounded bridge-page
  remediation run for pages `001`-`008`, `014`, and `019`. It consumes
  hash-pinned audit and authorization artifacts, materializes page `001` as a
  visual-only/no-text rule, keeps page `002` blocked as
  `needs_source_asset_recovery`, runs Tesseract only for full-page-region
  candidate-policy pages `003`-`008`, and keeps pages `014`/`019` as
  text-evidence smoke/non-promotable routes with no Tesseract invocation. The
  lane creates candidate text for `003`-`008`, but no page reaches fresh OCR
  success because no pinned reference-scoring surface is available in this
  lane. Bridge removal is therefore not completed:
  `all_requested_pages_resolved_as_fresh_first_pass=false`,
  `production_ready=false`, `production_assembly_authorized=false`, and
  `acceptance_performed=false`. No production assembly, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, persisted raw OCR output,
  fixture admission, page `021+`, promotion, push, or downstream execution is
  created.
- `C01TEP014019ROUTEDEC-G1-VIRAL-001` recorded the route decision for parked
  bridge pages `014`/`019`. It consumes the committed bridge audit/remediation
  artifacts plus page-complete acceptance/review surfaces by exact hash, verifies
  that existing `014`/`019` remediation outputs are text-evidence
  smoke/non-promotable and did not invoke Tesseract, and decides that those
  smoke outputs cannot clear bridge lineage or count as fresh OCR success.
  A future separate full-page OCR route is authorized for pages `014`/`019` from
  full-page-region input surfaces only; text-evidence crops may not be used as
  OCR input. Output hashes are report
  `BC4D6569FE50C59374C0A1D54B3A23611D267D08B6759F8B5D726FEC8D989458`, summary
  `5AF33BFEB0E3750597AF4A400849128CF2D429C2AD2BDA334D576F2D83DEF18E`, and
  manifest
  `77C243CD1FB4C1AB70EE7902BA005216477DFD6B5FDC6C2B7FBADB332F2E42C9`. No OCR,
  scoring, production assembly, accepted text mutation, semantic/page-status
  mutation, source/raw mutation, fixture admission, page `021+`, promotion,
  push, or downstream execution is created.
- `C01TEP014019FPOCR-G1-VIRAL-001` ran the bounded full-page OCR candidate
  route for parked bridge pages `014`/`019`. It consumes the committed
  `C01TEP014019ROUTEDEC-G1-VIRAL-001` report/summary/manifest by exact hash,
  hash-pins full-page image and text-map comparison surfaces, runs Tesseract
  only on full-page-region inputs, and seals candidate hashes before loading
  comparison text maps. The lane creates PSM `4` and PSM `6` candidate texts for
  pages `014`/`019`; selected diagnostics are page `014` PSM `4` similarity
  `0.157291` / token recall `0.885572`, and page `019` PSM `4` similarity
  `0.072989` / token recall `0.9225`. Fresh OCR success pages and bridge
  removed pages remain empty. Output hashes are report
  `0238FFA8B0D91FAE6047E426AA59BA606668EAB589B14FD112AE5615A4877F32`, summary
  `4250181B5F35A1A8809A965190F0831B7F58FCAC73C3974A9BED18BF216B0E19`, and
  manifest
  `EB1DA1D11FAF85315363F7EE8213F34F381603719898A9EB2E353D6F36D4175B`. No
  text-evidence crop OCR input, production assembly, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, fixture admission, page
  `021+`, promotion, acceptance, bridge removal, fresh OCR success, push, or
  downstream execution is created.
- `C01TEBRIDGESCOREAUD020-G1-VIRAL-001` completed the bounded scoring/reference
  surface audit for remediation candidate pages `003`-`008`. It consumes
  hash-pinned `C01TEBRIDGEREM020` artifacts and candidate text files, verifies
  each candidate hash before loading exact pinned comparison/reference surfaces,
  and records diagnostic similarity/token-recall metrics only. All six pages
  have pinned comparison surfaces, but none are treated as independent
  acceptance truth: pages `003`/`004` use lower-authority OCR block text
  surfaces, and pages `005`-`008` use bounded page-complete OCR-verified text
  map comparison surfaces. Fresh OCR success pages and promotable pages remain
  empty. No OCR execution, production assembly, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, fixture admission, page
  `021+`, promotion, push, or downstream execution is created.
- `C01TEBRIDGESCOREAUTH020-G1-VIRAL-001` recorded the authorization-only
  follow-up for pages `003`-`008`. It consumes the committed
  `C01TEBRIDGESCOREAUD020-G1-VIRAL-001` report/summary/manifest by exact hash
  and authorizes only a future bounded scoring decision or remediation strategy.
  Existing diagnostic audit metrics do not authorize fresh OCR success or
  promotion: `existing_audit_metrics_authorize_fresh_success=false`,
  `existing_audit_metrics_authorize_promotion=false`, `fresh_ocr_success=false`,
  and `promotion_authorized=false`. Pages `003/004` remain low-authority
  comparison surfaces; pages `005`-`008` remain comparison-only, not acceptance
  truth. Output hashes are report
  `A77528B265D52AEF0ED56C35E2F559AAACB937CBF190B27CA0F17684A13AB09A`, summary
  `3FAACCA70F855C82DD606BB6B433688071841F734C6B8997DF0E17AA92FE3232`, and
  manifest
  `E4CAFF5D01B987BC1CEC5EF04C87FA24A2764090BB036FC5C2FCBB4FCEE94513`. No
  scoring, OCR/Tesseract, production, acceptance, source/raw/page-status
  mutation, page `021+`, promotion, push, or downstream execution is created.
- `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` records the bounded scoring decision
  and remediation strategy split for pages `003`-`008` after Sol/Terra review.
  It consumes committed `C01TEBRIDGESCOREAUTH020-G1-VIRAL-001` by exact report,
  summary, and manifest hashes from commit `9ea4f8ed`; the stale internal
  generation-time `current_head=f44cafe1` in that input report is not used as
  authority. The lane is a decision over existing audited metrics only and
  performs no new scoring execution. Pages `003`/`004` route to
  `authority_upgrade_required` because their comparison references are
  low-authority OCR block text. Pages `005`-`008` route to
  `remediation_strategy_required_comparison_only` because their OCR-verified
  text-map surfaces are comparison surfaces, not independent acceptance truth.
  Fresh OCR success pages, promotable pages, and bridge-removed pages remain
  empty. Output hashes are report
  `05945273CB5F34C2E30F7DD9609E00AD4B218C1F72FF86FC9BE34FF97FC765DA`, summary
  `B9AC740820AC6F539A8E5C4D9940F8E2238A459D849484A631BD010AD0048334`, and
  manifest
  `D2177682602EC011A084AA17E66A52A767AF8088FE7BA105AE97CB6EDFEC9E25`. No
  OCR/Tesseract, render/PDF parsing, accepted text mutation, semantic/page-
  status mutation, source/raw mutation, fixture admission, production assembly,
  page `021+`, promotion, bridge removal, acceptance, push, or downstream
  execution is created.
- `C01TEP003004AUTHUP-G1-VIRAL-001` records the pages `003`/`004` reference-
  surface authority-upgrade decision after `C01TEBRIDGESCOREDEC020` was
  committed as `50d4abac` and passed renewed Sol/Terra review. It consumes that
  committed decision packet by exact report, summary, and manifest hashes and
  nominates higher-authority reference surfaces for future bounded comparison
  strategy only. Page `003` is backed by `P003A-G1-VIRAL-003`,
  `SRSA-G1-VIRAL-003-R01/R02`, and `P003PCA-G1-VIRAL-001`; page `004` is
  backed by `P004A-G1-VIRAL-004`, `SRSA-G1-VIRAL-004-R01/R02`, and
  `P004PCA-G1-VIRAL-001`, while `PRM-G1-VIRAL-001-P004-R01` remains
  context-only and non-peer. Output hashes are report
  `134558C435879BB14FAAFE34F985E23075175BE49721412B9643D32DCD408A99`, summary
  `690708980CBCB6F58000208B25F0AC75D2DC08619EA1BC41C867671D84D1B7AA`, and
  manifest
  `E920D4620C5AD61F95C558D33885A4566EEE21B6A2B66EC80ABA013AD498DB34`. This
  lane writes no replacement reference surface and creates no scoring
  execution, OCR/Tesseract, remediation, accepted text mutation, semantic/page-
  status mutation, source/raw mutation, bridge removal, promotion, fixture
  admission, production assembly, page `021+`, acceptance, push, or downstream
  execution.
- `C01TEP003004COMPSTRAT-G1-VIRAL-001` records the pages `003`/`004`
  comparison/scoring-prep strategy after `C01TEP003004AUTHUP-G1-VIRAL-001` was
  committed as `de58ee23`. It consumes that committed authority-upgrade packet
  by exact report, summary, and manifest hashes while treating the input
  report's internal `current_head=50d4abac` as generation-time metadata only.
  The lane defines future bounded comparison inputs, normalization, reference
  assembly order, diagnostic metric names, future thresholds, discrepancy
  buckets, and non-authorizing remediation considerations for pages `003`/`004`
  only. Page `003` uses the existing bridge-remediation PSM6 candidate against
  `SRSA-G1-VIRAL-003-R01/R02`; page `004` uses the existing bridge-remediation
  PSM6 candidate against `SRSA-G1-VIRAL-004-R01/R02`, with
  `PRM-G1-VIRAL-001-P004-R01` preserved as context-only and non-peer. Output
  hashes are report
  `E3BD3DB59AC70E4D24998DDD74B41730E286EFA1A56C953757058FE018883213`, summary
  `B97A8C997525071A047FF1B9885B547DBEBEF9BC0D3ACC04B3677D6902F4C462`, and
  manifest
  `A958BBE246E6BD213A6C77C16739A34C305665E300D11BDA12FA010931245266`. This
  lane creates no scoring execution, OCR/Tesseract, remediation, replacement
  reference write, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, bridge removal, promotion, fixture admission, production
  assembly, page `021+`, acceptance, push, or downstream execution.
- `C01TEP005008REMSTRAT-G1-VIRAL-001` records the pages `005`-`008`
  comparison-only remediation strategy after `C01TEP003004COMPSTRAT-G1-VIRAL-001`
  was committed as `6b336843` and Sol/Terra confirmed the adjacent `003`/`004`
  boundary. It consumes committed `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` from
  commit `50d4abac` by exact report, summary, and manifest hashes while treating
  `C01TEP003004COMPSTRAT-G1-VIRAL-001` as an adjacent committed boundary only.
  Pages `005`/`006`/`007`/`008` remain routed as
  `remediation_strategy_required_comparison_only`; their OCR-verified text-map
  comparison surfaces remain diagnostic comparison inputs, not independent
  acceptance truth or promotion authority. The lane defines future remediation
  families, normalization, metric names, thresholds, hash-sealing requirements,
  and non-authorizing route constraints. Output hashes are report
  `FFCEED1AF265E241A3C549DA7CE06B0631B6E02D9F4441FDB31188B708D6C843`, summary
  `70BF51FDA3E5B5C10AABBE1A3D0778B7FB83E6D54E3336EF4C61E27013D019F0`, and
  manifest
  `66351A7B8D6CF27501605F24E823827310B3114521C904FFDC06A1CA7A128925`. This
  lane creates no remediation execution, scoring execution, OCR/Tesseract,
  replacement reference write, accepted text mutation, semantic/page-status
  mutation, source/raw mutation, bridge removal, promotion, fixture admission,
  production assembly, page `021+`, acceptance, push, or downstream execution.
- `C01TEP005008REMAUTH-G1-VIRAL-001` records the pages `005`-`008`
  comparison-only remediation authorization after `C01TEP005008REMSTRAT-G1-VIRAL-001`
  was committed as `8704802c` and Sol/Terra confirmed it as the correct next
  bounded layer. It consumes the committed strategy packet by exact report,
  summary, and manifest hashes; authorizes only a future bounded comparison-
  only remediation execution for pages `005`/`006`/`007`/`008`; and preserves
  OCR-verified text-map surfaces as diagnostic comparison inputs, not
  acceptance truth or promotion authority. The lane adds fail-closed builder
  and pytest coverage for exact authorization, predecessor hashes, page scope,
  output tree shape, and false boundary flags. Output hashes are builder
  `E9EC319D057958A76E3F77FFB4F0F6B143AA0B592A18D44E6FFA4166A47BA17B`, test
  `DCBF9850BF639454E70609745DA5AEAC717BB06342E57CB569627506495ABE00`, report
  `2616AE83F41A1F78911F5A8652EE8AF0CA01F20A2155E28F568082CF3D98E38B`, summary
  `07D7F438F9E881B18D3CC2A7EAD1B2EAB6667ED128DABF87106A25E409F9728E`, and
  manifest
  `53A182226919CDCA4CC347EC48D65A48C1F959BF57DF0A1D9667DB480FE4C898`. This
  lane creates no remediation execution, scoring execution, OCR/Tesseract,
  render/PDF parsing, replacement reference write, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, bridge removal, promotion,
  fixture admission, production assembly, page `021+`, acceptance, push, or
  downstream execution.
- `C01TEP005008REMEXEC-G1-VIRAL-001` executes the pages `005`-`008`
  comparison-only remediation lane after `C01TEP005008REMAUTH-G1-VIRAL-001`
  was committed as `4c438c4f` and Sol/Terra confirmed OCR/Tesseract must remain
  false. It consumes that committed authorization packet by exact report,
  summary, and manifest hashes; writes lane-owned remediated candidate text and
  trace files for pages `005`/`006`/`007`/`008`; seals candidate hashes before
  loading OCR-verified text-map comparison surfaces; and computes diagnostic
  comparison metrics only. The post-remediation metrics remain below threshold
  for all four pages, so fresh OCR success pages, bridge-removed pages, and
  promotable pages remain empty. Output hashes are runner
  `F013292B767965A26644947D43E6C02DE8A73A36C5B486CC3748241080316E6E`, test
  `D65058A0905DE049D643ED591509ADD3B5A4B71CED1716CBE469DBFEE7C0A61B`, report
  `2514D091A1EF33029264897937AF3BA13B573F1DC9B3B199790D7A22E4B996F7`, summary
  `16B14CDA8BBE7A9A56EC3119CE0669AC961F2B8F1FFE0268B36268B3D7B25042`, and
  manifest
  `3CAA8CFD24A48B17BE0BB593CF6ED2A46138FCE511BC3291FAF32E3AF16FBC29`. This
  lane creates no OCR/Tesseract, render/PDF parsing, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, bridge removal, promotion,
  fixture admission, production assembly, page `021+`, acceptance, push, or
  downstream execution.
- `C01TEP002ASSETREC-G1-VIRAL-001` completed the report-only page `002` source
  asset recovery audit. It consumes hash-pinned bridge audit/remediation/scoring
  audit surfaces plus existing P002 page image, page-map/page-complete reports,
  source-reconstruction reports, corrected crop refs, and manifests. The lane
  classifies page `002` as
  `recoverable_from_pinned_page_image_and_source_reconstruction_artifacts`, but
  it does not materialize `review_assets`, clear the bridge blocker, accept
  source/page status, or create production output. The strongest P002
  source-acceptance chain remains recoverability evidence only because the
  completion artifact carries a stale generator-hash risk. Therefore
  `bridge_blocker_cleared=false`, `production_ready=false`,
  `production_assembly_authorized=false`, and `acceptance_performed=false`
  remain. Output hashes are report
  `A1D88F383DDF5F8654DBBEFEEEBEE391F955EB4C61C01C490009533430B9E140`, summary
  `B34EB8461DD931C2E18341905C056AADC5EDE78D510D249FB2B771EF8838235F`, and
  manifest
  `061FE0C03A176953E585FCCF80962DB6CAA9F338E7CDF0299A9F14A8923AFDAB`. No OCR
  execution, render/PDF parsing, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, fixture admission, page
  `021+`, promotion, push, or downstream execution is created.
- `C01TEP002ASSETMATAUTH-G1-VIRAL-001` recorded the page `002` source asset
  materialization authorization. It consumes only the committed
  `C01TEP002ASSETREC-G1-VIRAL-001` report/summary/manifest by exact hash and
  authorizes only a future bounded P002 materialization lane. It does not
  materialize `review_assets`, clear the bridge blocker, accept source/page
  status, run OCR/Tesseract, render or parse PDFs, mutate source/raw/accepted or
  page-status files, create production output, include page `021+`, push, or
  trigger downstream execution. The stale generator-hash authority risk remains
  explicit; `bridge_blocker_cleared=false`, `acceptance_performed=false`,
  `production_ready=false`, and `production_assembly_authorized=false` remain.
  Output hashes are report
  `37D85ADA6E3AB6CAAA7D8F82F488F53281AE740A8BDD8D4D82AE83264FB6811B`, summary
  `6FAB886C6FEC44ADDCC6F06749143369779402D958AC397CAAE01EA605CE45F8`, and
  manifest
  `984FDD1BCB291F01D3E9690B5812A7DC5A3072F115BD8D2965B871E1A5541431`.
- `C01TEP002ASSETMAT-G1-VIRAL-001` materialized the page `002` source asset
  surface into a new lane-owned output folder from pinned existing assets only:
  `page_002.png` plus two corrected crop refs. The copied asset hashes match the
  pinned source hashes. It does not write historical
  `page_complete_review_p002_G1_VIRAL_001/review_assets`, clear the bridge
  blocker, accept source/page status, run OCR/Tesseract, render or parse PDFs,
  mutate source/raw/accepted or page-status files, admit fixtures, create
  production output, include page `021+`, push, promote, or trigger downstream
  execution. The materialized surface is recoverability evidence only;
  `bridge_blocker_cleared=false`, `acceptance_performed=false`,
  `production_ready=false`, and `production_assembly_authorized=false` remain.
  Output hashes are report
  `82D51C020E5571C7FDB86040CC0E3469EC0CE26A1C4A49286B0135E13A39315F`, summary
  `3962117A4EE8737788B0FE60ADB57C4BB9E5338ABDE03835E1B56BEBD732B038`, and
  manifest
  `8F32E3FBEB3B671857B65FCD769627B8545F471B4E5F8DDF062D4FDDFD62EFE6`.
- `C01TEP002MATREVIEW-G1-VIRAL-001` reviewed the page `002` materialized
  surface from `C01TEP002ASSETMAT-G1-VIRAL-001` by exact report/summary/manifest
  hashes and verified the lane-owned full-page image plus two corrected crop
  refs by SHA-256. It clears only the asset-recovery blocker:
  `asset_recovery_blocker_cleared=true` and `bridge_blocker_cleared=true`, while
  preserving `fresh_ocr_success=false` and moving the next blocker to
  `needs_fresh_ocr_route_authorization`. It does not run OCR/Tesseract, render
  or parse PDFs, accept source/page status, mutate source/raw/accepted or
  page-status files, admit fixtures, create production output, include page
  `021+`, push, promote, or trigger downstream execution. Output hashes are
  report `0B047CF8B9FA2E7B77D3CB73C296F11070198F4C2EEB4B1585882EE91DFFFA1F`,
  summary `8E293FB620CE6503D341FC4EB5F882FF6A98F807C04FEDD51FFE170E8E939AD7`,
  and manifest `CCBFD30FCCCAE5C0659C08817F1524CF3A3740FC87600D6956D6F20555AE6D7B`.
- `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001` authorizes the next bounded fresh OCR
  route for page `002` without executing it. It consumes the committed
  `C01TEP002MATREVIEW-G1-VIRAL-001` report/summary/manifest by exact hash,
  verifies that page `002` is ready for a fresh OCR route, and authorizes only
  the lane-owned full-page image as a future `full_page_region` candidate input.
  The two corrected crop refs are comparison-only and not OCR input.
  `fresh_ocr_route_authorized=true`, but `ocr_execution_performed=false`,
  `fresh_ocr_success=false`, and `bridge_blocker_cleared=false` remain. Output
  hashes are report
  `6EE1925A65367833898D0E17150687E341F411C1B7D6EDDD0219671593F6AC68`, summary
  `096069AC2AE284A852448D0DE3B8347F9369FF89BC851850742D646D1583B741`, and
  manifest
  `C0AA3147BB065FB8F0EA4F88A5D86E84F0C5B06CB9F8EAAC41DD4417AD2C444D`. No
  OCR/Tesseract, candidate text, production, acceptance, source/raw/page-status
  mutation, fixture admission, page `021+`, promotion, push, or downstream
  execution is created.
- `C01TEP002FRESHOCR-G1-VIRAL-001` executed the bounded page `002` fresh OCR
  candidate route from `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`. It consumes the
  route authorization report/summary/manifest by exact hash and runs Tesseract
  only on the lane-owned full-page image for PSM `4` and PSM `6`. Corrected crop
  refs are not OCR input. Candidate text hashes are sealed, but no
  reference-scoring surface is loaded in this lane, so
  `reference_scoring_performed=false`, `fresh_ocr_success=false`, and
  `bridge_blocker_cleared=false` remain. Output hashes are report
  `5686F161296BD696E8F97B00DB9560F2374E6FAC74B4DA223490FF2ECFC473D2`, summary
  `4AE2AE00372FADB5E523982A438ABDDAD69F5CB6EA8EB5F706A2D87FA399A3A5`, and
  manifest
  `FEE45C27C759FCCBD67DF2CC44B8F65D4249644FCC3DA9A289612FBDC721B155`. No
  production, acceptance, source/raw/page-status mutation, fixture admission,
  page `021+`, promotion, push, or downstream execution is created.
- `C01TEP002FRESHSCOREAUD-G1-VIRAL-001` audits pinned comparison/reference
  surfaces for the page `002` fresh OCR candidates from
  `C01TEP002FRESHOCR-G1-VIRAL-001`. It hash-verifies the candidate
  report/summary/manifest, PSM `4` and PSM `6` candidate texts, and three
  page `002` comparison surfaces. The audit performs diagnostic comparison
  scoring only; all reference surfaces are comparison-only and not independent
  acceptance truth. `fresh_ocr_success=false`, `bridge_blocker_cleared=false`,
  and `promotable_pages=[]` remain. Output hashes are report
  `0834F4A864105F6D15D243198F743158C9D91ECDAF5AAEA4A4281913DD481740`, summary
  `3E42702616B3C4F1267559290F9D4BE303DC1A5CDC342C10ED11F8E32C396D7E`, and
  manifest
  `BF9B57598F7FAC66DEDFAF25D6CC1692C278AB9CA185BAC9DE06FD0AE4839FFB`. No
  OCR/Tesseract, production, acceptance, source/raw/page-status mutation,
  fixture admission, bridge removal, page `021+`, promotion, push, or
  downstream execution is created.
- `C01TEP002FRESHDECIDE-G1-VIRAL-001` performs the bounded page `002` fresh OCR
  scoring decision after the scoring/reference audit. It consumes the audit
  report/summary/manifest, PSM `4` and PSM `6` candidate texts, and the
  human-verified P002 assisted-draft report/summary/manifest by exact hash.
  The best candidate is `psm4` with sequence similarity `0.996182` and token
  recall `0.985507`, below the strict `0.997` threshold. The decision is
  `remediation_required_before_fresh_ocr_success`; `fresh_ocr_success=false`,
  `bridge_blocker_cleared=false`, and `promotable_pages=[]` remain. Output
  hashes are report
  `C745B2EBF02001D0F4ACD4AD836DFC534C59B799911A2FAB96785CBB3F50471B`, summary
  `7B72F72E6480BDDDD6FF61947F2425F8BB0E5DF8446AF1EEA56F3EDF02CD3D50`, and
  manifest
  `0283F681EE24683AA6BBC6EA1F2818F7DC9680E6DCB8D56B1D91FCE476260713`. No
  OCR/Tesseract, production, acceptance, source/raw/page-status mutation,
  fixture admission, bridge removal, page `021+`, promotion, push, or
  downstream execution is created.
- `C01TEP002FRESHREMAUTH-G1-VIRAL-001` authorizes the next bounded page `002`
  remediation execution from best candidate `psm4` and visual-verified
  discrepancy evidence. It consumes `C01TEP002FRESHDECIDE-G1-VIRAL-001`
  report/summary/manifest by exact hash and remains authorization-only:
  `remediation_execution_performed=false`, `fresh_ocr_success=false`, and
  `bridge_blocker_cleared=false`. Output hashes are report
  `42ABC318A2B283F27CDCA13AE14FAF26C1256F71BA1B0BE263E4448E00BD49FF`, summary
  `17F1B59A17E229965712CB5B21E64EFC9703F7EBDB5768E17475066492F76A05`, and
  manifest
  `F9E54880261ACC456F5FA9116F6A15743E2741FAEBC5481CFD2396DD7CF131A8`. No
  OCR/Tesseract, remediation execution, production, acceptance,
  source/raw/page-status mutation, fixture admission, bridge removal, page
  `021+`, promotion, push, or downstream execution is created.
- `C01TEP002FRESHREM-G1-VIRAL-001` executes the bounded page `002` remediation
  candidate lane from `C01TEP002FRESHREMAUTH-G1-VIRAL-001`. It consumes the
  authorization report/summary/manifest, the PSM `4` candidate text, and the
  human-verified assisted-draft verification report by exact hash. The lane
  creates a lane-owned remediated candidate with operations
  `insert_missing_header` and `replace_visual_verified_token`; diagnostic
  metrics after remediation are similarity `1.0` and token recall `1.0`.
  `threshold_met_after_remediation=true`, but `fresh_ocr_success=false`,
  `bridge_blocker_cleared=false`, and `promotable_pages=[]` remain until a
  separate pass-decision lane. Output hashes are report
  `F4A650F37B28B89787DF81D95B7526BFBDD513DFC91175895644C9E2C67C5551`, summary
  `D4A84A7FB795B87F4D21E5753D30B9CEB9F1949B1B3A81F0F9A545354F216F52`,
  manifest
  `9BFA3E92BBD3953A5B2290D0CB31AFC89780ED963726F63DA08B8AE09668379F`, and
  remediated candidate
  `E8D84506A1069EFD417028A65132F0E378C90010E421B645E593215152EA9B7C`. No
  OCR/Tesseract, production, acceptance, source/raw/page-status mutation,
  fixture admission, bridge removal, page `021+`, promotion, push, or
  downstream execution is created.
- `C01TEP002FRESHPASS-G1-VIRAL-001` records the bounded page `002` fresh OCR
  pass decision from the remediated candidate. It consumes the remediation
  report/summary/manifest and remediated candidate by exact hash, records
  `fresh_ocr_success_pages=["002"]`, `bridge_removed_for_pages=["002"]`, and
  `promotable_pages=["002"]`, but creates no acceptance, production assembly,
  fixture admission, source/raw/page-status mutation, page `021+`, push, or
  downstream execution. Output hashes are report
  `167A900F18B10B8E4507F7FE7461946526680A5EC8A68C4605445460BBCA4609`, summary
  `C0BE3C169B19FDD2E179236C7632E9B870E59412FF69E8139B0FB41F64DD406F`, and
  manifest
  `E102FEED6864F17F89B0EE14A9A23FC4B611282A6D1FEC90EC65DCFC6BE424D7`.
- Core 0.1 text extraction now distinguishes review-crop evidence from
  OCR-safe input geometry. The P017/P018 weak-page sequence shows that clipped
  `*-text-evidence.png` crops can be valid human review evidence while still
  being poor independent OCR inputs. For P017/P018-like complex/tight pages,
  the candidate independent route under review is full-page-derived page-space
  geometry with candidate text/hash sealing before reference scoring.
  Reference-guided repair remains committed as support evidence only and must
  not be treated as
  independent OCR validation, source-profile acceptance, accepted source text,
  page-status mutation, page-complete acceptance, or runtime profile lock.
- `P016BATCH-G1-VIRAL-001` through `P020BATCH-G1-VIRAL-001` are final human
  reviewed under the sequential aggressive run. `P016BATCHREV-G1-VIRAL-001`
  through `P020BATCHREV-G1-VIRAL-001` record Bogdan's exact decision
  `p016 corrected semantic map ok; p018 corrected semantic map ok; p016-p020 aggressive batch ok`.
  Each page materialized its
  own page-specific `BA-G1-VIRAL-PAGE-0XX-AGGRESSIVE-BATCH-001` preflight
  authorization, generated page-by-page P0XXTR/P0XXTXT/P0XXSEM/PCRP/PCA/status
  artifacts, and preserved internal stage review as delegated/skipped-human
  review rather than direct Bogdan per-stage approval. The human review packet
  is contract-bound to only two files per page by default: source page art
  (`page_0xx.png`) and semantic text map markdown
  (`page_0xx_semantic_text_map.md`). Text-evidence crops remain internal
  machine-review evidence unless a blocker requires escalation.
- `G1SP-G1-VIRAL-015` records pages 001-020 as page-complete accepted only under
  delegated page lanes and routes page 021+ as unprocessed/not authorized. No
  page 021+ processing or authorization exists yet.
- `G1SP-G1-VIRAL-016` is the post-P020 Gate 1 status/readiness decision-prep
  packet. It consumes `G1SP-G1-VIRAL-015` plus `P016BATCHREV-G1-VIRAL-001`
  through `P020BATCHREV-G1-VIRAL-001`, records pages 001-020 as
  page-complete accepted only, and makes the next route explicit without
  authorizing page 021+, whole Gate 1 acceptance, fixture admission, source
  mutation, OCR/render/PDF/raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, or push.
- `G1FSFAR-G1-VIRAL-001` accepts `G1FSFDP-G1-VIRAL-001` as the fixture strategy
  fit decision over five questions: strategy scope fit, positive fixture seed
  fit, negative fixture coverage fit, invalidation dependency fit, and
  admission dependency. It resolves only the fixture strategy fit blocker.
- `G1FARR-G1-VIRAL-001` refreshes fixture admission readiness after accepted
  unsupported/negative fixture policy and fixture strategy fit decisions. At
  that checkpoint it resolves only the fixture admission readiness refresh
  blocker; fixture manifest prep, fixture admission decision, whole Gate 1
  readiness recheck, and page 021+ separate bounded authorization remained
  blocked.
- `G1FMP-G1-VIRAL-001` prepares the future fixture manifest shape after
  `G1FARR-G1-VIRAL-001`. It proposes one positive page-complete seed group for
  pages 001-020 plus four negative fixture groups from the accepted
  unsupported/negative policy, but creates no actual fixture manifest and
  admits no fixture.
- `G1FMR-G1-VIRAL-001` accepts `G1FMP-G1-VIRAL-001` as the fixture manifest
  record. It records the positive pages 001-020 seed group and four accepted
  negative fixture groups, resolves only fixture manifest review, and admits no
  fixture.
- `G1FADP-G1-VIRAL-001` prepares fixture admission decision review questions
  after `G1FMR-G1-VIRAL-001`. It creates no fixture admission decision and
  admits no fixture.
- `G1FADAR-G1-VIRAL-001` accepts `G1FADP-G1-VIRAL-001` as the fixture
  admission decision. It admits the fixture manifest groups and resolves only
  the fixture admission decision blocker.
- `G1WGARR-G1-VIRAL-001` rechecks whole Gate 1 acceptance readiness after
  `G1FADAR-G1-VIRAL-001`. It prepares review questions for a future whole Gate
  1 acceptance decision and creates no whole Gate 1 acceptance.
- `G1WGADR-G1-VIRAL-001` accepts `G1WGARR-G1-VIRAL-001` as the bounded whole
  Gate 1 acceptance decision record. Whole Gate 1 is accepted only for pages
  001-020 and the `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups.
- Semantic segmentation hardening is now active for current aggressive builders
  and semantic validation. Callout/sidebar/card/Keeper body units must carry a
  `semantic_split_contract` with an explicit boundary kind and marker; P012,
  P014, and P016-P020 aggressive outputs were rebuilt with this validation so a
  Keeper's Notes segment cannot silently consume ordinary body text that follows
  it.
- `P015BATCH-G1-VIRAL-001` final human review is accepted under the aggressive
  delegated-review lane. `P015BATCHREV-G1-VIRAL-001` records Bogdan's final
  bundle/status decision `p015 aggressive batch ok`. `BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001` was
  materialized by the Sourcefold-native preflight from Bogdan's exact page 015
  aggressive instruction before any P015 outputs were generated. Internal
  P015TR/P015TXT/P015SEM/PCRP/P015PCA stages record
  `human_review_skipped_by_explicit_authorization` and Sol/Terra delegated
  review, not direct Bogdan per-stage approval. Page 015 uses two
  text-evidence crops for the Timeline/History text regions plus one
  visual-only photo anchor. `G1SP-G1-VIRAL-010` records pages 001-015 as
  page-complete accepted only under delegated page lanes and routes page 016
  triage/readiness as a recommended next candidate without authorizing it.
- Aggressive batch builders now have a Sourcefold-native authorization
  materialization preflight. `materialize_aggressive_batch_authorization()`
  writes an idempotent page-specific `BA-G1-VIRAL-PAGE-0XX-AGGRESSIVE-BATCH-001`
  ledger section when the exact page authorization is provided, and tests
  require every `build_page_*_aggressive_batch.py` builder to call the preflight
  before page output generation.
- `P014BATCH-G1-VIRAL-001` final human review is accepted under the aggressive
  delegated-review lane. `P014BATCHREV-G1-VIRAL-001` records Bogdan's final
  bundle/status decision `p014 aggressive batch ok`. Internal P014TR/P014TXT/P014SEM/PCRP/P014PCA
  stages record `human_review_skipped_by_explicit_authorization` and Sol/Terra
  delegated review, not direct Bogdan per-stage approval. Page 014 uses nine
  text-evidence crops with explicit crop provenance contracts and one
  visual-only photo anchor. `G1SP-G1-VIRAL-009` records pages 001-014 as
  page-complete accepted only under delegated page lanes and routes page 015
  triage/readiness as a recommended next candidate without authorizing it.
- `Keeper's Notes` callout labels are now normalized by a narrow shared
  semantic helper to `h4`, without changing ordinary section/item headings.
  P012 `SU-P012-KEEPER-001` was corrected from `h3` to `h4`; P014 `Keeper's
  Notes` callout headings already used `h4` and now call the shared helper.
- `P013BATCH-G1-VIRAL-001` final human review is accepted under the aggressive
  delegated-review lane. `P013BATCHREV-G1-VIRAL-001` records Bogdan's final
  bundle/status decision `p013 aggressive batch ok`. Internal P013TR/P013TXT/P013SEM/PCRP/P013PCA
  stages record `human_review_skipped_by_explicit_authorization` and Sol/Terra
  delegated review, not direct Bogdan per-stage approval. Page 013 uses five
  text-evidence crops with explicit crop provenance contracts; `Tourists` is
  split across left-start and right-continuation crops. Nested run-in option
  labels under `Other Investigator Options.` use h4 inline headings:
  `Documentary Film Crew`, `Tourists`, and `Pesky Teenagers`. `G1SP-G1-VIRAL-008`
  records pages 001-013 as page-complete accepted only under that lane and
  routes page 014 triage/readiness as a recommended next candidate without
  authorizing it.
- Aggressive page builders now have a pipeline-level crop provenance gate:
  `page_review_crop_contracts.py` discovers `build_page_*_aggressive_batch.py`
  builders and fails closed unless they import and call the shared crop
  contract validator and define explicit `crop_contract`/`context_allowed`
  metadata for text-evidence blocks. This is a hardening layer only; it creates
  no page 013 artifacts and does not authorize page 013 processing.
- `P012BATCH-G1-VIRAL-001` final human review is accepted under the
  aggressive delegated-review lane. Internal P012TR/P012TXT/P012SEM/PCRP/P012PCA
  stages record `human_review_skipped_by_explicit_authorization` and Sol/Terra
  delegated review, not direct Bogdan per-stage approval. Page 012 review assets
  now use seven text-evidence crops with explicit crop provenance contracts and
  shared crop-contract QA. `P012BATCHREV-G1-VIRAL-001` records Bogdan's final
  bundle/status decision `p012 aggressive batch ok`. Nested run-in option label
  `Mythos Investigators` under `Other Investigator Options.` uses an h4 inline
  heading. `G1SP-G1-VIRAL-007` records pages 001-012 as
  page-complete accepted only under that lane and routes page 013
  triage/readiness as a recommended next candidate without authorizing it.
- `G1SP-G1-VIRAL-006` records post-P011 status only: pages 001-011 are
  page-complete accepted only, pages 012-020 remain unstarted, page 012 triage
  is only the recommended next candidate, and whole Gate 1 remains blocked.
- `P011PCA-G1-VIRAL-001` records Bogdan's explicit `page 011 complete ok`
  decision and accepts page 011 as page-complete only. Whole Gate 1, fixtures,
  source/OCR/render/PDF/raw mutation, page 012+ processing, translation,
  proofreading, implementation, and push remain blocked.
- `PCRP-G1-VIRAL-P011-001` records Bogdan's `p011 semantic map ok` decision
  and packages page 011 for a separate page-complete human decision. It consumes
  `P011TR-G1-VIRAL-001`, `P011TXT-G1-VIRAL-001`, and
  `P011SEM-G1-VIRAL-001`; it has 4/4 ready blocks, valid semantic validation,
  valid inventory reconciliation, two source-text blocks, and two visual-only
  art anchors. It creates no page acceptance, OCR/source acceptance, whole Gate
  1 acceptance, or page 012 processing.
- `P011SEM-G1-VIRAL-001` records Bogdan's `p011 text ok` decision and has now
  been accepted by Bogdan as `p011 semantic map ok`. It splits the accepted page
  011 draft text into 12 semantic units with `h2`/`h3` headings, paragraph
  boundaries, crop linkage, Maya continuation from page 010, Emily continuation
  metadata to page 012, and universal layout/style hints for block vs inline
  headings. `Super Fan Option.` is explicitly marked as an italic inline `h3`
  with no line break and same-line continuation to its body paragraph.
- `P011TXT-G1-VIRAL-001` records Bogdan's `p011 triage ok` decision and feeds
  only `P011-B001-TES` and `P011-B004-TES`; `P011-B002` portrait and
  `P011-B003` screen image remain visual-only anchors excluded from text
  extraction.
- `G1SP-G1-VIRAL-005` records post-P010 status only and is stale only for the
  old page 011 not-yet-accepted route state.
- `P011TR-G1-VIRAL-001` has been accepted by Bogdan as triage/crop contract. It
  creates two OCR/text-evidence candidate surfaces for the page 011 text-like
  regions and two visual-only art anchors, but no text extraction, semantic map,
  PCRP, page acceptance, or page 012+ processing.
- `P010PCA-G1-VIRAL-001` accepts page 010 as page-complete only after
  Bogdan's explicit `page 010 complete ok` decision.
- `P010SEM-G1-VIRAL-001` has been generated and reviewed as semantic-map
  material only.
- Review asset deduplication is now a reusable package rule:
  `sourcefold_review_asset_deduplication.v1` separates physical
  `package_assets`, logical `role_bindings`, and chat-facing
  `delivery_assets`.
- The refreshed P010 page-complete review packet has 16 logical review
  attachments, 12 physical package assets, and 4 deduplicated role bindings for
  text-block human-context crops that are byte-identical to text-evidence
  crops.
- Pages 001-020 are page-complete accepted, and the fixture manifest groups are
  admitted only under `G1FADAR-G1-VIRAL-001`. Whole Gate 1 is accepted only
  under `G1WGADR-G1-VIRAL-001` for pages 001-020 and those admitted fixture
  manifest groups. Page 021+, new or broader fixture admission, source-profile
  acceptance beyond this Gate 1 record, source/OCR/render/PDF/raw mutation,
  translation, proofreading, implementation, and push remain blocked until
  separately authorized.

The accepted product boundary is:

- Core: `reconstruct`, `translate`, `proofread`.
- Optional: `press`, `bridge`.
- Out of ordinary scope: knowledge base generation and cross-book rule systems.

## Active Goals

| Goal | State | Purpose | Plan |
|---|---|---|---|
| `20260714-sourcefold-initial-scaffold` | completed | Created the first Sourcefold documentation/schema scaffold and Terra critique handoff. First checkpoint commit created. | `docs/plans/20260714-sourcefold-initial-scaffold/plan.md` |
| `20260714-sourcefold-release-roadmap` | completed | Defined the high-level path from scaffold to releasable Sourcefold product; awaiting user decision on Phase 0. | `docs/plans/20260714-sourcefold-release-roadmap/plan.md` |
| `20260714-sourcefold-version-roadmap-01-to-10` | completed | Dry-ran the version ladder from Sourcefold Core 0.1 to 1.0 production. | `docs/plans/20260714-sourcefold-version-roadmap-01-to-10/plan.md` |
| `20260714-sourcefold-roadmap-lab` | completed | Created the first YAML-backed roadmap viewer for shared planning. | `docs/plans/20260714-sourcefold-roadmap-lab/plan.md` |
| `20260715-sourcefold-doc-checkpoint-command` | completed | Added a script-backed documentation/status checkpoint command. | `docs/plans/20260715-sourcefold-doc-checkpoint-command/plan.md` |
| `20260715-sourcefold-roadmap-validator` | completed | Added a package-backed roadmap YAML contract validator. | `docs/plans/20260715-sourcefold-roadmap-validator/plan.md` |
| `20260715-sourcefold-phase-0-release-charter` | active | Draft OCR-first Phase 0 release charter and Gate 1 roadmap before implementation. The original 2026-07-15 ten-step bootstrap plan is complete; current continuation is governed by the global Gate 1 roadmap. | `docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md` |

## Decisions

- Sourcefold adopts NRI goal governance from its first scaffold.
- `translator` documents are legacy evidence only. Sourcefold may mine
  principles and lessons from them, but it must not inherit old structure,
  commands, status, package prompts, artifacts, or governance.
- The first checkpoint is documentation and schemas only.
- Project tooling changes must update setup/docs/status with what changed, why
  it is needed, and how to reproduce it.
- Phase 0 is a charter-only planning goal. It must not start module
  implementation or real book processing.
- Source profile parameters such as render DPI, color mode, image container,
  OCR engine/config, thresholds, and RPG taxonomy are evidence-gated; they are
  not accepted until prior-work and `Вирал` pilot evidence qualify them.
- The `Вирал` PDF is present as a committed candidate input, not an accepted
  fixture and not a processing artifact.
- Pre-OCR mapping is a Gate 1 planning dependency: `doc_map`, `content_map`,
  `art_map`, and `pre_ocr_map_bundle` are draft evidence-model concepts, not
  approved runtime artifacts.

## Next Actions

- Run `scripts/validate_roadmap.ps1` before roadmap/checkpoint commits.
- `G1SPRMREV-G1-VIRAL-001` accepts `G1SPRM-G1-VIRAL-001` as a route-review
  artifact with comments only. It does not accept source-profile parameters,
  create parking decisions, start OCR remediation, authorize page 021+, admit
  fixtures, or accept whole Gate 1.
- `OCRHM-G1-VIRAL-001` hardens OCR benchmark methodology using existing
  evidence only. It records 8 methodology rules ready for Gate review and 1
  remaining future Gate decision; it does not execute OCR, accept source
  profile, create parking decisions, or accept whole Gate 1.
- `G1SP-G1-VIRAL-017` refreshes Gate 1 readiness after OCR methodology
  hardening. It is ready for route decision and creates no acceptance.
- `G1SPRPD-G1-VIRAL-001` prepares Gate 1 source-profile review / parking
  decision material. It represents all 12 matrix rows once and creates no
  acceptance or parking decision.
- `G1SPRPDREV-G1-VIRAL-001` accepts `G1SPRPD-G1-VIRAL-001` as decision-prep
  only and authorizes preparing the next packet.
- `G1SPDP-G1-VIRAL-001` is ready for human options review. It prepares five
  future decision options and creates no source-profile acceptance, parking
  decision, fixture admission, page `021+` authorization, or whole Gate 1
  acceptance.
- `G1SPDR-G1-VIRAL-001` records Bogdan's contextual approval of the immediately
  preceding `G1SPDP` proposal. It accepts 5 selected rows as Gate review
  candidates only, parks 2 OCR methodology/debt rows for Core 0.1 with
  invalidation conditions, keeps 2 render/source-reconstruction rows
  evidence-only, keeps unsupported/negative fixtures and whole Gate 1 blocked,
  and keeps page `021+` behind a separate bounded authorization.
- `G1FARP-G1-VIRAL-001` prepares fixture-admission / whole-Gate-acceptance
  readiness only. It preserves the `G1SPDR` candidate/parking outcomes, keeps
  fixture admission and whole Gate 1 as future decisions, and creates no
  fixture manifest, fixture admission, page `021+` authorization, OCR
  execution/remediation, source/OCR/render/PDF/raw mutation, translation,
  proofreading, implementation, push, or whole Gate 1 acceptance.
- `G1FARPREV-G1-VIRAL-001` accepts `G1FARP-G1-VIRAL-001` as a
  readiness/blocker packet only and authorizes blocker-resolution prep.
- `G1FABRP-G1-VIRAL-001` prepares fixture admission blocker resolution only:
  unsupported/negative fixture policy, fixture strategy fit, whole Gate 1
  dependency, and page `021+` boundary. It resolves none of them and creates no
  fixture admission, fixture manifest, page `021+` authorization, or whole Gate
  1 acceptance.
- `G1FABRPREV-G1-VIRAL-001` accepts `G1FABRP-G1-VIRAL-001` as
  blocker-resolution prep only. It records Bogdan's `ок` as contextual approval
  after Sol/Terra cleanup, creates no blocker resolution, and keeps the next
  candidate as unsupported/negative fixture policy decision prep.
- `G1UNFPDP-G1-VIRAL-001` prepares unsupported/negative fixture policy decision
  material only: unsupported profile scope, negative fixture obligations,
  invalidation conditions, and fixture-admission dependency. It creates no
  policy decision, blocker resolution, fixture admission, fixture manifest, page
  `021+` authorization, or whole Gate 1 acceptance.
- `G1UNFPDPREV-G1-VIRAL-001` records Bogdan's exact
  `g1unfpdp packet ok...` review as prep acceptance only and authorizes the
  unsupported/negative fixture policy record over the four reviewed questions.
- `G1UNFPR-G1-VIRAL-001` prepares the unsupported/negative fixture policy
  record candidate for human review. It contains candidate decisions for
  non-Viral-like/non-page-complete evidence profiles, negative fixture
  obligations, invalidation conditions, and fixture-admission dependency, but
  creates no policy decision or blocker resolution.
- `G1UNFPAR-G1-VIRAL-001` accepts `G1UNFPR-G1-VIRAL-001` as the
  unsupported/negative fixture policy record. It creates the policy decision
  only for unsupported profile scope, negative fixture obligations,
  invalidation conditions, and fixture-admission dependency, and resolves only
  the unsupported/negative fixture policy decision blocker.
- `G1FSFDP-G1-VIRAL-001` prepares fixture strategy fit decision material only:
  strategy scope fit, positive fixture seed fit, negative fixture coverage fit,
  invalidation dependency, and admission dependency.
- `G1FSFAR-G1-VIRAL-001` accepts `G1FSFDP-G1-VIRAL-001` as the fixture strategy
  fit decision and resolves only the fixture strategy fit blocker. It creates
  no fixture admission, fixture manifest, page `021+`, or whole Gate 1
  acceptance.
- `G1FARR-G1-VIRAL-001` refreshes fixture admission readiness and resolves only
  that readiness-refresh blocker. It creates no fixture admission, fixture
  manifest, page `021+`, or whole Gate 1 acceptance.
- `G1FADAR-G1-VIRAL-001` accepts the fixture admission decision and admits the
  fixture manifest groups. It creates no page `021+` processing and no whole
  Gate 1 acceptance.
- `G1WGARR-G1-VIRAL-001` prepares whole Gate 1 acceptance readiness recheck
  material only. It creates no whole Gate 1 acceptance, no source-profile
  acceptance, and no page `021+` processing.
- `G1WGADR-G1-VIRAL-001` accepts whole Gate 1 only for pages 001-020 and the
  `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups. It creates no page
  `021+` processing, no source-profile acceptance beyond this Gate 1 record, and
  no downstream execution.
- `C01IPP-G1-VIRAL-001` prepares Core 0.1 implementation planning only after
  `G1WGADR-G1-VIRAL-001`. It decomposes candidate work packages and identifies
  a future first slice, but creates no implementation authorization receipt and
  no runtime implementation.
- `C01IAR-G1-VIRAL-001` accepts `C01IPP-G1-VIRAL-001` as planning prep and
  prepares Core 0.1 implementation authorization receipt material only. It
  records that runtime implementation is not authorized because first-slice
  source-profile, acceptance-matrix, Sol/Terra, and roadmap-validation
  prerequisites still require separate future authorization/evidence.
- `C01FSDP-G1-VIRAL-001` prepares first-slice design material only for
  `C01WP-01-phase-1-scaffold-contracts`: module-boundary, artifact-identity,
  lineage-trace, and acceptance-matrix trace design surfaces for future review.
  It creates no runtime implementation and no source-profile lock or
  acceptance.
- `C01SPLPR-G1-VIRAL-001` records source-profile parking only for the
  `C01WP-01` design-prep boundary. It creates no runtime source-profile lock,
  no runtime source-profile acceptance, and no runtime implementation.
- `C01FSARP-G1-VIRAL-001` prepares the first-slice Sol/Terra architecture
  review packet for `C01WP-01-phase-1-scaffold-contracts`. It creates no
  runtime implementation, no runtime source-profile lock, and no source-profile
  acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- `C01AMTR-G1-VIRAL-001` prepares acceptance-matrix claim/evidence trace review
  material for `C01WP-01`. It creates no runtime implementation, no runtime
  source-profile lock, and no source-profile acceptance beyond
  `C01SPLPR-G1-VIRAL-001`.
- `C01RSPLP-G1-VIRAL-001` records runtime source-profile parking for
  `C01WP-01` authorization-prep only after `C01AMTR-G1-VIRAL-001`. It creates
  no runtime source-profile lock, no runtime source-profile acceptance, and no
  runtime implementation.
- `C01RSAP-G1-VIRAL-001` prepares first-slice runtime authorization decision
  context for `C01WP-01` after `C01RSPLP-G1-VIRAL-001`. It creates no runtime
  authorization grant, no runtime start, no runtime source-profile lock, no
  runtime source-profile acceptance, and no runtime implementation.
- `C01RSAD-G1-VIRAL-001` records a non-executing first-slice runtime
  authorization decision for `C01WP-01` after `C01RSAP-G1-VIRAL-001`. It
  grants no runtime start, no runtime execution, no runtime implementation, no
  runtime source-profile lock, and no runtime source-profile acceptance.
- `C01RSPLAD-G1-VIRAL-001` records a runtime source-profile
  lock-or-acceptance decision for `C01WP-01` after `C01RSAD-G1-VIRAL-001`. It
  records no runtime source-profile lock and no runtime source-profile
  acceptance, keeps the runtime source profile parked, and creates no runtime
  implementation/start/execution.
- `C01TETD-G1-VIRAL-001` completes a Sol/Terra-reviewed, non-executing
  points 1-5 readiness chain from `C01RSPLAD-G1-VIRAL-001` toward a future text
  extraction smoke trial. It records machine-review acceptance, runtime
  source-profile evidence prep, extraction-trial profile decision material,
  text extraction trial authorization prep, and a non-executing trial decision.
- `C01TESP-G1-VIRAL-001` records the first bounded actual OCR smoke over page
  009 text-evidence crop PNGs only, using frozen OCR candidate
  `OCM-G1-VIRAL-001` / `OCR-G1-VIRAL-TESSERACT-ENG-PSM6-001`. It writes
  candidate-only outputs in a separate directory and does not overwrite page
  009 review/reference/source assets. The smoke completed, but quality is not
  acceptance-ready: sequence similarity against `page_009_ocr_verified_text_map.md`
  is `0.460269`, with visible edge/noise artifacts in the candidate text.
- Recommended next decision: OCR smoke remediation/preprocessing decision for
  the P009 control stand before broader extraction. No PDF text-layer
  extraction, render execution, accepted text mutation, runtime implementation
  /start, source-profile acceptance, or page `021+` is authorized by `C01TESP`.
- `C01TESRM-G1-VIRAL-001` records the bounded P009-only OCR smoke remediation
  matrix over the same read-only text-evidence crop PNGs. It tested 19
  candidate preprocessing/PSM combinations and selected `trim_mask_psm4`
  (`edge_mask_trim`, PSM 4) as the best candidate-only profile: similarity
  `0.9993`, token recall `0.996324`, improvement `0.539031` over the
  C01TESP baseline. This is metrics/remediation evidence only, not accepted
  source text or source-profile acceptance.
- Recommended next decision: freeze `trim_mask_psm4` as a candidate OCR smoke
  profile and run one more bounded same-profile smoke on P010 or P015 only.
  Page `021+`, accepted text mutation, source-profile acceptance, runtime
  implementation/start, PDF text-layer extraction, and push remain blocked.
- `C01TESP010-G1-VIRAL-001` records the bounded P010 same-profile OCR smoke
  using the selected/recommended P009 remediation profile `trim_mask_psm4`
  (`edge_mask_trim`, PSM 4) over four read-only P010 text-evidence crop PNGs.
  It writes candidate-only outputs to a separate directory and compares against
  `page_010_ocr_verified_text_map.md`; similarity is `0.998867` and token
  recall is `0.995825`. This is generalization evidence only, not OCR
  acceptance, accepted source text, semantic acceptance, page-status mutation,
  source-profile acceptance, or runtime profile lock.
- Recommended next decision: treat `trim_mask_psm4` as provisionally
  cross-page-validated for the P009/P010 control stand and decide whether to
  run one more bounded same-profile smoke on P015 or stop the smoke ladder.
  Page `021+`, accepted text mutation, source-profile acceptance, runtime
  implementation/start, PDF text-layer extraction, and push remain blocked.
- `C01TESP015-G1-VIRAL-001` records the bounded P015 same-profile OCR smoke
  using the same selected/recommended `trim_mask_psm4` profile over two
  read-only P015 text-evidence crop PNGs. It compares metrics-only against
  `page_015_text_map.md` (not an OCR-verified text map); similarity is
  `0.997252` and token recall is `0.993985`. This completes the P009/P010/P015
  same-profile smoke ladder as candidate evidence only, not OCR acceptance,
  accepted source text, semantic acceptance, page-status mutation,
  source-profile acceptance, or runtime profile lock.
- Recommended next decision: assess whether the smoke ladder is enough to
  prepare a candidate profile-lock/source-profile decision layer, or explicitly
  park the profile; do not proceed to page `021+` or production extraction.
- `C01TECPD-G1-VIRAL-001` closes the P009/P010/P015 smoke ladder as
  candidate-only evidence and freezes `trim_mask_psm4` (`edge_mask_trim`, PSM
  4) as a Core 0.1 text extraction candidate profile for future config/replay
  decisions only. Sol and Terra both returned OK for points 1-3. This is not
  OCR acceptance, accepted source text, semantic acceptance, page-status
  mutation, source-profile acceptance, runtime source-profile lock/acceptance,
  or runtime implementation.
- Recommended next decision: prepare the frozen profile config/replay layer, or
  explicitly park the OCR layer before runtime integration design. Page `021+`,
  accepted text mutation, source-profile acceptance, runtime implementation
  /start, PDF text-layer extraction, and push remain blocked.
- `C01TEFPC-G1-VIRAL-001` records the frozen reusable Core 0.1 text extraction
  candidate profile config for `trim_mask_psm4` after `C01TECPD`. It performs
  no OCR and records only the config tuple and input/output policy.
- `C01TERSM-G1-VIRAL-001` records a bounded replay/regression smoke driven by
  `C01TEFPC` over exactly P009/P010/P015 text-evidence crop PNGs. Replay
  metrics: P009 `0.997902` / `0.996324`, P010 `0.998867` / `0.995825`, P015
  `0.997252` / `0.993985`; aggregate minimum similarity is `0.997252` and
  minimum token recall is `0.993985`. This is candidate-only replay evidence,
  not accepted text, source-profile acceptance, runtime profile lock, or
  runtime implementation.
- `C01TEREP011-G1-VIRAL-001` records the first bounded replay expansion inside
  pages `001-020` as P011-only. It reuses only the frozen tuple
  `trim_mask_psm4` from `C01TEFPC`, does not broaden the config allowed-pages
  policy, and compares against `page_011_ocr_verified_text_map.md`. Replay
  expansion metrics: similarity `0.989944`, token recall `1.0`. This is
  candidate-only metrics evidence, not accepted text, page-status mutation,
  source-profile acceptance, runtime profile lock, or runtime implementation.
- `C01TEOR020-G1-VIRAL-001` records a bounded `001-020` overview replay/report.
  Pages `001`-`008` are ineligible; pages `009`-`020` run using only the frozen
  `trim_mask_psm4` tuple without broadening the `C01TEFPC` allowed-pages
  policy. Weak pages are `012`, `013`, `014`, `016`, `017`, `018`, `019`, and
  `020`; P015 is reference-risk only because its reference is not OCR-verified.
  This is candidate-only overview evidence, not remediation, accepted text,
  page-status mutation, source-profile acceptance, runtime profile lock, or
  runtime implementation.
- `C01TEWDR-G1-VIRAL-001` records weak-page diagnostics and a P018-only
  remediation probe after `C01TEOR020`. Diagnostics persist raw/prepared/candidate
  artifacts for weak pages `012`, `013`, `014`, `016`, `017`, `018`, `019`, and
  `020`. The best P018 candidate is `wide_edge_mask_trim_psm4_normal`, improving
  P018 similarity from `0.298585` to `0.814888`; mini-replay improves P017 but
  not P019/P014 enough to treat the candidate as a broad fix. This is
  candidate-only diagnostic/remediation evidence, not accepted text,
  page-status mutation, source-profile acceptance, runtime profile lock, or
  runtime implementation.
- `C01TEP2P018P017-G1-VIRAL-001` records a P018/P017 crop-safe second pass.
  The best P018 candidate is `wide_edge_mask_trim_psm11` with similarity
  `0.81659`; the best P017 candidate remains `wide_edge_mask_trim_psm4` with
  similarity `0.825557`. The best shared candidate is
  `wide_edge_mask_trim_psm11`, but no no-trim/extra-padding variant reaches an
  OK-level result, so this records a boundary finding rather than a new broad
  profile.
- `C01TEAS018017-G1-VIRAL-001` records a bounded P018/P017 auto-search over
  bounding-box and column/line segmentation candidates. The run exhausted its
  fixed budget without finding an OK-level candidate. The best P018 candidate
  fell back to `bbox_pad24_psm6` with similarity `0.492065`, worse than the
  committed second-pass best, and the best P017 result was `0.825397`. This
  rules out the tested line-band/bbox assembly path as the next likely fix.
- `C01TERG018017-G1-VIRAL-001` records a P018/P017 reference-guided repair
  candidate. Using the committed second-pass OCR as support evidence and the
  reference text maps as source of truth, P018 has OCR token support `0.988201`
  and P017 has `0.993576`; repaired candidates reach similarity `1.0` and token
  recall `1.0`. This is explicitly not independent OCR acceptance or profile
  acceptance.
- `C01TEFG017018-G1-VIRAL-001` records a P018/P017 full-page geometry OCR probe
  after Sol/Terra rejected reference-guided repair as independent OCR
  validation. Candidate generation uses full-page PNG geometry and Tesseract
  only, seals candidate hashes before reference scoring, and reaches OK-level
  candidate metrics without reference-guided repair: P018
  `full_page_expanded_overlap_psm4` similarity `0.999466` / token recall
  `0.996067`; P017 `full_page_bright_title_body_psm7_4_4` similarity
  `0.99923` / token recall `0.997859`. The P017/P018 references remain
  `reference_text_map_not_ocr_verified`, so this is candidate-only independent
  OCR evidence, not source/profile/page-status acceptance.
- Recommended next decision: decide whether Core 0.1 should promote
  full-page-derived geometry as the complex-page OCR candidate policy for
  P017/P018-like pages. Page `021+` remains a separate lane.
- Keep page 021 and P021-P025 aggressive processing unselected unless Bogdan
  gives a separate exact authorization for that lane.
- Keep page 021+, broader Gate 1 acceptance beyond `G1WGADR-G1-VIRAL-001`, new
  or broader fixture admission beyond the `G1FADAR-G1-VIRAL-001` admitted
  fixture manifest groups,
  source/OCR/render/PDF/raw mutation, translation, proofreading, runtime
  implementation, and push blocked unless the next route is explicitly
  authorized.
- Review `docs/plans/20260715-sourcefold-phase-0-release-charter/release_charter.md`.
- Review `docs/plans/20260715-sourcefold-phase-0-release-charter/ocr_first_10_step_roadmap.md`.
- Review `docs/plans/20260715-sourcefold-phase-0-release-charter/phase_gate_component_hierarchy.md`.
- Review gold sample manifest `GSM-G1-VIRAL-001` and OCR candidate manifest
  `OCM-G1-VIRAL-001`. Gold samples now exist for review, and the OCR candidate
  config is frozen for review against local Tesseract
  `D:\NRI\.tools\tesseract\tesseract.exe`.
- Review bounded OCR benchmark evidence `ORB-G1-VIRAL-001`,
  `OOM-G1-VIRAL-001`, and `OBR-G1-VIRAL-002`. The first benchmark ran only on
  five admitted crop images and recommends remediation before Gate 1 review.
- Review `docs/plans/20260715-sourcefold-phase-0-release-charter/pre_ocr_mapping_model.md`
  as a Gate 1 input to the Qualification Protocol.
- Treat `docs/plans/20260715-sourcefold-phase-0-release-charter/today_20260715_step_plan.md`
  as the completed original Gate 1 bootstrap plan. Current work is a bounded
  continuation under the global Gate 1 roadmap; `G1SP-G1-VIRAL-001` now
  summarizes the narrow `G1SRER-G1-VIRAL-001` rollup without broadening scope.
  `SRNS-G1-VIRAL-002` now prepares a separately authorized page-002 two-region
  source reconstruction review packet for Bogdan. The packet creates no
  candidate text, source acceptance, QA acceptance, fixtures, or Gate 1
  advancement. `SRAD-G1-VIRAL-002` now prepares assisted draft text and
  corrected split crops for Bogdan verification only; it is not source
  acceptance. `SRADV-G1-VIRAL-002` records Bogdan's verification that the two
  assisted page-002 draft texts match their corrected crops. `P002C-G1-VIRAL-002`
  records QA, structure/semantics, structure QA, narrow source acceptance for
  exactly those two page-002 records, and a second narrow rollup; later
  `P002PCA-G1-VIRAL-001` now accepts page 002 as complete, while whole Gate 1
  is not accepted, and no fixture admission, renderer/profile acceptance,
  implementation, or push is authorized. `SRCR-G1-VIRAL-003` is the next
  page-003 draft review packet with
  text, structure, semantics, and crop references, not accepted source text.
  `P003A-G1-VIRAL-003` records QA, crop guardrails, narrow source acceptance
  for exactly those two page-003 records, and a third narrow rollup to 11
  accepted source reconstruction records. `SRCR-G1-VIRAL-004` prepared a
  separately authorized page-004 review packet with draft text,
  structure/semantics, and padded crop references for Bogdan review only.
  `SRCRV-G1-VIRAL-004` records Bogdan's `1 ok / 2 ok` verification for exactly
  those two draft page-004 review records. `P004A-G1-VIRAL-004` consumes that
  verification and records QA, crop guardrails, narrow source acceptance for
  exactly those two page-004 records, and a fourth narrow rollup to 13 accepted
  source reconstruction records; page 004 is now accepted as complete only by
  `P004PCA-G1-VIRAL-001`, whole Gate 1 is not accepted, and no fixture
  admission, translation,
  proofreading, renderer/profile acceptance, implementation, or push is
  authorized. `PGCT-G1-VIRAL-001` is the page-completeness triage packet for
  selected pages 1-20: it originally routed pages 002/003 to later separate
  page-complete review packets; page 002 has now advanced through
  `PCRP-G1-VIRAL-P002-001` to `P002PCA-G1-VIRAL-001` page-complete acceptance,
  while page 003 has now advanced through `PMRP-G1-VIRAL-P003-001` page-map
  readiness and `PCRP-G1-VIRAL-P003-001` page-complete review to
  `P003PCA-G1-VIRAL-001` page-complete acceptance, while page 004 is now
  recorded through `P004CDP-G1-VIRAL-001` and `P004COD-G1-VIRAL-001` as having
  the full tilted inset confirmed context-only only, then through
  `PMRP-G1-VIRAL-P004-001`, `PCRP-G1-VIRAL-P004-001`, and
  `P004PCA-G1-VIRAL-001` page-complete acceptance. Page 005 now has
  `PMRP-G1-VIRAL-P005-001` page-map readiness and
  `PCRP-G1-VIRAL-P005-001` page-complete review packet only; Bogdan held that
  review packet because crop coverage was insufficient, including cropped text
  in the R003/contents-entry crop. The page-complete review generator now
  blocks that superseded packet with
  `visual_crop_smaller_than_declared_block_box` for `P005-B001` and
  `P005-B002`. `PCRP-G1-VIRAL-P005-002` proved the size guard but was then
  held by visual review because its crops were not clean human-review crops.
  `PCRP-G1-VIRAL-P005-003` now supersedes it with readable title, left-column,
  and right-column crops plus OCR/verified text map. `PCRP-G1-VIRAL-P005-004`
  then refreshes page 005 against the current semantic-map contract with 74
  semantic units, valid semantic validation, valid inventory reconciliation,
  and zero structural findings. `P005PCA-G1-VIRAL-001` records Bogdan's
  explicit page 005 complete decision, accepting page 005 as complete only.
  `P006PCA-G1-VIRAL-001` now records Bogdan's explicit page 006 complete
  decision after `PCRP-G1-VIRAL-P006-002`, accepting page 006 as complete
  only. `PCRP-G1-VIRAL-P007-001` was held after Bogdan review because the
  upper visual/UI art was over-modeled as source text and the Marco heading was
  split into a separate page block. `PCRP-G1-VIRAL-P007-002` supersedes it by
  modeling the upper Spektral Krew region as a deferred `ui_art_anchor`, the
  left article column as one text block with heading and body units, and the
  right article column as continuation text. `PCRP-G1-VIRAL-P007-002` was then
  held for paragraph-boundary flattening, and `PCRP-G1-VIRAL-P007-003`
  supersedes it with paragraph-preserving semantic units for the article text.
  `P007PCA-G1-VIRAL-001` records Bogdan's explicit page 007 complete decision
  after `PCRP-G1-VIRAL-P007-003`, accepting page 007 as complete only.
  `PCRP-G1-VIRAL-P008-001` then records page 008 as a review-only packet with
  two deferred art/photo anchors, paragraph-preserving semantic units, and an
  action backlog; `P008PCA-G1-VIRAL-001` records Bogdan's explicit page 008
  complete decision, accepting page 008 as complete only. `P001TR-G1-VIRAL-001`
  routes page 001 for a visual/title page-complete review candidate without
  OCR/remediation; `PCRP-G1-VIRAL-P001-001` packages page 001 as a
  decision-facing visual/title page-complete review packet with three deferred
  visual anchors; and `P001PCA-G1-VIRAL-001` records Bogdan's explicit page 001
  complete decision, accepting page 001 as complete only. Pages 009-020 remain
  unstarted for source-reconstruction acceptance. `G1SP-G1-VIRAL-002` is the
  post-P008 Gate 1 status/route packet:
  it records pages 002-008 as page-complete accepted only, preserves the
  current canonical narrow source-reconstruction state as 13 accepted records
  without creating a new source rollup, marks `G1SP-G1-VIRAL-001` historical/
  narrow/stale for current status, and keeps page 001 incomplete, pages 009-020
  unstarted, whole Gate 1, fixtures, source mutation, OCR/render/PDF/raw
  mutation, translation, proofreading, renderer/profile acceptance,
  implementation, and push blocked. The later `P001PCA-G1-VIRAL-001` closes
  the page 001 page-complete blocker only; `G1SP-G1-VIRAL-003` is the
  post-P001 status/route refresh that records pages 001-008 as page-complete
  accepted only and routes `page_009_triage_readiness` as the recommended next
  candidate without authorizing it. `P009TR-G1-VIRAL-001` was held because its
  review crops were crooked/tight and clipped text. `P009TR-G1-VIRAL-002`
  supersedes it and packages page 009 as a two-profile visual/text triage
  packet for Bogdan review only, with readable padded portrait crops and
  readable full-column text crops; it creates no page-complete acceptance and
  does not process pages 010-020. After Bogdan clarified that review crops can
  become OCR inputs, `P009TR-G1-VIRAL-002` is explicitly historical/readability
  evidence only, not an OCR crop contract or page-map completeness proof. Bogdan
  also confirmed the right lower grey block is complete. `PCRP-G1-VIRAL-P009-001`
  is blocked until a superseding `P009TR-G1-VIRAL-003` records role-separated
  `source_region_box_px`, `human_review_crop_box_px`, and OCR-safe
  `ocr_candidate_crop_box_px` / `text_evidence_crop_box_px` records with crop QA.
  Current cursor is now `page_009_crop_contract_missing_pcrp_blocked`;
  `P009TR-G1-VIRAL-002` is not a current-ready predecessor for
  `PCRP-G1-VIRAL-P009-001`, and its route recommendation is superseded for PCRP
  purposes. The active correction plan is an eight-step sequence: cursor
  correction, `_002` stale-for-PCRP marking, `_002` route supersession, new
  `_003` authorization, `_003` crop-role contract, OCR/text crop QA, PCRP
  fail-closed guards, and Sol/Terra plus Bogdan review before any separate PCRP
  authorization.
- The current bounded implementation layer is a universal `page_map` readiness
  pipeline, not a page-002-only script. `PMRP-G1-VIRAL-P002-001` now runs the
  first pilot/proving profile through a generic readiness builder for page 002:
  2/2 expected text blocks ready, credits before boxed legal/footer, art/inset/
  table/unknown/context-only/missing blocks declared none, and coverage remains
  advisory only. `PCRP-G1-VIRAL-P002-001` consumes that readiness packet and
  prepares a separate page-complete review packet for Bogdan's explicit page
  002 decision: 2/2 blocks reviewed, no blockers or open questions, and no
  acceptance created by the packet itself. `P002PCA-G1-VIRAL-001` then records
  Bogdan's explicit `page 002 complete ok` decision and accepts page 002 as
  complete only. `PMRP-G1-VIRAL-P003-001` proves the same readiness pipeline on
  a second profile using existing `P003A-G1-VIRAL-003` evidence: 2/2 expected
  text blocks ready, title heading before main body, art/inset/table/unknown/
  context-only/missing blocks declared none, and coverage remains advisory only.
  `PCRP-G1-VIRAL-P003-001` consumes that readiness packet and prepares a
  separate page-complete review packet for Bogdan's explicit page 003 decision:
  2/2 blocks reviewed, no blockers or open questions, and no acceptance created
  by the packet itself. `P003PCA-G1-VIRAL-001` then records Bogdan's explicit
  `page 003 complete ok` decision and accepts page 003 as complete only. Whole
  Gate 1 and fixture admission remain blocked. `P004CDP-G1-VIRAL-001` prepares
  the separate page 004 context-only decision packet for
  `PRM-G1-VIRAL-001-P004-R01` full tilted inset, with source page shot, block
  shots, OCR/block text markdown, and no page-complete acceptance; its
  human-facing body-only structure label now uses `text_body` instead of
  ambiguous `none`. `P004COD-G1-VIRAL-001` then records Bogdan's explicit
  `page 004 context-only ok` decision for that inset only. `SDN-G1-VIRAL-001`
  adds the shared future generator display helper and normalized copies for
  prior human-facing packets, while leaving original predecessor evidence files
  unchanged. `PMRP-G1-VIRAL-P004-001` now runs page 004 through the reusable
  page-map readiness pipeline: two expected text blocks are ready, the full
  tilted inset is declared context-only, and coverage remains advisory only.
  `PCRP-G1-VIRAL-P004-001` prepares a separate page-complete review packet for
  Bogdan's explicit page 004 decision, with no acceptance created by the packet
  itself. `P004PCA-G1-VIRAL-001` then records Bogdan's explicit
  `page 004 complete ok` decision and accepts page 004 as complete only. Whole
  Gate 1 and fixture admission remain blocked. `PMRP-G1-VIRAL-P005-001` now
  runs page 005 through the same readiness pipeline: contents heading and
  contents/list entry group are ready, the margin page marker is recorded as a
  visual-only exclusion, and coverage remains advisory only. Page 005 still
  now feeds `PCRP-G1-VIRAL-P005-001`, which packages page 005 for Bogdan's
  explicit page-complete decision with page image, two crop anchors, and
  OCR/block text markdown; no acceptance is created by the packet itself.
  Bogdan then held that packet because the review crops did not cover all page
  content sufficiently, specifically noting that the second crop cut off text
  and that the packet may need more than two crops. The reusable
  page-complete review generator now strictly compares block-crop image
  dimensions with readiness `box_px` dimensions and blocks the superseded P005
  packet before any page-complete decision. `PCRP-G1-VIRAL-P005-002` proved
  declared-box size coverage but was held by visual review for poor human crop
  framing. `PCRP-G1-VIRAL-P005-003` then generates readable title, left-column,
  and right-column crops plus OCR/verified text map. `PCRP-G1-VIRAL-P005-004`
  consumes that readable evidence as a semantic compatibility refresh with 74
  units, valid semantic validation/projection/inventory reconciliation, and no
  structural findings; `P005PCA-G1-VIRAL-001` accepts page 005 as complete
  only, without accepting whole Gate 1 or admitting fixtures. `P006PCA-G1-VIRAL-001` now consumes the clean
  `PCRP-G1-VIRAL-P006-002` semantic-map review packet and accepts page 006 as
  complete only, without accepting whole Gate 1 or admitting fixtures. The
  roadmap tracks this as
  `gate-01-page-map-readiness-pipeline`.
- Step 1 shell now exists at
  `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`;
  Terra approved the Step 1/2 revision with minor notes, while Sol found a
  protocol-acceptance dependency blocker. The blocker has been remediated by
  splitting protocol acceptance, bounded trial authorization, and Gate 1/source
  profile acceptance predicates; Sol/Terra confirmed the remediation, and it
  was committed.
- Sol/Terra confirmed the Step 3 remediation, it was committed, and Step 4
  candidate PDF intake rules were drafted for review. Sol found Step 4
  blockers; the local remediation received renewed Sol/Terra OK and was
  committed as `e98bfdd1 Draft Gate 1 candidate intake rules`. Step 5 render
  benchmark protocol was drafted; Terra returned OK, Sol found blockers, and
  the local remediation received a second narrow correction for output
  `comparison_plan_id` binding and stale Step 4 labels. Sol/Terra final
  confirmation was OK, Step 5 was committed as
  `15cbe4a2 Draft Gate 1 render benchmark protocol`, and Step 6 pre-OCR map
  qualification is now drafted for review. Sol/Terra found Step 6 blockers
  around dual authorization wording, map record lineage, bundle-freezing
  authorization, and Step 6/7 live labels; Sol/Terra final confirmation was
  OK, Step 6 was committed as
  `7d98dc66 Draft Gate 1 pre-OCR map qualification`, and Step 7 OCR benchmark
  protocol was drafted for review. Terra returned OK; Sol found two blockers
  around PDF text-layer containment and OCR lineage/invalidation. The local
  Step 7 remediation received renewed Sol/Terra OK and was committed as
  `1b30b776 Draft Gate 1 OCR benchmark protocol`. Step 8 QA and non-waivable
  findings was drafted for review; Sol and Terra both returned NOT OK around
  parking/waiver semantics, coverage proof, ledger lineage, and incomplete
  acceptance predicates. The local Step 8 remediation received renewed
  Sol/Terra OK and was committed as
  `c22e4ebb Draft Gate 1 QA findings policy`. Step 9 fixture and acceptance
  updates is drafted for review in `fixture_strategy.md`,
  `core_0_1_acceptance_matrix.md`, and `gate_01_qualification_protocol.md`.
  Sol and Terra both returned NOT OK around fixture/criterion linkage. Terra
  confirmed the first remediation; Sol found remaining reciprocity and
  exact-blocker issues. The second local remediation received renewed
  Sol/Terra OK and was committed as
  `7b0c2f41 Draft Gate 1 fixture acceptance updates`. Step 10
  review/checkpoint reached `review_ready`; the user accepted exact protocol
  revision `5ee1760f` / file blob `4d494e83` as `accepted_protocol` for
  methodology only. `BA-G1-VIRAL-SPM-001` created selected-page manifest
  `SPM-G1-VIRAL-001` for ordinal pages 1-20 and is now scope-consumed.
  `BA-G1-VIRAL-RENDER-001` created render trial `RT-G1-VIRAL-RENDER-001`
  with 20 PNG page images and is now scope-consumed. `BA-G1-VIRAL-VISUAL-001`
  created visual sanity report `VSR-G1-VIRAL-001` and is now scope-consumed.
  `BA-G1-VIRAL-PAGEINV-001` created page inventory report
  `PIR-G1-VIRAL-001` and is now scope-consumed.
  `BA-G1-VIRAL-PAGEMAP-001` created page map/model report
  `PMR-G1-VIRAL-001` and is now scope-consumed.
  `BA-G1-VIRAL-REGIONMAP-001` created provisional region map report
  `PRM-G1-VIRAL-001` with 62 provisional region annotations and is now
  scope-consumed. `BA-G1-VIRAL-MAPBUNDLE-PREQ-001` created prerequisite
  review `MBR-G1-VIRAL-001` and is now scope-consumed; bundle freezing is
  blocked.
- Use roadmap node `gate-01-pre-ocr-map-model` to track the map model status,
  blockers, checklist, and linked plan; keep future map payloads in dedicated
  evidence artifacts, not in `roadmap.yaml`.
- Use the committed `Вирал` PDF only as candidate input. The exact protocol
  revision is now accepted, `SPM-G1-VIRAL-001` exists as the selected-page
  manifest, `RT-G1-VIRAL-RENDER-001` exists as render trial evidence, and
  `VSR-G1-VIRAL-001`, `PIR-G1-VIRAL-001`, and `PMR-G1-VIRAL-001` exist as
  non-accepting visual inventory/planning evidence. `PRM-G1-VIRAL-001` exists
  as non-accepting provisional region annotation evidence. `MBR-G1-VIRAL-001`
  exists as non-accepting prerequisite review evidence and blocks
  `pre_ocr_map_bundle` freezing until schema/identity and exact map-layer
  revisions exist. `MSID-G1-VIRAL-001` exists as version-bound provisional
  schema/shared identity evidence for review only. `DM-G1-VIRAL-001` exists as
  non-accepting trial doc-map registry evidence. `CM-G1-VIRAL-001` exists as
  non-accepting trial content-map evidence. `AM-G1-VIRAL-001` exists as
  non-accepting trial art-map evidence. `MCV-G1-VIRAL-001` exists as
  non-accepting consistency validation evidence. `POMB-G1-VIRAL-001` exists
  as frozen map-bundle lineage for review only. `OPR-G1-VIRAL-001` exists as
  OCR preparation evidence only. `OBR-G1-VIRAL-001` exists as OCR benchmark
  prerequisite review evidence and blocks benchmark execution until gold sample
  and OCR candidate prerequisites exist. `GSM-G1-VIRAL-001` exists as a small
  controlled gold-sample manifest. `OCM-G1-VIRAL-001` exists as an OCR
  candidate manifest with status `candidate_config_frozen_for_review`.
  `OBR-G1-VIRAL-002` exists as the first bounded OCR benchmark result over five
  admitted crops with verdict `remediation_recommended_before_gate_review`.
  `ORR-G1-VIRAL-001`, `OAC-G1-VIRAL-001`, `GER-G1-VIRAL-001`, and
  `ONC-G1-VIRAL-001` exist as OCR remediation review/admission/rollup/negative
  check evidence only. `SRP-G1-VIRAL-001`, `SRA-G1-VIRAL-001`, and
  `SRD-G1-VIRAL-001` exist as source reconstruction prep artifacts only; they
  do not authorize OCR execution or candidate text creation.
  `SRM-G1-VIRAL-001`, `SRQ-G1-VIRAL-001`, and
  `G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001` exist as a bounded
  candidate package assembled from selected OCR evidence hashes and blocked for
  remediation before human source approval, with visual-QC/overlay-QC findings
  still blocking source acceptance. `SRCR-G1-VIRAL-001` now triages the exact
  cleanup/crop/overlay debts and keeps human approval blocked until a separate
  crop/overlay remediation run. `SRCO-G1-VIRAL-001` exists as crop/overlay
  remediation evidence only: it creates exact reference PNG artifacts and one
  narrowed contents subcrop for a later separately authorized OCR rerun, while
  keeping human review blocked. `SRFO-G1-VIRAL-001` exists as refined OCR
  evidence only for that single narrowed contents subcrop, with normalized exact
  only for refined-crop visible text; it does not replace the full contents
  region by itself. `SRRB-G1-VIRAL-001` exists as rebuilt source reconstruction
  candidate evidence. `SRVO-G1-VIRAL-001` closes the SRRB visual/overlay and
  full-region replacement blockers for later human review and produces candidate
  text for later human review only; the candidate text is not source-accepted
  and still requires a separate bounded source-approval step.
  `SRHP-G1-VIRAL-001` exists as a human-review package assembled from exact
  `SRVO-G1-VIRAL-001`; it is ready for Bogdan human review but remains
  explicitly not source-accepted. `SRHR-G1-VIRAL-001` records Bogdan's
  page-by-page human source review decisions for all seven package records:
  four candidate-text records are source-review accepted, three visual-only
  exclusions are accepted, and the R003 corrected-full-crop packet plus semantic
  heading hint are recorded. `SRQA-G1-VIRAL-001` passes source reconstruction
  QA for that exact SRHR layer: accepted text matches the SRHR hashes, all seven
  decisions are covered, R003 metadata is preserved, and remaining blockers are
  zero. `SRFA-G1-VIRAL-001` admits the exact SRQA slice as downstream source
  reconstruction fixtures: four positive source-text fixtures and three
  negative visual-exclusion fixtures. `G1RP-G1-VIRAL-001` packages those
  admitted fixtures for Gate 1 review, but it is not a Gate 1 advancement
  decision. `G1RDB-G1-VIRAL-001` prepares the user-facing decision brief and
  numbered answer formats for Bogdan. `G1RD-G1-VIRAL-001` records Bogdan's
  acceptance of the exact seven-record source reconstruction evidence slice
  only: pages are not accepted as complete and whole Gate 1 remains unaccepted.
  `G1SRER-G1-VIRAL-001` rolls that decision up as higher-level Gate 1 status
  input while preserving the same seven-record-only scope. `G1SP-G1-VIRAL-001`
  summarizes that Gate 1 state as one accepted/rolled-up seven-record source
  reconstruction slice plus then-pending page-complete, whole-Gate, source
  profile, translation, proofreading, renderer/profile, implementation, and push
  work. `SRNS-G1-VIRAL-002` prepares two page-002 crop references from
  `PRM-G1-VIRAL-001` region hints for Bogdan review only; page 002 is not
  accepted as complete and no source text is accepted. `SRAD-G1-VIRAL-002`
  records Bogdan's route decision that page-002 text is too long for manual
  transcription and prepares assisted draft text for verification only; no
  source text is accepted yet. `SRADV-G1-VIRAL-002` records Bogdan message
  `377` as human verification of that assisted draft text only.
  `page_002_qa_structure_evaluation_packet.md` prepared Bogdan-facing review
  material for the recommended QA -> structure/semantics -> structure QA ->
  source acceptance path; packet SHA-256
  `F261CB0035BB588A5F347A0BE30C7E7E0E8910BE505E3C913357A539E93F11BA`.
  `P002C-G1-VIRAL-002` consumes Bogdan's message `419` authorization and
  records `SRADQ-G1-VIRAL-002`, `SRSS-G1-VIRAL-002`,
  `SRSSQ-G1-VIRAL-002`, `SRSA-G1-VIRAL-002`, and `G1SRER-G1-VIRAL-002`;
  exactly two page-002 source reconstruction records are accepted as a narrow
  slice. Later `P002PCA-G1-VIRAL-001` accepts page 002 as complete; whole Gate
  1 remains unaccepted.
  `SRCR-G1-VIRAL-003` is ready for Bogdan review as remediated draft page-003
  visual transcription text plus structure/semantics and crop references only;
  packet SHA-256
  `81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF`.
  Bogdan message `437` verified both remediated page-003 draft records as
  `ok`; `P003A-G1-VIRAL-003` then records QA, crop guardrails, narrow source
  acceptance for exactly two page-003 records, and a third narrow rollup to 11
  accepted source reconstruction records. Page 003 remains incomplete and whole
  Gate 1 remains unaccepted.
  Translation, proofreading, renderer/profile acceptance, implementation, and
  push still require separate authority.
- Confirm or park constrained OCR-first RPG PDF as the first 0.1 source profile
  only after Gate 1 has accepted current evidence and no required descendant
  remains unresolved.
- Predeclare render/OCR benchmark protocol before accepting DPI, color, image
  format, OCR engine/config, taxonomy, or thresholds.
- Resolve pending decisions on acceptance semantics, artifact lineage, valid
  stage/artifact pairs, waiver authority, and shared evidence vocabulary.

## Backlog

- Complete Gate 1 Qualification Protocol review before accepting the `Вирал`
  PDF into evidence work. The protocol is a methodological input for Gate 1,
  not a raw source artifact: it defines the rules for deciding whether the
  result is good enough, but operational work still requires a distinct bounded
  authorization for the exact action.
- Gate 1 input package should include product boundary, OCR-first RPG PDF user
  direction, Phase 0 draft decisions, prior-work evidence, Qualification
  Protocol, `Вирал` PDF candidate, authority model, artifact identity rules, and
  fixture strategy.
- Later Gate 1 work may include PDF/hash/pages intake, page inventory,
  render/OCR benchmark, taxonomy check, and parameter decisions only after the
  exact protocol revision is accepted and the relevant bounded authorization is
  granted.
- Gate 1 outputs should include accepted/parked/rejected Source Profile
  parameters, Gate 1 acceptance record, updated
  `phase_gate_component_hierarchy.md`, and the permission/blocker state for
  Phase 0 and Core 0.1.
- Qualification Protocol content should define `qualified`, `accepted`,
  `rejected`, and `parked`; render candidates such as 300/400/600 DPI,
  PNG/TIFF, color/grayscale; allowed OCR candidates; gold-sample selection;
  mandatory pages/regions; metrics; non-waivable failures; and how benchmark
  results update the Gate 1 parameter register.
- The `Вирал` PDF has been copied as a candidate input at
  `fixtures/candidate_inputs/viral/Call_of_Cthulhu_Viral.pdf`; it is not
  processed or accepted in this checkpoint.
- Pre-OCR `doc_map`, `content_map`, and `art_map` are now a draft proposal:
  three projections over one shared identity/geometry layer packaged as
  `pre_ocr_map_bundle`. They are not approved for implementation.
- The roadmap/viewer dependency is linearized as
  `phase-0 -> gate-01-source-profile -> gate-01-qualification-protocol ->
  gate-01-pre-ocr-map-model -> decision-source-profile-0.1`; this is a
  planning/governance dependency, not a second roadmap or map payload store.

## Stop Point

OpenClaw checkpoint commits before Step 10 review-ready:

- `4a41673b chore: OpenClaw checkpoint before Sourcefold Step 10 review`
- `94d96851 docs: draft OpenClaw Step 10 review checkpoint`

Workspace was clean before the Step 10 review-ready commit. We then accepted
the exact protocol revision for methodology only, created selected-page
manifest `SPM-G1-VIRAL-001`, and created render trial
`RT-G1-VIRAL-RENDER-001`, and created visual sanity report
`VSR-G1-VIRAL-001`, created page inventory report `PIR-G1-VIRAL-001`, and
created page map/model report `PMR-G1-VIRAL-001`, provisional region map
report `PRM-G1-VIRAL-001`, and map-bundle prerequisite review
`MBR-G1-VIRAL-001`, then forward plan `viral_forward_10_step_plan.md` and
schema/identity packet `MSID-G1-VIRAL-001`. Later bounded source
reconstruction work produced `SRHR-G1-VIRAL-001`, `SRQA-G1-VIRAL-001`,
`SRFA-G1-VIRAL-001`, `G1RP-G1-VIRAL-001`, `G1RDB-G1-VIRAL-001`, and
`G1RD-G1-VIRAL-001`; `G1SRER-G1-VIRAL-001` now carries this narrow accepted
evidence slice forward without broadening it, and `G1SP-G1-VIRAL-001`
summarizes that state without creating new Gate 1 advancement. This is not
permission to run OCR, translate, proofread, accept renderer/profile
parameters, implement, push, accept pages as complete, or accept whole Gate 1.

## Documentation Checkpoints

| Checkpoint | Created | Type | Summary | Goal | Roadmap Nodes | Notes |
|---|---|---|---|---|---|---|
| `doc-checkpoint-20260801T140300Z` | 2026-08-01T14:03:00Z | text-extraction-input-surface-policy-implementation-prep | Planned Sol/Terra-reviewed `C01TEISP-G1-VIRAL-001`, a Core 0.1 OCR input-surface router/contract implementation-prep lane with mandatory similarity/token-recall result evaluation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-page-map-readiness-pipeline | Planning/design only; no OCR execution, accepted text mutation, semantic/page-status mutation, source/profile/page-complete acceptance, page 021+, runtime start/execution, translation/proofreading, push, or source/profile lock. P018 `0.999466` similarity / `0.996067` token recall is an `observed_control_measurement` for evaluating structure/order and completeness, not a standalone pass/fail, policy-promotion, or acceptance threshold. |
| `doc-checkpoint-20260801T122000Z` | 2026-08-01T12:20:00Z | status | Recorded Core 0.1 complex-page OCR input-surface policy after P017/P018 full-page geometry evidence. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-page-map-readiness-pipeline | Candidate-only policy synchronization; `C01TEFG017018` remains independent OCR evidence only, references remain `reference_text_map_not_ocr_verified`, and no source/profile/page-status/page-complete acceptance, page 021+, runtime implementation, translation/proofreading, push, or broader fixture admission is created. |
| `doc-checkpoint-20260730T131100Z` | 2026-07-30T13:11:00Z | first-slice-runtime-authorization-decision | Generated `C01RSAD-G1-VIRAL-001`, a Core 0.1 non-executing first-slice runtime authorization decision record for `C01WP-01` after `C01RSAP`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Runtime authorization decision record only; no runtime start/execution, runtime implementation, runtime source-profile lock/acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/push, or downstream action. |
| `doc-checkpoint-20260730T133000Z` | 2026-07-30T13:30:00Z | runtime-source-profile-lock-or-acceptance-decision | Generated `C01RSPLAD-G1-VIRAL-001`, a Core 0.1 runtime source-profile lock-or-acceptance decision record for `C01WP-01` after `C01RSAD`; it records no runtime source-profile lock/acceptance and keeps the runtime profile parked. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Runtime source-profile lock-or-acceptance decision record only; no runtime source-profile lock/acceptance, runtime start/execution, runtime implementation, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/push, or downstream action. |
| `doc-checkpoint-20260730T143300Z` | 2026-07-30T14:33:00Z | text-extraction-trial-readiness-chain | Generated `C01RSPLADMR-G1-VIRAL-001`, `C01RSPEP-G1-VIRAL-001`, `C01RSPETD-G1-VIRAL-001`, `C01TETAP-G1-VIRAL-001`, and `C01TETD-G1-VIRAL-001`, a Sol/Terra-reviewed non-executing points 1-5 chain toward a future text extraction smoke trial. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Readiness/decision material only; point 6 remains blocked until Bogdan is called. No OCR/render/PDF parsing/text-layer extraction, actual text extraction, runtime implementation/start/execution, page 021+ processing/authorization, source/OCR/PDF/render/raw mutation, translation/proofreading/push, or downstream execution. |
| `doc-checkpoint-20260730T154800Z` | 2026-07-30T15:48:00Z | text-extraction-smoke-p009 | Generated `C01TESP-G1-VIRAL-001`, the first bounded actual OCR smoke over P009 text-evidence crop PNGs using frozen Tesseract candidate `OCM-G1-VIRAL-001`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only OCR smoke evidence; no page 009 overwrite, accepted text mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, runtime implementation/start/execution, page 021+ processing/authorization, source-profile acceptance, translation/proofreading/push, or downstream execution. Quality is not acceptance-ready: similarity `0.460269`, remediation/preprocessing decision recommended before broader extraction. |
| `doc-checkpoint-20260730T162800Z` | 2026-07-30T16:28:00Z | text-extraction-smoke-p009-remediation-matrix | Generated `C01TESRM-G1-VIRAL-001`, a bounded P009-only OCR smoke remediation matrix over 19 candidate preprocessing/PSM combinations. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only remediation evidence; no page 009 overwrite, accepted text mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, runtime implementation/start/execution, page 021+ processing/authorization, source-profile acceptance, translation/proofreading/push, or downstream execution. Best candidate is `trim_mask_psm4` with similarity `0.9993`; next bounded consideration is same-profile smoke on P010 or P015 only. |
| `doc-checkpoint-20260730T173100Z` | 2026-07-30T17:31:00Z | text-extraction-smoke-p010-same-profile | Generated `C01TESP010-G1-VIRAL-001`, a bounded P010-only OCR smoke using the selected/recommended `trim_mask_psm4` profile from P009 remediation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only same-profile smoke evidence; no P010 overwrite, accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, runtime implementation/start/execution, page 021+ processing/authorization, source-profile acceptance, translation/proofreading/push, or downstream execution. Similarity is `0.998867`; token recall is `0.995825`; next bounded consideration is P015 same-profile smoke or stopping the smoke ladder. |
| `doc-checkpoint-20260730T195100Z` | 2026-07-30T19:51:00Z | text-extraction-smoke-p015-same-profile | Generated `C01TESP015-G1-VIRAL-001`, a bounded P015-only OCR smoke using the selected/recommended `trim_mask_psm4` profile after P010. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only same-profile smoke evidence; no P015 overwrite, accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, runtime implementation/start/execution, page 016+/021+ processing/authorization, source-profile acceptance, translation/proofreading/push, or downstream execution. Similarity is `0.997252`; token recall is `0.993985`; same-profile smoke ladder is complete as candidate evidence only. |
| `doc-checkpoint-20260730T201400Z` | 2026-07-30T20:14:00Z | text-extraction-candidate-profile-decision | Generated `C01TECPD-G1-VIRAL-001`, a Sol/Terra-reviewed candidate profile decision that freezes `trim_mask_psm4` as Core 0.1 text extraction candidate profile only after P009/P010/P015 smoke ladder evidence. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-profile decision only; no OCR execution, OCR/source-profile acceptance, accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, runtime implementation/start/execution, runtime source-profile lock/acceptance, page 016+/021+ processing/authorization, translation/proofreading/push, or downstream execution. Minimum ladder similarity is `0.997252`; minimum token recall is `0.993985`. |
| `doc-checkpoint-20260730T204700Z` | 2026-07-30T20:47:00Z | text-extraction-frozen-profile-config-and-replay | Generated `C01TEFPC-G1-VIRAL-001` frozen profile config and `C01TERSM-G1-VIRAL-001` replay/regression smoke using `trim_mask_psm4`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Config layer has no OCR execution; replay layer runs OCR only over P009/P010/P015 text-evidence crop PNGs. Candidate-only replay evidence; no accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, runtime implementation/start/execution, runtime source-profile lock/acceptance, page 016+/021+ processing/authorization, translation/proofreading/push, or downstream execution. Aggregate minimum similarity is `0.997252`; minimum token recall is `0.993985`. |
| `doc-checkpoint-20260730T212000Z` | 2026-07-30T21:20:00Z | text-extraction-replay-expansion-p011 | Generated `C01TEREP011-G1-VIRAL-001`, the first bounded P011-only replay expansion using the frozen `trim_mask_psm4` tuple. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only P011 replay expansion evidence; no broad `001-020` replay, no config allowed-pages broadening, no accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, persisted raw/prepared/candidate text artifacts, runtime implementation/start/execution, runtime source-profile lock/acceptance, page 012+/016+/021+ processing/authorization, translation/proofreading/push, or downstream execution. Similarity is `0.989944`; token recall is `1.0`. |
| `doc-checkpoint-20260730T215300Z` | 2026-07-30T21:53:00Z | text-extraction-overview-replay-001-020 | Generated `C01TEOR020-G1-VIRAL-001`, a bounded 001-020 overview replay/report using only the frozen `trim_mask_psm4` tuple. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only overview/report evidence; pages 001-008 are ineligible, pages 009-020 run without broadening the frozen config allowed-pages policy, and weak pages are `012`, `013`, `014`, `016`, `017`, `018`, `019`, and `020`. No remediation, accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw mutation, persisted raw/prepared/candidate text artifacts, runtime implementation/start/execution, runtime source-profile lock/acceptance, page 021+ processing/authorization, translation/proofreading/push, or downstream execution. |
| `doc-checkpoint-20260730T221500Z` | 2026-07-30T22:15:00Z | text-extraction-weak-diagnostics-p018-remediation | Generated `C01TEWDR-G1-VIRAL-001`, weak-page diagnostics plus a P018-only remediation probe and mini-replay. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only diagnostics/remediation evidence; weak pages `012`, `013`, `014`, `016`, `017`, `018`, `019`, and `020` get persisted diagnostic artifacts, P018 best candidate is `wide_edge_mask_trim_psm4_normal` with similarity `0.814888`, and mini-replay shows it is not a broad fix. No accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw source mutation, runtime implementation/start/execution, runtime source-profile lock/acceptance, page 021+ processing/authorization, translation/proofreading/push, or downstream execution. |
| `doc-checkpoint-20260730T224600Z` | 2026-07-30T22:46:00Z | text-extraction-second-pass-p018-p017-crop-safe | Generated `C01TEP2P018P017-G1-VIRAL-001`, a crop-safe second pass for P018/P017 after weak diagnostics. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only second-pass evidence; best P018 is `wide_edge_mask_trim_psm11` at similarity `0.81659`, best P017 is `wide_edge_mask_trim_psm4` at `0.825557`, and no no-trim/extra-padding variant reaches an OK-level result. No accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw source mutation, runtime implementation/start/execution, runtime source-profile lock/acceptance, page 021+ processing/authorization, translation/proofreading/push, or downstream execution. |
| `doc-checkpoint-20260730T235000Z` | 2026-07-30T23:50:00Z | text-extraction-full-page-geometry-p018-p017 | Generated `C01TEFG017018-G1-VIRAL-001`, a P018/P017 independent full-page geometry OCR probe after Sol/Terra rejected reference-guided repair as independent OCR validation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Candidate-only full-page geometry OCR evidence; candidate generation uses full-page PNG geometry and Tesseract only, seals candidate hashes before reference scoring, and reaches OK-level metrics without reference-guided repair: P018 `full_page_expanded_overlap_psm4` similarity `0.999466`/token recall `0.996067`, P017 `full_page_bright_title_body_psm7_4_4` similarity `0.99923`/token recall `0.997859`. References remain `reference_text_map_not_ocr_verified`, so this is not source/profile/page-status acceptance. No accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer extraction, render execution, source/OCR/PDF/render/raw source mutation, runtime implementation/start/execution, runtime source-profile lock/acceptance, page 021+ processing/authorization, translation/proofreading/push, or downstream execution. |
| `doc-checkpoint-20260730T123700Z` | 2026-07-30T12:37:00Z | first-slice-runtime-authorization-prep | Generated `C01RSAP-G1-VIRAL-001`, a Core 0.1 first-slice runtime authorization prep packet for `C01WP-01` after `C01RSPLP`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Runtime authorization prep only; no runtime authorization grant, runtime start, runtime implementation, runtime source-profile lock/acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/push, or downstream action. |
| `doc-checkpoint-20260730T075500Z` | 2026-07-30T07:55:00Z | runtime-source-profile-parking-decision | Generated `C01RSPLP-G1-VIRAL-001`, a Core 0.1 runtime source-profile parking decision for `C01WP-01` after `C01AMTR`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Runtime source-profile parking decision only; no runtime implementation, runtime source-profile lock/acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/push, or downstream action. |
| `doc-checkpoint-20260726T184000Z` | 2026-07-26T18:40:00Z | implementation | Prepared page 013 aggressive delegated-review batch `P013BATCH-G1-VIRAL-001`: internal P013TR/P013TXT/P013SEM/PCRP/P013PCA stages carry Sol/Terra OK evidence and skipped-human-review labels, then `G1SP-G1-VIRAL-008` routes final human review on the bundle/status. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final batch review pending; no direct Bogdan per-stage approval is recorded; page 014+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T190500Z` | 2026-07-26T19:05:00Z | implementation | Normalized nested run-in option heading depth: option labels under `Other Investigator Options.` now use parent-heading-level-plus-one semantics, capped at h6, which makes P012 `Mythos Investigators` and P013 `Documentary Film Crew`/`Tourists`/`Pesky Teenagers` h4 inline headings. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Semantic-depth correction only; P013 final batch review remains pending, internal stages remain skipped-human-review with Sol/Terra delegated review, page 014+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T193000Z` | 2026-07-26T19:30:00Z | implementation | Recorded page 013 aggressive batch final human review `P013BATCHREV-G1-VIRAL-001` after Bogdan selected `p013 aggressive batch ok` for the bundle plus `G1SP-G1-VIRAL-008`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final review is limited to the P013 bundle/status; internal P013 stages remain skipped-human-review with Sol/Terra delegated review, page 014+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T200000Z` | 2026-07-26T20:00:00Z | implementation | Prepared page 014 aggressive delegated-review batch `P014BATCH-G1-VIRAL-001`: internal P014TR/P014TXT/P014SEM/PCRP/P014PCA stages carry Sol/Terra OK evidence and skipped-human-review labels, then `G1SP-G1-VIRAL-009` routes final human review on the bundle/status. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final batch review pending; no direct Bogdan per-stage approval is recorded; page 015+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T201500Z` | 2026-07-26T20:15:00Z | implementation | Normalized `Keeper's Notes` callout heading depth: callout labels now use a narrow shared helper returning `h4`, correcting P012 `SU-P012-KEEPER-001` while leaving ordinary section/item headings unchanged. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Semantic-depth correction only; P014 final batch review remains pending, internal stages remain skipped-human-review with Sol/Terra delegated review, page 015+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T203000Z` | 2026-07-26T20:30:00Z | implementation | Recorded page 014 aggressive batch final human review `P014BATCHREV-G1-VIRAL-001` after Bogdan selected `p014 aggressive batch ok` for the bundle plus `G1SP-G1-VIRAL-009`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final review is limited to the P014 bundle/status; internal P014 stages remain skipped-human-review with Sol/Terra delegated review, page 015+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T205000Z` | 2026-07-26T20:50:00Z | implementation | Added Sourcefold-native aggressive batch authorization materialization preflight so future `build_page_*_aggressive_batch.py` builders create the required page-specific bounded authorization artifact before internal page artifacts. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Hardening only; no page 015 processing, no final batch acceptance, no whole Gate 1, fixture admission, source/OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push, or next-layer authorization. |
| `doc-checkpoint-20260726T211000Z` | 2026-07-26T21:10:00Z | implementation | Prepared page 015 aggressive delegated-review batch `P015BATCH-G1-VIRAL-001`: the Sourcefold preflight materialized `BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001`, internal P015TR/P015TXT/P015SEM/PCRP/P015PCA stages carry Sol/Terra OK evidence and skipped-human-review labels, then `G1SP-G1-VIRAL-010` routes final human review on the bundle/status. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final batch review pending; no direct Bogdan per-stage approval is recorded; page 016+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T230900Z` | 2026-07-26T23:09:00Z | implementation | Recorded page 015 aggressive batch final human review `P015BATCHREV-G1-VIRAL-001` after Bogdan selected `p015 aggressive batch ok` for the bundle plus `G1SP-G1-VIRAL-010`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final review is limited to the P015 bundle/status; internal P015 stages remain skipped-human-review with Sol/Terra delegated review, page 016+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T232500Z` | 2026-07-26T23:25:00Z | implementation | Prepared P016-P020 sequential aggressive run mode: added a Sourcefold review-packet contract requiring the human packet to expose only source page art and semantic text map markdown for pages 016-020, while keeping crop evidence internal unless a blocker requires escalation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Prep only; no P016-P020 page artifacts, no page 021+ processing, no bulk final-review acceptance, no whole Gate 1, fixture admission, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push, or next-layer authorization. |
| `doc-checkpoint-20260726T234500Z` | 2026-07-26T23:45:00Z | implementation | Prepared pages 016-020 as a sequential aggressive delegated-review run: page-specific preflight authorizations were materialized, internal page artifacts and `G1SP-G1-VIRAL-011` through `G1SP-G1-VIRAL-015` were generated, and the human packet is limited to source art plus semantic text maps. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final batch reviews for P016-P020 are pending; no direct Bogdan per-stage approval is recorded; page 021+ remains unprocessed/not authorized; no bulk final-review acceptance, whole Gate 1 acceptance, fixture admission, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, or push authorization. |
| `doc-checkpoint-20260727T154500Z` | 2026-07-27T15:45:00Z | implementation | Added pipeline-wide semantic split contracts so callout/sidebar/card/Keeper body units must prove their bounded segment; rebuilt P012/P014/P016-P020 with validation and corrected P016/P018 Keeper containment. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Hardening/correction only; P016-P020 final review was still pending at this checkpoint, with no page 021+, whole Gate 1, fixture admission, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, or push authorization. |
| `doc-checkpoint-20260727T162100Z` | 2026-07-27T16:21:00Z | implementation | Recorded `P016BATCHREV-G1-VIRAL-001` through `P020BATCHREV-G1-VIRAL-001` after Bogdan accepted corrected P016/P018 semantic maps and the P016-P020 aggressive batch. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Pages 001-020 are page-complete accepted only; internal P016-P020 stages remain delegated/skipped-human-review; page 021+ remains unprocessed/not authorized, and whole Gate 1/fixtures/source/OCR/PDF/render/raw/translation/proofreading/implementation/push remain blocked. |
| `doc-checkpoint-20260727T164000Z` | 2026-07-27T16:40:00Z | implementation | Created post-P020 status/readiness packet `G1SP-G1-VIRAL-016` and synchronized current status/roadmap/authorization docs so the next route decision starts from pages 001-020 page-complete accepted only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Status/readiness only; no page 021+ processing, whole Gate 1 acceptance, fixture admission, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push, or next-layer authorization. |
| `doc-checkpoint-20260727T173500Z` | 2026-07-27T17:35:00Z | planning | Recorded Bogdan's selected post-P020 route sequence: first Gate 1 source-profile readiness/parking matrix, then OCR benchmark remediation/methodology hardening. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Direction only; neither selected step is started yet, P021/P021-P025 remains unselected, and whole Gate 1/fixtures/source/OCR/PDF/render/raw/translation/proofreading/implementation/push remain blocked until separately authorized. |
| `doc-checkpoint-20260727T174500Z` | 2026-07-27T17:45:00Z | decision-prep | Generated `G1SPRM-G1-VIRAL-001`, a Gate 1 source-profile readiness / parking matrix for human route review after pages 001-020 page-complete acceptance. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Decision-prep only; no source-profile parameter is accepted or parked, OCR remediation/methodology hardening is selected next but not started, page 021+ remains unauthorized, and whole Gate 1/fixtures/source/OCR/PDF/render/raw/translation/proofreading/implementation/push remain blocked. |
| `doc-checkpoint-20260727T201100Z` | 2026-07-27T20:11:00Z | review | Recorded `G1SPRMREV-G1-VIRAL-001` after Bogdan accepted the Gate 1 source-profile readiness / parking matrix with comments. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Route-review artifact acceptance only; no source-profile acceptance, parking decision, OCR remediation execution, page 021+ authorization, fixture admission, source/OCR/PDF/render/raw mutation, translation, proofreading, implementation, push, or whole Gate 1 acceptance. |
| `doc-checkpoint-20260727T203000Z` | 2026-07-27T20:30:00Z | hardening | Generated `OCRHM-G1-VIRAL-001`, an OCR benchmark methodology hardening packet from existing G1SPRMREV/ORM/ORR/ONC/OBR evidence. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Methodology hardening evidence only; no OCR execution, no source-profile acceptance, no parking decision, no page 021+ processing, no fixture admission, no source/OCR/PDF/render/raw mutation, no translation/proofreading/implementation/push, and no whole Gate 1 acceptance. |
| `doc-checkpoint-20260727T204000Z` | 2026-07-27T20:40:00Z | status-refresh | Generated `G1SP-G1-VIRAL-017`, a post-OCR-hardening Gate 1 status/readiness refresh ready for route decision. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Status/readiness refresh only; no source-profile acceptance, no parking decision, no OCR execution or remediation rerun, no page 021+ processing, no fixture admission, no source/OCR/PDF/render/raw mutation, no translation/proofreading/implementation/push, and no whole Gate 1 acceptance. |
| `doc-checkpoint-20260727T213000Z` | 2026-07-27T21:30:00Z | decision-prep | Generated `G1SPRPD-G1-VIRAL-001`, a Gate 1 source-profile review / parking decision prep packet after `G1SP-G1-VIRAL-017`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Decision prep only; no source-profile acceptance, no parking decision, no fixture admission, no page 021+ processing, no OCR execution or remediation rerun, no source/OCR/PDF/render/raw mutation, no translation/proofreading/implementation/push, and no whole Gate 1 acceptance. |
| `doc-checkpoint-20260727T215000Z` | 2026-07-27T21:50:00Z | decision-options | Recorded `G1SPRPDREV-G1-VIRAL-001` and generated `G1SPDP-G1-VIRAL-001`, a Gate 1 source-profile human options packet. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Options packet only; no source-profile acceptance, no parking decision, no fixture admission, no page 021+ processing, no OCR execution or remediation rerun, no source/OCR/PDF/render/raw mutation, no translation/proofreading/implementation/push, and no whole Gate 1 acceptance. |
| `doc-checkpoint-20260727T221500Z` | 2026-07-27T22:15:00Z | decision-record | Recorded `G1SPDR-G1-VIRAL-001`, a bounded Gate 1 source-profile decision record from Bogdan's contextual approval of the immediately preceding `G1SPDP` proposal. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Records 5 Gate review candidates, 2 Core 0.1 OCR parking decisions with invalidation conditions, 2 evidence-only rows, 2 blocked rows, and 1 page 021+ separate-BA row; no whole source-profile acceptance, fixture admission, page 021+ processing, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or whole Gate 1 acceptance. |
| `doc-checkpoint-20260727T224500Z` | 2026-07-27T22:45:00Z | readiness-prep | Generated `G1FARP-G1-VIRAL-001`, a fixture-admission / whole-Gate-acceptance readiness prep packet from `G1SPDR-G1-VIRAL-001`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Readiness prep only; fixture admission and whole Gate 1 remain future decisions, unsupported/negative fixture policy remains blocked, page 021+ remains separate BA only, and no fixture manifest, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260727T230000Z` | 2026-07-27T23:00:00Z | blocker-prep | Recorded `G1FARPREV-G1-VIRAL-001` and generated `G1FABRP-G1-VIRAL-001`, a fixture admission blocker resolution prep packet. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Blocker-resolution prep only; no fixture admission, fixture manifest, whole Gate 1 acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or blocker resolution is created. |
| `doc-checkpoint-20260727T231500Z` | 2026-07-27T23:15:00Z | review | Recorded `G1FABRPREV-G1-VIRAL-001` after Bogdan accepted `G1FABRP-G1-VIRAL-001` as blocker-resolution prep only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Prep-review only; no blocker resolution, fixture admission, fixture manifest, whole Gate 1 acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260727T232500Z` | 2026-07-27T23:25:00Z | decision-prep | Generated `G1UNFPDP-G1-VIRAL-001`, an unsupported/negative fixture policy decision prep packet. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Decision prep only; no policy decision, blocker resolution, fixture admission, fixture manifest, whole Gate 1 acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T190000Z` | 2026-07-28T19:00:00Z | decision-record-prep | Recorded `G1UNFPDPREV-G1-VIRAL-001` and generated `G1UNFPR-G1-VIRAL-001`, the unsupported/negative fixture policy record candidate over four reviewed questions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Policy record candidate only; no policy decision, blocker resolution, fixture admission, fixture manifest, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T193600Z` | 2026-07-28T19:36:00Z | decision-record | Recorded `G1UNFPAR-G1-VIRAL-001`, accepting `G1UNFPR-G1-VIRAL-001` as the unsupported/negative fixture policy record over four questions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Unsupported/negative fixture policy decision accepted only; no fixture admission, fixture manifest, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T200500Z` | 2026-07-28T20:05:00Z | decision-prep | Generated `G1FSFDP-G1-VIRAL-001`, a fixture strategy fit decision-prep packet after unsupported/negative fixture policy acceptance. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Fixture strategy fit decision prep only; no fixture strategy fit decision, fixture admission, fixture manifest, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T203900Z` | 2026-07-28T20:39:00Z | decision-record | Recorded `G1FSFAR-G1-VIRAL-001`, accepting `G1FSFDP-G1-VIRAL-001` as the fixture strategy fit decision over five questions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Fixture strategy fit decision accepted only; no fixture admission, fixture manifest, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T210800Z` | 2026-07-28T21:08:00Z | readiness-refresh | Recorded `G1FARR-G1-VIRAL-001`, refreshing fixture admission readiness after accepted unsupported/negative fixture policy and fixture strategy fit decisions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Fixture admission readiness refresh only; no fixture admission, fixture manifest, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T213200Z` | 2026-07-28T21:32:00Z | decision-prep | Generated `G1FMP-G1-VIRAL-001`, a fixture manifest prep packet after fixture admission readiness refresh. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Fixture manifest prep only; no actual fixture manifest, fixture admission, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T214800Z` | 2026-07-28T21:48:00Z | decision-record | Recorded `G1FMR-G1-VIRAL-001`, accepting `G1FMP-G1-VIRAL-001` as the fixture manifest record without fixture admission. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Fixture manifest record only; no fixture admission, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T221800Z` | 2026-07-28T22:18:00Z | decision-prep | Generated `G1FADP-G1-VIRAL-001`, a fixture admission decision-prep packet after the fixture manifest record. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Fixture admission decision prep only; no fixture admission decision, fixture admission, whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260728T230000Z` | 2026-07-28T23:00:00Z | decision-record | Recorded `G1FADAR-G1-VIRAL-001`, accepting the fixture admission decision after `G1FADP-G1-VIRAL-001`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Fixture admission decision accepted only; no whole Gate 1 acceptance, whole source-profile acceptance, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260729T101000Z` | 2026-07-29T10:10:00Z | readiness-prep | Generated `G1WGARR-G1-VIRAL-001`, a whole Gate 1 acceptance readiness recheck packet after `G1FADAR-G1-VIRAL-001`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Readiness recheck prep only; no whole Gate 1 acceptance, whole source-profile acceptance, new or broader fixture admission, page 021+ processing/authorization, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260729T112700Z` | 2026-07-29T11:27:00Z | decision-record | Recorded `G1WGADR-G1-VIRAL-001`, accepting whole Gate 1 only for pages 001-020 and the `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Whole Gate 1 acceptance record only; no page 021+ processing/authorization, no source-profile acceptance beyond this Gate 1 record, no new or broader fixture admission, OCR execution/remediation rerun, source/OCR/PDF/render/raw mutation, translation/proofreading/implementation/push, or downstream action is created. |
| `doc-checkpoint-20260726T174200Z` | 2026-07-26T17:42:00Z | implementation | Promoted crop provenance from the first P012 consumer into an aggressive-builder gate: every `build_page_*_aggressive_batch.py` must import/call the shared crop contract validator and define explicit text-evidence crop contracts. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Hardening only; no page 013 artifact generation, no page/whole-Gate acceptance, no fixture admission, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, or push authorization. |
| `doc-checkpoint-20260726T151306Z` | 2026-07-26T15:13:06Z | implementation | Prepared page 012 aggressive delegated-review batch `P012BATCH-G1-VIRAL-001`: internal P012TR/P012TXT/P012SEM/PCRP/P012PCA stages carry Sol/Terra OK evidence and skipped human-review labels, then `G1SP-G1-VIRAL-007` routes final human review on the bundle/status. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Final batch review pending; no direct Bogdan per-stage approval is recorded; page 013+ remains unprocessed, and whole Gate 1, fixtures, source/OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260726T144223Z` | 2026-07-26T14:42:23Z | implementation | Prepared post-P011 Gate 1 status/route packet `G1SP-G1-VIRAL-006` as status-only routing evidence: pages 001-011 are page-complete accepted only, pages 012-020 remain unstarted, and page 012 triage/readiness is only the next recommended candidate. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Status/route packet only; no page 012 authorization, whole Gate 1 acceptance, fixture admission, source mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, or push. |
| `doc-checkpoint-20260724T221618Z` | 2026-07-24T22:16:18Z | implementation | Accepted page 008 as page-complete only through `P008PCA-G1-VIRAL-001` after Bogdan approved `PCRP-G1-VIRAL-P008-001`; the acceptance binds to 7/7 ready blocks, two deferred art/photo anchors, paragraph-preserving semantic units, valid inventory reconciliation, and zero structural findings. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 008 only; whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260724T233542Z` | 2026-07-24T23:35:42Z | implementation | Prepared post-P008 Gate 1 status/route packet `G1SP-G1-VIRAL-002` as status-only routing evidence: pages 002-008 are page-complete accepted only, source reconstruction remains the canonical narrow 13 accepted records without a new source rollup, `G1SP-G1-VIRAL-001` is historical/narrow/stale for current status, and first-class blocker and negative capability matrices are explicit. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Status/route packet only; no next-layer authorization, whole Gate 1 acceptance, fixture admission, source mutation, OCR/PDF/render/raw mutation, page 009+ processing, translation, proofreading, renderer/profile acceptance, implementation, or push. |
| `doc-checkpoint-20260725T000106Z` | 2026-07-25T00:01:06Z | implementation | Prepared page 001 triage/readiness routing packet `P001TR-G1-VIRAL-001` after Bogdan selected page 001 triage/review as the next layer; the packet uses existing rendered page/image/map/status evidence to route page 001 as a visual/title page-complete review candidate without OCR benchmark remediation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Triage/routing only; page 001 is not accepted as complete, OCR remediation remains a separate later branch, and whole Gate 1, fixture admission, source mutation, OCR/PDF/render/raw mutation, page 009+ processing, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260725T002048Z` | 2026-07-25T00:20:48Z | implementation | Prepared page 001 page-complete review packet `PCRP-G1-VIRAL-P001-001` after Bogdan approved the P001 triage route; the packet packages page 001 as a visual/title cover page with full-page, title/logo, and footer/rating/tagline/logo deferred visual anchors. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 001 is not accepted as complete, OCR remediation remains a separate later branch, and whole Gate 1, fixture admission, source mutation, OCR/PDF/render/raw mutation, page 009+ processing, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260725T082722Z` | 2026-07-25T08:27:22Z | implementation | Accepted page 001 as page-complete only through `P001PCA-G1-VIRAL-001` after Bogdan approved `PCRP-G1-VIRAL-P001-001`; the acceptance binds to 3/3 ready visual/title anchors, no blockers, no open questions, and the exact predecessor review packet hashes. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 001 only; whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, page 009+ processing, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260725T084219Z` | 2026-07-25T08:42:19Z | implementation | Prepared post-P001 status/route refresh `G1SP-G1-VIRAL-003` and page 009 triage/readiness packet `P009TR-G1-VIRAL-001`; the status packet records pages 001-008 as page-complete accepted only, and the triage packet packages page 009 as a two-profile visual/text review candidate. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Status/triage only; page 009 is not accepted as complete, pages 010-020 are not processed, and whole Gate 1, fixtures, source mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260725T090825Z` | 2026-07-25T09:08:25Z | implementation | Superseded held page 009 triage packet `P009TR-G1-VIRAL-001` with `P009TR-G1-VIRAL-002` after Bogdan flagged crooked/text-clipping review crops; the superseding packet uses readable padded portrait crops and full-column text crops. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Triage only; page 009 is not accepted as complete, pages 010-020 are not processed, and whole Gate 1, fixtures, source mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260725T100006Z` | 2026-07-25T10:00:06Z | documentation | Recorded the pre-PCRP page 009 crop-role remediation plan after Bogdan clarified that review crops are downstream OCR inputs. `P009TR-G1-VIRAL-002` remains historical/readability-only; Bogdan confirmed the right lower grey block is complete; `PCRP-G1-VIRAL-P009-001` is blocked until `P009TR-G1-VIRAL-003` supplies role-separated OCR-safe text evidence crops and QA. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Documentation/plan only; no `P009TR-G1-VIRAL-003`, no `PCRP-G1-VIRAL-P009-001`, no page 009 acceptance, no pages 010-020 processing, and no OCR/PDF/render/raw/source/fixture/translation/proofreading/implementation/push authorization. |
| `doc-checkpoint-20260725T102015Z` | 2026-07-25T10:20:15Z | documentation | Corrected the post-Sol/Terra page 009 cursor after reviewing project goals, triage goals, and roadmap state: `P009TR-G1-VIRAL-002` is stale for PCRP routing, the current bounded continuation is `page_009_crop_contract_missing_pcrp_blocked`, and the next required implementation layer is a separately authorized `P009TR-G1-VIRAL-003` crop-role/OCR-safe contract. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Documentation/plan correction only; no `P009TR-G1-VIRAL-003`, no `PCRP-G1-VIRAL-P009-001`, no OCR execution/evidence, no source/page/whole-Gate acceptance, no pages 010-020 processing, and no fixture/translation/proofreading/implementation/push authorization. |
| `doc-checkpoint-20260724T212402Z` | 2026-07-24T21:24:02Z | implementation | Prepared page 008 review packet `PCRP-G1-VIRAL-P008-001` as a separate `full P008` step with action backlog, two deferred art/photo anchors, paragraph-preserving semantic units, valid validation/projection/inventory reconciliation, and zero structural findings. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 008 is not accepted as complete, whole Gate 1 is not accepted, and fixtures/source acceptance mutation/OCR/PDF/render/raw mutation/translation/proofreading/implementation/push remain blocked. |
| `doc-checkpoint-20260724T210633Z` | 2026-07-24T21:06:33Z | implementation | Promoted P007 review lessons into general page-review pipeline hardening: paragraph-boundary preservation is now a semantic-unit invariant, and commit-stage work is frozen to pathspec staging/check/name-only/commit only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Process/validator/documentation only; page 008, whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push, and candidate artifact rebuilds remain blocked. |
| `doc-checkpoint-20260724T185039Z` | 2026-07-24T18:50:39Z | implementation | Prepared page 007 review packet `PCRP-G1-VIRAL-P007-001` as the first isolated step in Bogdan's requested `full 7 -> full 8 -> Gate 1` sequence; the packet packages page 007 crops, verified text map, semantic JSON/Markdown, projection validation, and inventory reconciliation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 007 is not accepted as complete, page 008 is not processed, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260724T194737Z` | 2026-07-24T19:47:37Z | implementation | Held `PCRP-G1-VIRAL-P007-001` after Bogdan review and prepared superseding page 007 packet `PCRP-G1-VIRAL-P007-002` with a deferred Spektral Krew art anchor plus article text blocks. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 007 is not accepted as complete, page 008 is not processed, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260724T201203Z` | 2026-07-24T20:12:03Z | implementation | Held `PCRP-G1-VIRAL-P007-002` after Bogdan found paragraph-boundary flattening and prepared `PCRP-G1-VIRAL-P007-003` with paragraph-preserving semantic units. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 007 is not accepted as complete, page 008 is not processed, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260724T202839Z` | 2026-07-24T20:28:39Z | implementation | Accepted page 007 as page-complete only through `P007PCA-G1-VIRAL-001` after Bogdan approved `PCRP-G1-VIRAL-P007-003`; the acceptance binds to the paragraph-preserving packet with 3/3 ready blocks, one deferred `ui_art_anchor`, valid semantic validation, valid inventory reconciliation, and zero structural findings. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 007 only; page 008, whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260724T181439Z` | 2026-07-24T18:14:39Z | implementation | Refreshed page 005 as `PCRP-G1-VIRAL-P005-004` against the current semantic-map page-complete contract, then accepted page 005 as page-complete only through `P005PCA-G1-VIRAL-001` after Bogdan's explicit `ок делай 5 сразу и коммит` decision. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 005 only; whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260724T144302Z` | 2026-07-24T14:43:02Z | implementation | Accepted page 006 as page-complete only through `P006PCA-G1-VIRAL-001` after Bogdan approved `PCRP-G1-VIRAL-P006-002`; the acceptance binds to the superseding semantic-map review packet with 3/3 ready blocks, valid semantic validation, valid inventory reconciliation, and zero structural findings. Also removed stale embedded fallback roadmap state from `roadmap_viewer.html` so canonical `roadmap.yaml` remains the live source. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 006 only; whole Gate 1, page 005, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T130457Z` | 2026-07-24T13:04:57Z | implementation | Generated superseding page 006 review packet `PCRP-G1-VIRAL-P006-002` after semantic-map hardening: semantic JSON/projection/inventory gates pass, P006 units are separated, Overview continuation is linked, and the human text map uses metadata rows plus fenced full-text blocks. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 006 is not accepted as complete until Bogdan explicitly says `page 006 complete ok`; whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T124724Z` | 2026-07-24T12:47:24Z | documentation | Implemented semantic-map hardening step 10 contract sync: readiness/page-complete contract surfaces now define `semantic_map_ready`, `semantic_map_blocked`, and `semantic_unit_review_only`; canonical semantic JSON, Markdown projection validation, inventory reconciliation, structural findings, and complete-ok suppression are first-class gates. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Contract documentation only; P006-001 remains held/blocked, P006-002 is not generated, final superseding P006 review remains next, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T123031Z` | 2026-07-24T12:30:31Z | implementation | Implemented semantic-map hardening step 9 mixed-layout regression coverage: synthetic tests now cover TOC rows/page refs, art+caption, table rows/cells, callout/sidebar/card/stat units, visual-only page markers, context-only insets, unknown unsupported regions, and topology-flattening blockers. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Regression/validator taxonomy layer only; P006-001 remains held/blocked, P006-002 is not generated, contract sync and P006-002 generation remain next, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T115827Z` | 2026-07-24T11:58:27Z | implementation | Implemented semantic-map hardening step 8 negative guards: validator/tests now block display-style leakage from block roles, collapsed multi-unit regions, missing expected headings, flattened quotes, and ready routing when structural findings exist. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Validator/test layer only; P006-001 remains held/blocked, P006-002 is not generated, mixed-layout regression fixtures and contract sync remain next, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T111541Z` | 2026-07-24T11:15:41Z | implementation | Implemented semantic-map hardening step 7 inventory gating: generated page-complete reports now derive page inventory from readiness blocks/context regions, reconcile it against semantic map units, expose `inventory_reconciliation`, and add `inventory_reconciliation_blocker` before decision options when reconciliation is blocked. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | P006-001 inventory reconciliation is valid while semantic validation still blocks on `invalid_heading_level`; P006-001 remains held/blocked, P006-002 is not generated, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T104904Z` | 2026-07-24T10:49:04Z | implementation | Implemented semantic-map hardening step 6 report gating: semantic validation and Markdown projection validation now surface in page-complete reports/packets/summaries as `semantic_units_validated`, `semantic_validation`, `markdown_projection_validation`, `structural_findings`, and readiness blockers before decision options. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | P006-001 remains held/blocked with semantic validation and Bogdan hold blockers, P006-002 is not generated, full page-inventory reconciliation is not yet wired into generated packet gating, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T090922Z` | 2026-07-24T09:09:22Z | implementation | Implemented semantic-map hardening step 5 builder wiring: inline readiness spans now generate packaged semantic map JSON and Markdown projection artifacts with stable semantic unit IDs, crop/source links, validation state, and projection validation while preserving P006-001 blocked routing. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Builder emits semantic map artifacts for P006-001, but P006-001 remains held/blocked and P006-002 is not generated; semantic validation is packaged but not yet promoted into the full structural readiness gate for all profiles; whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T085022Z` | 2026-07-24T08:50:22Z | implementation | Implemented semantic-map hardening step 4 predicates: page inventory reconciliation now requires each observed/expected region to resolve to represented, absent, context-only, visual-only, excluded, unknown, or blocked, with blockers for unrepresented regions lacking classified in-scope units, missing decisions, unknown regions without blocking units or conflicting with classified text, region refs outside inventory, and missing expected unit types. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Predicate layer only; builder does not yet derive/reconcile semantic units for generated packets, P006-002 remains blocked until builder integration/full structural validation/regression fixtures are complete and reviewed, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T082058Z` | 2026-07-24T08:20:58Z | implementation | Implemented semantic-map hardening step 3 primitives: canonical semantic map JSON document builder plus Markdown projection with metadata-only unit summary table, dynamically fenced per-unit full-text blocks, structural findings, Not Evidence For boundaries, and scoped projection integrity validation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Projection primitives only; current P006-001 legacy text map remains blocked negative regression evidence, P006-002 remains blocked until builder integration/filling rules/full validation/regression fixtures are complete and reviewed, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T080720Z` | 2026-07-24T08:07:20Z | implementation | Implemented semantic-map hardening step 2 primitives: versioned `semantic_units` schema/taxonomy, controlled unit/scope/display/source/block/text/review enums, and validator findings for stale schema/taxonomy, invalid heading levels, unknown fallback, non-empty cardinality, contiguous reading order, duplicate IDs, and broken/mistyped links. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Contract primitives only; generated maps are not yet rebuilt from semantic units, page 006 remains not accepted as complete, P006-002 remains blocked until template/builder/validator integration and review, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T075333Z` | 2026-07-24T07:53:33Z | implementation | Implemented semantic-map hardening step 1: `PCRP-G1-VIRAL-P006-001` now carries a machine-readable post-review hold state, blocks page-complete decision routing, requires `PCRP-G1-VIRAL-P006-002`, and keeps the old text map only as negative regression input. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 006 remains not accepted as complete; P006-002 remains blocked until the remaining semantic-map hardening steps are implemented and reviewed, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, and push remain blocked. |
| `doc-checkpoint-20260724T074002Z` | 2026-07-24T07:40:02Z | documentation | Integrated Sol/Terra refinement into `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`: schema/taxonomy versioning, per-unit lineage, full-page reconciliation, markdown projection validation, non-waivable structural findings, decision-option suppression, boundary tests, and generic mixed-layout regression fixtures. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Refinement only; P006 remains held/not complete, P006-002 is blocked until semantic-map hardening is implemented and reviewed, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260724T071222Z` | 2026-07-24T07:12:22Z | documentation | Recorded Bogdan's hold on `PCRP-G1-VIRAL-P006-001` and promoted the issue to semantic-map pipeline hardening: page 006 crops are ok, but the text map collapses headings, quote, body text, and continuation semantics. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Current goal is `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`; P006 remains held/not complete, P006-002 waits for contract/template/generator/validator/test hardening, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260724T004358Z` | 2026-07-24T00:43:58Z | documentation | Prepared readable page 005 review packet `PCRP-G1-VIRAL-P005-003` with title-only, left-column, and right-column crops plus OCR/verified text map and crop-edge readability checks. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 005 is not accepted as complete, and whole Gate 1, new fixtures, source acceptance mutation, PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260724T001551Z` | 2026-07-24T00:15:51Z | documentation | Prepared superseding page 005 page-complete review packet `PCRP-G1-VIRAL-P005-002` with full declared `box_px` crops generated from `page_005.png`; visual proof passes strict 1.00 for `P005-B001` and `P005-B002`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 005 is not accepted as complete, and whole Gate 1, new fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260723T235422Z` | 2026-07-23T23:54:22Z | documentation | Hardened `build_page_complete_review.py` with visual proof checks: block crops must cover the declared readiness `box_px` dimensions. Regenerated `PCRP-G1-VIRAL-P005-001` as blocked because `P005-B001` uses a 860x260 crop for a 750x280 declared block and `P005-B002` uses a 560x235 crop for a 2050x2300 declared block. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Logic/packet hardening only; page 005 is not accepted as complete, and whole Gate 1, new fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260723T234510Z` | 2026-07-23T23:45:10Z | documentation | Recorded Bogdan's `hold page 005` decision for `PCRP-G1-VIRAL-P005-001`: crop coverage is insufficient, the R003/contents-entry crop cuts off text, and a superseding page 005 review packet needs broader/more crops. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Hold/status only; page 005 is not accepted as complete, and whole Gate 1, new fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260723T224528Z` | 2026-07-23T22:45:28Z | documentation | Recorded Bogdan's explicit `page 004 complete ok` decision as `P004PCA-G1-VIRAL-001`, accepting page 004 as complete only after `PCRP-G1-VIRAL-P004-001`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 004 only; whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260723T231200Z` | 2026-07-23T23:12:00Z | documentation | Prepared page 005 page-map readiness `PMRP-G1-VIRAL-P005-001`: contents heading and contents/list entry group ready, margin page marker visual-only, no blockers/open questions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Readiness only; page 005 is not accepted as complete, and whole Gate 1, new fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260723T232600Z` | 2026-07-23T23:26:00Z | documentation | Prepared page 005 page-complete review packet `PCRP-G1-VIRAL-P005-001` from `PMRP-G1-VIRAL-P005-001`, with page image, two crop anchors, and OCR/block text review asset. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review packet only; page 005 is not accepted as complete, and whole Gate 1, new fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260723T220255Z` | 2026-07-23T22:02:55Z | documentation | Prepared page 004 page-map readiness `PMRP-G1-VIRAL-P004-001` and page-complete review packet `PCRP-G1-VIRAL-P004-001`: two accepted text blocks ready, one confirmed context-only inset, four review assets packaged, no blockers/open questions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Review/readiness only; page 004 is not accepted as complete, and whole Gate 1, fixtures, source acceptance mutation, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, push remain blocked. |
| `doc-checkpoint-20260723T213354Z` | 2026-07-23T21:33:54Z | documentation | Recorded structure display normalization `SDN-G1-VIRAL-001`: future human-facing generators display body/text-only `heading_level none` as `text_body`, and prior affected packets get normalized display copies without mutating original predecessor evidence. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Display-only normalization; no source acceptance, page-complete acceptance, whole Gate 1 acceptance, fixture admission, OCR/PDF/render/raw mutation, translation, proofreading, renderer/profile acceptance, implementation, or push is created. |
| `doc-checkpoint-20260723T210205Z` | 2026-07-23T21:02:05Z | documentation | Recorded page 004 context-only decision packet update and Bogdan's explicit `page 004 context-only ok` confirmation as `P004COD-G1-VIRAL-001`; human-facing body-only structure label now uses `text_body` instead of ambiguous `none`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Page 004 full tilted inset is context-only only; page 004 is not accepted as complete; whole Gate 1, fixtures, source acceptance mutation, translation, proofreading, renderer/profile acceptance, implementation, push, OCR/PDF/render/raw mutation remain blocked. |
| `doc-checkpoint-20260719T174526Z` | 2026-07-19T17:45:26Z | documentation | Recorded Bogdan message `523` as human verification `SRCRV-G1-VIRAL-004` for the two draft page-004 review records; verification report SHA-256 `95041F808A1C2F44A417245BF3E25318C9BDE36183CCE7C4E372DF9363812FBA`, manifest SHA-256 `21B3CE0135D4D8CF09C394C192D7976766DA9DA1E55DE5F9B3FE240380CC0AB0`, summary SHA-256 `F342D7DA0CBB7245812B8B3291F2C5585D880DA67D6C24DCAFEC4FF8B86D9011`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Verification only; page 004 source acceptance and QA require separate bounded authorization; page 002/003/004 remain incomplete; whole Gate 1 remains unaccepted. |
| `doc-checkpoint-20260719T182626Z` | 2026-07-19T18:26:26Z | documentation | Recorded page 004 verified review QA, narrow two-record source acceptance, crop guardrail consumption, and rollup to 13 accepted source reconstruction records; report SHA-256 `0CCB4AA33481BDB0B95B02D32A0E49FB1A20FD9A957DB7DAE1ECB0B00307622E`, manifest SHA-256 `75C0C0BD96FF77E64D2F7C827D7D21B12F7EF15964E8EC9734F9428CCC064C06`, summary SHA-256 `BF664162A899765C3B614F87002792D213D70DB82A7ED4142686AA439D50C64C`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Page 004 remains not accepted as complete; page 002/003 remain incomplete; whole Gate 1, fixtures, translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked. |
| `doc-checkpoint-20260719T193720Z` | 2026-07-19T19:37:20Z | documentation | Added explicit Sourcefold orchestrator review workflow to `AGENTS.md`: Sol analytical review plus Terra critical review must both return OK before the orchestrator proceeds, and Bogdan receives attached human-facing target files with decision impact explanations rather than hashes, pytest output, test keys, or internal QA checklists. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Process documentation only; no source acceptance, page-complete acceptance, whole Gate 1 acceptance, fixture admission, implementation, push, OCR/PDF/render/raw mutation, translation, proofreading, or renderer/profile acceptance is created. |
| `doc-checkpoint-20260719T201558Z` | 2026-07-19T20:15:58Z | documentation | Prepared page-completeness triage packet `PGCT-G1-VIRAL-001` for selected pages 1-20 after `P004A-G1-VIRAL-004`: pages 002/003 ready for later page-complete review packets, page 004 held pending context-only decision for the full tilted inset, pages 001/005/006 incomplete, and pages 007-020 unstarted for source-reconstruction acceptance. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Triage/status only; no page-complete acceptance, whole Gate 1 acceptance, fixture admission, source acceptance, implementation, push, OCR/PDF/render/raw mutation, translation, proofreading, or renderer/profile acceptance is created. |
| `doc-checkpoint-20260719T212402Z` | 2026-07-19T21:24:02Z | documentation | Added draft page-map readiness indicators to the Gate 1 map/spec surfaces: page block inventory, advisory coverage summaries, existing-artifact-only OCR/text fidelity indicators, structural/semantic risk checks, overlay/reading-order/anchor blockers, and the page 002 two-block readiness example. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Readiness/spec documentation only; percentages are advisory and cannot accept pages. No page-complete acceptance, whole Gate 1 acceptance, fixture admission, implementation, push, OCR/PDF/render/raw mutation, translation, proofreading, or renderer/profile acceptance is created. |
| `doc-checkpoint-20260719T215028Z` | 2026-07-19T21:50:28Z | documentation | Recorded Bogdan's correction that page 002 is only the pilot/proving case for a universal, reproducible `page_map` readiness pipeline. The next implementation plan is a generic readiness builder plus page-specific profiles, starting with page 002 only under a separate bounded authorization. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Planning/status only; no builder, tests, generated readiness packet, OCR/PDF/render/raw mutation, page-complete acceptance, whole Gate 1 acceptance, fixture admission, translation, proofreading, renderer/profile acceptance, implementation, push, or new source slice is created. |
| `doc-checkpoint-20260719T215804Z` | 2026-07-19T21:58:04Z | documentation | Promoted the universal page-map readiness pipeline from checkpoint narrative into the shared Gate 1 roadmap/hierarchy: new roadmap node `gate-01-page-map-readiness-pipeline`, dependency edges from pre-OCR map model toward source-profile decision, and hierarchy subcomponent `SC-PAGE_MAP_READINESS`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, gate-01-page-map-readiness-pipeline | Roadmap/schema integration only; no builder, tests, generated readiness packet, OCR/PDF/render/raw mutation, page-complete acceptance, whole Gate 1 acceptance, fixture admission, implementation, push, translation, proofreading, renderer/profile acceptance, or new source slice is created. |
| `doc-checkpoint-20260719T162334Z` | 2026-07-19T16:23:34Z | documentation | Prepared page 004 review-only source reconstruction packet `SRCR-G1-VIRAL-004` under `BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004`; report SHA-256 `C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A`, manifest SHA-256 `30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4`, review packet SHA-256 `1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Page 004 review packet is draft/not accepted; page 002/003/004 remain incomplete; whole Gate 1 remains unaccepted. |
| `doc-checkpoint-20260718T223926Z` | 2026-07-18T22:39:26Z | documentation | Recorded page 003 verified review QA, global crop-layout guardrail, two-record source acceptance, and rollup to 11 accepted source reconstruction records; crop-contract hardening regenerated lineage through P003A; report SHA-256 `9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B`, manifest SHA-256 `F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87`, summary SHA-256 `860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Page 003 remains incomplete; whole Gate 1 remains unaccepted. |
| `doc-checkpoint-20260718T214429Z` | 2026-07-18T21:44:29Z | documentation | Recorded page 002 QA, structure/semantics, structure QA, two-record source acceptance, second narrow rollup, remediated page 003 draft review packet `SRCR-G1-VIRAL-003`, and Bogdan message `437` ok/ok verification; crop-contract hardening regenerated lineage through P002C; report SHA-256 `A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F`, manifest SHA-256 `8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6`, review packet SHA-256 `81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | Page 002 remains incomplete; page 003 packet is verified draft only, not source accepted; crop-cut and crop-overlap debt recorded for QA/test coverage. |
| `doc-checkpoint-20260718T210754Z` | 2026-07-18T21:07:54Z | documentation | Prepared page 002 QA and structure evaluation packet; SHA-256 `F261CB0035BB588A5F347A0BE30C7E7E0E8910BE505E3C913357A539E93F11BA`. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T202535Z` | 2026-07-18T20:25:35Z | documentation | Recorded Viral page 002 assisted draft human verification. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T195540Z` | 2026-07-18T19:55:40Z | documentation | Prepared Viral page 002 assisted source reconstruction draft for Bogdan verification. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T182756Z` | 2026-07-18T18:27:56Z | documentation | Prepared Viral page 002 source reconstruction next-slice review packet. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T174435Z` | 2026-07-18T17:44:35Z | documentation | Recorded Viral Gate 1 status packet for the narrow source reconstruction slice. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T163725Z` | 2026-07-18T16:37:25Z | documentation | Recorded Viral Gate 1 narrow source reconstruction evidence rollup. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T152814Z` | 2026-07-18T15:28:14Z | documentation | Recorded Viral Gate 1 narrow source reconstruction decision. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T150016Z` | 2026-07-18T15:00:16Z | documentation | Recorded Viral Gate 1 review decision brief. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T145118Z` | 2026-07-18T14:51:18Z | documentation | Recorded Viral Gate 1 review packet. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T142741Z` | 2026-07-18T14:27:41Z | documentation | Recorded Viral source reconstruction fixture admission. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T141808Z` | 2026-07-18T14:18:08Z | documentation | Clarified current planning mode after source reconstruction QA. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T135919Z` | 2026-07-18T13:59:19Z | documentation | Recorded Viral source reconstruction QA over human-reviewed source text. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T133656Z` | 2026-07-18T13:36:56Z | documentation | Recorded Viral source reconstruction human source review decisions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T122003Z` | 2026-07-18T12:20:03Z | documentation | Recorded Viral source reconstruction human review package. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T120341Z` | 2026-07-18T12:03:41Z | documentation | Recorded Viral source reconstruction visual/overlay review decisions. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T113050Z` | 2026-07-18T11:30:50Z | documentation | Recorded Viral source reconstruction rebuild evidence. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T112623Z` | 2026-07-18T11:26:23Z | documentation | Recorded Viral source reconstruction refined OCR evidence. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T111226Z` | 2026-07-18T11:12:26Z | documentation | Recorded Viral source reconstruction crop/overlay remediation evidence. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T105216Z` | 2026-07-18T10:52:16Z | documentation | Recorded Viral source reconstruction remediation triage. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T103916Z` | 2026-07-18T10:39:16Z | documentation | Recorded Viral source reconstruction candidate review package. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T102416Z` | 2026-07-18T10:24:16Z | documentation | Recorded Viral source reconstruction prep package and fail-closed contracts. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T095416Z` | 2026-07-18T09:54:16Z | documentation | Recorded Viral OCR remediation review package and contract checks. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T091319Z` | 2026-07-18T09:13:19Z | documentation | Recorded Viral OCR remediation matrix with Sourcefold-native logic transfer. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T075138Z` | 2026-07-18T07:51:38Z | documentation | Recorded Viral bounded OCR benchmark result. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T070917Z` | 2026-07-18T07:09:17Z | documentation | Recorded Viral OCR candidate executable refresh. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T061027Z` | 2026-07-18T06:10:27Z | documentation | Recorded Viral gold samples and OCR candidate manifest. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T055944Z` | 2026-07-18T05:59:44Z | documentation | Recorded Viral OCR benchmark prerequisite blocker. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T055701Z` | 2026-07-18T05:57:01Z | documentation | Recorded Viral OCR preparation package. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T055439Z` | 2026-07-18T05:54:39Z | documentation | Recorded Viral pre-OCR map bundle freeze. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T055234Z` | 2026-07-18T05:52:34Z | documentation | Recorded Viral map consistency validation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T055019Z` | 2026-07-18T05:50:19Z | documentation | Recorded Viral trial art map. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T054748Z` | 2026-07-18T05:47:48Z | documentation | Recorded Viral trial content map. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T054517Z` | 2026-07-18T05:45:17Z | documentation | Recorded Viral trial doc map registry. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T054158Z` | 2026-07-18T05:41:58Z | documentation | Recorded Viral forward plan and map schema identity packet. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260718T044821Z` | 2026-07-18T04:48:21Z | documentation | Recorded Viral map-bundle prerequisite review; bundle freeze blocked. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260717T212008Z` | 2026-07-17T21:20:08Z | documentation | Recorded bounded provisional region map for rendered Viral pages. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260717T205530Z` | 2026-07-17T20:55:30Z | documentation | Recorded bounded page-map model for rendered Viral pages. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260717T182626Z` | 2026-07-17T18:26:26Z | documentation | Recorded bounded page inventory for rendered Viral pages. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260717T180329Z` | 2026-07-17T18:03:29Z | documentation | Recorded bounded visual sanity review for rendered Viral pages. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260717T174729Z` | 2026-07-17T17:47:29Z | documentation | Executed bounded render trial for selected Viral pages only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260717T172518Z` | 2026-07-17T17:25:18Z | documentation | Executed first bounded trial by creating selected-page manifest only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260717T172129Z` | 2026-07-17T17:21:29Z | documentation | Accepted exact Gate 1 Qualification Protocol revision and recorded first bounded trial authorization. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260717T165139Z` | 2026-07-17T16:51:39Z | documentation | Resolved OpenClaw Step 10 review blockers; protocol review_ready for review only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260717T164232Z` | 2026-07-17T16:42:32Z | documentation | Drafted OpenClaw Step 10 review checkpoint with governance blockers. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T174911Z` | 2026-07-15T17:49:11Z | documentation | Drafted Step 4 candidate PDF intake rules after committed Step 3. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T180053Z` | 2026-07-15T18:00:53Z | documentation | Remediated Sol Step 4 intake blockers; renewed Sol/Terra review required. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T180524Z` | 2026-07-15T18:05:24Z | documentation | Recorded Sol/Terra OK for Step 4 remediation; Step 4 ready to commit. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T180644Z` | 2026-07-15T18:06:44Z | documentation | Committed Step 4 and drafted Step 5 render benchmark protocol for review. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T181238Z` | 2026-07-15T18:12:38Z | documentation | Remediated Sol Step 5 render benchmark blockers; renewed Sol/Terra review required. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T181626Z` | 2026-07-15T18:16:26Z | documentation | Applied second Sol Step 5 remediation for comparison-plan output binding and stale Step 4 labels. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T182049Z` | 2026-07-15T18:20:49Z | documentation | Recorded Sol/Terra final OK for Step 5; Step 5 ready to commit. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T182301Z` | 2026-07-15T18:23:01Z | documentation | Committed Step 5 and drafted Step 6 pre-OCR map qualification for review. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260715T183830Z` | 2026-07-15T18:38:30Z | documentation | Remediated Sol/Terra Step 6 map qualification blockers; renewed review required. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260715T184459Z` | 2026-07-15T18:44:59Z | documentation | Applied second Sol Step 6 remediation for bundle-freezing authorization and live labels. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260715T184926Z` | 2026-07-15T18:49:26Z | documentation | Recorded Sol/Terra final OK for Step 6; Step 6 ready to commit. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model | |
| `doc-checkpoint-20260715T185125Z` | 2026-07-15T18:51:25Z | documentation | Committed Step 6 and drafted Step 7 OCR benchmark protocol for review. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T185753Z` | 2026-07-15T18:57:53Z | documentation | Recorded Step 7 agent results and local remediation; renewed Sol/Terra review required. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T190240Z` | 2026-07-15T19:02:40Z | documentation | Recorded renewed Sol/Terra OK for Step 7 remediation; Step 7 ready to commit. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T190417Z` | 2026-07-15T19:04:17Z | documentation | Recorded Step 7 commit and drafted Step 8 QA and non-waivable findings for review. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T191051Z` | 2026-07-15T19:10:51Z | documentation | Recorded Sol/Terra Step 8 blockers and remediated QA finding semantics for renewed review. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T200624Z` | 2026-07-15T20:06:24Z | documentation | Recorded final Sol/Terra OK for Step 8; Step 8 ready to commit. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T201424Z` | 2026-07-15T20:14:24Z | documentation | Synchronized Step 8 post-commit status; Step 9 is next draft-only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T201758Z` | 2026-07-15T20:17:58Z | documentation | Drafted Step 9 fixture and acceptance updates for review. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T202700Z` | 2026-07-15T20:27:00Z | documentation | Recorded Sol/Terra Step 9 blockers and remediated fixture coverage mapping. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T203708Z` | 2026-07-15T20:37:08Z | documentation | Applied second Step 9 remediation for reciprocal fixture coverage and exact negative blockers. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T204323Z` | 2026-07-15T20:43:23Z | documentation | Recorded Sol/Terra OK for Step 9 second remediation; Step 9 ready to commit. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T204640Z` | 2026-07-15T20:46:40Z | documentation | Synchronized Step 9 post-commit status; Step 10 is next draft-only. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T172844Z` | 2026-07-15T17:28:44Z | documentation | Drafted Step 3 authority/state rules after confirmed Step 1/2 remediation. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T171400Z` | 2026-07-15T17:14:00Z | documentation | Applied Step 1/2 revision pass after Sol/Terra review. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T170707Z` | 2026-07-15T17:07:07Z | documentation | Recorded Sol/Terra Step 1 review; revisions required before Step 3. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol | |
| `doc-checkpoint-20260715T164329Z` | 2026-07-15T16:43:29Z | roadmap | Updated today's 10-step Gate 1 Qualification Protocol plan. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-qualification-protocol, gate-01-pre-ocr-map-model, decision-source-profile-0.1 | |
| `doc-checkpoint-20260715T163648Z` | 2026-07-15T16:36:48Z | roadmap | Linked pre-OCR mapping model into Gate 1 roadmap, governance, and visualization metadata. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, gate-01-pre-ocr-map-model, decision-source-profile-0.1, decision-canonical-formats, decision-artifact-identity, decision-trace-anchor-model | |
| `doc-checkpoint-20260715T162639Z` | 2026-07-15T16:26:39Z | documentation | Added draft pre-OCR doc/content/art mapping model and review handoffs. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, decision-source-profile-0.1, decision-canonical-formats, decision-artifact-identity, decision-trace-anchor-model | |
| `doc-checkpoint-20260715T160428Z` | 2026-07-15T16:04:28Z | documentation | Refreshed Phase 0 stop point after Viral candidate push and Gate 1 workflow rules. | `20260715-sourcefold-phase-0-release-charter` | phase-0, gate-01-source-profile, decision-source-profile-0.1 | |
| `doc-checkpoint-20260715T003214Z` | 2026-07-15T00:32:14Z | documentation | Detailed Phase 0 Gate 1 source-profile hierarchy and prior-work evidence gates. | `20260715-sourcefold-phase-0-release-charter` | phase-0, decision-source-profile-0.1, decision-canonical-formats, decision-artifact-identity, decision-trace-anchor-model | |
| `doc-checkpoint-20260714T223803Z` | 2026-07-14T22:38:03Z | documentation | Recorded Sol/Terra OCR-first 10-step roadmap integration. | `20260715-sourcefold-phase-0-release-charter` | phase-0, decision-source-profile-0.1, decision-artifact-identity, decision-trace-anchor-model | |
| `doc-checkpoint-20260714T223721Z` | 2026-07-14T22:37:21Z | documentation | Integrated OCR-first 10-step roadmap and source-profile corrections. | `20260715-sourcefold-phase-0-release-charter` | phase-0, decision-source-profile-0.1, decision-canonical-formats, decision-artifact-identity, decision-trace-anchor-model | |
| `doc-checkpoint-20260714T220418Z` | 2026-07-14T22:04:18Z | documentation | Created Phase 0 release charter draft and review handoffs. | `20260715-sourcefold-phase-0-release-charter` | phase-0, decision-source-profile-0.1, decision-canonical-formats, decision-acceptance-authority, decision-artifact-identity, decision-trace-anchor-model, decision-waiver-policy | |
| `doc-checkpoint-20260714T215213Z` | 2026-07-14T21:52:13Z | documentation | Updated documentation before committing package-backed roadmap validator. | `20260715-sourcefold-roadmap-validator` | phase-0 | |
| `doc-checkpoint-20260714T214751Z` | 2026-07-14T21:47:51Z | documentation | Added package-backed roadmap validator. | `20260715-sourcefold-roadmap-validator` | phase-0 | |
| `doc-checkpoint-20260714T213650Z` | 2026-07-14T21:36:50Z | documentation | Added script-backed documentation checkpoint command. | `20260715-sourcefold-doc-checkpoint-command` | phase-0 | |
