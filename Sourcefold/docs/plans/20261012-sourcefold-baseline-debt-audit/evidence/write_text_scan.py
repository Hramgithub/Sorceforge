import ast, sys, pathlib
root = pathlib.Path(sys.argv[1])
hits = {}
for p in sorted(root.glob("*.py")):
    tree = ast.parse(p.read_text(encoding="utf-8-sig"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "write_text":
            if not any(k.arg == "newline" for k in node.keywords):
                hits.setdefault(p.name, []).append(node.lineno)
print(len(hits), "of", len(list(root.glob("*.py"))))
for k, v in hits.items():
    print(k, v)
