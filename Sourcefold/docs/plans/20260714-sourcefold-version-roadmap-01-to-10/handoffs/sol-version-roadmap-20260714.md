# Sol V2 Immutable Handoff Receipt: Sourcefold 0.1 to 1.0

- Goal id: `20260714-sourcefold-version-roadmap-01-to-10`
- Step id: `V2`
- Role / model / effort: Sol analyst-architect / `gpt-5.6-sol` / high
- Result: constructive product-level roadmap proposed from Sourcefold Core 0.1 RC through Sourcefold 1.0 production.
- Timestamp: `2026-07-14T20:38:39Z` (`2026-07-14T23:38:39+03:00`, Europe/Moscow)
- Elapsed time: approximately 2 minutes of goal-active analysis before immutable receipt creation; tool waits and approval latency excluded.
- Token use: unavailable as a final exact total at immutable receipt creation. Pre-write goal telemetry snapshot: 15,019 tokens.

## Scope

This handoff dry-runs the product maturity path from the first contract-valid,
fixture-backed Core release candidate to a supportable 1.0 production release.
It defines version purpose, capability claims, exclusions, entry dependencies,
release gates, required evidence, and likely bounded implementation goals.

This is not a module implementation design, delivery estimate, commitment to a
UI or hosted service, or final release review. It does not approve any
candidate. Canonical plan, context, project status, architecture, contracts,
quality criteria, and release artifacts remain unchanged.

## Files Checked

Only the assigned files were inspected:

- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/plans/20260714-sourcefold-release-roadmap/roadmap.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`

No CoC, Dune, Git, FoundryVTT, `.tools`, `.agents`, temporary, or Translator
files were inspected.

## Architectural Trace

### Mandatory dependency spine

```text
Release charter and acceptance vocabulary
  -> identity, lineage, trace, finding, waiver, and evidence contracts
  -> executable graph/evidence validation
  -> reconstruct -> Accepted Source Text
  -> translate   -> Faithful RU Draft
  -> proofread   -> Proofread RU Master
  -> candidate freeze and candidate-bound release evidence
  -> independent Terra release review
  -> promotion
```

The core artifact contract is cumulative. Each downstream stage consumes an
accepted immutable upstream artifact, never an ad hoc work file. Every accepted
artifact must expose identity, hashes, producing module, source/predecessor,
tool or model versions, trace anchors, findings, waivers, QA state, acceptance
state, and applicable terminology evidence. QA may route work back to the
current or an earlier stage, so the operational shape is a governed DAG rather
than a one-way wizard.

### Optional branches

```text
Proofread RU Master
  +-> press  -> declared rendered projection
  +-> bridge -> declared destination export
```

`press` and `bridge` are sibling optional branches. Neither is an upstream
dependency of core acceptance, neither may alter the accepted master in place,
and neither may repair, mask, or substitute for unresolved core findings. Their
failures block only their own release claims unless a later candidate explicitly
declares that branch part of its supported capability set.

### Promotion rule

Each release train ends in a frozen candidate with a capability manifest,
evidence package, known limitations, and independent Terra release review.
Promotion applies to the exact reviewed bits or manifest. Any mutation after
freeze requires a new candidate and review. Passing automated checks is not the
same as artifact acceptance; artifact acceptance is not the same as candidate
conformance; candidate conformance is not the same as release approval.

## Proposed Version Ladder

### 0.1 — Core vertical-slice release candidate

Recommended milestone: `Sourcefold Core 0.1.0-rc.1`. If the frozen candidate
passes independent release review unchanged, it may be tagged `0.1.0` as a
qualified preview release, not advertised as production-ready.

**Purpose**

Prove that Sourcefold's product promise is real for one declared source profile,
one language pair (source to Russian), one supported structure subset, and one
representative pilot: source truth can move through reconstruct, translate, and
proofread with inspectable acceptance and lineage.

**Expected capabilities**

- Ingest immutable source evidence under a written input profile.
- Produce Accepted Source Text, Faithful RU Draft, and Proofread RU Master.
- Enforce valid stage, artifact-type, predecessor, finding, waiver, and
  acceptance states.
- Preserve in-scope meaning, reading order, structure, mechanics, numbers,
  names, definitions, modality, conditions, negations, and traceability.
- Detect source mutation or hash mismatch and create new lineage when inputs
  change.
- Run and revalidate retained positive and negative fixtures without hidden
  state.
- Freeze a candidate and evidence package that a qualified operator and an
  independent reviewer can inspect.

**Non-goals**

- Universal PDF or OCR support, multiple source profiles, or broad format
  compatibility.
- `press` or `bridge` as release blockers.
- Knowledge-base generation, cross-book rule systems, Translator compatibility,
  full UI, multi-user service, or destination catalogue.
- Automated acceptance authority unless Phase 0 explicitly grants it.

**Entry dependencies**

- Accepted first-release charter and named acceptance authority.
- Distinct definitions for `accepted`, `passed`, `waived`, `conformant`, and
  `released`.
- Decisions for artifact identity, lineage, trace anchors, legal DAG edges,
  waiver completeness, evidence vocabulary, schema evolution, canonical text
  and evidence formats.
- Representative pilot plus focused positive and negative contract fixtures.
- Acceptance matrix mapping every claim to automated checks, operator checks,
  or human decisions.

**Exit / release gate**

- All existing roadmap Phase 0 through Phase 5 gates pass for the declared
  profile and candidate.
- The pilot has a valid evidence DAG and no unresolved core finding.
- Every downstream artifact references accepted upstream evidence.
- Injected reconstruction, translation, proofreading, lineage, and waiver
  defects are rejected or routed correctly.
- A clean qualified operator run needs no undocumented state.
- Candidate-bound Terra high-effort release review recommends promotion.

**Evidence**

- Release charter, contract decision log, capability/exclusion manifest, and
  release acceptance matrix.
- Versioned schemas and validator results for positive and negative fixtures.
- Accepted pilot chain, trace map, finding/waiver ledger, acceptance ledger,
  rerun/revalidation report, and clean-environment operator record.
- Frozen revision or SHA-256 manifest, test report, known limitations, and
  independent Terra release receipt.

**Likely implementation goals**

- `sourcefold-phase-0-release-charter`
- `sourcefold-01-contract-evidence-spine`
- `sourcefold-01-thin-core-lane`
- `sourcefold-01-quality-completion`
- `sourcefold-01-operator-hardening`
- `sourcefold-01-candidate-freeze-release-review`

### 0.2 — Repeatable profile-driven Core beta

Recommended train: `0.2.0-beta.1` -> `0.2.0-rc.1` -> `0.2.0`.

**Purpose**

Turn the one-profile proof into a repeatable bounded product by separating
declared source-profile support from hidden pilot assumptions.

**Expected capabilities**

- Explicit capability negotiation: supported input profile, structure subset,
  language pair, schema version, and exclusions are machine-inspectable.
- At least one additional deliberately different fixture or profile proves
  that the product is not hard-coded to the 0.1 pilot.
- Profile-specific configuration changes behavior without changing core
  acceptance meanings.
- Cross-profile regression, supersession, partial rerun, and revalidation retain
  valid lineage and do not reuse stale acceptance.
- Unsupported profiles fail early with actionable diagnostics.

**Non-goals**

- Open-ended plugin architecture, universal documents, arbitrary languages, or
  production scale.
- Optional lane delivery.
- Compatibility promises for every pre-1.0 schema revision.

**Entry dependencies**

- Promoted 0.1 candidate and preserved 0.1 evidence corpus.
- A profile declaration contract and a policy for schema/profile versioning.
- A second fixture selected for meaningful structural variance, not superficial
  duplication.

**Exit / release gate**

- No pilot-specific path, state, or manual repair is required.
- Both declared profiles satisfy their acceptance matrices in clean runs.
- Unsupported or contradictory profile declarations fail before artifact
  acceptance.
- Regression proves that new profile support does not weaken 0.1 semantics.
- Frozen candidate has independent release review.

**Evidence**

- Versioned profile manifests, support matrix, two accepted artifact chains,
  differential regression report, unsupported-profile negative fixtures, and
  candidate-bound review receipt.

**Likely implementation goals**

- `sourcefold-02-profile-contract`
- `sourcefold-02-second-profile-pilot`
- `sourcefold-02-cross-profile-regression`
- `sourcefold-02-release-candidate`

### 0.3 — Core quality-depth beta

Recommended train: `0.3.0-beta.1` -> `0.3.0-rc.1` -> `0.3.0`.

**Purpose**

Demonstrate that supported output is semantically and structurally trustworthy
across the declared quality surface, not merely contract-shaped.

**Expected capabilities**

- Acceptance coverage for all declared structure classes: headings, emphasis,
  quotes, lists, tables, cards/stat blocks, page markers, uncertain readings,
  and reading order where applicable.
- Acceptance coverage for numbers, dates, dice, mechanics, names, definitions,
  terminology provenance, modality, conditions, negations, actors, and Russian
  language quality.
- Adversarial defects test semantic drift separately from language defects.
- Findings route backward across stages without losing provenance.
- Quality exclusions are explicit at profile and release level.

**Non-goals**

- Claiming perfect translation, replacing accountable human acceptance, or
  declaring quality for unlisted structures.
- Layout rendering quality or destination-export fidelity.
- Knowledge-base semantics.

**Entry dependencies**

- Stable 0.2 profile and evidence contracts.
- Approved classification of finding types and severity/release-blocking rules.
- Representative adversarial corpus and terminology decision policy.

**Exit / release gate**

- Every in-scope acceptance criterion has positive, negative, and regression
  evidence or an explicit exclusion.
- No unresolved release-blocking finding exists in any accepted chain.
- Waivers are complete, authorized, bounded, and visible in release evidence.
- Independent reviewers can trace sampled claims from RU master to source.

**Evidence**

- Criterion-to-test coverage map, adversarial fixture results, terminology
  provenance records, cross-stage routing records, waiver audit, sampled manual
  trace audit, and frozen-candidate review.

**Likely implementation goals**

- `sourcefold-03-quality-taxonomy`
- `sourcefold-03-adversarial-fixtures`
- `sourcefold-03-cross-stage-finding-routing`
- `sourcefold-03-quality-release-candidate`

### 0.4 — Long-form and recovery beta

Recommended train: `0.4.0-beta.1` -> `0.4.0-rc.1` -> `0.4.0`.

**Purpose**

Prove that Core remains auditable and recoverable over realistic long-form work,
interruption, correction, and selective rerun.

**Expected capabilities**

- Process a representative full-length source within declared resource limits.
- Resume controlled interruptions without ambiguous duplicate or partial
  acceptance.
- Rerun a bounded segment and supersede only affected descendants while
  preserving historical evidence.
- Explain which artifacts are current, stale, superseded, blocked, or require
  revalidation.
- Keep evidence navigation practical at long-form scale.

**Non-goals**

- Distributed execution, unlimited scale, hosted orchestration, or throughput
  guarantees outside measured envelopes.
- Multi-user conflict resolution.
- Optional-lane completion.

**Entry dependencies**

- 0.3 quality semantics and fixtures.
- Defined run, checkpoint, supersession, stale-state, and revalidation contracts.
- Declared resource envelope and representative long-form corpus.

**Exit / release gate**

- Full-length clean run and controlled interruption/resume pass.
- Injected late-stage and early-stage corrections invalidate exactly the
  required descendants and never silently retain stale acceptance.
- Resource limits and failure modes are documented and actionable.
- Historical and current accepted states remain distinguishable and auditable.

**Evidence**

- Full-length run manifest, resource measurements, interruption matrix,
  supersession/revalidation graph snapshots, stale-state negative tests,
  operator recovery record, and candidate review.

**Likely implementation goals**

- `sourcefold-04-long-form-pilot`
- `sourcefold-04-checkpoint-resume`
- `sourcefold-04-supersession-revalidation`
- `sourcefold-04-scale-release-candidate`

### 0.5 — Supportable Core public beta

Recommended train: `0.5.0-beta.1` -> `0.5.0-rc.1` -> `0.5.0`.

**Purpose**

Turn the validated Core into a package that a qualified non-implementer can
install, operate, diagnose, upgrade, and support under explicit policies.

**Expected capabilities**

- Documented installation, invocation, configuration, workspace layout,
  review/acceptance flow, recovery, backup, upgrade, and uninstall boundaries.
- Stable operator-facing commands and actionable contract, lineage, QA, and
  provider/tool failure diagnostics.
- Clean credential handling and no secret material in artifacts or evidence.
- Versioned schemas with a tested migration or explicit revalidation path.
- A support matrix for environment, profile, schema, provider/tool versions,
  and known limitations.

**Non-goals**

- Production SLA, zero-downtime upgrades, GUI, hosted service, or broad public
  compatibility guarantee.
- Making `press` or `bridge` part of Core.
- Freezing the entire API forever before 1.0.

**Entry dependencies**

- 0.4 long-form reliability and recovery evidence.
- Distribution format decision, supported environment matrix, schema lifecycle
  policy, credential boundary, and support/diagnostic vocabulary.

**Exit / release gate**

- A qualified operator completes install-to-accepted-master and recovery using
  only published documentation.
- Upgrade/revalidation from at least the immediately prior supported release
  passes without lineage ambiguity.
- Secret scanning and clean-environment smoke/integration/regression checks pass.
- Support matrix matches measured evidence, not aspiration.

**Evidence**

- Reproducible package/build manifest, clean-install record, operator usability
  record, upgrade/revalidation fixtures, diagnostic catalogue validation,
  credential/secret scan, support matrix, and candidate review.

**Likely implementation goals**

- `sourcefold-05-distribution-contract`
- `sourcefold-05-operator-workflow`
- `sourcefold-05-schema-upgrade-revalidation`
- `sourcefold-05-public-beta-candidate`

### 0.6 — Press optional-lane beta

Recommended train: `0.6.0-beta.1` -> `0.6.0-rc.1` -> `0.6.0`.

**Purpose**

Add a bounded rendering branch while proving that presentation work cannot
change or conceal the accepted RU master.

**Expected capabilities**

- Render at least one declared projection, preferably readable Markdown first;
  HTML or PDF are additional explicit profiles, not implied capabilities.
- Record the accepted RU master identity, press profile, renderer/tool versions,
  transformations, and output hashes.
- Separate layout/rendering findings from core semantic and language findings.
- Rebuild reproducibly or explain declared nondeterminism.
- Reject unaccepted or stale masters as release inputs.

**Non-goals**

- Desktop-publishing completeness, universal templates, semantic repair during
  layout, or making press acceptance satisfy Core acceptance.
- Bridge destinations or knowledge-base generation.

**Entry dependencies**

- Supportable 0.5 Core and immutable Proofread RU Master contract.
- Press profile, transform policy, losslessness rules, and distinct layout
  finding/acceptance vocabulary.

**Exit / release gate**

- Rendered outputs trace to an accepted current master.
- Text-diff/semantic checks prove the renderer did not alter protected content.
- Layout defects remain branch-local and cannot mutate core state.
- Clean rebuild and candidate-bound visual/operator review pass for each claimed
  output profile.

**Evidence**

- Press contract/profile, input/output manifest, transform log, protected-text
  comparison, layout finding ledger, clean rebuild evidence, visual QA, and
  candidate review.

**Likely implementation goals**

- `sourcefold-06-press-contract`
- `sourcefold-06-markdown-projection`
- `sourcefold-06-render-integrity-qa`
- `sourcefold-06-press-beta-candidate`

### 0.7 — Bridge optional-lane beta

Recommended train: `0.7.0-beta.1` -> `0.7.0-rc.1` -> `0.7.0`.

**Purpose**

Prove one bounded export integration without turning Sourcefold into a catalogue
of destinations or allowing lossy mappings to hide core truth.

**Expected capabilities**

- Export an accepted artifact to one declared destination contract.
- Record source identity/hash, bridge version, destination assumptions,
  transformation map, loss classification, and output receipt.
- Validate destination-required fields and reject unsupported mappings before
  claiming success.
- Re-export idempotently where the destination permits it, or record explicit
  non-idempotent behavior.
- Keep destination state and credentials outside canonical core evidence except
  for sanitized receipts.

**Non-goals**

- Destination catalogue, bidirectional synchronization, remote system of record,
  arbitrary plugins, or bridge output as acceptance evidence for Core.
- Cross-book rule integration or knowledge-base generation.

**Entry dependencies**

- Supportable 0.5 Core; 0.6 is not a mandatory predecessor unless the selected
  bridge explicitly consumes a press projection.
- One destination owner, explicit export schema, loss policy, credential model,
  idempotency semantics, and rollback/retry boundary.

**Exit / release gate**

- Positive, negative, loss, retry, stale-input, and credential-isolation cases
  pass against the declared destination contract.
- Every exported claim traces to the exact accepted source artifact.
- Lossy mappings are visible and accepted by the authorized role.
- Bridge failure leaves Core evidence and accepted artifacts unchanged.

**Evidence**

- Destination contract, mapping/loss matrix, sanitized export receipts,
  idempotency/retry results, stale-input rejection, credential boundary check,
  destination-owner acceptance, and candidate review.

**Likely implementation goals**

- `sourcefold-07-bridge-destination-charter`
- `sourcefold-07-export-contract`
- `sourcefold-07-loss-retry-qa`
- `sourcefold-07-bridge-beta-candidate`

### 0.8 — Production-readiness beta

Recommended train: `0.8.0-beta.1` -> `0.8.0-rc.1` -> `0.8.0`.

**Purpose**

Converge Core and whichever optional lanes are intended for the 1.0 support
statement into one operable, secure, upgradeable product candidate family.

**Expected capabilities**

- Declared 1.0 capability and support matrix with Core mandatory and optional
  lanes independently claimable.
- Reproducible distribution, dependency inventory, version reporting, backup,
  restore, upgrade, rollback or revalidation, and evidence retention policy.
- Measured reliability and resource envelopes for representative supported work.
- Safe failure behavior, sanitized diagnostics, and operator-visible state
  transitions.
- Compatibility policy for 1.x schemas, commands, profiles, and accepted
  artifacts proposed and tested before freeze.

**Non-goals**

- New major feature lanes, unbounded scalability, hosted-service operations, or
  claims for optional branches that have not passed their own gates.
- Last-minute broadening to UI, multi-user workflow, KB generation, or arbitrary
  destination support.

**Entry dependencies**

- 0.5 Core supportability.
- Accepted decision on whether 0.6 press and/or 0.7 bridge are in the 1.0
  supported capability set; unselected branches remain optional previews.
- Production threat/credential boundary, dependency policy, retention policy,
  compatibility policy, and representative workload envelope.

**Exit / release gate**

- 1.0 acceptance matrix has an owner and evidence route for every claimed
  capability and non-goal.
- Clean install, representative end-to-end run, interruption/recovery,
  upgrade/revalidation, backup/restore, and dependency/secret checks pass.
- Optional-lane failures cannot corrupt Core and are reported independently.
- No unresolved architecture or policy decision is deferred into 0.9 freeze.

**Evidence**

- 1.0 capability/support matrix, compatibility proposal and fixtures,
  reproducible build manifest, dependency inventory, security/credential checks,
  reliability envelope, backup/restore and upgrade evidence, failure-isolation
  report, and 0.8 candidate review.

**Likely implementation goals**

- `sourcefold-08-production-charter`
- `sourcefold-08-distribution-security`
- `sourcefold-08-upgrade-backup-recovery`
- `sourcefold-08-production-readiness-candidate`

### 0.9 — 1.0 production release candidate

Recommended milestone: `Sourcefold 1.0.0-rc.1`; use `rc.N` for every candidate
mutation. The repository/product version may remain on the 0.9 release train
during stabilization, but the externally reviewed artifact should carry the
actual target tag `1.0.0-rc.N` to avoid ambiguity about what can be promoted.

**Purpose**

Freeze the 1.0 capability set and prove the exact production candidate. This is
a stabilization and evidence-completion train, not a feature train.

**Expected capabilities**

- Feature-complete Core with the exact supported profiles and environment matrix
  intended for 1.0.
- Only those optional press/bridge profiles that passed independent branch gates
  are included in the supported 1.0 claim.
- Final 1.x compatibility, migration/revalidation, support, limitation,
  credential, and evidence-retention policies are publishable.
- Candidate artifacts, tests, documentation, schemas, fixtures, and evidence
  resolve to one frozen manifest.

**Non-goals**

- New capabilities, schema redesign, new profiles/destinations, opportunistic
  refactors, or changing acceptance authority during RC.
- Treating unresolved release blockers as documentation-only known issues.

**Entry dependencies**

- Accepted 0.8 production-readiness evidence.
- Closed 1.0 scope and acceptance matrix.
- Release owner, support owner, waiver authority, candidate-freeze procedure,
  and rollback/reissue procedure.

**Exit / release gate**

- All 1.0 acceptance rows pass against the exact candidate or are explicitly
  excluded from the claim; release-blocking criteria cannot be waived merely to
  meet the version date.
- No unresolved release-blocking finding, undocumented state, secret, or
  unsupported dependency exists.
- Full clean-room rehearsal and upgrade/revalidation rehearsal pass.
- Independent Terra high-effort release review recommends production release
  for the exact frozen candidate.
- Any change after review creates `rc.N+1` and invalidates prior promotion.

**Evidence**

- Final release acceptance matrix, frozen SHA-256 manifest/revision, reproducible
  build provenance, full test and rehearsal reports, accepted representative
  chains, optional-lane receipts where claimed, limitations/support documents,
  participation declaration, and independent Terra release receipt.

**Likely implementation goals**

- `sourcefold-09-feature-freeze`
- `sourcefold-09-release-evidence-completion`
- `sourcefold-09-clean-room-rehearsal`
- `sourcefold-10-rc-independent-release-review`

### 1.0 — Production stable

Recommended milestone: `Sourcefold 1.0.0`. Promotion must point to the unchanged
`1.0.0-rc.N` candidate approved by independent Terra release review.

**Purpose**

Publish a production-supportable Sourcefold whose claims, constraints,
operational behavior, evidence, and compatibility commitments are explicit.

**Expected capabilities**

- Supported headless operator workflow from declared source evidence through
  accepted Proofread RU Master for every profile listed in the 1.0 matrix.
- Auditable identity, lineage, trace, finding, waiver, QA, acceptance,
  supersession, revalidation, and release evidence throughout Core.
- Reproducible install/run/upgrade/recovery inside the declared support envelope.
- Stable 1.x compatibility and deprecation policy for public contracts.
- Optional `press` and `bridge` support only for profiles explicitly named in
  the capability matrix; all others remain experimental or excluded.

**Non-goals**

- Universal OCR/PDF or language support, UI or hosted service, multi-user
  collaboration, destination catalogue, knowledge-base generation, cross-book
  systems, Translator compatibility, or any undeclared profile.
- Guaranteeing identical model/provider prose output; the guarantee is governed
  evidence, acceptance, and declared reproducibility semantics.

**Entry dependencies**

- Unchanged independently approved `1.0.0-rc.N` candidate.
- Final release notes, support/capability matrix, known limitations, upgrade and
  recovery guidance, artifact retention policy, and release/rollback procedure.

**Exit / release gate**

- Promotion is a metadata/distribution action only; no code, contract, fixture,
  evidence, or documentation content differs from the approved RC except
  authorized release metadata already covered by the manifest procedure.
- Published artifacts verify against the approved manifest and can be installed
  in a clean supported environment.
- Release evidence and support ownership are durably discoverable.
- Independent Terra approval is attached to the exact production artifact. If
  Terra is unavailable, final acceptance remains pending.

**Evidence**

- Signed or otherwise integrity-verifiable production manifest, distribution
  verification, clean-install smoke result, final release notes and capability
  matrix, linked RC evidence package, independent Terra release receipt, and
  rollback/reissue readiness record.

**Likely implementation goals**

- `sourcefold-10-production-promotion`
- `sourcefold-10-distribution-verification`
- `sourcefold-10-release-handoff`

## Recommended Naming And Channel Policy

- Use semantic versions: `MAJOR.MINOR.PATCH[-prerelease.N]`.
- Use `beta.N` when a train's declared capabilities are available for bounded
  operator evaluation but contracts or behavior may still change.
- Use `rc.N` only after feature and claim freeze; every material candidate change
  increments `N` and requires regenerated candidate-bound evidence.
- Use the bare version (`0.x.0`, `1.0.0`) only for an unchanged candidate that
  passed its release gate and independent Terra release review.
- Reserve `stable` as a distribution channel label, not part of the SemVer tag.
  Before 1.0 it means stable within the explicitly narrow preview support matrix,
  not production maturity.
- Use product labels to prevent overclaiming: `Sourcefold Core 0.1 RC`,
  `Sourcefold 0.x Beta`, `Sourcefold 1.0 RC`, and `Sourcefold 1.0 Production`.
- Do not call ordinary development snapshots RCs. If snapshots need identity,
  bind them to revision/hash manifests rather than inventing release status.

## Risks And Controls

| Risk | Consequence | Roadmap control |
|---|---|---|
| Acceptance vocabulary remains ambiguous | Plausible output is mistaken for accepted or released output | Block 0.1 implementation on Phase 0 definitions and authority |
| Fixture success is generalized into universal support | Unsupported documents receive false quality claims | Profile/capability manifests, negative fixtures, explicit exclusions from 0.1 onward |
| Human acceptance becomes ceremonial | Automation silently becomes release authority | Acceptance ledger, named authority, distinct pass/accept/conform/release states |
| Evidence becomes too heavy to operate | Operators bypass governance or create hidden work files | 0.4 evidence navigation and 0.5 non-implementer operator trials |
| Profile expansion weakens earlier semantics | New formats regress accepted 0.1 behavior | Cumulative cross-profile regression and frozen prior evidence corpus |
| Nondeterministic tools/providers obscure provenance | Results cannot be explained or revalidated | Record tool/model versions, inputs, configuration, hashes, and declared nondeterminism |
| Long-form correction leaves stale descendants | Released RU master no longer matches source truth | Explicit supersession/revalidation DAG and injected early-stage corrections |
| Press or bridge contaminates Core | Rendering/export defects mask or rewrite accepted content | One-way optional branches, separate findings, immutable accepted master |
| Schema evolution invalidates accepted history | Old evidence becomes unreadable or falsely current | Versioned schemas and tested migration or explicit revalidation path |
| 0.x labels are mistaken for production | Users depend on unstable contracts | Narrow support matrices, preview labels, no production claim before 1.0 |
| 0.9 becomes a feature train | Candidate never stabilizes and evidence constantly expires | Closed 1.0 matrix; RC changes limited to blockers and force `rc.N+1` |
| Candidate mutates after independent review | Approval no longer applies to shipped bits | Exact manifest binding and metadata-only promotion |
| Optional branches delay Core indefinitely | Product boundary expands faster than core maturity | Core gates remain independent; unready optional lanes are excluded from 1.0 claims |

## Assumptions

- The conservative default is explicit human acceptance at every Core stage until
  Phase 0 decides otherwise; automation constrains or recommends but does not
  silently grant acceptance.
- The first language pair remains source-to-Russian and the first product remains
  headless and operator-run through 1.0 unless a later accepted charter changes
  the product boundary.
- Canonical text/evidence formats are intentionally not selected here. The
  existing roadmap's Markdown/JSON question remains a Phase 0 decision.
- Version numbers express product maturity and supported claims, not a calendar.
  No train advances merely because implementation work occurred.
- 0.1 evidence remains a permanent regression anchor for later trains.
- Pre-1.0 compatibility may evolve only through an explicit migration or
  revalidation policy; 1.0 publishes the supported 1.x contract.
- `press` and `bridge` may be omitted from the 1.0 supported matrix without
  invalidating Sourcefold Core 1.0, because the accepted product boundary marks
  them optional.
- The active-goal task packet supplied to Sol is authoritative for V2. No
  unlisted canonical plan/context file was inspected because the assignment
  explicitly constrained inspection to the five named sources.

## Verification / Evidence For This Handoff

- Every 0.1 capability and exclusion traces to the assigned release roadmap.
- The dependency spine and optional-branch rules trace to the assigned product
  boundary and module contracts.
- Quality gates retain the assigned reconstruct, translate, proofread, press,
  and bridge acceptance semantics.
- Every release train names its purpose, capabilities, non-goals, entry
  dependencies, exit/release gate, evidence, and likely implementation goals.
- This architecture handoff recommends gates and sequencing only; it does not
  act as independent release approval.

## Changed Files

- Created only:
  `Sourcefold/docs/plans/20260714-sourcefold-version-roadmap-01-to-10/handoffs/sol-version-roadmap-20260714.md`

No canonical plan, context, status, architecture, contract, quality, code, or
release file was changed.

## Blockers

- No blocker to adopting this as a planning proposal.
- 0.1 implementation remains blocked by the unresolved Phase 0 decisions already
  identified in the assigned release roadmap: supported source profile,
  canonical text/evidence formats, acceptance authority, artifact identity and
  lineage, trace anchors, valid DAG edges, waiver authority/completeness,
  evidence vocabulary, and schema evolution.
- Final acceptance of any release remains pending until an independent Terra
  high-effort release review approves the exact frozen candidate.

## Next Action

The orchestrator should compare this V2 ladder with the canonical version
roadmap draft, resolve any scope conflicts, and present the user with the small
set of product decisions that determine 0.1. If the boundary is accepted, open
`sourcefold-phase-0-release-charter` as the next bundled goal. Do not start
module implementation until Phase 0 contracts, acceptance semantics, fixture
strategy, and release acceptance matrix are accepted.
