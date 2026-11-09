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
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kblib import KB, ROOT, SCHEMAS, book_ids, dump, is_ref, pick, records  # noqa: E402
from derived import mismatches  # noqa: E402
from validate import Validator  # noqa: E402

ATTR_WORDS = "Рассудок и Скорость — словами, «РАС», «СКО», «SAN», «MOV» — только в raw как напечатано (Р-146)"
MEASURES = "меры — метрические: ярд = метр, фут ÷ 3, миля × 1,6 км, дюйм → см, галлон → л (Р-64)"
# writing rules a script can see (docs/conventions.md); each: (pattern, message, error or warning)
RULES = [
    (re.compile(r"\d\s*D\s*\d|\d\s*[кК]\s*(?:100|20|12|10|[2-468])(?!\d)"), "кубы пишутся строчной латинской d: 1d6 (Р-27)", True),
    (re.compile(r"(?<![А-ЯЁа-яё])(?:РАЗ|ВЕЛ)(?![А-ЯЁа-яё])"), "размер — «ТЕЛ»", True),
    (re.compile(r"(?<![А-ЯЁа-яё])ОЗ(?![А-ЯЁа-яё])"), "пункты здоровья — «ПЗ»", True),
    (re.compile(r"(?<![А-ЯЁа-яё])ЛОВ(?![А-ЯЁа-яё])"), "ловкость — «ЛВК»", True),
    (re.compile(r"(?<![А-ЯЁа-яё])(?:РАС|СКО)(?![А-ЯЁа-яё])|\b(?:SAN|MOV)\b"), ATTR_WORDS, True),
    (re.compile(r"(?m)^[ \t]*[*\-–][ \t]"), "разметки списков в данных нет: перечисление — через «;», напечатанный по пунктам список — абзацами с «•» (Р-152)", True),
    (re.compile(r"d\d+\)?\s*[xхX]\s*\d"), "умножение — знак ×: (2d6+6)×5 (Р-27)", True),
    (re.compile(r"(?<![А-ЯЁа-яё])(?:фут(?:а|ов|ах|ам|ами|е|ом|ы)?|дюйм(?:а|ов|ах|ам|ы)?|мил(?:я|и|ю|е|ь|ях|ям|ями|ей)|"
                r"ярд(?:а|ов|ах|ам|ы)?|галлон(?:а|ов|ах|ы)?|унци(?:я|и|й|ю|ях))(?![А-ЯЁа-яё])"),
     MEASURES, True),
]
DECISION = re.compile(r"^Р-\d+$")
# where the old measures may stay (Р-64, Р-124, Р-142): our remarks about the data, reasons of corrections and misprints,
# names of calibres, and a scenario's numbers quoted as printed
KEEP_MEASURES = re.compile(r"^(quality\.notes|errata\[\d+\]\.(note|expected)|corrections\[\d+\]\.reason|caliber|source_variants\[\d+\]\..*)$")
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
    registry = set(json.loads((ROOT / "pipeline/source/books.json").read_text(encoding="utf-8")))
    ids: dict[str, list[Path]] = defaultdict(list)
    kinds = Counter()
    validators: dict[str, Validator] = {}
    refs: list[tuple[Path, str, str]] = []
    rel = lambda p: p.relative_to(ROOT).as_posix()
    checked = 0

    for p, rec in records():
        if rec is None:
            errors["JSON"].append(f"{rel(p)}: не читается как JSON")
            continue
        if not isinstance(rec, dict) or "id" not in rec:
            if p in scope:
                errors["запись без id"].append(f"{rel(p)}: не объект JSON или нет поля id")
            continue
        if p in scope:
            checked += 1
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
        nm = rec.get("name") if isinstance(rec.get("name"), dict) else {}
        for a in rec.get("aliases") or []:
            if a in (nm.get("ru"), nm.get("en")):
                errors["в «также» (aliases) — своё же название: оно уже в name"].append(f"{rel(p)}: {a}")
        if rec.get("kind") == "location" and not rec.get("part_of") and rec.get("location_type") not in ("город", "корабль", "город сценария"):
            errors["место без part_of бывает только у города, корабля и города сценария (Р-189, Р-197): иначе его нет в дереве гайда (Р-163)"].append(f"{rel(p)}: {rec.get('location_type')}")
        if rec.get("kind") == "location" and rec.get("location_type") == "здание":
            for al in rec.get("aliases") or []:
                if re.match(r"(Семья|Семейство)\b", al):
                    errors["у здания в псевдонимах нет имён людей: «Семья …» (Р-82)"].append(f"{rel(p)}: aliases: {al}")
        for i, ab in enumerate(rec.get("abilities") or []):
            if isinstance(ab, dict) and not re.search(r"[А-ЯЁа-яё]", ab.get("summary") or ""):
                errors["у способности русский текст в summary; raw — как напечатано (Р-33, Р-144)"].append(f"{rel(p)}: abilities[{i}] «{ab.get('name')}»")
        for path, s in strings(rec):
            if path.rsplit(".", 1)[-1] == "book_id" and s not in registry:
                errors["книга не записана в pipeline/source/books.json (Р-148)"].append(f"{rel(p)}: {path} = {s}")
        if rec.get("kind") == "character":
            for f, pr, ex in mismatches(rec):
                warnings["производное значение не по правилам 7-й редакции и не в errata (Р-35, Р-36, Р-161)"].append(f"{rel(p)}: {f}: напечатано {pr}, по правилам {ex}")
        q = rec.get("quality") or {}
        if bool(rec.get("errata")) != ("parse_uncertain" in (q.get("flags") or [])):
            errors["флаг «опечатка книги» (parse_uncertain) стоит ровно у записей с errata (Р-141): `python pipeline/fix/errata_flag.py <файл>`"].append(
                f"{rel(p)}: errata {len(rec.get('errata') or [])}, флаг {'есть' if 'parse_uncertain' in (q.get('flags') or []) else 'нет'}")
        for path, s in strings(rec):
            # a glossary entry quotes words as they are used and as they must not be (Р-184): no writing rules for it
            if rec.get("kind") == "term" or path.rsplit(".", 1)[-1] in QUOTED:
                continue
            for pat, msg, is_error in RULES:
                # the English text of a record (name.en and the like) keeps the book's English words: «MOV Rates»
                if msg == ATTR_WORDS and (re.split(r"[.\[]", path)[-1].rstrip("]") in {"raw", "to", "reason", "en"} or "source_variants" in path or path.startswith("corrections")):
                    continue
                if msg == MEASURES and KEEP_MEASURES.match(path):
                    continue
                m = pat.search(s)
                if m:
                    (errors if is_error else warnings)[msg].append(f"{rel(p)}: {path}: «…{s[max(0, m.start() - 15):m.end() + 15]}…»")

    for i, ps in ids.items():
        if len(ps) > 1:
            errors["повтор id"].append(f"{i}: {', '.join(rel(p) for p in ps)}")
    for p, path, r in refs:
        # a correction's «from» quotes the old value: the old id of a record that moved to a shared one (Р-154)
        if re.match(r"^corrections\[\d+\]\.from$", path):
            continue
        if r not in ids and not VIRTUAL.match(r):
            errors["ссылка на несуществующую запись"].append(f"{rel(p)}: {path} → {r}")

    print(f"Записей: {sum(kinds.values())} ({', '.join(f'{k} {n}' for k, n in sorted(kinds.items(), key=lambda x: str(x[0])))}); "
          f"проверено записей: {checked}; ссылок: {len(refs)}")
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
