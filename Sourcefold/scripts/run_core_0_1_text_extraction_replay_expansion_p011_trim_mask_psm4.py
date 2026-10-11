from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from difflib import SequenceMatcher
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "run_core_0_1_text_extraction_replay_expansion_p011_trim_mask_psm4.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_replay_expansion_p011_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
CONFIG_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_frozen_profile_config_G1_VIRAL_001"
P011_ROOT = TRIAL_ROOT / "page_complete_review_p011_G1_VIRAL_001" / "review_assets"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_replay_expansion_p011_trim_mask_psm4_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

EXPANSION_ID = "C01TEREP011-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REPLAY-EXPANSION-P011-TRIM-MASK-PSM4-001"
HUMAN_DECISION = "bounded replay expansion внутри 001-020"
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

P011_SPEC = {
    "page": "011",
    "root": P011_ROOT,
    "reference_label": "reference_ocr_verified_text_map",
    "reference": "page_011_ocr_verified_text_map.md",
    "inputs": [
        ("left_maya_continuation_secret_appearance", "1b_P011-left-maya-continuation-secret-appearance-text-evidence.png"),
        ("right_emily_profile_text", "4b_P011-right-emily-profile-text-text-evidence.png"),
    ],
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run P011-only Core 0.1 replay expansion smoke.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P011 replay expansion is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P011 replay expansion requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P011 replay expansion requires the exact bounded human decision")


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

    reference = P011_ROOT / P011_SPEC["reference"]
    if not reference.exists():
        raise SystemExit(f"missing P011 reference: {reference}")
    verified["p011_reference_ocr_verified_text_map"] = {
        "path": reference.relative_to(ROOT).as_posix(),
        "sha256": sha256_file(reference),
    }
    for input_id, filename in P011_SPEC["inputs"]:
        input_path = P011_ROOT / filename
        if not input_path.exists():
            raise SystemExit(f"missing P011 input: {input_path}")
        verified[f"p011_input_{input_id}"] = {
            "path": input_path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(input_path),
        }
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


def run_tesseract(input_path: Path, input_id: str, psm: int, scratch_root: Path) -> tuple[str, dict]:
    prepared_path = scratch_root / "prepared" / f"{input_id}.png"
    prepared_path.parent.mkdir(parents=True, exist_ok=True)
    transform_trim_mask(Image.open(input_path)).save(prepared_path)
    output_base = scratch_root / "ocr" / input_id
    output_base.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(TESSERACT),
        str(prepared_path),
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
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout)
    txt_path = output_base.with_suffix(".txt")
    tsv_path = output_base.with_suffix(".tsv")
    text = txt_path.read_text(encoding="utf-8", errors="replace")
    return text, {
        "input_id": input_id,
        "source_input_path": input_path.relative_to(ROOT).as_posix(),
        "source_input_sha256": sha256_file(input_path),
        "scratch_outputs_persisted": False,
        "ocr_text_sha256": sha256_text(text),
        "ocr_tsv_sha256": sha256_file(tsv_path),
        "stderr_sha256": sha256_text(completed.stderr),
        "stdout_sha256": sha256_text(completed.stdout),
        "command_profile": "tesseract -l eng --oem 1 --psm 4 txt tsv",
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
    reference_path = P011_ROOT / P011_SPEC["reference"]
    reference_text = extract_reference_text(reference_path)
    chunks = []
    input_results = []
    with tempfile.TemporaryDirectory(prefix="sourcefold_p011_replay_expansion_") as scratch:
        scratch_root = Path(scratch)
        for input_id, filename in P011_SPEC["inputs"]:
            text, input_result = run_tesseract(P011_ROOT / filename, input_id, config["profile_tuple"]["tesseract_psm"], scratch_root)
            chunks.append(f"## {input_id}\n\n{text.strip()}")
            input_results.append(input_result)

    candidate_text = "\n\n".join(chunks).strip() + "\n"
    normalized = normalize_text(candidate_text)
    metrics = {
        "sequence_similarity_ratio": round(similarity_ratio(normalized, reference_text), 6),
        "token_recall": round(token_recall(normalized, reference_text), 6),
        "normalized_candidate_chars": len(normalized),
        "reference_chars": len(normalize_text(reference_text)),
    }
    report = {
        "expansion_id": EXPANSION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_replay_expansion_p011_completed",
        "source_frozen_profile_config": CONFIG_ID,
        "frozen_config_tuple_reused_only": True,
        "frozen_config_allowed_pages_not_broadened": True,
        "profile_id": PROFILE_ID,
        "profile_tuple": config["profile_tuple"],
        "pages": ["011"],
        "candidate_count": 1,
        "input_count": 2,
        "output_artifact_policy": "report_summary_manifest_metrics_only",
        "raw_ocr_artifacts_persisted": False,
        "prepared_input_artifacts_persisted": False,
        "candidate_text_artifacts_persisted": False,
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
        "page_012_plus_included": False,
        "page_016_plus_included": False,
        "page_021_plus_included": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "verified_inputs": verified_inputs,
        "page_result": {
            "page": "011",
            "reference_label": P011_SPEC["reference_label"],
            "reference_text_map": reference_path.relative_to(ROOT).as_posix(),
            "input_count": len(P011_SPEC["inputs"]),
            "candidate_text_sha256": sha256_text(candidate_text),
            "normalized_text_sha256": sha256_text(normalized + "\n"),
            "input_results": input_results,
            "metrics": metrics,
        },
        "aggregate_metrics": {
            "page_count": 1,
            "input_count": 2,
            "min_sequence_similarity_ratio": metrics["sequence_similarity_ratio"],
            "min_token_recall": metrics["token_recall"],
        },
        "recommendation": "p011_expansion_complete_decide_next_single_page_expansion_or_runtime_design",
    }
    write_json(OUT_ROOT / "replay_expansion_report.json", report)
    summary_lines = [
        "# Core 0.1 Text Extraction Replay Expansion - P011 - C01TEREP011-G1-VIRAL-001",
        "",
        "Status: `candidate_only_replay_expansion_p011_completed`",
        "",
        "This layer reuses only the frozen profile tuple from `C01TEFPC-G1-VIRAL-001`; it does not broaden the config allowed-pages policy.",
        "",
        "| Page | Reference | Inputs | Similarity | Token recall |",
        "|---|---|---:|---:|---:|",
        f"| `011` | `{P011_SPEC['reference_label']}` | `2` | `{metrics['sequence_similarity_ratio']}` | `{metrics['token_recall']}` |",
        "",
        "Boundary: candidate-only metrics/report/summary/manifest; no persisted raw OCR, prepared input, or candidate text artifacts.",
        "No accepted/semantic/source/page-status mutation, no PDF/render/runtime/page 012+/page 021+/push.",
        "",
    ]
    write_text(OUT_ROOT / "replay_expansion_summary.md", "\n".join(summary_lines))
    manifest_lines = [
        "# Core 0.1 Text Extraction Replay Expansion Manifest - P011 - C01TEREP011-G1-VIRAL-001",
        "",
        "Boundary: candidate-only metrics/report/summary/manifest outputs.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "replay_expansion_manifest.md":
            manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "replay_expansion_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
