"""Build a change proposal for creatures extracted from a book.

For every extracted creature:
- locate its physical page by the name in per-page text of the source PDF;
- look for the same creature in the knowledge base (kb/creatures) by name and aliases;
- if absent, look in the web helper data that was not migrated (e.g. Malleus cards) and
  report it as a canonical candidate outside the base;
- compare numbers with the match and list differences.

Nothing is written to kb/. Output: proposals/<book_id>/creatures/*.json (candidate
records) and proposals/<book_id>/proposal.md + proposal.json for the owner's decision.

Usage: python pipeline/propose/creatures.py --extracted <dir> --book-id <id>
        --page-text <dir with pNN.txt> --kb kb/creatures --helper <helper monsters dir>
        --out proposals
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CHAR_RU = {"STR": "СИЛ", "CON": "ВЫН", "SIZ": "ТЕЛ", "DEX": "ЛВК", "APP": "НАР", "INT": "ИНТ", "POW": "МОЩ", "EDU": "ОБР"}


def norm(s: str) -> str:
    return re.sub(r"[^а-яa-z0-9]+", " ", (s or "").lower().replace("ё", "е")).strip()


def stems(s: str) -> set[str]:
    return {w[:6] for w in norm(s).split() if len(w) >= 4}


def same_name(a: str, b: str) -> bool:
    sa, sb = stems(a), stems(b)
    return bool(sa) and sa == sb


def find_page(name: str, pages: dict[int, str]) -> int | None:
    """Page of the stat block: the name and a characteristics line on the same page."""
    key = norm(name)
    hits = [p for p, t in sorted(pages.items()) if key and key in norm(t)]
    with_stats = [p for p in hits if re.search(r"СИЛ\s+\d", pages[p])]
    return (with_stats or hits or [None])[0]


PCT = re.compile(r"(\d+)%\s*\((\d+)/(\d+)\)")
SANR = re.compile(r"(\d+(?:\s*[DdКк]\s*\d+)?)\s*/\s*(\d+\s*[DdКк]\s*\d+|\d+)")


def kb_numbers(rec: dict) -> dict[str, str]:
    sb = rec["statblock"]
    out = {CHAR_RU.get(k, k): v.get("raw") for k, v in sb.get("characteristics", {}).items()}
    for k, ru in (("hp", "ПЗ"), ("mp", "ПМ"), ("damage_bonus", "БкУ"), ("build", "Комплекция"), ("move", "СКО")):
        if isinstance(sb.get(k), dict):
            out[ru] = sb[k].get("raw")
    for a in sb.get("attacks", []):
        out[a["name"]["ru"]] = a["chance"]["raw"]
    if sb.get("dodge"):
        out["Уклонение"] = sb["dodge"]["raw"]
    for s in sb.get("skills", []):
        out["навык: " + s["name"]] = s["value"]["raw"]
    if sb.get("sanity_loss"):
        out["Рассудок"] = f"{sb['sanity_loss'][0]['success']}/{sb['sanity_loss'][0]['fail']}"
    return out


def helper_numbers(h: dict) -> dict[str, str]:
    """Numbers of a web-helper record, in either the rulebook-addendum or the Malleus-card format."""
    out: dict[str, str] = {}
    stats = h.get("stats") or {}
    malleus_keys = {"hit_points": "ПЗ", "magic_points": "ПМ", "damage_bonus": "БкУ", "build": "Комплекция", "move": "СКО"}
    for k, v in stats.items():
        out[malleus_keys.get(k, k)] = str(v)
    for c in h.get("characteristics") or []:
        if isinstance(c, dict) and c.get("name"):
            out[c["name"]] = str(c.get("average"))
    combat = h.get("combat")
    if isinstance(combat, str):
        names = [n for n in ("Ближний бой", "Уклонение") if n in combat]
        for n, m in zip(names, PCT.finditer(combat)):
            out[n] = f"{m.group(1)}% ({m.group(2)}/{m.group(3)})"
    if isinstance(h.get("skills"), str):
        for m in re.finditer(r"([А-ЯЁ][а-яё ]+?)\s+(\d+)%", h["skills"].replace("\n", " ")):
            out["навык: " + m.group(1).strip()] = f"{m.group(2)}%"
    if isinstance(h.get("sanity_loss"), str):
        m = SANR.search(h["sanity_loss"])
        if m:
            out["Рассудок"] = f"{m.group(1)}/{m.group(2)}".replace("к", "d")
    return out


def canon(v) -> str:
    return re.sub(r"\s+", "", str(v or "")).lower().replace("к", "d").replace("+", "").replace("нет", "0")


def same_value(a: str, b: str) -> bool:
    ca, cb = canon(a), canon(b)
    if ca == cb:
        return True
    m = re.match(r"^(\d+)[–-](\d+)$", cb)  # a range like "50–55" contains the scenario value
    if m and ca.isdigit():
        return int(m.group(1)) <= int(ca) <= int(m.group(2))
    return False


def diff(a: dict[str, str], b: dict[str, str]) -> list[dict]:
    out = []
    for k in sorted(set(a) | set(b)):
        va, vb = a.get(k), b.get(k)
        if va is None or vb is None:
            out.append({"field": k, "scenario": va, "other": vb, "kind": "only_one_side"})
        elif not same_value(va, vb):
            out.append({"field": k, "scenario": va, "other": vb, "kind": "different"})
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--extracted", type=Path, required=True)
    ap.add_argument("--book-id", required=True)
    ap.add_argument("--page-text", type=Path, required=True)
    ap.add_argument("--kb", type=Path, required=True)
    ap.add_argument("--helper", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    pages = {int(re.sub(r"\D", "", f.stem)): f.read_text(encoding="utf-8") for f in a.page_text.glob("p*.txt")}
    kb = [json.loads(p.read_text(encoding="utf-8")) for p in a.kb.glob("*.json")]
    kb_ids = {r["id"].split(":")[-1] for r in kb}
    helper = [json.loads(p.read_text(encoding="utf-8")) for p in a.helper.glob("*.json")]
    out_dir = a.out / a.book_id
    (out_dir / "creatures").mkdir(parents=True, exist_ok=True)
    items = []
    for f in sorted(a.extracted.glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        name = rec["name"]["ru"]
        page = find_page(name + (", " + rec["subcategory"] if rec.get("subcategory") else ""), pages) or find_page(name, pages)
        rec["sources"][0]["physical_page"] = page
        match = next((k for k in kb if any(same_name(name, n) for n in [k["name"]["ru"], *(k.get("aliases") or [])])), None)
        item = {"id": rec["id"], "name": name, "page": page, "flags": rec["quality"]["flags"], "notes": rec["quality"].get("notes")}
        if match:
            rec["same_as"] = [match["id"]]
            item.update(action="add_variant", same_as=match["id"], differences=diff(kb_numbers(rec), kb_numbers(match)))
        else:
            cand = next((h for h in helper if h["id"] not in kb_ids and
                         any(same_name(name, n) for n in [h.get("name", ""), *(h.get("aliases") or [])])), None)
            item["action"] = "add_new"
            if cand:
                item["canonical_outside_base"] = {"helper_id": cand["id"], "name": cand.get("name"),
                                                  "source": (cand.get("source") or {}).get("book") or cand.get("source_set")}
                mine, theirs = kb_numbers(rec), helper_numbers(cand)
                item["differences_vs_candidate"] = diff(mine, theirs)
                item["matched_vs_candidate"] = len(set(mine) & set(theirs)) - sum(
                    d["kind"] == "different" for d in item["differences_vs_candidate"])
        (out_dir / "creatures" / f"{rec['id'].split('/')[-1]}.json").write_text(
            json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        items.append(item)
    (out_dir / "proposal.json").write_text(json.dumps({"book_id": a.book_id, "items": items}, ensure_ascii=False, indent=2) + "\n",
                                           encoding="utf-8")
    md = [f"# Предложение изменений: {a.book_id}", "", "Ничего не записано в базу. Записи-кандидаты — в `creatures/`.", ""]
    for it in items:
        md.append(f"## {it['name']} — {'новое существо' if it['action'] == 'add_new' else 'вариант записи из базы'}")
        md.append(f"- Страница PDF сценария: {it['page']}")
        if it.get("same_as"):
            md.append(f"- Совпадает с записью базы `{it['same_as']}`; отличия: {len(it['differences'])}")
            md += [f"  - {d['field']}: в сценарии {d['scenario']}, в базе {d['other']}" for d in it["differences"]]
        if it.get("canonical_outside_base"):
            c = it["canonical_outside_base"]
            md.append(f"- В базе нет, но есть в данных веб-помощника вне базы: `{c['helper_id']}` «{c['name']}» ({c['source']})")
            diffs = it["differences_vs_candidate"]
            md.append(f"  - совпадает полей: {it['matched_vs_candidate']}; отличий: {sum(d['kind'] == 'different' for d in diffs)}; "
                      f"есть только с одной стороны: {sum(d['kind'] == 'only_one_side' for d in diffs)}")
            md += [f"  - {d['field']}: в сценарии {d['scenario'] or '—'}, там {d['other'] or '—'}" for d in diffs]
        if it["flags"]:
            md.append(f"- Пометки: {', '.join(it['flags'])} — {it['notes']}")
        md.append("")
    (out_dir / "proposal.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
