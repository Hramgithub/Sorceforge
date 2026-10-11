# Sourcefold Version Roadmap: 0.1 To 1.0

Goal id: `20260714-sourcefold-version-roadmap-01-to-10`

Status: draft for user review

Date: 2026-07-14

## Reading This Roadmap

This is a dry run from the first Sourcefold release candidate to a bounded
production release.

The version ladder is not a calendar. A version advances only when its release
claim has evidence. The main line is **Sourcefold Core**:

```text
immutable source evidence
  -> reconstruct
  -> Accepted Source Text
  -> translate
  -> Faithful RU Draft
  -> proofread
  -> Proofread RU Master
```

`press` and `bridge` are optional branches from an accepted RU master. They may
have preview releases, but they are not required for Sourcefold Core 1.0.
Knowledge base work and Translator migration are outside this 1.0 roadmap.

## Version Summary

| Version | Product Meaning | Production Claim |
|---|---|---|
| `0.1` | Core invariant proven on one declared source profile. | Preview RC, not production. |
| `0.2` | Profile declarations and repeatability beyond one pilot. | Bounded Core beta. |
| `0.3` | Quality-depth coverage and adversarial regression. | Quality beta. |
| `0.4` | Long-form recovery, rerun, supersession, and revalidation. | Reliability beta. |
| `0.5` | Supportable operator workflow and packaging. | Public Core beta. |
| `0.6-preview` | Optional `press` branch preview, if wanted. | Not required for Core 1.0. |
| `0.7-preview` | Optional `bridge` branch preview, if wanted. | Not required for Core 1.0. |
| `0.8` | Production-readiness beta for Core. | Candidate-family readiness. |
| `0.9` | `1.0.0-rc.N` freeze and evidence completion. | Release candidate only. |
| `1.0` | Bounded production-stable Sourcefold Core. | Production Core. |

## 0.1: Sourcefold Core 0.1 RC

Purpose: prove that Sourcefold's central product promise works once, under a
declared boundary.

Expected capabilities:

- formal release scope and supported input profile;
- one language pair: source to Russian;
- one supported structure subset;
- full `reconstruct -> translate -> proofread` flow;
- Accepted Source Text, Faithful RU Draft, and Proofread RU Master;
- artifact identity, hashes, lineage, trace anchors, findings, waivers, QA
  state, and acceptance evidence;
- invalid acceptance, open findings, malformed waivers, wrong predecessors, and
  changed hashes rejected by validation;
- clean operator rerun or revalidation for retained fixtures;
- candidate freeze and independent Terra release review.

Non-goals:

- broad PDF/OCR support;
- multiple source profiles;
- `press`, `bridge`, KB, UI, Translator migration;
- automated semantic acceptance unless explicitly allowed by the release
  charter.

Entry dependencies:

- Phase 0 release charter;
- acceptance vocabulary: `accepted`, `passed`, `waived`, `conformant`,
  `released`;
- identity, lineage, anchors, DAG edges, waiver policy, evidence vocabulary,
  schema evolution;
- representative pilot plus positive/negative fixtures;
- release acceptance matrix.

Exit gate:

- pilot has a valid evidence DAG and no unresolved core finding;
- downstream artifacts consume accepted upstream artifacts only;
- injected source, translation, proofreading, lineage, and waiver defects are
  caught or routed correctly;
- clean operator run needs no hidden state;
- frozen candidate passes independent Terra release review.

Evidence:

- release charter;
- contract decision log;
- schema and validator reports;
- accepted pilot chain;
- trace map;
- finding/waiver/acceptance ledgers;
- rerun/revalidation report;
- frozen candidate manifest;
- release receipt.

Likely goals:

- `sourcefold-phase-0-release-charter`;
- `sourcefold-01-contract-evidence-spine`;
- `sourcefold-01-thin-core-lane`;
- `sourcefold-01-quality-completion`;
- `sourcefold-01-operator-hardening`;
- `sourcefold-01-candidate-freeze-review`.

## 0.2: Repeatable Profile-Driven Core Beta

Purpose: prove 0.1 was not hard-coded to one pilot.

Expected capabilities:

- machine-inspectable source-profile declaration;
- explicit support matrix for profile, structure subset, language pair, schema
  version, and exclusions;
- at least one additional deliberately different fixture or profile;
- unsupported profile rejection with actionable diagnostics;
- cross-profile regression without weakening 0.1 semantics;
- partial rerun and revalidation without stale acceptance reuse.

Non-goals:

- universal document support;
- arbitrary languages;
- plugin architecture;
- optional lanes.

Entry dependencies:

- promoted 0.1 evidence corpus;
- profile declaration contract;
- schema/profile versioning policy;
- second fixture selected for meaningful structural variance.

Exit gate:

- both declared profiles satisfy their acceptance matrices;
- unsupported or contradictory profiles fail before artifact acceptance;
- regression proves no 0.1 semantics were weakened;
- frozen candidate receives release review.

Evidence:

- profile manifests;
- support matrix;
- two accepted artifact chains;
- unsupported-profile negative fixtures;
- cross-profile regression report.

## 0.3: Core Quality-Depth Beta

Purpose: make Core quality trustworthy, not merely contract-shaped.

Expected capabilities:

- coverage for in-scope headings, emphasis, quotes, lists, tables, cards/stat
  blocks, page markers, uncertain readings, and reading order;
- coverage for numbers, dates, dice, mechanics, names, definitions, modality,
  conditions, negations, actors, terminology, and Russian language quality;
- adversarial fixtures for semantic drift and language polish drift;
- findings route backward across stages without losing provenance;
- explicit quality exclusions at profile and release level.

Non-goals:

- perfect translation claims;
- replacing human acceptance;
- layout rendering quality;
- destination export fidelity;
- knowledge-base semantics.

Entry dependencies:

- stable 0.2 profile/evidence contracts;
- finding taxonomy and severity policy;
- terminology decision policy;
- adversarial corpus.

Exit gate:

- every in-scope criterion has positive, negative, and regression evidence or
  an explicit exclusion;
- no unresolved release-blocking finding remains;
- waivers are authorized, bounded, evidenced, and visible;
- sampled RU claims trace back to source evidence.

Evidence:

- criterion-to-test coverage map;
- adversarial fixture results;
- terminology provenance;
- cross-stage routing records;
- waiver audit;
- sampled manual trace audit.

## 0.4: Long-Form Recovery Beta

Purpose: prove Sourcefold remains auditable on realistic long-form work.

Expected capabilities:

- representative full-length source within declared resource limits;
- controlled interruption and resume;
- segment rerun and descendant supersession;
- stale/current/superseded/blocked state explanation;
- practical evidence navigation at long-form scale.

Non-goals:

- distributed execution;
- unlimited throughput;
- hosted orchestration;
- multi-user conflict resolution;
- optional-lane completion.

Entry dependencies:

- 0.3 quality semantics;
- run/checkpoint/supersession/revalidation contracts;
- declared resource envelope;
- long-form corpus.

Exit gate:

- full-length run passes;
- controlled interruption/resume passes;
- early and late corrections invalidate exactly the required descendants;
- historical and current accepted states remain distinguishable.

Evidence:

- long-form run manifest;
- resource measurements;
- interruption matrix;
- supersession/revalidation graph snapshots;
- stale-state negative tests;
- operator recovery record.

## 0.5: Supportable Core Public Beta

Purpose: turn validated Core into a package a qualified non-implementer can
operate and diagnose.

Expected capabilities:

- documented install, invocation, configuration, workspace layout, review flow,
  recovery, upgrade, backup, and support boundaries;
- stable operator-facing commands;
- actionable errors for contract, lineage, QA, provider/tool failures;
- clean credential handling;
- schema migration or explicit revalidation path;
- environment/profile/schema/provider support matrix.

Non-goals:

- production SLA;
- GUI or hosted service;
- broad public compatibility guarantees;
- press/bridge as Core requirements.

Entry dependencies:

- 0.4 reliability evidence;
- distribution format decision;
- supported environment matrix;
- schema lifecycle policy;
- credential boundary.

Exit gate:

- non-implementer operator completes install-to-accepted-master from docs;
- upgrade/revalidation from prior release passes;
- secret scan and clean-environment checks pass;
- support matrix matches measured evidence.

Evidence:

- build/package manifest;
- clean-install record;
- operator usability record;
- upgrade/revalidation fixtures;
- diagnostic catalogue validation;
- credential/secret scan.

## 0.6-preview: Optional Press Branch

Purpose: preview rendering from an accepted RU master without making rendering a
Core release dependency.

Expected capabilities:

- one declared projection, preferably readable Markdown first;
- accepted RU master identity recorded as input;
- renderer/profile/tool versions and output hashes;
- protected-text comparison proving rendering did not alter accepted content;
- layout findings separated from core findings.

Non-goals:

- production publishing claim;
- PDF/layout completeness;
- semantic repair during layout;
- bridge or KB work.

Entry dependencies:

- supportable 0.5 Core;
- press profile and transform policy;
- distinct layout finding vocabulary.

Exit gate:

- projection traces to current accepted master;
- stale/unaccepted master is rejected;
- rendering defects cannot mutate Core;
- preview candidate has bounded review evidence.

Evidence:

- press profile;
- input/output manifest;
- transform log;
- protected-text comparison;
- layout finding ledger.

## 0.7-preview: Optional Bridge Branch

Purpose: preview one bounded export integration without creating a destination
catalogue.

Expected capabilities:

- one declared destination contract;
- mapping and loss classification;
- sanitized export receipt;
- stale-input rejection;
- credential isolation;
- retry/idempotency behavior where applicable.

Non-goals:

- production integration platform;
- arbitrary plugins;
- bidirectional sync;
- destination as source of truth;
- KB/cross-book integration.

Entry dependencies:

- supportable 0.5 Core;
- destination owner;
- export schema;
- loss policy;
- credential and retry boundary.

Exit gate:

- positive, negative, loss, retry, stale-input, and credential-isolation cases
  pass;
- every exported claim traces to accepted source artifact;
- bridge failure leaves Core evidence unchanged.

Evidence:

- destination contract;
- mapping/loss matrix;
- sanitized receipts;
- idempotency/retry results;
- credential boundary check.

## 0.8: Production-Readiness Beta For Core

Purpose: converge Core into a production candidate family.

Expected capabilities:

- declared 1.0 Core capability/support matrix;
- reproducible distribution;
- dependency inventory;
- version reporting;
- backup, restore, upgrade, rollback or revalidation;
- evidence retention policy;
- measured reliability and resource envelope;
- safe failure behavior and sanitized diagnostics;
- proposed 1.x compatibility/deprecation policy.

Non-goals:

- new feature lanes;
- UI or hosted service;
- KB;
- arbitrary destinations;
- broadening source support without evidence.

Entry dependencies:

- 0.5 Core supportability;
- decision whether 0.6/0.7 previews remain excluded from Core 1.0;
- production security/credential boundary;
- retention and compatibility policy.

Exit gate:

- every 1.0 Core claim has an evidence route;
- clean install, representative run, interruption/recovery,
  upgrade/revalidation, backup/restore, dependency and secret checks pass;
- no architecture or policy decision is deferred into RC freeze.

Evidence:

- 1.0 capability matrix;
- compatibility proposal;
- reproducible build manifest;
- dependency inventory;
- security checks;
- reliability envelope;
- backup/restore and upgrade evidence.

## 0.9: Sourcefold 1.0 RC Freeze

Purpose: freeze the exact production candidate. This is not a feature train.

Expected capabilities:

- feature-complete Core for the 1.0 support matrix;
- final 1.x compatibility and support policies;
- candidate artifacts, tests, docs, schemas, fixtures, and evidence bound to
  one frozen manifest;
- independent Terra release review.

Non-goals:

- new profiles;
- schema redesign;
- opportunistic refactors;
- new optional branch claims;
- changing acceptance authority during RC.

Entry dependencies:

- accepted 0.8 evidence;
- closed 1.0 Core scope and acceptance matrix;
- release owner and support owner;
- freeze/reissue procedure.

Exit gate:

- all 1.0 Core acceptance rows pass or are explicitly excluded from the claim;
- no unresolved release-blocking finding;
- clean-room rehearsal and upgrade/revalidation rehearsal pass;
- independent Terra high-effort release review recommends release for the exact
  frozen candidate;
- any mutation creates `1.0.0-rc.N+1`.

Evidence:

- final release acceptance matrix;
- frozen SHA-256 manifest or revision;
- full test and rehearsal reports;
- accepted representative chains;
- limitations/support docs;
- participation declaration;
- Terra release receipt.

## 1.0: Sourcefold Core Production

Purpose: publish a production-supportable Sourcefold Core whose claims,
constraints, operational behavior, evidence, and compatibility commitments are
explicit.

Expected capabilities:

- supported headless operator workflow from declared source evidence to
  Proofread RU Master for every profile in the 1.0 matrix;
- auditable identity, lineage, trace, finding, waiver, QA, acceptance,
  supersession, revalidation, and release evidence throughout Core;
- reproducible install/run/upgrade/recovery inside the declared support
  envelope;
- stable 1.x compatibility and deprecation policy;
- optional `press` or `bridge` only if explicitly named in the support matrix;
  otherwise they remain preview/excluded.

Non-goals:

- universal OCR/PDF;
- arbitrary language pairs;
- UI or hosted service;
- multi-user collaboration;
- destination catalogue;
- KB/cross-book systems;
- Translator compatibility;
- undeclared profiles.

Entry dependencies:

- unchanged independently approved `1.0.0-rc.N`;
- final release notes;
- support/capability matrix;
- known limitations;
- upgrade/recovery guidance;
- artifact retention policy;
- release/rollback procedure.

Exit gate:

- promotion is metadata/distribution only;
- published artifacts verify against the approved manifest;
- clean supported install smoke passes;
- release evidence and support ownership are durable;
- independent Terra approval attaches to the exact production artifact.

Evidence:

- production manifest;
- distribution verification;
- clean-install smoke result;
- release notes and support matrix;
- linked RC evidence package;
- independent Terra release receipt;
- rollback/reissue readiness record.

## Post-1.0 Directions

These should not be used to justify delaying Core 1.0 unless a later charter
changes the product boundary:

- production `press` profiles, including HTML/PDF;
- production `bridge` destination catalogue;
- UI or hosted orchestration;
- multi-user review workflow;
- broader OCR/PDF/source classes;
- additional language pairs;
- Translator migration or compatibility layer;
- separate knowledge-base product direction.

## Recommended Next Goal

Start Phase 0:

```text
20260714-sourcefold-phase-0-release-charter
```

Expected output:

- release charter for 0.1;
- acceptance vocabulary;
- identity/lineage/trace/waiver/evidence decisions;
- fixture strategy;
- release acceptance matrix.

No module implementation should start before Phase 0 is accepted.
