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

- Rules of writing records: `docs/conventions.md` (one source; briefs include it verbatim). The import
  pipeline and its tools: `pipeline/README.md`.
- Check every change: `python tools/check.py --changed` (schemas, references across the whole base,
  writing rules, file format); rebuild the viewer with `python tools/build_viewer.py` to look at it; the built
  `app/kb.html` is not kept in git (Р-231) — it is built again for every deploy.
- Summary of the base (records by kind, pictures, source books): `python tools/status.py [--md]`; what is
  done and what is not — `docs/handoff/20261021-kb-state.md`. Workflows for Claude — `.claude/skills/`
  (kb-import, kb-translate, kb-translate-codex, kb-rules-book, kb-terms, kb-integrate, kb-check, kb-verify, kb-art, kb-release, kb-decision, viewer-change).
- Bulk fixes in `pipeline/fix/` take an explicit scope (files, `--changed` or `--all`); changes to
  records an agent does not own go through proposals (`pipeline/integrate/README.md`).
- Numbers come from the primary source named in the decisions (Malleus Monstrorum
  over the Keeper Rulebook and the Keeper Deck); every changed value goes to
  `corrections`; book misprints are kept as printed and flagged.
- Dice as `6d6`; characteristic abbreviations as in the Russian Keeper Rulebook;
  kb JSON is UTF-8, 2-space indent, LF (`pipeline/fix/normalize_terms.py`).

## Scripts and paths

- Lead and helper scripts that are not part of `tools/` or `pipeline/` live in `.cache/lead-tools/`
  (gitignored; one subfolder per unit, e.g. `gen-<unit>`, `tr-<unit>`), not in a session scratchpad:
  scratchpads are temporary and change with every session.
- Never hardcode absolute paths in scripts, briefs or prompts. Compute them: from the script location
  (`__file__`, `$PSScriptRoot`), from the repository root, and the owner's library root from
  `pipeline/source/library.json` (`folders[].path`). Inside the repository use paths relative to its root.
  External installs (Tesseract, Poppler) are the only exception.

## Memory and parallel work

- Owner's rule (2026-11-26): system RAM never above 85 %. The lead runs `tools/memguard.ps1` in the background for
  the whole session (it stops our largest python/PDF/OCR processes above the limit, log `.cache/memguard.log`) and
  checks `pwsh -NoProfile -File tools/memguard.ps1 -Once` before launching each helper; the number of helpers is
  not fixed — a new one only while usage is below 75 % (each helper adds ~1–1.5 %; the guard keeps 85 %).
- Helpers never start many python processes at once: no parallel loops of `tools/terms.py`, `pages.py` or check
  tools (each loads the whole base, ~300 MB). Look up many terms in one run: `python -B tools/terms.py w1 w2 …` or
  `--file words.txt`.

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
