# Q1 import QA receipt

- Goal: `20261011-sourcefold-standalone-export`; step: `Q1`.
- Role: bounded QA (`nri-qa`); assigned profile `gpt-6-luna` / `medium`. Actual runtime model/effort: unavailable.
- Orchestrator policy owner: main chat `gpt-6-sol` / `medium`; ownership unchanged.
- Assignment state: `platform-unverified`; scoped override: none.
- Scope: read-only verification of the staged standalone import and recorded evidence. No implementation, evidence regeneration, commit, push, or canonical plan/context/status edits.
- Result: **PASS**, with recorded test-result caveat below.
- Timestamp: `2026-10-11T20:14:53Z`.
- Elapsed: approximately 10 minutes. Token use: unavailable.
- Changed files: this receipt only.

## Verification and evidence

### Topology, source identity, and staging

- Read destination root `AGENTS.md`, `Sourcefold/AGENTS.md`, goal `plan.md`, `context.md`, `release.md`, and `handoffs/A1-architecture-review.md` before verification.
- Source NRI `HEAD` is exactly `22fafc14942e925b2e5f088f3c7ab1cd8efe3003`. Destination branch is `main`; configured `origin` URL is exactly `https://github.com/Hramgithub/Sorceforge.git`. Destination has no commits yet; staged import is uncommitted. No remote operation was performed.
- Destination preserves nested `Sourcefold/` topology. Source commit tree contains 3974 `Sourcefold/` paths; destination index contains all 3974 plus four new paths under `Sourcefold/docs/plans/20261011-sourcefold-standalone-export/` (`plan.md`, `context.md`, `release.md`, and A1 receipt).
- The exact six active guidance files in the declared allowlist all differ from their source working-tree bytes: `AGENTS.md`, `README.md`, `SETUP.md`, `PROJECT_STATUS.md`, `docs/architecture/role_model.md`, and `docs/plans/README.md` under `Sourcefold/`. No other source working-tree difference was found.
- All 3968 non-allowlisted files were SHA-256 compared between source working tree and destination working tree; all match, with no missing source path. Additionally, raw Git object hashes for all 3968 source working-tree files match the destination staged index blob IDs (3968/3968). Some source-tree blob IDs differ from the working tree because the source checkout has `core.autocrlf=true`; the candidate index preserves the exact measured source working-tree bytes. The explicit root `.gitattributes` uses `* -text` to preserve imported bytes.
- Six additional repository-root files are present and classified by the release packet: `.gitattributes`, `.gitignore`, `AGENTS.md`, `NRI_OCR_LAYOUT_RULES.md`, `README.md`, and `docs/governance/nri_goal_governance.md`. Together with 3978 nested paths, the destination index has 3984 paths total.
- Worktree status showed the import staged and no unstaged diff or pre-receipt untracked files. No unrelated NRI paths were staged.

### Exclusions, secrets, and file size

- `git ls-files -ci --exclude-standard` returned zero tracked ignored paths. A tracked-path scan found zero paths under `node_modules`, cache/temp/log/browser-profile/OCR-overlay/bytecode directories or with common log/temp/backup/credential names.
- The existing release/context secret-pattern scan is recorded as no matches. I did not rerun it or expose any matching file content.
- Staged Git index inventory contains 3984 blobs. Largest blob is 20,718,150 bytes; zero are at or above 100 MiB.

### Roadmap and Python test evidence

- Executed the read-only roadmap validator with the configured bundled Node runtime. It passed: 6 statuses, 7 lanes, 26 nodes, 25 edges, 254 documentation checkpoints. The validator source contains no write operations; no dependency installation occurred.
- Reviewed existing Q1 release/context evidence: focused Python validation `37 passed, 1 skipped`; full collection `1029`, with `989 passed`, `27 skipped`, and `13 failed` (totals reconcile). The records distinguish 12 stale evidence-lineage SHA assertions, reported as reproducing identically in NRI, from one test requiring historical `D:\NRI\.tools\tesseract\tesseract.exe`. The Tesseract path limitation is explicit in both current context and release, not hidden.
- The 3968 non-allowlisted files, including tests and fixtures, are byte-identical to NRI working-tree inputs. Tests were not rerun: the task forbids regenerating evidence, and the existing results are recorded in the designated release/context. Thus this QA verifies the recorded source-reproduction claim and exact source/test/evidence bytes, but does not independently reproduce the 12 failures at runtime.

## Blockers and next action

No import-scope blocker found. Runtime reproduction of the recorded Python failures was not repeated under the no-evidence-regeneration constraint; treat the existing V1/release test evidence as the recorded basis. Independent R1 release review remains required before any commit or publication. The user-provided remote was not contacted.
