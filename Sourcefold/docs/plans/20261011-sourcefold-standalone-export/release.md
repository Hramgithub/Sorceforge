# Release candidate: Sourcefold standalone export

- Goal ID: `20261011-sourcefold-standalone-export`
- Candidate state: published. Initial candidate
  `c557381c119ec03d420a0121784a5e111ebd94e8` and administrative successor
  `161aec0a474ad5160a6a44a063e662f8ea182bad` were independently approved.
  Remote `refs/heads/main` was verified at the successor SHA.
- Source: NRI `22fafc14942e925b2e5f088f3c7ab1cd8efe3003`
- Destination remote: `https://github.com/Hramgithub/Sorceforge.git`
- Product topology: `Sourcefold/` nested under repository root

## Candidate scope

- 3974 tracked source paths retained from NRI.
- 3968 source paths are byte-identical to the source working tree.
- Six active guidance paths are intentionally edited for standalone use:
  `AGENTS.md`, `README.md`, `SETUP.md`, `PROJECT_STATUS.md`,
  `docs/architecture/role_model.md`, and `docs/plans/README.md` under
  `Sourcefold/`.
- New repository-root guidance, ignore/attribute policy, shared governance and
  OCR layout policy copies, and this goal packet are added.
- Governed fixtures and run evidence are retained. Unrelated NRI projects,
  local dependencies, caches, credentials, browser profiles, and temporary
  files are excluded.

## Verification

- Roadmap: passed (`6` statuses, `7` lanes, `26` nodes, `25` edges, `254`
  documentation checkpoints).
- Focused Python suite: `37 passed, 1 skipped`.
- Full Python collection: `1029` tests.
  - `989 passed`, `27 skipped`.
  - `12` evidence-lineage SHA assertions fail identically in the NRI source and
    are therefore inherited project debt, not import drift.
  - `1` test requires the historical machine-specific Tesseract executable at
    `D:\NRI\.tools\tesseract\tesseract.exe`; OCR runtime portability remains a
    documented gap and no OCR execution is authorized by this import.
- Secret-pattern scan: no matches.
- Files at or above GitHub's 100 MiB hard limit: none.
- Runtime/temp candidates inside the import surface: none.
- Viral PDF SHA-256:
  `0A80B6F389821B87553D26746D2BE171B4482BA9BBC6E3EB3FEC26274EDBED05`.

## Release constraints

- This extraction does not advance Sourcefold beyond Phase 0.
- It does not establish whole-book, production-ready, source-acceptance, OCR,
  translation, or proofreading authorization.
- Historical evidence and machine-specific provenance remain immutable.
- Publication awaits bounded QA and an independent `gpt-6-astra` release
  decision over the exact candidate.

## Independent release decision

R1 **APPROVED** exact candidate
`c557381c119ec03d420a0121784a5e111ebd94e8`. The immutable decision is recorded
in `handoffs/R1-release-review.md`. It permits a normal non-force initial push
after a fresh empty-remote check. The receipt-integration commit must receive a
bounded delta review before it becomes the publication target.

The successor delta review subsequently **APPROVED**
`161aec0a474ad5160a6a44a063e662f8ea182bad`; see
`handoffs/R1-successor-delta-review.md`. A normal non-force push created remote
`main`, and `git ls-remote --heads origin` verified that SHA at
`2026-10-11T23:24:00+03:00`.
