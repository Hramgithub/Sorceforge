import json, sys
p = sys.argv[1]; out = sys.argv[2]
cars = {"eq-modern-transport-cadillac-suv", "eq-modern-transport-vnedorozhnik-firmy-dodzh", "eq-modern-transport-korvet-kabriolet"}
lines = []
for line in open(p, encoding="utf-8"):
    if not line.strip(): continue
    r = json.loads(line)
    if r["id"] in cars and r["verdict"] == "error":
        r["verdict"] = "minor"
        r["normalized"] = "maxKmh is not in the book (app-derived); graded minor as in batch 1"
    lines.append(json.dumps(r, ensure_ascii=False))
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(len(lines))
