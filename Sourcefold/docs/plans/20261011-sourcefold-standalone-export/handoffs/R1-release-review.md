# R1 independent release review: Sourcefold standalone export

- Goal ID: `20261011-sourcefold-standalone-export`; step ID: `R1`; review_kind: `release`.
- Role: `nri-independent-critic`; assigned profile `gpt-6-astra` / `high`. Independently verified platform model/effort: unavailable.
- Participation declaration: I did not implement or materially design this candidate. I performed independent read-only review and authored only this receipt.
- Orchestrator policy owner: main chat `/root`, `gpt-6-sol` / `medium`; orchestration ownership remains there.
- Assignment state: `platform-unverified`; scoped override: none.
- Decision: **APPROVED** for publication of the exact reviewed standalone source/evidence snapshot, subject to the publication preconditions below.
- Blocker findings: none. Non-blocker limitations are explicitly listed below; this is not a green-suite or product-runtime acceptance.
- Assignment result: completed.
- Timestamp: `2026-10-11T20:19:22Z` (UTC clock tool).
- Elapsed: approximately 3 minutes. Token use: unavailable.

## Exact frozen candidate

- Repository: `C:/_Hobby/_work/Sorceforge`, branch `main`.
- Reviewed commit: `c557381c119ec03d420a0121784a5e111ebd94e8`.
- Reviewed tree: `3a7f1a8a4113fcf362fcdbdcff99c86af7556e43`.
- Parent: none; initial root commit.
- Commit time: `2026-10-11T23:16:24+03:00` (`20:16:24Z`).
- Source identity: NRI `22fafc14942e925b2e5f088f3c7ab1cd8efe3003` at `C:/_Hobby/_work/NRI`.
- Candidate freeze evidence: committed export `release.md`, source/allowlist contract, and the exact assigned commit above. Release file LastWriteTimeUtc observed `20:15:55`, before commit and review. The commit is the immutable revision boundary; no future-dated freeze is inferred.
- Configured fetch and push remote: `https://github.com/Hramgithub/Sorceforge.git`, named `origin`.

Independent `git ls-remote origin` during this review returned no refs and exit code 0. This confirms an empty advertised remote at that observation, not a guarantee that it remains empty until publication. The critic did not fetch, commit, amend, or push.

## Independent inventory and byte verification

Source commit enumeration contains exactly 3974 paths below `Sourcefold/`. Candidate HEAD contains 3985 paths: all 3974 source paths, no missing source path, plus the ten initial additions and Q1 receipt.

Compared every source-working-tree path to its destination-working-tree counterpart with SHA-256. Result: **3968 identical**, **six changed**, **zero unexpected differences**, and every allowlisted file actually changed. The exact allowlist is:

- `Sourcefold/AGENTS.md`
- `Sourcefold/README.md`
- `Sourcefold/SETUP.md`
- `Sourcefold/PROJECT_STATUS.md`
- `Sourcefold/docs/architecture/role_model.md`
- `Sourcefold/docs/plans/README.md`

Independently bound all destination files to the frozen Git tree: raw `git hash-object --stdin-paths` results matched the corresponding HEAD blob IDs for **3985/3985** files. Therefore the SHA-256 source/destination comparison describes the committed bytes, not only unstaged working copies.

The source tree was clean for `Sourcefold/`; source status showed only the previously protected `.codex/config.toml` and `CODEX_CONFIG_APPLIED.md` modifications. Source HEAD matched the assigned revision. The preserved identity is exact source-checkout bytes, as the QA explicitly records; source Git object bytes can differ in line endings due to NRI `core.autocrlf`. No claim is made that every imported text blob has the original source Git blob ID.

The 11 added paths are exactly:

- Root `.gitattributes`, `.gitignore`, `AGENTS.md`, `README.md`, `NRI_OCR_LAYOUT_RULES.md`.
- Root `docs/governance/nri_goal_governance.md`.
- Export-goal `plan.md`, `context.md`, `release.md`, `handoffs/A1-architecture-review.md`, `handoffs/Q1-import-qa.md`.

Read every six-file guidance diff. Changes are limited to current role/governance links, actual project inventory, standalone topology/setup, explicit runtime gaps, and the standalone transition checkpoint. No implementation, fixture, test, historical receipt, schema, source PDF, or acceptance record was changed.

The nested topology is justified by the roadmap validator's actual path resolver: `Sourcefold/...` paths resolve from the parent repository, while ordinary paths resolve from the nested product root. Product/schema identity remains Sourcefold; the repository slug alone is Sorceforge.

## Policy, exclusions, size, and secret checks

- Root governance SHA-256 matches its NRI counterpart: `CADB101DF6E6CF95A078109B3ECCA635B7AD4A1972FA45FC5E770C3E93588200`.
- Root OCR layout policy SHA-256 matches its NRI counterpart: `A1FD77774AD70C206802DF8042ED4A9352BBAC1166252411D9DDBF9B211B2970`.
- Viral source-candidate PDF is present as payload, SHA-256 `0A80B6F389821B87553D26746D2BE171B4482BA9BBC6E3EB3FEC26274EDBED05`.
- Largest committed blob is that PDF, **20718150 bytes**; no blob reaches 50 MiB or 100 MiB. No LFS conversion is necessary for this bounded export.
- `git ls-files -ci --exclude-standard`: zero tracked ignored files.
- Committed-path scan: zero standard dependency/cache/temp/log/browser-profile/bytecode/credential-file path matches. Governed overlay-named fixture evidence is retained according to A1, not discarded by a broad name filter.
- Independent tracked-text Git grep for AWS access-key IDs, GitHub token formats, long OpenAI-style key signatures, and private-key headers: zero matching paths; grep exit 1, meaning no matches. This is a bounded signature check, not proof that no conceivable secret exists.
- Worktree was clean before writing this receipt. Local development dependencies may exist ignored on disk but are not in the candidate tree.

Unrelated NRI projects, runtime directories, caches, credentials, browser profiles, and temporary files are outside the published candidate. All 3408 governed fixture/evidence paths are intentionally retained; failed or superseded evidence is not promoted to production authority by being retained.

## Test evidence, inherited failures, and non-blockers

Consumed A1 architecture and Q1 bounded QA receipts. Q1 independently ran the roadmap validator successfully: six statuses, seven lanes, 26 nodes, 25 edges, 254 documentation checkpoints. V1/Q1 record focused Python results of 37 passed / one skipped, and full collection of 1029 cases: 989 passed, 27 skipped, 13 failed. This review does not relabel that suite as passing.

The orchestrator additionally supplied the actual V1 commands and failed node IDs from captured tool records. Twelve stale evidence-lineage assertions were rerun in NRI: 12 failed / 64 passed with the same assertion hash pairs. The separate thirteenth failure is `test_012_016_020_pre_output_scope_and_pins`, which reaches the inherited Tesseract executable requirement. The test runner used an existing external pytest interpreter and MinerU site-packages; this is environment-backed testing, not proof of a locked standalone Python environment. No persisted raw V1 log was available; exact runtime counts/source rerun results remain attributed to those V1 records and QA, not a fresh critic test run.

Independent corroboration:

- All relevant tests, producers, and evidence are within the 3968 byte-identical set.
- A sampled stale lineage pin in `gate_1_review_decision_report.json` expects brief-report SHA `E577B18D7E8945C39FA5286D83FD9D8607B45636ABD82243ED4A9F002B306FE8`; actual source and export both equal `210CEC9E840D255E66012E8F65161BDE181A8A689C9BB94195ECAD1B18395775`. This independently confirms an inherited mismatch without regenerating evidence.
- The method-family script imports `overview.TESSERACT`, checks its existence, and the overview script defines `D:\NRI\.tools\tesseract\tesseract.exe`. SETUP and release explicitly disclose this portability limitation.

These are **non-blockers for publishing the archival source/evidence snapshot**, but they remain unresolved debt and limitations for future runtime or lineage acceptance. Do not reseal records or rerun OCR just to make the export appear green. Python dependency locking, historical OCR runtime rebinding, browser-viewer CDN dependence, and future live execution belong to separately scoped work.

## Phase 0 and authority boundary

Root README, project README/AGENTS, current status, and export release explicitly retain Phase 0. The six guidance diffs add no gate acceptance, whole-book acceptance, promotion of candidate-only OCR evidence, or permission to process a source. Historical bounded acceptance stays historical and scope-limited. Export approval is not OCR, rendering, translation, proofreading, production, or whole-Gate authorization.

The copied NRI governance remains authoritative for main-chat ownership, critic independence, immutable receipts, and release invalidation. Older role names inside unchanged historical narrative do not override current AGENTS/role-model rules.

## Allowed administrative changes after review

The orchestrator may capture this immutable receipt and update only administrative export-goal state or publication-result bookkeeping in its owned plan/context/release and standalone-transition status. It may record verified revision/time/remote outcomes and link this receipt. No such update may change Phase 0 state, evidence/code bytes, the six-file portability scope, accepted-input meaning, or historical receipts.

These administrative operations are allowed work, **not automatic approval of a different commit**. This receipt approves `c557381c119ec03d420a0121784a5e111ebd94e8`. If receipt integration, amendment, or bookkeeping creates another pre-publication commit, preserve this receipt, produce the exact new revision and bounded diff, and obtain a successor revision/delta review. Do not silently extend this exact-commit approval across mutations. The current receipt itself is untracked at creation and was not part of the frozen candidate.

## Publish preconditions

1. Reconfirm branch, explicit reviewed SHA, clean intended worktree/index, and exact origin URL. Publish this reviewed commit, or a successor whose administrative delta has been independently reviewed.
2. Query the remote again immediately before initial publication. If any unexpected ref/branch is now advertised, stop and reconcile that evidence; do not overwrite remote history or use plain force.
3. Perform an explicit non-force initial publication to `refs/heads/main`. This review grants no destructive rewrite authority. Normal remote race/non-fast-forward failures must stop publication.
4. Verify the remote `refs/heads/main` SHA equals the actually approved published revision, and record that evidence. Preserve the NRI source checkout and its pre-existing changes. Publication status must remain pending until that check succeeds.

## Files checked and limitations

Read root and Sourcefold AGENTS, complete local NRI governance, export plan/context/release, A1/Q1 receipts, root README/attributes/ignore, all six active guidance files and their source diffs, roadmap path resolver/package metadata, representative lineage test/report/predecessor data, and the method-family/overview Tesseract binding. Inspected the entire source/candidate path inventory, every imported file's SHA-256 equality, every committed candidate blob identity, all committed blob sizes, configured remote and fresh advertised refs, and relevant source/destination Git status.

Normal sandbox Git access to this sibling checkout was denied. Read-only checks then succeeded with escalated discovered PortableGit; no access change or Git mutation was performed. No subagent was spawned, no test/evidence producer was executed, no dependencies installed, and no canonical file edited by this critic. Sole created file: this immutable review receipt. Orchestration and publication remain with the main chat.
