from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from difflib import SequenceMatcher
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_text_extraction_smoke_p010_trim_mask_psm4.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_smoke_p010_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P010_ROOT = TRIAL_ROOT / "page_complete_review_p010_G1_VIRAL_001" / "review_assets"
P009_REMEDIATION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001"
OUTPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

SMOKE_ID = "C01TESP010-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P010-TRIM-MASK-PSM4-001"
HUMAN_DECISION = "ок. пошли делать 010"
SOURCE_REMEDIATION_ID = "C01TESRM-G1-VIRAL-001"
SELECTED_CANDIDATE_ID = "trim_mask_psm4"
SELECTED_VARIANT = "edge_mask_trim"
SELECTED_PSM = 4

INPUTS = {
    "upper_left_peter_continuation_gear_text_evidence": P010_ROOT
    / "1b_P010-upper-left-continuation-gear-text-evidence.png",
    "lower_left_hyeon_profile_text_evidence": P010_ROOT / "5b_P010-lower-left-hyeon-profile-text-evidence.png",
    "upper_right_hyeon_continuation_appearance_gear_text_evidence": P010_ROOT
    / "2b_P010-upper-right-continuation-appearance-gear-text-evidence.png",
    "lower_right_maya_profile_text_evidence": P010_ROOT / "6b_P010-lower-right-maya-profile-text-evidence.png",
}
REFERENCE_TEXT_MAP = P010_ROOT / "page_010_ocr_verified_text_map.md"
REFERENCE_SEMANTIC_MAP = P010_ROOT / "page_010_semantic_text_map.md"
REFERENCE_SEMANTIC_JSON = P010_ROOT / "page_010_semantic_text_map.json"
FULL_PAGE_IMAGE = P010_ROOT / "page_010.png"
P009_REMEDIATION_REPORT = P009_REMEDIATION_ROOT / "remediation_report.json"
P009_REMEDIATION_SUMMARY = P009_REMEDIATION_ROOT / "remediation_summary.md"
P009_REMEDIATION_MANIFEST = P009_REMEDIATION_ROOT / "remediation_manifest.md"
P009_REMEDIATION_RANKINGS = P009_REMEDIATION_ROOT / "variant_rankings.json"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def check_authorization(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build bounded P010 same-profile OCR smoke outputs.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 P010 same-profile OCR smoke is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 P010 same-profile OCR smoke requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 P010 same-profile OCR smoke requires the exact bounded human decision")
    return args


def verify_inputs() -> dict[str, dict[str, str]]:
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"Refusing to overwrite existing candidate output directory: {OUTPUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"Missing OCR executable: {TESSERACT}")

    remediation = read_json(P009_REMEDIATION_REPORT)
    if remediation["matrix_id"] != SOURCE_REMEDIATION_ID:
        raise SystemExit("unexpected source remediation id")
    if remediation["page"] != "009" or remediation["page_021_plus_included"]:
        raise SystemExit("source remediation is not bounded to P009 only")
    if remediation["accepted_text_mutation_performed"] or remediation["source_or_raw_mutation_performed"]:
        raise SystemExit("source remediation mutation boundary is not clean")
    if SELECTED_CANDIDATE_ID not in {item["candidate_id"] for item in remediation["candidate_results"]}:
        raise SystemExit("selected P009 remediation candidate is missing")

    paths = {
        "source_remediation_report": P009_REMEDIATION_REPORT,
        "source_remediation_summary": P009_REMEDIATION_SUMMARY,
        "source_remediation_manifest": P009_REMEDIATION_MANIFEST,
        "source_remediation_rankings": P009_REMEDIATION_RANKINGS,
        "reference_ocr_verified_text_map": REFERENCE_TEXT_MAP,
        "reference_semantic_map": REFERENCE_SEMANTIC_MAP,
        "reference_semantic_json": REFERENCE_SEMANTIC_JSON,
        "full_page_image_read_only": FULL_PAGE_IMAGE,
        **{f"p010_input_{key}": path for key, path in INPUTS.items()},
    }
    verified: dict[str, dict[str, str]] = {}
    for key, path in paths.items():
        if not path.exists():
            raise SystemExit(f"missing input: {path}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
    return verified


def normalize_text(text: str) -> str:
    text = text.replace("\f", " ")
    text = text.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def metric_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", normalize_text(text).lower()).strip()


def extract_reference_text() -> str:
    source = REFERENCE_TEXT_MAP.read_text(encoding="utf-8-sig")
    blocks = re.findall(r"```text\n(.*?)\n```", source, flags=re.DOTALL)
    return "\n\n".join(block.strip() for block in blocks if block.strip())


def similarity_ratio(candidate: str, reference: str) -> float:
    return SequenceMatcher(None, metric_text(candidate), metric_text(reference)).ratio()


def token_recall(candidate: str, reference: str) -> float:
    candidate_tokens = set(metric_text(candidate).split())
    reference_tokens = metric_text(reference).split()
    if not reference_tokens:
        return 1.0
    return sum(1 for token in reference_tokens if token in candidate_tokens) / len(reference_tokens)


def transform_trim_mask(source: Image.Image) -> Image.Image:
    image = source.convert("RGB")
    trimmed = image.crop((12, 12, image.width - 12, image.height - 12))
    canvas = Image.new("RGB", (trimmed.width + 24, trimmed.height + 24), "white")
    canvas.paste(trimmed, (12, 12))
    return ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB")


def run_tesseract(image_path: Path, output_base: Path) -> dict[str, str | int]:
    output_base.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(TESSERACT),
        str(image_path),
        str(output_base),
        "-l",
        "eng",
        "--oem",
        "1",
        "--psm",
        str(SELECTED_PSM),
        "txt",
        "tsv",
    ]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    write_text(output_base.with_suffix(".stderr.txt"), completed.stderr)
    write_text(output_base.with_suffix(".stdout.txt"), completed.stdout)
    write_text(output_base.with_suffix(".log.txt"), " ".join(command) + f"\nexit_code={completed.returncode}\n")
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout)
    return {
        "command": " ".join(command),
        "exit_code": completed.returncode,
        "stdout_path": output_base.with_suffix(".stdout.txt").relative_to(ROOT).as_posix(),
        "stderr_path": output_base.with_suffix(".stderr.txt").relative_to(ROOT).as_posix(),
        "log_path": output_base.with_suffix(".log.txt").relative_to(ROOT).as_posix(),
    }


def build_candidate(reference_text: str) -> dict:
    chunks: list[str] = []
    raw_outputs: list[dict] = []
    for input_id, input_path in INPUTS.items():
        prepared_path = OUTPUT_ROOT / "prepared_inputs" / SELECTED_CANDIDATE_ID / f"{input_id}.png"
        prepared_path.parent.mkdir(parents=True, exist_ok=True)
        transform_trim_mask(Image.open(input_path)).save(prepared_path)

        output_base = OUTPUT_ROOT / "raw_ocr" / SELECTED_CANDIDATE_ID / input_id
        command_record = run_tesseract(prepared_path, output_base)
        txt_path = output_base.with_suffix(".txt")
        tsv_path = output_base.with_suffix(".tsv")
        text = txt_path.read_text(encoding="utf-8", errors="replace")
        chunks.append(f"## {input_id}\n\n```text\n{text.strip()}\n```")
        raw_outputs.append(
            {
                "input_id": input_id,
                "source_input_path": input_path.relative_to(ROOT).as_posix(),
                "source_input_sha256": sha256_file(input_path),
                "prepared_input_path": prepared_path.relative_to(ROOT).as_posix(),
                "prepared_input_sha256": sha256_file(prepared_path),
                "txt_path": txt_path.relative_to(ROOT).as_posix(),
                "txt_sha256": sha256_file(txt_path),
                "tsv_path": tsv_path.relative_to(ROOT).as_posix(),
                "tsv_sha256": sha256_file(tsv_path),
                "stderr_sha256": sha256_file(output_base.with_suffix(".stderr.txt")),
                "stdout_sha256": sha256_file(output_base.with_suffix(".stdout.txt")),
                "log_sha256": sha256_file(output_base.with_suffix(".log.txt")),
                "command": command_record["command"],
            }
        )

    candidate_text = "\n\n".join(chunks).strip() + "\n"
    normalized = normalize_text(re.sub(r"```text|```|## [^\n]+", " ", candidate_text))
    candidate_dir = OUTPUT_ROOT / "candidate_texts"
    candidate_text_path = candidate_dir / f"{SELECTED_CANDIDATE_ID}.md"
    normalized_text_path = candidate_dir / f"{SELECTED_CANDIDATE_ID}.normalized.txt"
    write_text(candidate_text_path, "# Candidate OCR Text - P010\n\n" + candidate_text)
    write_text(normalized_text_path, normalized + "\n")
    return {
        "candidate_id": SELECTED_CANDIDATE_ID,
        "strategy": "full_column",
        "variant": SELECTED_VARIANT,
        "psm": SELECTED_PSM,
        "raw_outputs": raw_outputs,
        "candidate_text_path": candidate_text_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_text_path),
        "normalized_text_path": normalized_text_path.relative_to(ROOT).as_posix(),
        "normalized_text_sha256": sha256_file(normalized_text_path),
        "metrics": {
            "sequence_similarity_ratio": round(similarity_ratio(normalized, reference_text), 6),
            "token_recall": round(token_recall(normalized, reference_text), 6),
            "normalized_candidate_chars": len(normalized),
            "reference_chars": len(normalize_text(reference_text)),
        },
    }


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
    reference_text = extract_reference_text()
    candidate = build_candidate(reference_text)

    report = {
        "smoke_id": SMOKE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_p010_same_profile_smoke_completed",
        "source_remediation": SOURCE_REMEDIATION_ID,
        "source_selected_candidate": SELECTED_CANDIDATE_ID,
        "page": "010",
        "page_021_plus_included": False,
        "candidate_count": 1,
        "candidate_id": SELECTED_CANDIDATE_ID,
        "variant": SELECTED_VARIANT,
        "psm": SELECTED_PSM,
        "ocr_execution_performed": True,
        "pdf_parsing_performed": False,
        "pdf_text_layer_extraction_performed": False,
        "render_execution_performed": False,
        "source_or_raw_mutation_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "runtime_implementation_created": False,
        "runtime_start_performed": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "input_policy": "read_only_existing_p010_text_evidence_crops",
        "output_policy": "candidate_only_separate_same_profile_directory",
        "reference_text_map": verified_inputs["reference_ocr_verified_text_map"],
        "verified_inputs": verified_inputs,
        "candidate_result": candidate,
        "metrics": candidate["metrics"],
        "recommendation": "compare_same_profile_generalization_before_any_broader_extraction",
    }
    write_json(OUTPUT_ROOT / "smoke_report.json", report)

    summary = [
        "# Core 0.1 P010 Same-Profile OCR Smoke",
        "",
        f"Smoke id: `{SMOKE_ID}`",
        "",
        "Status: `candidate_only_p010_same_profile_smoke_completed`",
        "",
        "Boundary: P010-only candidate evidence over read-only text-evidence crop PNGs.",
        "",
        f"Source selected profile: `{SOURCE_REMEDIATION_ID}` / `{SELECTED_CANDIDATE_ID}`.",
        f"Variant: `{SELECTED_VARIANT}`.",
        f"PSM: `{SELECTED_PSM}`.",
        f"Similarity against P010 verified text map: `{candidate['metrics']['sequence_similarity_ratio']}`.",
        f"Token recall: `{candidate['metrics']['token_recall']}`.",
        "",
        "Preserved limits:",
        "",
        "- No P010 source/review/reference/accepted-text overwrite.",
        "- No semantic text or page-status mutation.",
        "- No page 021+ processing or authorization.",
        "- No PDF parsing/text-layer extraction.",
        "- No render execution.",
        "- No runtime implementation/start.",
        "- No translation/proofreading/push.",
        "",
    ]
    write_text(OUTPUT_ROOT / "smoke_summary.md", "\n".join(summary))

    manifest_lines = [
        "# Core 0.1 P010 Same-Profile OCR Smoke Manifest",
        "",
        f"Smoke id: `{SMOKE_ID}`",
        "",
        "Boundary: candidate-only P010 same-profile OCR smoke outputs; no source/review/reference asset is overwritten.",
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
