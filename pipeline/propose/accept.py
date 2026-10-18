"""Accept a creature change proposal into the knowledge base.

Reads proposals/<book_id>/decision.json:
{
  "decided": "2026-10-18", "decision": "R-19",
  "accept": ["detenysh", "glubokovodnyy-gibrid"],
  "prefer_values": {"glubokovodnyy-gibrid": "candidate"}   # take differing/missing values from the
}                                                            # canonical candidate found by the proposal
Accepted records are written to kb/books/<book_id>/creatures/<slug>.json. Every value taken
from the candidate is logged in `corrections` with the scenario's original value.

Usage: python pipeline/propose/accept.py --proposals proposals --book-id <id>
        --helper <helper monsters dir> --kb-books kb/books
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from creatures import helper_numbers  # noqa: E402

CHAR_EN = {"СИЛ": "STR", "ВЫН": "CON", "ТЕЛ": "SIZ", "ЛВК": "DEX", "НАР": "APP", "ИНТ": "INT", "МОЩ": "POW", "ОБР": "EDU"}
PCT = re.compile(r"(\d+)%\s*\((\d+)/(\d+)\)")


def set_value(rec: dict, field: str, value: str) -> tuple[str, str | None]:
    """Write one value (labelled as in the proposal) into the record; return (path, old raw)."""
    sb = rec["statblock"]
    if field in CHAR_EN:
        key = CHAR_EN[field]
        old = sb["characteristics"].get(key, {}).get("raw")
        n = re.match(r"^\d+", value)
        sb["characteristics"][key] = {"raw": value, "value": int(n.group()) if n else None}
        return f"statblock.characteristics.{key}", old
    if field == "СКО":
        old = sb.get("move", {}).get("raw")
        nums = [int(x) for x in re.findall(r"\d+", value)]
        modes = [{"mode": "walk", "value": nums[0]}] if nums else []
        if len(nums) > 1:
            modes.append({"mode": "swim" if "плав" in value else "other", "value": nums[1]})
        sb["move"] = {"raw": value, "value": nums[0] if nums else None, "modes": modes}
        return "statblock.move", old
    if field == "Уклонение":
        old = sb.get("dodge", {}).get("raw")
        m = PCT.search(value)
        sb["dodge"] = {"raw": value, "value": int(m.group(1)), "half": int(m.group(2)), "fifth": int(m.group(3))}
        return "statblock.dodge", old
    if field == "Рассудок":
        old_list = sb.get("sanity_loss") or []
        old = f"{old_list[0]['success']}/{old_list[0]['fail']}" if old_list else None
        s, f = value.split("/")
        trigger = old_list[0].get("trigger") if old_list else None
        sb["sanity_loss"] = [{"success": s, "fail": f, "trigger": trigger}] + old_list[1:]
        return "statblock.sanity_loss", old
    if field.startswith("навык: "):
        name = field[len("навык: "):]
        skills = sb.setdefault("skills", [])
        for s in skills:
            if s["name"] == name:
                old = s["value"]["raw"]
                s["value"] = {"raw": value, "value": int(value.rstrip("%"))}
                return f"statblock.skills.{name}", old
        skills.append({"name": name, "value": {"raw": value, "value": int(value.rstrip("%"))}})
        return f"statblock.skills.{name}", None
    raise KeyError(field)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--proposals", type=Path, required=True)
    ap.add_argument("--book-id", required=True)
    ap.add_argument("--helper", type=Path, required=True)
    ap.add_argument("--kb-books", type=Path, required=True)
    a = ap.parse_args()
    pdir = a.proposals / a.book_id
    decision = json.loads((pdir / "decision.json").read_text(encoding="utf-8"))
    proposal = json.loads((pdir / "proposal.json").read_text(encoding="utf-8"))
    items = {it["id"].split("/")[-1]: it for it in proposal["items"]}
    out = a.kb_books / a.book_id / "creatures"
    out.mkdir(parents=True, exist_ok=True)
    for slug in decision["accept"]:
        rec = json.loads((pdir / "creatures" / f"{slug}.json").read_text(encoding="utf-8"))
        it = items[slug]
        if decision.get("prefer_values", {}).get(slug) == "candidate" and it.get("canonical_outside_base"):
            cand = json.loads((a.helper / f"{it['canonical_outside_base']['helper_id']}.json").read_text(encoding="utf-8"))
            theirs = helper_numbers(cand)
            for d in it["differences_vs_candidate"]:
                if d["other"] is None:
                    continue  # nothing to take from the candidate
                path, old = set_value(rec, d["field"], d["other"])
                rec["corrections"].append({
                    "field": path, "from": old, "to": d["other"],
                    "reason": f"решение владельца {decision['decision']}: значения из «{it['canonical_outside_base']['name']}» "
                              f"({it['canonical_outside_base']['source']}) считаются более правильными",
                    "ref": f"proposals/{a.book_id}/proposal.md"})
            rec["quality"] = {"needs_review": False, "flags": [],
                              "notes": "значения, отличавшиеся от карточки Malleus, заменены по решению владельца"}
        rec["sources"][0]["verified"] = True
        (out / f"{slug}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("accepted", rec["id"])


if __name__ == "__main__":
    main()
