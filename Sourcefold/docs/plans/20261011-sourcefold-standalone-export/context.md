# Context: Sourcefold standalone export

- Goal ID: `20261011-sourcefold-standalone-export`
- State: `completed`
- Destination: `C:\_Hobby\_work\Sorceforge`
- Remote: `https://github.com/Hramgithub/Sorceforge.git`
- Remote state at preflight: empty (`git ls-remote` returned no refs)
- Source NRI branch: `main`

## Current evidence

- `Sourcefold/` contains 3974 tracked paths and no untracked paths.
- Approximate tracked payload size is 658,489,435 bytes.
- Largest file is the governed Viral candidate PDF at 20,718,150 bytes; no
  tracked file exceeds 50 MiB.
- 3408 tracked paths are under `fixtures/`; project guidance describes
  candidate inputs and bounded run evidence as durable unless separately
  classified or superseded.
- The roadmap validator explicitly resolves canonical paths beginning with
  `Sourcefold/` relative to the parent repository root.
- Several scripts and historical evidence records contain `D:\NRI` and
  `.tools` paths; these require classification rather than silent rewriting.
- Sourcefold currently references NRI governance outside its subtree and has a
  stale local model-role matrix relative to current root governance.

## Current step

Completed: `main` was published without force and the remote revision was
verified. No project acceptance state changed.

## Completed evidence

- A1 architecture receipt: `handoffs/A1-architecture-review.md`.
- I1 materialized the exact tracked `Sourcefold/` snapshot from NRI commit
  `22fafc14942e925b2e5f088f3c7ab1cd8efe3003` with Git archive semantics.
- The destination uses `core.longpaths=true`; the empty remote is configured as
  `origin` and no remote mutation has occurred.
- Root copies of NRI goal governance and OCR layout rules match their source
  SHA-256 values.
- All 3968 non-allowlisted source paths are byte-identical to the NRI working
  tree; no source path is missing. Six active guidance files are the explicit
  portability-edit allowlist.
- `npm ci` completed with zero reported vulnerabilities and roadmap validation
  passed: 6 statuses, 7 lanes, 26 nodes, 25 edges, and 254 checkpoints.
- Focused Python validation passed: 37 passed, 1 skipped.
- Full collection found 1029 tests. The standalone result is 989 passed, 27
  skipped, and 13 failed: 12 stale evidence-lineage hashes reproduce unchanged
  in the NRI source, while one test requires the documented historical
  `D:\NRI\.tools\tesseract\tesseract.exe` path. No evidence was regenerated or
  rewritten during extraction.
- Secret-pattern scan returned no matches. No file is at or above 100 MiB and
  no runtime/temp candidate was found in the import surface.
- Viral PDF SHA-256:
  `0A80B6F389821B87553D26746D2BE171B4482BA9BBC6E3EB3FEC26274EDBED05`.
- Q1 bounded QA passed and recorded its immutable receipt at
  `handoffs/Q1-import-qa.md`.
- R1 independently approved candidate commit
  `c557381c119ec03d420a0121784a5e111ebd94e8`; receipt:
  `handoffs/R1-release-review.md`. The receipt itself and owned goal-state
  bookkeeping require a bounded successor-delta review before publication.

## Remote mutation

- `refs/heads/main` was created by a normal non-force push at
  `161aec0a474ad5160a6a44a063e662f8ea182bad`.
- `git ls-remote --heads origin` verified the same SHA at
  `2026-10-11T23:24:00+03:00`.
- Local `main` tracks `origin/main`.
- Source NRI remained on its original branch and retained only the two
  pre-existing user modifications outside `Sourcefold/`.
