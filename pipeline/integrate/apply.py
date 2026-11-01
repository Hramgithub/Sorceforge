"""Apply proposal files to kb records (Р-139): the edits that extraction agents propose for records they do not own.

Each proposal changes one field of one record (format: schemas/proposal.schema.json, guide: pipeline/integrate/README.md).
Every change of a value is written to the record's `corrections` (field, from, to, reason, ref) unless the proposal
says `"correction": false`. Proposals are applied in order; a proposal that does not fit (no such record, the text to
replace is not there or is there twice, nothing matches) stops the run before anything is written, so a file is applied
whole or not at all. The changed records are then checked with tools/check.py.

Usage: python pipeline/integrate/apply.py <proposals.json> [...] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import ROOT, SCHEMAS, index, read, write  # noqa: E402
from validate import Validator  # noqa: E402


class Misfit(Exception):
    pass


def short(v) -> str | int | float | None:
    """A value as it is written to `corrections`: text and numbers as they are, the rest as short JSON."""
    if v is None or isinstance(v, (str, int, float)) and not isinstance(v, bool):
        return v
    if isinstance(v, dict):
        for k in ("id", "location", "title", "name"):
            if isinstance(v.get(k), str):
                return v[k]
    return json.dumps(v, ensure_ascii=False)


def walk(rec, path: str):
    """The container that holds the last step of the path, and that step (a key or a list index)."""
    steps = [int(s) if s.isdigit() else s for s in path.split(".")]
    node = rec
    for s in steps[:-1]:
        try:
            node = node[s]
        except (KeyError, IndexError, TypeError):
            raise Misfit(f"нет поля {path}")
    return node, steps[-1]


def apply_one(rec, p) -> tuple | None:
    """Change the record; return (field, from, to) for `corrections`."""
    node, last = walk(rec, p["path"])
    op = p["op"]
    if op == "set":
        old = node.get(last) if isinstance(node, dict) else node[last]
        if isinstance(node, dict) and last not in node and p.get("after") and node is rec:
            items = list(rec.items())
            at = next((i for i, (k, _) in enumerate(items) if k == p["after"]), None)
            if at is None:
                raise Misfit(f"нет поля {p['after']} для «after»")
            items.insert(at + 1, (last, p["value"]))
            rec.clear()
            rec.update(items)
        else:
            node[last] = p["value"]
        return p["path"], short(old), short(p["value"])
    if op == "append":
        lst = node.setdefault(last, []) if isinstance(node, dict) else node[last]
        if not isinstance(lst, list):
            raise Misfit(f"{p['path']} — не список")
        if p["value"] in lst:
            return None
        lst.append(p["value"])
        return p["path"], None, short(p["value"])
    if op == "remove":
        lst = node.get(last) if isinstance(node, dict) else node[last]
        m = p.get("match") or {}
        gone = [x for x in lst or [] if isinstance(x, dict) and all(x.get(k) == v for k, v in m.items()) or x == m.get("value", object())]
        if not gone:
            raise Misfit(f"в {p['path']} нет элемента {json.dumps(m, ensure_ascii=False)}")
        node[last] = [x for x in lst if x not in gone]
        return p["path"], "; ".join(str(short(x)) for x in gone), None
    if op == "replace":
        text = node.get(last) if isinstance(node, dict) else node[last]
        if not isinstance(text, str):
            raise Misfit(f"{p['path']} — не текст")
        n = text.count(p["old"])
        if n != 1:
            raise Misfit(f"в {p['path']} кусок «{p['old'][:60]}» встречается {n} раз, нужно ровно 1")
        node[last] = text.replace(p["old"], p["new"])
        return p["path"], p["old"], p["new"]
    raise Misfit(f"неизвестная операция {op}")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    where = index()
    shape = Validator(SCHEMAS / "proposal.schema.json")
    touched: dict[str, dict] = {}
    done = skipped = 0
    for f in a.files:
        doc = read(f)
        errs = shape.validate(doc)
        if errs:
            print(f"{f}: файл предложений не по схеме:\n  " + "\n  ".join(errs))
            return 1
        for i, p in enumerate(doc["proposals"]):
            if p["target"] not in where:
                print(f"{f} #{i}: нет записи {p['target']}")
                return 1
            rec = touched.setdefault(p["target"], read(where[p["target"]]))
            try:
                change = apply_one(rec, p)
            except Misfit as e:
                print(f"{f} #{i} ({p['target']}): {e}")
                return 1
            if change is None:
                skipped += 1
                continue
            done += 1
            if p.get("correction", True):
                field, frm, to = change
                rec.setdefault("corrections", []).append({"field": field, "from": frm, "to": to, "reason": p["reason"], "ref": p.get("ref")})
    print(f"правок: {done}, уже было: {skipped}, записей: {len(touched)}" + (" (пробный прогон, ничего не записано)" if a.dry_run else ""))
    if a.dry_run or not touched:
        return 0
    paths = [where[i] for i in touched]
    for i, rec in touched.items():
        write(where[i], rec)
    return subprocess.run([sys.executable, str(ROOT / "tools/check.py"), *map(str, paths)]).returncode


if __name__ == "__main__":
    sys.exit(main())
