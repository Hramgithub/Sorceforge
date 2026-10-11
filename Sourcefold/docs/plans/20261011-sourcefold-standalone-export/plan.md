# Goal plan: Sourcefold standalone export

- Goal ID: `20261011-sourcefold-standalone-export`
- State: `active`
- Objective: publish a clean, portable Sourcefold snapshot from NRI to
  `https://github.com/Hramgithub/Sorceforge.git` without mutating the source
  checkout or importing unrelated NRI state.
- Policy orchestrator: main chat, `gpt-6-sol` / medium.
- Actual orchestrator model/effort: unavailable.
- Scoped override: none.

## Ownership

| Step | Owner | Requested effort | State |
|---|---|---:|---|
| A1 topology, dependency, and portability review | `gpt-6-astra` architect | high | completed |
| I1 materialize exact tracked Sourcefold snapshot | main-chat orchestrator | medium | completed |
| I2 integrate minimal standalone portability changes | main-chat orchestrator | medium | completed |
| V1 roadmap, tests, blob identity, and secret checks | main-chat orchestrator | medium | completed with inherited gaps documented |
| Q1 bounded import QA | `gpt-6-luna` QA | medium | completed: PASS |
| R1 independent release review | `gpt-6-astra` critic | high | completed: APPROVED for `c557381c119ec03d420a0121784a5e111ebd94e8` |
| P1 commit and publish `main` | main-chat orchestrator | medium | active |

The critic must not implement or materially design the candidate.

## Source boundary

- Source repository: `C:\_Hobby\_work\NRI`.
- Source subtree: `Sourcefold/` at the current NRI `HEAD`.
- Initial measured boundary: 3974 tracked paths and no untracked Sourcefold
  paths.
- Original NRI files and its existing `.codex/config.toml` and
  `CODEX_CONFIG_APPLIED.md` changes are protected and must remain untouched.
- Only project-local portability additions explicitly recorded in this goal may
  be added beyond the tracked Sourcefold snapshot.

## Decisions to close before import

1. Preserve the nested `Sourcefold/` topology or flatten it without breaking
   canonical `Sourcefold/...` paths and the roadmap validator.
2. Classify the 3408 tracked fixture/evidence paths as durable governed
   evidence or removable generated state based on project contracts, not size.
3. Identify NRI-external governance, tool, source, and absolute-path
   dependencies that require a local copy, path change, or explicit gap note.
4. Keep the product name `Sourcefold`; treat `Sorceforge` as the repository
   slug supplied by the user, not a product rename.

## Planned verification

- source-to-destination tracked path and blob/hash comparison;
- no ignored runtime, temp, credentials, browser profiles, or unrelated NRI
  payloads;
- no ordinary Git blob above GitHub's 100 MiB hard limit;
- roadmap validation from the documented Sourcefold working directory;
- focused and broad Python test discovery using a discovered runtime;
- link/path and machine-specific dependency audit;
- clean Git state and exact remote identity after publication.

## Closed architecture decisions

- Preserve the nested `Sourcefold/` topology; the roadmap validator resolves
  canonical `Sourcefold/...` paths from the repository root.
- Retain all 3974 tracked source paths, including all 3408 governed fixture and
  evidence paths. No tracked failed-attempt or overlay-named evidence is
  classified as disposable solely from its name.
- Copy the shared governance and OCR layout policies into the repository root.
  Update only active guidance; preserve historical receipts and run evidence
  byte-for-byte.
- Record hard-coded `D:\NRI` OCR runtime paths as a portability gap. Do not
  bulk-rewrite scripts or immutable evidence during the extraction.

## Definition of Done

- the chosen topology is justified and internally consistent;
- all included source paths match NRI bytes unless a reviewed portability edit
  explicitly supersedes them;
- exclusions are enumerated and no durable governed evidence is silently
  discarded as trash;
- standalone limitations and historical absolute paths are documented;
- QA passes and the independent critic approves the exact candidate;
- `main` is published to the user-provided remote and verified clean;
- the NRI source checkout retains only its pre-existing user changes.
