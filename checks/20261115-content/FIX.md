# Исправления по сверке контента — задание помощникам

Read `docs/conventions.md` fully first. Your part's list is the row of `checks/20261115-content/summary.md` with your
unit name; the details (pages, exact values) are in the unit reports of this folder (named in your prompt).

Rules:
- Numbers and facts from the book page (`python -B pipeline/source/pages.py show|image <book> <page>`); Malleus Monstrorum
  is the primary source for creatures (Р-22), the Russian Keeper Rulebook for rules, the fan translation for Dark Ages.
- Edit records directly only inside your scope (prompt). Every changed value goes to `corrections` (`field`, `from`, `to`,
  `reason`, `ref` — the decision you follow, e.g. «Р-22», «Р-242»; «Р-247» for this fix pass if nothing else fits).
  Book misprints stay as printed and go to `errata` (+ flag, `python -B pipeline/fix/errata_flag.py <file>`).
- New records follow existing models of the same kind and book; Grep first that the thing is not there under another name.
- Records outside your scope: write proposals (`pipeline/integrate/README.md`) to `checks/20261115-content/proposals-<unit>.json`.
- Pictures: workflow `checks/20261114-art/README.md` (unit name = yours): mapping → `add_images.py` (dry-run, then real);
  do not apply the art proposals — the lead applies them. Maps: `map` records as in `.claude/skills/kb-art/SKILL.md` and
  existing map records (image from the page render, spots on every printed label, Р-120/Р-206).
- Russian text: official forms of names (glossary `python -B tools/terms.py <word>`, existing records); our translation
  of English text gets the flag `translated`.
- Run `python -B tools/check.py <your changed files>` → 0 errors. Write `checks/20261115-content/fix-<unit>.md` (Russian):
  each item of your row → done (files) / not done (why). Do not commit — the lead commits. Do the work yourself
  (no sub-agents); scripts in scratchpad\fix-<unit>\. If resumed after a network error, continue where you stopped.
