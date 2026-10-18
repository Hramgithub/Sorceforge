"""Migrate the 56 Keeper Rulebook creatures from the web helper into kb/creatures.

Input: git_coc/web_helper_coc_gm/public/docs/monsters/data/monsters/*.json
(records whose source_set starts with "keeper_rulebook").
Output: kb/creatures/<slug>.json in schema sourcefold.creature.v0.

Rules:
- every parsed number keeps the helper's original text in `raw`;
- what does not fit a known pattern is not guessed: the record gets
  quality.flags = ["parse_uncertain"] and a note with the unparsed fragment;
- text that looks cut off in the helper gets the flag "incomplete";
- hand-checked records in schemas/examples/creature/ replace the migrated ones;
- corrections from checks/20261017-rules-core/report.md are applied and logged.

Usage: python pipeline/migrate/helper_creatures.py --helper <monsters dir>
       --examples schemas/examples/creature --out kb/creatures
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

CHAR = {"СИЛ": "STR", "ВЫН": "CON", "ТЕЛ": "SIZ", "ЛВК": "DEX", "НАР": "APP", "ИНТ": "INT", "МОЩ": "POW", "ОБР": "EDU"}
CHAPTER14_OFFSET = 21  # printed page - physical page in chapter 14 (checked on 3 creatures)
MOVE_MODES = {"полёт": "fly", "плавание": "swim", "рытьё": "burrow", "ходьба": "walk"}
STOP_HEADS = ("Уклонение", "Броня:", "Навыки:", "Обитает:", "Потеря рассудка:")
ATTACK = re.compile(r"^(?P<name>[^%]*?)\s*(?P<pct>\d+)%\s*\((?P<h>\d+)\s*/\s*(?P<f>\d+)\)\s*,?\s*(?P<rest>.*)$")
DICE = re.compile(r"\d+\s*[кd]\s*\d+(?:\s*[+−-]\s*\d+(?!\s*[кd/\d]))?")  # "1к6 + 1/2 БкУ" -> "1к6"
SAN = re.compile(r"(\d+(?:\s*[кd]\s*\d+)?)\s*/\s*(\d+\s*[кd]\s*\d+(?:\s*\+\s*\d+)?|\d+)")
ROLL = re.compile(r"\b(СИЛ|ВЫН|ТЕЛ|ЛВК|НАР|ИНТ|МОЩ|ОБР)\s+(\d+)\s+(\(?\d+\s*[кd]\s*\d+(?:\s*[+−-]\s*\d+)?\)?\s*[×xх]\s*\d+)")
CORRECTIONS = {
    "ghatanothoa": [("statblock.characteristics.INT", "210", "100",
                     "значение перетекло из соседнего блока характеристик; в книге ИНТ 100 (стр. 293 PDF)")],
}
REF_IMAGES = "checks/20261018-creatures (проверка по изображениям страниц)"
# Additions found by checking page images (checks/20261018-creatures/verify.jsonl).
OVERRIDES = {
    "cho-cho": {
        "characteristics": {"POW": {"raw": "50", "value": 50}},
        "fields": {"mp": {"raw": "10", "value": 10}},
        "skills": [("Запугивание", 40), ("Плавание", 45), ("Скрытность", 60), ("Чтение следов", 50)],
        "reason": "в данных веб-помощника нет МОЩ, ПМ и навыков; добавлено по книге (стр. 284 PDF)",
    },
    "rhan-tegoth": {
        "name_ru": "Ран-Тигот",
        "reason": "в книге имя пишется «Ран-Тигот» (стр. 302–303 PDF)",
        "note": "в книге к ВЫН 300 есть сноска, в запись не перенесена",
    },
    "cthugha": {
        "flag": "incomplete",
        "note": "в данных веб-помощника нет атаки «Сполох пламени» (стр. 300 PDF); нужно добавить по книге",
    },
}


def apply_overrides(rec: dict, cid: str) -> None:
    o = OVERRIDES.get(cid)
    if not o:
        return
    sb = rec["statblock"]
    for key, val in o.get("characteristics", {}).items():
        rec["corrections"].append({"field": f"statblock.characteristics.{key}", "from": None, "to": val["raw"],
                                   "reason": o["reason"], "ref": REF_IMAGES})
        sb["characteristics"][key] = val
    for key, val in o.get("fields", {}).items():
        rec["corrections"].append({"field": f"statblock.{key}", "from": None, "to": val["raw"],
                                   "reason": o["reason"], "ref": REF_IMAGES})
        sb[key] = val
    if o.get("skills"):
        sb["skills"] = [{"name": n, "value": {"raw": f"{v}%", "value": v}} for n, v in o["skills"]]
        rec["corrections"].append({"field": "statblock.skills", "from": None,
                                   "to": ", ".join(f"{n} {v}%" for n, v in o["skills"]),
                                   "reason": o["reason"], "ref": REF_IMAGES})
    if o.get("name_ru"):
        old = rec["name"]["ru"]
        rec["name"]["ru"] = o["name_ru"]
        rec["aliases"] = sorted(set(rec["aliases"]) | {old})
        rec["corrections"].append({"field": "name.ru", "from": old, "to": o["name_ru"], "reason": o["reason"], "ref": REF_IMAGES})
    q = rec["quality"]
    if o.get("flag"):
        q["flags"] = sorted(set(q["flags"]) | {o["flag"]})
        q["needs_review"] = True
    if o.get("note"):
        q["notes"] = "; ".join(x for x in (q.get("notes"), o["note"]) if x)


def dice(text: str) -> str:
    return re.sub(r"\s+", "", text).replace("к", "d")


def to_int(text: str):
    m = re.match(r"^\s*(\d+)\s*$", text or "")
    return int(m.group(1)) if m else None


def category(cat: str, sub: str) -> str:
    if cat == "Животные":
        return "animal"
    if cat == "Божества Мифов":
        return "avatar" if "воплощение" in (sub or "") else "mythos_deity"
    if cat == "Традиционные монстры":
        return "supernatural"
    return "mythos_monster"


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def looks_cut(text: str, source: str) -> bool:
    """True if the helper field stops mid-sentence compared with the helper's own source text.

    The helper drops final periods, so punctuation alone proves nothing. The field is
    located in raw_source_text by its last 40 characters; if the source continues with
    a letter or digit right after it, the field was cut off.
    """
    t = squash(text).rstrip(" .")
    if len(t) < 12:  # short values like "нет" match anywhere in the source
        return False
    src = squash(source)
    tail = t[-40:]
    i = src.find(tail)
    if i < 0:
        return False
    after = src[i + len(tail):i + len(tail) + 2].strip()
    return bool(after) and after[0].isalnum()


def move(raw: str) -> dict:
    out = {"raw": raw, "value": None, "modes": []}
    for part in [p.strip() for p in re.split(r"[/;]", raw or "") if p.strip()]:
        num = re.search(r"\d+", part)
        word = re.sub(r"[\d()]", "", part).strip().lower()
        mode = next((v for k, v in MOVE_MODES.items() if k in word), "walk" if not word else "other")
        entry = {"mode": mode, "value": int(num.group()) if num else None}
        if mode == "other":
            entry["note"] = part
        out["modes"].append(entry)
    walk = next((m["value"] for m in out["modes"] if m["mode"] == "walk"), None)
    out["value"] = walk if walk is not None else (out["modes"][0]["value"] if out["modes"] else None)
    return out


def split_lines(lines: list[str]) -> list[str]:
    segs = []
    for line in lines:
        # armor, skills, habitat and sanity have their own helper fields; drop their duplicates here
        line = re.split(r"\s*(?:Броня:|Навыки:|Обитает:|Потеря рассудка:)", line)[0]
        parts = re.split(r"\s+(?=(?:Уклонение|Броня:|Навыки:|Обитает:|Потеря рассудка:)\b)", line)
        for part in parts:
            # split "… урон смертельный Плевок слизью 50% (25/10) …" before a new "Name NN% (h/f)"
            segs.extend(s.strip() for s in re.split(r"\s+(?=[А-ЯЁ][а-яё()\s]{2,40}\d+%\s*\()", part) if s.strip())
    return segs


def attacks(lines: list[str]) -> tuple[list[dict], dict | None, list[str]]:
    result, dodge, unparsed = [], None, []
    for seg in split_lines(lines):
        if seg.startswith(STOP_HEADS[1:]):
            continue  # armor / skills / habitat / sanity are taken from their own fields
        m = ATTACK.match(seg)
        if not m or not m.group("name").strip():
            unparsed.append(seg)
            continue
        name = m.group("name").strip().rstrip(":")
        chance = {"raw": f"{m.group('pct')}% ({m.group('h')}/{m.group('f')})", "value": int(m.group("pct")),
                  "half": int(m.group("h")), "fifth": int(m.group("f"))}
        if name.startswith("Уклонение"):
            dodge = chance
            continue
        rest = m.group("rest").strip()
        raw_damage = re.sub(r"^урон\s*:?\s*", "", rest)
        dm = DICE.search(raw_damage)
        attack = {
            "name": {"ru": name, "en": None},
            "kind": "maneuver" if "манёвр" in name else "attack",
            "skill": "Ближний бой" if name.startswith("Ближний бой") else name,
            "chance": chance,
        }
        if raw_damage:
            attack["damage"] = {"raw": raw_damage, "dice": dice(dm.group()) if dm else None, "adds_db": "БкУ" in raw_damage}
        result.append(attack)
    return result, dodge, unparsed


def sanity(text: str) -> list[dict]:
    out = []
    for chunk in re.split(r"[;,]\s*(?=\d)|\.\s+", text or ""):
        m = SAN.search(chunk)
        if m:
            trigger = chunk[m.end():].strip(" .,;—-")
            out.append({"success": dice(m.group(1)), "fail": dice(m.group(2)), "trigger": trigger or None})
    return out


def armor(raw: str) -> dict:
    raw = (raw or "").strip()
    if not raw:
        return {"raw": "", "value": None, "note": "в данных помощника нет"}
    if raw.lower().startswith("нет"):
        return {"raw": raw, "value": 0, "note": raw[3:].strip(" .") or None}
    m = re.match(r"^(\d+)\s*пункт\w*\s*(.*)$", raw)
    if m:
        return {"raw": raw, "value": int(m.group(1)), "note": m.group(2).strip(" .()") or None}
    return {"raw": raw, "value": None, "note": None}


def skills(raw: str) -> list[dict]:
    out = []
    for part in [p.strip() for p in re.split(r",\s*(?![^()]*\))", raw or "") if p.strip()]:
        m = re.match(r"^(.*?)\s*(\d+)%(.*)$", part)
        if m:
            out.append({"name": (m.group(1) + m.group(3)).strip(), "value": {"raw": f"{m.group(2)}%", "value": int(m.group(2))}})
    return out


def value(raw):
    if raw is None:
        return None
    raw = str(raw).strip()
    if raw.lower() == "нет":
        return {"raw": raw, "value": None}
    n = to_int(raw)
    if n is not None:
        return {"raw": raw, "value": n}
    d = DICE.search(raw)
    return {"raw": raw, "value": dice(d.group()) if d else None}


def migrate(h: dict) -> dict:
    stats = h.get("stats") or {}
    combat = h.get("combat") or {}
    text = h.get("raw_source_text") or ""
    rolls = {CHAR[k]: r for k, _, r in ROLL.findall(text)}
    chars = {}
    for ru, en in CHAR.items():
        if ru in stats:
            entry = {"raw": str(stats[ru]), "value": to_int(str(stats[ru]))}
            if en in rolls:
                entry["roll"] = re.sub(r"\s+", "", rolls[en]).replace("к", "d").replace("x", "×").replace("х", "×")
            chars[en] = entry
    flags, notes = set(), []
    atk, dodge, unparsed = attacks(combat.get("attack_lines") or [])
    if unparsed:
        flags.add("parse_uncertain")
        notes.append("не разобрано: " + " | ".join(unparsed)[:400])
    for field in ("armor", "sanity_loss", "spells"):
        if looks_cut(combat.get(field), text):
            flags.add("incomplete")
            notes.append(f"{field} выглядит обрезанным")
    for a in atk:
        if a.get("damage", {}).get("raw", "x") == "":
            flags.add("incomplete")
    statblock = {"characteristics": chars, "averages": bool(rolls)}
    statblock["hp"] = value(stats.get("ПЗ")) or {"raw": "", "value": None, "note": "в данных помощника нет"}
    if "ПЗ" not in stats:
        flags.add("incomplete")
    for key, field in (("ПМ", "mp"), ("БкУ", "damage_bonus"), ("Комплекция", "build")):
        if key in stats:
            statblock[field] = value(stats[key])
    if "СКО" in stats and stats["СКО"] is not None:
        statblock["move"] = move(str(stats["СКО"]))
    statblock["armor"] = armor(combat.get("armor"))
    apr = str(combat.get("attacks_per_round") or "").strip()
    if apr:
        statblock["attacks_per_round"] = value(apr)
    statblock["attacks"] = atk
    if dodge:
        statblock["dodge"] = dodge
    statblock["skills"] = skills(combat.get("skills"))
    if (combat.get("spells") or "").strip():
        statblock["spells"] = {"raw": combat["spells"].strip()}
    san_raw = (combat.get("sanity_loss") or "").strip()
    statblock["sanity_loss"] = sanity(san_raw)
    if san_raw and not statblock["sanity_loss"] and not re.search(r"не вызывает|не вредит|^нет", san_raw):
        flags.add("parse_uncertain")
        notes.append("потеря рассудка не разобрана")
    src = h.get("source") or {}
    printed = min(src.get("pdf_pages") or [0]) or None
    sub = h.get("subcategory")
    record = {
        "schema": "sourcefold.creature.v0",
        "id": f"coc:creature:{h['id']}",
        "kind": "creature",
        "name": {"ru": h["name"], "en": h.get("name_en")},
        "aliases": [a for a in h.get("aliases") or [] if a not in (h["name"], h.get("name_en"))],
        "category": category(h.get("category"), sub),
        "subcategory": sub,
        "axes": {"era": ["any"], "ruleset": "core"},
        "statblock": statblock,
        "description": {"ru": (h.get("description_short") or "").strip(), "en": None},
        "sources": [{
            "book_id": "keeper-rulebook-ru",
            "physical_page": printed - CHAPTER14_OFFSET if printed else None,
            "printed_page": printed,
            "method": "helper_migration",
            "verified": False,
        }],
        "corrections": [],
        "quality": {"needs_review": bool(flags), "flags": sorted(flags), "notes": "; ".join(notes) or None},
    }
    for field, old, new, reason in CORRECTIONS.get(h["id"], []):
        key = field.rsplit(".", 1)[1]
        record["statblock"]["characteristics"][key] = {"raw": new, "value": int(new),
                                                       **({"roll": chars[key]["roll"]} if "roll" in chars.get(key, {}) else {})}
        record["corrections"].append({"field": field, "from": old, "to": new, "reason": reason,
                                      "ref": "checks/20261017-rules-core/report.md"})
    apply_overrides(record, h["id"])
    return record


def mark_verified(out: Path, results: Path | None, verify: Path | None) -> int:
    """Set sources[0].verified for records whose numbers matched the book (step 3)."""
    ok: set[str] = set()
    if results and results.exists():
        for r in json.loads(results.read_text(encoding="utf-8"))["results"]:
            if r["status"] == "ok":
                ok.add(r["id"].split(":")[-1])
    if verify and verify.exists():
        for line in verify.read_text(encoding="utf-8").splitlines():
            if line.strip():
                v = json.loads(line)
                if v.get("verdict") == "ok_ocr":
                    ok.add(v["slug"])
    n = 0
    for slug in ok:
        p = out / f"{slug}.json"
        if not p.exists():
            continue
        rec = json.loads(p.read_text(encoding="utf-8"))
        if rec["sources"][0]["method"] == "helper_migration" and not rec["sources"][0].get("verified"):
            rec["sources"][0]["verified"] = True
            p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            n += 1
    return n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--helper", type=Path, required=True)
    ap.add_argument("--examples", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--check-results", type=Path, help="checks/20261018-creatures/results.json")
    ap.add_argument("--verify", type=Path, help="checks/20261018-creatures/verify.jsonl")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    curated = {p.stem for p in a.examples.glob("*.json")}
    n = flagged = 0
    for p in sorted(a.helper.glob("*.json")):
        h = json.loads(p.read_text(encoding="utf-8"))
        if not str(h.get("source_set", "")).startswith("keeper_rulebook"):
            continue
        n += 1
        if h["id"] in curated:
            shutil.copyfile(a.examples / f"{h['id']}.json", a.out / f"{h['id']}.json")
            continue
        rec = migrate(h)
        flagged += bool(rec["quality"]["flags"])
        (a.out / f"{h['id']}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    verified = mark_verified(a.out, a.check_results, a.verify)
    print(f"creatures: {n}, curated: {len(curated)}, flagged: {flagged}, marked verified: {verified}")


if __name__ == "__main__":
    main()
