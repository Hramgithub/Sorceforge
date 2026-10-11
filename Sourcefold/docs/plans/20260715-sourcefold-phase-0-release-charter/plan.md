# Phase 0 Release Charter Plan

Goal id: `20260715-sourcefold-phase-0-release-charter`

Status: active

## Objective

Define the Sourcefold Core 0.1 release boundary and contract decisions before
module implementation starts.

## Documentation Checkpoint: doc-checkpoint-20260808T163500Z

Timestamp: 2026-08-08T16:35:00Z

Context:

- `C01TEBRIDGESCOREAUTH020-G1-VIRAL-001` authorized only a future bounded
  scoring decision or remediation strategy for pages `003`-`008`.
- Sol/Terra reviewed the next scope and required a decision-only layer with no
  new scoring execution, no promotion, and conservative reference-authority
  routing.

Result:

- Generated `C01TEBRIDGESCOREDEC020-G1-VIRAL-001`.
- Consumed committed `C01TEBRIDGESCOREAUTH020-G1-VIRAL-001` report, summary,
  and manifest by exact hash from commit `9ea4f8ed`.
- Treated the input report's internal `current_head=f44cafe1` as generation-
  time metadata only.
- Routed pages `003`/`004` to `authority_upgrade_required`.
- Routed pages `005`-`008` to
  `remediation_strategy_required_comparison_only`.
- Recorded `decision_performed=true` and
  `scoring_execution_performed=false`.
- Kept fresh OCR success pages, promotable pages, and bridge-removed pages
  empty.

Boundaries:

- No new scoring execution, OCR/Tesseract, render execution, PDF parsing/text-
  layer extraction, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, fixture admission, bridge removal, production assembly,
  page `021+`, translation/proofreading, push, promotion, acceptance, or
  downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260808T165200Z

Timestamp: 2026-08-08T16:52:00Z

Context:

- `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` routed pages `003`/`004` to
  `authority_upgrade_required`.
- Sol/Terra initially blocked the follow-up because `C01TEBRIDGESCOREDEC020`
  was uncommitted; after commit `50d4abac`, renewed Sol/Terra review approved
  a report-only reference-surface authority-upgrade decision.

Result:

- Generated `C01TEP003004AUTHUP-G1-VIRAL-001`.
- Consumed committed `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` by exact report,
  summary, and manifest hashes.
- Nominated page `003` higher-authority reference surfaces from
  `P003A-G1-VIRAL-003`, `SRSA-G1-VIRAL-003-R01/R02`, and
  `P003PCA-G1-VIRAL-001`.
- Nominated page `004` higher-authority reference surfaces from
  `P004A-G1-VIRAL-004`, `SRSA-G1-VIRAL-004-R01/R02`, and
  `P004PCA-G1-VIRAL-001`.
- Preserved `PRM-G1-VIRAL-001-P004-R01` as context-only and non-peer.

Boundaries:

- No replacement reference surface, scoring execution, OCR/Tesseract,
  remediation, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, bridge removal, promotion, fixture admission, production
  assembly, page `021+`, translation/proofreading, push, acceptance, or
  downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260808T172500Z

Timestamp: 2026-08-08T17:25:00Z

Context:

- `C01TEP003004AUTHUP-G1-VIRAL-001` nominated higher-authority reference
  surfaces for pages `003`/`004` after commit `de58ee23`.
- The requested lane is limited to a report-only comparison/scoring-prep
  strategy over those nominated surfaces, with no execution or replacement
  writes.

Result:

- Generated `C01TEP003004COMPSTRAT-G1-VIRAL-001`.
- Consumed committed `C01TEP003004AUTHUP-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `de58ee23`.
- Treated the input report's internal `current_head=50d4abac` as generation-
  time metadata only.
- Defined future comparison inputs, normalization, reference assembly order,
  diagnostic metric names, thresholds, discrepancy buckets, and
  non-authorizing remediation considerations for pages `003`/`004` only.
- Preserved page `004` `PRM-G1-VIRAL-001-P004-R01` as context-only and
  non-peer.

Boundaries:

- No scoring execution, OCR/Tesseract, remediation, replacement reference
  write, accepted text mutation, semantic/page-status mutation, source/raw
  mutation, bridge removal, promotion, fixture admission, production assembly,
  page `021+`, translation/proofreading, push, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260808T184700Z

Timestamp: 2026-08-08T18:47:00Z

Context:

- `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` routed pages `005`-`008` to
  `remediation_strategy_required_comparison_only`.
- `C01TEP003004COMPSTRAT-G1-VIRAL-001` is committed as `6b336843` and remains
  an adjacent boundary for pages `003`/`004`, not an input scope for this lane.
- Sol/Terra approved a report-only comparison-remediation strategy for pages
  `005`-`008` with no execution or promotion.

Result:

- Generated `C01TEP005008REMSTRAT-G1-VIRAL-001`.
- Consumed committed `C01TEBRIDGESCOREDEC020-G1-VIRAL-001` report, summary,
  and manifest by exact hash from commit `50d4abac`.
- Recorded future remediation families, normalization, metric names,
  thresholds, hash-sealing requirements, and route constraints for pages
  `005`/`006`/`007`/`008`.
- Kept OCR-verified text-map comparison surfaces diagnostic-only, not
  acceptance truth or promotion authority.

Boundaries:

- No remediation execution, scoring execution, OCR/Tesseract, render/PDF
  parsing, replacement reference write, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, bridge removal,
  promotion, fixture admission, production assembly, page `021+`,
  translation/proofreading, push, acceptance, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260808T192500Z

Timestamp: 2026-08-08T19:25:00Z

Context:

- `C01TEP005008REMSTRAT-G1-VIRAL-001` authorized the next layer only as a
  separate bounded remediation-execution authorization or stop.
- After commit `8704802c`, Sol/Terra approved
  `C01TEP005008REMAUTH-G1-VIRAL-001` as an authorization-only packet for a
  future pages `005`-`008` comparison-only remediation execution.
- Sol required fail-closed builder/test coverage in addition to
  report/summary/manifest and documentation sync.

Result:

- Generated `C01TEP005008REMAUTH-G1-VIRAL-001`.
- Added fail-closed builder
  `scripts/build_core_0_1_text_extraction_comparison_remediation_authorization_005_008.py`
  and pytest coverage
  `tests/test_core_0_1_text_extraction_comparison_remediation_authorization_005_008.py`.
- Consumed committed `C01TEP005008REMSTRAT-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `8704802c`.
- Authorized only a future bounded comparison-only remediation execution for
  pages `005`/`006`/`007`/`008`.
- Preserved comparison surfaces as diagnostic-only, not acceptance truth or
  promotion authority.

Boundaries:

- No remediation execution, scoring execution, OCR/Tesseract, render/PDF
  parsing, replacement reference write, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, bridge removal,
  promotion, fixture admission, production assembly, page `021+`,
  translation/proofreading, push, acceptance, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260808T194000Z

Timestamp: 2026-08-08T19:40:00Z

Context:

- `C01TEP005008REMAUTH-G1-VIRAL-001` authorized only a future bounded
  comparison-only remediation execution for pages `005`-`008`.
- Sol/Terra confirmed the next execution layer must keep OCR/Tesseract false,
  stay page-scoped to `005`-`008`, and avoid fresh-success, bridge-removal,
  promotion, acceptance, production, page `021+`, push, and downstream effects.

Result:

- Generated `C01TEP005008REMEXEC-G1-VIRAL-001`.
- Added fail-closed runner
  `scripts/run_core_0_1_text_extraction_comparison_remediation_005_008.py`
  and pytest coverage
  `tests/test_core_0_1_text_extraction_comparison_remediation_execution_005_008.py`.
- Consumed committed `C01TEP005008REMAUTH-G1-VIRAL-001` report, summary, and
  manifest by exact hash from commit `4c438c4f`.
- Wrote lane-owned remediated candidate text and trace files for pages
  `005`/`006`/`007`/`008`.
- Sealed remediated candidate hashes before reference comparison and computed
  diagnostic metrics only.
- All pages remain below threshold; fresh OCR success pages, bridge-removed
  pages, and promotable pages remain empty.

Boundaries:

- No OCR/Tesseract, render/PDF parsing, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, bridge removal,
  promotion, fixture admission, production assembly, page `021+`,
  translation/proofreading, push, acceptance, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260802T223000Z

Timestamp: 2026-08-02T22:30:00Z

Context:

- `C01TEASM020-G1-VIRAL-001` showed selected static evidence for ten pages but
  excluded `001`-`008`, `014`, and `019`.
- Bogdan clarified those pages were not content failures and approved a bounded
  eligibility/parked-pages bridge.

Result:

- Generated `C01TEBRIDGE020-G1-VIRAL-001`.
- Hash-pinned page-complete acceptance reports for `001`-`008`, `014`, and
  `019`.
- Classified `001`-`008` as `accepted_page_complete_bridge`.
- Classified `014` and `019` as
  `parked_overview_but_page_complete_accepted_bridge`.
- Created selector replay v4 with static evidence coverage for all pages
  `001`-`020`.
- Recorded `all_pages_static_evidence_covered=true`,
  `all_pages_first_pass_success=false`, and `production_ready=false`.

Boundaries:

- No OCR execution, render execution, PDF parsing/text-layer extraction,
  reference-token insertion, accepted/semantic/page-status mutation, source/raw
  mutation, runtime selector integration, runtime execution, production
  assembly, clean production output folder, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T215800Z

Timestamp: 2026-08-02T21:58:00Z

Context:

- `C01TEMF012016020-G1-VIRAL-001` selected static method entries for `012`,
  `016`, and `020`, creating selector replay v3.
- Selector replay v3 still left pages `001`-`008` not-run/ineligible and
  pages `014`/`019` parked.
- Bogdan approved the next bounded assembly prep/contract step.

Result:

- Generated `C01TEASM020-G1-VIRAL-001`, a manifest-only, hash-reference-only
  assembly-readiness dry-run.
- Wrote selected-page manifest entries for
  `009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, and `020`.
- Recorded excluded/blocking pages `001`-`008` as not-run/ineligible and
  `014`/`019` as parked.
- Proved no failed, weak, parked, or superseded candidates are included in the
  selected manifest.
- Recorded `production_ready=false` and `all_pages_first_pass_success=false`.

Boundaries:

- No copied candidate text, inline candidate text, OCR execution, render
  execution, PDF parsing/text-layer extraction, reference-token insertion,
  accepted/semantic/page-status mutation, source/raw mutation, runtime selector
  integration, runtime execution, production assembly, clean production output
  folder, page `001`-`020` runtime loop, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T205700Z

Timestamp: 2026-08-02T20:57:00Z

Context:

- `C01TESEL020-G1-VIRAL-001` left pages `012`, `016`, `017`, `018`, and
  `020` unresolved.
- `C01TEP013DISC-G1-VIRAL-001` proved the cold-start discovery pattern for P013
  over sealed diagnostic evidence.
- Bogdan approved the next bounded unresolved-pages discovery layer.

Result:

- Generated `C01TEUNRES020-G1-VIRAL-001`.
- Opened fresh static method entries for pages `017` and `018`.
- Kept pages `012`, `016`, and `020` unresolved because their best existing
  evidence remains below threshold.
- Created selector replay v2 with selected pages
  `009`, `010`, `011`, `013`, `015`, `017`, and `018`.
- Recorded `production_ready=false` and `all_pages_first_pass_success=false`.

Boundaries:

- No OCR execution, render execution, PDF parsing/text-layer extraction,
  reference-token insertion, candidate text copy, accepted/semantic/page-status
  mutation, source/raw mutation, runtime selector integration, production
  assembly, clean production output folder, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T203600Z

Timestamp: 2026-08-02T20:36:00Z

Context:

- The static `001`-`020` selector replay showed that P013 is selected only when
  the prior MRS registry entry is available.
- Bogdan requested automating the search/selection layer that would discover
  the P013 method without using that MRS entry as input.

Result:

- Generated `C01TEP013DISC-G1-VIRAL-001`, a bounded P013 cold-start method
  discovery dry-run over existing hash-pinned diagnostic lanes.
- Ranked `5` diagnostic lanes and `18` candidate records.
- Selected `p013_sac_d_noise_then_declared_seam_fracture` as
  `C01TEP013DISC-G1-VIRAL-001-P013`.
- Recorded the tied `p013_sac_e_paragraph_join_d` as an unselected equivalent
  and used the `line_join` tie-break before candidate-id fallback.
- Created a P013-only selector dry-run from the fresh discovered entry.

Boundaries:

- No prior P013 MRS registry input, OCR execution, render execution, PDF
  parsing/text-layer extraction, reference-token insertion, accepted/semantic/
  page-status/source/raw mutation, runtime selector integration, production
  assembly, clean production output folder, page `001`-`020` runtime loop, page
  `021+`, translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T160400Z

Timestamp: 2026-08-02T16:04:00Z

Context:

- P013 MRS selected `C01TEP013MRS-G1-VIRAL-001-P013`, but explicitly did not
  create a page `001`-`020` selector loop or production output.
- Bogdan approved the next bounded step after the selector replay plan.

Result:

- Generated `C01TESEL020-G1-VIRAL-001`, a static `001`-`020` selector replay
  over sealed prior artifacts.
- Selected pages `009`, `010`, `011`, and `015` from frozen baseline hashes.
- Selected page `013` from `C01TEP013MRS-G1-VIRAL-001-P013`.
- Kept `012`, `016`, `017`, `018`, and `020` unresolved.
- Kept `014` and `019` parked.
- Recorded `production_ready=false` and `all_pages_first_pass_success=false`.

Boundaries:

- No OCR execution, render execution, PDF parsing/text-layer extraction,
  reference-token insertion, candidate text copy, accepted/semantic/page-status
  mutation, source/raw mutation, runtime selector integration, production
  assembly, clean production output folder, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T153700Z

Timestamp: 2026-08-02T15:37:00Z

Context:

- P013 SAC crossed the diagnostic threshold with
  `p013_sac_d_noise_then_declared_seam_fracture` and tied
  `p013_sac_e_paragraph_join_d`.
- Sol/Terra allowed only a P013 method-registry candidate decision record, not
  enabled selector integration or production output.

Result:

- Generated `C01TEP013MRS-G1-VIRAL-001`.
- Selected `C01TEP013MRS-G1-VIRAL-001-P013` for
  `p013_sac_d_noise_then_declared_seam_fracture`.
- Recorded `p013_sac_e_paragraph_join_d` as an unselected separator-only
  equivalent with the same normalized hash and metrics.
- Created a static P013 selector dry-run only.

Boundaries:

- No selector rule, selector enablement, runtime selector integration,
  production assembly, clean production output folder, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, page `001`-`020` runtime
  loop, page `021+`, translation/proofreading, push, promotion, acceptance, or
  downstream execution is created.

## Scope

In scope:

- 0.1 release charter and non-goals;
- first source profile decision record;
- canonical artifact/evidence format decisions;
- acceptance vocabulary and authority;
- artifact identity, lineage, trace anchors, supersession, and rerun rules;
- waiver policy;
- fixture strategy and release acceptance matrix;
- Sol architecture review and Terra independent critique handoffs.

Out of scope:

- implementation of `reconstruct`, `translate`, `proofread`, `press`, or
  `bridge`;
- real book processing;
- Translator migration or compatibility;
- broad OCR/PDF claims;
- UI or hosted workflow.

## Role Ownership

| Role | Model | Effort | Responsibility |
|---|---|---|---|
| Orchestrator | `gpt-5.6-terra` | medium | Owns canonical context, plan/status, integration, user-facing decisions. |
| Sol architect | `gpt-5.6-sol` | high | Reviews architecture, dependencies, source profile, lineage/acceptance model. |
| Terra critic | `gpt-5.6-terra` | high | Independently critiques scope, premature-implementation risks, missing gates. |

## Task Packets

| Packet | Owner | Status | Handoff |
|---|---|---|---|
| Draft Phase 0 charter documents | Orchestrator | active | this plan/context |
| Architecture review | Sol | completed | `handoffs/sol-architecture-20260715.md` |
| Independent critique | Terra | completed | `handoffs/terra-critique-20260715.md` |
| OCR-first 10-step roadmap | Sol | completed | `handoffs/sol-ocr-first-10-step-roadmap-20260715.md` |
| OCR-first 10-step critique | Terra | completed | `handoffs/terra-ocr-first-10-step-critique-20260715.md` |
| Prior-work evidence analysis | Sol | completed | `handoffs/sol-prior-work-evidence-analysis-20260715.md` |
| Phase/Gate/Component architecture | Sol | completed | `handoffs/sol-phase-gate-component-architecture-20260715.md` |
| Phase/Gate/Component critique | Terra | completed | `handoffs/terra-phase-gate-component-critique-20260715.md` |
| Pre-OCR map taxonomy analysis | Sol | completed | `handoffs/sol-doc-content-art-map-analysis-20260715.md` |
| Pre-OCR map architecture | Sol | completed | `handoffs/sol-doc-content-art-map-architecture-20260715.md` |
| Pre-OCR map critique | Terra | completed | `handoffs/terra-doc-content-art-map-critique-20260715.md` |
| Prior-books map evidence scout | Sol | completed | `handoffs/sol-prior-books-map-evidence-20260715.md` |
| Step 1 Qualification Protocol architecture review | Sol | completed | `handoffs/sol-step-1-qualification-protocol-review-20260715.md` |
| Step 1 Qualification Protocol independent critique | Terra | completed | `handoffs/terra-step-1-qualification-protocol-critique-20260715.md` |
| Step 1/2 revision approval review | Sol | blocker found | `handoffs/sol-step-1-2-revision-approval-20260715.md` |
| Step 1/2 revision approval critique | Terra | ok with notes | `handoffs/terra-step-1-2-revision-approval-20260715.md` |
| Step 3 authority/state review | Sol | blocker found; remediated locally | `handoffs/sol-step-3-authority-review-20260715.md` |
| Step 3 authority/state critique | Terra | ok with notes | `handoffs/terra-step-3-authority-critique-20260715.md` |
| Step 4 candidate intake review | Sol | blocker found; remediated locally | `handoffs/sol-step-4-intake-review-20260715.md` |
| Step 4 candidate intake critique | Terra | ok to commit after matching Sol approval | `handoffs/terra-step-4-intake-critique-20260715.md` |
| Step 4 remediation confirmation | Sol | ok to commit and proceed to Step 5 draft-only | `handoffs/sol-step-4-remediation-confirmation-20260715.md` |
| Step 4 remediation confirmation critique | Terra | ok to commit and proceed to Step 5 draft-only | `handoffs/terra-step-4-remediation-confirmation-20260715.md` |
| Step 5 render benchmark review | Sol | blocker found; remediated locally | `handoffs/sol-step-5-render-review-20260715.md` |
| Step 5 render benchmark critique | Terra | ok before Sol second blocker | `handoffs/terra-step-5-render-critique-20260715.md` |
| Step 5 remediation confirmation | Sol | blocker found; second remediation applied locally | `handoffs/sol-step-5-remediation-confirmation-20260715.md` |
| Step 5 remediation confirmation critique | Terra | blocker found; second remediation applied locally | `handoffs/terra-step-5-remediation-confirmation-20260715.md` |
| Step 5 final confirmation | Sol | ok to commit and proceed to Step 6 draft-only | `handoffs/sol-step-5-final-confirmation-20260715.md` |
| Step 5 final confirmation critique | Terra | ok to commit and proceed to Step 6 draft-only | `handoffs/terra-step-5-final-confirmation-20260715.md` |
| Step 6 pre-OCR map review | Sol | blocker found; remediated locally | `handoffs/sol-step-6-map-review-20260715.md` |
| Step 6 pre-OCR map critique | Terra | blocker found; remediated locally | `handoffs/terra-step-6-map-critique-20260715.md` |
| Step 6 remediation confirmation | Sol | blocker found; second remediation applied locally | `handoffs/sol-step-6-remediation-confirmation-20260715.md` |
| Step 6 remediation confirmation critique | Terra | ok before Sol second blocker | `handoffs/terra-step-6-remediation-confirmation-20260715.md` |
| Step 6 final confirmation | Sol | ok to commit and proceed to Step 7 draft-only | `handoffs/sol-step-6-final-confirmation-20260715.md` |
| Step 6 final confirmation critique | Terra | ok to commit and proceed to Step 7 draft-only | `handoffs/terra-step-6-final-confirmation-20260715.md` |
| Step 7 OCR benchmark review | Sol | blockers found; remediated locally | `handoffs/sol-step-7-ocr-review-20260715.md` |
| Step 7 OCR benchmark critique | Terra | ok before Sol blockers | `handoffs/terra-step-7-ocr-critique-20260715.md` |
| Step 7 remediation confirmation | Sol | ok to commit | `handoffs/sol-step-7-remediation-confirmation-20260715.md` |
| Step 7 remediation confirmation critique | Terra | ok to commit | `handoffs/terra-step-7-remediation-confirmation-20260715.md` |
| Step 8 QA findings review | Sol | blockers found; remediated locally | `handoffs/sol-step-8-qa-review-20260715.md` |
| Step 8 QA findings critique | Terra | blockers found; remediated locally | `handoffs/terra-step-8-qa-critique-20260715.md` |
| Step 8 remediation confirmation | Sol | semantic remediation ok; context drift blocker found | `handoffs/sol-step-8-remediation-confirmation-20260715.md` |
| Step 8 remediation confirmation critique | Terra | ok before label drift blocker | `handoffs/terra-step-8-remediation-confirmation-20260715.md` |
| Step 8 final confirmation | Sol | ok before Terra label blocker | `handoffs/sol-step-8-final-confirmation-20260715.md` |
| Step 8 final confirmation critique | Terra | label blocker found; remediated locally | `handoffs/terra-step-8-final-confirmation-20260715.md` |
| Step 8 label final confirmation | Sol | ok to commit | `handoffs/sol-step-8-label-final-confirmation-20260715.md` |
| Step 8 label final confirmation critique | Terra | ok to commit | `handoffs/terra-step-8-label-final-confirmation-20260715.md` |
| Step 9 fixture acceptance review | Sol | blockers found; remediated locally | `handoffs/sol-step-9-fixture-acceptance-review-20260715.md` |
| Step 9 fixture acceptance critique | Terra | blocker found; remediated locally | `handoffs/terra-step-9-fixture-acceptance-critique-20260715.md` |
| Step 9 first remediation confirmation | Sol | remaining blockers found; remediated locally | `handoffs/sol-step-9-remediation-confirmation-20260715.md` |
| Step 9 first remediation confirmation critique | Terra | ok before Sol blockers | `handoffs/terra-step-9-remediation-confirmation-20260715.md` |
| Step 9 second remediation confirmation | Sol | ok to commit | `handoffs/sol-step-9-second-remediation-confirmation-20260715.md` |
| Step 9 second remediation confirmation critique | Terra | ok to commit | `handoffs/terra-step-9-second-remediation-confirmation-20260715.md` |

## Documentation Checkpoint: doc-checkpoint-20260803T213200Z

Timestamp: 2026-08-03T21:32:00Z

Context:

- After `C01TEBRIDGEREM020-G1-VIRAL-001` kept page `002` blocked as
  `needs_source_asset_recovery`, and after `C01TEBRIDGESCOREAUD020-G1-VIRAL-001`
  stabilized pages `003`-`008` as comparison-only, the next bounded split was
  a report-only P002 source asset recovery audit.

Result:

- Generated `C01TEP002ASSETREC-G1-VIRAL-001`.
- Page `002` is classified as
  `recoverable_from_pinned_page_image_and_source_reconstruction_artifacts`.
- The strongest P002 source-acceptance chain is retained only as recoverability
  evidence because the completion artifact carries
  `stale_generator_hash_in_completion_artifact`.
- `bridge_blocker_cleared=false`; the next allowed action is a separate bounded
  P002 source-asset materialization authorization.

Boundaries:

- No `review_assets` materialization, OCR/Tesseract, render/PDF parsing,
  accepted text mutation, semantic/page-status mutation, source/raw mutation,
  fixture admission, production assembly, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260803T221800Z

Timestamp: 2026-08-03T22:18:00Z

Context:

- After `C01TEP002ASSETREC-G1-VIRAL-001` classified page `002` as recoverable
  while leaving `bridge_blocker_cleared=false`, Bogdan authorized broader
  orchestration, delegation, expanded planning, and commits.
- The next bounded split is a future-lane-only materialization authorization,
  not source asset materialization itself.

Result:

- Generated `C01TEP002ASSETMATAUTH-G1-VIRAL-001`.
- The lane consumes only committed `C01TEP002ASSETREC-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- It authorizes only a future bounded page `002` source asset materialization
  lane from the pinned recovery audit.
- `stale_generator_hash_in_completion_artifact` remains an authority risk.
- `bridge_blocker_cleared=false`; materialization, blocker removal, and any
  source/page acceptance require later bounded lanes.

Boundaries:

- Authorization-only. No `review_assets` materialization, OCR/Tesseract,
  render execution, PDF parsing/text-layer extraction, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, fixture admission,
  production assembly, bridge blocker clearing, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260803T224000Z

Timestamp: 2026-08-03T22:40:00Z

Context:

- `C01TEP002ASSETMATAUTH-G1-VIRAL-001` authorized only a future bounded page
  `002` source asset materialization lane from the pinned recovery audit.
- Sol/Terra constrained the lane to a new lane-owned output root and blocked
  writes to historical `page_complete_review_p002_G1_VIRAL_001/review_assets/`.

Result:

- Generated `C01TEP002ASSETMAT-G1-VIRAL-001`.
- Copied pinned `page_002.png` and two corrected crop refs into the lane-owned
  output root.
- Materialized asset hashes match the pinned source hashes.
- The materialized surface is recoverability evidence only.
- Output hashes are report
  `82D51C020E5571C7FDB86040CC0E3469EC0CE26A1C4A49286B0135E13A39315F`, summary
  `3962117A4EE8737788B0FE60ADB57C4BB9E5338ABDE03835E1B56BEBD732B038`, and
  manifest
  `8F32E3FBEB3B671857B65FCD769627B8545F471B4E5F8DDF062D4FDDFD62EFE6`.
- `stale_generator_hash_in_completion_artifact` remains an authority risk.
- `bridge_blocker_cleared=false`; a separate materialized-surface review is
  required before blocker clearance or source/page acceptance.

Boundaries:

- No historical `review_assets` write, OCR/Tesseract, render execution, PDF
  parsing/text-layer extraction, accepted text mutation, semantic/page-status
  mutation, source/raw mutation, fixture admission, production assembly, bridge
  blocker clearing, page `021+`, translation/proofreading, push, promotion,
  acceptance, or downstream execution is created.

## Core 0.1 P002 Materialized Surface Review

Result:

- Generated `C01TEP002MATREVIEW-G1-VIRAL-001`.
- Consumed committed `C01TEP002ASSETMAT-G1-VIRAL-001` report/summary/manifest
  by exact hash.
- Verified the lane-owned `page_002.png` and two corrected crop refs by
  SHA-256.
- Cleared only the page `002` asset-recovery blocker:
  `asset_recovery_blocker_cleared=true` and `bridge_blocker_cleared=true`.
- Preserved `fresh_ocr_success=false`; the next blocker is
  `needs_fresh_ocr_route_authorization`.
- Output hashes are report
  `0B047CF8B9FA2E7B77D3CB73C296F11070198F4C2EEB4B1585882EE91DFFFA1F`, summary
  `8E293FB620CE6503D341FC4EB5F882FF6A98F807C04FEDD51FFE170E8E939AD7`, and
  manifest
  `CCBFD30FCCCAE5C0659C08817F1524CF3A3740FC87600D6956D6F20555AE6D7B`.

Boundaries:

- No OCR/Tesseract, render execution, PDF parsing/text-layer extraction,
  accepted text mutation, semantic/page-status mutation, source/raw mutation,
  fixture admission, production assembly, fresh OCR success, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream execution
  is created.

## Core 0.1 P002 Fresh OCR Route Authorization

Result:

- Generated `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`.
- Consumed committed `C01TEP002MATREVIEW-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Authorized a future bounded fresh OCR candidate route for page `002` from the
  lane-owned full-page image only.
- Kept the two corrected crop refs as comparison-only surfaces, not OCR input.
- `fresh_ocr_route_authorized=true`, but `ocr_execution_performed=false`,
  `fresh_ocr_success=false`, and `bridge_blocker_cleared=false`.
- Output hashes are report
  `6EE1925A65367833898D0E17150687E341F411C1B7D6EDDD0219671593F6AC68`, summary
  `096069AC2AE284A852448D0DE3B8347F9369FF89BC851850742D646D1583B741`, and
  manifest
  `C0AA3147BB065FB8F0EA4F88A5D86E84F0C5B06CB9F8EAAC41DD4417AD2C444D`.

Boundaries:

- No OCR/Tesseract, candidate text, render execution, PDF parsing/text-layer
  extraction, accepted text mutation, semantic/page-status mutation, source/raw
  mutation, fixture admission, production assembly, fresh OCR success, bridge
  removal, page `021+`, translation/proofreading, push, promotion, acceptance,
  or downstream execution is created.

## Core 0.1 P002 Fresh OCR Candidate

Result:

- Generated `C01TEP002FRESHOCR-G1-VIRAL-001`.
- Consumed committed `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Ran Tesseract on the lane-owned page `002` full-page image only, for PSM `4`
  and PSM `6`.
- Corrected crop refs were not used as OCR input.
- Candidate hashes were sealed; no reference-scoring surface was loaded.
- `reference_scoring_performed=false`, `fresh_ocr_success=false`, and
  `bridge_blocker_cleared=false`.
- Output hashes are report
  `5686F161296BD696E8F97B00DB9560F2374E6FAC74B4DA223490FF2ECFC473D2`, summary
  `4AE2AE00372FADB5E523982A438ABDDAD69F5CB6EA8EB5F706A2D87FA399A3A5`, and
  manifest
  `FEE45C27C759FCCBD67DF2CC44B8F65D4249644FCC3DA9A289612FBDC721B155`.

Boundaries:

- No reference scoring, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, fixture admission, production assembly, fresh OCR
  success, bridge removal, page `021+`, translation/proofreading, push,
  promotion, acceptance, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260804T001900Z

Timestamp: 2026-08-04T00:19:00Z

Context:

- P002 fresh OCR candidate execution produced PSM `4` and PSM `6` text from the
  lane-owned full-page image.
- The next bounded step is a scoring/reference audit, not an acceptance or
  bridge-removal decision.

Result:

- Generated `C01TEP002FRESHSCOREAUD-G1-VIRAL-001`.
- Consumed committed `C01TEP002FRESHOCR-G1-VIRAL-001`
  report/summary/manifest and both candidate texts by exact hash.
- Audited pinned page `002` comparison surfaces only.
- Performed diagnostic comparison metrics only.
- All reference surfaces are comparison-only, not independent acceptance truth.
- `fresh_ocr_success=false`, `bridge_blocker_cleared=false`, and
  `promotable_pages=[]`.
- Output hashes are report
  `0834F4A864105F6D15D243198F743158C9D91ECDAF5AAEA4A4281913DD481740`, summary
  `3E42702616B3C4F1267559290F9D4BE303DC1A5CDC342C10ED11F8E32C396D7E`, and
  manifest
  `BF9B57598F7FAC66DEDFAF25D6CC1692C278AB9CA185BAC9DE06FD0AE4839FFB`.

Boundaries:

- No OCR/Tesseract, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, fixture admission, production assembly, fresh OCR
  success, bridge removal, page `021+`, translation/proofreading, push,
  promotion, acceptance, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260804T005000Z

Timestamp: 2026-08-04T00:50:00Z

Result:

- Generated `C01TEP002FRESHPASS-G1-VIRAL-001`.
- Consumed committed `C01TEP002FRESHREM-G1-VIRAL-001` report/summary/manifest
  and remediated candidate by exact hash.
- Recorded page `002` as fresh OCR success for the bounded first-pass
  remediation path.
- Recorded bridge removal for page `002` only.
- Output hashes are report
  `167A900F18B10B8E4507F7FE7461946526680A5EC8A68C4605445460BBCA4609`, summary
  `C0BE3C169B19FDD2E179236C7632E9B870E59412FF69E8139B0FB41F64DD406F`, and
  manifest
  `E102FEED6864F17F89B0EE14A9A23FC4B611282A6D1FEC90EC65DCFC6BE424D7`.

Boundaries:

- No acceptance, production assembly, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, fixture admission, page
  `021+`, translation/proofreading, push, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260804T002800Z

Timestamp: 2026-08-04T00:28:00Z

Context:

- P002 scoring decision selected `psm4` but required remediation before fresh
  OCR success or bridge removal.
- The next bounded step is authorization for remediation execution.

Result:

- Generated `C01TEP002FRESHREMAUTH-G1-VIRAL-001`.
- Consumed committed `C01TEP002FRESHDECIDE-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Authorized a future bounded page `002` remediation execution from best
  candidate `psm4` and visual-verified discrepancy evidence.
- Did not execute remediation.
- Output hashes are report
  `42ABC318A2B283F27CDCA13AE14FAF26C1256F71BA1B0BE263E4448E00BD49FF`, summary
  `17F1B59A17E229965712CB5B21E64EFC9703F7EBDB5768E17475066492F76A05`, and
  manifest
  `F9E54880261ACC456F5FA9116F6A15743E2741FAEBC5481CFD2396DD7CF131A8`.

Boundaries:

- No OCR/Tesseract, remediation execution, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, fixture admission,
  production assembly, fresh OCR success, bridge removal, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Documentation Checkpoint: doc-checkpoint-20260804T004500Z

Timestamp: 2026-08-04T00:45:00Z

Context:

- P002 remediation authorization allowed a future bounded remediation execution
  from best candidate `psm4`.

Result:

- Generated `C01TEP002FRESHREM-G1-VIRAL-001`.
- Consumed committed `C01TEP002FRESHREMAUTH-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Consumed PSM `4` candidate text and human-verified P002 assisted-draft
  verification report by exact hash.
- Created one lane-owned remediated candidate text.
- Applied `insert_missing_header` and `replace_visual_verified_token`.
- Diagnostic metrics after remediation are similarity `1.0` and token recall
  `1.0`; threshold met after remediation is `true`.
- Fresh OCR success and bridge removal remain false until a separate
  pass-decision lane.
- Output hashes are report
  `F4A650F37B28B89787DF81D95B7526BFBDD513DFC91175895644C9E2C67C5551`, summary
  `D4A84A7FB795B87F4D21E5753D30B9CEB9F1949B1B3A81F0F9A545354F216F52`,
  manifest
  `9BFA3E92BBD3953A5B2290D0CB31AFC89780ED963726F63DA08B8AE09668379F`, and
  remediated candidate
  `E8D84506A1069EFD417028A65132F0E378C90010E421B645E593215152EA9B7C`.

Boundaries:

- No OCR/Tesseract, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, fixture admission, production assembly, fresh OCR
  success, bridge removal, page `021+`, translation/proofreading, push,
  promotion, acceptance, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260804T002400Z

Timestamp: 2026-08-04T00:24:00Z

Context:

- P002 scoring/reference audit showed comparison surfaces exist but cannot be
  treated as independent acceptance truth.
- The next bounded step is a scoring/remediation-routing decision.

Result:

- Generated `C01TEP002FRESHDECIDE-G1-VIRAL-001`.
- Consumed committed `C01TEP002FRESHSCOREAUD-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Consumed PSM `4` and PSM `6` candidate texts by exact hash.
- Consumed human-verified P002 assisted-draft verification surfaces by exact
  hash as comparison evidence only.
- Selected `psm4` as best candidate at similarity `0.996182` and token recall
  `0.985507`.
- Strict threshold `0.997` is not met, so the decision is
  `remediation_required_before_fresh_ocr_success`.
- Output hashes are report
  `C745B2EBF02001D0F4ACD4AD836DFC534C59B799911A2FAB96785CBB3F50471B`, summary
  `7B72F72E6480BDDDD6FF61947F2425F8BB0E5DF8446AF1EEA56F3EDF02CD3D50`, and
  manifest
  `0283F681EE24683AA6BBC6EA1F2818F7DC9680E6DCB8D56B1D91FCE476260713`.

Boundaries:

- No OCR/Tesseract, accepted text mutation, semantic/page-status mutation,
  source/raw mutation, fixture admission, production assembly, fresh OCR
  success, bridge removal, page `021+`, translation/proofreading, push,
  promotion, acceptance, or downstream execution is created.

## Core 0.1 Bridge Page Scoring Authorization 003-008

Result:

- Generated `C01TEBRIDGESCOREAUTH020-G1-VIRAL-001`.
- Consumed committed `C01TEBRIDGESCOREAUD020-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Recorded that existing diagnostic audit metrics do not authorize fresh OCR
  success or promotion.
- Authorized only a future bounded scoring decision or remediation strategy for
  pages `003-008`.
- Output hashes are report
  `A77528B265D52AEF0ED56C35E2F559AAACB937CBF190B27CA0F17684A13AB09A`, summary
  `3FAACCA70F855C82DD606BB6B433688071841F734C6B8997DF0E17AA92FE3232`, and
  manifest
  `E4CAFF5D01B987BC1CEC5EF04C87FA24A2764090BB036FC5C2FCBB4FCEE94513`.

Boundaries:

- No scoring, OCR/Tesseract, render execution, PDF parsing/text-layer
  extraction, accepted text mutation, semantic/page-status mutation, source/raw
  mutation, fixture admission, production assembly, fresh OCR success, page
  `021+`, translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Core 0.1 P014/P019 Route Decision

Result:

- Generated `C01TEP014019ROUTEDEC-G1-VIRAL-001`.
- Consumed committed bridge audit/remediation artifacts and page-complete
  `014`/`019` surfaces by exact hash.
- Confirmed existing text-evidence smoke outputs for `014`/`019` are
  non-promotable and cannot clear bridge lineage or count as fresh OCR success.
- Authorized only a future separate full-page OCR route for `014`/`019`; text
  evidence crops may not be used as OCR input.
- Output hashes are report
  `BC4D6569FE50C59374C0A1D54B3A23611D267D08B6759F8B5D726FEC8D989458`, summary
  `5AF33BFEB0E3750597AF4A400849128CF2D429C2AD2BDA334D576F2D83DEF18E`, and
  manifest
  `77C243CD1FB4C1AB70EE7902BA005216477DFD6B5FDC6C2B7FBADB332F2E42C9`.

Boundaries:

- No OCR/Tesseract, scoring, render execution, PDF parsing/text-layer
  extraction, accepted text mutation, semantic/page-status mutation, source/raw
  mutation, fixture admission, production assembly, fresh OCR success, page
  `021+`, translation/proofreading, push, promotion, acceptance, or downstream
  execution is created.

## Core 0.1 P014/P019 Full-Page OCR

Result:

- Generated `C01TEP014019FPOCR-G1-VIRAL-001`.
- Consumed committed `C01TEP014019ROUTEDEC-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Ran Tesseract only on full-page-region input surfaces for pages `014` and
  `019`; text-evidence crops were not used as OCR input.
- Sealed candidate hashes before loading comparison text maps.
- Created candidate text and OCR metadata for PSM `4` and PSM `6` on pages
  `014` and `019`.
- Selected diagnostics remain non-promotable: page `014` PSM `4` similarity
  `0.157291` / token recall `0.885572`; page `019` PSM `4` similarity
  `0.072989` / token recall `0.9225`.
- Fresh OCR success pages and bridge removed pages remain empty.
- Output hashes are report
  `0238FFA8B0D91FAE6047E426AA59BA606668EAB589B14FD112AE5615A4877F32`, summary
  `4250181B5F35A1A8809A965190F0831B7F58FCAC73C3974A9BED18BF216B0E19`, and
  manifest
  `EB1DA1D11FAF85315363F7EE8213F34F381603719898A9EB2E353D6F36D4175B`.

Boundaries:

- No accepted text mutation, semantic/page-status mutation, source/raw mutation,
  fixture admission, production assembly, fresh OCR success, bridge removal,
  page `021+`, translation/proofreading, push, promotion, acceptance, or
  downstream execution is created.

## Deliverables

| Artifact | Purpose | Status |
|---|---|---|
| `release_charter.md` | 0.1 boundary, source profile options, non-goals, exit gate. | draft |
| `acceptance_vocabulary.md` | Meaning of accepted/passed/waived/conformant/released. | draft |
| `artifact_lineage_model.md` | Artifact identity, DAG, anchors, hashes, supersession. | draft |
| `fixture_strategy.md` | Positive/negative fixture plan for Phase 1. | Step 9 confirmed and committed |
| `release_acceptance_matrix.md` | Mapping of release criteria to evidence. | draft |
| `core_0_1_acceptance_matrix.md` | Executable OCR-first Core 0.1 acceptance skeleton. | Step 9 confirmed and committed |
| `user_ocr_profile_notes.md` | Captured user corrections about PDF/OCR-first profile. | draft |
| `ocr_first_10_step_roadmap.md` | Expanded OCR-first roadmap from Phase 0 to Core 0.1 RC. | draft |
| `phase_gate_component_hierarchy.md` | Phase/gate/component/subcomponent/parameter hierarchy for Gate 1. | draft governed model |
| `prior_work_evidence_index.md` | Prior scenario/log evidence index for profile parameter decisions. | draft evidence index |
| `gate_01_qualification_protocol.md` | Protocol shell for qualifying Gate 1 render/OCR/taxonomy parameters before `Вирал` processing. | accepted_protocol at `5ee1760f` / blob `4d494e83` |
| `bounded_trial_authorizations.md` | Action-specific authorization ledger for candidate-derived trials. | Current through `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-CANDIDATE-001`; `C01TEP002FRESHOCR-G1-VIRAL-001` creates candidate-only page 002 OCR outputs without reference scoring, fresh success, bridge removal, promotion, acceptance, or production |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/render_output_manifest.md` | First bounded render trial output manifest. | `valid_for_review`; render evidence only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/visual_sanity_report.md` | First bounded visual sanity/page inventory report. | `valid_for_review`; non-accepting inventory only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_inventory_report.md` | First bounded page-level inventory report. | `valid_for_review`; non-accepting page inventory only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_model_report.md` | First bounded page-level map/model report. | `valid_for_review`; non-accepting planning evidence only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/provisional_region_map_report.md` | First bounded provisional region map report. | `valid_for_review`; non-accepting annotation evidence only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_completeness_triage_G1_VIRAL_001/page_completeness_triage_packet.md` | Human-facing triage packet for selected pages 1-20 after page 004 source acceptance. | `ready_for_bogdan_decision`; triage/status only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p002_G1_VIRAL_001/page_map_readiness_packet.md` | First human-facing page-map readiness packet from the reusable pipeline, using page 002 as the pilot profile. | `ready_for_page_complete_review_packet`; readiness only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p002_G1_VIRAL_001/page_complete_review_packet.md` | Separate page-complete review packet for page 002 using `PMRP-G1-VIRAL-P002-001` as readiness input. | `ready_for_bogdan_page_complete_decision`; review packet only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p002_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 002 after Bogdan's `page 002 complete ok` decision. | `page_002_complete_accepted`; page 002 only, no whole Gate 1 or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p003_G1_VIRAL_001/page_map_readiness_packet.md` | Second human-facing page-map readiness packet from the reusable pipeline, using existing `P003A-G1-VIRAL-003` evidence. | `ready_for_page_complete_review_packet`; readiness only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/page_complete_review_packet.md` | Separate page-complete review packet for page 003 using `PMRP-G1-VIRAL-P003-001` as readiness input. | `ready_for_bogdan_page_complete_decision`; review packet only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p003_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 003 after Bogdan's `page 003 complete ok` decision. | `page_003_complete_accepted`; page 003 only, no whole Gate 1 or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/page_004_context_decision_packet.md` | Separate page 004 context-only decision packet for the full tilted inset `PRM-G1-VIRAL-001-P004-R01`, with review assets. | `ready_for_bogdan_page_004_context_only_decision`; decision packet only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_only_confirmation_G1_VIRAL_001/page_004_context_only_confirmation_record.md` | Explicit page 004 context-only confirmation record for the full tilted inset `PRM-G1-VIRAL-001-P004-R01` after Bogdan's `page 004 context-only ok` decision. | `page_004_context_only_confirmed`; context region only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/structure_display_normalization_G1_VIRAL_001/structure_display_normalization_report.json` | Display-only normalization package for human-facing `Draft structure/semantics` labels, plus normalized copies of prior affected packets. | `human_facing_structure_display_normalized`; no predecessor evidence mutation or acceptance changes |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p004_G1_VIRAL_001/page_map_readiness_packet.md` | Third human-facing page-map readiness packet from the reusable pipeline, using page 004 source acceptance plus context-only confirmation. | `ready_for_page_complete_review_packet`; readiness only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p004_G1_VIRAL_001/page_complete_review_packet.md` | Separate page-complete review packet for page 004 using `PMRP-G1-VIRAL-P004-001` as readiness input. | `ready_for_bogdan_page_complete_decision`; review packet only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p004_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 004 after Bogdan's `page 004 complete ok` decision. | `page_004_complete_accepted`; page 004 only, no whole Gate 1 or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p005_G1_VIRAL_001/page_map_readiness_packet.md` | Fourth human-facing page-map readiness packet from the reusable pipeline, using existing page 005 human/QA/fixture evidence. | `ready_for_page_complete_review_packet`; readiness only, no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_001/page_complete_review_packet.md` | Superseded page-complete review packet for page 005 using `PMRP-G1-VIRAL-P005-001` as readiness input. | `blocked`; visual proof crops are smaller than declared readiness blocks; no page-complete acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_002/page_complete_review_packet.md` | Superseded page-complete review packet for page 005 with full declared `box_px` crops generated from `page_005.png`. | `superseded_by_readable_crop_packet`; size proof passed, but human-readable crop framing was insufficient |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_003/page_complete_review_packet.md` | Readable superseding page-complete review packet for page 005 with title-only, left-column, and right-column crops plus OCR/verified text map. | consumed by `PCRP-G1-VIRAL-P005-004`; review packet only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_004/page_complete_review_packet.md` | Semantic compatibility refresh for page 005 with canonical semantic JSON/Markdown, validated projection, and inventory reconciliation. | consumed by `P005PCA-G1-VIRAL-001`; review packet only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p005_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 005 after Bogdan's `page 005 complete ok` decision. | `page_005_complete_accepted`; page 005 only, no whole Gate 1 or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_002/page_complete_review_packet.md` | Superseding page-complete review packet for page 006 after semantic-map hardening, with validated semantic JSON/Markdown projection, corrected heading/quote units, and linked Overview continuation. | consumed by `P006PCA-G1-VIRAL-001`; review packet only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p006_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 006 after Bogdan's `page 006 complete ok` decision. | `page_006_complete_accepted`; page 006 only, no whole Gate 1 or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_001/page_complete_review_packet.md` | First page 007 page-complete review packet with upper visual/UI art over-modeled as text and heading split as a separate page block. | held by Bogdan; superseded by `PCRP-G1-VIRAL-P007-002` |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_002/page_complete_review_packet.md` | Superseding page 007 review packet with deferred Spektral Krew `ui_art_anchor`, left article text block containing heading/body units, right continuation block, semantic JSON/Markdown, projection validation, and inventory reconciliation. | held by Bogdan for paragraph-boundary flattening; superseded by `PCRP-G1-VIRAL-P007-003` |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_003/page_complete_review_packet.md` | Paragraph-preserving superseding page 007 review packet with the same three crop/block model as P007-002 and separate semantic units for visible article paragraphs. | consumed by `P007PCA-G1-VIRAL-001`; review packet only, page 007 only, no page 008 processing |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p007_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 007 after Bogdan's `page 007 complete ok` decision. | `page_007_complete_accepted`; page 007 only, no page 008, whole Gate 1, or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p008_G1_VIRAL_001/page_complete_review_packet.md` | Page 008 review packet with action backlog, Marco continuation text, Corrina text/appearance blocks, deferred portrait/photo and crystal/object anchors, semantic JSON/Markdown, projection validation, and inventory reconciliation. | consumed by `P008PCA-G1-VIRAL-001`; review packet only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p008_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 008 after Bogdan's `page 008 complete ok` decision. | `page_008_complete_accepted`; page 008 only, no whole Gate 1 or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_002/gate_1_status_summary.md` | Post-P008 Gate 1 status/route packet that records pages 002-008 page-complete accepted only, current canonical narrow 13 source records, stale/narrow `G1SP-G1-VIRAL-001`, first-class blockers, negative capability matrix, state taxonomy, predecessor binding, and non-authorizing routing options. | `gate_1_status_route_packet_ready_no_acceptance`; status only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_001_triage_G1_VIRAL_001/page_001_triage_summary.md` | Page 001 triage/readiness routing packet with full-page cover visual anchor, title/logo area, footer/rating/tagline/logo mixed visual area, and routing recommendation to a visual/title page-complete review without OCR/remediation. | `page_001_triage_ready_for_bogdan_routing_decision`; triage only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p001_G1_VIRAL_001/page_complete_review_packet.md` | Page 001 visual/title page-complete review packet with full-page cover, title/logo, and footer/rating/tagline/logo deferred visual anchors, consuming `P001TR-G1-VIRAL-001`. | `ready_for_bogdan_page_complete_decision`; review packet only, no acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_triage_G1_VIRAL_003/page_009_triage_summary.md` | Page 009 crop-role contract with separate source-region, human-review, OCR-candidate, and text-evidence crop boxes. | accepted by Bogdan as crop contract only; no PCRP or page acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_text_extraction_G1_VIRAL_001/page_009_text_map.md` | Draft page 009 text map from the two text evidence crops after crop-contract OK. | `draft_text_ready_for_bogdan_review_no_ocr_acceptance`; no source/PCRP/page acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_semantic_text_map_G1_VIRAL_001/page_009_semantic_text_map.md` | Semantic page 009 text map with heading levels, block roles, display styles, reading order, paragraph boundaries, crop linkage, and inventory reconciliation after text OK. | `semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance`; no source/PCRP/page acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p009_G1_VIRAL_001/page_complete_review_packet.md` | Page 009 page-complete review packet consuming the crop contract, text draft, and semantic map. | `ready_for_bogdan_page_complete_decision`; review packet only, no acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 009 after Bogdan's `page 009 complete ok` decision. | `page_009_complete_accepted`; page 009 only, no whole Gate 1 or fixture admission |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_004/gate_1_status_summary.md` | Post-P009 Gate 1 status/route packet recording pages 001-009 page-complete accepted only and routing page 010 triage/readiness as the next candidate. | `gate_1_status_route_packet_ready_no_acceptance`; status only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_triage_G1_VIRAL_001/page_010_triage_summary.md` | Page 010 triage crop-contract packet with source-region, human-review, OCR-candidate, and text-evidence crops; lower R05 is modeled as two peer text blocks with no shared lower crop. | `page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp`; no text extraction, PCRP, or page acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_text_extraction_G1_VIRAL_001/page_010_text_map.md` | Draft page 010 text map from the four text evidence crops after triage OK, with logical order `B001 -> B005 -> B002 -> B006` and crop-order validation before semantic/PCRP. | `draft_text_ready_for_bogdan_review_no_ocr_acceptance`; no source/semantic/PCRP/page acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_semantic_text_map_G1_VIRAL_001/page_010_semantic_text_map.md` | Semantic page 010 text map with heading levels, block roles, display styles, continuation links, paragraph boundaries, crop linkage, text-extraction consumer gate, and inventory reconciliation after text OK. | `semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance`; no source/PCRP/page acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p010_G1_VIRAL_001/page_complete_review_packet.md` | Page 010 page-complete review packet consuming P010TR/P010TXT/P010SEM with 6/6 ready blocks, no blockers, valid semantic validation/projection/inventory checks, and review asset deduplication: 16 logical attachments, 12 physical assets, 4 alias role bindings. | `ready_for_bogdan_page_complete_decision`; no page acceptance |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_record.md` | Explicit page-complete acceptance record for page 010 after Bogdan's `page 010 complete ok` decision. | `page_010_complete_accepted`; page 010 only, no whole Gate 1 or fixture admission |
| `scripts/review_asset_deduplication.py` | Shared page-review package asset deduplication contract separating physical package assets, logical role bindings, and chat delivery assets. | `sourcefold_review_asset_deduplication.v1`; reusable fail-closed guard |
| `scripts/crop_order_validation.py` | Shared crop-order validation rule for text extraction consumers before semantic/PCRP movement. | `sourcefold_crop_order_validation.v1`; reusable fail-closed guard |
| `viral_forward_10_step_plan.md` | Sol/Terra-reviewed forward plan after bundle-freeze prerequisite blocker. | active; not an authorization by itself |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/map_schema_identity_packet.md` | Version-bound provisional map schema/shared identity packet. | `valid_for_review`; non-accepting schema prerequisite only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/doc_map_trial_report.md` | First non-accepting trial doc-map registry. | `valid_for_review`; non-accepting registry evidence only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/content_map_trial_report.md` | First non-accepting trial content-map layer. | `valid_for_review`; structural candidates only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/art_map_trial_report.md` | First non-accepting trial art-map layer. | `valid_for_review`; visual/mixed flags only |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/map_consistency_validation_report.md` | First non-accepting cross-map consistency validation. | `passed_for_bundle_freeze_review`; does not freeze bundle |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/pre_ocr_map_bundle_report.md` | First frozen pre-OCR map bundle lineage. | `frozen_for_review`; `not_admitted_for_ocr` |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_prep_package_report.md` | OCR candidate/scoring/gold-sample-plan and map admission prep package. | `ready_for_gold_and_ocr_authorization`; no OCR/gold text |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_benchmark_prerequisite_review.md` | OCR benchmark prerequisite/blocker review. | `blocked_waiting_gold_and_ocr_candidate`; no OCR run |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gold_sample_manifest.md` | Small controlled gold-sample manifest for OCR benchmark review. | `valid_for_review`; not accepted source text |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_candidate_manifest.md` | OCR candidate manifest/config. | `candidate_config_frozen_for_review`; no OCR run |
| `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_benchmark_OBR-G1-VIRAL-002/` | First bounded OCR benchmark run over five admitted crops, with ORB/OOM/OBR and raw outputs. | `remediation_recommended_before_gate_review`; not Gate 1 acceptance |
| `pre_ocr_mapping_model.md` | Proposed doc/content/art map model for pre-OCR structural reconnaissance. | draft proposal |
| `today_20260715_step_plan.md` | Original 2026-07-15 ten-step Gate 1 bootstrap plan. | completed original plan; retained as bounded-continuation cursor |

## Steps

| Step | Status | Evidence |
|---|---|---|
| Create bundled goal shell | completed | `plan.md`, `context.md` |
| Draft charter/vocabulary/lineage/fixtures/matrix | completed | goal documents |
| Collect Sol architecture review | completed | `handoffs/sol-architecture-20260715.md` |
| Collect Terra independent critique | completed | `handoffs/terra-critique-20260715.md` |
| Integrate review findings without expanding scope | completed | updated docs/context |
| Update roadmap/status/checkpoint | completed | validator and documentation checkpoint |
| Capture OCR-first profile comments | completed | `user_ocr_profile_notes.md`, `ocr_first_10_step_roadmap.md` |
| Collect OCR-first Sol/Terra review | completed | OCR-first handoffs |
| Detail Phase 0 / Gate 1 hierarchy | completed | `phase_gate_component_hierarchy.md` |
| Collect prior-work evidence analysis | completed | `prior_work_evidence_index.md`, Sol handoff |
| Collect hierarchy critique | completed | Terra handoff |
| Preserve `Вирал` as candidate input | completed | `fixtures/candidate_inputs/viral/README.md` |
| Draft Gate 1 Qualification Protocol | active | Step 9 fixture and acceptance updates confirmed by Sol/Terra and committed as `7b0c2f41` |
| Analyze pre-OCR doc/content/art maps | completed | `pre_ocr_mapping_model.md`, Sol/Terra handoffs |
| Execute today's Gate 1 protocol plan | completed | Original ten-step bootstrap completed; current continuation is governed by the global Gate 1 roadmap and bounded authorizations |

## Exit Gate

Phase 0 is ready for user decision when:

- all 0.1 release decisions are either accepted or explicitly pending with an
  owner;
- the first source profile is selected or Gate 1 records exactly which
  parameters are accepted, evidence-gated, parked, or blocked;
- exact Gate 1 Qualification Protocol revision is accepted and a distinct
  bounded authorization names the exact action before any candidate PDF
  processing or benchmark work;
- no module implementation is blocked by ambiguous acceptance, lineage, waiver,
  or evidence vocabulary;
- Sol and Terra handoff findings are recorded;
- `npm run validate:roadmap` and documentation checkpoint pass.


## Documentation Checkpoint: doc-checkpoint-20260714T220418Z

- Created: 2026-07-14T22:04:18Z
- Type: documentation
- Summary: Created Phase 0 release charter draft and review handoffs.

Completed:
- Drafted release charter, acceptance vocabulary, lineage model, fixture strategy, and acceptance matrix
- Recorded Sol architecture handoff
- Recorded Terra independent critique handoff
- Updated roadmap decision nodes to active Phase 0 artifacts

Next:
- User chooses first 0.1 source profile and acceptance authority decisions

Blockers:
- No blockers supplied.

Roadmap nodes:
- phase-0
- decision-source-profile-0.1
- decision-canonical-formats
- decision-acceptance-authority
- decision-artifact-identity
- decision-trace-anchor-model
- decision-waiver-policy

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260714T223721Z

- Created: 2026-07-14T22:37:21Z
- Type: documentation
- Summary: Integrated OCR-first 10-step roadmap and source-profile corrections.

Completed:
- Captured user OCR-first PDF/page-image comments
- Recorded Sol OCR-first 10-step roadmap handoff
- Recorded Terra OCR-first critique handoff
- Added Core 0.1 executable acceptance matrix
- Expanded lineage and fixtures for PDF/page-image/OCR/order/overlay gates

Next:
- User confirms OCR-first profile details, page-image render profile, pilot discovery, and two-column rules

Blockers:
- No blockers supplied.

Roadmap nodes:
- phase-0
- decision-source-profile-0.1
- decision-canonical-formats
- decision-artifact-identity
- decision-trace-anchor-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260714T223803Z

- Created: 2026-07-14T22:38:03Z
- Type: documentation
- Summary: Recorded Sol/Terra OCR-first 10-step roadmap integration.

Completed:
- Added Sol OCR-first 10-step roadmap handoff
- Added Terra OCR-first critique handoff
- Added Core 0.1 executable acceptance matrix
- Expanded OCR-first lineage, fixtures, and 10-step roadmap

Next:
- User reviews OCR-first profile, 300-DPI page-image assumption, two-column profile, and pilot discovery

Blockers:
- No blockers supplied.

Roadmap nodes:
- phase-0
- decision-source-profile-0.1
- decision-artifact-identity
- decision-trace-anchor-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T003214Z

- Created: 2026-07-15T00:32:14Z
- Type: documentation
- Summary: Detailed Phase 0 Gate 1 source-profile hierarchy and prior-work evidence gates.

Completed:
- Recorded Sol prior-work evidence handoff
- Recorded Sol Phase/Gate/Component architecture handoff
- Recorded Terra hierarchy critique handoff
- Expanded Gate 1 Source Profile into subcomponents and parameter register
- Demoted fixed render values to evidence-gated benchmark candidates

Next:
- User supplies the Viral PDF so pages 1-20 can be hash-bound
- Predeclare render/OCR benchmark protocol before accepting DPI, color, format, OCR engine, or thresholds
- Reconcile Gate 1 parameter IDs with future schemas and fixtures

Blockers:
- Viral pilot PDF is not supplied or hash-bound
- Render/OCR/taxonomy parameters remain evidence-gated

Roadmap nodes:
- phase-0
- decision-source-profile-0.1
- decision-canonical-formats
- decision-artifact-identity
- decision-trace-anchor-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T160428Z

- Created: 2026-07-15T16:04:28Z
- Type: documentation
- Summary: Refreshed Phase 0 stop point after Viral candidate push and Gate 1 workflow rules.

Completed:
- Recorded current stop point at pushed commit d183215e
- Updated Sourcefold agent rules for Phase/Gate work and candidate inputs
- Updated Gate 1 hierarchy/spec to require Qualification Protocol before Viral processing
- Updated Phase 0 plan/context and project status

Next:
- Draft gate_01_qualification_protocol.md
- Review protocol with Sol/Terra before any Viral render/OCR/benchmark work
- Keep Viral PDF as candidate input until selected-page manifest and intake rules are accepted

Blockers:
- Gate 1 Qualification Protocol is not drafted
- Viral selected-page manifest is missing
- Render/OCR/taxonomy parameters remain evidence-gated

Roadmap nodes:
- phase-0
- gate-01-source-profile
- decision-source-profile-0.1

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T162639Z

- Created: 2026-07-15T16:26:39Z
- Type: documentation
- Summary: Added draft pre-OCR doc/content/art mapping model and review handoffs.

Completed:
- Captured user request for doc_map/content_map/art_map reconnaissance
- Recorded Sol taxonomy and architecture handoffs
- Recorded Terra independent critique handoff
- Recorded prior-books map evidence handoff
- Updated pre_ocr_mapping_model as evidence-gated proposal

Next:
- Fold pre-OCR mapping decisions into gate_01_qualification_protocol.md
- Decide canonical JSON schema and bundle identity before implementation
- Keep Viral unmapped until protocol acceptance

Blockers:
- Qualification Protocol absent
- Canonical map format and artifact identity unresolved
- Pre-OCR maps not approved for implementation

Roadmap nodes:
- phase-0
- gate-01-source-profile
- decision-source-profile-0.1
- decision-canonical-formats
- decision-artifact-identity
- decision-trace-anchor-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T163648Z

- Created: 2026-07-15T16:36:48Z
- Type: roadmap
- Summary: Linked pre-OCR mapping model into Gate 1 roadmap, governance, and visualization metadata.

Completed:
- Added roadmap node gate-01-pre-ocr-map-model and linear dependency from Gate 1 to Source Profile decision
- Bound pre-OCR map model to Gate 1 hierarchy and Core 0.1 acceptance rows
- Documented roadmap/viewer as state metadata only, not map payload storage

Next:
- Draft gate_01_qualification_protocol.md before any Viral mapping, rendering, OCR, or benchmark work
- Decide canonical map schema and artifact identity before implementing map artifacts
- Keep future map visualization reading canonical evidence artifacts, not roadmap YAML

Blockers:
- Qualification Protocol absent
- Canonical map schema and bundle identity unresolved
- Pre-OCR maps not approved for implementation

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-pre-ocr-map-model
- decision-source-profile-0.1
- decision-canonical-formats
- decision-artifact-identity
- decision-trace-anchor-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T164329Z

- Created: 2026-07-15T16:43:29Z
- Type: roadmap
- Summary: Updated today's 10-step Gate 1 Qualification Protocol plan.

Completed:
- Committed pre-OCR map roadmap governance wiring as c227b746
- Created today_20260715_step_plan.md with ten step-by-step Gate 1 actions
- Inserted gate-01-qualification-protocol into the roadmap chain before pre-OCR map model

Next:
- Start Step 1 by drafting gate_01_qualification_protocol.md shell
- Review the protocol shell before authorizing any Viral candidate action
- Keep Viral candidate unprocessed until protocol acceptance

Blockers:
- Gate 1 Qualification Protocol not drafted
- Authority and canonical schema decisions unresolved
- No Viral render OCR mapping or benchmark work authorized

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model
- decision-source-profile-0.1

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T170707Z

- Created: 2026-07-15T17:07:07Z
- Type: documentation
- Summary: Recorded Sol/Terra Step 1 review; revisions required before Step 3.

Completed:
- Recorded Sol Step 1 architecture review handoff
- Recorded Terra Step 1 independent critique handoff
- Updated plan/context/status/roadmap to mark Step 1 as reviewed with required revisions

Next:
- Revise Step 1 state namespaces, shell acceptance boundary, evidence identity, and candidate quarantine
- Revise Step 2 input package under the same review constraints
- Keep Step 3 blocked until revisions are reviewed

Blockers:
- Step 1 required revisions pending
- Step 2 draft needs revision
- Step 3 authority/state work blocked
- No Viral processing authorized

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T171400Z

- Created: 2026-07-15T17:14:00Z
- Type: documentation
- Summary: Applied Step 1/2 revision pass after Sol/Terra review.

Completed:
- Applied Step 1/2 revision pass after Sol/Terra review
- Separated protocol, permission, decision, evidence, and finding/waiver state namespaces
- Strengthened evidence identity/lineage/action authorization/stale behavior
- Made candidate PDF quarantine absolute before Step 4 and bounded authorization

Next:
- User reviews revised Step 1/2 protocol text
- If accepted, continue to Step 3 authority/state drafting
- Keep Viral candidate unprocessed and Step 3 blocked until review decision

Blockers:
- User review of Step 1/2 revisions pending
- Step 3 authority/state drafting not authorized yet
- No Viral processing authorized

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T172844Z

- Created: 2026-07-15T17:28:44Z
- Type: documentation
- Summary: Drafted Step 3 authority/state rules after confirmed Step 1/2 remediation.

Completed:
- Committed confirmed Step 1/2 remediation as 2872f650
- Drafted Step 3 authority/state rules in gate_01_qualification_protocol.md
- Kept Viral quarantine and default-deny operational boundary intact

Next:
- Review Step 3 authority/state draft
- Do not continue to Step 4 candidate PDF intake until Step 3 review is accepted
- Keep Viral candidate unprocessed

Blockers:
- Step 3 review pending
- Step 4 candidate PDF intake not authorized
- No Viral processing authorized

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260715T174911Z

- Created: 2026-07-15T17:49:11Z
- Type: documentation
- Summary: Drafted Step 4 candidate PDF intake rules after committed Step 3.

Completed:
- Committed Step 3 authority/state rules as 85b0b765
- Drafted Step 4 candidate PDF intake rules
- Kept Viral candidate fully quarantined with no PDF interaction

Next:
- Review Step 4 candidate intake draft with Sol/Terra before commit
- Do not continue to Step 5 render benchmark rules until Step 4 review is accepted
- Keep Viral candidate unprocessed

Blockers:
- Step 4 review pending
- Step 5 render benchmark drafting not authorized
- No Viral processing authorized

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260717T164232Z

- Created: 2026-07-17T16:42:32Z
- Type: documentation
- Summary: Drafted OpenClaw Step 10 review checkpoint with governance blockers.

Completed:
- Created OpenClaw pre-Step-10 checkpoint commit 4a41673b
- Collected read-only protocol, roadmap/status, and safety reviews
- Added explicit Step 10 protocol section and normalized protocol status namespace
- Tightened adjacent authorization wording to require accepted_protocol plus distinct bounded authorization

Next:
- Review Step 10 cleanup and decide whether to move protocol to review_ready or keep blocked
- Keep Viral candidate quarantined until exact accepted protocol plus bounded authorization
- Rerun roadmap validation before any follow-up commit

Blockers:
- Protocol is not accepted
- No bounded trial authorization exists
- Step 10 review/checkpoint records blockers and does not authorize candidate-derived action

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260717T165139Z

- Created: 2026-07-17T16:51:39Z
- Type: documentation
- Summary: Resolved OpenClaw Step 10 review blockers; protocol review_ready for review only.

Completed:
- Remediated Sol/Terra Step 10 blockers in roadmap, protocol, matrix, status, and hierarchy
- Updated hard-stop table so every candidate-derived row requires exact accepted_protocol plus distinct bounded authorization
- Changed Step 10 state to review_ready for user/Sol/Terra review only
- Kept protocol acceptance and bounded trial authorization explicitly missing

Next:
- User/Sol/Terra review exact review_ready protocol revision
- Do not process Viral or create candidate-derived artifacts before accepted_protocol plus distinct bounded authorization
- If review passes, user may separately accept exact protocol revision hash

Blockers:
- No blockers to `review_ready`.
- Protocol acceptance remains a separate future user decision.
- Bounded trial authorization remains a separate future action gate; no
  candidate-derived action is authorized.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260717T172129Z

- Created: 2026-07-17T17:21:29Z
- Type: documentation
- Summary: Accepted exact Gate 1 Qualification Protocol revision and recorded first bounded trial authorization.

Completed:
- User accepted Gate 1 Qualification Protocol revision 5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a / file blob 4d494e83d8d63dd3778a3813b3ee529449cee51a as accepted_protocol for methodology only.
- Recorded bounded authorization BA-G1-VIRAL-SPM-001 for selected-page manifest creation only, with exact inputs, outputs, limits, authority, expiry, and invalidation behavior.
- Preserved default-deny candidate quarantine for every action not named by BA-G1-VIRAL-SPM-001.

Next:
- Execute only BA-G1-VIRAL-SPM-001 if proceeding with candidate work: create selected-page manifest for ordinal pages 1-20.
- Record resulting manifest with protocol revision 5ee1760f, authorization ID BA-G1-VIRAL-SPM-001, predecessor identity, actor, timestamp, and invalidation rules.
- Keep render, OCR, mapping, benchmarks, QA, fixtures, source acceptance, translation, proofreading, and implementation blocked until separately authorized.

Blockers:
- Selected-page manifest has not been created yet.
- All candidate-derived actions outside BA-G1-VIRAL-SPM-001 remain blocked by default.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- Gate 1 Qualification Protocol revision 5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a / file blob 4d494e83d8d63dd3778a3813b3ee529449cee51a is accepted as accepted_protocol for methodology only.
- Bounded authorization BA-G1-VIRAL-SPM-001 authorizes only selected-page manifest creation for Viral ordinal pages 1-20 using already recorded candidate identity; rendering, OCR, mapping, benchmarks, QA, fixtures, source acceptance, translation, proofreading, and implementation remain blocked.

## Documentation Checkpoint: doc-checkpoint-20260717T172518Z

- Created: 2026-07-17T17:25:18Z
- Type: documentation
- Summary: Executed first bounded trial by creating selected-page manifest only.

Completed:
- Executed bounded authorization BA-G1-VIRAL-SPM-001 within scope.
- Created selected-page manifest SPM-G1-VIRAL-001 for Viral ordinal pages 1-20 using already recorded candidate identity only.
- Marked BA-G1-VIRAL-SPM-001 as scope-consumed; no render, OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, or implementation action was authorized.

Next:
- Review SPM-G1-VIRAL-001 before requesting any next bounded candidate action.
- If proceeding, create a separate bounded authorization for the exact next action; do not reuse BA-G1-VIRAL-SPM-001.
- Keep render, OCR, mapping, benchmarks, QA, fixtures, source acceptance, translation, proofreading, and implementation blocked until separately authorized.

Blockers:
- SPM-G1-VIRAL-001 review pending.
- All candidate-derived actions outside the completed selected-page manifest remain blocked by default.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- Selected-page manifest SPM-G1-VIRAL-001 was created under BA-G1-VIRAL-SPM-001 for Viral ordinal pages 1-20 using already recorded candidate identity only.
- BA-G1-VIRAL-SPM-001 is scope-consumed and cannot authorize render, OCR, mapping, benchmarks, QA, fixtures, source acceptance, translation, proofreading, or implementation.

## Documentation Checkpoint: doc-checkpoint-20260717T174729Z

- Created: 2026-07-17T17:47:29Z
- Type: documentation
- Summary: Executed bounded render trial for selected Viral pages only.

Completed:
- Recorded bounded render authorization BA-G1-VIRAL-RENDER-001 after Sol/Terra read-only review.
- Created frozen render candidate manifest RCM-G1-VIRAL-RENDER-001 and frozen comparison plan CP-G1-VIRAL-RENDER-001.
- Executed render trial RT-G1-VIRAL-RENDER-001 for SPM-G1-VIRAL-001 ordinal pages 1-20 using PyMuPDF 1.27.2.3 at 300 DPI RGB PNG.
- Recorded render_output_manifest.md with 20 PNG outputs and SHA-256 identities; BA-G1-VIRAL-RENDER-001 is scope-consumed.

Next:
- Review RT-G1-VIRAL-RENDER-001 render output manifest before requesting any next bounded candidate action.
- Create a separate bounded authorization for OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation before any such action.
- Keep render evidence as trial evidence only; do not treat PyMuPDF, 300 DPI, RGB, or PNG as accepted profile parameters.

Blockers:
- RT-G1-VIRAL-RENDER-001 review pending.
- OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- Bounded render authorization BA-G1-VIRAL-RENDER-001 was executed only for SPM-G1-VIRAL-001 ordinal pages 1-20 using PyMuPDF 1.27.2.3 at 300 DPI RGB PNG.
- Render trial RT-G1-VIRAL-RENDER-001 produced 20 PNG page images and output manifest SHA-256 622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC.
- BA-G1-VIRAL-RENDER-001 is scope-consumed and cannot authorize OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## Documentation Checkpoint: doc-checkpoint-20260717T180329Z

- Created: 2026-07-17T18:03:29Z
- Type: documentation
- Summary: Recorded bounded visual sanity review for rendered Viral pages.

Completed:
- Formally reviewed RT-G1-VIRAL-RENDER-001 output manifest: 20 rows and 20 PNG files present.
- Recorded bounded visual sanity authorization BA-G1-VIRAL-VISUAL-001.
- Created visual_sanity_contact_sheet.png and visual sanity report VSR-G1-VIRAL-001.
- Recorded broad page-kind and gross render sanity only; no OCR, transcription, mapping, benchmark scoring, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation was performed.

Next:
- Decide whether the next bounded candidate action is page inventory/map authorization or render benchmark authorization.
- Keep VSR-G1-VIRAL-001 as non-accepting inventory evidence only.
- Create a separate bounded authorization before OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

Blockers:
- Next candidate-derived action authorization is missing.
- OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- Bounded visual sanity authorization BA-G1-VIRAL-VISUAL-001 produced VSR-G1-VIRAL-001 for RT-G1-VIRAL-RENDER-001 as non-accepting inventory evidence only.
- BA-G1-VIRAL-VISUAL-001 is scope-consumed and cannot authorize OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## Documentation Checkpoint: doc-checkpoint-20260717T182626Z

- Created: 2026-07-17T18:26:26Z
- Type: documentation
- Summary: Recorded bounded page inventory for rendered Viral pages.

Completed:
- Recorded bounded page inventory authorization BA-G1-VIRAL-PAGEINV-001 after Sol/Terra read-only boundary review.
- Created page inventory report PIR-G1-VIRAL-001 for RT-G1-VIRAL-RENDER-001 ordinal pages 1-20 using rendered PNG/contact sheet predecessors only.
- Recorded broad page-kind and coarse layout hints only; no OCR, transcription, PDF text-layer extraction, map, regions, anchors, reading order, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation was performed.

Next:
- Review PIR-G1-VIRAL-001 as non-accepting page-level inventory evidence only.
- If proceeding, request a fresh bounded authorization for the exact next action, likely page map/model work or a render benchmark/OCR trial.
- Keep OCR, map, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until separately authorized.

Blockers:
- PIR-G1-VIRAL-001 review pending.
- Map/OCR/benchmark/QA/fixture/source-acceptance/translation/proofreading/implementation authorizations remain missing.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol

Accepted decisions:
- Bounded page inventory authorization BA-G1-VIRAL-PAGEINV-001 produced PIR-G1-VIRAL-001 for RT-G1-VIRAL-RENDER-001 as non-accepting page-level inventory evidence only.
- BA-G1-VIRAL-PAGEINV-001 is scope-consumed and cannot authorize OCR, map, region registry, anchors, reading order, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## Documentation Checkpoint: doc-checkpoint-20260717T205530Z

- Created: 2026-07-17T20:55:30Z
- Type: documentation
- Summary: Recorded bounded page-map model for rendered Viral pages.

Completed:
- Committed page inventory checkpoint 29298265 before starting the page-map/model trial.
- Recorded bounded page-map/model authorization BA-G1-VIRAL-PAGEMAP-001 after Sol/Terra read-only boundary review.
- Created page map/model report PMR-G1-VIRAL-001 for Viral pages 1-20 using existing PNG/PIR evidence only.
- Recorded page-level planning/model fields only; no OCR, transcription, PDF text-layer extraction, region coordinates, anchors, reading order, pre_ocr_map_bundle, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation was performed.

Next:
- Review PMR-G1-VIRAL-001 as non-accepting page-level planning evidence only.
- If proceeding, request a fresh bounded authorization for either provisional region-map creation, render benchmark, or OCR trial.
- Keep doc_map/content_map/art_map, pre_ocr_map_bundle freezing, OCR, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until separately authorized.

Blockers:
- PMR-G1-VIRAL-001 review pending.
- Region-map/OCR/benchmark/QA/fixture/source-acceptance/translation/proofreading/implementation authorizations remain missing.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- Bounded page-map/model authorization BA-G1-VIRAL-PAGEMAP-001 produced PMR-G1-VIRAL-001 for RT-G1-VIRAL-RENDER-001 as non-accepting page-level planning evidence only.
- BA-G1-VIRAL-PAGEMAP-001 is scope-consumed and cannot authorize doc_map, content_map, art_map, pre_ocr_map_bundle freezing, OCR, region registry, anchors, reading order, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## Documentation Checkpoint: doc-checkpoint-20260717T212008Z

- Created: 2026-07-17T21:20:08Z
- Type: documentation
- Summary: Recorded bounded provisional region map for rendered Viral pages.

Completed:
- Committed page map/model checkpoint 186d88fd before starting provisional region-map annotation.
- Recorded bounded region-map authorization BA-G1-VIRAL-REGIONMAP-001 after Sol/Terra read-only boundary review.
- Created provisional region map report PRM-G1-VIRAL-001 with 62 provisional visual region annotations for Viral pages 1-20 using rendered PNG predecessors only.
- Recorded approximate pixel and normalized boxes as provisional annotations only; no OCR, transcription, PDF text-layer extraction, accepted reading order, QA, benchmark, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, implementation, or pre_ocr_map_bundle freezing was performed.

Next:
- Review PRM-G1-VIRAL-001 as non-accepting provisional annotation evidence only.
- If proceeding, request a fresh bounded authorization for map-bundle freezing, render benchmark, or OCR trial.
- Keep OCR, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, implementation, and pre_ocr_map_bundle freezing blocked until separately authorized.

Blockers:
- PRM-G1-VIRAL-001 review pending.
- Map-bundle-freezing/OCR/benchmark/QA/fixture/source-acceptance/translation/proofreading/implementation authorizations remain missing.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- Bounded region-map authorization BA-G1-VIRAL-REGIONMAP-001 produced PRM-G1-VIRAL-001 as non-accepting provisional annotation evidence only.
- BA-G1-VIRAL-REGIONMAP-001 is scope-consumed and cannot authorize pre_ocr_map_bundle freezing, OCR, accepted anchors, accepted reading order, benchmark, QA, fixture, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

## Documentation Checkpoint: doc-checkpoint-20260718T044821Z

- Created: 2026-07-18T04:48:21Z
- Type: documentation
- Summary: Recorded Viral map-bundle prerequisite review; bundle freeze blocked.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-MAPBUNDLE-PREQ-001 for prerequisite/lineage review only.
- Created MBR-G1-VIRAL-001 from existing SPM/RT/VSR/PIR/PMR/PRM predecessor hashes.
- Recorded Sol NOT OK for freezing a real pre_ocr_map_bundle from current predecessors and Terra conditional OK only for non-accepting lineage/index evidence.

Next:
- Request a fresh bounded authorization for version-bound provisional map schema/shared identity and exact doc_map/content_map/art_map trial artifacts.
- Keep pre_ocr_map_bundle freezing, OCR, benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked.

Blockers:
- No exact doc_map/content_map/art_map revisions exist.
- No accepted or version-bound provisional schema set and shared page/region identity model exists.
- MBR-G1-VIRAL-001 blocks real pre_ocr_map_bundle freezing from SPM/RT/VSR/PIR/PMR/PRM alone.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-MAPBUNDLE-PREQ-001 produced MBR-G1-VIRAL-001 as non-accepting prerequisite review only; it does not create or freeze pre_ocr_map_bundle.
- A real pre_ocr_map_bundle freeze remains blocked until exact doc_map, content_map, art_map, schema, and shared identity predecessors exist.

## Documentation Checkpoint: doc-checkpoint-20260718T054158Z

- Created: 2026-07-18T05:41:58Z
- Type: documentation
- Summary: Recorded Viral forward plan and map schema identity packet.

Completed:
- Recorded Sol/Terra-reviewed Viral forward 10-step plan.
- Recorded bounded authorization BA-G1-VIRAL-MAPSCHEMA-001 for schema/shared identity only.
- Created MSID-G1-VIRAL-001 as version-bound provisional schema/shared identity evidence.
- Recorded Sol OK and Terra conditional OK for MSID limited use.

Next:
- Request fresh BA-G1-VIRAL-DOCMAP-001 before creating any doc_map payload.
- Keep content_map, art_map, bundle freezing, OCR, benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- MSID review/commit alone does not authorize map payload creation.
- Bundle freezing remains blocked until exact reviewed doc_map/content_map/art_map hashes and cross-map validation exist.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-MAPSCHEMA-001 produced MSID-G1-VIRAL-001 as non-accepting version-bound provisional schema/shared identity evidence only.
- MSID-G1-VIRAL-001 may support future separately authorized non-accepting map-layer trials, but cannot create map payloads or freeze pre_ocr_map_bundle by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T054517Z

- Created: 2026-07-18T05:45:17Z
- Type: documentation
- Summary: Recorded Viral trial doc map registry.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-DOCMAP-001 for non-accepting doc_map only.
- Created DM-G1-VIRAL-001 with MSID trial page/region IDs and PRM provenance only.
- Confirmed doc_map payload contains no OCR text, copied text, accepted reading order, accepted coordinates, or bundle freeze.

Next:
- Request fresh BA-G1-VIRAL-CONTENTMAP-001 before creating content_map payload.
- Keep art_map, map consistency validation, pre_ocr_map_bundle freezing, OCR, benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- DM-G1-VIRAL-001 is non-accepting registry evidence only.
- Content/art map layers and bundle freeze remain missing.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-DOCMAP-001 produced DM-G1-VIRAL-001 as non-accepting trial doc-map registry evidence only.
- DM-G1-VIRAL-001 may support future separately authorized content_map/art_map trials, but cannot freeze pre_ocr_map_bundle or authorize OCR by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T054748Z

- Created: 2026-07-18T05:47:48Z
- Type: documentation
- Summary: Recorded Viral trial content map.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-CONTENTMAP-001 for non-accepting content_map only.
- Created CM-G1-VIRAL-001 referencing DM/MSID trial IDs with structural candidates only.
- Confirmed content_map payload contains no copied text, OCR output, PDF text-layer content, accepted reading order, or accepted OCR routing.

Next:
- Request fresh BA-G1-VIRAL-ARTMAP-001 before creating art_map payload.
- Keep map consistency validation, pre_ocr_map_bundle freezing, OCR, benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- CM-G1-VIRAL-001 is non-accepting structural-candidate evidence only.
- Art map, cross-map validation, and bundle freeze remain missing.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-CONTENTMAP-001 produced CM-G1-VIRAL-001 as non-accepting trial content-map evidence only.
- CM-G1-VIRAL-001 may support future separately authorized art-map/consistency/bundle steps, but cannot freeze pre_ocr_map_bundle or authorize OCR by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T055019Z

- Created: 2026-07-18T05:50:19Z
- Type: documentation
- Summary: Recorded Viral trial art map.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-ARTMAP-001 for non-accepting art_map only.
- Created AM-G1-VIRAL-001 referencing DM/MSID trial IDs with visual/mixed flags only.
- Confirmed art_map payload contains no text-in-art transcription, OCR output, PDF text-layer content, semantic art interpretation, or accepted coordinates.

Next:
- Request fresh BA-G1-VIRAL-MAPCONSISTENCY-001 before validating cross-map references and payload leakage.
- Keep pre_ocr_map_bundle freezing, OCR, benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- AM-G1-VIRAL-001 is non-accepting visual/mixed evidence only.
- Cross-map validation and bundle freeze remain missing.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-ARTMAP-001 produced AM-G1-VIRAL-001 as non-accepting trial art-map evidence only.
- AM-G1-VIRAL-001 may support future separately authorized map consistency and bundle steps, but cannot freeze pre_ocr_map_bundle or authorize OCR by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T055234Z

- Created: 2026-07-18T05:52:34Z
- Type: documentation
- Summary: Recorded Viral map consistency validation.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-MAPCONSISTENCY-001 for validation only.
- Created MCV-G1-VIRAL-001 with verdict passed_for_bundle_freeze_review over current MSID/DM/CM/AM hashes.
- Confirmed cross-map references, union coverage, intentional mixed overlap, stale-hash binding, and payload containment for the trial map set.

Next:
- Request fresh BA-G1-VIRAL-MAPBUNDLE-001 before freezing pre_ocr_map_bundle.
- Keep OCR, benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- MCV-G1-VIRAL-001 does not freeze pre_ocr_map_bundle by itself.
- OCR prep/benchmark remain blocked until bundle/admission prerequisites exist.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-MAPCONSISTENCY-001 produced MCV-G1-VIRAL-001 as non-accepting cross-map consistency validation only.
- MCV-G1-VIRAL-001 may support a future separately authorized pre_ocr_map_bundle freeze, but cannot freeze the bundle or authorize OCR by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T055439Z

- Created: 2026-07-18T05:54:39Z
- Type: documentation
- Summary: Recorded Viral pre-OCR map bundle freeze.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-MAPBUNDLE-001 for bundle freeze only.
- Created POMB-G1-VIRAL-001 binding exact MSID/DM/CM/AM/MCV hashes.
- Recorded POMB-G1-VIRAL-001 as frozen_for_review and not_admitted_for_ocr.

Next:
- Request fresh BA-G1-VIRAL-OCRPREP-001 before preparing OCR candidate/scoring/gold-sample plan and map-consumption admission.
- Keep OCR execution, benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- POMB-G1-VIRAL-001 is not_admitted_for_ocr.
- OCR prep and benchmark remain blocked until explicit admission/prep authorization exists.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-MAPBUNDLE-001 produced POMB-G1-VIRAL-001 as frozen_for_review pre-OCR map bundle lineage only.
- POMB-G1-VIRAL-001 is not_admitted_for_ocr and cannot authorize OCR prep, OCR benchmark, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T055701Z

- Created: 2026-07-18T05:57:01Z
- Type: documentation
- Summary: Recorded Viral OCR preparation package.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-OCRPREP-001 for OCR preparation only.
- Created OPR-G1-VIRAL-001 with OCR candidate manifest stub, scoring plan stub, gold-sample creation plan, and map-consumption admission for planning only.
- Confirmed no OCR execution, OCR output, gold text, copied source text, PDF text-layer content, benchmark, QA, fixture, source acceptance, translation, proofreading, or implementation was performed.

Next:
- Request separate bounded authorization for gold sample creation and admitted OCR benchmark execution, or record OCR benchmark blocked if prerequisites remain missing.
- Keep QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- OPR-G1-VIRAL-001 does not create gold samples or OCR output.
- OCR benchmark execution remains blocked until gold sample authorization and exact OCR candidate identity/config exist.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-OCRPREP-001 produced OPR-G1-VIRAL-001 as OCR preparation evidence only.
- OPR-G1-VIRAL-001 cannot authorize OCR execution, benchmark scoring, gold text creation, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T055944Z

- Created: 2026-07-18T05:59:44Z
- Type: documentation
- Summary: Recorded Viral OCR benchmark prerequisite blocker.

Completed:
- Recorded bounded authorization BA-G1-VIRAL-OCRBENCH-PREQ-001 for prerequisite review only.
- Created OBR-G1-VIRAL-001 with verdict blocked_waiting_gold_and_ocr_candidate.
- Completed the ten-step forward plan through the safe OCR benchmark stop without OCR execution or gold text creation.

Next:
- Request bounded gold-sample creation authorization.
- Request bounded OCR candidate manifest authorization with exact engine/config/environment/output format.
- Only after those are current, request bounded OCR benchmark execution authorization.

Blockers:
- Gold-sample manifest and gold text/sample answers do not exist.
- Exact OCR candidate engine/config/environment manifest does not exist.
- OCR benchmark execution remains blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-OCRBENCH-PREQ-001 produced OBR-G1-VIRAL-001 as OCR benchmark prerequisite review only.
- OCR benchmark execution is blocked until gold-sample creation and OCR candidate manifest/config are separately authorized and frozen.

## Documentation Checkpoint: doc-checkpoint-20260718T061027Z

- Created: 2026-07-18T06:10:27Z
- Type: documentation
- Summary: Recorded Viral gold samples and OCR candidate manifest.

Completed:
- Recorded BA-G1-VIRAL-GOLDSAMPLE-001 and created GSM-G1-VIRAL-001 with five small manually read gold samples.
- Recorded BA-G1-VIRAL-OCRCANDIDATE-001 and created OCM-G1-VIRAL-001 with Tesseract candidate config attempt.
- Confirmed no OCR was run, no PDF text-layer was used, and OCR candidate execution is blocked because tesseract is not available in PATH.

Next:
- Provision or supply an OCR engine executable/version/language data under separate approval.
- Freeze executable OCR candidate manifest/config after engine availability is confirmed.
- Then request bounded OCR benchmark execution authorization.

Blockers:
- OCM-G1-VIRAL-001 is blocked_missing_executable.
- Tesseract command is not available in PATH.
- OCR benchmark execution remains blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-GOLDSAMPLE-001 produced GSM-G1-VIRAL-001 as gold-sample evidence for review only, not accepted source text.
- BA-G1-VIRAL-OCRCANDIDATE-001 produced OCM-G1-VIRAL-001 with status blocked_missing_executable; OCR benchmark execution remains blocked until OCR engine provisioning/freeze occurs.

## Documentation Checkpoint: doc-checkpoint-20260718T070917Z

- Created: 2026-07-18T07:09:17Z
- Type: documentation
- Summary: Recorded Viral OCR candidate executable refresh.

Completed:
- Recorded BA-G1-VIRAL-OCRCANDIDATE-002 for OCR candidate refresh only.
- Refreshed OCM-G1-VIRAL-001 with local Tesseract v5.4.0.20240606, executable hash, eng/osd tessdata hashes, and status candidate_config_frozen_for_review.
- Confirmed no OCR was run and OCR benchmark execution still requires a separate bounded authorization.

Next:
- Request bounded OCR benchmark execution authorization naming exact GSM/OCM/POMB inputs, outputs, limits, expiry, and invalidation behavior.
- Keep QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, and implementation blocked until their separate steps.

Blockers:
- No OCR benchmark execution authorization exists.
- No OCR output manifest or benchmark result exists.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-OCRCANDIDATE-002 refreshed OCM-G1-VIRAL-001 with local Tesseract executable/version/language-data identity and status candidate_config_frozen_for_review.
- OCM-G1-VIRAL-001 still cannot authorize OCR benchmark execution, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement by itself.

## Documentation Checkpoint: doc-checkpoint-20260718T075138Z

- Created: 2026-07-18T07:51:38Z
- Type: documentation
- Summary: Recorded Viral bounded OCR benchmark result.

Completed:
- Recorded BA-G1-VIRAL-OCRBENCH-001 for bounded OCR benchmark execution only.
- Created ORB-G1-VIRAL-001, OOM-G1-VIRAL-001, and OBR-G1-VIRAL-002 under the Viral render trial benchmark folder.
- Ran Tesseract only on five admitted exact crop images and recorded raw text, TSV, logs, stderr captures, hashes, and benchmark findings.
- Recorded verdict remediation_recommended_before_gate_review with no Gate 1 advancement, QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, or implementation.

Next:
- Request separate bounded OCR remediation authorization before any Gate 1 review package.
- Keep Gate 1 advancement and all acceptance actions blocked until separately authorized after remediation evidence.

Blockers:
- OBR-G1-VIRAL-002 does not support Gate 1 advancement as-is.
- OCR remediation authorization is missing.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- BA-G1-VIRAL-OCRBENCH-001 produced non-accepting benchmark evidence only: ORB-G1-VIRAL-001, OOM-G1-VIRAL-001, and OBR-G1-VIRAL-002.
- The first OCR benchmark result recommends remediation before Gate 1 review and cannot authorize QA, fixtures, source acceptance, translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement.

## Documentation Checkpoint: doc-checkpoint-20260718T091319Z

- Created: 2026-07-18T09:13:19Z
- Type: documentation
- Summary: Recorded Viral OCR remediation matrix with Sourcefold-native logic transfer.

Completed:
- Recorded BA-G1-VIRAL-REMEDIATE-001 bounded authorization.
- Added Sourcefold-native OCR remediation transfer plan.
- Added local OCR remediation matrix runner.
- Generated ORM-G1-VIRAL-001 evidence with 5/5 remediation-route passes.

Next:
- Sol/Terra final review confirmation before commit.
- Use remediation evidence only for a later Gate 1 review package under separate authority.

Blockers:
- ORM-G1-VIRAL-001 is remediation evidence only, not source acceptance or Gate 1 advancement.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.


## Documentation Checkpoint: doc-checkpoint-20260718T095416Z

- Created: 2026-07-18T09:54:16Z
- Type: documentation
- Summary: Recorded Viral OCR remediation review package and contract checks.

Completed:
- Recorded BA-G1-VIRAL-REMEDIATION-REVIEW-001 for review/admission/rollup only.
- Generated ORR-G1-VIRAL-001, OAC-G1-VIRAL-001, GER-G1-VIRAL-001, and ONC-G1-VIRAL-001 from existing ORM-G1-VIRAL-001 evidence only.
- Added Sourcefold-native review package generator and pytest contract checks.

Next:
- Use ORR/OAC/GER/ONC only as remediation evidence for a later Gate 1 rollup.
- Do not ask Bogdan for source evaluation until a separate source reconstruction review package contains readable text aligned to source page images/regions.

Blockers:
- No source reconstruction package exists yet.
- ORR/OAC/GER/ONC do not authorize source acceptance, QA, fixtures, translation, proofreading, implementation, or Gate 1 advancement.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T102416Z

- Created: 2026-07-18T10:24:16Z
- Type: documentation
- Summary: Recorded Viral source reconstruction prep package and fail-closed contracts.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-PREP-001 for prep/design/static package logic only.
- Created SRP-G1-VIRAL-001 source reconstruction protocol.
- Created SRA-G1-VIRAL-001 exact admitted page/region/zone/crop manifest with five OCR-candidate regions and two visual-QC-only regions.
- Added fail-closed Sourcefold-native generator skeleton and dry-run report SRD-G1-VIRAL-001.
- Added pytest contract checks for predecessor hashes, exact admitted manifest, zone/crop uniqueness, non-execution boundary, and fail-closed execution.

Next:
- Sol/Terra/critic review of SRP/SRA/SRD/script/tests.
- Only after OK, request separate BA-G1-VIRAL-SOURCE-RECON-RUN-001 naming exact command, config, manifest hash, output directory, limits, expiry, and invalidation behavior.

Blockers:
- No source reconstruction run authorization exists.
- Prep package does not create candidate text, source acceptance, QA, fixtures, translation, proofreading, implementation, or Gate 1 advancement.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T103916Z

- Created: 2026-07-18T10:39:16Z
- Type: documentation
- Summary: Recorded Viral source reconstruction candidate review package.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-RUN-001 for one bounded source reconstruction candidate assembly.
- Extended `scripts/build_source_reconstruction_review_package.py` from prep-only skeleton to fail-closed run mode.
- Generated SRM-G1-VIRAL-001 from exact SRA hash and selected OCR evidence hashes.
- Generated SRQ-G1-VIRAL-001 evidence-only precheck.
- Generated G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001 as a candidate package blocked for remediation before human approval.
- Added exact-byte attributes for source reconstruction prep/review evidence.

Next:
- Sol/Terra/critic review of SRM/SRQ/review package/script/tests.
- Remediate visual-QC/overlay-QC blockers before presenting the candidate review package to Bogdan for approval.
- Corrections must go to a separate corrections/remediation artifact, not raw OCR outputs.

Blockers:
- Candidate package is human-review-only and not source acceptance.
- Visual-QC and overlay-QC findings remain blockers for source acceptance and Gate 1 advancement.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T105216Z

- Created: 2026-07-18T10:52:16Z
- Type: documentation
- Summary: Recorded Viral source reconstruction remediation triage.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-REMEDIATE-001 for remediation triage only.
- Added script-backed SRCR-G1-VIRAL-001 remediation report.
- Classified one candidate record as ready for later human review, two as needing overlay verification, two as needing crop/visual remediation, and two visual-QC-only records as separate visual work.
- Added pytest checks for boundary preservation and expected route classification.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-CROP-REMEDIATE-001 before new crop/OCR remediation.
- Keep Bogdan out of source approval until the candidate package is regenerated as human-ready.

Blockers:
- Only one candidate record is ready for later human review.
- Separate crop/overlay remediation authorization is needed before human source approval.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T111226Z

- Created: 2026-07-18T11:12:26Z
- Type: documentation
- Summary: Recorded Viral source reconstruction crop/overlay remediation evidence.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-CROP-REMEDIATE-001 for crop/overlay remediation evidence only.
- Added script-backed SRCO-G1-VIRAL-001 crop/overlay remediation report.
- Created exact crop/overlay reference PNG artifacts from existing rendered crop inputs only.
- Prepared one narrowed contents subcrop for a later separately authorized OCR rerun.
- Added pytest checks for boundary preservation, exact route anchors, artifact hashes, and next authorization narrowing.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001 before any OCR on refined crops.
- Keep Bogdan out of source approval until a later regenerated package is human-ready.

Blockers:
- Human review remains blocked.
- One refined crop still requires a separately authorized OCR rerun before the source reconstruction package can be regenerated.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T112623Z

- Created: 2026-07-18T11:26:23Z
- Type: documentation
- Summary: Recorded Viral source reconstruction refined OCR evidence.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001 for one refined crop OCR rerun only.
- Added script-backed SRFO-G1-VIRAL-001 refined OCR report and raw output manifest.
- Ran OCR only on SRA-G1-VIRAL-001-R003 narrow contents candidate from SRCO-G1-VIRAL-001.
- Bound exact SRCO report hash, source crop hash, refined crop hash, OCR engine identity, and disabled PSM 3/6.
- Added pytest checks for fail-closed authorization, single-target identity, disk hashes, and non-acceptance boundaries.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-REBUILD-001 before rebuilding the source reconstruction package from SRCR/SRCO/SRFO evidence.
- Keep Bogdan out of source approval until the rebuilt package is human-ready after overlay/visual-QC review.

Blockers:
- Human review remains blocked.
- SRFO is exact only for refined-crop visible text; it does not replace the full contents/list region.
- Overlay status for the refined OCR result still needs visual review.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T113050Z

- Created: 2026-07-18T11:30:50Z
- Type: documentation
- Summary: Recorded Viral source reconstruction rebuild evidence.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-REBUILD-001 for a no-OCR rebuild package.
- Added script-backed SRRB-G1-VIRAL-001 from exact SRCO/SRFO report hashes.
- Consolidated candidate, refined OCR, and visual-QC records into a blocked rebuild report.
- Added pytest checks for fail-closed authorization, lineage hashes, crop hashes, no OCR/PDF dependencies, and no automatic human-ready promotion.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001 before any visual/overlay review decisions.
- Keep Bogdan out of source approval until all visual/overlay blockers are resolved and a later package is explicitly marked human-ready.

Blockers:
- Human review remains blocked.
- Six records still require visual, overlay, or full-region replacement decisions.
- SRRB is not source acceptance and does not advance Gate 1.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T120341Z

- Created: 2026-07-18T12:03:41Z
- Type: documentation
- Summary: Recorded Viral source reconstruction visual/overlay review decisions.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001 for visual/overlay review only.
- Added script-backed SRVO-G1-VIRAL-001 visual/overlay review report.
- Closed all six SRRB visual, overlay, and full-region replacement blockers for later human review.
- Produced candidate text for later human review only; candidate text remains not source-accepted.
- Added pytest checks for fail-closed authorization, lineage hashes, disk crop hashes, blocker closure, and no OCR/PDF/raw-output boundary violations.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001 before assembling or presenting a human review package.
- Keep source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, and Gate 1 advancement blocked.

Blockers:
- Visual/overlay blockers are closed for later human review.
- Human review package assembly still needs a separate bounded authorization.
- Source text is not accepted.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T122003Z

- Created: 2026-07-18T12:20:03Z
- Type: documentation
- Summary: Recorded Viral source reconstruction human review package.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001 for human-package assembly only.
- Added script-backed SRHP-G1-VIRAL-001 from exact SRVO-G1-VIRAL-001 hash.
- Produced a human-review markdown package with all seven SRVO records: four candidate-text records and three visual-only exclusions.
- Bound generator script/test hashes, SRVO hash, visual references, and source crop hashes.
- Added pytest checks for fail-closed authorization, exact lineage, all-record coverage, no source/QA acceptance, and no OCR/PDF/raw-output boundary violations.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001 before treating Bogdan review/approval as a source decision.
- Keep QA acceptance, fixtures, translation, proofreading, implementation, and Gate 1 advancement blocked.

Blockers:
- Human package is ready for review, but source text is not accepted.
- Any source approval remains a separate bounded step.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No accepted decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T133656Z

- Created: 2026-07-18T13:36:56Z
- Type: documentation
- Summary: Recorded Viral source reconstruction human source review decisions.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001 for Bogdan page-by-page human source review only.
- Added script-backed SRHR-G1-VIRAL-001 from exact SRHP-G1-VIRAL-001 hash.
- Recorded all seven numbered review decisions with Telegram packet/response message ids.
- Accepted four candidate-text records as source review text and three visual-only exclusions as exclusions.
- Preserved R003 corrected-full-crop resend and Bogdan's semantic heading hint as review metadata.
- Added pytest checks for fail-closed authorization, exact lineage, all decision coverage, corrected packet handling, and no OCR/PDF/raw-output boundary violations.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-QA-001 before any QA acceptance or fixture creation.
- Keep fixtures, translation, proofreading, implementation, renderer/profile acceptance, and Gate 1 advancement blocked.

Blockers:
- QA acceptance remains blocked.
- Fixture creation remains blocked.
- Gate 1 advancement remains blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- Bogdan accepted SRHR-G1-VIRAL-001 source review text for records R002, R003, R004, and R005.
- Bogdan accepted visual-only exclusions for records R001, R006, and R007.

## Documentation Checkpoint: doc-checkpoint-20260718T135919Z

- Created: 2026-07-18T13:59:19Z
- Type: documentation
- Summary: Recorded Viral source reconstruction QA over human-reviewed source text.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-QA-001 for source reconstruction QA only.
- Added script-backed SRQA-G1-VIRAL-001 from exact SRHR report and accepted-text hashes.
- Verified four accepted source-text records and three accepted visual-only exclusions.
- Verified R003 corrected-full-crop note and semantic heading hint are preserved as metadata.
- Added pytest checks for fail-closed authorization, exact lineage, all-record QA coverage, R003 metadata, and no OCR/PDF/raw-output boundary violations.

Next:
- Request BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001 before creating or admitting fixtures from SRQA.
- Keep translation, proofreading, implementation, renderer/profile acceptance, and Gate 1 advancement blocked.

Blockers:
- Fixture creation remains blocked.
- Gate 1 advancement remains blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- SRQA-G1-VIRAL-001 accepts source reconstruction QA for the exact SRHR-G1-VIRAL-001 slice only.

## Documentation Checkpoint: doc-checkpoint-20260718T141808Z

- Created: 2026-07-18T14:18:08Z
- Type: documentation
- Summary: Clarified current planning mode after source reconstruction QA.

Completed:
- Marked the original 2026-07-15 daily plan as completed Gate 1 bootstrap work.
- Recorded that current work proceeds under the global Gate 1 roadmap as a bounded continuation.
- Set the current next bounded action to BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001 if SRQA fragments should become admitted fixtures/downstream input.

Next:
- Decide whether to run fixture admission from SRQA or prepare a Gate 1 review packet later.

Blockers:
- Fixture admission is not yet authorized.
- Gate 1 advancement remains blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No new source/QA decisions supplied.

## Documentation Checkpoint: doc-checkpoint-20260718T142741Z

- Created: 2026-07-18T14:27:41Z
- Type: documentation
- Summary: Recorded Viral source reconstruction fixture admission.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001 for fixture admission only.
- Added script-backed SRFA-G1-VIRAL-001 from exact SRQA report and summary hashes.
- Admitted four positive source-text fixtures and three negative visual-exclusion fixtures as stable downstream test inputs.
- Preserved R003 corrected-full-crop note and Bogdan's semantic heading hint as fixture metadata.
- Added pytest checks for fail-closed authorization, exact lineage, admitted fixture counts, metadata preservation, and no OCR/PDF/raw-output boundary violations.

Next:
- Request BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001 before packaging SRFA for Gate 1 review.
- Keep translation, proofreading, implementation, renderer/profile acceptance, and Gate 1 advancement blocked.

Blockers:
- Gate 1 advancement remains blocked.
- Translation, proofreading, renderer/profile acceptance, and implementation remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- SRFA-G1-VIRAL-001 admits the exact SRQA-G1-VIRAL-001 slice as downstream source reconstruction fixtures only.

## Documentation Checkpoint: doc-checkpoint-20260718T145118Z

- Created: 2026-07-18T14:51:18Z
- Type: documentation
- Summary: Recorded Viral Gate 1 review packet.

Completed:
- Recorded BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001 for packet assembly only.
- Added script-backed G1RP-G1-VIRAL-001 from exact SRFA report, admitted fixtures, and summary hashes.
- Packaged all seven admitted fixtures for Gate 1 review: four positive source-text items and three negative visual-exclusion items.
- Preserved R003 corrected-full-crop note and Bogdan's semantic heading hint as packet metadata.
- Added pytest checks for fail-closed authorization, exact lineage, all-item packet coverage, metadata preservation, and no OCR/PDF/raw-output boundary violations.

Next:
- Request BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001 before any Gate 1 decision or advancement.
- Keep translation, proofreading, implementation, and renderer/profile acceptance blocked.

Blockers:
- Gate 1 advancement remains blocked pending a separate review decision.
- Translation, proofreading, renderer/profile acceptance, and implementation remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- G1RP-G1-VIRAL-001 is ready as a Gate 1 review input only; it does not accept or advance Gate 1.

## Documentation Checkpoint: doc-checkpoint-20260718T150016Z

- Created: 2026-07-18T15:00:16Z
- Type: documentation
- Summary: Recorded Viral Gate 1 review decision brief.

Completed:
- Recorded BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001 for decision-brief preparation only.
- Added script-backed G1RDB-G1-VIRAL-001 from exact G1RP report, manifest, payload, and summary hashes.
- Added accepted protocol revision, G1RP/SRFA/SRQA lineage, and non-waivable checklist coverage.
- Added one numbered Bogdan decision question with accept, hold, reject, and park answer shapes.
- Added pytest checks for fail-closed authorization, exact lineage, numbered question shape, boundary flags, and no OCR/PDF/raw-output boundary violations.
- Recorded Sol/Terra review requirements: Sol OK with checklist requirements; Terra NOT OK until stale Stop Point/deliverables and lineage/wording were corrected.

Next:
- Bogdan review is required before BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001 can record any Gate 1 decision.
- Keep translation, proofreading, implementation, renderer/profile acceptance, and Gate 1 advancement blocked.

Blockers:
- Gate 1 advancement remains blocked pending Bogdan's decision.
- Translation, proofreading, renderer/profile acceptance, and implementation remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- No Gate 1 decision is recorded; G1RDB-G1-VIRAL-001 only prepares the decision brief for Bogdan.

## Documentation Checkpoint: doc-checkpoint-20260718T152814Z

- Created: 2026-07-18T15:28:14Z
- Type: documentation
- Summary: Recorded Viral Gate 1 narrow source reconstruction decision.

Completed:
- Recorded BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001 for Bogdan's message 303 decision only.
- Added script-backed G1RD-G1-VIRAL-001 from exact G1RDB report, JSON, and Markdown hashes.
- Accepted exact G1RP-G1-VIRAL-001 as a narrow Gate 1 source reconstruction evidence slice for seven reviewed records only.
- Preserved accepted_pages_as_complete=false and whole_gate_1_acceptance=false.
- Added pytest checks for fail-closed authorization, exact G1RDB lineage, Bogdan message id, narrow scope, blocked forbidden work, and no OCR/PDF/raw-output boundary violations.

Next:
- Request BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001 before carrying this narrow decision forward.
- Keep page-complete acceptance, whole Gate 1, translation, proofreading, implementation, renderer/profile acceptance, push, OCR, PDF parsing/rendering, and raw OCR mutation blocked.

Blockers:
- Page-complete acceptance remains blocked.
- Whole Gate 1 acceptance remains blocked.
- Translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- Bogdan accepted only exact G1RP-G1-VIRAL-001 as a seven-record Gate 1 source reconstruction evidence slice.

## Documentation Checkpoint: doc-checkpoint-20260718T163725Z

- Created: 2026-07-18T16:37:25Z
- Type: documentation
- Summary: Recorded Viral Gate 1 narrow source reconstruction evidence rollup.

Completed:
- Recorded BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001 for rollup only.
- Added script-backed G1SRER-G1-VIRAL-001 from exact G1RD report, record, Markdown, and summary hashes.
- Carried the seven-record Gate 1 source reconstruction evidence slice forward as status input.
- Preserved accepted_pages_as_complete=false, page_complete_acceptance=false, and whole_gate_1_acceptance=false.
- Added pytest checks for fail-closed authorization, exact G1RD lineage, narrow scope preservation, blocked forbidden work, and no OCR/PDF/raw-output boundary violations.

Next:
- Build a higher-level Gate 1 status packet only under a separate bounded authorization, or continue source reconstruction with a next-slice authorization.
- Keep page-complete acceptance, whole Gate 1, translation, proofreading, implementation, renderer/profile acceptance, push, OCR, PDF parsing/rendering, and raw OCR mutation blocked.

Blockers:
- Page-complete acceptance remains blocked.
- Whole Gate 1 acceptance remains blocked.
- Translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- G1SRER-G1-VIRAL-001 carries only the exact G1RD-G1-VIRAL-001 seven-record source reconstruction evidence slice forward.

## Documentation Checkpoint: doc-checkpoint-20260718T174435Z

- Created: 2026-07-18T17:44:35Z
- Type: documentation
- Summary: Recorded Viral Gate 1 status packet for the narrow source reconstruction slice.

Completed:
- Recorded BA-G1-VIRAL-GATE-1-STATUS-PACKET-001 for status packaging only.
- Added script-backed G1SP-G1-VIRAL-001 from exact G1SRER report, manifest, payload, and summary hashes.
- Summarized current Gate 1 state as one accepted/rolled-up seven-record source reconstruction slice plus pending work.
- Preserved accepted_pages_as_complete=false, page_complete_acceptance=false, whole_gate_1_acceptance=false, and new_gate_1_advancement_created=false.
- Added pytest checks for fail-closed authorization, exact G1SRER lineage, narrow-slice summary, pending broader work, and no OCR/PDF/raw-output boundary violations.

Next:
- Continue source reconstruction with a separately authorized next slice, or review this status packet without treating it as new Gate 1 advancement.
- Keep page-complete acceptance, whole Gate 1, source profile acceptance, translation, proofreading, renderer/profile acceptance, push, OCR, PDF parsing/rendering, and raw OCR mutation blocked.

Blockers:
- Only one seven-record source reconstruction slice is accepted/rolled up.
- Page-complete acceptance remains blocked.
- Whole Gate 1 acceptance remains blocked.
- Translation, proofreading, renderer/profile acceptance, implementation, and push remain blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- G1SP-G1-VIRAL-001 summarizes only the exact G1SRER-G1-VIRAL-001 seven-record source reconstruction evidence rollup and does not create new Gate 1 advancement.

## Documentation Checkpoint: doc-checkpoint-20260718T182756Z

- Created: 2026-07-18T18:27:56Z
- Type: documentation
- Summary: Prepared Viral page 002 source reconstruction next-slice review packet.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001 for one page-002 next-slice review packet only.
- Added script-backed SRNS-G1-VIRAL-002 from exact G1SP status-packet hashes, PRM-G1-VIRAL-001 region hints, and existing page_002.png.
- Created two crop references for PRM-G1-VIRAL-001-P002-R01 and PRM-G1-VIRAL-001-P002-R02.
- Added a numbered human review packet with answer shapes for Bogdan.
- Added pytest checks for fail-closed authorization, exact lineage, two-record scope, crop hashes, no candidate text, no acceptance, and no OCR/PDF/render/raw-output boundary violations.

Next:
- Present page_002 original plus the two SRNS crop references to Bogdan and record his numbered decisions only under a separate bounded human-review authorization.
- Keep page-002 complete acceptance, whole Gate 1, QA, fixtures, translation, proofreading, renderer/profile acceptance, implementation, and push blocked.

Blockers:
- SRNS-G1-VIRAL-002 is ready for Bogdan review but creates no candidate text or source acceptance.
- Page 002 is not accepted as complete.
- Whole Gate 1 remains blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- None. SRNS-G1-VIRAL-002 is review input only.

## Documentation Checkpoint: doc-checkpoint-20260718T195540Z

- Created: 2026-07-18T19:55:40Z
- Type: documentation
- Summary: Prepared Viral page 002 assisted source reconstruction draft for Bogdan verification.

Completed:
- Recorded BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-001 for a page-002 assisted draft only.
- Captured Bogdan's route decisions from messages 351 and 356: both page-002 regions contain text, but the text is too long for manual transcription.
- Added corrected split crops for credits/play-testers and lower special-thanks/legal text.
- Added assisted draft text for Bogdan verification only.
- Added pytest checks for fail-closed authorization, SRNS lineage, corrected crop hashes, draft text hashes, and no source/QA/fixture/Gate acceptance.

Next:
- Present SRAD-G1-VIRAL-002 assisted draft text and corrected crops to Bogdan for numbered verification under a separate bounded authorization.
- Keep page-002 complete acceptance, source acceptance, QA, fixtures, whole Gate 1, translation, proofreading, renderer/profile acceptance, implementation, and push blocked.

Blockers:
- At this checkpoint, SRAD-G1-VIRAL-002 still required Bogdan verification before any source acceptance.
- Page 002 is not accepted as complete.
- Whole Gate 1 remains blocked.

Roadmap nodes:
- phase-0
- gate-01-source-profile
- gate-01-qualification-protocol
- gate-01-pre-ocr-map-model

Accepted decisions:
- None. SRAD-G1-VIRAL-002 is assisted draft input only.

## Documentation Checkpoint: doc-checkpoint-20260718T202535Z

Timestamp: 2026-07-18T20:25:35Z

Scope:

- Recorded `BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-HUMAN-VERIFY-001`
  as consumed by `SRADV-G1-VIRAL-002`.
- `SRADV-G1-VIRAL-002` records Bogdan Telegram message `377`: `1 ок`, `2 ок`,
  headings ignored, text OK.
- This verifies two assisted page-002 draft text records against corrected
  crops only.

Guardrails:

- No source acceptance, QA acceptance, fixture admission, Gate 1 advancement,
  page-complete acceptance, whole-Gate acceptance, OCR execution, PDF
  parsing/rendering, raw OCR mutation, translation, proofreading,
  renderer/profile acceptance, implementation, or push.

Next:

- `BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-QA-001` can QA this
  verification if authorized.

Open blockers:

- Page 002 is not accepted as complete.
- Source acceptance, QA, fixtures, whole Gate 1, translation, proofreading,
  renderer/profile acceptance, implementation, and push remain blocked.

## Documentation Checkpoint: doc-checkpoint-20260718T210754Z

Timestamp: 2026-07-18T21:07:54Z

Scope:

- Added `page_002_qa_structure_evaluation_packet.md` for Bogdan review.
- Packet SHA-256:
  `F261CB0035BB588A5F347A0BE30C7E7E0E8910BE505E3C913357A539E93F11BA`.
- The packet consolidates the next path after `SRADV-G1-VIRAL-002`:
  `SRADQ` QA, `SRSS` structure/semantics, structure QA, then a separate
  source acceptance decision if authorized.
- The packet includes proposed semantic roles, heading levels, and presentation
  flags such as bold, italic, underline, centered, small-caps, and font scale.

Guardrails:

- The packet is planning/evaluation material only.
- It does not accept source text, page 002 as complete, whole Gate 1, QA,
  fixtures, structure, translation, proofreading, renderer/profile behavior,
  implementation, or push.

Next:

- Bogdan reviews the packet and chooses whether to run `SRADQ` first as
  recommended.

## Documentation Checkpoint: doc-checkpoint-20260718T214429Z

Timestamp: 2026-07-18T21:44:29Z

Scope:

- Bogdan Telegram message `419` authorized running the page-002 plan 1-6 end to
  end and preparing the next review block without stopping for intermediate
  approvals.
- `P002C-G1-VIRAL-002` records `SRADQ-G1-VIRAL-002`,
  `SRSS-G1-VIRAL-002`, `SRSSQ-G1-VIRAL-002`, `SRSA-G1-VIRAL-002`, and
  `G1SRER-G1-VIRAL-002`.
- Exactly two page-002 records are now accepted as a narrow source
  reconstruction slice. Page 002 remains incomplete and whole Gate 1 remains
  unaccepted.
- `SRCR-G1-VIRAL-003` is ready for Bogdan review as a remediated draft
  page-003 packet with visual transcription draft text, structure/semantics,
  and crop references after Bogdan reported the initial crop cut text.
- Report SHA-256:
  `A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F`.
- Manifest SHA-256:
  `8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6`.
- Next review packet SHA-256:
  `81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF`.

Guardrails:

- The page-003 text layer is a remediated draft for review after a crop-cut
  blocker; it is not accepted source text and still requires Bogdan review.
- Bogdan message `437` verifies the remediated draft packet as `1 ок`, `2 ок`;
  that creates `SRCRV-G1-VIRAL-003` only, not source acceptance.
- No fixture admission, page-complete acceptance, whole-Gate acceptance,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push is authorized.

Next:

- Next bounded step can QA `SRCRV-G1-VIRAL-003` and then, if authorized, make a
  separate source acceptance decision for the page-003 records.

## Documentation Checkpoint: doc-checkpoint-20260718T223926Z

Timestamp: 2026-07-18T22:39:26Z

Scope:

- Bogdan Telegram message `441` authorized committing the crop remediation,
  then running page-003 QA/source acceptance and crop guardrail work.
- `P003A-G1-VIRAL-003` records `SRCRQ-G1-VIRAL-003`,
  `SRCG-G1-VIRAL-003`, `SRSA-G1-VIRAL-003`, and
  `G1SRER-G1-VIRAL-003`.
- Exactly two page-003 records are now accepted as a narrow source
  reconstruction slice. Page 003 remains incomplete and whole Gate 1 remains
  unaccepted.
- Report SHA-256:
  `9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B`.
- Manifest SHA-256:
  `F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87`.
- Summary SHA-256:
  `860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2`.

Guardrails:

- `SRCG-G1-VIRAL-003` consumes predecessor global crop layout evidence
  `SRCG-GLOBAL-CROP-BOX-LAYOUT-001`: approved boxes, crop overlap, and
  too-small gutters are blockers.
- No fixture admission, page-complete acceptance, whole-Gate acceptance,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push is authorized.

## Documentation Checkpoint: doc-checkpoint-20260719T162334Z

Timestamp: 2026-07-19T16:23:34Z

Scope:

- Bogdan Telegram message `514` authorized running plan steps 1-6 and committing
  the result.
- `BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004` records exact authority, inputs,
  outputs, limits, and invalidation for the page-004 review packet.
- `SRCR-G1-VIRAL-004` prepares draft text, structure/semantics, and two padded
  crop references for Bogdan review only.
- `PRM-G1-VIRAL-001-P004-R01` is context-only because it contains the
  title/body regions and would overlap peer crop records under the global crop
  layout guardrail.

Hashes:

- Report SHA-256:
  `C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A`.
- Manifest SHA-256:
  `30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4`.
- Human review packet SHA-256:
  `1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446`.

Guardrails:

- `SRCG-GLOBAL-CROP-BOX-LAYOUT-001` passed for the two peer crop records.
- No source acceptance, QA acceptance, fixture admission, page-complete
  acceptance, whole-Gate acceptance, translation, proofreading,
  renderer/profile acceptance, implementation, or push is authorized.

## Documentation Checkpoint: doc-checkpoint-20260719T174526Z

Timestamp: 2026-07-19T17:45:26Z

Scope:

- Bogdan Telegram message `523` recorded `1 ok / 2 ok` for the two
  `SRCR-G1-VIRAL-004` review records.
- `BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004-HUMAN-VERIFY-001` records exact
  authority, inputs, outputs, limits, and invalidation for the human
  verification layer.
- `SRCRV-G1-VIRAL-004` verifies the two draft page-004 review records only.

Hashes:

- Verification report SHA-256:
  `95041F808A1C2F44A417245BF3E25318C9BDE36183CCE7C4E372DF9363812FBA`.
- Verification manifest SHA-256:
  `21B3CE0135D4D8CF09C394C192D7976766DA9DA1E55DE5F9B3FE240380CC0AB0`.
- Verification summary SHA-256:
  `F342D7DA0CBB7245812B8B3291F2C5585D880DA67D6C24DCAFEC4FF8B86D9011`.

Guardrails:

- Verification consumes exact `SRCR-G1-VIRAL-004` report, manifest, and human
  review packet hashes.
- No source acceptance, QA acceptance, fixture admission, page-complete
  acceptance, whole-Gate acceptance, translation, proofreading,
  renderer/profile acceptance, implementation, or push is authorized.

## Documentation Checkpoint: doc-checkpoint-20260719T182626Z

Timestamp: 2026-07-19T18:26:26Z

Scope:

- `BA-G1-VIRAL-P004-QA-SOURCE-ACCEPTANCE-001` consumed exact
  `SRCR-G1-VIRAL-004` and `SRCRV-G1-VIRAL-004` predecessor evidence.
- `P004A-G1-VIRAL-004` records page-004 QA, crop guardrail consumption, narrow
  two-record source acceptance, and a fourth source reconstruction rollup.
- Accepted source reconstruction records moved from 11 to 13.

Guardrails:

- Page 004 is not accepted as complete.
- Page 002 and page 003 are not accepted as complete.
- Whole Gate 1, fixture admission, translation, proofreading,
  renderer/profile acceptance, implementation, and push remain blocked.

## Documentation Checkpoint: doc-checkpoint-20260719T201558Z

Timestamp: 2026-07-19T20:15:58Z

Scope:

- `BA-G1-VIRAL-PAGE-COMPLETENESS-TRIAGE-001` produced `PGCT-G1-VIRAL-001`.
- The packet classifies selected pages 1-20 for the next human decision:
  pages 002/003 are ready for later separate page-complete review packets,
  page 004 is held pending a context-only decision for the full tilted inset,
  pages 001/005/006 remain incomplete, and pages 007-020 remain unstarted for
  source-reconstruction acceptance.
- This is the packet to show Bogdan before any page-complete action is chosen.

Guardrails:

- This checkpoint is triage/status only.
- No page-complete acceptance, whole Gate 1 acceptance, fixture admission,
  source acceptance, translation, proofreading, renderer/profile acceptance,
  implementation, push, OCR/PDF/render/raw mutation, or new source slice is
  created.

## Documentation Checkpoint: doc-checkpoint-20260719T212402Z

Timestamp: 2026-07-19T21:24:02Z

Scope:

- Added draft page-map readiness indicators to `pre_ocr_mapping_model.md`.
- Added vocabulary for `readiness`, `coverage_summary`,
  `page_complete_candidate`, and `page_complete_accepted`.
- Added declared future acceptance-matrix and fixture-obligation links for
  page-complete readiness without creating executable fixtures.
- Page 002 is documented as the current example: credits block plus boxed
  legal/footer block are the two known required in-scope text blocks; both have
  accepted source records, but page 002 still needs a separate page-complete
  review packet.

Guardrails:

- Readiness and coverage percentages are advisory routing signals only.
- OCR/text fidelity indicators may use only already-authorized existing
  artifacts and must not run OCR, rerun OCR, extract PDF text-layer payloads,
  edit raw OCR output, or create accepted source text.
- No page-complete acceptance, whole Gate 1 acceptance, fixture admission,
  source acceptance, translation, proofreading, renderer/profile acceptance,
  implementation, push, OCR/PDF/render/raw mutation, or new source slice is
  created.

## Documentation Checkpoint: doc-checkpoint-20260719T215028Z

Timestamp: 2026-07-19T21:50:28Z

Scope:

- Recorded Bogdan's correction that page 002 is only the pilot/proving case,
  not the end architecture.
- The next implementation plan is a reusable `page_map` readiness pipeline:
  generic builder, page-specific profiles, stable readiness JSON/Markdown
  outputs, content-type-specific checks, and page 002 as the first bounded
  profile/output.
- The work is now intended to be visible as a Gate 1 roadmap dependency and as
  a hierarchy subcomponent, rather than only as checkpoint narrative.
- The planned pilot should prove the reusable path for each later page:
  expected block inventory, explicit `none` states, advisory coverage,
  existing-artifact-only fidelity indicators, anchors, reading order,
  overlay/nesting declarations, blockers/open questions, and human-facing
  decision packet generation.

Guardrails:

- Planning/status only; no implementation is created by this checkpoint.
- Page 002 readiness remains separate from page-complete acceptance.
- No OCR, OCR rerun, render, PDF parsing, PDF text-layer extraction, raw
  artifact mutation, fixture admission, whole Gate 1 acceptance, translation,
  proofreading, renderer/profile acceptance, implementation, push, or new
  source slice is authorized.

## Documentation Checkpoint: doc-checkpoint-20260719T215804Z

Timestamp: 2026-07-19T21:58:04Z

Scope:

- Promoted the universal page-map readiness pipeline into the shared Gate 1
  roadmap and hierarchy.
- `roadmap.yaml` now tracks `gate-01-page-map-readiness-pipeline` as a planned
  dependency between the pre-OCR map model and the source-profile decision.
- `phase_gate_component_hierarchy.md` now records
  `SC-PAGE_MAP_READINESS` and its planned parameters for generic builder,
  page-specific profiles, advisory coverage, existing-artifact-only fidelity
  inputs, the page 002 pilot, and human-facing packet output.

Guardrails:

- This is roadmap/hierarchy integration only; it creates no implementation
  artifact.
- No OCR, OCR rerun, render, PDF parsing, PDF text-layer extraction, raw
  artifact mutation, page-complete acceptance, whole Gate 1 acceptance, fixture
  admission, translation, proofreading, renderer/profile acceptance,
  implementation, push, or new source slice is authorized.

## Documentation Checkpoint: doc-checkpoint-20260723T220255Z

Timestamp: 2026-07-23T22:02:55Z

Scope:

- `BA-G1-VIRAL-PAGE-MAP-READINESS-P004-001` consumed exact
  `P004A-G1-VIRAL-004` and `P004COD-G1-VIRAL-001`.
- `PMRP-G1-VIRAL-P004-001` records page 004 readiness through the reusable
  `page_map` pipeline: two expected text blocks ready, one confirmed
  context-only inset, no blockers, no open questions, and advisory coverage
  only.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P004-001` consumed exact
  `PMRP-G1-VIRAL-P004-001`.
- `PCRP-G1-VIRAL-P004-001` prepares a separate page-complete review packet
  with page image, two text crops, and OCR/block text markdown review assets
  for Bogdan's explicit page 004 decision.

Guardrails:

- The readiness packet and review packet create no page-complete acceptance.
- Page 004 is not accepted as complete.
- Whole Gate 1 is not accepted.
- No fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

Next:

- After Sol/Terra gate, present the page 004 review assets to Bogdan and ask
  only for `page 004 complete ok` or `hold page 004: <reason>`.

## Documentation Checkpoint: doc-checkpoint-20260723T224528Z

Timestamp: 2026-07-23T22:45:28Z

Scope:

- Bogdan gave the explicit decision `page 004 complete ok`.
- `BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P004-001` consumed exact
  `PCRP-G1-VIRAL-P004-001`.
- `P004PCA-G1-VIRAL-001` records page 004 as complete accepted only.

Guardrails:

- Only page 004 is accepted as complete.
- Whole Gate 1 is not accepted.
- No fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260723T231200Z

Timestamp: 2026-07-23T23:12:00Z

Scope:

- `BA-G1-VIRAL-PAGE-MAP-READINESS-P005-001` consumed exact page 005 source
  evidence from `SRHR-G1-VIRAL-001`, `SRQA-G1-VIRAL-001`, and
  `SRFA-G1-VIRAL-001`, plus `PRM-G1-VIRAL-001` region hints.
- `PMRP-G1-VIRAL-P005-001` records page 005 readiness through the reusable
  `page_map` pipeline: contents heading and contents/list entry group are
  ready, the margin page marker is visual-only, no blockers or open questions
  remain, and coverage is advisory only.

Guardrails:

- Readiness only; page 005 is not accepted as complete.
- Whole Gate 1 is not accepted.
- No new fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260723T232600Z

Timestamp: 2026-07-23T23:26:00Z

Scope:

- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-001` consumed exact
  `PMRP-G1-VIRAL-P005-001`.
- `PCRP-G1-VIRAL-P005-001` prepares a separate page-complete review packet for
  Bogdan's explicit page 005 decision, with source page image, two crop anchors,
  and OCR/block text markdown packaged as review assets.
- Bogdan held `PCRP-G1-VIRAL-P005-001` because the review crops did not cover
  all page content sufficiently; the R003/contents-entry crop cuts off text,
  and a superseding page 005 review packet needs broader/more crops.
- `build_page_complete_review.py` now enforces visual proof checks by strictly comparing
  each block-crop image dimension with the readiness `box_px` dimensions. The
  regenerated P005 packet is `blocked` because `P005-B001` packages a 860x260
  crop for a declared 750x280 block and `P005-B002` packages a 560x235 crop
  for a declared 2050x2300 block.

Guardrails:

- Review packet only; page 005 is not accepted as complete.
- Whole Gate 1 is not accepted.
- No new fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260724T001551Z

Timestamp: 2026-07-24T00:15:51Z

Scope:

- Bogdan approved `PCRP-G1-VIRAL-P005-002` after the first page 005 packet was
  held for insufficient crop coverage.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-002` consumed exact
  `PMRP-G1-VIRAL-P005-001`.
- `build_page_complete_review.py` now generates superseding review block crops
  from the declared readiness `box_px` on the existing `page_005.png`.
- `PCRP-G1-VIRAL-P005-002` packages the page image, full declared crops for
  `P005-B001` and `P005-B002`, and OCR/block text markdown.
- Visual proof passes strict `1.00` width and height ratios for both page 005
  blocks.

Guardrails:

- Review packet only; page 005 is not accepted as complete.
- Whole Gate 1 is not accepted.
- No new fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

Next:

- Superseded by readable crop packet `PCRP-G1-VIRAL-P005-003`.

## Documentation Checkpoint: doc-checkpoint-20260724T004358Z

Timestamp: 2026-07-24T00:43:58Z

Scope:

- Bogdan requested a dry run without intermediate Sol/Terra stops until the
  page 005 packet contained the right human-review crops: title only, left
  column, and right column.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-003` consumed exact
  `PMRP-G1-VIRAL-P005-001`.
- `build_page_complete_review.py` now generates readable review crops from
  `page_005.png` for page 005: title-only, left-column, and right-column.
- `PCRP-G1-VIRAL-P005-003` packages the page image, those three readable crops,
  and `page_005_ocr_verified_text_map.md` with crop-matched text and heading
  depth/style notes.
- Human-review crop edge checks pass, so the crop set is framed for readable
  manual review rather than only matching declared `box_px` dimensions.

Guardrails:

- Review packet only; page 005 is not accepted as complete by
  `PCRP-G1-VIRAL-P005-003`.
- Whole Gate 1 is not accepted.
- No new fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

Next:

- Refresh page 005 against the current semantic-map page-complete contract
  before acceptance routing.

## Documentation Checkpoint: doc-checkpoint-20260724T181439Z

Timestamp: 2026-07-24T18:14:39Z

Scope:

- Bogdan explicitly said "ок делай 5 сразу и коммит" after the orchestrator
  confirmed `PCRP-G1-VIRAL-P005-003` was a readable review packet but not an
  acceptance record.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-004` consumes
  `PCRP-G1-VIRAL-P005-003` as the compatibility-refresh predecessor.
- `PCRP-G1-VIRAL-P005-004` adds canonical semantic map JSON/Markdown,
  projection validation, and inventory reconciliation for page 005.
- `P005PCA-G1-VIRAL-001` accepts page 005 as complete only.

Evidence:

- `PCRP-G1-VIRAL-P005-004`: 2/2 ready blocks, 74 semantic units, valid
  semantic validation, valid Markdown projection, valid inventory
  reconciliation, and zero structural findings.
- `P005PCA-G1-VIRAL-001`: accepted pages as complete = [`005`] only.

Guardrails:

- Page 005 only is accepted as complete.
- Whole Gate 1 is not accepted.
- No fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260724T123031Z

Timestamp: 2026-07-24T12:30:31Z

Scope:

- Execute step 9 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  add regression coverage for P005/P006 patterns and synthetic mixed-layout
  semantic structures.

Implemented Plan:

1. Extend taxonomy with `page_ref` semantic units for TOC-like page-reference
   rows.
2. Allow represented regions to be covered by bounded `in_scope_text`,
   `visual_only`, and `context_only` units according to expected unit types.
3. Allow visual/context-only decisions to carry visual/context scoped units
   while still blocking in-scope text leakage.
4. Add synthetic TOC row/page-reference regression coverage.
5. Add synthetic art+caption, table row/cell, callout/sidebar/card/stat,
   page-marker, context-inset, and unknown-unsupported regression coverage.
6. Add topology-flattening blockers for table rows/cells, stat labels/values,
   and callout/sidebar/card containers without linked child content.

Guardrails:

- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Generate the superseding P006 review packet only after Step 10 contract sync
  passes Sol/Terra review.

## Documentation Checkpoint: doc-checkpoint-20260724T124724Z

Timestamp: 2026-07-24T12:47:24Z

Scope:

- Execute step 10 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  update readiness/page-complete contracts so semantic structural criteria,
  non-waivable structure loss, and semantic-map readiness vocabulary are
  first-class gates.

Implemented Plan:

1. Add `semantic_map_ready`, `semantic_map_blocked`, and
   `semantic_unit_review_only` vocabulary to the readiness and page-complete
   review contract.
2. State that canonical semantic-map JSON is authoritative and Markdown maps
   are projection-only review surfaces.
3. Require semantic validation, Markdown projection validation, page inventory
   reconciliation, and structural finding roll-up before report status,
   manifest/status sync, and decision-option filtering.
4. Map semantic structure loss to non-waivable acceptance/finding classes:
   collapsed units, missing headings, flattened quotes, invalid heading levels,
   table/card/stat/callout/sidebar topology loss, missing captions/page
   markers, unsupported regions, stale lineage, and payload leakage.
5. Update the Core 0.1 acceptance matrix with semantic-map gate criteria for
   page-complete review packets.

Guardrails:

- This step is contract/documentation sync only.
- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Send `PCRP-G1-VIRAL-P006-002` through Sol/Terra review, then show Bogdan the
  human-facing packet and review assets.

## Documentation Checkpoint: doc-checkpoint-20260724T144302Z

Timestamp: 2026-07-24T14:43:02Z

Scope:

- Record Bogdan's page 006 complete decision after review of
  `PCRP-G1-VIRAL-P006-002`.
- Create `P006PCA-G1-VIRAL-001` as a page-complete acceptance record for page
  006 only.

Implemented Plan:

1. Added bounded authorization `BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P006-001`.
2. Added fail-closed acceptance profile and tests for page 006.
3. Generated the page 006 acceptance report, record, summary, and manifest.
4. Updated status, roadmap, plan, and context surfaces to record page 006
   page-complete acceptance only.
5. Removed stale embedded roadmap fallback state from `roadmap_viewer.html`;
   the viewer now prompts for canonical `roadmap.yaml` when auto-load fails.

Guardrails:

- Only page 006 is accepted as complete.
- Page 005 remains pending Bogdan page-complete decision.
- Whole Gate 1 is not accepted.
- No fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260724T130457Z

Timestamp: 2026-07-24T13:04:57Z

Scope:

- Execute step 11 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  generate superseding review packet `PCRP-G1-VIRAL-P006-002` after hardening.

Implemented Plan:

1. Add bounded authorization `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P006-002`.
2. Add profile `006-002` without the P006-001 post-review hold blocker.
3. Correct P006 semantic spans: `Introduction=h2`, separate `Summary`, quote
   unit without heading level, separate `Overview`, full body text units, and
   right-column continuation link.
4. Generate OCR/verified text map as metadata rows plus fenced full-text blocks.
5. Generate canonical semantic JSON and Markdown projection artifacts.
6. Add regression tests for P006-002 readiness, no acceptance creation,
   separated semantic units, continuation link, and safe text-map projection.

Guardrails:

- This step creates a review packet only.
- Page 006 is not accepted as complete unless Bogdan later sends the explicit
  `page 006 complete ok` decision.
- This step does not accept whole Gate 1, create fixtures, mutate source
  acceptance, run OCR, parse/extract PDF text, rerender, mutate raw artifacts,
  translate, proofread, accept renderer/profile behavior, or push.

Next:

- Sol/Terra review `PCRP-G1-VIRAL-P006-002`; if clean, send the packet and
  review assets to Bogdan for the page-complete decision.

## Documentation Checkpoint: doc-checkpoint-20260724T115827Z

Timestamp: 2026-07-24T11:58:27Z

Scope:

- Execute step 8 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  strengthen negative tests and structural guard predicates for non-waivable
  semantic-map findings.

Implemented Plan:

1. Add validator finding `style_is_block_role` when display style contains a
   source/page block role instead of a typography/display role.
2. Add reconciliation findings `collapsed_units`, `missing_expected_heading`,
   and `quote_flattened` for represented regions whose expected semantic units
   are swallowed into one body unit.
3. Add negative tests for display-style leakage.
4. Add negative tests for collapsed heading/quote/body regions.
5. Strengthen P006-001 report tests so structural findings still suppress
   `accept_page_006`/complete-ok routing.

Guardrails:

- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Add generic mixed-layout regression fixtures for P005/P006 patterns and
  synthetic art+caption, table, callout/sidebar, stat/card, page marker, and
  unknown unsupported regions.

## Documentation Checkpoint: doc-checkpoint-20260724T111541Z

Timestamp: 2026-07-24T11:15:41Z

Scope:

- Execute step 7 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  wire page-inventory reconciliation into generated report readiness gating.

Implemented Plan:

1. Derive page inventory from readiness `block_inventory` plus declared
   context-only regions.
2. Load semantic units from the canonical semantic map JSON artifact instead of
   copying semantic payload into status rollups.
3. Run `reconcile_page_inventory` during `build_report`.
4. Add report field `inventory_reconciliation`.
5. Add `inventory_reconciliation_blocker` when reconciliation is readiness
   blocked.
6. Render inventory reconciliation state into the human packet and summary.
7. Add regression tests that P006-001 inventory reconciliation is valid while
   semantic validation still blocks on `invalid_heading_level`.

Guardrails:

- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Expand structural finding taxonomy and generic mixed-layout regression
  fixtures for art+caption, tables, callouts/sidebars, stat/card blocks,
  page markers, and unknown unsupported regions.

## Documentation Checkpoint: doc-checkpoint-20260724T104904Z

Timestamp: 2026-07-24T10:49:04Z

Scope:

- Execute step 6 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  promote semantic validation and Markdown projection validation into report
  status and decision-option gating.

Implemented Plan:

1. Collect semantic map attachment validation state in `build_report`.
2. Add report fields `semantic_units_validated`, `semantic_validation`,
   `markdown_projection_validation`, and `structural_findings`.
3. Add `semantic_validation_blocker` when semantic validation is readiness
   blocked.
4. Add `markdown_projection_validation_blocker` when Markdown projection
   validation is readiness blocked.
5. Render semantic validation state and structural findings into the human
   packet.
6. Render semantic validation/finding counts into the summary.
7. Add regression tests that P006-001 report-level status includes the
   semantic validation blocker and still creates no acceptance.

Guardrails:

- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Wire page-inventory reconciliation into generated packet gating, then add
  generic mixed-layout regression fixtures.

## Documentation Checkpoint: doc-checkpoint-20260724T090922Z

Timestamp: 2026-07-24T09:09:22Z

Scope:

- Execute step 5 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  wire the builder to generate semantic map JSON/Markdown artifacts from inline
  readiness spans.
- Keep P006-001 held/blocked and avoid generating P006-002.

Implemented Plan:

1. Add `generated_semantic_map_attachment` profile metadata for P006-001.
2. Generate stable semantic unit IDs from inline readiness block/span order.
3. Map span semantic roles to unit type, display style, heading level, source
   role, block role, source region IDs, crop IDs, source block IDs, span IDs,
   and evidence predecessors.
4. Materialize canonical JSON and Markdown projection artifacts under
   `review_assets`.
5. Include semantic and projection validation state on the report attachments.
6. Keep the legacy OCR/verified text map unchanged as blocked negative
   evidence.
7. Add regression tests that P006-001 packages the semantic map artifacts
   without creating acceptance or generating P006-002.

Guardrails:

- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Promote semantic validation/reconciliation into full structural readiness
  gating before report status, packet text, manifest hashes, and decision
  options.

## Documentation Checkpoint: doc-checkpoint-20260724T085022Z

Timestamp: 2026-07-24T08:50:22Z

Scope:

- Execute step 4 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  add filling rules and page-inventory reconciliation predicates.
- Keep this below builder integration so later generated packets can fail
  closed using the same predicates.

Implemented Plan:

1. Add explicit `REGION_DECISIONS`: represented, absent, context-only,
   visual-only, excluded, unknown, and blocked.
2. Add `reconcile_page_inventory` to balance observed/expected regions against
   semantic units through `source_region_ids`.
3. Block represented regions without classified `in_scope_text` units.
4. Block regions with missing decisions.
5. Block unknown/blocked regions unless they carry an unknown/unclassified
   bounded semantic unit.
6. Block unknown/blocked regions that also carry classified `in_scope_text`
   units.
7. Block semantic units that point at regions outside the inventory.
8. Block missing expected unit types for represented regions.
9. Add focused regression tests for represented/context regions, missing units,
   missing decisions, unknown fallback, external region refs, and expected unit
   type coverage.

Guardrails:

- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Refactor the page-complete review builder to derive semantic units and run
  validation/reconciliation before report status, packet text, manifest hashes,
  and decision options.

## Documentation Checkpoint: doc-checkpoint-20260724T082058Z

Timestamp: 2026-07-24T08:20:58Z

Scope:

- Execute step 3 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  add canonical semantic map JSON and human Markdown projection primitives.
- Keep this step below builder integration; the legacy P006-001 text map stays
  blocked evidence until a superseding packet is generated later.

Implemented Plan:

1. Add `semantic_map_document` as the canonical JSON-like semantic-map document
   builder.
2. Include validation results, structural findings, and `Not Evidence For`
   boundaries in the canonical map document.
3. Add `build_semantic_map_markdown` as a projection only: metadata summary
   table first, then stable per-unit fenced text blocks.
4. Add table-cell escaping and metadata-only row generation so long prose does
   not enter Markdown table cells.
5. Add `validate_semantic_map_markdown` to check row/column integrity, reject
   long prose table cells, ignore table-like content inside fenced unit text,
   and enforce one well-formed fenced text block per unit inside the Unit Text
   section.
6. Add focused regression tests for canonical JSON, Markdown projection shape,
   full-text block placement, Not Evidence For boundaries, and bad table
   rejection, including source text containing pipes or Markdown fence
   delimiters.

Guardrails:

- This step does not create P006-002, accept page 006, accept whole Gate 1,
  create fixtures, mutate source acceptance, run OCR, parse/extract PDF text,
  rerender, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, or push.

Next:

- Add filling rules and reconciliation predicates, then wire semantic-map
  generation into the page-complete review builder.

## Documentation Checkpoint: doc-checkpoint-20260724T080720Z

Timestamp: 2026-07-24T08:07:20Z

Scope:

- Execute step 2 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  introduce reusable semantic-unit schema/taxonomy primitives and a validator
  entrypoint.
- Keep this step below the template/builder integration layer so later steps
  can wire the schema into canonical JSON and Markdown projection without
  changing the vocabulary underneath.

Implemented Plan:

1. Add `scripts/page_review_semantic_units.py`.
2. Define schema/taxonomy versions and controlled registries for unit types,
   unit scopes, display styles, source roles, block roles, text source states,
   and review states.
3. Separate `unit_type` from heading level and display style; only heading
   units may carry `heading_level`.
4. Require positive reading order, list cardinality for region/crop/span/
   predecessor references, non-empty region/crop/predecessor evidence, unique
   contiguous reading order, unique unit ids, and valid continuation/container
   links.
5. Require unknown/unsupported units to remain `unknown` or `blocked` until
   classified.
6. Add focused tests for valid heading units, quote heading-level rejection,
   unknown fallback blocking, empty evidence references, duplicate reading
   order, mistyped links, and broken continuation links.

Guardrails:

- This step does not run OCR, parse/extract PDF text, rerender, mutate raw
  artifacts, create fixture admission, mutate source acceptance, or create any
  page-complete/whole-Gate acceptance.
- P006-002 remains blocked until template, builder, validator integration, and
  regression coverage are complete and reviewed.

Next:

- Integrate semantic units into canonical report JSON and human map projection
  so Markdown becomes a projection rather than the source of truth.

## Documentation Checkpoint: doc-checkpoint-20260724T075333Z

Timestamp: 2026-07-24T07:53:33Z

Scope:

- Execute step 1 of `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`:
  convert the Bogdan hold on `PCRP-G1-VIRAL-P006-001` into
  machine-readable report/packet/status routing.
- Keep the change narrow: no semantic-unit schema, validator, template rewrite,
  or P006-002 generation in this step.

Implemented Plan:

1. Add a `post_review_hold` profile state for `PCRP-G1-VIRAL-P006-001`.
2. Convert that state into a blocking report finding with the original hold
   reason and required superseding package `PCRP-G1-VIRAL-P006-002`.
3. Suppress the page-complete decision path by setting
   `requires_bogdan_decision=false` and exposing only hold/correction routing.
4. Mark the old P006 text map as negative regression input, not valid structure
   evidence.
5. Project the post-review state into the human packet and summary so the
   review surface cannot imply page-complete readiness.
6. Update focused regression tests to require blocked P006 status, suppressed
   `page 006 complete ok`, and explicit supersession routing.

Guardrails:

- Page 006 remains not accepted as complete.
- P006-002 remains blocked until the remaining semantic-map hardening work is
  implemented and reviewed.
- No new OCR, PDF parsing/text-layer extraction, rerendering, raw mutation,
  fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, whole Gate 1 acceptance, or push is created.

Next:

- Run local checks.
- Run Sol/Terra on step 1 only.
- Present the step 1 review surface to Bogdan before commit.

## Documentation Checkpoint: doc-checkpoint-20260724T071222Z

Timestamp: 2026-07-24T07:12:22Z

Scope:

- Bogdan held `PCRP-G1-VIRAL-P006-001`: page 006 crops are correct, but
  `page_006_ocr_verified_text_map.md` is not structurally reliable.
- The text map blocker is pipeline-level. The current generator can report
  readiness while headings, quotes, body paragraphs, and continuations are
  collapsed into a crop/block row.
- The current goal is
  `BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001`: harden the
  page-complete review semantic-map contract, templates, generator logic,
  validation, and tests before preparing `PCRP-G1-VIRAL-P006-002`.

Execution Plan:

1. Treat `PCRP-G1-VIRAL-P006-001` as held; do not create page-complete
   acceptance.
2. Introduce a reproducible semantic-unit model separate from visual crops and
   source regions/blocks.
3. Update the human text-map template so it shows unit structure clearly and
   never hides long prose inside broken markdown table cells.
4. Add rules for headings, quotes, body text, continuations, art, captions,
   tables, callouts, sidebars, cards, stat blocks, page markers, and explicit
   absent/context-only/visual-only declarations.
5. Refactor the page-complete review builder to generate maps from semantic
   units/spans instead of block text rows.
6. Add a structural validator and structural findings that block
   `ready_for_bogdan_page_complete_decision`.
7. Add tests for collapsed units, invalid heading levels, quote flattening,
   technical role leakage into style, markdown table integrity, and missing
   continuation links.
8. Add regression coverage for P005/P006 plus synthetic future mixed layouts.
9. Sync the relevant reconstruct/quality/readiness contract surfaces.
10. Generate `PCRP-G1-VIRAL-P006-002` only after hardening passes local checks
    and Sol/Terra.

Sol/Terra Refinement:

- Convert the plan from prose into an executable contract: semantic-unit schema,
  taxonomy/version registry, validator predicates, finding severities, waiver
  eligibility, and decision-option suppression.
- Treat `PCRP-G1-VIRAL-P006-001` as held/superseded for acceptance routing; its
  text map becomes negative regression evidence for collapsed structure.
- Add per-unit lineage and stale checks: schema/taxonomy/profile/script/test
  revisions, predecessor hashes, source block/span links, crop links, and
  evidence state.
- Require full-page reconciliation across source regions, crops, semantic
  units, continuations, and explicit absent/context-only/visual-only/excluded/
  unknown decisions.
- Specify the human map shape: metadata-only summary table, per-unit full text
  blocks, escaping/fenced text rules, preview limits, continuation links,
  structural findings, and "Not Evidence For" boundaries.
- Require builder fail-closed behavior when semantic decomposition is missing
  or when any path attempts OCR, PDF parsing/text-layer extraction, rerendering,
  or raw artifact mutation.
- Add report fields: `semantic_validation`, `semantic_units_validated`,
  `structural_findings`, and `decision_options_suppressed`.
- Add generic synthetic regression fixtures beyond Viral page IDs: mixed
  heading/body/quote, TOC rows, art+caption, table, callout/sidebar, stat/card,
  page marker, context-only inset, visual-only art, column/page continuation,
  and unsupported/unknown unit.
- Sync exact surfaces: builder, tests, report JSON, packet Markdown, manifest
  hashes, `pre_ocr_mapping_model.md`, `gate_01_qualification_protocol.md`,
  `contracts/reconstruct.md`, quality/acceptance docs, roadmap, status, and
  page-complete acceptance logic.

Guardrails:

- This is planning/context only until implementation begins under the active
  bounded continuation.
- Page 006 remains not accepted as complete.
- Whole Gate 1 remains not accepted.
- No fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created by this checkpoint.

## Documentation Checkpoint: doc-checkpoint-20260719T193720Z

Timestamp: 2026-07-19T19:37:20Z

Scope:

- `AGENTS.md` now explicitly records the Sourcefold orchestrator review
  workflow.
- Sol is the analytical reviewer and Terra is the critic.
- The orchestrator proceeds only after both reviewers return OK for the same
  bounded scope.
- If either reviewer returns blockers or NOT OK, the orchestrator must fix the
  concrete blockers and repeat the Sol/Terra review cycle.
- Bogdan receives attached human-facing target files with plain-language
  guidance: what to inspect, what decision is needed, and what each choice
  affects.

Guardrails:

- Do not ask Bogdan to verify hashes, pytest output, test keys, stale scans,
  diff checks, line-ending checks, or internal QA checklists.
- This is process documentation only. It creates no source acceptance,
  page-complete acceptance, whole-Gate acceptance, fixture admission,
  implementation, push, OCR/PDF/render/raw mutation, translation,
  proofreading, or renderer/profile acceptance.

## Documentation Checkpoint: doc-checkpoint-20260724T210633Z

Timestamp: 2026-07-24T21:06:33Z

Scope:

- Bogdan asked to make the P007 commit-delay lessons part of the pipeline and
  asked whether paragraph preservation was recorded beyond page 007.
- `BA-G1-VIRAL-PAGE-REVIEW-PIPELINE-HARDENING-002` authorizes only process,
  validator, test, and documentation hardening.

Completed:

- Commit-stage discipline is now explicit: before saying "ready to commit",
  generated files must already pass scoped working-tree `git diff --check`,
  manifest/hash integrity checks, tests, and Sol/Terra review.
- A post-review whitespace, hash, manifest, or provenance issue is build/fix
  work, not commit-stage work.
- Commit stage is limited to pathspec staging, `git diff --cached --check`,
  `git diff --cached --name-only`, and `git commit`; no regeneration or hash
  surgery belongs there.
- Paragraph-boundary preservation is promoted to the general semantic-unit
  contract: visible source paragraph breaks must be represented as separate
  `paragraph`/`continuation` units, or by explicit paragraph-boundary metadata
  under a separately reviewed contract.

Next:

- Use this hardened contract as the default starting point for `full P008`.
- Keep P008 separate from P007 and keep Gate 1 rollup behind P008 review.

Guardrails:

- No page 008 processing, page-complete acceptance, whole Gate 1 acceptance,
  fixture admission, source acceptance mutation, OCR/render/PDF/raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, push,
  or candidate artifact rebuild is created by this hardening step.

## Documentation Checkpoint: doc-checkpoint-20260724T212402Z

Timestamp: 2026-07-24T21:24:02Z

Scope:

- Bogdan chose to continue with `full P008` before Gate 1 and asked for a
  backlog/action-log file showing where Codex orchestrated, where tools were
  used, and where scripts generated outputs.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P008-001` authorizes only a page 008
  review packet, not acceptance.

Completed:

- Prepared `PCRP-G1-VIRAL-P008-001` as a page 008 only review packet.
- Packaged the source page image, seven review crops, OCR/verified text map,
  semantic JSON/Markdown, summary, packet, report, manifest, and
  `page_008_action_backlog.md`.
- Classified the portrait/photo and crystal/object regions as deferred visual
  anchors with zero source text.
- Preserved paragraph boundaries as 14 semantic text units across Marco
  continuation, Marco appearance/gear, Corrina heading/body, Corrina
  continuation/body, and Corrina appearance/gear.
- Semantic validation, Markdown projection, and inventory reconciliation pass
  with zero structural findings.

Next:

- Run full checks and Sol/Terra review for the P008 review-packet scope.
- If clean, send the P008 packet, text maps, crops, and backlog file to Bogdan
  for human review.

Guardrails:

- `PCRP-G1-VIRAL-P008-001` creates no page-complete acceptance.
- Whole Gate 1 is not accepted.
- No fixture admission, source acceptance mutation, OCR, render, PDF
  parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader page action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260724T202839Z

Timestamp: 2026-07-24T20:28:39Z

Scope:

- Bogdan chose the next sequence as `full 7`, then `full 8`, then Gate 1,
  explicitly saying not to mix pages 7 and 8 together.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-001` authorized the first page 007
  packet, which Bogdan held for art-anchor and block/unit modeling errors.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-002` authorized the art-anchor/block
  correction, which Bogdan held for paragraph-boundary flattening.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-003` authorizes only the
  paragraph-preserving superseding page 007 page-complete review packet.
- `BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P007-001` authorizes only the page 007
  page-complete acceptance after Bogdan's explicit `page 007 complete ok`.
- `PCRP-G1-VIRAL-P007-003` packages a deferred Spektral Krew `ui_art_anchor`,
  a left article text block with paragraph-preserving semantic units, a right
  continuation/article block with paragraph-preserving semantic units, semantic
  JSON/Markdown, Markdown projection validation, and inventory reconciliation.
- `P007PCA-G1-VIRAL-001` consumes `PCRP-G1-VIRAL-P007-003` and accepts page
  007 as complete only.
- `BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P008-001` authorized only the separate
  page 008 review packet with the requested action backlog.
- `PCRP-G1-VIRAL-P008-001` packages Marco page-continuation text, Marco
  appearance/gear, Corrina portrait/photo anchor, Corrina body text, Corrina
  appearance/gear, crystal/object art anchor, semantic JSON/Markdown, Markdown
  projection validation, inventory reconciliation, and an action backlog.
- `BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P008-001` authorizes only the page 008
  page-complete acceptance after Bogdan's explicit `page 008 complete ok`.
- `P008PCA-G1-VIRAL-001` consumes `PCRP-G1-VIRAL-P008-001` and accepts page
  008 as complete only.

Completed:

- Superseding page 007 review packet was accepted by Bogdan's separate
  page-complete decision.
- Review state: 3/3 ready blocks, 7 text semantic units, valid semantic
  validation, valid Markdown projection, valid inventory reconciliation, zero
  structural findings, and no blockers/open questions.
- Page 007 right-column body text ends at the visible page boundary and is not
  linked to page 008 in this packet; page 008 processing remains separate.
- Page 007 acceptance state: `P007PCA-G1-VIRAL-001` accepts page 007 as
  complete only.
- Page 008 review state: 7/7 ready blocks, two deferred visual anchors, 14 text
  semantic units, valid semantic validation, valid Markdown projection, valid
  inventory reconciliation, zero structural findings, no blockers/open
  questions, and an action backlog.
- Page 008 acceptance state: `P008PCA-G1-VIRAL-001` accepts page 008 as
  complete only.

Next:

- Run focused/full checks and Sol/Terra review for the post-P008 Gate 1
  status/route packet.
- After `G1SP-G1-VIRAL-002` is clean and reviewed, send it to Bogdan for
  `status packet ok` or `hold status packet: <reason>`.

Guardrails:

- `PCRP-G1-VIRAL-P007-003` itself creates no page-complete acceptance;
  `P007PCA-G1-VIRAL-001` is the separate acceptance layer.
- `PCRP-G1-VIRAL-P008-001` itself creates no page-complete acceptance;
  `P008PCA-G1-VIRAL-001` is the separate acceptance layer.
- Page 009 is not processed.
- Whole Gate 1, fixture admission, source acceptance mutation, OCR, render,
  PDF parsing/text-layer extraction, raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, and push remain blocked.

## Gate 1 Status/Route Packet G1SP-G1-VIRAL-002

Authorization:

- `BA-G1-VIRAL-GATE-1-STATUS-REFRESH-002` authorizes only a post-P008 Gate 1
  status/route packet.

State:

- `G1SP-G1-VIRAL-002` records pages 002-008 as page-complete accepted only.
- `G1SP-G1-VIRAL-001` is historical/narrow/stale for current page-complete
  status and is not reused as the current full Gate 1 status.
- Current source reconstruction remains the canonical narrow state of 13
  accepted records, with no new source-acceptance rollup created here.
- First-class blockers are page 001 incomplete, pages 009-020 unstarted, whole
  Gate 1 not accepted, source profile parameters unaccepted/unparked, OCR
  benchmark remediation unresolved, and status-only/no-acceptance routing.

Boundaries:

- `G1SP-G1-VIRAL-002` does not authorize the next layer.
- Whole Gate 1 acceptance, fixture admission, source mutation/new source
  acceptance, OCR/render/PDF/raw mutation, page 009+ processing, translation,
  proofreading, renderer/profile acceptance, implementation, and push remain
  false.
- The routing matrix may recommend page 001 completion as the next candidate,
  but page 001 triage/review is a later separate bounded step.

## Page 001 Triage/Review Routing P001TR-G1-VIRAL-001

Authorization:

- `BA-G1-VIRAL-PAGE-001-TRIAGE-001` authorizes only page 001
  triage/readiness routing.

State:

- Bogdan selected page 001 triage/review as the next layer after
  `G1SP-G1-VIRAL-002`.
- OCR benchmark remediation remains a legal later branch, but is not the first
  selected step because it does not close the page 001 blocker.
- `P001TR-G1-VIRAL-001` uses existing rendered page 001 image and existing
  map/triage/status predecessor evidence only.
- Page 001 is routed as a visual/title page-complete review candidate without
  OCR/remediation.
- `PCRP-G1-VIRAL-P001-001` consumes `P001TR-G1-VIRAL-001` and packages page
  001 for Bogdan's explicit page-complete decision with full-page cover,
  title/logo, and footer/rating/tagline/logo deferred visual anchors.
- `P001PCA-G1-VIRAL-001` consumes `PCRP-G1-VIRAL-P001-001` and accepts page
  001 as complete only.
- `G1SP-G1-VIRAL-003` consumes the post-P008 status packet plus page 001
  acceptance and refreshes the route after the page 001 blocker closed.
- `P009TR-G1-VIRAL-001` was held for crooked/tight review crops and text
  clipping.
- `P009TR-G1-VIRAL-002` supersedes it, consumes `G1SP-G1-VIRAL-003`, and
  packages page 009 as a two-profile visual/text triage candidate for Bogdan
  review with readable padded portrait crops and full-column text crops.
- Bogdan clarified that review crops can become downstream OCR inputs, so
  `P009TR-G1-VIRAL-002` is not sufficient for `PCRP-G1-VIRAL-P009-001` as an
  OCR crop contract. It remains historical/readability-only; Bogdan confirmed
  the right lower grey block is complete. The next bounded layer is
  `P009TR-G1-VIRAL-003`, which must supersede `_002` for PCRP consumption and
  record role-separated crop boxes:
  - `source_region_box_px`: immutable PRM/page-map lineage only.
  - `human_review_crop_box_px`: broad human context crop, allowed to include
    portrait/art/frame context.
  - `ocr_candidate_crop_box_px` / `text_evidence_crop_box_px`: text-only OCR or
    verification crop, with no clipping and no extra portrait/art/frame content.
- Required QA before `PCRP-G1-VIRAL-P009-001`: edge/gutter checks on OCR/text
  evidence crops, blocker for text ink near any crop boundary, blocker for
  visual-only/art content inside OCR crops, page-map reconciliation proving every
  represented text-like region has an OCR/text evidence crop, semantic/text-map
  unit linkage to `text_evidence_crop_id`, and regression coverage for two-column
  pages with 0, 1, 2, and 3+ art regions in variable positions.
- `P009TR-G1-VIRAL-003` implements the eight-step correction path and was
  accepted by Bogdan as crop contract only. `P009TXT-G1-VIRAL-001` records that
  decision and creates a draft text map from the two text evidence crops. It
  creates no OCR run/output acceptance, no source acceptance, no PCRP, no
  page-complete acceptance, and no pages 010-020 processing. Bogdan accepted
  the draft text as `p009 text ok`, and `P009SEM-G1-VIRAL-001` now records a
  14-unit semantic text map for review. Bogdan accepted the semantic map as
  `p009 semantic map ok`, and `PCRP-G1-VIRAL-P009-001` now consumes the crop,
  text, and semantic predecessors as a page-complete review packet with 4/4 ready
  blocks and no blockers. Bogdan then approved page 009 as complete, and
  `P009PCA-G1-VIRAL-001` accepts page 009 only. It creates no source acceptance,
  no whole Gate 1 acceptance, and no pages 010-020 processing.

Boundaries:

- `P001TR-G1-VIRAL-001` creates no page-complete acceptance.
- `PCRP-G1-VIRAL-P001-001` is review packet only; the separate
  `P001PCA-G1-VIRAL-001` acceptance layer records the page 001 page-complete
  decision.
- Whole Gate 1 acceptance, fixture admission, source mutation/new source
  acceptance, OCR/render/PDF/raw mutation, pages 010-020 processing,
  translation, proofreading, renderer/profile acceptance, implementation, and
  push remain false.
- `P009TR-G1-VIRAL-002` must not be consumed as OCR evidence, page-map
  completeness proof, or sufficient readiness for `PCRP-G1-VIRAL-P009-001`.
- `PCRP-G1-VIRAL-P009-001` must fail closed until it consumes a current
  `P009TR-G1-VIRAL-003` crop-role contract with OCR-safe text evidence crops.
- The current bounded continuation is
  `page_009_complete_accepted_pages_010_020_unstarted`;
  `P009TR-G1-VIRAL-002` is historical/readability-only and stale for PCRP
  routing.
- `P009PCA-G1-VIRAL-001` accepts only page 009 as complete; page 010 has since
  advanced through P010TR/P010TXT/P010SEM/PCRP review and
  `P010PCA-G1-VIRAL-001` accepts only page 010 as complete. Pages 011-020
  remain unstarted.
- `G1SP-G1-VIRAL-005` historically recorded the post-P010 route state: pages
  001-010 were page-complete accepted only, pages 011-020 were unstarted at
  that checkpoint, and the next bounded candidate was page 011 triage.
- `P011TR-G1-VIRAL-001` packages page 011 triage/crop-contract review only:
  two text-like regions (`R01`, `R04`) have OCR/text-evidence crops, two art
  anchors (`R02`, `R03`) remain visual-only, and no text extraction, semantic
  map, PCRP, page-complete acceptance, whole Gate 1 acceptance, or page 012+
  processing is created.
- Bogdan accepted `P011TR-G1-VIRAL-001` with `p011 triage ok`.
- `P011TXT-G1-VIRAL-001` now records that decision and produces a draft text
  map from exactly two text evidence crops: `P011-B001-TES` and
  `P011-B004-TES`.
- `P011-B002` Emily portrait and `P011-B003` lower-left screen image remain
  visual-only anchors and are not text extraction inputs.
- Bogdan accepted `P011TXT-G1-VIRAL-001` with `p011 text ok`.
- `P011SEM-G1-VIRAL-001` now records that decision and produces a 12-unit
  semantic text map for review, with Maya continuation from page 010,
  `Maya's Secrets`/`APPEARANCE` `h3` headings, Emily `h2` profile heading,
  `Super Fan Option.` as a bounded `h3` inline option heading, and Emily
  continuation metadata to page 012.
- The universal semantic-map contract now supports optional layout/style hints
  for source typography and line flow. Page 011 uses these to mark block
  headings with line breaks and `Super Fan Option.` as italic inline heading
  with same-line continuation to `SU-P011-EMILY-004`.
- Bogdan accepted `P011SEM-G1-VIRAL-001` as `p011 semantic map ok`, and
  `PCRP-G1-VIRAL-P011-001` now consumes the triage, text, and semantic
  predecessors as a page-complete review packet with 4/4 ready blocks, two
  visual-only art anchors, valid semantic/projection/inventory checks, and no
  page/source/whole-Gate acceptance.
- Bogdan accepted page 011 as complete, and `P011PCA-G1-VIRAL-001` records
  page 011 page-complete acceptance only.
- `G1SP-G1-VIRAL-006` records the post-P011 route state: pages 001-011 are
  page-complete accepted only, pages 012-020 remain unstarted, and the next
  bounded candidate is page 012 triage/readiness without authorizing it.
- `P012BATCH-G1-VIRAL-001` tests the aggressive delegated-review model for page
  012: internal P012TR/P012TXT/P012SEM/PCRP/P012PCA stages are machine-reviewed
  by Sol/Terra with skipped-human-review labels, and final Bogdan review is
  deferred to the batch bundle plus `G1SP-G1-VIRAL-007`. Page 012 uses seven
  text-evidence crops with explicit crop provenance contracts, including a split
  two-part `Another Ghost Hunter Option` evidence surface and shared
  crop-contract QA. `P012BATCHREV-G1-VIRAL-001` records final human acceptance
  of that bundle/status with `p012 aggressive batch ok`. Nested run-in option
  labels under `Other Investigator Options.` use parent-heading-level-plus-one
  semantics, capped at h6; page 012 `Mythos Investigators` is an h4 inline
  heading under the h3 parent subsection.
- `BA-G1-VIRAL-AGGRESSIVE-CROP-PROVENANCE-GATE-001` promotes the crop
  provenance contract into an aggressive-builder gate: future
  `build_page_*_aggressive_batch.py` builders must import/call the shared
  validator and define explicit `crop_contract`/`context_allowed` metadata for
  text-evidence blocks.
- `P013BATCH-G1-VIRAL-001` runs page 013 in the aggressive delegated-review
  model: internal P013TR/P013TXT/P013SEM/PCRP/P013PCA stages are machine-reviewed
  by Sol/Terra with skipped-human-review labels, and final Bogdan review is
  deferred to the batch bundle plus `G1SP-G1-VIRAL-008`. Page 013 uses five
  text-evidence crops with explicit crop provenance contracts; the Tourists
  option is split across left-start and right-continuation evidence surfaces.
  Page 013 `Documentary Film Crew`, `Tourists`, and `Pesky Teenagers` are h4
  inline headings under the h3 `Other Investigator Options.` parent subsection.
- `P013BATCHREV-G1-VIRAL-001` records Bogdan's final human-facing review
  acceptance of the page 013 aggressive batch plus `G1SP-G1-VIRAL-008` with
  `p013 aggressive batch ok`; it does not convert internal P013 stages into
  direct Bogdan approvals.
- `P014BATCH-G1-VIRAL-001` runs page 014 in the aggressive delegated-review
  model: internal P014TR/P014TXT/P014SEM/PCRP/P014PCA stages are machine-reviewed
  by Sol/Terra with skipped-human-review labels. `P014BATCHREV-G1-VIRAL-001`
  records Bogdan's final human-facing review acceptance of the page 014
  aggressive batch plus `G1SP-G1-VIRAL-009` with `p014 aggressive batch ok`;
  it does not convert internal P014 stages into direct Bogdan approvals. Page 014 uses nine
  text-evidence crops with explicit crop provenance contracts plus one
  visual-only photo anchor.
- `Keeper's Notes` callout labels now use a narrow shared helper returning
  `h4`; P012 `SU-P012-KEEPER-001` is corrected from `h3` to `h4`, while ordinary
  section/item headings are unchanged.
- Aggressive batch startup now has a Sourcefold-native authorization
  materialization preflight. Future `build_page_*_aggressive_batch.py` builders
  must call `materialize_aggressive_batch_authorization()` before internal page
  output generation and must create the exact page-specific
  `BA-G1-VIRAL-PAGE-0XX-AGGRESSIVE-BATCH-001` ledger artifact from explicit
  bounded authority.
- `P015BATCH-G1-VIRAL-001` runs page 015 in the aggressive delegated-review
  model after the preflight materialized
  `BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001`. Internal
  P015TR/P015TXT/P015SEM/PCRP/P015PCA stages are machine-reviewed by Sol/Terra
  with skipped-human-review labels. `G1SP-G1-VIRAL-010` records pages 001-015
  as page-complete accepted only and routes page 016 triage/readiness as the
  next recommended candidate without authorizing it. `P015BATCHREV-G1-VIRAL-001`
  records Bogdan's final human-facing review acceptance of the page 015
  aggressive batch plus `G1SP-G1-VIRAL-010` with `p015 aggressive batch ok`;
  it does not convert internal P015 stages into direct Bogdan approvals.
- `BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001` records the next
  planned work mode: pages 016-020 may be processed sequentially in aggressive
  mode, one page at a time, with stop-on-first-blocker behavior. The future
  human review packet is contract-bound to only source page art plus semantic
  text map markdown for each page; text-evidence crops stay internal unless a
  blocker requires escalation.
- Current bounded continuation is
  `page_015_aggressive_batch_final_review_accepted_pages_016_020_unstarted`.

## Documentation Checkpoint: doc-checkpoint-20260726T211000Z

Timestamp: 2026-07-26T21:10:00Z

Context:

- Bogdan explicitly selected page 015 aggressive processing after the
  aggressive-batch authorization preflight hardening was committed.
- Sol/Terra read-only scope review allowed P015 only if the new preflight
  materialized `BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001`, bound exact
  predecessors and `page_015.png`, excluded the upper-right photo from text
  extraction, and kept page 016+ unprocessed.

Result:

- Added `BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001` via the shared preflight and
  generated `P015BATCH-G1-VIRAL-001`.
- Internal P015TR/P015TXT/P015SEM/PCRP/P015PCA stages record
  `human_review_skipped_by_explicit_authorization` and Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Page 015 is hash-bound to `page_015.png`, `G1SP-G1-VIRAL-009`, and
  `P014BATCHREV-G1-VIRAL-001`.
- Page 015 uses two text-evidence crops for Timeline/History and one
  visual-only photo anchor. The History section is marked as continuing to page
  016 without processing page 016.
- `G1SP-G1-VIRAL-010` records pages 001-015 as page-complete accepted only and
  routes page 016 triage/readiness as the next recommended candidate without
  authorizing it.

Boundaries:

- Final Bogdan batch/status review for P015 is still pending.
- No direct Bogdan per-stage approval is recorded for internal P015 stages.
- No page 016+ processing is created.
- No whole Gate 1 acceptance, fixture admission, source acceptance mutation,
  OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile
  acceptance, implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260726T230900Z

Timestamp: 2026-07-26T23:09:00Z

Context:

- Bogdan selected `p015 aggressive batch ok` for the P015 final bundle/status.
- The active Sourcefold auto-commit rule allows narrow final-review recording
  and commit after clean focused, roadmap, full-suite, and diff-check gates.

Result:

- Added `P015BATCHREV-G1-VIRAL-001` for the P015 final human-facing review.
- The final review accepts the page 015 aggressive batch plus
  `G1SP-G1-VIRAL-010` only.
- Internal P015TR/P015TXT/P015SEM/PCRP/P015PCA stages remain
  `human_review_skipped_by_explicit_authorization` with Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Pages 001-015 remain page-complete accepted only; pages 016-020 remain
  unstarted.

Boundaries:

- No page 016+ processing is created.
- No whole Gate 1 acceptance, fixture admission, source acceptance mutation,
  OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile
  acceptance, implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260726T232500Z

Timestamp: 2026-07-26T23:25:00Z

Context:

- Bogdan selected a P016-P020 sequential aggressive run as the next mode and
  clarified that his review packet should contain only source page art and
  semantic text map markdown for each page.
- The existing aggressive batch pipeline still needs to keep page-by-page
  internal evidence and hash-chain artifacts.

Result:

- Added `BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001` as prep-only
  authorization for the run-mode contract.
- Added `aggressive_review_packet_contract.py` and tests to enforce the
  human-facing packet shape: pages 016-020, exactly two required review files
  per page, and no crop/review-assets in the default human packet.
- The future run still uses page-specific aggressive builders and
  `BA-G1-VIRAL-PAGE-0XX-AGGRESSIVE-BATCH-001` authorization materialization
  when each page actually starts.

Boundaries:

- No P016-P020 page artifacts are created.
- No bulk final-review acceptance helper is created.
- No page 021+ processing is authorized.
- No whole Gate 1 acceptance, fixture admission, source acceptance mutation,
  OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile
  acceptance, implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260726T234500Z

Timestamp: 2026-07-26T23:45:00Z

Context:

- Bogdan authorized the prepared P016-P020 sequential aggressive run with
  `ок, тогда делай 16-20 агрессивно`.
- Sol/Terra scope review required real page-specific builders/tests and
  existing semantic map files before emitting the human packet.

Result:

- Added page-specific P016-P020 aggressive builders/tests and a shared
  `build_pages_016_020_aggressive_batch.py` implementation under the existing
  authorization preflight and crop provenance contracts.
- Materialized `BA-G1-VIRAL-PAGE-016-AGGRESSIVE-BATCH-001` through
  `BA-G1-VIRAL-PAGE-020-AGGRESSIVE-BATCH-001` before page outputs.
- Generated P016TR/P016TXT/P016SEM/PCRP/PCA through P020TR/P020TXT/P020SEM/PCRP/PCA,
  `G1SP-G1-VIRAL-011` through `G1SP-G1-VIRAL-015`, and
  `P016BATCH-G1-VIRAL-001` through `P020BATCH-G1-VIRAL-001`.
- P016 consumes the P015 History continuation; P020 records continuation toward
  page 021 without processing or authorizing page 021.

Boundaries:

- P016-P020 final human reviews are pending; no `P016BATCHREV-*` through
  `P020BATCHREV-*` artifacts are created.
- The human packet remains limited to five source pages and five semantic text
  maps; crop evidence remains internal unless a blocker requires escalation.
- No page 021+ processing, bulk final-review acceptance, whole Gate 1
  acceptance, fixture admission, source/OCR/render/PDF/raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, push,
  or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260726T200000Z

Timestamp: 2026-07-26T20:00:00Z

Context:

- Bogdan asked to commit P013 final review and move to page 014 in aggressive
  mode.
- Sol/Terra read-only scope review found one governance blocker: page 014 needed
  an exact bounded authorization before any P014 artifacts could be produced.

Result:

- Added `BA-G1-VIRAL-PAGE-014-AGGRESSIVE-BATCH-001` and generated
  `P014BATCH-G1-VIRAL-001`.
- Internal P014TR/P014TXT/P014SEM/PCRP/P014PCA stages record
  `human_review_skipped_by_explicit_authorization` and Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Page 014 is hash-bound to `page_014.png`, `G1SP-G1-VIRAL-008`, and
  `P013BATCHREV-G1-VIRAL-001`.
- Page 014 uses nine text-evidence crops with explicit crop provenance
  contracts and one visual-only photo anchor.
- `G1SP-G1-VIRAL-009` records pages 001-014 as page-complete accepted only and
  routes page 015 triage/readiness as the next recommended candidate without
  authorizing it.

Boundaries:

- Final Bogdan batch/status review for P014 is still pending.
- No direct Bogdan per-stage approval is recorded for internal P014 stages.
- No page 015+ processing is created.
- No whole Gate 1 acceptance, fixture admission, source acceptance mutation,
  OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile
  acceptance, implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260726T201500Z

Timestamp: 2026-07-26T20:15:00Z

Context:

- Bogdan compared heading levels for page 011 `Maya's Secrets`, page 012
  `Keeper's Notes`, and page 014 `Keeper's Notes`.
- Bogdan requested a narrow rule for `Keeper's Notes` so it behaves like a
  callout label and does not affect other headings.

Result:

- Added a shared semantic helper for `Keeper's Notes` callout heading level.
- The helper returns `h4` and is used by P012 and P014 builders.
- P012 `SU-P012-KEEPER-001` was corrected from `h3` to `h4` with
  `display_style=callout_heading`.
- P014 `Keeper's Notes` callout headings remain `h4` and now use the shared
  helper.
- P012/P013/P014 downstream hash-bound artifacts were regenerated and
  synchronized.

Boundaries:

- This is a semantic-depth correction only.
- Ordinary section/item headings are unchanged.
- Final Bogdan batch/status review for P014 is still pending.
- No page 015+ processing is created.
- No whole Gate 1 acceptance, fixture admission, source acceptance mutation,
  OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile
  acceptance, implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260726T203000Z

Timestamp: 2026-07-26T20:30:00Z

Context:

- Bogdan selected `p014 aggressive batch ok` for the P014 final bundle/status.
- The active Sourcefold auto-commit rule allows narrow final-review recording
  and commit after clean focused, roadmap, full-suite, and diff-check gates.

Result:

- Added `P014BATCHREV-G1-VIRAL-001` for the P014 final human-facing review.
- The final review accepts the page 014 aggressive batch plus
  `G1SP-G1-VIRAL-009` only.
- Internal P014TR/P014TXT/P014SEM/PCRP/P014PCA stages remain
  `human_review_skipped_by_explicit_authorization` with Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Pages 001-014 remain page-complete accepted only; pages 015-020 remain
  unstarted.

Boundaries:

- No page 015+ processing is created.
- No whole Gate 1 acceptance, fixture admission, source acceptance mutation,
  OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile
  acceptance, implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260726T205000Z

Timestamp: 2026-07-26T20:50:00Z

Context:

- Bogdan clarified that the page 014 startup authorization issue should be
  fixed inside Sourcefold aggressive batch, not as an OpenClaw workflow rule.
- Sol and Terra reviewed the intended scope and agreed the change belongs in a
  fail-closed Sourcefold preflight contract.

Result:

- Added `materialize_aggressive_batch_authorization()` to the bounded
  authorization contract module.
- Added fail-closed tests for idempotent materialization, page/lane mismatch,
  and aggressive-builder scanner enforcement.
- Updated P012/P013/P014 aggressive builders to call the authorization
  preflight before predecessor verification/output generation.
- Future P0XX aggressive builders must materialize the exact page-specific
  `BA-G1-VIRAL-PAGE-0XX-AGGRESSIVE-BATCH-001` ledger section from explicit
  bounded authority.

Boundaries:

- No page 015 processing is created.
- No final batch acceptance is created.
- No whole Gate 1 acceptance, fixture admission, source acceptance mutation,
  OCR/render/PDF/raw mutation, translation, proofreading, renderer/profile
  acceptance, implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260727T154500Z

Timestamp: 2026-07-27T15:45:00Z

Context:

- Bogdan's P016/P018 review exposed that `Keeper's Notes` units could consume
  ordinary body text after the callout.
- The issue was accepted as a pipeline-wide missing semantic containment guard,
  not only a P016/P018 aggressive-batch defect.

Result:

- Added shared fail-closed `semantic_split_contract` validation for bounded
  callout/sidebar/card/Keeper body segments.
- Current aggressive builders for P012, P014, and P016-P020 now emit and validate
  split contracts before semantic map output.
- P016/P018 were corrected and rebuilt through downstream status/hash-bound
  artifacts; P017/P019/P020 remain reviewed OK controls.

Boundaries:

- P016-P020 final human reviews remain pending.
- No page 021+ processing, bulk final-review acceptance, whole Gate 1
  acceptance, fixture admission, source/OCR/render/PDF/raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, push,
  or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260727T162100Z

Timestamp: 2026-07-27T16:21:00Z

Context:

- Bogdan accepted the corrected P016/P018 semantic maps and the P016-P020 final
  aggressive batch review with:
  `p016 corrected semantic map ok; p018 corrected semantic map ok; p016-p020 aggressive batch ok`.

Result:

- Added `accept_pages_016_020_aggressive_batch_review.py` and a fail-closed
  final-review test lane.
- Created `P016BATCHREV-G1-VIRAL-001` through `P020BATCHREV-G1-VIRAL-001`.
- Updated roadmap/status/authorization docs to record pages 001-020 as
  page-complete accepted only, with page 021+ still unprocessed and
  unauthorized.

Boundaries:

- Internal P016-P020 stages remain delegated/skipped-human-review stages, not
  direct Bogdan per-stage approvals.
- No whole Gate 1 acceptance, fixture admission, source/OCR/render/PDF/raw
  mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260727T164000Z

Timestamp: 2026-07-27T16:40:00Z

Context:

- Bogdan asked to reread the project context with Sol/Terra, prepare an update
  plan, and move on that plan after P016-P020 final human review was recorded.
- Sol/Terra agreed the next bounded step should be post-P020 Gate 1
  status/readiness decision-prep, not page 021 processing.

Result:

- Added `post_p020_gate_1_status_readiness_plan.md`.
- Added fail-closed `build_gate_1_status_readiness_post_p020.py` and
  `test_gate_1_status_readiness_post_p020.py`.
- Created `G1SP-G1-VIRAL-016` as a status/readiness packet that consumes
  `G1SP-G1-VIRAL-015` plus `P016BATCHREV-G1-VIRAL-001` through
  `P020BATCHREV-G1-VIRAL-001`.
- Updated current status, roadmap, and authorization ledgers so the current
  bounded continuation is
  `post_p020_gate_1_status_readiness_ready_page_021_plus_unprocessed`.

Boundaries:

- `G1SP-G1-VIRAL-016` is status/readiness-only and creates no acceptance.
- Page 021+ remains unprocessed and unauthorized.
- No whole Gate 1 acceptance, fixture admission, source/OCR/render/PDF/raw
  mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260727T173500Z

Timestamp: 2026-07-27T17:35:00Z

Context:

- After `G1SP-G1-VIRAL-016`, Bogdan selected the next route order from the
  available post-P020 choices.

Result:

- Recorded the selected sequence:
  1. Gate 1 source-profile readiness / parking matrix.
  2. OCR benchmark remediation / methodology hardening.
- Page 021 or P021-P025 aggressive processing is not selected by this route
  sequence.

Boundaries:

- This is planning direction only; neither selected route is started yet.
- No page 021+ processing, whole Gate 1 acceptance, fixture admission,
  source/OCR/render/PDF/raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader Gate action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260727T174500Z

Timestamp: 2026-07-27T17:45:00Z

Context:

- Bogdan authorized the first selected post-P020 route step with "приступай.
  бери сол и терру в помощь".
- `BA-G1-VIRAL-SOURCE-PROFILE-READINESS-PARKING-MATRIX-001` materializes only
  Gate 1 source-profile readiness / parking matrix decision-prep.

Result:

- `G1SPRM-G1-VIRAL-001` classifies current Gate 1 source-profile parameters
  against the pages 001-020 page-complete accepted-only baseline.
- The matrix marks OCR benchmark remediation / methodology hardening as the
  selected next branch, but does not start it.
- No source-profile parameter is accepted or parked by the matrix.

Boundaries:

- Page 021+ processing, whole Gate 1 acceptance, fixture admission,
  source/OCR/render/PDF/raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, and broader Gate action
  remain blocked until separately authorized.

## Documentation Checkpoint: doc-checkpoint-20260727T201100Z

Timestamp: 2026-07-27T20:11:00Z

Context:

- Bogdan reviewed the matrix classifications with Sol/Terra comments and said
  "ок принято с коментариями".
- `BA-G1-VIRAL-SOURCE-PROFILE-READINESS-MATRIX-REVIEW-001` materializes the
  review record only.

Result:

- `G1SPRMREV-G1-VIRAL-001` accepts `G1SPRM-G1-VIRAL-001` as a route-review
  artifact with comments.
- The accepted comments preserve that ready rows are review-ready only,
  OCR-hardening rows go to the next hardening branch, blocked rows remain
  blocked, and evidence-only rows do not become acceptance.
- OCR benchmark remediation / methodology hardening remains the selected next
  branch, requiring a separate bounded authorization.

Boundaries:

- No source-profile acceptance, parking decision, OCR remediation execution,
  page 021+ processing, fixture admission, source/OCR/render/PDF/raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation,
  push, whole Gate 1 acceptance, or broader Gate action is created.

## Documentation Checkpoint: doc-checkpoint-20260727T203000Z

Timestamp: 2026-07-27T20:30:00Z

Context:

- Bogdan asked to do both steps after the matrix review: commit the review
  record, then start OCR benchmark remediation / methodology hardening.
- `BA-G1-VIRAL-OCR-BENCHMARK-METHODOLOGY-HARDENING-001` materializes only the
  methodology hardening branch from existing evidence.

Result:

- `OCRHM-G1-VIRAL-001` consumes `G1SPRMREV-G1-VIRAL-001`,
  `ORM-G1-VIRAL-001`, `ORR-G1-VIRAL-001`, `ONC-G1-VIRAL-001`, and
  `OBR-G1-VIRAL-002`.
- It records 8 methodology rules as `hardened_for_gate_review` and 1 rule as
  `requires_future_gate_decision`.
- Recommended next packet is a post-OCR-hardening Gate 1 readiness refresh.

Boundaries:

- No OCR execution, remediation rerun, source-profile acceptance, parking
  decision, page 021+ processing, fixture admission, source/OCR/render/PDF/raw
  mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, whole Gate 1 acceptance, or broader Gate action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260727T204000Z

Timestamp: 2026-07-27T20:40:00Z

Context:

- Bogdan asked to commit `OCRHM-G1-VIRAL-001` and then prepare
  `post_ocr_hardening_gate_1_readiness_refresh`.

Result:

- `BA-G1-VIRAL-POST-OCR-HARDENING-STATUS-READINESS-001` is consumed.
- `G1SP-G1-VIRAL-017` refreshes Gate 1 readiness after OCR benchmark
  methodology hardening.
- The recommended next route decision is Gate 1 source-profile review /
  parking decisions, or a separately authorized page `021` / `P021-P025`
  continuation lane.

Boundaries:

- No source-profile acceptance, parking decision, OCR execution, remediation
  rerun, page `021+` processing, fixture admission, source/OCR/render/PDF/raw
  mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, whole Gate 1 acceptance, or broader Gate action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260727T213000Z

Timestamp: 2026-07-27T21:30:00Z

Context:

- Bogdan authorized the recommended Gate 1 source-profile review / parking
  decision prep route with "делай".
- Sol/Terra gave GO only for a bounded decision-prep packet, not actual
  acceptance or parking.

Result:

- `BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-001` is consumed.
- `G1SPRPD-G1-VIRAL-001` represents all 12 source-profile readiness matrix rows
  exactly once for human review.
- Counts: 5 accept-for-review candidates, 2 park-for-0.1 candidates with
  invalidation conditions, 2 evidence-only rows, 2 blocked-needs-decision rows,
  1 separate-bounded-authorization row, and 0 actual parked rows.

Boundaries:

- No source-profile acceptance, parking decision, fixture admission, OCR
  execution, remediation rerun, page `021+` processing, source/OCR/render/PDF
  /raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, whole Gate 1 acceptance, or broader Gate action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260727T215000Z

Timestamp: 2026-07-27T21:50:00Z

Context:

- Bogdan accepted `G1SPRPD-G1-VIRAL-001` as decision-prep only and authorized
  preparing the next source-profile decision packet, with no acceptance or
  parking yet.
- Sol/Terra gave GO only for a human-facing options packet.

Result:

- `BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-REVIEW-001` is
  consumed by `G1SPRPDREV-G1-VIRAL-001`.
- `BA-G1-VIRAL-SOURCE-PROFILE-DECISION-PACKET-001` is consumed by
  `G1SPDP-G1-VIRAL-001`.
- `G1SPDP-G1-VIRAL-001` prepares five future decision options for human review.

Boundaries:

- No source-profile acceptance, parking decision, fixture admission, OCR
  execution, remediation rerun, page `021+` processing, source/OCR/render/PDF
  /raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, whole Gate 1 acceptance, or broader Gate action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260727T221500Z

Timestamp: 2026-07-27T22:15:00Z

Context:

- Bogdan replied `ок` immediately after the assistant proposed the bounded
  `G1SPDP` decision phrase. The decision record preserves the full proposal as
  assistant text and Bogdan's raw reply as contextual approval.
- Sol/Terra gave GO only under that provenance and with fixture admission,
  whole Gate 1, page `021+`, OCR execution/remediation, mutation, and push
  blocked.

Result:

- `BA-G1-VIRAL-SOURCE-PROFILE-DECISION-RECORD-001` is consumed by
  `G1SPDR-G1-VIRAL-001`.
- `G1SPDR-G1-VIRAL-001` records 5 rows as Gate review candidates only, 2 OCR
  methodology/debt rows as Core 0.1 parking decisions with invalidation
  conditions, 2 rows as evidence-only, 2 rows as blocked, and 1 page `021+`
  row as requiring separate bounded authorization.

Boundaries:

- No whole source-profile acceptance, fixture admission, whole Gate 1
  acceptance, OCR execution/remediation rerun, page `021+` processing,
  source/OCR/render/PDF/raw mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, or broader Gate action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260727T224500Z

Timestamp: 2026-07-27T22:45:00Z

Context:

- Bogdan said "пошли дальше" after `G1SPDR-G1-VIRAL-001` was committed.
- Sol/Terra recommended a fixture-admission / whole-Gate-acceptance readiness
  prep packet before any P021 lane or Gate acceptance record.

Result:

- `BA-G1-VIRAL-FIXTURE-GATE-1-READINESS-PREP-001` is consumed by
  `G1FARP-G1-VIRAL-001`.
- `G1FARP-G1-VIRAL-001` preserves the `G1SPDR` counts: 5 Gate review
  candidate rows, 2 existing Core 0.1 OCR parking outcomes, 2 evidence-only
  rows, 2 blocked rows, and 1 page `021+` separate-BA row.
- Fixture admission readiness and whole Gate 1 acceptance readiness are both
  `not_ready_requires_future_decision`.

Boundaries:

- No fixture admission, fixture manifest creation, whole Gate 1 acceptance,
  whole source-profile acceptance, page `021+` processing, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation, translation,
  proofreading, renderer/profile acceptance, implementation, push, or
  downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260727T230000Z

Timestamp: 2026-07-27T23:00:00Z

Context:

- Bogdan accepted `G1FARP-G1-VIRAL-001` as a readiness/blocker packet only and
  authorized preparing fixture admission blocker resolution prep.

Result:

- `G1FARPREV-G1-VIRAL-001` records that review without admitting fixtures,
  accepting whole Gate 1, processing page `021+`, or pushing.
- `G1FABRP-G1-VIRAL-001` lists four blocker areas: unsupported/negative fixture
  policy, fixture strategy fit, whole Gate 1 dependency, and page `021+`
  boundary.
- The recommended sequence is unsupported/negative fixture policy decision
  prep, fixture strategy fit decision prep, fixture admission readiness
  refresh, then whole Gate 1 acceptance readiness recheck.

Boundaries:

- No fixture admission, fixture manifest creation, whole Gate 1 acceptance,
  whole source-profile acceptance, page `021+` processing, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation, translation,
  proofreading, renderer/profile acceptance, implementation, push, or blocker
  resolution is created.

Eight-step correction/implementation plan before `PCRP-G1-VIRAL-P009-001`:

Status: completed through `P009TR-G1-VIRAL-003`, then continued into
`P009TXT-G1-VIRAL-001`, `P009SEM-G1-VIRAL-001`, and
`PCRP-G1-VIRAL-P009-001`; `P009PCA-G1-VIRAL-001` now accepts page 009 only.
Page 010 has since advanced through the same bounded page-complete lane and
`P010PCA-G1-VIRAL-001` accepts page 010 only. Page 011 has also advanced
through the same bounded page-complete lane; `P011PCA-G1-VIRAL-001` accepts
page 011 only, and `G1SP-G1-VIRAL-006` refreshes the status route before any
page 012 work. Pages 012-014 have since advanced through aggressive
delegated-review lanes; page 014 is ready for final bundle/status review.

1. Correct the current status cursor from `page_009_triage_ready` to
   `page_009_crop_contract_missing_pcrp_blocked`.
2. Mark `P009TR-G1-VIRAL-002` stale for PCRP routing while preserving it as
   historical/readability-only evidence.
3. Record that `P009TR-G1-VIRAL-002`'s old route recommendation is superseded
   for PCRP purposes and must not be consumed by future PCRP code.
4. Create a new bounded authorization for `P009TR-G1-VIRAL-003` only, with no
   OCR execution, no PCRP, no acceptance, and no pages 010-020 processing.
5. Implement `P009TR-G1-VIRAL-003` as the crop-role contract: role-separated
   `source_region_box_px`, `human_review_crop_box_px`,
   `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`, with the right
   lower grey block marked complete/non-blocking.
6. Add crop QA for OCR/text evidence crops: edge/gutter checks, text-near-edge
   blockers, art/portrait/frame pollution blockers, page-map reconciliation,
   and semantic/text-map linkage to `text_evidence_crop_id`.
7. Add PCRP fail-closed guards and tests so `PCRP-G1-VIRAL-P009-001` rejects
   `P009TR-G1-VIRAL-002` and cannot proceed without current `P009TR-G1-VIRAL-003`
   crop-role QA.
8. Run Sol/Terra review on `P009TR-G1-VIRAL-003`; only after their OK and
   Bogdan review/route decision may a separate bounded authorization for
   `PCRP-G1-VIRAL-P009-001` be created.

## Documentation Checkpoint: doc-checkpoint-20260728T190000Z

Timestamp: 2026-07-28T19:00:00Z

Context:

- Bogdan replied with the exact review phrase:
  `g1unfpdp packet ok; proceed to prepare unsupported/negative fixture policy record over unsupported_profiles_scope, negative_fixture_obligations, invalidation_conditions, and fixture_admission_dependency; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push`.
- `G1UNFPDP-G1-VIRAL-001` was already ready as decision-prep only.

Result:

- `BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-DECISION-PREP-REVIEW-001`
  is consumed by `G1UNFPDPREV-G1-VIRAL-001`.
- `G1UNFPDPREV-G1-VIRAL-001` accepts the prep packet for policy-record
  preparation only and creates no policy decision.
- `BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-RECORD-001` is consumed by
  `G1UNFPR-G1-VIRAL-001`.
- `G1UNFPR-G1-VIRAL-001` prepares candidate policy decisions for unsupported
  profile scope, negative fixture obligations, invalidation conditions, and
  fixture-admission dependency.
- `BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-ACCEPTANCE-001` is consumed
  by `G1UNFPAR-G1-VIRAL-001`.
- `G1UNFPAR-G1-VIRAL-001` accepts the four unsupported/negative fixture policy
  decisions and resolves only the unsupported/negative fixture policy decision
  blocker.
- `BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-DECISION-PREP-001` is consumed by
  `G1FSFDP-G1-VIRAL-001`.
- `G1FSFDP-G1-VIRAL-001` prepares fixture strategy fit review questions only:
  strategy scope fit, positive fixture seed fit, negative fixture coverage fit,
  invalidation dependency, and admission dependency.
- `BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-ACCEPTANCE-001` is consumed by
  `G1FSFAR-G1-VIRAL-001`.
- `G1FSFAR-G1-VIRAL-001` accepts the fixture strategy fit decision over those
  five questions and resolves only the fixture strategy fit blocker.
- `BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-REFRESH-001` is consumed by
  `G1FARR-G1-VIRAL-001`.
- `G1FARR-G1-VIRAL-001` refreshes fixture admission readiness after the
  accepted unsupported/negative fixture policy and fixture strategy fit
  decisions, resolving only the readiness-refresh blocker.
- `BA-G1-VIRAL-FIXTURE-MANIFEST-PREP-001` is consumed by
  `G1FMP-G1-VIRAL-001`.
- `G1FMP-G1-VIRAL-001` prepares the future fixture manifest shape with one
  positive page-complete seed group and four negative fixture groups, but
  creates no actual fixture manifest and admits no fixtures.
- `BA-G1-VIRAL-FIXTURE-MANIFEST-ACCEPTANCE-001` is consumed by
  `G1FMR-G1-VIRAL-001`.
- `G1FMR-G1-VIRAL-001` records the fixture manifest shape with the accepted
  positive pages 001-020 seed group and four accepted negative fixture groups,
  but admits no fixtures.
- `BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-PREP-001` is consumed by
  `G1FADP-G1-VIRAL-001`.
- `G1FADP-G1-VIRAL-001` prepares fixture admission decision questions only and
  creates no fixture admission decision.
- `BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-ACCEPTANCE-001` is consumed by
  `G1FADAR-G1-VIRAL-001`.
- `G1FADAR-G1-VIRAL-001` accepts the fixture admission decision and admits the
  fixture manifest groups.
- `G1WGARR-G1-VIRAL-001` prepares whole Gate 1 acceptance readiness recheck
  material only before any whole Gate 1 acceptance.
- `G1WGADR-G1-VIRAL-001` accepts whole Gate 1 only for pages 001-020 and the
  `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups.
- `C01IPP-G1-VIRAL-001` prepares Core 0.1 implementation planning only from
  `G1WGADR-G1-VIRAL-001`; it identifies candidate work packages and a future
  first slice but creates no implementation authorization receipt and no
  runtime implementation.
- `C01IAR-G1-VIRAL-001` accepts `C01IPP-G1-VIRAL-001` as planning prep and
  prepares implementation authorization receipt material only. It records that
  runtime implementation remains unauthorized pending future first-slice
  prerequisites.
- `C01FSDP-G1-VIRAL-001` prepares first-slice design material only for
  `C01WP-01-phase-1-scaffold-contracts`; it creates no runtime implementation
  and no source-profile lock or acceptance.
- `C01SPLPR-G1-VIRAL-001` records source-profile parking only for the C01WP-01
  design-prep boundary; it creates no runtime source-profile lock, runtime
  source-profile acceptance, or runtime implementation.
- `C01FSARP-G1-VIRAL-001` prepares the first-slice Sol/Terra architecture
  review packet for `C01WP-01-phase-1-scaffold-contracts`; it creates no
  runtime implementation, runtime source-profile lock, or source-profile
  acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- `C01AMTR-G1-VIRAL-001` prepares acceptance-matrix claim/evidence trace review
  material for `C01WP-01`; it creates no runtime implementation, runtime
  source-profile lock, or source-profile acceptance beyond
  `C01SPLPR-G1-VIRAL-001`.
- `C01RSPLP-G1-VIRAL-001` records runtime source-profile parking for
  `C01WP-01` authorization-prep only; it creates no runtime implementation,
  runtime source-profile lock, or runtime source-profile acceptance.
- `C01RSAP-G1-VIRAL-001` prepares first-slice runtime authorization decision
  context for `C01WP-01` after `C01RSPLP-G1-VIRAL-001`; it creates no runtime
  authorization grant, runtime start, runtime implementation, runtime
  source-profile lock, or runtime source-profile acceptance.
- `C01RSAD-G1-VIRAL-001` records a non-executing first-slice runtime
  authorization decision for `C01WP-01` after `C01RSAP-G1-VIRAL-001`; it
  creates no runtime start/execution, runtime implementation, runtime
  source-profile lock, or runtime source-profile acceptance.
- `C01RSPLAD-G1-VIRAL-001` records a runtime source-profile
  lock-or-acceptance decision for `C01WP-01` after `C01RSAD-G1-VIRAL-001`; it
  records no runtime source-profile lock/acceptance, keeps the runtime source
  profile parked, and creates no runtime start/execution or implementation.
- `C01TETD-G1-VIRAL-001` completes the Sol/Terra-reviewed points 1-5
  readiness chain toward a future text extraction smoke trial; it creates no
  actual OCR, PDF parsing/text-layer extraction, text extraction, runtime
  implementation/start/execution, or page `021+` authorization.

Boundaries:

- Fixture admission decision acceptance only for the `G1FADAR-G1-VIRAL-001`
  admitted fixture manifest groups.
- Whole Gate 1 acceptance exists only under `G1WGADR-G1-VIRAL-001`.
- No whole source-profile acceptance beyond this Gate 1 record, new or broader
  fixture admission, page `021+` processing/authorization, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation, translation,
  proofreading, renderer/profile acceptance, implementation authorization
  receipt beyond `C01IAR`, runtime source-profile lock/acceptance, runtime
  implementation, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260730T123700Z

Timestamp: 2026-07-30T12:37:00Z

Context:

- Bogdan accepted `C01RSPLP-G1-VIRAL-001` as runtime source-profile parking
  decision material and authorized first-slice runtime authorization prep for
  `C01WP-01` with no runtime implementation, no runtime source-profile
  lock/acceptance, no OCR/render/PDF/raw mutation, no translation/proofreading,
  no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-RUNTIME-AUTHORIZATION-PREP-001` is
  consumed.
- `C01RSAP-G1-VIRAL-001` consumes `C01RSPLP-G1-VIRAL-001` as a reference-only
  runtime source-profile parking decision.
- The packet prepares first-slice runtime authorization decision context only.

Boundaries:

- Runtime authorization prep material only.
- No runtime authorization grant, runtime start, runtime implementation,
  runtime source-profile lock/acceptance, OCR execution/remediation rerun,
  source/OCR/render/PDF/raw mutation, translation/proofreading, page `021+`
  processing/authorization, new or broader fixture admission, push, or
  downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260730T131100Z

Timestamp: 2026-07-30T13:11:00Z

Context:

- Bogdan accepted `C01RSAP-G1-VIRAL-001` as first-slice runtime authorization
  prep material and authorized a first-slice runtime authorization decision for
  `C01WP-01` with no runtime implementation, no OCR/render/PDF/raw mutation, no
  translation/proofreading, no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-RUNTIME-AUTHORIZATION-DECISION-001` is
  consumed.
- `C01RSAD-G1-VIRAL-001` consumes `C01RSAP-G1-VIRAL-001`.
- The packet records a non-executing first-slice runtime authorization decision
  only.

Boundaries:

- Runtime authorization decision record material only.
- No runtime start/execution, runtime implementation, runtime source-profile
  lock/acceptance, OCR execution/remediation rerun, source/OCR/render/PDF/raw
  mutation, translation/proofreading, page `021+` processing/authorization,
  new or broader fixture admission, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260730T133000Z

Timestamp: 2026-07-30T13:30:00Z

Context:

- Bogdan accepted `C01RSAD-G1-VIRAL-001` as non-executing first-slice runtime
  authorization decision material and authorized a runtime source-profile
  lock-or-acceptance decision for `C01WP-01` with no runtime implementation, no
  runtime start/execution, no OCR/render/PDF/raw mutation, no
  translation/proofreading, no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-ACCEPTANCE-DECISION-001`
  is consumed.
- `C01RSPLAD-G1-VIRAL-001` consumes `C01RSAD-G1-VIRAL-001`.
- The packet records a runtime source-profile lock-or-acceptance decision only:
  no runtime source-profile lock is granted, no runtime source-profile
  acceptance is granted, and the runtime source profile remains parked.

Boundaries:

- Runtime source-profile lock-or-acceptance decision record material only.
- No runtime source-profile lock/acceptance, runtime start/execution, runtime
  implementation, OCR execution/remediation rerun, source/OCR/render/PDF/raw
  mutation, translation/proofreading, page `021+` processing/authorization,
  new or broader fixture admission, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260730T143300Z

Timestamp: 2026-07-30T14:33:00Z

Context:

- Bogdan instructed to do points 1-5 with Sol/Terra review instead of human
  review and to call him before point 6.

Result:

- `C01RSPLADMR-G1-VIRAL-001` records Sol/Terra machine-review acceptance of
  `C01RSPLAD-G1-VIRAL-001` for points 1-5 only.
- `C01RSPEP-G1-VIRAL-001` prepares runtime source-profile evidence surfaces
  without source observation or extraction.
- `C01RSPETD-G1-VIRAL-001` records future extraction-trial profile decision
  material without actual runtime profile lock/acceptance artifacts.
- `C01TETAP-G1-VIRAL-001` prepares future text extraction trial authorization
  context.
- `C01TETD-G1-VIRAL-001` records a non-executing future text extraction trial
  decision and leaves point 6 blocked until Bogdan is called.

Boundaries:

- Readiness/decision material only.
- No OCR/render/PDF parsing/text-layer extraction, actual text extraction,
  source/OCR/render/PDF/raw mutation, runtime implementation/start/execution,
  page `021+`, new or broader fixture admission, translation/proofreading,
  push, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260730T154800Z

Timestamp: 2026-07-30T15:48:00Z

Context:

- Bogdan accepted the P009 control-stand plan and authorized the first real
  bounded smoke extraction run with `теперь согласен, приступай`.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-001` is consumed.
- `C01TESP-G1-VIRAL-001` consumes `C01TETD-G1-VIRAL-001`.
- The smoke ran local Tesseract from frozen OCR candidate `OCM-G1-VIRAL-001`
  over only two read-only P009 text-evidence crop PNGs.
- Candidate-only outputs were written under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_smoke_p009_G1_VIRAL_001/`.
- The candidate text is noisy and not acceptance-ready: sequence similarity
  against `page_009_ocr_verified_text_map.md` is `0.460269`.

Boundaries:

- Candidate-only OCR smoke evidence.
- No page 009 source/review/reference/accepted-text asset is overwritten.
- No PDF parsing/text-layer extraction, render execution,
  source/OCR/render/PDF/raw mutation, runtime implementation/start/execution,
  source-profile acceptance, page `021+` processing/authorization, new or
  broader fixture admission, translation/proofreading, push, or downstream
  execution is created.
- Recommended next route is an OCR smoke remediation/preprocessing decision
  before broader extraction.

## Documentation Checkpoint: doc-checkpoint-20260730T162800Z

Timestamp: 2026-07-30T16:28:00Z

Context:

- Bogdan authorized the proposed next plan: commit the existing C01TESP smoke,
  then run a bounded P009 remediation/preprocessing matrix, then recommend only
  bounded P010/P015 consideration if the same-profile evidence improves.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-REMEDIATION-MATRIX-001`
  is consumed.
- `C01TESRM-G1-VIRAL-001` consumes `C01TESP-G1-VIRAL-001`.
- The matrix used a new fail-closed P009-specific runner and did not reuse the
  older broad remediation runner as-is.
- It tested 19 candidate preprocessing/PSM combinations over only the two
  read-only P009 text-evidence crop PNGs.
- Best candidate is `trim_mask_psm4` (`edge_mask_trim`, PSM 4), with sequence
  similarity `0.9993`, token recall `0.996324`, and improvement `0.539031`
  over the baseline `0.460269`.

Boundaries:

- Candidate-only remediation evidence.
- No page 009 source/review/reference/accepted-text asset is overwritten.
- No PDF parsing/text-layer extraction, render execution,
  source/OCR/render/PDF/raw mutation, runtime implementation/start/execution,
  source-profile acceptance, page `021+` processing/authorization, new or
  broader fixture admission, translation/proofreading, push, or downstream
  execution is created.
- Recommended next route is a same-profile bounded smoke consideration on P010
  or P015 only.

## Documentation Checkpoint: doc-checkpoint-20260730T173100Z

Timestamp: 2026-07-30T17:31:00Z

Context:

- Bogdan authorized "ок. пошли делать 010" after the P009 remediation matrix
  showed that the selected/recommended `trim_mask_psm4` profile should be
  checked against one more already accepted page before broader extraction.
- Sol and Terra both approved the intended scope with guardrails: exactly one
  candidate, P010-only text-evidence inputs, no matrix shape, and candidate-only
  wording.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P010-TRIM-MASK-PSM4-001` is
  consumed.
- `C01TESP010-G1-VIRAL-001` consumes `C01TESRM-G1-VIRAL-001`.
- The smoke used exactly one candidate: `trim_mask_psm4` (`edge_mask_trim`, PSM
  4), over four read-only P010 text-evidence crop PNGs in verified logical
  order.
- Sequence similarity against `page_010_ocr_verified_text_map.md` is
  `0.998867`; token recall is `0.995825`.

Boundaries:

- Candidate-only same-profile generalization evidence.
- No P010 source/review/reference/accepted-text/semantic/page-status asset is
  overwritten or accepted.
- No PDF parsing/text-layer extraction, render execution,
  source/OCR/render/PDF/raw mutation, runtime implementation/start/execution,
  source-profile acceptance, page `021+` processing/authorization, new or
  broader fixture admission, translation/proofreading, push, or downstream
  execution is created.
- Recommended next route is either one more bounded same-profile smoke on P015
  or stopping the smoke ladder, not page `021+`.

## Documentation Checkpoint: doc-checkpoint-20260730T195100Z

Timestamp: 2026-07-30T19:51:00Z

Context:

- Bogdan accepted committing `C01TESP010-G1-VIRAL-001` and authorized doing P015
  same-profile smoke next.
- Sol and Terra both approved the P015 scope with guardrails: exactly two P015
  text-evidence inputs, no visual anchor OCR, `reference_text_map` wording for
  `page_015_text_map.md`, and candidate-only evidence wording.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P015-TRIM-MASK-PSM4-001` is
  consumed.
- `C01TESP015-G1-VIRAL-001` consumes `C01TESRM-G1-VIRAL-001` and records
  `C01TESP010-G1-VIRAL-001` as prior same-profile smoke context.
- The smoke used exactly one candidate: `trim_mask_psm4` (`edge_mask_trim`, PSM
  4), over two read-only P015 text-evidence crop PNGs.
- Sequence similarity against `page_015_text_map.md` is `0.997252`; token
  recall is `0.993985`.

Boundaries:

- Candidate-only same-profile ladder evidence.
- No P015 source/review/reference/accepted-text/semantic/page-status asset is
  overwritten or accepted.
- No P015 visual anchor, full page image, triage duplicate, PDF/raw/source, or
  continuation page 016 is OCRed.
- No PDF parsing/text-layer extraction, render execution,
  source/OCR/render/PDF/raw mutation, runtime implementation/start/execution,
  source-profile acceptance, page `016+`/`021+` processing/authorization, new or
  broader fixture admission, translation/proofreading, push, or downstream
  execution is created.
- Recommended next route is a profile-lock/source-profile decision assessment
  or explicit parking; not page `021+`.

## Documentation Checkpoint: doc-checkpoint-20260730T201400Z

Timestamp: 2026-07-30T20:14:00Z

Context:

- The P009/P010/P015 same-profile smoke ladder was complete and committed.
- Bogdan accepted the next plan with `ок`: close the ladder as evidence,
  prepare a profile-lock decision packet, and run Sol/Terra gate.
- Sol and Terra both returned OK for points 1-3 only.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-CANDIDATE-PROFILE-DECISION-001` is
  consumed.
- Generated `C01TECPD-G1-VIRAL-001`, a Core 0.1 text extraction candidate
  profile decision packet.
- `trim_mask_psm4` (`edge_mask_trim`, Tesseract PSM 4) is frozen as a
  candidate profile for future config/replay decisions only.
- Evidence ladder: P009 remediation `0.9993` / `0.996324`, P010 same-profile
  `0.998867` / `0.995825`, P015 same-profile `0.997252` / `0.993985`.
- P015 remains labeled as `reference_text_map_not_ocr_verified`; it compares
  against `page_015_text_map.md`, not an OCR-verified text map.
- Recommended next route is frozen profile config or replay/regression smoke
  only if separately authorized.

Boundaries:

- Candidate-profile decision only.
- No OCR execution, OCR/source-profile acceptance, accepted text mutation,
  semantic/page-status mutation, PDF parsing/text-layer extraction, render
  execution, source/OCR/PDF/render/raw mutation, runtime implementation
  /start/execution, runtime source-profile lock/acceptance, page 016+/021+
  processing/authorization, translation/proofreading, push, or downstream
  execution.

## Documentation Checkpoint: doc-checkpoint-20260730T204700Z

Timestamp: 2026-07-30T20:47:00Z

Context:

- `C01TECPD-G1-VIRAL-001` was committed and froze `trim_mask_psm4` as a Core
  0.1 text extraction candidate profile only.
- Bogdan authorized doing both next layers: frozen profile config first, then
  replay/regression smoke.
- Sol and Terra approved the intended two-layer scope; config has no OCR, replay
  may run bounded OCR over exactly eight P009/P010/P015 crop inputs.

Result:

- Generated `C01TEFPC-G1-VIRAL-001`, the frozen reusable profile config for
  `trim_mask_psm4` (`edge_mask_trim`, Tesseract `-l eng --oem 1 --psm 4 txt
  tsv`) without OCR execution.
- Generated `C01TERSM-G1-VIRAL-001`, a candidate-only replay/regression smoke
  using only `C01TEFPC` and exactly P009/P010/P015 text-evidence crop PNGs.
- Replay metrics: P009 `0.997902` / `0.996324`, P010 `0.998867` / `0.995825`,
  P015 `0.997252` / `0.993985`.
- Aggregate replay minimum similarity is `0.997252`; minimum token recall is
  `0.993985`.

Boundaries:

- Config layer executes no OCR.
- Replay layer executes OCR only over the eight named text-evidence crop PNGs.
- No accepted text mutation, semantic/page-status mutation, PDF parsing
  /text-layer extraction, render execution, source/OCR/PDF/render/raw mutation,
  source-profile acceptance, runtime source-profile lock/acceptance, runtime
  implementation/start/execution, page 016+/021+ processing/authorization,
  translation/proofreading, push, or downstream execution.

## Documentation Checkpoint: doc-checkpoint-20260730T212000Z

Timestamp: 2026-07-30T21:20:00Z

Context:

- After `C01TERSM-G1-VIRAL-001`, Bogdan selected bounded replay expansion
  inside pages `001-020`.
- Sol and Terra rejected broad `001-020` replay and approved only a revised
  P011-only expansion scope with a new lane, new authorization, and exact
  P011 inputs.
- The layer reuses only the frozen `trim_mask_psm4` tuple from
  `C01TEFPC-G1-VIRAL-001`; it does not broaden the frozen config allowed-pages
  policy.

Result:

- Generated `C01TEREP011-G1-VIRAL-001`, the first bounded replay expansion
  inside `001-020`, limited to P011 only.
- Inputs were exactly `1b_P011-left-maya-continuation-secret-appearance-text-evidence.png`
  and `4b_P011-right-emily-profile-text-text-evidence.png`.
- Reference was `page_011_ocr_verified_text_map.md`.
- Similarity is `0.989944`; token recall is `1.0`.

Boundaries:

- Candidate-only metrics/report/summary/manifest output only.
- No persisted raw OCR, prepared input, or candidate text artifacts.
- No broad `001-020` replay, no config allowed-pages broadening, no accepted
  text mutation, semantic/page-status mutation, PDF parsing/text-layer
  extraction, render execution, source/OCR/PDF/render/raw mutation,
  source-profile acceptance, runtime source-profile lock/acceptance, runtime
  implementation/start/execution, page 012+/016+/021+ processing/authorization,
  translation/proofreading, push, or downstream execution.

## Documentation Checkpoint: doc-checkpoint-20260730T075500Z

Timestamp: 2026-07-30T07:55:00Z

Context:

- Bogdan accepted `C01AMTR-G1-VIRAL-001` as acceptance-matrix trace review
  material and authorized a runtime source-profile lock-or-parking decision for
  `C01WP-01` with no runtime implementation, no OCR/render/PDF/raw mutation, no
  translation/proofreading, no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-PARKING-DECISION-001`
  is consumed.
- `C01RSPLP-G1-VIRAL-001` consumes `C01AMTR-G1-VIRAL-001`.
- The decision parks runtime source-profile lock/acceptance for first-slice
  authorization-prep only.

Boundaries:

- Runtime source-profile parking decision material only.
- No runtime implementation, runtime source-profile lock/acceptance, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+` processing/authorization, new or
  broader fixture admission, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260730T003200Z

Timestamp: 2026-07-30T00:32:00Z

Context:

- Bogdan accepted `C01FSARP-G1-VIRAL-001` as first-slice architecture review
  packet material and authorized acceptance-matrix trace review for `C01WP-01`
  with no runtime implementation, no source-profile lock or acceptance beyond
  `C01SPLPR`, no OCR/render/PDF/raw mutation, no translation/proofreading, no
  page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-ACCEPTANCE-MATRIX-TRACE-REVIEW-001` is consumed.
- `C01AMTR-G1-VIRAL-001` consumes `C01FSARP-G1-VIRAL-001`.
- The review maps C01WP-01 acceptance-matrix claims to existing bounded
  evidence before any runtime authorization.

Boundaries:

- Acceptance-matrix trace review material only.
- No runtime implementation, runtime source-profile lock/acceptance, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+` processing/authorization, new or
  broader fixture admission, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260730T001800Z

Timestamp: 2026-07-30T00:18:00Z

Context:

- Bogdan accepted `C01SPLPR-G1-VIRAL-001` as source-profile receipt material
  and authorized a Core 0.1 first-slice architecture review packet for
  `C01WP-01` with no runtime implementation, no source-profile lock or
  acceptance beyond `C01SPLPR`, no OCR/render/PDF/raw mutation, no
  translation/proofreading, no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-ARCHITECTURE-REVIEW-PACKET-001` is
  consumed.
- `C01FSARP-G1-VIRAL-001` consumes `C01SPLPR-G1-VIRAL-001`.
- The packet prepares Sol architecture review targets and Terra critique
  targets for `C01WP-01-phase-1-scaffold-contracts`.

Boundaries:

- Architecture review packet material only.
- No runtime implementation, runtime source-profile lock/acceptance, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+` processing/authorization, new or
  broader fixture admission, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260729T232900Z

Timestamp: 2026-07-29T23:29:00Z

Context:

- Bogdan accepted `C01FSDP-G1-VIRAL-001` as first-slice design prep and
  authorized a single source-profile lock-or-parking receipt for `C01WP-01`
  with no runtime implementation, no source-profile lock or acceptance beyond
  this receipt, no OCR/render/PDF/raw mutation, no translation/proofreading, no
  page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-SINGLE-SOURCE-PROFILE-LOCK-OR-PARKING-RECEIPT-001` is consumed.
- `C01SPLPR-G1-VIRAL-001` consumes `C01FSDP-G1-VIRAL-001`.
- The receipt records source-profile parking only for the C01WP-01 design-prep
  boundary and keeps runtime source-profile lock/parking as a future separate
  prerequisite.

Boundaries:

- Source-profile receipt material only.
- No runtime implementation, runtime source-profile lock/acceptance, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+` processing/authorization, new or
  broader fixture admission, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260729T222500Z

Timestamp: 2026-07-29T22:25:00Z

Context:

- Bogdan accepted `C01IAR-G1-VIRAL-001` as receipt material and authorized Core
  0.1 first-slice design prep for `C01WP-01-phase-1-scaffold-contracts` with no
  runtime implementation, no source-profile lock or acceptance beyond
  `G1WGADR`, no OCR/render/PDF/raw mutation, no translation/proofreading, no
  page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-DESIGN-PREP-001` is consumed.
- `C01FSDP-G1-VIRAL-001` consumes `C01IAR-G1-VIRAL-001`.
- The packet prepares module-boundary, artifact-identity, lineage-trace, and
  acceptance-matrix trace design surfaces for future review.

Boundaries:

- First-slice design prep only.
- No runtime implementation, source-profile lock/acceptance, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+` processing/authorization, new or
  broader fixture admission, push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260729T215500Z

Timestamp: 2026-07-29T21:55:00Z

Context:

- Bogdan accepted `C01IPP-G1-VIRAL-001` as planning prep and authorized a Core
  0.1 implementation authorization receipt with no runtime implementation, no
  OCR/render/PDF/raw mutation, no translation/proofreading, no page `021+`, no
  source-profile acceptance beyond `G1WGADR`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-IMPLEMENTATION-AUTHORIZATION-RECEIPT-001` is consumed.
- `C01IAR-G1-VIRAL-001` consumes `C01IPP-G1-VIRAL-001`.
- The receipt records the accepted Gate 1 scope and the candidate first slice,
  but keeps runtime implementation unauthorized because first-slice
  source-profile, acceptance-matrix, Sol/Terra, and roadmap-validation
  prerequisites remain unsatisfied in this packet.

Boundaries:

- Implementation authorization receipt material only.
- No runtime implementation, first-slice design prep authorization, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+` processing/authorization,
  source-profile acceptance beyond `G1WGADR`, new or broader fixture admission,
  push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260729T132100Z

Timestamp: 2026-07-29T13:21:00Z

Context:

- Bogdan authorized `core_0_1_implementation_planning_prep` from
  `G1WGADR-G1-VIRAL-001` with no implementation, no OCR/render/PDF/raw
  mutation, no translation/proofreading, no page `021+`, no source-profile
  acceptance beyond `G1WGADR`, no push, and commit.

Result:

- `BA-G1-VIRAL-CORE-0-1-IMPLEMENTATION-PLANNING-PREP-001` is consumed.
- `C01IPP-G1-VIRAL-001` consumes `G1WGADR-G1-VIRAL-001`.
- The packet decomposes Core 0.1 into bounded work-package planning and marks
  `C01WP-01-phase-1-scaffold-contracts` as the candidate first implementation
  slice for a future separate authorization.

Boundaries:

- Core 0.1 implementation planning prep only.
- No implementation authorization receipt, runtime implementation, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+` processing/authorization,
  source-profile acceptance beyond `G1WGADR`, new or broader fixture admission,
  push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260729T101000Z

Timestamp: 2026-07-29T10:10:00Z

Context:

- Bogdan authorized proceeding with the proposed bounded whole Gate 1 acceptance
  readiness recheck prep and commit after `G1FADAR-G1-VIRAL-001`.

Result:

- `BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-READINESS-RECHECK-PREP-001` is consumed.
- `G1WGARR-G1-VIRAL-001` consumes `G1FADAR-G1-VIRAL-001`.
- The packet prepares review questions for whole Gate 1 acceptance scope, page
  `021+` boundary, acceptance-record boundary, and downstream boundary.

Boundaries:

- Whole Gate 1 acceptance readiness recheck prep only.
- No whole Gate 1 acceptance, whole source-profile acceptance, new or broader
  fixture admission, page `021+` processing/authorization, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading/implementation, push, or downstream action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260729T112700Z

Timestamp: 2026-07-29T11:27:00Z

Context:

- Bogdan accepted `G1WGARR-G1-VIRAL-001` and authorized preparing a whole Gate
  1 acceptance decision record limited to pages 001-020 and the `G1FADAR`
  admitted fixture manifest groups.

Result:

- `BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-DECISION-RECORD-001` is consumed.
- `G1WGADR-G1-VIRAL-001` consumes `G1WGARR-G1-VIRAL-001`.
- Whole Gate 1 is accepted only for pages 001-020 and the
  `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups.

Boundaries:

- Whole Gate 1 acceptance record only.
- No page `021+` processing/authorization, no source-profile acceptance beyond
  this Gate 1 record, no new or broader fixture admission, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading/implementation, push, or downstream action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260728T210800Z

Timestamp: 2026-07-28T21:08:00Z

Context:

- Bogdan authorized `fixture_admission_readiness_refresh` with exact boundaries:
  no fixture admission, no fixture manifest, no whole Gate 1 acceptance, no page
  `021+`, and no push.

Result:

- `BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-REFRESH-001` is consumed.
- `G1FARR-G1-VIRAL-001` consumes `G1SP-G1-VIRAL-017`,
  `G1FARP-G1-VIRAL-001`, `G1UNFPAR-G1-VIRAL-001`, and
  `G1FSFAR-G1-VIRAL-001`.
- Fixture admission readiness is refreshed after accepted unsupported/negative
  fixture policy and fixture strategy fit decisions.
- The fixture admission readiness refresh blocker is resolved only for this
  readiness layer.

Boundaries:

- No fixture admission, fixture manifest creation, whole Gate 1 acceptance,
  whole source-profile acceptance, page `021+` processing/authorization, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation, translation,
  proofreading, renderer/profile acceptance, implementation, push, or
  downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260728T213200Z

Timestamp: 2026-07-28T21:32:00Z

Context:

- Bogdan chose to continue in order after `G1FARR-G1-VIRAL-001` and authorized
  `fixture_manifest_prep` with no fixture admission, no whole Gate 1
  acceptance, no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-FIXTURE-MANIFEST-PREP-001` is consumed.
- `G1FMP-G1-VIRAL-001` consumes `G1FARR-G1-VIRAL-001`.
- The packet proposes a future manifest shape: one positive page-complete seed
  group over pages 001-020 and four negative fixture groups from the accepted
  unsupported/negative policy.
- The packet prepares four review questions for manifest shape and admission
  dependency.

Boundaries:

- Fixture manifest prep only.
- No actual fixture manifest creation, fixture admission, whole Gate 1
  acceptance, whole source-profile acceptance, page `021+`
  processing/authorization, OCR execution/remediation rerun,
  source/OCR/render/PDF/raw mutation, translation/proofreading/implementation,
  push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260728T214800Z

Timestamp: 2026-07-28T21:48:00Z

Context:

- Bogdan accepted `G1FMP-G1-VIRAL-001` as the fixture manifest prep packet and
  authorized preparing a fixture manifest acceptance record with no fixture
  admission, no whole Gate 1 acceptance, no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-FIXTURE-MANIFEST-ACCEPTANCE-001` is consumed.
- `G1FMR-G1-VIRAL-001` consumes `G1FMP-G1-VIRAL-001`.
- The fixture manifest record contains one positive page-complete seed group
  over pages 001-020 and four negative fixture groups from the accepted
  unsupported/negative policy.
- Only fixture manifest review is resolved.

Boundaries:

- Fixture manifest record only.
- No fixture admission, whole Gate 1 acceptance, whole source-profile
  acceptance, page `021+` processing/authorization, OCR execution/remediation
  rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading/implementation, push, or downstream action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260728T221800Z

Timestamp: 2026-07-28T22:18:00Z

Context:

- Bogdan authorized `fixture_admission_decision_prep` with no fixture
  admission, no whole Gate 1 acceptance, no page `021+`, no push, and commit.

Result:

- `BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-PREP-001` is consumed.
- `G1FADP-G1-VIRAL-001` consumes `G1FMR-G1-VIRAL-001`.
- The packet prepares five fixture admission review questions: positive group
  admission scope, negative group admission scope, invalidation/lineage
  blockers, admission decision boundary, and whole Gate 1 dependency.

Boundaries:

- Fixture admission decision prep only.
- No fixture admission decision, fixture admission, whole Gate 1 acceptance,
  whole source-profile acceptance, page `021+` processing/authorization, OCR
  execution/remediation rerun, source/OCR/render/PDF/raw mutation,
  translation/proofreading/implementation, push, or downstream action is
  created.

## Documentation Checkpoint: doc-checkpoint-20260728T230000Z

Timestamp: 2026-07-28T23:00:00Z

Context:

- Bogdan accepted `G1FADP-G1-VIRAL-001` as fixture admission decision prep and
  authorized preparing a fixture admission decision acceptance record with no
  whole Gate 1 acceptance, no page `021+`, and no push.

Result:

- `BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-ACCEPTANCE-001` is consumed.
- `G1FADAR-G1-VIRAL-001` consumes `G1FADP-G1-VIRAL-001`.
- The fixture admission decision is accepted and the fixture manifest groups
  are admitted.
- Only the fixture admission decision blocker is resolved.

Boundaries:

- Fixture admission decision acceptance only.
- No whole Gate 1 acceptance, whole source-profile acceptance, page `021+`
  processing/authorization, OCR execution/remediation rerun,
  source/OCR/render/PDF/raw mutation, translation/proofreading/implementation,
  push, or downstream action is created.

## Documentation Checkpoint: doc-checkpoint-20260730T215300Z

Timestamp: 2026-07-30T21:53:00Z

Context:

- Bogdan requested a bounded `001-020` replay overview after `C01TEREP011`.
- Sol/Terra narrowed the scope to overview/report only: reuse only the frozen
  `trim_mask_psm4` tuple, do not broaden `C01TEFPC` allowed pages, and do not
  remediate weak pages in the same layer.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-OVERVIEW-REPLAY-001-020-TRIM-MASK-PSM4-001`
  is consumed.
- `C01TEOR020-G1-VIRAL-001` records pages `001`-`008` as ineligible and runs
  pages `009`-`020` using the frozen tuple only.
- Weak pages are `012`, `013`, `014`, `016`, `017`, `018`, `019`, and `020`.
- P015 is reference-risk only because its reference is not OCR-verified.

Boundaries:

- Candidate-only overview/report/metrics evidence only.
- No remediation, alternate preprocessing, alternate PSM, crop/reference repair,
  accepted text mutation, semantic/page-status mutation, PDF parsing/text-layer
  extraction, render execution, source/OCR/PDF/render/raw mutation, persisted
  raw/prepared/candidate text artifacts, runtime implementation/start/execution,
  runtime source-profile lock/acceptance, page `021+`, translation/proofreading,
  push, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260730T221500Z

Timestamp: 2026-07-30T22:15:00Z

Context:

- Bogdan approved continuing through the planned sequence after the `001-020`
  overview: commit the overview, diagnose weak pages, probe P018 remediation,
  mini-replay any P018 fix, and update the route decision.

Result:

- `C01TEOR020-G1-VIRAL-001` was committed first as `3d9ebc2a`.
- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-WEAK-DIAGNOSTICS-P018-REMEDIATION-001`
  is consumed.
- `C01TEWDR-G1-VIRAL-001` persists diagnostic artifacts for weak pages `012`,
  `013`, `014`, `016`, `017`, `018`, `019`, and `020`.
- P018 best candidate is `wide_edge_mask_trim_psm4_normal`, improving P018
  similarity from `0.298585` to `0.814888` and token recall from `0.971485` to
  `0.976401`.
- Mini-replay shows this is not a broad fix: it improves P017, but does not
  resolve P019 or P014.

Boundaries:

- Candidate-only diagnostics/remediation evidence only.
- No accepted text mutation, semantic/page-status mutation, source/raw
  mutation, PDF parsing/text-layer extraction, render execution, runtime
  implementation/start/execution, runtime source-profile lock/acceptance,
  page `021+`, translation/proofreading, push, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260801T122000Z

- Created: 2026-08-01T12:20:00Z
- Type: status
- Summary: Recorded Core 0.1 complex-page OCR input-surface policy after
  P017/P018 full-page geometry evidence.

Completed:

- Updated Sourcefold AGENTS guidance so review crops are not treated as
  automatically OCR-safe for complex/tight pages.
- Declared `AM-04-03` and `AM-G1-05A` acceptance criteria for independent OCR
  geometry and input-surface labeling.
- Added Gate 1 OCR input surface policy separating `review_crop`,
  `ocr_candidate_crop`, `full_page_region`, and reference-guided support
  evidence.
- Linked the policy synchronization to prior probe evidence in
  `doc-checkpoint-20260730T235000Z`; this checkpoint does not restate or
  promote that evidence.

Next:

- Decide whether to promote full-page-derived geometry as the Core 0.1
  complex-page OCR candidate policy or park it explicitly.
- Keep page `021+`, source/profile acceptance, accepted text mutation, runtime
  implementation, translation/proofreading, push, and broader fixture admission
  blocked until separately authorized.

Blockers:

- `C01TEFG017018` is candidate-only evidence; P017/P018 references remain
  `reference_text_map_not_ocr_verified` and do not create
  source/profile/page-status/page-complete acceptance.

Roadmap nodes:

- `phase-0`
- `gate-01-source-profile`
- `gate-01-qualification-protocol`
- `gate-01-page-map-readiness-pipeline`

## Documentation Checkpoint: doc-checkpoint-20260801T140300Z

- Created: 2026-08-01T14:03:00Z
- Type: text-extraction-input-surface-policy-implementation-prep
- Summary: Planned Sol/Terra-reviewed `C01TEISP-G1-VIRAL-001`, a Core 0.1
  OCR input-surface router/contract implementation-prep lane with mandatory
  similarity/token-recall result evaluation.

Completed:

- Added `core_0_1_input_surface_policy_implementation_prep_plan.md` as the
  bounded design plan for universalizing the P017/P018 OCR lesson.
- The plan requires explicit `ocr_input_surface` metadata for OCR runs,
  separates `artifact_role` from surface class, and handles `review_crop`,
  `text_evidence_crop`, `ocr_candidate_crop`, and `full_page_region` surfaces.
- Sol/Terra review is folded in: `acceptance_evidence` is rejected in this
  lane, `review_crop`/`text_evidence_crop` fail closed unless explicitly
  `smoke_non_promotable`, and `full_page_region` requires a bounded
  authorization id, page family, region policy, and baseline-negative reason.
- The plan defines a two-stage router: baseline first for allowed candidate
  crops, then full-page-derived or separately authorized OCR-safe geometry for
  high-recall / low-sequence-similarity geometry failures.
- The plan adds mandatory result evaluation with both sequence similarity and
  token recall. P018 `0.999466` similarity / `0.996067` token recall is an
  `observed_control_measurement` for diagnostic deltas and structure/
  completeness assessment, not a hard threshold.

Next:

- After the planning commit, start the bounded implementation slice without
  broadening into OCR execution, runtime integration, policy promotion, or
  source/profile acceptance.

Blockers:

- This is planning/design only. No OCR execution, accepted text mutation,
  semantic/page-status mutation, source/profile/page-complete acceptance, page
  `021+`, runtime start/execution, translation/proofreading, push, or source/
  profile lock is created.
- The P018 metric anchor is a required diagnostic comparison, not a standalone
  pass/fail, policy-promotion, or acceptance threshold.
- `C01TEISP` cannot promote or park `C01TEFG017018`; only a future separate
  decision can do that.

Roadmap nodes:

- `phase-0`
- `gate-01-source-profile`
- `gate-01-qualification-protocol`
- `gate-01-page-map-readiness-pipeline`

## Documentation Checkpoint: doc-checkpoint-20260802T080000Z

- Created: 2026-08-02T08:00:00Z
- Type: text-extraction-input-surface-router-static-implementation
- Summary: Recorded committed `C01TEISP-G1-VIRAL-001` static OCR
  input-surface router/contract implementation and 001-020 replay result.

Completed:

- Recorded commits `6507f386` and `a01da448` as the bounded static
  implementation slice for `scripts/ocr_input_surface_policy.py` and
  `tests/test_ocr_input_surface_policy.py`.
- The router validates `ocr_input_surface` metadata, rejects unsafe or
  incomplete surfaces, rejects `acceptance_evidence`, blocks page `021+`, and
  consumes only static metadata plus saved score summaries.
- Static 001-020 replay routes `001`-`008` as `not_run_ineligible`,
  `009`/`010`/`011`/`015` as `baseline_ok`,
  `012`/`013`/`016`/`017`/`018`/`020` as
  `geometry_probe_required`, and `014`/`019` as
  `park_candidate_policy`.
- The replay changed the geometry-diagnosis detail: baseline OK remains
  similarity `>= 0.997` and token recall `>= 0.993`, while
  geometry-diagnosis can trigger at token recall `>= 0.97` when weak sequence
  and geometry/order flags are present.

Next:

- Prepare a separate bounded geometry-probe execution-prep lane for pages
  routed `geometry_probe_required`, starting with `012`, `013`, `016`, `017`,
  `018`, and `020`.
- Keep `014` and `019` parked until a lower-recall failure family is named.
- Run Sol/Terra on exact probe inputs, outputs, run ids, invalidation rules,
  and hash-manifest behavior before any OCR/runtime command.

Blockers:

- Static routing evidence does not execute OCR, render pages, parse PDFs, read
  PDF text layers, write non-temp OCR artifacts, mutate accepted source/status
  material, promote/park `C01TEFG017018`, create source/profile/page-status/
  page-complete acceptance, authorize page `021+`, translation/proofreading,
  push, or runtime integration.

Roadmap nodes:

- `phase-0`
- `gate-01-source-profile`
- `gate-01-qualification-protocol`
- `gate-01-page-map-readiness-pipeline`

## Documentation Checkpoint: doc-checkpoint-20260802T084500Z

- Created: 2026-08-02T08:45:00Z
- Type: text-extraction-geometry-probe-012-013-016-017-018-020
- Summary: Ran bounded `C01TEGP012013016017018020-G1-VIRAL-001` geometry
  probe after Sol/Terra review and recorded diagnostic results.

Completed:

- Added the geometry-probe execution-prep plan, fail-closed runner, and tests.
- Sol/Terra blocked the first draft until lineage hashes, strict
  `ocr_input_surface` validation, diagnostic-only wording, and negative tests
  were added. The fixed scope passed review before OCR execution.
- The first `_G1_VIRAL_001` output root stopped fail-closed before a complete
  report/manifest because triage `crop_box_px` was initially interpreted as
  `x1,y1,x2,y2`; it is marked incomplete/stale and not usable as evidence.
- Corrected `_G1_VIRAL_002` treats triage boxes as `x,y,width,height`, uses
  full-page PNG geometry and Tesseract only, validates per-region
  `ocr_input_surface`, seals candidate hashes before reference scoring, and
  emits report/summary/manifest.

Result:

- P017 and P018 controls still meet the diagnostic threshold:
  P017 `0.99923` similarity / `0.997859` token recall, P018 `0.999466` /
  `0.996067`.
- P012, P013, P016, and P020 do not meet the diagnostic threshold despite high
  token recall: P012 `0.98769` / `0.998024`, P013 `0.242772` / `0.993939`,
  P016 `0.98277` / `0.991089`, P020 `0.994304` / `0.998833`.

Next:

- Treat P017/P018 geometry as a confirmed control family.
- Do not promote the generic triage-box geometry family for P012/P013/P016/P020.
- Split the next research by failure family: P013 order/assembly first, then
  P012/P016/P020 high-recall structure repair.
- Keep P014/P019 parked until their lower-recall failure family is separately
  named.
- Add the iterative failed-page loop as the governing continuation: classify
  the failure, ask Sol for the next bounded change, ask Terra to critique it,
  run one bounded attempt after a clean gate, commit the stage, compare
  candidates by page type, and let only selected winners enter a future
  production output folder.

Blockers:

- Candidate-only diagnostic evidence only. No accepted text mutation,
  semantic/page-status mutation, source/profile/page-complete acceptance,
  policy promotion, page `021+`, translation/proofreading, push, or runtime
  integration is created.

Roadmap nodes:

- `phase-0`
- `gate-01-source-profile`
- `gate-01-qualification-protocol`
- `gate-01-page-map-readiness-pipeline`

## Documentation Checkpoint: doc-checkpoint-20260802T092500Z

- Created: 2026-08-02T09:25:00Z
- Type: text-extraction-iterative-failure-loop
- Summary: Added the governing loop for failed OCR pages and future production
  assembly from selected best methods only.

Completed:

- Added the failed-page cycle to the geometry-probe plan: classify failure,
  get Sol proposal, get Terra critique, run one bounded attempt, score,
  commit, compare candidates, and keep history restorable.
- Declared the method-registry direction: Sourcefold should retain best
  extraction method per page or page family.
- Declared the later production assembly target: an automatic selector either
  uses the known best method per page or runs all authorized methods and picks
  the best diagnostic result.
- Added the end-to-end `001`-`020` acceptance loop: run all twenty pages,
  inspect failures, improve failed page/page-family methods, register winners,
  then rerun all twenty pages from the same input set until the automatic
  pipeline succeeds on the first pass.

Next:

- Commit the current probe/cycle checkpoint.
- Start P013 as the first order/assembly failure-family lane.
- After P013, group P012/P016/P020 under high-recall structure repair.
- Once all failed page families have selected methods, implement the automatic
  selector/assembly script and require a clean `001`-`020` first-pass run into
  a production output folder with no failed/superseded variants.

Blockers:

- Production assembly is not authorized by this checkpoint. Failed/superseded
  candidates stay in evidence runs; the future production folder may contain
  only selected best page outputs plus the assembly manifest.

Roadmap nodes:

- `phase-0`
- `gate-01-source-profile`
- `gate-01-qualification-protocol`
- `gate-01-page-map-readiness-pipeline`

## Documentation Checkpoint: doc-checkpoint-20260730T224600Z

Timestamp: 2026-07-30T22:46:00Z

Context:

- Bogdan asked why visually aligned page/crop geometry still causes OCR edge
  loss and then authorized trying the P018/P017 second pass.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SECOND-PASS-P018-P017-CROP-SAFE-001`
  is consumed.
- `C01TEP2P018P017-G1-VIRAL-001` tests no-trim, extra-padding, soft-trim, and
  threshold variants with PSM `4`, `6`, and `11` for pages `018` and `017`.
- Best P018 candidate is `wide_edge_mask_trim_psm11`, similarity `0.81659`,
  token recall `0.974435`.
- Best P017 candidate is `wide_edge_mask_trim_psm4`, similarity `0.825557`,
  token recall `0.987152`.
- No no-trim/extra-padding variant reaches an OK-level result.

Boundaries:

- Candidate-only second-pass remediation evidence only.
- No accepted text mutation, semantic/page-status mutation, source/raw
  mutation, PDF parsing/text-layer extraction, render execution, runtime
  implementation/start/execution, runtime source-profile lock/acceptance,
  page `021+`, translation/proofreading, push, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260730T230600Z

Timestamp: 2026-07-30T23:06:00Z

Context:

- Bogdan authorized a bounded dry-run loop for P018/P017 without intermediate
  human stops.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-AUTO-SEARCH-P018-P017-COLUMN-LINE-001`
  is consumed.
- `C01TEAS018017-G1-VIRAL-001` tests bbox and column/line segmentation
  candidates for pages `018` and `017` only.
- The run exhausted its candidate budget without finding an OK-level candidate.
- Best P018 is `bbox_pad24_psm6`, similarity `0.492065`, token recall
  `0.978368`.
- Best P017 is `bbox_pad24_psm6`, similarity `0.825397`, token recall
  `0.987152`.
- The bbox/line-band path did not improve on the committed second-pass P018
  result.

Boundaries:

- Candidate-only auto-search evidence only.
- No accepted text mutation, semantic/page-status mutation, source/raw
  mutation, PDF parsing/text-layer extraction, render execution, runtime
  implementation/start/execution, runtime source-profile lock/acceptance,
  page `021+`, translation/proofreading, push, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260730T232500Z

Timestamp: 2026-07-30T23:25:00Z

Context:

- Bogdan authorized broad research until a useful result was found.
- Independent OCR attempts on P018/P017 failed to reach OK-level, so the next
  bounded probe tested reference-guided repair.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REFERENCE-GUIDED-REPAIR-P018-P017-001`
  is consumed.
- `C01TERG018017-G1-VIRAL-001` uses committed second-pass OCR candidates as
  support evidence and reference text maps as the source of truth.
- P018 support ratio is `0.988201`; P017 support ratio is `0.993576`.
- Repaired candidates reach similarity `1.0` and token recall `1.0`.
- This does not count as independent OCR acceptance.

Boundaries:

- Candidate-only reference-guided repair evidence only.
- No accepted text mutation, semantic/page-status mutation, source/raw
  mutation, PDF parsing/text-layer extraction, render execution, runtime
  implementation/start/execution, runtime source-profile lock/acceptance,
  page `021+`, translation/proofreading, push, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260730T235000Z

Timestamp: 2026-07-30T23:50:00Z

Context:

- Bogdan rejected the reference-guided repair conclusion as the desired OCR
  policy and asked for a retry with Sol/Terra review.
- Sol/Terra found that P017/P018 were being OCR'd from clipped review crops and
  recommended full-page-derived geometry instead.

Result:

- `BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FULL-PAGE-GEOMETRY-P018-P017-001`
  is consumed.
- `C01TEFG017018-G1-VIRAL-001` generates candidates from full-page PNG geometry
  and Tesseract only, then scores references after candidate hashes are sealed.
- P018 best independent candidate is `full_page_expanded_overlap_psm4`,
  similarity `0.999466`, token recall `0.996067`.
- P017 best independent candidate is `full_page_bright_title_body_psm7_4_4`,
  similarity `0.99923`, token recall `0.997859`.
- Both pages reach OK-level metrics without reference-guided repair.
- References remain `reference_text_map_not_ocr_verified`, so this is
  candidate-only independent OCR evidence, not source/profile/page-status
  acceptance.

Boundaries:

- Candidate-only full-page geometry OCR evidence only.
- No accepted text mutation, semantic/page-status mutation, source/raw
  mutation, PDF parsing/text-layer extraction, render execution, runtime
  implementation/start/execution, runtime source-profile lock/acceptance,
  page `021+`, translation/proofreading, push, or downstream execution is
  created.

## Documentation Checkpoint: doc-checkpoint-20260802T101500Z

Timestamp: 2026-08-02T10:15:00Z

Context:

- Bogdan asked to continue the `001`-`020` failed-page loop.
- P013 was selected first because the geometry probe showed high recall but
  severe order/assembly failure.
- Sol proposed a seam-dedupe assembly diagnostic; Terra required tighter
  deletion proof, pinned `_G1_VIRAL_002` lineage, explicit diagnostic gates,
  and no executable no-expansion OCR variant in this lane.

Result:

- Generated `C01TEP013SDD-G1-VIRAL-001`.
- The lane used sealed `_G1_VIRAL_002` P013 raw OCR text only and executed no
  OCR.
- Strict suffix-to-prefix seam dedupe found no exact deletion at the declared
  seams.
- Both fixed variants scored similarity `0.25788` and token recall `0.993939`;
  diagnostic threshold met is `False`.
- Dedupe-only is not the P013 winner. P013 remains in the failed-page loop and
  the next step is a new Sol proposal, likely non-overlapping/no-expansion
  geometry or logical-region re-OCR.

Boundaries:

- Candidate-only diagnostic assembly evidence.
- No OCR execution, reference-guided token insertion, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, PDF parsing/text-layer
  extraction, render execution, runtime implementation/start/execution,
  production assembly, method-registry winner, selector rule, page `021+`,
  translation/proofreading, push, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T150500Z

Timestamp: 2026-08-02T15:05:00Z

Context:

- Structural suppression improved P013 to `0.914027 / 0.993939`, leaving a
  smaller but still failing assembly gap.
- Sol/Terra required exact authorization matching, scorer-only reference
  loading after hash sealing, SSP-best floor guards, and a declared seam rule
  with boundary and token-containment proof.

Result:

- Generated `C01TEP013SAC-G1-VIRAL-001`.
- No OCR was executed; all candidate text, normalized text, retained-record
  trace, suppression-ledger, and assembly-trace artifacts were hash-sealed
  before reference scoring.
- Best variants `p013_sac_d_noise_then_declared_seam_fracture` and
  `p013_sac_e_paragraph_join_d` both scored similarity `0.998915`, token recall
  `0.993939`, diagnostic threshold met `True`.
- This is P013 method-registry candidate evidence, but selector and production
  behavior remain unchanged until separately reviewed.

Boundaries:

- Candidate-only P013 diagnostic assembly evidence.
- No OCR execution, reference-guided token insertion, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, PDF parsing/text-layer
  extraction, render execution, runtime implementation/start/execution,
  production assembly, selector rule, page `021+`, translation/proofreading,
  push, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T142500Z

Timestamp: 2026-08-02T14:25:00Z

Context:

- Expanded lane-order improved P013 to `0.433325 / 0.993939`, proving layout
  assembly matters but still leaving a large structure gap.
- Sol/Terra blocked the first structural-suppression prep until candidate
  generation became fully sealed before reference scoring and A0/C preserved
  the ELO floor.

Result:

- Generated `C01TEP013SSP-G1-VIRAL-001`.
- No OCR was executed; all candidate artifacts were generated and hash-sealed
  before reference scoring.
- Best variant `p013_ssp_a_near_overlap_confidence` scored similarity
  `0.914027`, token recall `0.993939`, diagnostic threshold met `False`.
- This is the strongest P013 structure result so far, but not a winner.

Boundaries:

- Candidate-only P013 diagnostic assembly evidence.
- No OCR execution, reference-guided token insertion, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, PDF parsing/text-layer
  extraction, render execution, runtime implementation/start/execution,
  production assembly, method-registry winner, selector rule, page `021+`,
  translation/proofreading, push, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T133500Z

Timestamp: 2026-08-02T13:35:00Z

Context:

- P013 seam dedupe safely failed and committed the first failed-page loop
  history stage.
- Sol proposed fresh no-expansion geometry OCR; Terra tightened the clipping,
  naming, OCR-profile, and registry-candidate gates.

Result:

- Generated `C01TEP013GNO-G1-VIRAL-001`.
- P013 OCR ran only over deterministic full-page-derived non-overlap crops
  with no expansion and no padding, using fixed `eng_oem1_psm4`.
- The three fixed assemblies all scored similarity `0.251286`, token recall
  `0.987879`, diagnostic threshold met `False`.
- No-expansion triage geometry is not the P013 winner and is not a method
  registry candidate.

Boundaries:

- Candidate-only P013 diagnostic OCR evidence.
- No reference-guided token insertion, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, PDF parsing/text-layer
  extraction, render execution, runtime implementation/start/execution,
  production assembly, method-registry winner, selector rule, page `021+`,
  translation/proofreading, push, or downstream execution is created.

## Documentation Checkpoint: doc-checkpoint-20260802T135500Z

Timestamp: 2026-08-02T13:55:00Z

Context:

- P013 no-expansion geometry underperformed, so the failed-page loop moved to
  assembly over the cached expanded PSM4 TSV output.
- Sol proposed lane-aware line ordering; Terra required exact page-space
  coordinate mapping and deterministic parameters before execution.

Result:

- Generated `C01TEP013ELO-G1-VIRAL-001`.
- No OCR was executed.
- Cached expanded PSM4 TSV line records were mapped from prepared-crop
  coordinates into page space using the pinned `24` px border and sealed
  `region_results[].page_space_box`.
- Best variant `p013_expanded_lane_order_lane_then_y_exact_collapse` scored
  similarity `0.433325`, token recall `0.993939`, diagnostic threshold met
  `False`.
- The result shows layout ordering is a real factor, but no P013 winner exists
  yet.

Boundaries:

- Candidate-only P013 diagnostic assembly evidence.
- No OCR execution, reference-guided token insertion, accepted text mutation,
  semantic/page-status mutation, source/raw mutation, PDF parsing/text-layer
  extraction, render execution, runtime implementation/start/execution,
  production assembly, method-registry winner, selector rule, page `021+`,
  translation/proofreading, push, or downstream execution is created.
