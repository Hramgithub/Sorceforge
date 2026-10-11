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
SCRIPT_PATH = ROOT / "scripts" / "run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
CONFIG_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_frozen_profile_config_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

OVERVIEW_ID = "C01TEOR020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-OVERVIEW-REPLAY-001-020-TRIM-MASK-PSM4-001"
HUMAN_DECISION = "сделай 001-020"
CONFIG_ID = "C01TEFPC-G1-VIRAL-001"
PROFILE_ID = "trim_mask_psm4"
WEAK_SIMILARITY_THRESHOLD = 0.997
WEAK_TOKEN_RECALL_THRESHOLD = 0.993

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

PAGE_DIRS = {
    "001": "page_complete_review_p001_G1_VIRAL_001",
    "002": "page_complete_review_p002_G1_VIRAL_001",
    "003": "page_complete_review_p003_G1_VIRAL_001",
    "004": "page_complete_review_p004_G1_VIRAL_001",
    "005": "page_complete_review_p005_G1_VIRAL_004",
    "006": "page_complete_review_p006_G1_VIRAL_002",
    "007": "page_complete_review_p007_G1_VIRAL_003",
    "008": "page_complete_review_p008_G1_VIRAL_001",
    "009": "page_complete_review_p009_G1_VIRAL_001",
    "010": "page_complete_review_p010_G1_VIRAL_001",
    "011": "page_complete_review_p011_G1_VIRAL_001",
    "012": "page_complete_review_p012_G1_VIRAL_001",
    "013": "page_complete_review_p013_G1_VIRAL_001",
    "014": "page_complete_review_p014_G1_VIRAL_001",
    "015": "page_complete_review_p015_G1_VIRAL_001",
    "016": "page_complete_review_p016_G1_VIRAL_001",
    "017": "page_complete_review_p017_G1_VIRAL_001",
    "018": "page_complete_review_p018_G1_VIRAL_001",
    "019": "page_complete_review_p019_G1_VIRAL_001",
    "020": "page_complete_review_p020_G1_VIRAL_001",
}

INPUT_ORDER_OVERRIDES = {
    "009": [
        "3b_P009-left-profile-text-column-text-evidence.png",
        "4b_P009-right-profile-text-column-text-evidence.png",
    ],
    "010": [
        "1b_P010-upper-left-continuation-gear-text-evidence.png",
        "5b_P010-lower-left-hyeon-profile-text-evidence.png",
        "2b_P010-upper-right-continuation-appearance-gear-text-evidence.png",
        "6b_P010-lower-right-maya-profile-text-evidence.png",
    ],
    "011": [
        "1b_P011-left-maya-continuation-secret-appearance-text-evidence.png",
        "4b_P011-right-emily-profile-text-text-evidence.png",
    ],
    "015": [
        "1_P015-timeline-text-evidence.png",
        "2_P015-history-text-evidence.png",
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
    parser = argparse.ArgumentParser(description="Run 001-020 Core 0.1 overview replay report.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("001-020 overview replay is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"001-020 overview replay requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("001-020 overview replay requires the exact bounded human decision")


def natural_key(path: Path) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def normalize_text(text: str) -> str:
    text = text.replace("\f", " ")
    text = text.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u00b0", " degrees ")
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def metric_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", normalize_text(text).lower()).strip()


def normalize_candidate_for_metrics(text: str) -> str:
    text = re.sub(r"```text|```|^## [^\n]+", " ", text, flags=re.MULTILINE)
    return normalize_text(text)


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


def verify_config() -> tuple[dict[str, dict[str, str]], dict]:
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
    return verified, config


def reference_for_page(page: str, assets: Path) -> tuple[str, Path] | None:
    ocr_reference = assets / f"page_{page}_ocr_verified_text_map.md"
    if ocr_reference.exists():
        return "reference_ocr_verified_text_map", ocr_reference
    text_reference = assets / f"page_{page}_text_map.md"
    if text_reference.exists():
        return "reference_text_map_not_ocr_verified", text_reference
    return None


def crop_paths_for_page(page: str, assets: Path) -> list[Path]:
    if page in INPUT_ORDER_OVERRIDES:
        return [assets / name for name in INPUT_ORDER_OVERRIDES[page]]
    return sorted(assets.glob("*text-evidence.png"), key=natural_key)


def input_id(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"^[0-9]+b?_", "", stem)
    stem = re.sub(r"[^a-zA-Z0-9]+", "_", stem).strip("_").lower()
    stem = re.sub(r"_+", "_", stem)
    return stem or "text_evidence"


def run_tesseract(input_path: Path, id_: str, psm: int, scratch_root: Path) -> tuple[str, dict]:
    prepared_path = scratch_root / "prepared" / f"{id_}.png"
    prepared_path.parent.mkdir(parents=True, exist_ok=True)
    transform_trim_mask(Image.open(input_path)).save(prepared_path)
    output_base = scratch_root / "ocr" / id_
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
    text = output_base.with_suffix(".txt").read_text(encoding="utf-8", errors="replace")
    return text, {
        "input_id": id_,
        "source_input_path": input_path.relative_to(ROOT).as_posix(),
        "source_input_sha256": sha256_file(input_path),
        "scratch_outputs_persisted": False,
        "ocr_text_sha256": sha256_text(text),
        "ocr_tsv_sha256": sha256_file(output_base.with_suffix(".tsv")),
        "stderr_sha256": sha256_text(completed.stderr),
        "stdout_sha256": sha256_text(completed.stdout),
        "command_profile": "tesseract -l eng --oem 1 --psm 4 txt tsv",
    }


def ineligible(page: str, reason: str, review_dir: Path | None = None, assets: Path | None = None) -> dict:
    result = {
        "page": page,
        "status": "not_run_ineligible",
        "reason": reason,
        "ocr_execution_performed": False,
        "weak_flags": ["not_run_ineligible"],
    }
    if review_dir is not None:
        result["review_dir"] = review_dir.relative_to(ROOT).as_posix()
    if assets is not None:
        result["review_assets_dir"] = assets.relative_to(ROOT).as_posix()
    return result


def replay_page(page: str, config: dict, scratch_root: Path) -> dict:
    review_dir = TRIAL_ROOT / PAGE_DIRS[page]
    assets = review_dir / "review_assets"
    if not review_dir.exists() or not assets.exists():
        return ineligible(page, "no_page_complete_review_assets_or_reference", review_dir)

    reference = reference_for_page(page, assets)
    crops = crop_paths_for_page(page, assets)
    missing_ordered = [path for path in crops if not path.exists()]
    existing_crops = [path for path in crops if path.exists()]
    if reference is None and not existing_crops:
        return ineligible(page, "no_eligible_text_evidence_crops_reference_pair", review_dir, assets)
    if reference is not None and not existing_crops:
        return ineligible(page, "reference_map_exists_but_no_text_evidence_crops", review_dir, assets)
    if reference is None:
        return ineligible(page, "text_evidence_crops_exist_but_no_reference_map", review_dir, assets)
    if missing_ordered:
        raise SystemExit(f"P{page} expected ordered input missing: {missing_ordered[0]}")

    reference_label, reference_path = reference
    reference_text = extract_reference_text(reference_path)
    chunks = []
    input_results = []
    for path in existing_crops:
        id_ = input_id(path)
        text, result = run_tesseract(path, id_, config["profile_tuple"]["tesseract_psm"], scratch_root / f"p{page}")
        chunks.append(f"## {id_}\n\n{text.strip()}")
        input_results.append(result)

    candidate_text = "\n\n".join(chunks).strip() + "\n"
    normalized = normalize_candidate_for_metrics(candidate_text)
    metrics = {
        "sequence_similarity_ratio": round(similarity_ratio(normalized, reference_text), 6),
        "token_recall": round(token_recall(normalized, reference_text), 6),
        "normalized_candidate_chars": len(normalized),
        "reference_chars": len(normalize_text(reference_text)),
    }
    weak_flags = []
    if metrics["sequence_similarity_ratio"] < WEAK_SIMILARITY_THRESHOLD:
        weak_flags.append("weak_similarity")
    if metrics["token_recall"] < WEAK_TOKEN_RECALL_THRESHOLD:
        weak_flags.append("weak_token_recall")
    if reference_label != "reference_ocr_verified_text_map":
        weak_flags.append("reference_not_ocr_verified")
    return {
        "page": page,
        "status": "run_completed",
        "review_dir": review_dir.relative_to(ROOT).as_posix(),
        "reference_label": reference_label,
        "reference_text_map": reference_path.relative_to(ROOT).as_posix(),
        "reference_text_map_sha256": sha256_file(reference_path),
        "input_count": len(existing_crops),
        "input_results": input_results,
        "candidate_text_sha256": sha256_text(candidate_text),
        "normalized_text_sha256": sha256_text(normalized + "\n"),
        "ocr_execution_performed": True,
        "metrics": metrics,
        "weak_flags": weak_flags,
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
    verified_config, config = verify_config()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix="sourcefold_001_020_overview_replay_") as scratch:
        scratch_root = Path(scratch)
        page_results = [replay_page(f"{page:03d}", config, scratch_root) for page in range(1, 21)]

    run_pages = [page for page in page_results if page["status"] == "run_completed"]
    ineligible_pages = [page for page in page_results if page["status"] == "not_run_ineligible"]
    weak_pages = [page for page in run_pages if any(flag.startswith("weak_") for flag in page["weak_flags"])]
    reference_risk_pages = [page for page in run_pages if "reference_not_ocr_verified" in page["weak_flags"]]
    aggregate = {
        "page_count": len(page_results),
        "run_page_count": len(run_pages),
        "ineligible_page_count": len(ineligible_pages),
        "input_count": sum(page["input_count"] for page in run_pages),
        "min_sequence_similarity_ratio": min(page["metrics"]["sequence_similarity_ratio"] for page in run_pages),
        "min_token_recall": min(page["metrics"]["token_recall"] for page in run_pages),
        "weak_similarity_threshold": WEAK_SIMILARITY_THRESHOLD,
        "weak_token_recall_threshold": WEAK_TOKEN_RECALL_THRESHOLD,
        "weak_pages": [page["page"] for page in weak_pages],
        "reference_risk_pages": [page["page"] for page in reference_risk_pages],
    }
    report = {
        "overview_id": OVERVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_001_020_overview_replay_completed",
        "source_frozen_profile_config": CONFIG_ID,
        "frozen_config_tuple_reused_only": True,
        "frozen_config_allowed_pages_not_broadened": True,
        "profile_id": PROFILE_ID,
        "profile_tuple": config["profile_tuple"],
        "requested_pages": [f"{page:03d}" for page in range(1, 21)],
        "eligible_run_pages": [page["page"] for page in run_pages],
        "ineligible_pages": [page["page"] for page in ineligible_pages],
        "candidate_count": 1,
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
        "page_021_plus_included": False,
        "remediation_performed": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "verified_config_inputs": verified_config,
        "page_results": page_results,
        "aggregate_metrics": aggregate,
        "recommendation": "review_weak_pages_then_authorize_separate_remediation_if_needed",
    }
    write_json(OUT_ROOT / "overview_replay_report.json", report)
    summary_lines = [
        "# Core 0.1 Text Extraction Overview Replay - 001-020 - C01TEOR020-G1-VIRAL-001",
        "",
        "Status: `candidate_only_001_020_overview_replay_completed`",
        "",
        "This overview reuses only the frozen profile tuple from `C01TEFPC-G1-VIRAL-001`; it does not broaden the config allowed-pages policy.",
        "",
        "| Page | Status | Reference | Inputs | Similarity | Token recall | Flags |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for page in page_results:
        if page["status"] == "run_completed":
            summary_lines.append(
                f"| `{page['page']}` | `run_completed` | `{page['reference_label']}` | "
                f"`{page['input_count']}` | `{page['metrics']['sequence_similarity_ratio']}` | "
                f"`{page['metrics']['token_recall']}` | `{', '.join(page['weak_flags']) or 'none'}` |"
            )
        else:
            summary_lines.append(
                f"| `{page['page']}` | `not_run_ineligible` | `n/a` | `0` | `n/a` | `n/a` | `{page['reason']}` |"
            )
    summary_lines.extend(
        [
            "",
            f"Weak thresholds: similarity `< {WEAK_SIMILARITY_THRESHOLD}`, token recall `< {WEAK_TOKEN_RECALL_THRESHOLD}`.",
            f"Weak pages: `{', '.join(aggregate['weak_pages']) or 'none'}`.",
            f"Reference-risk pages: `{', '.join(aggregate['reference_risk_pages']) or 'none'}`.",
            "",
            "Boundary: overview/report only; no remediation in this layer.",
            "No accepted/semantic/source/page-status mutation, no PDF/render/runtime/page 021+/push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "overview_replay_summary.md", "\n".join(summary_lines))
    manifest_lines = [
        "# Core 0.1 Text Extraction Overview Replay Manifest - 001-020 - C01TEOR020-G1-VIRAL-001",
        "",
        "Boundary: candidate-only overview report/summary/manifest outputs.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "overview_replay_manifest.md":
            manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "overview_replay_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
