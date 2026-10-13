"""Read-only: check method-family INPUT_HASHES without the Tesseract presence check,
hash osd.traineddata, and summarize the first-pass 001-020 page routes.

Usage: python -I static_pins.py <sourcefold_root> <tessdata_dir>
"""
import hashlib
import json
import sys
from pathlib import Path

SF = Path(sys.argv[1])
TESSDATA = Path(sys.argv[2])
sys.path[:0] = [str(SF.parent), str(SF), str(SF / "scripts")]

import build_core_0_1_text_extraction_012_016_020_method_family as mf  # noqa: E402


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


ok = bad = 0
for key, (path, expected) in mf.INPUT_HASHES.items():
    actual = sha(path)
    if actual == expected:
        ok += 1
    else:
        bad += 1
        print("MISMATCH", key, actual, expected)
print(f"method_family INPUT_HASHES: {ok} match, {bad} mismatch")
print("osd.traineddata", sha(TESSDATA / "osd.traineddata"))

trial = SF / "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001"
for report in sorted(trial.glob("*first_pass*/*report.json")):
    data = json.loads(report.read_text(encoding="utf-8-sig"))
    keys = [k for k in data if any(s in k for s in ("fresh", "bridge", "selected", "pages", "first_pass", "production"))]
    print("==", report.relative_to(SF).as_posix())
    for k in keys:
        v = data[k]
        if isinstance(v, (list, bool, str, int)) and len(json.dumps(v)) < 220:
            print(f"  {k}: {json.dumps(v)}")
