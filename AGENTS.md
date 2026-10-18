# Repository guidance

- Product name is `Sourcefold`; `Sorceforge` is only the repository slug.
- `main` holds the Call of Cthulhu 7e knowledge base (since 2026-10-17): JSON data
  in `kb/`, schemas in `schemas/`, viewer in `app/`, tools in `tools/` and
  `pipeline/`, book checks in `checks/`. The old Sourcefold Phase 0 code and
  evidence live in `https://github.com/Hramgithub/NRI` under `Sourcefold/`
  (commit `22fafc14`); kb_creator lives there under `kb_creator/`. The
  pre-cleanup snapshot of this repository is commit `72ea9be`.
- Read `README.md` and `docs/project-goal.md` (§6 decisions, §8 status) before
  proposing new work.

## Data rules

- Validate every changed record: `python tools/validate.py schemas/<kind>.schema.json <files>`;
  rebuild the viewer with `python tools/build_viewer.py` and commit `app/kb.html` with the data.
- Numbers come from the primary source named in the decisions (Malleus Monstrorum
  over the Keeper Rulebook and the Keeper Deck); every changed value goes to
  `corrections`; book misprints are kept as printed and flagged.
- Dice as `6d6`; characteristic abbreviations as in the Russian Keeper Rulebook;
  kb JSON is UTF-8, 2-space indent, LF (`pipeline/fix/normalize_terms.py`).

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
