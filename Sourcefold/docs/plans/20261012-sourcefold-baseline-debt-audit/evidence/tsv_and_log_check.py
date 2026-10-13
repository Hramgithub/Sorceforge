import hashlib, json, subprocess, sys
rows = json.load(open(sys.argv[1], encoding="utf-8"))["rows"]
nri = sys.argv[2]
ok = bad = 0
for r in rows:
    if r["class"] != "lf_sealed":
        continue
    b = subprocess.run(["git", "-C", nri, "show", "22fafc14:" + r["path"]], capture_output=True).stdout
    if hashlib.sha256(b).hexdigest().upper() == r["lf_sha256"] and b"\r" not in b:
        ok += 1
    else:
        bad += 1
print("NRI blob == LF seal identity:", ok, "mismatch:", bad)
import pathlib
root = pathlib.Path(sys.argv[3])
d = root / "Sourcefold/fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_benchmark_OBR-G1-VIRAL-002"
man = (d / "ocr_output_manifest.md").read_text(encoding="utf-8")
for i in range(1, 6):
    for f in sorted((d / "raw_outputs").glob(f"GS-G1-VIRAL-00{i}*log*")):
        data = f.read_bytes()
        lf = data.replace(b"\r\n", b"\n")
        forms = {"raw": data, "lf": lf, "crlf": lf.replace(b"\n", b"\r\n")}
        hit = [k for k, v in forms.items() if hashlib.sha256(v).hexdigest().upper() in man]
        print(f.name, "matches manifest as:", hit or "none")
