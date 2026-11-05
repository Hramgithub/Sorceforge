"""Derived values of a character's stat block against the 7th edition rules (Р-35, Р-36, Р-161).

HP = (CON + SIZ) / 10, MP = POW / 5, damage bonus and build by STR + SIZ, MOV by STR, DEX and SIZ with −1 per decade
from 40, dodge not below DEX / 2, half and fifth of every percentage. Book conventions are not mismatches (Р-161):
HP rounded up as well as down, MOV with or without the age penalty. Stat blocks on another scale (a body on a 1–18
scale, an inhuman being with characteristics over 100) are not checked. A field already listed in `errata` is known.
"""
from __future__ import annotations

import re

KNOWN = {"Скорость": ["move", "ско"], "ПМ": ["mp"], "ПЗ": ["hp"], "БкУ": ["damage_bonus", "бонус"], "Комплекция": ["build", "компл"], "Уклонение": ["dodge"]}


def db_build(total: int) -> tuple[str, int]:
    for top, db, build in ((64, "-2", -2), (84, "-1", -1), (124, "0", 0), (164, "+1d4", 1), (204, "+1d6", 2)):
        if total <= top:
            return db, build
    extra = (total - 205) // 80
    return f"+{2 + extra}d6", 3 + extra


def norm_db(v) -> str:
    s = str(v if v is not None else "").replace(" ", "").replace("к", "d").replace("–", "-").replace("−", "-").lower()
    if s in ("", "0", "нет", "none"):
        return "0"
    return "+" + s if re.fullmatch(r"\d+d\d+", s) else s


def num(v):
    if isinstance(v, (int, float)):
        return int(v)
    m = re.search(r"-?\d+", str(v or ""))
    return int(m.group()) if m else None


def mismatches(r: dict) -> list[tuple[str, str, str]]:
    """(field, printed, expected) for each derived value that is neither by the rules nor a book convention nor known."""
    sb = r.get("statblock") or {}
    ch = {k: (v or {}).get("value") for k, v in (sb.get("characteristics") or {}).items()}
    vals = [v for v in ch.values() if isinstance(v, int)]
    if not vals or max(vals) > 100 or max(vals) <= 25:
        return []
    S, C, Z, D, P = (ch.get(k) for k in ("STR", "CON", "SIZ", "DEX", "POW"))
    out = []
    if C and Z and sb.get("hp") and num(sb["hp"].get("value")) not in ((C + Z) // 10, -(-(C + Z) // 10)):
        out.append(("ПЗ", sb["hp"].get("raw"), str((C + Z) // 10)))
    if P and sb.get("mp") and num(sb["mp"].get("value")) not in (P // 5, -(-P // 5)):
        out.append(("ПМ", sb["mp"].get("raw"), str(P // 5)))
    if S and Z:
        db, build = db_build(S + Z)
        if sb.get("damage_bonus") and norm_db(sb["damage_bonus"].get("value", sb["damage_bonus"].get("raw"))) != db:
            out.append(("БкУ", sb["damage_bonus"].get("raw"), db))
        if sb.get("build") and num(sb["build"].get("value")) != build:
            out.append(("Комплекция", sb["build"].get("raw"), str(build)))
    if S and D and Z and sb.get("move"):
        base = 9 if S > Z and D > Z else 7 if S < Z and D < Z else 8
        age = num((r.get("age") or {}).get("value")) or 0
        aged = base - max(0, age // 10 - 3)
        if num(sb["move"].get("value")) not in (base, aged):
            out.append(("Скорость", sb["move"].get("raw"), str(aged)))
    if D and sb.get("dodge") and isinstance(sb["dodge"].get("value"), int) and sb["dodge"]["value"] < D // 2:
        out.append(("Уклонение", sb["dodge"].get("raw"), f"не ниже {D // 2}%"))
    pcts = [("Уклонение", sb.get("dodge"))] + [((a.get("name") or {}).get("ru"), a.get("chance")) for a in sb.get("attacks") or []] \
        + [(s.get("name"), s.get("value")) for s in sb.get("skills") or []]
    for name, v in pcts:
        if isinstance(v, dict) and isinstance(v.get("value"), int) and v.get("half") is not None and v.get("fifth") is not None \
                and (v["half"], v["fifth"]) != (v["value"] // 2, v["value"] // 5):
            out.append((name or "?", v.get("raw"), f"{v['value']}% ({v['value'] // 2}/{v['value'] // 5})"))
    known = " ".join((e.get("field") or "") for e in r.get("errata") or []).lower()
    text = str(r).lower()
    listed = lambda f: any(k in known for k in [f.lower().split(" (")[0]] + KNOWN.get(f, []))
    return [(f, pr, ex) for f, pr, ex in out if not listed(f) and not (f == "Скорость" and "хромот" in text)]
