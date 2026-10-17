"""Aggregate layer-3 reviewer results with layer-2 statuses into per-section verdicts.

Inputs: entries.json (layer 2), review result JSONL files (layer 3).
Output: semantic_review.json with every reviewed item and a per-kind summary
combining layer-2 matches (not re-reviewed) with layer-3 verdicts, plus the
control-sample agreement rate for layer-2 matches.

Usage: python aggregate_review.py --entries <entries.json> --results <r1.jsonl> [...] --out <semantic_review.json>
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entries", type=Path, required=True)
    ap.add_argument("--results", type=Path, nargs="+", required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    layer2 = json.loads(a.entries.read_text(encoding="utf-8"))["entries"]
    reviewed: dict[tuple[str, str], dict] = {}
    for f in a.results:
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                reviewed[(r["kind"], r["id"])] = r
    summary: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    control = collections.Counter()
    for e in layer2:
        key = (e["kind"], e["id"])
        if e["status"] == "other_source":
            summary[e["kind"]]["other_source"] += 1
        elif key in reviewed:
            v = reviewed[key]["verdict"]
            summary[e["kind"]][v] += 1
            if reviewed[key].get("reason") == "control_match":
                control[v] += 1
        elif e["status"] == "match":
            summary[e["kind"]]["ok_auto"] += 1
        else:
            summary[e["kind"]]["unchecked_" + e["status"]] += 1
    out = {
        "summary": {k: dict(v) for k, v in summary.items()},
        "control_sample": dict(control),
        "items": sorted(reviewed.values(), key=lambda r: (r["kind"], r["verdict"], r["id"])),
    }
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for k, v in out["summary"].items():
        print(k, v)
    print("control sample:", dict(control))


if __name__ == "__main__":
    main()
