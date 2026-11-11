"""Build the glossary kb/terms/ (Р-184) from the owner's terminology registry and the names of the base's records.

Priority of the Russian term: an official localization (a record whose source is an official Russian edition) >
the owner's registry (CoC_Terminology_Decisions.csv) > a trusted fan translation > our own translation. Every
known translation stays in `variants` with where it comes from; a disagreement between the official name and the
owner's registry is listed in the report for the owner.

Usage: python -I pipeline/migrate/terms_build.py <registry.csv> [--dry-run]
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import KB, ROOT, records  # noqa: E402

REGISTRY_BOOK = "coc-terminology"
CHARACTERISTICS = [  # the Russian Keeper Rulebook, p. 26-31 (official)
    ("Strength", "Сила", "СИЛ", "str"), ("Constitution", "Выносливость", "ВЫН", "con"), ("Size", "Телосложение", "ТЕЛ", "siz"),
    ("Dexterity", "Ловкость", "ЛВК", "dex"), ("Appearance", "Наружность", "НАР", "app"), ("Intelligence", "Интеллект", "ИНТ", "int"),
    ("Power", "Мощь", "МОЩ", "pow"), ("Education", "Образование", "ОБР", "edu"), ("Luck", "Удача", None, "luck"),
    ("Sanity", "Рассудок", "РАС", "san"), ("Hit Points", "пункты здоровья", "ПЗ", None), ("Magic Points", "пункты магии", "ПМ", None),
    ("Damage Bonus", "бонус к урону", "БкУ", None), ("Build", "Комплекция", None, None), ("Movement Rate", "Скорость", None, None),
]


# names Windows keeps for devices cannot be file names (con.json is the console)
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(10)), *(f"lpt{i}" for i in range(10))}


TR = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", ["a","b","v","g","d","e","e","zh","z","i","y","k","l","m","n","o","p","r","s","t","u","f","kh","ts","ch","sh","shch","","y","","e","yu","ya"]))


def translit(ru: str) -> str:
    return "".join(TR.get(c, c) for c in ru.lower())


def slug(en: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", en.lower().replace("’", "").replace("'", "")).strip("-")
    return s + "-term" if s in RESERVED else s


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("registry", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    books = json.loads((ROOT / "pipeline/source/books.json").read_text(encoding="utf-8"))
    official = {b for b, v in books.items() if v.get("edition") == "official" and v.get("lang") == "ru"}
    terms: dict[str, dict] = {}

    def term(en: str) -> dict:
        k = en.strip().lower()
        if k not in terms:
            terms[k] = {"en": en.strip(), "variants": [], "aliases": [], "avoid": [], "refs": [], "domain": None, "scope": None,
                        "status": "review", "definition": None, "sources": [], "notes": []}
        return terms[k]

    # 1. the owner's registry
    for r in csv.DictReader(a.registry.open(encoding="utf-8")):
        t = term(r["source_term"])
        scope = r["source_scope"] if r["source_scope"] not in ("KeeperBook glossary", "CoC 7e character skills") else None
        t["variants"].append({"ru": r["accepted_ru"].strip(), "by": "owner", "book_id": REGISTRY_BOOK, "page": None,
                              "note": f"{r['decision_rule']}; {r['status']}"})
        t["aliases"] += [x.strip() for x in r["aliases"].split(";") if x.strip()]
        t["avoid"] += [x.strip() for x in r["bad_ru"].split(";") if x.strip()]
        t["domain"] = t["domain"] or r["domain"] or None
        t["scope"] = scope
        if r["status"] == "accepted":
            t["status"] = "accepted"
        m = re.search(r"Определение:\s*(.+?)(?:\s+Источник:|$)", r["notes"])
        if m and not t["definition"]:
            t["definition"] = m.group(1).strip()
        t["sources"].append({"book_id": REGISTRY_BOOK, "physical_page": None, "printed_page": None, "method": "manual", "verified": False,
                             "note": f"CoC_Terminology_Decisions.csv: {r['source_term']}"})

    # 1b. the glossary of the Russian Keeper Rulebook (official terms and definitions), if transcribed
    gl = ROOT / "checks/20261108-terms/kr-glossary.json"
    if gl.exists():
        for g in json.loads(gl.read_text(encoding="utf-8")):
            # a Russian entry without an English one (МКН, «Трудный успех») is keyed by its Russian name
            if g.get("en"):
                t = term(g["en"])
            else:
                # a Russian entry without an English one joins the term that already has this Russian name
                t = next((x for x in terms.values() if any(v["ru"].lower() == g["ru"].lower() for v in x["variants"])), None) or term(g["ru"])
                if t["en"] and t["en"].lower() == g["ru"].lower():
                    t["en"] = None
            t["variants"].append({"ru": g["ru"], "by": "official", "book_id": "keeper-rulebook-ru", "page": g.get("page"), "note": "глоссарий «Книги хранителя»"})
            t["definition"] = g.get("definition") or t["definition"]
            t["domain"] = t["domain"] or "glossary"
            t["sources"].append({"book_id": "keeper-rulebook-ru", "physical_page": g.get("physical_page"), "printed_page": g.get("page"),
                                 "method": "book_text", "verified": True, "note": "глоссарий"})

    # 1c. terms chosen while translating an English book (checks/*/new-terms.json: {en, ru, aliases, avoid, domain, ref, note});
    #     our translation — page and book come from the record in `ref`
    by_id = {r.get("id"): r for _, r in records()}
    for nt in sorted(ROOT.glob("checks/*/new-terms.json")):
        for g in json.loads(nt.read_text(encoding="utf-8")):
            t = term(g["en"])
            src = ((by_id.get(g.get("ref")) or {}).get("sources") or [{}])[0]
            t["variants"].append({"ru": g["ru"], "by": "ours", "book_id": src.get("book_id"), "page": src.get("printed_page"),
                                  "note": g.get("note") or f"выбрано при переносе ({nt.parent.name})"})
            t["aliases"] += g.get("aliases") or []
            t["avoid"] += g.get("avoid") or []
            t["domain"] = t["domain"] or g.get("domain")
            if g.get("ref"):
                t["refs"].append(g["ref"])
            if src.get("book_id"):
                t["sources"].append({"book_id": src["book_id"], "physical_page": src.get("physical_page"), "printed_page": src.get("printed_page"),
                                     "method": "book_text", "verified": bool(src.get("verified")), "note": f"{nt.parent.name}/new-terms.json"})

    # 2. official characteristics
    for en, ru, abbr, cid in CHARACTERISTICS:
        t = term(en)
        t["variants"].append({"ru": ru, "by": "official", "book_id": "keeper-rulebook-ru", "page": None, "note": "характеристики, гл. 3"})
        if abbr:
            t["aliases"].append(abbr)
        t["domain"] = t["domain"] or "characteristic"
        if cid:
            t["refs"].append(f"coc:characteristic:{cid}")
        t["sources"].append({"book_id": "keeper-rulebook-ru", "physical_page": None, "printed_page": 26, "method": "book_text", "verified": True,
                             "note": "характеристики и производные значения, с. 26–31"})

    # 3. names of records: skills and occupations (official when a source is an official Russian edition);
    #    Pulp archetypes and talents — our translation
    # a translated name that is word for word the name of an official record of the same kind (a pulp occupation
    # «Антиквар» = the Investigator Handbook's «Антиквар») is the official term
    recs = [r for _, r in records()]
    official_names = defaultdict(dict)
    for r in recs:
        if any(s.get("book_id") in official for s in r.get("sources") or []) and (r.get("name") or {}).get("ru"):
            official_names[r.get("kind")][r["name"]["ru"].lower()] = r
    for rec in recs:
        kind, name = rec.get("kind"), rec.get("name") or {}
        if kind not in ("skill", "occupation", "archetype", "talent") or not name.get("en") or not name.get("ru"):
            continue
        srcs = rec.get("sources") or []
        off = next((s for s in srcs if s.get("book_id") in official), None)
        by = "official" if off and "translated" not in ((rec.get("quality") or {}).get("flags") or []) else "ours"
        twin = official_names[kind].get(name["ru"].lower())
        if by == "ours" and twin:
            by, off = "official", next(s for s in twin["sources"] if s.get("book_id") in official)
        t = term(name["en"])
        t["variants"].append({"ru": name["ru"], "by": by, "book_id": (off or (srcs[0] if srcs else {})).get("book_id"),
                              "page": (off or (srcs[0] if srcs else {})).get("printed_page"), "note": f"имя записи {rec['id']}"})
        t["refs"].append(rec["id"])
        t["domain"] = t["domain"] or {"skill": "skill", "occupation": "occupation", "archetype": "pulp archetype", "talent": "pulp talent"}[kind]
        if not t["sources"] or all(s["book_id"] == REGISTRY_BOOK for s in t["sources"]):
            s0 = off or (srcs[0] if srcs else None)
            if s0:
                t["sources"].append({"book_id": s0["book_id"], "physical_page": s0.get("physical_page"), "printed_page": s0.get("printed_page"),
                                     "method": "book_text", "verified": bool(s0.get("verified")), "note": f"имя записи {rec['id']}"})

    # choose by priority, write
    rank = {"official": 0, "owner": 1, "trusted": 2, "ours": 3}
    out, conflicts, used = [], [], set()
    for k, t in sorted(terms.items()):
        t["en"] = t["en"] if t["en"] is not None else None
        seen, vs = set(), []
        for v in sorted(t["variants"], key=lambda v: rank.get(v["by"], 9)):
            key = (v["ru"].lower(), v["by"])
            if key not in seen:
                seen.add(key); vs.append(v)
        best = vs[0]
        # the glossary inverts headwords for the alphabet («Удачи проверка»): the same words in the order of the
        # owner's registry are the term itself, still official
        natural = next((v for v in vs if v["by"] == "owner" and sorted(v["ru"].lower().split()) == sorted(best["ru"].lower().split())
                        and v["ru"].lower() != best["ru"].lower()), None)
        if best["by"] == "official" and natural:
            best = {**best, "ru": natural["ru"], "note": (best.get("note") or "") + "; в глоссарии — «" + vs[0]["ru"] + "» (порядок слов для алфавита)"}
        others = {v["ru"].lower() for v in vs if v["by"] != best["by"]} - {best["ru"].lower()}
        if best["by"] == "official" and any(v["by"] == "owner" and v["ru"].lower() != best["ru"].lower() for v in vs):
            conflicts.append((t["en"], best["ru"], [v["ru"] for v in vs if v["by"] == "owner"]))
        s = slug(t["en"] or translit(k)) or "term"
        while s in used:
            s += "-2"
        used.add(s)
        rec = {"schema": "sourcefold.term.v0", "id": f"coc:term:{s}", "kind": "term", "name": {"ru": best["ru"], "en": t["en"]},
               "aliases": sorted(set(t["aliases"]) - {best["ru"]}), "avoid": sorted(set(t["avoid"])), "domain": t["domain"], "scope": t["scope"],
               "status": "accepted" if best["by"] == "official" or t["status"] == "accepted" else "review",
               "chosen_by": best["by"], "variants": vs,
               "definition": {"ru": t["definition"], "en": None} if t["definition"] else None,
               "refs": sorted(set(t["refs"])), "sources": t["sources"] or [{"book_id": REGISTRY_BOOK, "physical_page": None, "printed_page": None,
                                                                             "method": "manual", "verified": False, "note": None}],
               "quality": {"needs_review": False, "flags": [], "notes": ("Другие переводы: " + "; ".join(sorted(others))) if others else None}}
        if rec["definition"] is None:
            del rec["definition"]
        out.append(rec)
    print(f"терминов: {len(out)}; принято: {sum(r['status'] == 'accepted' for r in out)}; "
          f"по источнику: { {b: sum(r['chosen_by'] == b for r in out) for b in rank} }; расхождений официального с реестром: {len(conflicts)}")
    for en, ru, owner in conflicts[:40]:
        print(f"  {en}: официально «{ru}», в реестре {owner}")
    if not a.dry_run:
        d = KB / "terms"
        d.mkdir(exist_ok=True)
        for r in out:
            (d / (r["id"].split(":")[-1] + ".json")).write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        rep = ROOT / "checks/20261108-terms/conflicts.md"
        rep.parent.mkdir(parents=True, exist_ok=True)
        rep.write_text("# Расхождения официальных названий с реестром терминов владельца\n\n| Термин | Официально (принято) | В реестре владельца |\n|---|---|---|\n"
                       + "".join(f"| {en} | {ru} | {'; '.join(o)} |\n" for en, ru, o in conflicts), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
