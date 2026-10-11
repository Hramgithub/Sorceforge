# Terra Engineering Critique Receipt

- Goal id: `20260714-sourcefold-initial-scaffold`
- Step id: `S4`
- Role / model / effort: Terra engineering assistant / `gpt-5.6-terra` / medium
- Timestamp: `2026-07-14T22:42:11+03:00`
- Elapsed time: approximately 3 minutes
- Token use: unavailable (exact telemetry was not exposed)

## Scope

Read-only structural-risk critique of the assigned Sourcefold documentation,
module-contract, fixture, and artifact-manifest scaffold. No implementation,
processing, migration, or canonical project-state changes were performed.

## Files Checked

- `Sourcefold/AGENTS.md`
- `Sourcefold/README.md`
- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/architecture/product_boundary.md`
- `Sourcefold/docs/architecture/module_contracts.md`
- `Sourcefold/docs/architecture/role_model.md`
- `Sourcefold/docs/architecture/decision_log.md`
- `Sourcefold/docs/plans/README.md`
- `Sourcefold/docs/quality/acceptance_criteria.md`
- `Sourcefold/docs/legacy/translator_evidence_index.md`
- `Sourcefold/contracts/reconstruct.md`
- `Sourcefold/contracts/translate.md`
- `Sourcefold/contracts/proofread.md`
- `Sourcefold/contracts/press.md`
- `Sourcefold/contracts/bridge.md`
- `Sourcefold/manifests/artifact_manifest.schema.json`
- `Sourcefold/fixtures/README.md`

## Findings

### Blocking

None for the documentation/schema-only scaffold. The core-versus-optional
boundary, contributor ownership, and no-migration boundary are consistent
enough to retain the scaffold as a planning baseline.

### Should Fix Before Implementation

1. **Acceptance cannot yet be made internally consistent by the manifest.**
   The schema allows `acceptance.status: accepted` while QA is `not_run` or
   `open_findings`, permits open finding references, and does not require
   acceptance actor, time, or evidence. This conflicts with the contracts and
   criteria that require resolved or explicitly waived findings and explicit
   evidence. Recommendation: define conditional schema rules for an accepted
   artifact, including QA state, no open findings, acceptance authority/time,
   and evidence or ledger references; define the waiver record requirements.

2. **Artifact lineage is only path-level, not artifact-level.** Inputs and
   outputs contain optional file hashes but no immutable upstream artifact id,
   manifest hash, source-evidence identity, or unit/page/anchor mapping. That
   prevents a consumer from proving that a draft derives from one accepted
   source text, or that a proofread edit remains traceable to it. Recommendation:
   introduce typed artifact references and a minimum traceability-anchor model
   before a module writes real artifacts.

3. **The schema does not enforce valid stage/artifact combinations or required
   upstream acceptance.** Any listed `artifact_type` can be paired with any
   `producing_stage`; the contract's stage prerequisites remain prose only.
   Recommendation: specify valid producer/type pairs and required accepted
   predecessor references, either through schema conditionals plus a graph
   validator or through an explicit validation specification.

4. **Acceptance terminology has more than one possible authority.** The
   documents use acceptance for core artifacts, press/bridge outputs, and goal
   governance/release evidence, without a declared relationship between stage
   acceptance, destination conformance, and product/release approval.
   Recommendation: name and model these separately so an accepted export or
   projection can never be interpreted as acceptance of the RU master or a
   release decision.

5. **The prose contracts require ledgers and provenance that lack a stable
   representation.** Acceptance ledgers, defect/uncertainty ledgers,
   terminology provenance, transformation assumptions, and rendering
   deviations are named but have no common identifiers, formats, or linkage
   rules. Recommendation: define a small shared evidence vocabulary and its
   references before fixtures or module implementation begin.

### Pending Decisions

1. Choose the durable identity model: content-addressed artifacts, stable ids
   with mandatory hashes, or both; decide whether external immutable source
   files receive Sourcefold manifests.
2. Define the smallest traceability unit for each source class (page, block,
   table cell, card/stat block, image region) and the policy for many-to-many
   translation/proofreading mappings.
3. Set waiver policy and authority: allowed stages, required rationale/evidence,
   expiry or review requirements, and whether a waived item may coexist with
   QA `passed`.
4. Decide the manifest evolution mechanism. With root
   `additionalProperties: false`, every future optional-lane or destination
   field requires a schema revision; a deliberate extension-point policy will
   avoid incompatible ad hoc fields.

## Verification / Evidence

- All assigned files above were read; no unlisted project areas were inspected.
- The module flow and stage terms are consistent across the product boundary,
  contract index, contracts, and acceptance criteria.
- `artifact_manifest.schema.json` parsed successfully with PowerShell
  `ConvertFrom-Json`; this verifies JSON syntax only, not full JSON Schema
  semantic validation.
- The receipt target did not exist before this task; this new file is the only
  artifact created.

## Changed Files

- `Sourcefold/docs/plans/20260714-sourcefold-initial-scaffold/handoffs/terra-engineering-critique-20260714.md` (new immutable handoff receipt)

## Blockers

None for this critique. The listed recommendations should be resolved by the
orchestrator/architect before real artifact-producing module work begins.

## Next Action

Have the orchestrator record decisions on acceptance semantics, lineage, and
evidence representation in the goal's canonical plan/context, then request an
implementation specification or an independent critic review as appropriate.
