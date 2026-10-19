"""Check derived values of character records against the 7th edition rules.

For each character with a stat block: HP = (CON + SIZ) // 10, MP = POW // 5, damage bonus and build by
STR + SIZ, MOV from STR, DEX, SIZ and age (−1 per decade from 40), dodge not below DEX // 2, and the
half / fifth of every percentage. Mismatches that are not yet listed in `errata` are reported; with
--write they are added to `errata` as kept as printed (the printed value stays in the record).

Usage: python checks/20261020-characters/check_characters.py [--kb kb] [--write] [--out <json>]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ALIASES = {"Скорость": ["move", "ско"], "ПМ": ["mp"], "ПЗ": ["hp"], "БкУ": ["damage_bonus", "бонус"], "Комплекция": ["build", "компл"], "Уклонение": ["dodge"]}


def db_build(total: int) -> tuple[str, int]:
    if total <= 64:
        return "-2", -2
    if total <= 84:
        return "-1", -1
    if total <= 124:
        return "0", 0
    if total <= 164:
        return "+1d4", 1
    if total <= 204:
        return "+1d6", 2
    extra = (total - 205) // 80
    return f"+{2 + extra}d6", 3 + extra


def norm_db(v) -> str:
    s = str(v if v is not None else "").replace(" ", "").replace("к", "d").replace("–", "-").replace("−", "-").lower()
    if s in ("", "0", "нет", "none"):
        return "0"
    if re.fullmatch(r"\d+d\d+", s):
        s = "+" + s
    return s


def num(v):
    if isinstance(v, (int, float)):
        return int(v)
    m = re.search(r"-?\d+", str(v or ""))
    return int(m.group()) if m else None


def checks(r: dict) -> list[tuple[str, str, str]]:
    sb = r.get("statblock") or {}
    ch = {k: (v or {}).get("value") for k, v in (sb.get("characteristics") or {}).items()}
    out = []
    S, C, Z, D, P = (ch.get(k) for k in ("STR", "CON", "SIZ", "DEX", "POW"))
    if C and Z and sb.get("hp"):
        exp = (C + Z) // 10
        if num(sb["hp"].get("value")) != exp:
            out.append(("ПЗ", sb["hp"].get("raw"), str(exp)))
    if P and sb.get("mp"):
        exp = P // 5
        if num(sb["mp"].get("value")) != exp:
            out.append(("ПМ", sb["mp"].get("raw"), str(exp)))
    if S and Z:
        db, build = db_build(S + Z)
        if sb.get("damage_bonus") and norm_db(sb["damage_bonus"].get("value", sb["damage_bonus"].get("raw"))) != db:
            out.append(("БкУ", sb["damage_bonus"].get("raw"), db))
        if sb.get("build") and num(sb["build"].get("value")) != build:
            out.append(("Комплекция", sb["build"].get("raw"), str(build)))
    if S and D and Z and sb.get("move"):
        base = 9 if S > Z and D > Z else 7 if S < Z and D < Z else 8
        age = num((r.get("age") or {}).get("value")) or 0
        exp = base - max(0, age // 10 - 3)
        if num(sb["move"].get("value")) != exp:
            out.append(("Скорость", sb["move"].get("raw"), str(exp)))
    if D and sb.get("dodge") and isinstance(sb["dodge"].get("value"), int) and sb["dodge"]["value"] < D // 2:
        out.append(("Уклонение", sb["dodge"].get("raw"), f"не ниже {D // 2}% (половина ЛВК)"))
    pcts = [("Уклонение", sb.get("dodge"))] + [((a.get("name") or {}).get("ru"), a.get("chance")) for a in sb.get("attacks") or []] \
        + [(s.get("name"), s.get("value")) for s in sb.get("skills") or []]
    for name, v in pcts:
        if isinstance(v, dict) and isinstance(v.get("value"), int) and v.get("half") is not None and v.get("fifth") is not None:
            if (v["half"], v["fifth"]) != (v["value"] // 2, v["value"] // 5):
                out.append((name, v.get("raw"), f"{v['value']}% ({v['value'] // 2}/{v['value'] // 5})"))
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=Path(__file__).resolve().parents[2] / "kb")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    report = []
    for p in sorted(a.kb.rglob("characters/*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        known = " ".join((e.get("field") or "") for e in r.get("errata") or []).lower()
        text = json.dumps(r, ensure_ascii=False).lower()
        def listed(f: str) -> bool:
            keys = [f.lower().split(" (")[0]] + ALIASES.get(f, [])
            return any(k in known for k in keys)
        new = [(f, pr, ex) for f, pr, ex in checks(r) if not listed(f or "")
               and not (f == "Скорость" and "хромот" in text)]
        for f, pr, ex in new:
            report.append({"id": r["id"], "field": f, "printed": pr, "expected": ex})
            print(f"{p.parent.parent.name}/{p.stem}: {f} напечатано {pr}, по правилам {ex}")
        if a.write and new:
            for f, pr, ex in new:
                r.setdefault("errata", []).append({"field": f, "printed": pr, "expected": ex,
                                                   "note": "не сходится с правилами 7-й редакции; оставлено как напечатано (сквозная проверка)"})
            fl = r.setdefault("quality", {"needs_review": False, "flags": [], "notes": None}).setdefault("flags", [])
            if "parse_uncertain" not in fl:
                fl.append("parse_uncertain")
            p.write_bytes((json.dumps(r, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    if a.out:
        a.out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"new mismatches: {len(report)}")


if __name__ == "__main__":
    main()
