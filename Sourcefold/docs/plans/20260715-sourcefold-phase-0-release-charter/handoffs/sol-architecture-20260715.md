# Sol Architecture Handoff

Agent: `gpt-5.6-sol` / architect

Timestamp: 2026-07-15T01:03:10+03:00

Mutations: none

Token use: 23,357 goal tokens

## Scope

Architecture review of Sourcefold Phase 0 release-charter decisions. This is
not implementation or release approval.

## Recommended Charter Shape

Treat Phase 0 as a normative decision package, not an implementation plan:

- `release_charter.md`: product claim, supported environment, language pair,
  source profile, structure subset, exclusions, release boundaries.
- `contract_decisions.md`: identity, lineage, anchors, valid DAG edges,
  acceptance authority, waiver policy, evidence vocabulary, schema evolution.
- `fixture_strategy.md`: representative pilot plus positive/negative fixtures.
- `release_acceptance_matrix.md`: every requirement mapped to automated
  validation, operator inspection, human decision, blocking severity, and
  required evidence.

Normative core lane:

```text
immutable Source Evidence
  -> reconstruct
  -> Accepted Source Text
  -> translate
  -> accepted Faithful RU Draft
  -> proofread
  -> accepted Proofread RU Master
  -> frozen 0.1 candidate
  -> independent Terra release review
```

## Source Profile Recommendation

Recommended: constrained born-digital text-layer PDF.

Definition:

- immutable, unencrypted English PDF;
- deterministic reading order;
- stable pages;
- no OCR requirement;
- support headings, paragraphs, emphasis, quotes, lists, simple rectangular
  tables, bounded cards/stat blocks, page markers, numbers, dates, dice,
  mechanics, names, and definitions;
- exclude scans, handwriting, ambiguous multi-column flow, rotated text,
  complex/nested tables, equations, and essential text embedded only in images.

Rationale: this exercises `reconstruct` and traceability without making OCR
quality, layout inference, or provider behavior part of the first release
claim.

Alternative: prepared structured Markdown plus source manifest has lower
implementation risk but may reduce `reconstruct` to ingestion/validation.

## Required Vocabulary And Lineage Decisions

- `passed`: one defined check; never artifact lifecycle state.
- `waived`: authorized disposition of one finding; visible and not corrected.
- `conformant`: exact artifact revision has complete evidence, no open
  blocking findings, and only permitted waivers.
- `accepted`: human approval of an exact conformant revision/hash for
  downstream use.
- `released`: exact frozen candidate promoted after candidate-bound evidence
  and independent Terra recommendation.

Additional controlled terms: `open`, `resolved`, `rejected`, `superseded`,
`stale`, `frozen`, `revalidated`.

Lineage policy:

- stable logical `artifact_id` plus immutable `revision_id` and SHA-256;
- never mutate accepted revisions;
- corrections create new revisions with `supersedes`;
- derived artifacts reference exact predecessor revision, hash, schema version,
  profile version, run record, and acceptance record;
- changed/superseded predecessors make descendants `stale`;
- trace anchors use stable block/unit ids in structured Markdown and sidecar
  JSON mappings;
- source anchors include page plus block/region identity;
- schema changes require migration or revalidation.

## User-Pending Decisions

- Approve headless Core 0.1 RC and English-to-Russian language pair.
- Select source profile and actual pilot.
- Approve Markdown plus JSON as canonical carriers.
- Confirm human acceptance at every core stage.
- Name stage acceptors, waiver authority, and release owner.
- Decide whether self-waiver is prohibited.
- Approve non-waivable finding classes and whether permitted waivers can still
  yield `conformant`.
- Approve supported Windows environment or require broader platform claim.
- Decide whether canonical Markdown is sufficient demonstration and no separate
  `press` artifact is needed.

## Blockers

- Source profile/pilot.
- Canonical formats.
- Acceptance and waiver authorities.
- Non-waivable classes.
- Supported environment.
- Goal-id date discrepancy between old roadmap recommendation and current
  `20260715-...` goal path.

## Verification/Evidence

Sol cross-checked roadmap blockers, contract inputs/outputs/gates, core DAG,
decision-node dependencies, required fixtures, and release-review boundary.

## Release Status

Not reviewed or approved for release. Independent Terra release review remains
mandatory for future frozen candidates.
