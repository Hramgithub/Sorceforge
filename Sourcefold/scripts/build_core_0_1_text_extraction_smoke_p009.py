from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_text_extraction_smoke_p009.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_smoke_p009.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P009_ROOT = TRIAL_ROOT / "page_complete_review_p009_G1_VIRAL_001" / "review_assets"
OUTPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p009_G1_VIRAL_001"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")
OCR_MANIFEST = TRIAL_ROOT / "ocr_candidate_manifest.md"
SOURCE_DECISION = TRIAL_ROOT / "c01tetd_G1_VIRAL_001" / "c01tetd.json"
SOURCE_DECISION_REPORT = TRIAL_ROOT / "c01tetd_G1_VIRAL_001" / "c01tetd_report.json"
SOURCE_DECISION_SUMMARY = TRIAL_ROOT / "c01tetd_G1_VIRAL_001" / "c01tetd_summary.md"
SOURCE_DECISION_MANIFEST = TRIAL_ROOT / "c01tetd_G1_VIRAL_001" / "c01tetd_manifest.md"

SMOKE_ID = "C01TESP-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-001"
HUMAN_DECISION = "теперь согласен, приступай"
OCR_CANDIDATE_ID = "OCR-G1-VIRAL-TESSERACT-ENG-PSM6-001"

INPUTS = {
    "left_profile_text_evidence": P009_ROOT / "3b_P009-left-profile-text-column-text-evidence.png",
    "right_profile_text_evidence": P009_ROOT / "4b_P009-right-profile-text-column-text-evidence.png",
}
REFERENCE_TEXT_MAP = P009_ROOT / "page_009_ocr_verified_text_map.md"
REFERENCE_SEMANTIC_MAP = P009_ROOT / "page_009_semantic_text_map.md"
REFERENCE_SEMANTIC_JSON = P009_ROOT / "page_009_semantic_text_map.json"
FULL_PAGE_IMAGE = P009_ROOT / "page_009.png"

SOURCE_HASH_INPUTS = {
    "C01TETD-G1-VIRAL-001.decision": SOURCE_DECISION,
    "C01TETD-G1-VIRAL-001.report": SOURCE_DECISION_REPORT,
    "C01TETD-G1-VIRAL-001.summary": SOURCE_DECISION_SUMMARY,
    "C01TETD-G1-VIRAL-001.manifest": SOURCE_DECISION_MANIFEST,
    "OCM-G1-VIRAL-001.ocr_candidate_manifest": OCR_MANIFEST,
    "P009.reference_ocr_verified_text_map": REFERENCE_TEXT_MAP,
    "P009.reference_semantic_map": REFERENCE_SEMANTIC_MAP,
    "P009.reference_semantic_json": REFERENCE_SEMANTIC_JSON,
    "P009.full_page_image_read_only": FULL_PAGE_IMAGE,
    **{f"P009.{key}": path for key, path in INPUTS.items()},
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def check_authorization(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Core 0.1 P009 text extraction smoke candidate outputs.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 P009 text extraction smoke is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 P009 text extraction smoke requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 P009 text extraction smoke requires the exact bounded human decision")
    return args


def verify_inputs() -> dict[str, dict[str, str]]:
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"Refusing to overwrite existing candidate output directory: {OUTPUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"Missing frozen OCR executable: {TESSERACT}")

    decision = read_json(SOURCE_DECISION)
    if decision["decision_id"] != "C01TETD-G1-VIRAL-001":
        raise SystemExit("unexpected source decision")
    if not decision["requires_bogdan_call_before_point_6"]:
        raise SystemExit("source decision does not require Bogdan call before point 6")
    if decision["scope"]["page_021_plus_included"]:
        raise SystemExit("source decision unexpectedly includes page 021+")

    manifest_text = OCR_MANIFEST.read_text(encoding="utf-8-sig")
    required_manifest_tokens = [
        "Manifest id: `OCM-G1-VIRAL-001`",
        "Status: `candidate_config_frozen_for_review`",
        f"Candidate id: `{OCR_CANDIDATE_ID}`",
        r"D:\NRI\.tools\tesseract\tesseract.exe",
        "- Language: `eng`",
        "- OEM: `1`",
        "- PSM: `6`",
    ]
    for token in required_manifest_tokens:
        if token not in manifest_text:
            raise SystemExit(f"OCR candidate manifest missing token: {token}")

    verified: dict[str, dict[str, str]] = {}
    for key, path in SOURCE_HASH_INPUTS.items():
        if not path.exists():
            raise SystemExit(f"missing input: {path}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
    return verified


def run_tesseract(input_path: Path, output_base: Path) -> dict[str, str]:
    output_base.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(TESSERACT),
        str(input_path),
        str(output_base),
        "-l",
        "eng",
        "--oem",
        "1",
        "--psm",
        "6",
        "txt",
        "tsv",
    ]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout)
    return {"stdout": completed.stdout, "stderr": completed.stderr, "command": " ".join(command)}


def normalize_text(text: str) -> str:
    text = text.replace("\f", " ")
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_reference_text() -> str:
    source = REFERENCE_TEXT_MAP.read_text(encoding="utf-8-sig")
    blocks = re.findall(r"```text\n(.*?)\n```", source, flags=re.DOTALL)
    return "\n\n".join(block.strip() for block in blocks if block.strip())


def similarity_ratio(candidate: str, reference: str) -> float:
    return SequenceMatcher(None, normalize_text(candidate).lower(), normalize_text(reference).lower()).ratio()


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file():
            hashes[path.relative_to(OUTPUT_ROOT).as_posix()] = {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
    return hashes


def build() -> None:
    verified_inputs = verify_inputs()
    OUTPUT_ROOT.mkdir(parents=True)

    raw_results: dict[str, dict[str, str]] = {}
    combined_parts: list[str] = []
    command_records: list[dict[str, str]] = []
    for key, input_path in INPUTS.items():
        output_base = OUTPUT_ROOT / "ocr_raw" / key
        command_record = run_tesseract(input_path, output_base)
        txt_path = output_base.with_suffix(".txt")
        tsv_path = output_base.with_suffix(".tsv")
        raw_text = txt_path.read_text(encoding="utf-8", errors="replace")
        combined_parts.append(f"## {key}\n\n```text\n{raw_text.strip()}\n```\n")
        raw_results[key] = {
            "input_path": input_path.relative_to(ROOT).as_posix(),
            "input_sha256": sha256_file(input_path),
            "txt_path": txt_path.relative_to(ROOT).as_posix(),
            "txt_sha256": sha256_file(txt_path),
            "tsv_path": tsv_path.relative_to(ROOT).as_posix(),
            "tsv_sha256": sha256_file(tsv_path),
        }
        command_records.append(command_record)

    combined_text = "\n".join(combined_parts).strip() + "\n"
    normalized_text = normalize_text("\n".join((OUTPUT_ROOT / "ocr_raw" / key).with_suffix(".txt").read_text(encoding="utf-8", errors="replace") for key in INPUTS))
    reference_text = extract_reference_text()
    ratio = similarity_ratio(normalized_text, reference_text)

    write_text(
        OUTPUT_ROOT / "candidate_text.md",
        "\n".join(
            [
                "# Core 0.1 Text Extraction Smoke Candidate - P009",
                "",
                f"Smoke id: `{SMOKE_ID}`",
                "",
                "Boundary: candidate-only OCR smoke over read-only P009 text-evidence crop PNGs.",
                "",
                combined_text,
            ]
        ),
    )
    write_text(
        OUTPUT_ROOT / "normalized_candidate_text.txt",
        normalized_text + "\n",
    )

    report = {
        "smoke_id": SMOKE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_ocr_smoke_completed_no_source_mutation",
        "source_decision": "C01TETD-G1-VIRAL-001",
        "page": "009",
        "page_021_plus_included": False,
        "ocr_candidate_manifest_id": "OCM-G1-VIRAL-001",
        "ocr_candidate_id": OCR_CANDIDATE_ID,
        "ocr_engine": "Tesseract OCR",
        "ocr_executable": str(TESSERACT),
        "ocr_execution_performed": True,
        "pdf_parsing_performed": False,
        "pdf_text_layer_extraction_performed": False,
        "render_execution_performed": False,
        "source_or_raw_mutation_performed": False,
        "accepted_text_mutation_performed": False,
        "runtime_implementation_created": False,
        "runtime_start_performed": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "input_policy": "read_only_existing_p009_text_evidence_crops",
        "output_policy": "candidate_only_separate_directory",
        "raw_results": raw_results,
        "reference_text_map": verified_inputs["P009.reference_ocr_verified_text_map"],
        "metrics": {
            "normalized_candidate_chars": len(normalized_text),
            "reference_chars": len(normalize_text(reference_text)),
            "sequence_similarity_ratio": round(ratio, 6),
        },
        "commands": command_records,
        "verified_inputs": verified_inputs,
    }
    write_json(OUTPUT_ROOT / "smoke_report.json", report)

    summary_lines = [
        "# Core 0.1 Text Extraction Smoke - P009",
        "",
        f"Smoke id: `{SMOKE_ID}`",
        "",
        "Status: `candidate_ocr_smoke_completed_no_source_mutation`",
        "",
        "This is the first bounded actual OCR smoke over P009 text-evidence crop PNGs.",
        "",
        "Boundary:",
        "",
        "- Inputs: read-only P009 text-evidence crop PNGs.",
        "- Outputs: candidate-only OCR text, TSV, manifest, report, and metrics.",
        "- PDF parsing/text-layer extraction: `false`.",
        "- Render execution: `false`.",
        "- Source/raw/PDF/accepted-text mutation: `false`.",
        "- Runtime implementation/start: `false`.",
        "- Page 021+: `false`.",
        "",
        f"Sequence similarity against the P009 verified text map: `{report['metrics']['sequence_similarity_ratio']}`.",
        "",
    ]
    write_text(OUTPUT_ROOT / "smoke_summary.md", "\n".join(summary_lines))

    manifest_lines = [
        "# Core 0.1 Text Extraction Smoke P009 Manifest - C01TESP-G1-VIRAL-001",
        "",
        "Boundary: candidate-only OCR smoke outputs; no P009 source/review/reference asset is overwritten.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "smoke_manifest.md":
            manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(OUTPUT_ROOT / "smoke_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
