# Repository guidance

- Product name is `Sourcefold`; `Sorceforge` is only the repository slug.
- As of 2026-10-13 `main` holds only audit and handoff documents. The full
  Sourcefold Phase 0 code and evidence live in `https://github.com/Hramgithub/NRI`
  under `Sourcefold/` (commit `22fafc14`); kb_creator lives there under
  `kb_creator/`. The pre-cleanup snapshot of this repository is commit `72ea9be`.
- Read `README.md` and `Sourcefold/docs/audit/20261013-idea-vs-implementation.md`
  before proposing new work.

## Working with the owner

- Think in English; write every user-facing message in Russian.
- Report results only; no step-by-step reasoning in chat.
- Every finished artifact is committed and pushed to `main` immediately
  (rollback is preferred over uncommitted work). Force push and history
  rewrites only with explicit confirmation.
- Discuss decisions one question at a time with a recommended option; record
  each answer in the decision log and commit it.

## Safety

- Do not commit secrets, credentials, local runtime folders, caches, temporary
  logs, or browser profiles.
- Old evidence is reached through the NRI repository or this repository's
  history; do not recreate or rewrite it here.
