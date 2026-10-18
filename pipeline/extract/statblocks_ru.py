"""Extract creature stat blocks from MinerU markdown of a Russian CoC scenario.

Finds every characteristics line ("СИЛ 100 ВЫН 40 ...") and builds a creature record
(schema sourcefold.creature.v0) from the text up to the next stat block. The creature
name is the nearest short line or heading above the characteristics. Attack lines
("Name NN% (h/f), урон ..."), dodge, skills, armor, sanity loss, special abilities
("Name: text") are parsed; raw text is kept beside every value. Anything unexpected
is flagged instead of guessed.

Usage: python pipeline/extract/statblocks_ru.py --md <mineru .md> --book-id <id>
        --pages <first-last physical pages of the md> --out <dir>
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CHAR = {"СИЛ": "STR", "ВЫН": "CON", "ТЕЛ": "SIZ", "ЛВК": "DEX", "НАР": "APP", "ИНТ": "INT", "МОЩ": "POW", "ОБР": "EDU"}
STATLINE = re.compile(r"^\s*СИЛ\s+\S+\s+ВЫН\s+")
ATTACK = re.compile(r"^(?P<name>[^%]{2,60}?)\s+(?P<pct>\d+)%\s*\((?P<h>\d+)\s*/\s*(?P<f>\d+)\)\s*,?\s*(?P<rest>.*)$")
DICE = re.compile(r"\d+\s*[DdКк]\s*\d+(?:\s*[+−-]\s*\d+(?!\s*[DdКк/\d]))?")
SAN = re.compile(r"(\d+(?:\s*[DdКк]\s*\d+)?)\s*/\s*(\d+\s*[DdКк]\s*\d+(?:\s*\+\s*\d+)?|\d+)")
TRANSLIT = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                    ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t",
                     "u", "f", "kh", "ts", "ch", "sh", "shch", "", "y", "", "e", "yu", "ya"]))


def slug(text: str) -> str:
    s = "".join(TRANSLIT.get(c, c) for c in text.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def dice(text: str) -> str:
    return re.sub(r"\s+", "", text).replace("D", "d").replace("к", "d").replace("К", "d")


def clean(line: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"^#+\s*", "", line)).strip()


def num(text: str):
    m = re.match(r"^[+]?(\d+)$", text.strip())
    return int(m.group(1)) if m else None


def value(raw: str) -> dict:
    raw = raw.strip()
    if raw in ("-", "—", ""):
        return {"raw": raw, "value": None}
    n = num(raw)
    if n is not None:
        return {"raw": raw, "value": n}
    d = DICE.search(raw)
    return {"raw": raw, "value": dice(d.group()) if d else None}


def parse_stats(lines: list[str]) -> tuple[dict, dict, list[str]]:
    text = " ".join(lines)
    chars, derived, notes = {}, {}, []
    for ru, en in CHAR.items():
        m = re.search(rf"\b{ru}\s+(\S+)", text)
        if m and m.group(1) not in ("-", "—"):
            chars[en] = {"raw": m.group(1), "value": num(m.group(1))}
    for key, field in (("ПЗ", "hp"), ("ПМ", "mp"), ("БкУ", "damage_bonus"), ("Компл", "build")):
        m = re.search(rf"\b{key}\s+(\S+)", text)
        if m:
            derived[field] = value(m.group(1))
    m = re.search(r"\bСКО\s+([\d/]+(?:\s+(?:плавание|полёт|рытьё))?)", text)
    if m:
        raw = m.group(1)
        parts = raw.split()[0].split("/")
        mode2 = {"плавание": "swim", "полёт": "fly", "рытьё": "burrow"}.get(raw.split()[1] if len(raw.split()) > 1 else "", "other")
        modes = [{"mode": "walk", "value": num(parts[0])}]
        if len(parts) > 1:
            modes.append({"mode": mode2, "value": num(parts[1])})
        derived["move"] = {"raw": raw, "value": num(parts[0]), "modes": modes}
    return chars, derived, notes


def build(name: str, block: list[str], book_id: str, page: int | None) -> dict:
    stat_lines = [l for l in block if re.search(r"\b(СИЛ|НАР|БкУ)\s", l)][:3]
    chars, derived, notes = parse_stats(stat_lines)
    sb = {"characteristics": chars, "averages": False, "hp": derived.get("hp", {"raw": "", "value": None})}
    for k in ("mp", "damage_bonus", "build", "move"):
        if k in derived:
            sb[k] = derived[k]
    attacks, abilities, skills, san, flags = [], [], [], [], set()
    for line in block:
        if line in stat_lines or line.lower() in ("бой", "навыки"):
            continue
        if line.startswith("Атак за раунд:"):
            raw = line.split(":", 1)[1].strip()
            m = re.match(r"(\d+)", raw)
            sb["attacks_per_round"] = {"raw": raw, "value": int(m.group(1)) if m else None}
            continue
        if line.startswith("Броня:"):
            raw = line.split(":", 1)[1].strip()
            m = re.match(r"(\d+)\s*пункт", raw)
            sb["armor"] = {"raw": raw, "value": 0 if raw.lower().startswith("нет") else (int(m.group(1)) if m else None)}
            continue
        if line.startswith("Навыки"):
            line = line[len("Навыки"):].strip()
        m = ATTACK.match(line)
        if m:
            chance = {"raw": f"{m.group('pct')}% ({m.group('h')}/{m.group('f')})", "value": int(m.group("pct")),
                      "half": int(m.group("h")), "fifth": int(m.group("f"))}
            if chance["half"] != chance["value"] // 2 or chance["fifth"] != chance["value"] // 5:
                flags.add("parse_uncertain")
                notes.append(f"в источнике половина/пятая не сходятся с процентом: {chance['raw']}")
            nm = m.group("name").strip()
            if nm.startswith("Уклонение"):
                sb["dodge"] = chance
                continue
            rest = m.group("rest").strip()
            raw_dmg = re.sub(r"^урон\s*:?\s*", "", rest)
            dm = DICE.search(raw_dmg)
            atk = {"name": {"ru": nm, "en": None}, "kind": "attack",
                   "skill": "Ближний бой" if nm.startswith("Ближний бой") else nm, "chance": chance}
            if raw_dmg:
                atk["damage"] = {"raw": raw_dmg, "dice": dice(dm.group()) if dm else None, "adds_db": "БкУ" in raw_dmg}
            attacks.append(atk)
            continue
        if re.search(r"\d+%", line) and not ATTACK.match(line) and "," in line or re.match(r"^[А-ЯЁ][а-яё ]+\s\d+%\.?$", line):
            for part in re.split(r",\s*", line.rstrip(".")):
                sm = re.match(r"^(.*?)\s*(\d+)%$", part.strip())
                if sm:
                    skills.append({"name": sm.group(1).strip(), "value": {"raw": f"{sm.group(2)}%", "value": int(sm.group(2))}})
            continue
        if "Рассудк" in line and SAN.search(line):
            for sm in SAN.finditer(line):
                trigger = line[sm.end():].strip(" .,")
                trigger = re.sub(r"^пункт\w*\s+Рассудка,?\s*", "", trigger)
                san.append({"success": dice(sm.group(1)), "fail": dice(sm.group(2)), "trigger": trigger or None})
            continue
        am = re.match(r"^([А-ЯЁ][^:]{2,40}):\s*(.+)$", line)
        if am:
            abilities.append({"name": am.group(1).strip(), "summary": am.group(2).strip()})
            continue
    sb["attacks"] = attacks
    sb["skills"] = skills
    sb["sanity_loss"] = san
    rec = {
        "schema": "sourcefold.creature.v0",
        "id": f"{book_id}/creature/{slug(name.split(',')[0])}",
        "kind": "creature",
        "name": {"ru": name.split(",")[0].strip(), "en": None},
        "aliases": [],
        "category": "mythos_monster",
        "subcategory": name.split(",", 1)[1].strip() if "," in name else None,
        "axes": {"era": ["1920s"], "ruleset": "core"},
        "statblock": sb,
        "abilities": abilities,
        "sources": [{"book_id": book_id, "physical_page": page, "printed_page": None, "method": "mineru", "verified": False}],
        "corrections": [],
        "quality": {"needs_review": bool(flags), "flags": sorted(flags), "notes": "; ".join(notes) or None},
    }
    if "armor" not in sb:
        rec["quality"]["flags"] = sorted(set(rec["quality"]["flags"]) | {"incomplete"})
        rec["quality"]["needs_review"] = True
    return rec


def extract(md: str, book_id: str, first_page: int, last_page: int) -> list[dict]:
    lines = [clean(l) for l in md.splitlines()]
    # drop images and running headers (all-caps lines without digits, e.g. the scenario title);
    # stat lines like "НАР - МОЩ 40 ОБР - ПЗ 6" are all caps too but contain digits
    lines = [l for l in lines if l and not l.startswith("![") and not (l.upper() == l and not re.search(r"\d", l))]
    starts = [i for i, l in enumerate(lines) if STATLINE.match(l)]
    records = []
    for k, i in enumerate(starts):
        # name: nearest heading or short line above (skip long paragraphs)
        name = next((lines[j] for j in range(i - 1, max(-1, i - 6), -1) if len(lines[j]) <= 80 and not lines[j].endswith(".")), "Безымянное существо")
        end = starts[k + 1] - 1 if k + 1 < len(starts) else len(lines)
        if k + 1 < len(starts):
            # stop before the next creature's name/description
            nxt_name = next((j for j in range(starts[k + 1] - 1, i, -1) if len(lines[j]) <= 80 and not lines[j].endswith(".")), end)
            end = nxt_name
        block = lines[i:end]
        page = first_page if first_page == last_page else None
        records.append(build(name, block, book_id, page))
    return records


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", type=Path, required=True)
    ap.add_argument("--book-id", required=True)
    ap.add_argument("--pages", required=True, help="first-last physical pages covered by the md")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    first, last = (int(x) for x in a.pages.split("-"))
    recs = extract(a.md.read_text(encoding="utf-8"), a.book_id, first, last)
    a.out.mkdir(parents=True, exist_ok=True)
    for r in recs:
        (a.out / f"{r['id'].split('/')[-1]}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"extracted {len(recs)} creatures -> {a.out}")
    for r in recs:
        print(" ", r["id"], r["quality"]["flags"])


if __name__ == "__main__":
    main()
