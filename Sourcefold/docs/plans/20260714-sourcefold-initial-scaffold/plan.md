# Plan: Sourcefold Initial Scaffold

Goal id: `20260714-sourcefold-initial-scaffold`

State: completed

Owner: `gpt-5.5` orchestrator, medium effort

## Objective

Create the first Sourcefold documentation/schema scaffold, project rollup, and
NRI-governed goal bundle without migrating code, history, package prompts,
runtime artifacts, or active processing from `translator`.

## Role Ownership

| Role | Effort | Scope |
|---|---|---|
| `gpt-5.5` orchestrator | medium | Canonical context/status, scaffold integration, user-facing synthesis, commit scope. |
| Terra engineering assistant | medium | Critique scaffold structure after creation and write immutable handoff. |

## Steps

| Step | Owner | Status | Evidence | Next action |
|---|---|---|---|---|
| S1 Read required governance and evidence | Orchestrator | completed | Root rules, NRI governance, config status, Sourcefold bootstrap, and three named Translator evidence docs read. | Use only extracted principles. |
| S2 Create goal bundle and project rollup | Orchestrator | completed | `PROJECT_STATUS.md`, this plan, and `context.md`. | Record critique result. |
| S3 Create documentation/schema scaffold | Orchestrator | completed | Sourcefold docs, contracts, schema, fixtures README. | Verify file list. |
| S4 Terra engineering critique | Terra | completed | `handoffs/terra-engineering-critique-20260714.md`, SHA-256 `E0233140A78FE16D330C6A07D84DAC3D7E0DE5524D6874274415A91DB716AFD1`. | Record recommendations as pending decisions. |
| S5 Commit first checkpoint | Orchestrator | completed | First checkpoint commit created with only Sourcefold scaffold, Terra handoff, and prompt record staged. | Await user decision on Terra pending recommendations. |

## Definition Of Done

- Requested Sourcefold scaffold files exist.
- No code is copied from `translator`.
- No real book processing is started.
- Translator legacy material is indexed as evidence only.
- Terra medium critique is captured in an immutable handoff.
- Any Terra expansion suggestions are recorded as pending decisions rather than
  implemented without user approval.
- First checkpoint is committed only after scoped verification.

Result: first checkpoint commit created.

## Watchdog

Expected Terra artifact:
`docs/plans/20260714-sourcefold-initial-scaffold/handoffs/terra-engineering-critique-20260714.md`.

If the handoff is absent after the delegate step returns, request checkpoint,
then restart or resume the same narrow critique task and verify the artifact.
The orchestrator must not perform Terra's critique after the first missing
artifact.

## Terra Critique Result

Terra found no blocking issue for retaining the documentation/schema scaffold as
a planning baseline.

Should fix before implementation:

- make accepted artifacts internally enforce QA state, resolved or waived
  findings, acceptance authority, timestamp, and evidence;
- add artifact-level lineage and traceability anchors beyond path-level file
  references;
- define valid stage/artifact combinations and required accepted predecessors;
- separate stage acceptance, destination conformance, and release approval;
- define stable ledger/provenance/evidence identifiers and linkage rules.

Pending user or architecture decisions:

- durable identity model for artifacts and immutable source files;
- smallest traceability units and many-to-many mapping policy;
- waiver policy, authority, rationale, and interaction with QA state;
- manifest evolution and extension-point policy.

## Compact Task Packet: Terra Critique

Goal id: `20260714-sourcefold-initial-scaffold`

Step id: `S4`

Role and effort: Terra engineering assistant, medium.

Relevant paths:

- `Sourcefold/AGENTS.md`
- `Sourcefold/README.md`
- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/architecture/`
- `Sourcefold/contracts/`
- `Sourcefold/docs/quality/acceptance_criteria.md`
- `Sourcefold/docs/legacy/translator_evidence_index.md`
- `Sourcefold/manifests/artifact_manifest.schema.json`

Expected artifact:
`Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/handoffs/terra-engineering-critique-20260714.md`.

Acceptance criteria: identify structural risks, missing boundary language,
contract/schema gaps, or accidental legacy inheritance. Do not modify canonical
plan/context/status. Do not broaden scope into code migration or real book
processing.

Forbidden scope: `CoC`, `Dune`, `Git`, `FoundryVTT`, `.tools`, `.agents`,
temporary folders, and all `translator` files except the three named legacy
evidence docs already summarized in Sourcefold docs.
