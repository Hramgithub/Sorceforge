from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_text_extraction_smoke_p009_remediation_matrix.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_smoke_p009_remediation_matrix.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P009_ROOT = TRIAL_ROOT / "page_complete_review_p009_G1_VIRAL_001" / "review_assets"
SOURCE_SMOKE_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p009_G1_VIRAL_001"
OUTPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

MATRIX_ID = "C01TESRM-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-REMEDIATION-MATRIX-001"
HUMAN_DECISION = "иди по этому плану 1-5"
BASELINE_SMOKE_ID = "C01TESP-G1-VIRAL-001"

INPUTS = {
    "left_profile_text_evidence": P009_ROOT / "3b_P009-left-profile-text-column-text-evidence.png",
    "right_profile_text_evidence": P009_ROOT / "4b_P009-right-profile-text-column-text-evidence.png",
}
REFERENCE_TEXT_MAP = P009_ROOT / "page_009_ocr_verified_text_map.md"
REFERENCE_SEMANTIC_MAP = P009_ROOT / "page_009_semantic_text_map.md"
REFERENCE_SEMANTIC_JSON = P009_ROOT / "page_009_semantic_text_map.json"
SOURCE_SMOKE_REPORT = SOURCE_SMOKE_ROOT / "smoke_report.json"
SOURCE_SMOKE_MANIFEST = SOURCE_SMOKE_ROOT / "smoke_manifest.md"
SOURCE_SMOKE_SUMMARY = SOURCE_SMOKE_ROOT / "smoke_summary.md"

PSM_MODES = (6, 4, 11)


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    strategy: str
    variant: str
    psm: int


CANDIDATES = (
    Candidate("full_original_psm6", "full_column", "original", 6),
    Candidate("full_original_psm4", "full_column", "original", 4),
    Candidate("full_original_psm11", "full_column", "original", 11),
    Candidate("trim_mask_psm6", "full_column", "edge_mask_trim", 6),
    Candidate("trim_mask_psm4", "full_column", "edge_mask_trim", 4),
    Candidate("trim_mask_psm11", "full_column", "edge_mask_trim", 11),
    Candidate("grayscale_psm6", "full_column", "grayscale_autocontrast", 6),
    Candidate("grayscale_psm4", "full_column", "grayscale_autocontrast", 4),
    Candidate("grayscale_psm11", "full_column", "grayscale_autocontrast", 11),
    Candidate("threshold_psm6", "full_column", "binary_threshold", 6),
    Candidate("threshold_psm4", "full_column", "binary_threshold", 4),
    Candidate("threshold_psm11", "full_column", "binary_threshold", 11),
    Candidate("denoise_sharpen_psm6", "full_column", "denoise_sharpen", 6),
    Candidate("denoise_sharpen_psm4", "full_column", "denoise_sharpen", 4),
    Candidate("denoise_sharpen_psm11", "full_column", "denoise_sharpen", 11),
    Candidate("split_threshold_psm6", "split_header_body", "binary_threshold", 6),
    Candidate("split_threshold_psm4", "split_header_body", "binary_threshold", 4),
    Candidate("split_denoise_sharpen_psm6", "split_header_body", "denoise_sharpen", 6),
    Candidate("split_denoise_sharpen_psm4", "split_header_body", "denoise_sharpen", 4),
)


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
    parser = argparse.ArgumentParser(description="Build bounded P009 OCR smoke remediation matrix.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 P009 OCR remediation matrix is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 P009 OCR remediation matrix requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 P009 OCR remediation matrix requires the exact bounded human decision")
    return args


def verify_inputs() -> dict[str, dict[str, str]]:
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"Refusing to overwrite existing remediation output directory: {OUTPUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"Missing OCR executable: {TESSERACT}")
    smoke = read_json(SOURCE_SMOKE_REPORT)
    if smoke["smoke_id"] != BASELINE_SMOKE_ID:
        raise SystemExit("unexpected baseline smoke id")
    if smoke["page"] != "009" or smoke["page_021_plus_included"]:
        raise SystemExit("baseline smoke is not bounded to P009 only")
    if smoke["source_or_raw_mutation_performed"] or smoke["accepted_text_mutation_performed"]:
        raise SystemExit("baseline smoke mutation boundary is not clean")

    paths = {
        "baseline_smoke_report": SOURCE_SMOKE_REPORT,
        "baseline_smoke_manifest": SOURCE_SMOKE_MANIFEST,
        "baseline_smoke_summary": SOURCE_SMOKE_SUMMARY,
        "reference_ocr_verified_text_map": REFERENCE_TEXT_MAP,
        "reference_semantic_map": REFERENCE_SEMANTIC_MAP,
        "reference_semantic_json": REFERENCE_SEMANTIC_JSON,
        **{f"p009_input_{key}": path for key, path in INPUTS.items()},
    }
    verified: dict[str, dict[str, str]] = {}
    for key, path in paths.items():
        if not path.exists():
            raise SystemExit(f"missing input: {path}")
        verified[key] = {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(path),
        }
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


def transform_image(source: Image.Image, variant: str) -> Image.Image:
    image = source.convert("RGB")
    if variant == "original":
        return image
    if variant == "edge_mask_trim":
        trimmed = image.crop((12, 12, image.width - 12, image.height - 12))
        canvas = Image.new("RGB", (trimmed.width + 24, trimmed.height + 24), "white")
        canvas.paste(trimmed, (12, 12))
        return ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB")
    if variant == "grayscale_autocontrast":
        return ImageOps.autocontrast(ImageOps.grayscale(image)).convert("RGB")
    if variant == "binary_threshold":
        gray = ImageOps.autocontrast(ImageOps.grayscale(image))
        return gray.point(lambda p: 255 if p > 168 else 0).convert("RGB")
    if variant == "denoise_sharpen":
        gray = ImageOps.autocontrast(ImageOps.grayscale(image))
        return gray.filter(ImageFilter.MedianFilter(size=3)).filter(ImageFilter.SHARPEN).convert("RGB")
    raise ValueError(f"unknown variant: {variant}")


def prepare_inputs(candidate: Candidate) -> list[tuple[str, Path]]:
    prepared: list[tuple[str, Path]] = []
    for side, input_path in INPUTS.items():
        source = Image.open(input_path)
        image = transform_image(source, candidate.variant)
        if candidate.strategy == "full_column":
            out = OUTPUT_ROOT / "prepared_inputs" / candidate.candidate_id / f"{side}.png"
            write_image(out, image)
            prepared.append((side, out))
        elif candidate.strategy == "split_header_body":
            split_at = max(1, int(image.height * 0.24))
            parts = {
                f"{side}_header": image.crop((0, 0, image.width, split_at)),
                f"{side}_body": image.crop((0, split_at, image.width, image.height)),
            }
            for part_id, part in parts.items():
                out = OUTPUT_ROOT / "prepared_inputs" / candidate.candidate_id / f"{part_id}.png"
                write_image(out, part)
                prepared.append((part_id, out))
        else:
            raise ValueError(f"unknown strategy: {candidate.strategy}")
    return prepared


def write_image(path: Path, image: Image.Image) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)


def run_tesseract(image_path: Path, output_base: Path, psm: int) -> dict[str, str | int]:
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
    return {
        "command": " ".join(command),
        "exit_code": completed.returncode,
        "stdout_path": output_base.with_suffix(".stdout.txt").relative_to(ROOT).as_posix(),
        "stderr_path": output_base.with_suffix(".stderr.txt").relative_to(ROOT).as_posix(),
        "log_path": output_base.with_suffix(".log.txt").relative_to(ROOT).as_posix(),
    }


def build_candidate(candidate: Candidate, reference_text: str) -> dict:
    prepared_inputs = prepare_inputs(candidate)
    chunks: list[str] = []
    raw_outputs: list[dict] = []
    for input_id, image_path in prepared_inputs:
        output_base = OUTPUT_ROOT / "raw_ocr" / candidate.candidate_id / input_id
        command_record = run_tesseract(image_path, output_base, candidate.psm)
        txt_path = output_base.with_suffix(".txt")
        tsv_path = output_base.with_suffix(".tsv")
        text = txt_path.read_text(encoding="utf-8", errors="replace")
        chunks.append(f"## {input_id}\n\n```text\n{text.strip()}\n```")
        raw_outputs.append(
            {
                "input_id": input_id,
                "prepared_input_path": image_path.relative_to(ROOT).as_posix(),
                "prepared_input_sha256": sha256_file(image_path),
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
    similarity = similarity_ratio(normalized, reference_text)
    recall = token_recall(normalized, reference_text)
    candidate_dir = OUTPUT_ROOT / "candidate_texts"
    write_text(candidate_dir / f"{candidate.candidate_id}.md", "# Candidate OCR Text\n\n" + candidate_text)
    write_text(candidate_dir / f"{candidate.candidate_id}.normalized.txt", normalized + "\n")
    return {
        "candidate_id": candidate.candidate_id,
        "strategy": candidate.strategy,
        "variant": candidate.variant,
        "psm": candidate.psm,
        "raw_outputs": raw_outputs,
        "candidate_text_path": (candidate_dir / f"{candidate.candidate_id}.md").relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_dir / f"{candidate.candidate_id}.md"),
        "normalized_text_path": (candidate_dir / f"{candidate.candidate_id}.normalized.txt").relative_to(ROOT).as_posix(),
        "normalized_text_sha256": sha256_file(candidate_dir / f"{candidate.candidate_id}.normalized.txt"),
        "metrics": {
            "sequence_similarity_ratio": round(similarity, 6),
            "token_recall": round(recall, 6),
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
    baseline = read_json(SOURCE_SMOKE_REPORT)
    baseline_similarity = baseline["metrics"]["sequence_similarity_ratio"]

    results = [build_candidate(candidate, reference_text) for candidate in CANDIDATES]
    rankings = sorted(
        results,
        key=lambda item: (item["metrics"]["sequence_similarity_ratio"], item["metrics"]["token_recall"]),
        reverse=True,
    )
    best = rankings[0]
    improvement = round(best["metrics"]["sequence_similarity_ratio"] - baseline_similarity, 6)
    recommendation = (
        "candidate_only_remediation_improves_control_stand_continue_same_scope"
        if improvement > 0
        else "candidate_only_remediation_does_not_improve_control_stand_reassess_profile"
    )

    report = {
        "matrix_id": MATRIX_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_p009_remediation_matrix_completed",
        "source_smoke": BASELINE_SMOKE_ID,
        "old_broad_runner_reused": False,
        "page": "009",
        "page_021_plus_included": False,
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
        "output_policy": "candidate_only_separate_remediation_directory",
        "candidate_count": len(results),
        "psm_modes": list(PSM_MODES),
        "preprocessing_variants": sorted({candidate.variant for candidate in CANDIDATES}),
        "strategies": sorted({candidate.strategy for candidate in CANDIDATES}),
        "baseline_similarity": baseline_similarity,
        "best_candidate_id": best["candidate_id"],
        "best_similarity": best["metrics"]["sequence_similarity_ratio"],
        "best_token_recall": best["metrics"]["token_recall"],
        "improvement_over_baseline": improvement,
        "recommendation": recommendation,
        "verified_inputs": verified_inputs,
        "candidate_results": results,
        "variant_rankings": [
            {
                "rank": rank,
                "candidate_id": item["candidate_id"],
                "strategy": item["strategy"],
                "variant": item["variant"],
                "psm": item["psm"],
                "sequence_similarity_ratio": item["metrics"]["sequence_similarity_ratio"],
                "token_recall": item["metrics"]["token_recall"],
            }
            for rank, item in enumerate(rankings, 1)
        ],
    }
    write_json(OUTPUT_ROOT / "remediation_report.json", report)
    write_json(OUTPUT_ROOT / "variant_rankings.json", report["variant_rankings"])

    summary = [
        "# Core 0.1 P009 OCR Smoke Remediation Matrix",
        "",
        f"Matrix id: `{MATRIX_ID}`",
        "",
        "Status: `candidate_only_p009_remediation_matrix_completed`",
        "",
        "Boundary: P009-only remediation matrix over read-only text-evidence crop PNGs.",
        "",
        f"Baseline similarity: `{baseline_similarity}`.",
        f"Best candidate: `{best['candidate_id']}`.",
        f"Best similarity: `{best['metrics']['sequence_similarity_ratio']}`.",
        f"Improvement over baseline: `{improvement}`.",
        f"Recommendation: `{recommendation}`.",
        "",
        "Preserved limits:",
        "",
        "- No page 009 source/review/reference/accepted-text overwrite.",
        "- No page 021+ processing or authorization.",
        "- No PDF parsing/text-layer extraction.",
        "- No render execution.",
        "- No source/OCR/render/PDF/raw mutation.",
        "- No runtime implementation/start.",
        "- No translation/proofreading/push.",
        "",
        "Top variants:",
        "",
        "| Rank | Candidate | Similarity | Token recall |",
        "|---:|---|---:|---:|",
    ]
    for item in report["variant_rankings"][:8]:
        summary.append(
            f"| {item['rank']} | `{item['candidate_id']}` | `{item['sequence_similarity_ratio']}` | `{item['token_recall']}` |"
        )
    summary.append("")
    write_text(OUTPUT_ROOT / "remediation_summary.md", "\n".join(summary))

    manifest_lines = [
        "# Core 0.1 P009 OCR Smoke Remediation Matrix Manifest",
        "",
        f"Matrix id: `{MATRIX_ID}`",
        "",
        "Boundary: candidate-only remediation evidence; no accepted text/source/profile mutation.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "remediation_manifest.md":
            manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(OUTPUT_ROOT / "remediation_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
