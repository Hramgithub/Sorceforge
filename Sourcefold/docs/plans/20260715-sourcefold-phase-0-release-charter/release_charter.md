# Sourcefold Core 0.1 Release Charter

Status: draft for Phase 0 decision

## Release Claim

Sourcefold Core 0.1 RC proves that the core lane can produce an auditable
Russian master for one declared source profile:

```text
reconstruct -> translate -> proofread
```

The release is a headless, operator-run release candidate. It is not a
production claim and not a broad document-ingestion claim.

## Recommended 0.1 Boundary

| Area | Recommendation | Status |
|---|---|---|
| Product lane | Core only: `reconstruct`, `translate`, `proofread`. | proposed |
| Operator mode | Headless CLI/scripted workflow with durable artifacts. | proposed |
| Language pair | Source language to Russian. | proposed |
| Source profile | Constrained OCR-first RPG PDF profile. | pending user decision |
| Canonical text format | UTF-8 Markdown with explicit anchors and page/block markers. | proposed |
| Canonical evidence format | JSON manifests/ledgers validated by schema. | proposed |
| Release state | RC only until candidate freeze and independent Terra review. | proposed |

## First Source Profile Options

| Option | Description | Strength | Risk | Recommendation |
|---|---|---|---|---|
| OCR-first RPG PDF profile | Input is PDF; Sourcefold creates page images; OCR is primary text acquisition; text layer is auxiliary. | Matches real NRI evidence better and exercises `reconstruct`. | Requires staged OCR/order/overlay QA methodology. | current user preference |
| Constrained born-digital text-layer PDF | Immutable, unencrypted text-layer PDF with deterministic reading order and no OCR requirement. | Exercises `reconstruct` without OCR. | Text layers in real RPG PDFs are often unreliable. | demoted |
| Prepared Markdown package | Operator supplies source text as Markdown plus source/evidence metadata. | Best for proving contracts before extraction complexity. | Reconstruction may look too easy unless evidence/anchors are strict. | fallback only |

Current recommendation:

Use a **constrained OCR-first RPG PDF profile**. The input is always a PDF; the
first acquisition step creates page screenshots/images that become working
visual evidence. OCR is the primary text acquisition route. Existing PDF text
layers may be used only as auxiliary comparison evidence, never as the primary
source of truth.

Render profile status: evidence-gated. Selected pages must be rendered by a
pinned tool/configuration to stable page images with page ids, PDF-page mapping,
dimensions, file hashes, and canonical pixel hashes. `300 DPI`, `8-bit sRGB`,
and `PNG` are benchmark candidates, not accepted values, until prior-work and
`Вирал` pilot evidence qualify them.

This is still constrained: 0.1 does not claim broad OCR/PDF support.

## Decision Closure Table

Every Phase 0 decision must use this closure shape before implementation can
start.

| Decision | Proposed Value | Approver | Status | Invalidation Conditions |
|---|---|---|---|---|
| Source profile | Constrained OCR-first RPG PDF profile. | user | pending | Any change to source class, page-image evidence, OCR-primary rule, structure subset, or immutable evidence rules. |
| Canonical text carrier | UTF-8 Markdown with explicit anchors/page markers. | user/orchestrator | proposed | Any change to anchor model, canonicalization, or supported structures. |
| Evidence format | JSON manifests/ledgers validated by schema. | user/orchestrator | proposed | Any change to manifest boundary, hash algorithm, or schema versioning. |
| Acceptance authority | Human operator/reviewer accepts; tools only pass/fail/conform. | user/orchestrator | proposed | Any automated acceptance claim or authority change. |
| Artifact identity | Stable id plus schema version, content hash, predecessors, source profile, status. | Sol/Terra/user | draft | Any hash/canonicalization, predecessor, or supersession model change. |
| Trace anchors | Source page/block/span to derived block ids, optional block hashes. | Sol/Terra/user | draft | Any change to anchor granularity or source profile evidence. |
| Waiver policy | Finding-scoped waiver with authority, rationale, anchor scope, evidence, review point. | user/orchestrator | pending | Any waiver affecting release claim, severity eligibility, or closure semantics. |
| Fixture strategy | One positive fixture plus negative fixtures for unsupported profile, waiver, stale lineage, open finding, and bad edge. | user/orchestrator | draft | Any change to source profile or acceptance/lineage rules. |

Required closure fields for each accepted decision:

- final value;
- rationale;
- approver;
- date/version;
- affected acceptance-matrix rows;
- invalidation conditions.

## Supported Layout And Structure Subset

Proposed layout profile:

- PDF input is converted to page images before OCR review.
- One- and two-column pages are in scope.
- Reading order must be evidenced by page image, OCR block geometry, reading
  order ledger, overlay review, and human acceptance.
- Complex layout is allowed only when it can be reduced to reviewed anchored
  blocks within the supported structure taxonomy.
- Reading-order ambiguity creates a finding and blocks source acceptance until
  resolved. For Core 0.1, unresolved reading-order ambiguity is non-waivable.

Provisional structure subset:

- headings;
- paragraphs;
- emphasis;
- quotes;
- ordered/unordered lists;
- simple tables;
- stat blocks;
- boxed text;
- callouts;
- sidebars;
- captions;
- page headers/footers;
- page markers;
- anchored blocks.

Needs evidence pass before acceptance:

- final RPG structure taxonomy from prior processed books;
- exact supported/deferred structure list;
- examples from prior projects;
- structure-specific findings and acceptance criteria.

Deferred unless explicitly included:

- handwritten text;
- unreadable scans;
- decorative text requiring visual interpretation;
- maps as semantic text source;
- complex nested tables;
- text meaningful only inside images without review evidence.

## Non-Goals

- broad OCR/PDF support;
- multiple source profiles;
- `press` or `bridge` release claims;
- UI, hosted service, multi-user workflow;
- knowledge base generation;
- Translator compatibility or migration;
- automated semantic acceptance without human authority.

## Exit Gate

Current post-P020 readiness status: `G1FARP-G1-VIRAL-001` prepares
fixture-admission / whole-Gate-acceptance readiness only from
`G1SPDR-G1-VIRAL-001`. It preserves 5 Gate review candidate rows, 2 existing
Core 0.1 OCR parking outcomes, 2 evidence-only rows, 2 blocked rows, and 1
page `021+` separate-BA row. Fixture admission and whole Gate 1 acceptance
remain separate future decisions.
`G1FARPREV-G1-VIRAL-001` accepts that readiness/blocker packet only, and
`G1FABRP-G1-VIRAL-001` now prepares fixture admission blocker-resolution
questions without admitting fixtures, creating fixture manifests, processing
page `021+`, or accepting whole Gate 1.
`G1FABRPREV-G1-VIRAL-001` accepts `G1FABRP-G1-VIRAL-001` as blocker-resolution
prep only; `G1UNFPDP-G1-VIRAL-001` prepares unsupported/negative fixture policy
decision material only. `G1UNFPDPREV-G1-VIRAL-001` accepts that prep packet for
policy-record preparation, `G1UNFPR-G1-VIRAL-001` prepares the policy record
candidate, and `G1UNFPAR-G1-VIRAL-001` accepts the unsupported/negative fixture
policy decision only. `G1FSFDP-G1-VIRAL-001` prepares fixture strategy fit
decision material, and `G1FSFAR-G1-VIRAL-001` accepts the fixture strategy fit
decision only. `G1FARR-G1-VIRAL-001` refreshes fixture admission readiness
only. `G1FMP-G1-VIRAL-001` prepares the future fixture manifest shape only, and
`G1FMR-G1-VIRAL-001` records that fixture manifest shape without admitting
fixtures. `G1FADP-G1-VIRAL-001` prepares fixture admission decision material
only, `G1FADAR-G1-VIRAL-001` accepts fixture admission without accepting whole
Gate 1, `G1WGARR-G1-VIRAL-001` prepares whole Gate 1 acceptance readiness
recheck only, and `G1WGADR-G1-VIRAL-001` accepts whole Gate 1 only for pages
001-020 and the `G1FADAR` admitted fixture manifest groups. Page `021+` remains
blocked. `C01IPP-G1-VIRAL-001` prepares Core 0.1 implementation planning only
from that accepted Gate 1 scope; it does not create runtime implementation or
an implementation authorization receipt. `C01IAR-G1-VIRAL-001` prepares that
authorization receipt as evidence material only and records runtime
implementation as still unauthorized pending first-slice prerequisites.
`C01FSDP-G1-VIRAL-001` prepares first-slice design material for
`C01WP-01-phase-1-scaffold-contracts` only and still creates no runtime
implementation or source-profile lock/acceptance. `C01SPLPR-G1-VIRAL-001`
records source-profile parking only for the C01WP-01 design-prep boundary and
still creates no runtime source-profile lock or runtime implementation.
`C01FSARP-G1-VIRAL-001` prepares the first-slice Sol/Terra architecture review
packet only and still creates no runtime implementation or runtime
source-profile lock/acceptance. `C01AMTR-G1-VIRAL-001` prepares
acceptance-matrix claim/evidence trace review material only and still creates no
runtime implementation or runtime source-profile lock/acceptance.
`C01RSPLP-G1-VIRAL-001` records runtime source-profile parking for C01WP-01
authorization-prep only and still creates no runtime implementation or runtime
source-profile lock/acceptance.
`C01RSAP-G1-VIRAL-001` prepares first-slice runtime authorization decision
context for C01WP-01 only and still creates no runtime authorization grant,
runtime start, runtime implementation, or runtime source-profile
lock/acceptance.
`C01RSAD-G1-VIRAL-001` records a non-executing first-slice runtime
authorization decision for C01WP-01 only and still creates no runtime
start/execution, runtime implementation, or runtime source-profile
lock/acceptance.
`C01RSPLAD-G1-VIRAL-001` records a runtime source-profile
lock-or-acceptance decision for C01WP-01 only; it grants no runtime
source-profile lock/acceptance, keeps the runtime source profile parked, and
still creates no runtime start/execution or implementation.
`C01TETD-G1-VIRAL-001` completes a Sol/Terra-reviewed points 1-5 readiness
chain toward a future text extraction smoke trial; point 6 remains blocked
until Bogdan is called, and no OCR/PDF parsing/text-layer extraction or actual
text extraction is performed.

Phase 0 exits only when these are accepted or explicitly parked:

- source profile;
- OCR/page-image acquisition boundary;
- canonical formats;
- acceptance vocabulary;
- acceptance authority;
- artifact identity;
- lineage and trace anchors;
- waiver policy;
- fixture strategy;
- release acceptance matrix.

## Implementation Authorization Receipt

Module/schema implementation may start only after a Phase 0 receipt states:

- every required decision is `accepted` or explicitly `parked` out of 0.1;
- the first source profile is locked;
- the acceptance matrix maps every 0.1 claim to evidence;
- Sol architecture review is recorded;
- Terra independent critique is recorded;
- roadmap validation passes;
- the user authorizes Phase 1.
