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
SCRIPT_PATH = ROOT / "scripts" / "run_core_0_1_text_extraction_replay_regression_smoke_trim_mask_psm4.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_replay_regression_smoke_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
CONFIG_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_frozen_profile_config_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_replay_regression_smoke_trim_mask_psm4_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

REPLAY_ID = "C01TERSM-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REPLAY-REGRESSION-SMOKE-TRIM-MASK-PSM4-001"
HUMAN_DECISION = "делай"
CONFIG_ID = "C01TEFPC-G1-VIRAL-001"
PROFILE_ID = "trim_mask_psm4"

CONFIG_HASHES = {
    "C01TEFPC-G1-VIRAL-001.config": (
        CONFIG_ROOT / "core_0_1_text_extraction_frozen_profile_config.json",
        "4807057B7F043DC197651CD7DBCA40496FA4CAFCD7F08ECE6A59A306C14D7987",
    ),
    "C01TEFPC-G1-VIRAL-001.report": (
        CONFIG_ROOT / "core_0_1_text_extraction_frozen_profile_config_report.json",
        "993025D6724B8F977CF059A0C6E39F3E7E64A9D85CEECB06C68665FA71F1CD1C",
    ),
    "C01TEFPC-G1-VIRAL-001.summary": (
        CONFIG_ROOT / "core_0_1_text_extraction_frozen_profile_config_summary.md",
        "3A4BC1206451B1778C63823BFB1E35AF009827AA28F5623A1D823B7E68E1B856",
    ),
    "C01TEFPC-G1-VIRAL-001.manifest": (
        CONFIG_ROOT / "core_0_1_text_extraction_frozen_profile_config_manifest.md",
        "A1931595C1276FD77FF0E3FA6771B5A72686319A30D6F4E2C096DF2F9B5AB3FC",
    ),
}

PAGE_SPECS = {
    "009": {
        "root": TRIAL_ROOT / "page_complete_review_p009_G1_VIRAL_001" / "review_assets",
        "reference_label": "reference_ocr_verified_text_map",
        "reference": "page_009_ocr_verified_text_map.md",
        "inputs": [
            ("left_profile_text_column", "3b_P009-left-profile-text-column-text-evidence.png"),
            ("right_profile_text_column", "4b_P009-right-profile-text-column-text-evidence.png"),
        ],
    },
    "010": {
        "root": TRIAL_ROOT / "page_complete_review_p010_G1_VIRAL_001" / "review_assets",
        "reference_label": "reference_ocr_verified_text_map",
        "reference": "page_010_ocr_verified_text_map.md",
        "inputs": [
            ("upper_left_peter_continuation_gear", "1b_P010-upper-left-continuation-gear-text-evidence.png"),
            ("lower_left_hyeon_profile", "5b_P010-lower-left-hyeon-profile-text-evidence.png"),
            ("upper_right_hyeon_continuation_appearance_gear", "2b_P010-upper-right-continuation-appearance-gear-text-evidence.png"),
            ("lower_right_maya_profile", "6b_P010-lower-right-maya-profile-text-evidence.png"),
        ],
    },
    "015": {
        "root": TRIAL_ROOT / "page_complete_review_p015_G1_VIRAL_001" / "review_assets",
        "reference_label": "reference_text_map_not_ocr_verified",
        "reference": "page_015_text_map.md",
        "inputs": [
            ("timeline_text_evidence", "1_P015-timeline-text-evidence.png"),
            ("history_text_evidence", "2_P015-history-text-evidence.png"),
        ],
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run Core 0.1 frozen-profile replay regression smoke.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 replay regression smoke is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 replay regression smoke requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 replay regression smoke requires the exact bounded human decision")


def verify_config_and_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in CONFIG_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    config = read_json(CONFIG_HASHES["C01TEFPC-G1-VIRAL-001.config"][0])
    if config["config_id"] != CONFIG_ID or config["profile_id"] != PROFILE_ID:
        raise SystemExit("unexpected frozen profile config")
    tuple_ = config["profile_tuple"]
    if tuple_["preprocessing_variant"] != "edge_mask_trim" or tuple_["tesseract_psm"] != 4:
        raise SystemExit("frozen config tuple drift")
    if config["ocr_execution_performed"]:
        raise SystemExit("frozen config unexpectedly executed OCR")

    input_count = 0
    for page, spec in PAGE_SPECS.items():
        root = spec["root"]
        reference = root / spec["reference"]
        if not reference.exists():
            raise SystemExit(f"missing reference for P{page}: {reference}")
        verified[f"p{page}_reference_{spec['reference_label']}"] = {
            "path": reference.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(reference),
        }
        for input_id, filename in spec["inputs"]:
            input_path = root / filename
            if not input_path.exists():
                raise SystemExit(f"missing input {input_path}")
            verified[f"p{page}_input_{input_id}"] = {
                "path": input_path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(input_path),
            }
            input_count += 1
    if input_count != 8:
        raise SystemExit(f"expected exactly 8 text-evidence crop inputs, got {input_count}")
    return verified, config


def normalize_text(text: str) -> str:
    text = text.replace("\f", " ")
    text = text.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u00b0", " degrees ")
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def metric_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", normalize_text(text).lower()).strip()


def extract_reference_text(path: Path) -> str:
    source = path.read_text(encoding="utf-8-sig")
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


def run_tesseract(image_path: Path, output_base: Path, psm: int) -> str:
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
        str(psm),
        "txt",
        "tsv",
    ]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    write_text(output_base.with_suffix(".stderr.txt"), completed.stderr)
    write_text(output_base.with_suffix(".stdout.txt"), completed.stdout)
    write_text(output_base.with_suffix(".log.txt"), " ".join(command) + f"\nexit_code={completed.returncode}\n")
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout)
    return " ".join(command)


def replay_page(page: str, spec: dict, config: dict) -> dict:
    tuple_ = config["profile_tuple"]
    root: Path = spec["root"]
    reference_path = root / spec["reference"]
    reference_text = extract_reference_text(reference_path)
    chunks: list[str] = []
    raw_outputs = []
    for input_id, filename in spec["inputs"]:
        input_path = root / filename
        prepared_path = OUT_ROOT / "prepared_inputs" / f"p{page}" / PROFILE_ID / f"{input_id}.png"
        prepared_path.parent.mkdir(parents=True, exist_ok=True)
        transform_trim_mask(Image.open(input_path)).save(prepared_path)
        output_base = OUT_ROOT / "raw_ocr" / f"p{page}" / PROFILE_ID / input_id
        command = run_tesseract(prepared_path, output_base, tuple_["tesseract_psm"])
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
                "command": command,
            }
        )
    candidate_text = "\n\n".join(chunks).strip() + "\n"
    normalized = normalize_text(re.sub(r"```text|```|## [^\n]+", " ", candidate_text))
    candidate_dir = OUT_ROOT / "candidate_texts" / f"p{page}"
    candidate_path = candidate_dir / f"{PROFILE_ID}.md"
    normalized_path = candidate_dir / f"{PROFILE_ID}.normalized.txt"
    write_text(candidate_path, f"# Candidate OCR Replay Text - P{page}\n\n" + candidate_text)
    write_text(normalized_path, normalized + "\n")
    metrics = {
        "sequence_similarity_ratio": round(similarity_ratio(normalized, reference_text), 6),
        "token_recall": round(token_recall(normalized, reference_text), 6),
        "normalized_candidate_chars": len(normalized),
        "reference_chars": len(normalize_text(reference_text)),
    }
    return {
        "page": page,
        "reference_label": spec["reference_label"],
        "reference_text_map": reference_path.relative_to(ROOT).as_posix(),
        "input_count": len(spec["inputs"]),
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_path),
        "normalized_text_path": normalized_path.relative_to(ROOT).as_posix(),
        "normalized_text_sha256": sha256_file(normalized_path),
        "raw_outputs": raw_outputs,
        "metrics": metrics,
    }


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file():
            hashes[path.relative_to(OUT_ROOT).as_posix()] = {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
    return hashes


def build() -> None:
    verified_inputs, config = verify_config_and_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    page_results = [replay_page(page, PAGE_SPECS[page], config) for page in ["009", "010", "015"]]
    aggregate = {
        "page_count": len(page_results),
        "input_count": sum(page["input_count"] for page in page_results),
        "min_sequence_similarity_ratio": min(page["metrics"]["sequence_similarity_ratio"] for page in page_results),
        "min_token_recall": min(page["metrics"]["token_recall"] for page in page_results),
    }
    report = {
        "replay_id": REPLAY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_replay_regression_smoke_completed",
        "source_frozen_profile_config": CONFIG_ID,
        "profile_id": PROFILE_ID,
        "profile_tuple": config["profile_tuple"],
        "pages": ["009", "010", "015"],
        "candidate_count": 1,
        "input_count": 8,
        "old_broad_runner_reused": False,
        "ocr_execution_performed": True,
        "pdf_parsing_performed": False,
        "pdf_text_layer_extraction_performed": False,
        "render_execution_performed": False,
        "source_or_raw_mutation_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_profile_acceptance_created": False,
        "runtime_source_profile_lock_created": False,
        "runtime_implementation_created": False,
        "runtime_start_performed": False,
        "page_016_plus_included": False,
        "page_021_plus_included": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "verified_inputs": verified_inputs,
        "page_results": page_results,
        "aggregate_metrics": aggregate,
        "recommendation": "frozen_profile_replay_reproduced_ladder_prepare_next_bounded_decision",
    }
    write_json(OUT_ROOT / "replay_report.json", report)
    lines = [
        "# Core 0.1 Text Extraction Replay Regression Smoke - C01TERSM-G1-VIRAL-001",
        "",
        "Status: `candidate_only_replay_regression_smoke_completed`",
        "",
        "Replay uses only frozen profile config `C01TEFPC-G1-VIRAL-001`.",
        "",
        "| Page | Reference | Inputs | Similarity | Token recall |",
        "|---|---|---:|---:|---:|",
    ]
    for page in page_results:
        lines.append(
            f"| `{page['page']}` | `{page['reference_label']}` | `{page['input_count']}` | "
            f"`{page['metrics']['sequence_similarity_ratio']}` | `{page['metrics']['token_recall']}` |"
        )
    lines.extend(
        [
            "",
            "Boundary: candidate-only replay; no accepted/semantic/source/page-status mutation, no PDF/render/runtime/page 016+/page 021+/push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "replay_summary.md", "\n".join(lines))
    manifest_lines = [
        "# Core 0.1 Text Extraction Replay Regression Smoke Manifest - C01TERSM-G1-VIRAL-001",
        "",
        "Boundary: candidate-only replay outputs; no accepted/source/runtime mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "replay_manifest.md":
            manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "replay_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
