import json, sys, collections
old = {(e["kind"], e["id"]): e for e in json.load(open(sys.argv[1], encoding="utf-8"))["entries"]}
new = {(e["kind"], e["id"]): e for e in json.load(open(sys.argv[2], encoding="utf-8"))["entries"]}
rev = json.load(open(sys.argv[3], encoding="utf-8"))
reviewed = {(i["kind"], i["id"]) for i in rev["items"]}
t = collections.Counter(); todo = []
for k, o in old.items():
    if o["status"] == "unverifiable_page_text":
        n = new[k]["status"]
        t[(k[0], n)] += 1
        if n != "match" and k not in reviewed:
            todo.append(new[k])
for (kind, st), c in sorted(t.items()): print(kind, st, c)
print("need layer-3 review:", len(todo))
for e in todo: print("  ", e["kind"], e["id"], e["status"], e.get("page"), e.get("missing_numbers"))
json.dump(todo, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
