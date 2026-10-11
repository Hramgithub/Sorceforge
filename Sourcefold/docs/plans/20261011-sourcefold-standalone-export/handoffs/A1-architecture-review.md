# A1 architecture review: Sourcefold standalone export

- Goal: `20261011-sourcefold-standalone-export`; step: `A1`.
- Role: architecture and dependency analyst; assigned model/effort `gpt-6-astra` / high; independently verified runtime model/effort unavailable.
- Orchestrator policy owner: main chat, `gpt-6-sol` / medium. Ownership remains with the main chat.
- Assignment state: `platform-unverified`; scoped override: none.
- Source: `C:/_Hobby/_work/NRI/Sourcefold`; observed NRI HEAD `22fafc14942e925b2e5f088f3c7ab1cd8efe3003`.
- Destination: `C:/_Hobby/_work/Sorceforge`; user-supplied remote `https://github.com/Hramgithub/Sorceforge.git`.
- Scope: read-only topology, tracked inclusion boundary, external dependencies and minimum import verification. Sole authorized write: this receipt. No source copy, runtime installation, processing, source mutation, Git mutation or release decision.
- Result: architecture recommendation complete; import execution/QA/release remain with the assigned owners.
- Timestamp: `2026-10-11T19:51:00Z` (drafting time, approximate to the minute). Elapsed approximately 4 minutes; exact elapsed/token metering unavailable.

## Recommended decision

Keep `Sourcefold/` nested inside the Sorceforge repository and retain all 3974 tracked Sourcefold paths from the frozen source revision. Add a small root entry point and project-local copies of the governing NRI rules, fix only active guidance needed for standalone use, and document historical runtime dependencies. Do not flatten, rename the product, remove failed fixture attempts, rewrite manifests, or change execution-script hashes as part of an archival export.

This produces a portable source/evidence repository with runnable static checks after declared dev dependencies are installed. It does not establish a newly runnable, accepted book-processing system or authorize repeating historical OCR runs.

## 1. Topology and data-contract dependency

`Sourcefold/tools/roadmap-validator/validate-roadmap.mjs:7-26` computes `projectRoot` as its grandparent and `repoRoot` as the project's parent. Canonical values starting `Sourcefold/` resolve against that parent; other values resolve against the project root. The validator checks existence of canonical/viewer paths, reference documents, every node's linked plan and checkpoint plans.

`Sourcefold/docs/roadmap/roadmap.yaml:6-13` uses `Sourcefold/docs/...` for canonical/viewer/reference paths. Targeted scan of docs/scripts/tests/contracts found 382 `Sourcefold/` reference lines in 72 files. Many additional fixture records carry such lineage paths. Most Python tools instead derive their root from `Path(__file__).resolve().parents[1]`, then descend into fixtures/scripts: preserving the project directory preserves both conventions simultaneously.

Flattening would make the validator's canonical paths point outside the checkout or into a nonexistent sibling `Sourcefold`, require broad path migration, and risk changing pinned evidence/generator hashes. It is a separately scoped migration, not necessary export work. Do not make flattening appear to pass by symlinking back to NRI.

Proposed tree:

```text
Sorceforge/
  README.md                     # repository/product naming and cd Sourcefold
  AGENTS.md                     # thin standalone policy entry point
  .gitattributes                # explicit byte-preservation policy for import
  .gitignore                    # optional root runtime exclusions only
  NRI_OCR_LAYOUT_RULES.md        # attributed governance snapshot
  docs/governance/nri_goal_governance.md
  Sourcefold/                   # original tracked topology
    AGENTS.md
    README.md
    SETUP.md
    package.json
    package-lock.json
    contracts/ docs/ fixtures/ manifests/ scripts/ tests/ tools/
```

`npm ci`, `npm run validate:roadmap` and Python tests run from `Sorceforge/Sourcefold`, not from the repository root. The root README should make that single-directory distinction explicit.

## 2. Exact inclusion boundary

Live native-Git `ls-files -- Sourcefold` inventory:

| Tracked category | Files | Treatment |
| --- | ---: | --- |
| fixtures | 3408 | Retain all; candidate inputs, reviewed assets, trial candidates, manifests, metrics, negative evidence and lineage |
| docs | 186 | Retain historical decisions, plans, receipts, roadmap and acceptance boundaries |
| scripts | 186 | Retain reusable contracts and scoped historical producers; presence is not new execution authority |
| tests | 179 | Retain complete regression corpus; this is file count, not test-case count |
| contracts | 5 | Retain |
| manifests | 1 | Retain |
| tools | 1 | Retain roadmap validator |
| Top-level project files | 8 | `.gitattributes`, `.gitignore`, `AGENTS.md`, package/lock, README, SETUP, PROJECT_STATUS |
| Total | 3974 | No source-subtree exclusions recommended |

Of the 3408 fixture files, 3404 are below `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/`. The other four are the Viral candidate PDF, its README, the selected-page manifest and fixtures README. The local PDF's README records 20,718,150 bytes and SHA-256 `0A80B6F389821B87553D26746D2BE171B4482BA9BBC6E3EB3FEC26274EDBED05`; the old Yandex.Disk origin is provenance, not a required live filesystem path once the local candidate copy is verified.

Representative large retained groups are the crop-safe second pass (401 files), OCR remediation matrix (351), P009 remediation matrix (318), weak-page diagnostics (270), corrected geometry probe (168) and automatic column/line segmentation search (159). Size or a generated filename does not make these disposable.

Retention is supported by:

- `Sourcefold/AGENTS.md`: candidate inputs are durable for bounded qualification and require separate authorization before processing.
- `Sourcefold/PROJECT_STATUS.md:37-53`: the first geometry attempt is explicitly quarantined, and failed/superseded candidates remain in evidence run folders, separate from any future production assembly.
- `Sourcefold/scripts/build_core_0_1_text_extraction_first_pass_runtime_selector_run_001_020.py`: exact SHA-256 pins bind authorization, readiness, selected-page manifests and specific candidate files across trial directories.
- `Sourcefold/scripts/artifact_lifecycle_validation.py`: stale/held/superseded/readability-only evidence must not be used as current authority; retaining that evidence is different from selecting it for production.
- `Sourcefold/.gitattributes`: named OCR/reconstruction trial groups deliberately preserve exact bytes, including TSV trailing empty columns.

A targeted tracked-path scan found zero entries under standard tmp/temp/cache/node_modules/__pycache__/logs/ocr-overlays/browser-profiles directories or ending `.log`, `.tmp`, `.pyc`, `.bak`. This is a narrow classification check, not a complete secret/content audit. Twelve tracked paths contain `overlay` in their name; they belong to explicit reconstruction evidence and must not be confused with ignored generic `ocr-overlays/` runtime debris.

Therefore export the frozen Git-tracked subtree, not an indiscriminate directory copy. Exclude untracked/ignored tools, runtime caches, credentials and unrelated NRI projects by construction. Any later proposed deletion of tracked evidence requires its own exact dependency/retention assessment and authorization; no such deletion is needed here.

## 3. Governance and active-reference remediation

Required local policy support:

1. Add the current canonical NRI governance at destination `docs/governance/nri_goal_governance.md` with source revision/provenance in the export record. Add `NRI_OCR_LAYOUT_RULES.md` at the destination root because the inherited workspace mandate otherwise disappears. These are bounded, explicit imports of governing policies, not a migration of Translator governance.
2. Add a thin root `AGENTS.md` that establishes those two local authorities, protects immutable inputs/evidence, names the nested project root and retains the current NRI role/acceptance boundaries. Do not import NRI's local `.codex`, credential, host or unrelated project configuration.
3. Update active `Sourcefold/AGENTS.md` and `Sourcefold/docs/architecture/role_model.md` to defer to the imported current role matrix. Their current matrices conflict with each other and with NRI: AGENTS uses GPT-5.6/GPT-5.5; role_model uses GPT-5.5 orchestration, Terra criticism and GPT-5.4 execution. Main-chat policy is GPT-6 Sol/medium, with architecture/independent criticism GPT-6 Astra/high, engineering Sol/high, execution Luna/high, QA Luna/medium. Apply the orchestrator's recorded resolution; retain historical reviewers/receipts unchanged.
4. Correct active file-relative policy links: `Sourcefold/AGENTS.md` already names `../docs/governance/nri_goal_governance.md` correctly for this nested topology. From `Sourcefold/docs/architecture/role_model.md` and `Sourcefold/docs/plans/README.md`, the correct relative path to root governance is `../../../docs/governance/nri_goal_governance.md`; their current `../../docs/...` spelling resolves inside Sourcefold instead.
5. Add an export/standalone note to active README/SETUP with actual snapshot state and limitations. The README still calls fixtures empty and the project documentation/schema-only, while it contains 186 scripts, 179 test files and 3408 fixture artifacts. Do not publish that stale scaffold description as an accurate inventory. Preserve historical plans and receipts as historical evidence.

Legacy `translator/...` references in `docs/legacy/translator_evidence_index.md` and the bootstrap document are deliberate external historical references. Label their origin/revision and availability; do not copy Translator code or its status to make every historical mention locally resolvable. Targeted script/tool search found no direct CoC/Dune/Translator code import or runtime subtree dependency; this does not certify every historical hyperlink as portable.

Freeze imported code/evidence bytes. Record a small allowlist of portability-edited active guidance and separately added files; all other imported paths should retain source blob identity. Do not use a global search-and-replace for `NRI`, usernames, drive letters, Sourcefold or the repository slug.

## 4. Runtime and host dependencies

| Dependency | Evidence/use | Export treatment |
| --- | --- | --- |
| Node/npm and `yaml` | package/lock declare private `@nri/sourcefold-devtools`; lock pins `yaml@2.9.0`, its integrity and node engine constraint | Preserve package and lock; install with `npm ci` in Sourcefold. Do not copy `node_modules`. Do not equate the dependency's Node minimum with a verified whole-project supported range. |
| Python + pytest | 179 test files; many tests use pytest, scripts use standard JSON/path/hash/subprocess APIs | Document and provision a discovered development interpreter and pytest for checks. No Python lock/requirements file was identified in the inspected project root; do not claim reproducible Python setup from package-lock alone. |
| Pillow | OCR preprocessing and image/geometry contract checks (`from PIL import Image, ImageOps`) | Declare test/runtime dependency; do not copy a workstation virtualenv. No proof of a complete transitive environment was gathered by A1. |
| Tesseract English OCR | Historical scripts hardcode `D:/NRI/.tools/tesseract/tesseract.exe`; frozen config records language, OEM/PSM and txt/TSV outputs | Preserve historical producer/config bytes, document nonportable execution. Future rerun needs explicit executable/model identity, runtime rebinding/new record and bounded authorization. No global path rewrite and no opportunistic copying `.tools`. |
| Browser network and local HTTP | `docs/roadmap/roadmap_viewer.html:7` loads js-yaml 4.1.0 from jsDelivr; line 596 fetches sibling roadmap.yaml | Viewer is not fully offline; a local static server/browser may be needed for fetch. CLI validator uses locked npm `yaml`, a different parser/runtime. Offline viewer packaging would be a separate change unless explicitly included. |
| PowerShell | Roadmap wrapper and documentation checkpoint script | Document on Windows; checkpoint defaults to dry-run, `-Apply` mutates canonical docs and is not an import-validation command. |
| Windows long paths | Longest tracked relative path is 272 characters; under requested destination it becomes 299 characters | Set destination Git `core.longpaths=true` before materialization and use long-path-capable copying/archive extraction. Verify a fresh checkout, not only file creation. Do not shorten governed IDs/directories to bypass this. |
| Historical source and machine paths | Viral README names original Yandex.Disk path; trial records contain old workstation paths and engine receipts | Keep as attributed provenance. Distinguish source already copied into fixtures from an actual missing required runtime. Do not assert the old location is currently live. |

Known execution path examples: `scripts/build_core_0_1_text_extraction_smoke_p009.py:18,109`, `build_core_0_1_text_extraction_frozen_profile_config.py:139`, P010/P015 smoke scripts, overview replay, remediation matrix and refined-OCR runners. New location support for these producers is outside a byte-preserving export: their script hashes and outputs participate in lineage.

The protected source PDF is present in the tracked boundary, so no additional book assets should be silently sourced from external drives. OCR and source-processing authorization remains bounded to exact named inputs/actions, not renewed by cloning, moving, test success or publication.

## 5. Minimum verification contract

All execution below belongs to V1/Q1 in the destination after import; A1 did not run tests or install dependencies and did not write into NRI.

### V1 inventory and byte preservation

- Freeze source commit and enumerate all 3974 tracked paths. Compare destination imported paths and Git blob IDs (or exact-byte SHA-256 before staging), allowing only a documented finite portability-edit list. Include all 3408 fixture paths and inherited `.gitattributes`.
- Prevent line-ending normalization from silently altering evidence. Export Git object bytes and apply a root attribute policy that preserves imported bytes, while retaining the project's more specific attributes. Do not copy all unrelated NRI LFS attributes; derive only what is applicable and verify effective attributes/index blobs.
- Check source PDF identity, binary header/payload validity, largest ordinary blob and no pointer substitutions. The governing packet measured no file over 50 MiB; V1 must confirm the actual staged candidate. No LFS migration is required solely because the overall corpus is large.
- Audit added/changed files and tracked payloads for secrets, temporary/runtime directories and unrelated project content. Path heuristics alone do not satisfy this check.

### V1 reproducible static-tool checks

From `Sorceforge/Sourcefold`, install locked Node dependencies and run `npm run validate:roadmap`. Validate canonical and viewer paths and representative checkpoint/linked-plan existence. Run checkpoint helper only in dry-run with the explicit export goal if that command is being verified; confirm no canonical file changed.

Run a focused Python gate using a discovered interpreter, for example `python -B -m pytest -p no:cacheprovider` followed by:

```text
tests/test_artifact_lifecycle_validation.py
tests/test_bounded_authorization_contract.py
tests/test_human_review_gate_contract.py
tests/test_ocr_input_surface_policy.py
tests/test_source_reconstruction_crop_guardrails.py
tests/test_core_0_1_text_extraction_first_pass_runtime_selector_run_001_020.py
```

This covers stale-artifact refusal, exact authorization scope, human review boundary, OCR-safe surface/ref-scoring quarantine, geometry semantics, and sealed existing runtime-report lineage/fail-closed entry points. Some selector pre-output tests intentionally skip when real output exists; report such skips precisely rather than claiming those checks ran anew.

Then run the whole existing `tests/` suite in the destination. Use an external temporary/cache directory and disable Python bytecode/cache output as appropriate. Review collection/subprocess behavior first: many tests invoke scripts only with missing/wrong authorization to prove refusal, or read existing sealed evidence. Do not run historical authorized producers or fresh OCR merely to make a test pass. Record all failures/skips and compare whether they represent import breakage, dependency absence or pre-existing evidence state. Verify before/after hashes for governed payloads.

### Q1 fresh-checkout and policy checks

- Verify the destination can be checked out under the requested Windows path with all files, then run the roadmap validator and focused suite from documented cwd without relying on NRI imports, symlinks or copied runtime state.
- Check active policy links and matrix, root README cwd instructions, retained historical external references and the precise portability exception list.
- Confirm production readiness, whole-book acceptance and current OCR authority are not inferred from fixture admission or imported receipts. Existing first-pass selector tests explicitly expect `production_ready=false` and `all_pages_fresh_ocr_success=false`.
- Independent critic R1 reviews the frozen exact candidate after evidence capture. A1 is architecture input, not final release approval.

If the broad tests fail for a genuine portability defect, separate the minimally required fix from archive preservation; assign a bounded remediation, update its tests and freeze/review again. Do not rewrite historical evidence to erase failures.

## 6. Sorceforge versus Sourcefold

Use exactly the user's remote slug `Sorceforge` and destination directory. Preserve product name `Sourcefold`, canonical folder/path prefix, package name `@nri/sourcefold-devtools`, schema IDs, gate/run IDs and historical references. Those are separate identities; a repository-hosting name does not rename contracts.

Root README should say: this repository is named Sorceforge and contains the Sourcefold project in `Sourcefold/`. Verify remote URL before commit/publish. Avoid casual correction to Sourceforge or Sourcefold in Git commands; do not manufacture package/domain/trademark claims. Renaming paths or schemas requires a separately authorized migration and lineage plan.

## Assumptions, blockers and next action

Assumptions: the goal packet's 3974-path frozen source boundary is intended; publication of that already tracked project snapshot is within the main chat's user authorization; this is not a book-processing or runtime-porting task. Relevant exact task constraints prevail over stale local model defaults, as explicitly confirmed by the orchestrator.

No blocker to the recommended nested, full-evidence import. Known limitations are nonportable historical OCR executables, viewer CDN dependency, stale active guidance and missing standalone policy support. Artifact state remains candidate/review/evidence according to each contract; export does not upgrade it.

Next action: main chat closes topology/retention decisions, materializes exact tracked bytes, integrates the finite policy/README/SETUP additions, then invokes V1/Q1 and independent R1. Any import mutation of scripts, data contracts or historical evidence is a scope deviation requiring an explicit separate rationale.

Files checked: assigned destination plan/context; source AGENTS/README/PROJECT_STATUS/SETUP/package/lock/attributes/ignore; roadmap YAML/viewer/validator and wrapper; documentation checkpoint script; current role model/plans index/legacy evidence index/bootstrap references; fixture READMEs; canonical Phase-0 context; representative OCR policy/lifecycle/runtime-selector/frozen-profile/smoke scripts and their tests; full Git-tracked path inventory and targeted external-path/import scans. Native Git HEAD/path counts and live longest-path calculations were verified. No full file-content audit, actual OCR, complete regression run or release decision was performed.

Changed files: this receipt only. NRI was read-only. Memory was consulted for the prior Sourcefold long-path failure; the current 299-character destination path risk was independently verified.
