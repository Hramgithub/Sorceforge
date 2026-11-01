"""One check of the knowledge base (Р-139).

On the chosen files: the schema of the record's kind, the file format (UTF-8, 2-space indent, LF, one trailing
newline) and the writing rules of docs/conventions.md that a script can see (dice `1d6`, characteristic
abbreviations, yards). On the whole base, always: duplicate ids and references to records that do not exist.

Usage:
  python tools/check.py                 all of kb
  python tools/check.py <files|dirs>    only these files (references are still checked across the whole base)
  python tools/check.py --changed       files changed against HEAD and new ones
Exit code 1 when there are errors; warnings do not fail.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kblib import KB, ROOT, SCHEMAS, book_ids, dump, is_ref, pick, records  # noqa: E402
from validate import Validator  # noqa: E402

MEASURES = "меры — метрические: ярд = метр, фут ÷ 3, миля × 1,6 км, дюйм → см, галлон → л (Р-64)"
# writing rules a script can see (docs/conventions.md); each: (pattern, message, error or warning)
RULES = [
    (re.compile(r"\d\s*D\s*\d|\d\s*[кК]\s*(?:100|20|12|10|[2-468])(?!\d)"), "кубы пишутся строчной латинской d: 1d6 (Р-27)", True),
    (re.compile(r"(?<![А-ЯЁа-яё])(?:РАЗ|ВЕЛ)(?![А-ЯЁа-яё])"), "размер — «ТЕЛ»", True),
    (re.compile(r"(?<![А-ЯЁа-яё])ОЗ(?![А-ЯЁа-яё])"), "пункты здоровья — «ПЗ»", True),
    (re.compile(r"(?<![А-ЯЁа-яё])ЛОВ(?![А-ЯЁа-яё])"), "ловкость — «ЛВК»", True),
    (re.compile(r"d\d+\)?\s*[xхX]\s*\d"), "умножение — знак ×: (2d6+6)×5 (Р-27)", True),
    (re.compile(r"\d\s*ярд|(?<![А-ЯЁа-яё])(?:фут(?:а|ов)?|дюйм(?:а|ов)?|мил[яюиье]|миль|галлон(?:а|ов)?|унци[йяю])(?![А-ЯЁа-яё])"),
     MEASURES, True),
]
DECISION = re.compile(r"^Р-\d+$")
# where the old measures may stay (Р-64, Р-124): our remarks about the data, reasons of corrections and misprints,
# names of calibres, and a scenario's numbers quoted as printed
KEEP_MEASURES = {"notes", "note", "reason", "caliber"}
# characteristics are named by id but are not records (schemas/skill.schema.json, opposed_by)
VIRTUAL = re.compile(r"^coc:characteristic:[a-z]+$")
# fields that quote other data as it was: a correction's «from» and a misprint's «printed» keep the old writing
QUOTED = {"from", "printed"}


def strings(value, path=""):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from strings(v, f"{path}[{i}]")
    elif isinstance(value, dict):
        for k, v in value.items():
            yield from strings(v, f"{path}.{k}" if path else k)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--changed", action="store_true")
    ap.add_argument("--limit", type=int, default=20, help="problems shown per check")
    a = ap.parse_args()
    scope = set(pick(a.paths, a.changed, not a.paths and not a.changed))
    sys.stdout.reconfigure(encoding="utf-8")

    errors: dict[str, list[str]] = defaultdict(list)
    warnings: dict[str, list[str]] = defaultdict(list)
    books = book_ids()
    ids: dict[str, list[Path]] = defaultdict(list)
    kinds = Counter()
    validators: dict[str, Validator] = {}
    refs: list[tuple[Path, str, str]] = []
    rel = lambda p: p.relative_to(ROOT).as_posix()

    for p, rec in records():
        if rec is None:
            errors["JSON"].append(f"{rel(p)}: не читается как JSON")
            continue
        if not isinstance(rec, dict) or "id" not in rec:
            continue
        ids[rec["id"]].append(p)
        kinds[rec.get("kind")] += 1
        for path, s in strings(rec):
            if path not in ("id", "schema") and is_ref(s, books):
                refs.append((p, path, s))
        if p not in scope:
            continue
        kind = rec.get("kind")
        schema = SCHEMAS / f"{kind}.schema.json"
        if not schema.exists():
            errors["схема"].append(f"{rel(p)}: нет схемы для вида «{kind}»")
        else:
            v = validators.setdefault(kind, Validator(schema))
            for e in v.validate(rec):
                errors["схема"].append(f"{rel(p)}: {e}")
        if p.read_bytes() != dump(rec).encode("utf-8"):
            errors["формат файла"].append(f"{rel(p)}: не UTF-8 / отступ 2 / LF / перевод строки в конце — `python pipeline/fix/normalize_terms.py {rel(p)}`")
        for i, c in enumerate(rec.get("corrections") or []):
            if isinstance(c, dict) and c.get("ref") is not None and not DECISION.match(str(c["ref"])):
                errors["в corrections.ref — только номер решения «Р-NN» или null; книга и страница — в reason (Р-140)"].append(f"{rel(p)}: corrections[{i}].ref = {c['ref']!r}")
        q = rec.get("quality") or {}
        if bool(rec.get("errata")) != ("parse_uncertain" in (q.get("flags") or [])):
            errors["флаг «опечатка книги» (parse_uncertain) стоит ровно у записей с errata (Р-141): `python pipeline/fix/errata_flag.py <файл>`"].append(
                f"{rel(p)}: errata {len(rec.get('errata') or [])}, флаг {'есть' if 'parse_uncertain' in (q.get('flags') or []) else 'нет'}")
        for path, s in strings(rec):
            if path.rsplit(".", 1)[-1] in QUOTED:
                continue
            for pat, msg, is_error in RULES:
                if msg == MEASURES and (re.split(r"[.\[]", path)[-1].rstrip("]") in KEEP_MEASURES or "source_variants" in path):
                    continue
                m = pat.search(s)
                if m:
                    (errors if is_error else warnings)[msg].append(f"{rel(p)}: {path}: «…{s[max(0, m.start() - 15):m.end() + 15]}…»")

    for i, ps in ids.items():
        if len(ps) > 1:
            errors["повтор id"].append(f"{i}: {', '.join(rel(p) for p in ps)}")
    for p, path, r in refs:
        if r not in ids and not VIRTUAL.match(r):
            errors["ссылка на несуществующую запись"].append(f"{rel(p)}: {path} → {r}")

    print(f"Записей: {sum(kinds.values())} ({', '.join(f'{k} {n}' for k, n in sorted(kinds.items(), key=lambda x: str(x[0])))}); "
          f"проверено файлов: {len(scope)}; ссылок: {len(refs)}")
    for title, box in (("Ошибки", errors), ("Предупреждения", warnings)):
        for check, items in box.items():
            print(f"\n{title} — {check}: {len(items)}")
            for x in items[:a.limit]:
                print("  " + x)
            if len(items) > a.limit:
                print(f"  … и ещё {len(items) - a.limit}")
    n = sum(map(len, errors.values()))
    print(f"\nИтог: ошибок {n}, предупреждений {sum(map(len, warnings.values()))}")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
