"""Build kb/occupations/ from occupations read off the Investigator Handbook page images (decision R-46).

Input: JSONL files with {name, group, lovecraftian, description, skill_points{raw, formula}, credit_rating, contacts,
skills[], era, physical_page, printed_page, note?, group_description?}.

Usage: python pipeline/migrate/ih_occupations.py <jsonl> [<jsonl> ...] [--out kb/occupations]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TR = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
              ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f",
               "kh", "ts", "ch", "sh", "shch", "", "y", "", "e", "yu", "ya"]))


def slug(name: str) -> str:
    s = "".join(TR.get(c, c) for c in name.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def era(v: str) -> list[str]:
    v = (v or "any").lower()
    if v.startswith("modern") or "соврем" in v:
        return ["modern"]
    if v.startswith("classic") or "классич" in v or "1920" in v:
        return ["1920s"]
    return ["any"]


def options(f) -> list:
    """Formula as a list of alternatives, each a list of [characteristic, multiplier]."""
    if not f:
        return []
    return [f] if isinstance(f[0][0], str) else f


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[2] / "kb" / "occupations")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    rows = [json.loads(l) for f in a.inputs for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    used: set[str] = set()
    for r in rows:
        sl = slug(r["name"])
        while sl in used:
            sl += "-2"
        used.add(sl)
        desc = r.get("description") or ""
        if r.get("group_description") and r["group_description"] not in desc:
            desc = (r["group_description"] + "\n\n" + desc).strip()
        rec = {
            "schema": "sourcefold.occupation.v0",
            "id": f"coc:occupation:{sl}",
            "kind": "occupation",
            "name": {"ru": r["name"], "en": None},
            "group": r.get("group"),
            "lovecraftian": bool(r.get("lovecraftian")),
            "description": {"ru": desc, "en": None},
            "skill_points": {"raw": r["skill_points"]["raw"], "options": options(r["skill_points"].get("formula"))},
            "credit_rating": r["credit_rating"],
            "contacts": r.get("contacts"),
            "skills": r["skills"],
            "axes": {"era": era(r.get("era")), "ruleset": "core"},
            "sources": [{"book_id": "investigator-handbook-ru", "physical_page": r["physical_page"],
                         "printed_page": r.get("printed_page"), "method": "book_text", "verified": True}],
            "quality": {"needs_review": False, "flags": [], "notes": r.get("note")},
        }
        (a.out / f"{sl}.json").write_bytes((json.dumps(rec, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    print(f"{len(rows)} occupations -> {a.out}")


if __name__ == "__main__":
    main()
