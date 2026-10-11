from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps

from ocr_input_surface_policy import validate_ocr_input_surface
import run_core_0_1_text_extraction_full_page_geometry_probe_p018_p017 as fg
import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002"
LEDGER = overview.LEDGER
TESSERACT = overview.TESSERACT

LANE_ID = "C01TEGP012013016017018020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-GEOMETRY-PROBE-012-013-016-017-018-020-001"
HUMAN_DECISION = "коммит затем делай 1-5 план"
PAGES = ["012", "013", "016", "017", "018", "020"]
PARKED_PAGES = ["014", "019"]
ALLOWED_PAGES = set(PAGES)
FORBIDDEN_ROLE_TOKENS = {"acceptance_evidence", "accepted_source", "source_profile", "page_complete_acceptance", "runtime_lock"}
DIAGNOSTIC_SEQUENCE_SIMILARITY = 0.997
DIAGNOSTIC_TOKEN_RECALL = 0.993
CONTROL = {"page": "018", "candidate_id": "full_page_expanded_overlap_psm4", "similarity": 0.999466, "token_recall": 0.996067}
EXPECTED_COMMITS = ["6507f386", "a01da448"]
EXPECTED_INPUT_HASHES = {
    "router_script": (
        ROOT / "scripts" / "ocr_input_surface_policy.py",
        "B0FD483CA63710FA75E7194C2E5A9E394E0FE9A2DB84F0913A85892F5761BBBB",
    ),
    "router_test": (
        ROOT / "tests" / "test_ocr_input_surface_policy.py",
        "682294FDB2027EF35C488F8F6B31589B6F6BB87D6098187997ADA4F794D381B9",
    ),
    "overview_001_020_report": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4_G1_VIRAL_001"
        / "overview_replay_report.json",
        "7FE37ECD8BAB5EAC4C9557C244D0E2CA618704783E6CFC9D706CFB60B46E0357",
    ),
    "p017_p018_geometry_control_report": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_full_page_geometry_probe_p018_p017_G1_VIRAL_001"
        / "full_page_geometry_probe_p018_p017_report.json",
        "5338382319130D59C9B109E27F58DD496FAAAFF9AD93CADD606F8552776996FB",
    ),
    "p012_triage_packet": (
        TRIAL_ROOT / "page_012_triage_G1_VIRAL_001" / "page_012_triage_packet.json",
        "93A2CCE7F4F639BFC10CAA33840FB587491FCA89827188ECDD53586B8E6A4689",
    ),
    "p013_triage_packet": (
        TRIAL_ROOT / "page_013_triage_G1_VIRAL_001" / "page_013_triage_packet.json",
        "2724A753543F5903EA8CE10176B5A88C206DBE479FF3DED72701273D5C8B5879",
    ),
    "p016_triage_report": (
        TRIAL_ROOT / "page_016_triage_G1_VIRAL_001" / "page_016_triage_report.json",
        "C98349F2ED24682CCBFDD3E3F9FAFE6A4EF291FBAF5B7FA09590E25B94B2E115",
    ),
    "p020_triage_report": (
        TRIAL_ROOT / "page_020_triage_G1_VIRAL_001" / "page_020_triage_report.json",
        "92B446992A502D4DC607B9787E9A69CB13B26C1AA193F43B2C075E76F097F2F3",
    ),
    "p012_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["012"] / "review_assets" / "page_012.png",
        "D5040085668216E68E617A06B513DC09CE3797E4D3F6BC6AC7BF35B68BD08ED6",
    ),
    "p013_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["013"] / "review_assets" / "page_013.png",
        "DC9BF562A4B3B7E43B38F29F484B64B13958330F449672D6A695B36E0D8F0935",
    ),
    "p016_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["016"] / "review_assets" / "page_016.png",
        "7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56",
    ),
    "p017_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["017"] / "review_assets" / "page_017.png",
        "1198CBB7D55877B31FEEA3E32CD95EABEB504A4610CA98D7CB2047C30142E08F",
    ),
    "p018_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["018"] / "review_assets" / "page_018.png",
        "6E8F440CEB5F11A4081722ADF5CD65F74E622641884192390E9DA0CAE6C6BFD4",
    ),
    "p020_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["020"] / "review_assets" / "page_020.png",
        "53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E",
    ),
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


def validate_page_id(page: str) -> None:
    if page in PARKED_PAGES:
        raise SystemExit(f"P{page} is parked outside this geometry probe")
    if not re.fullmatch(r"\d{3}", page):
        raise SystemExit(f"invalid page id: {page}")
    if int(page) >= 21:
        raise SystemExit(f"P{page} is outside this lane; page 021+ is blocked")
    if page not in ALLOWED_PAGES:
        raise SystemExit(f"P{page} is not authorized for {LANE_ID}")


def strict_slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    slug = re.sub(r"_+", "_", slug)
    if not slug or not re.fullmatch(r"[a-z0-9_]+", slug):
        raise SystemExit(f"unsafe region id: {value}")
    return slug


def validate_box(box: object, image: Image.Image) -> tuple[int, int, int, int]:
    if not isinstance(box, list) or len(box) != 4 or not all(isinstance(item, int) for item in box):
        raise SystemExit(f"invalid crop_box_px: {box}")
    left, top, width, height = box
    if left < 0 or top < 0 or width <= 0 or height <= 0:
        raise SystemExit(f"invalid crop_box_px order: {box}")
    right = left + width
    bottom = top + height
    if right > image.width or bottom > image.height:
        raise SystemExit(f"crop_box_px out of page bounds: {box}")
    return left, top, right, bottom


def reject_forbidden_role(role: str) -> None:
    role_key = role.lower()
    if any(token in role_key for token in FORBIDDEN_ROLE_TOKENS):
        raise SystemExit(f"forbidden role for candidate-only geometry probe: {role}")


def full_page_region_surface(
    *,
    page: str,
    image_path: Path,
    image_sha256: str,
    region_id: str,
    page_space_box: tuple[int, int, int, int],
    prepared_path: Path,
    preprocessing_profile: str,
    psm: int,
) -> dict[str, Any]:
    return {
        "surface_class": "full_page_region",
        "artifact_role": "ocr_candidate_full_page_region",
        "ocr_allowed": True,
        "source_artifact": {
            "path": image_path.relative_to(ROOT).as_posix(),
            "sha256": image_sha256,
            "hash_status": "matched",
        },
        "page_id": f"P{page}",
        "regions": [
            {
                "region_id": region_id,
                "page_space_box": list(page_space_box),
                "prepared_region_path": prepared_path.relative_to(ROOT).as_posix(),
            }
        ],
        "preprocessing_profile": preprocessing_profile,
        "ocr_engine_profile": {
            "engine": "tesseract",
            "profile": f"eng_oem1_psm{psm}",
        },
        "allowed_purpose": "candidate_policy",
        "reference_policy": "scorer_only_after_candidate_hash",
        "failure_behavior": "partial_artifacts_quarantined_no_scoring_or_acceptance",
        "authorization": {
            "full_page_region_authorization_id": AUTHORIZATION_ID,
            "page_family": "router_selected_geometry_probe_required",
            "region_policy": "full_page_derived_page_space_regions",
            "negative_reason_not_baseline": "static_router_geometry_probe_required",
        },
        "reference_loaded_before_candidate_hash": False,
    }


def validate_surface_or_exit(surface: dict[str, Any]) -> dict[str, Any]:
    validation = validate_ocr_input_surface(surface)
    if validation["status"] != "passed":
        raise SystemExit(f"ocr_input_surface validation failed: {validation['findings']}")
    return validation


def verify_expected_inputs() -> dict[str, dict[str, str]]:
    verified = {}
    for key, (path, expected) in EXPECTED_INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    return verified


def verify_router_commits() -> list[str]:
    for commit in EXPECTED_COMMITS:
        exists = subprocess.run(["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd=ROOT, capture_output=True)
        if exists.returncode != 0:
            raise SystemExit(f"missing router commit: {commit}")
        ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT, capture_output=True)
        if ancestor.returncode != 0:
            raise SystemExit(f"router commit is not an ancestor of HEAD: {commit}")
    return EXPECTED_COMMITS


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run 012/013/016/017/018/020 full-page geometry OCR probe.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("geometry probe is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"geometry probe requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("geometry probe requires the exact bounded human decision")


def verify_inputs() -> dict[str, Any]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")
    return {
        "authorization_ledger": {
            "path": LEDGER.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(LEDGER),
        },
        "source_router_commits": verify_router_commits(),
        "pinned_inputs": verify_expected_inputs(),
        "parked_pages": PARKED_PAGES,
    }


def page_image_path(page: str) -> Path:
    validate_page_id(page)
    path = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets" / f"page_{page}.png"
    if not path.exists():
        raise SystemExit(f"P{page} missing full-page review image: {path}")
    return path


def reference_for_page(page: str) -> tuple[str, Path, str]:
    validate_page_id(page)
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    reference = overview.reference_for_page(page, assets)
    if reference is None:
        raise SystemExit(f"P{page} missing reference")
    label, path = reference
    return label, path, overview.extract_reference_text(path)


def triage_report_path(page: str) -> Path:
    validate_page_id(page)
    return TRIAL_ROOT / f"page_{page}_triage_G1_VIRAL_001" / f"page_{page}_triage_report.json"


def triage_packet_path(page: str) -> Path:
    validate_page_id(page)
    return TRIAL_ROOT / f"page_{page}_triage_G1_VIRAL_001" / f"page_{page}_triage_packet.json"


def expand_box(box: list[int], image: Image.Image, padding: int = 24) -> tuple[int, int, int, int]:
    left, top, right, bottom = validate_box(box, image)
    return (
        max(0, left - padding),
        max(0, top - padding),
        min(image.width, right + padding),
        min(image.height, bottom + padding),
    )


def body_region(source: Image.Image, box: tuple[int, int, int, int], border: int = 24) -> Image.Image:
    crop = source.crop(box).convert("RGB")
    canvas = Image.new("RGB", (crop.width + border * 2, crop.height + border * 2), "white")
    canvas.paste(crop, (border, border))
    return ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB")


def run_tesseract(prepared: Path, base: Path, psm: int) -> tuple[str, dict[str, str]]:
    command = [
        str(TESSERACT),
        str(prepared),
        str(base),
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
    text_path = base.with_suffix(".txt")
    tsv_path = base.with_suffix(".tsv")
    stderr_path = base.with_suffix(".stderr.txt")
    stdout_path = base.with_suffix(".stdout.txt")
    write_text(stderr_path, completed.stderr)
    write_text(stdout_path, completed.stdout)
    text = text_path.read_text(encoding="utf-8", errors="replace")
    return text, {
        "prepared_region_path": prepared.relative_to(ROOT).as_posix(),
        "prepared_region_sha256": sha256_file(prepared),
        "raw_ocr_text_path": text_path.relative_to(ROOT).as_posix(),
        "raw_ocr_text_sha256": sha256_file(text_path),
        "raw_ocr_tsv_path": tsv_path.relative_to(ROOT).as_posix(),
        "raw_ocr_tsv_sha256": sha256_file(tsv_path),
        "stderr_path": stderr_path.relative_to(ROOT).as_posix(),
        "stdout_path": stdout_path.relative_to(ROOT).as_posix(),
    }


def metrics(candidate_text: str, reference_text: str) -> dict[str, Any]:
    page_metrics = fg.metrics(candidate_text, reference_text)
    page_metrics["similarity_delta_from_p018_control"] = round(
        page_metrics["sequence_similarity_ratio"] - CONTROL["similarity"], 6
    )
    page_metrics["token_recall_delta_from_p018_control"] = round(page_metrics["token_recall"] - CONTROL["token_recall"], 6)
    page_metrics["structure_order_assessment"] = (
        "control_or_better" if page_metrics["sequence_similarity_ratio"] >= CONTROL["similarity"] else "below_control"
    )
    page_metrics["completeness_assessment"] = (
        "control_or_better" if page_metrics["token_recall"] >= CONTROL["token_recall"] else "below_control"
    )
    return page_metrics


def triage_box_specs(page: str) -> list[dict[str, Any]]:
    validate_page_id(page)
    report_path = triage_report_path(page)
    if not report_path.exists():
        raise SystemExit(f"P{page} missing triage report: {report_path}")
    report = json.loads(report_path.read_text(encoding="utf-8-sig"))
    if not report.get("review_blocks") and not report.get("text_blocks"):
        packet_path = triage_packet_path(page)
        if not packet_path.exists():
            raise SystemExit(f"P{page} missing triage packet: {packet_path}")
        report = json.loads(packet_path.read_text(encoding="utf-8-sig"))
    specs = []
    for index, item in enumerate(report.get("review_blocks") or report.get("text_blocks") or [], start=1):
        asset = item.get("asset", "")
        if "text-evidence" not in asset:
            continue
        role = item["role"]
        reject_forbidden_role(role)
        specs.append(
            {
                "id": item.get("text_evidence_crop_id") or f"P{page}-B{index:03d}-TES",
                "role": role,
                "box": item["crop_box_px"],
                "psm": 4,
                "source_triage_asset": asset,
            }
        )
    if not specs:
        raise SystemExit(f"P{page} has no text evidence box specs")
    return specs


def generate_triage_box_candidate(page: str) -> dict[str, Any]:
    validate_page_id(page)
    image_path = page_image_path(page)
    source_image = Image.open(image_path).convert("RGB")
    image_sha256 = sha256_file(image_path)
    chunks: list[str] = []
    region_results: list[dict[str, Any]] = []
    family_id = "full_page_triage_boxes_expanded_psm4"
    for index, spec in enumerate(triage_box_specs(page), start=1):
        box = expand_box(spec["box"], source_image)
        region_id = strict_slug(spec["id"])
        prepared = OUT_ROOT / "prepared_regions" / family_id / f"p{page}" / f"{index:02d}_{region_id}.png"
        base = OUT_ROOT / "raw_ocr" / family_id / f"p{page}" / f"{index:02d}_{region_id}"
        prepared.parent.mkdir(parents=True, exist_ok=True)
        base.parent.mkdir(parents=True, exist_ok=True)
        body_region(source_image, box).save(prepared)
        surface = full_page_region_surface(
            page=page,
            image_path=image_path,
            image_sha256=image_sha256,
            region_id=region_id,
            page_space_box=box,
            prepared_path=prepared,
            preprocessing_profile="full_page_triage_boxes_expanded_psm4",
            psm=spec["psm"],
        )
        surface_validation = validate_surface_or_exit(surface)
        text, ocr_result = run_tesseract(prepared, base, spec["psm"])
        chunks.append(f"## {spec['role']}\n\n{text.strip()}")
        region_results.append(
            {
                "region_id": spec["id"],
                "region_role": spec["role"],
                "source_triage_asset": spec["source_triage_asset"],
                "source_triage_crop_box_px": spec["box"],
                "page_space_box": list(box),
                "psm": spec["psm"],
                "ocr_input_surface": surface,
                "ocr_input_surface_validation": surface_validation,
                "ocr_result": ocr_result,
            }
        )
    candidate_text = "\n\n".join(chunks).strip() + "\n"
    candidate_path = OUT_ROOT / "candidate_texts" / family_id / f"page_{page}_candidate.md"
    write_text(candidate_path, candidate_text)
    return {
        "page": page,
        "candidate_id": family_id,
        "description": "Full-page-derived expanded triage page-space boxes with PSM 4.",
        "source_page_image_path": image_path.relative_to(ROOT).as_posix(),
        "source_page_image_sha256": image_sha256,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_path),
        "region_results": region_results,
    }


def generate_control_candidate(page: str, spec: dict[str, Any]) -> dict[str, Any]:
    validate_page_id(page)
    image_path = page_image_path(page)
    source_image = Image.open(image_path).convert("RGB")
    image_sha256 = sha256_file(image_path)
    chunks: list[str] = []
    region_results: list[dict[str, Any]] = []
    for index, region in enumerate(spec["regions"], start=1):
        prepared = OUT_ROOT / "prepared_regions" / spec["id"] / f"p{page}" / f"{index:02d}_{region['id']}.png"
        base = OUT_ROOT / "raw_ocr" / spec["id"] / f"p{page}" / f"{index:02d}_{region['id']}"
        prepared.parent.mkdir(parents=True, exist_ok=True)
        base.parent.mkdir(parents=True, exist_ok=True)
        fg.prepare_region(source_image, region).save(prepared)
        surface = full_page_region_surface(
            page=page,
            image_path=image_path,
            image_sha256=image_sha256,
            region_id=region["id"],
            page_space_box=tuple(region["box"]),
            prepared_path=prepared,
            preprocessing_profile=spec["id"],
            psm=region["psm"],
        )
        surface_validation = validate_surface_or_exit(surface)
        text, ocr_result = run_tesseract(prepared, base, region["psm"])
        chunks.append(f"## {region['id']}\n\n{text.strip()}")
        region_results.append(
            {
                "region_id": region["id"],
                "region_kind": region["kind"],
                "page_space_box": list(region["box"]),
                "psm": region["psm"],
                "ocr_input_surface": surface,
                "ocr_input_surface_validation": surface_validation,
                "ocr_result": ocr_result,
            }
        )
    candidate_text = "\n\n".join(chunks).strip() + "\n"
    candidate_path = OUT_ROOT / "candidate_texts" / spec["id"] / f"page_{page}_candidate.md"
    write_text(candidate_path, candidate_text)
    return {
        "page": page,
        "candidate_id": spec["id"],
        "description": spec["description"],
        "source_page_image_path": image_path.relative_to(ROOT).as_posix(),
        "source_page_image_sha256": image_sha256,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_path),
        "region_results": region_results,
    }


def candidates_for_page(page: str) -> list[dict[str, Any]]:
    if page in {"017", "018"}:
        return [generate_control_candidate(page, spec) for spec in fg.candidate_specs()[page]]
    return [generate_triage_box_candidate(page)]


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)

    page_results: dict[str, list[dict[str, Any]]] = {}
    for page in PAGES:
        page_results[page] = candidates_for_page(page)

    for page, results in page_results.items():
        label, reference_path, reference_text = reference_for_page(page)
        for result in results:
            candidate_path = ROOT / result["candidate_text_path"]
            candidate_text = candidate_path.read_text(encoding="utf-8", errors="replace")
            page_metrics = metrics(candidate_text, reference_text)
            result["reference_label"] = label
            result["reference_path"] = reference_path.relative_to(ROOT).as_posix()
            result["reference_sha256"] = sha256_file(reference_path)
            result["reference_risk_flag"] = label != "reference_ocr_verified_text_map"
            result["metrics"] = page_metrics
            result["diagnostic_threshold_met"] = (
                page_metrics["sequence_similarity_ratio"] >= DIAGNOSTIC_SEQUENCE_SIMILARITY
                and page_metrics["token_recall"] >= DIAGNOSTIC_TOKEN_RECALL
            )
        results.sort(
            key=lambda item: (
                item["metrics"]["sequence_similarity_ratio"],
                item["metrics"]["token_recall"],
            ),
            reverse=True,
        )
        write_json(OUT_ROOT / "rankings" / f"page_{page}_candidate_rankings.json", results)

    best_by_page = {page: results[0] for page, results in page_results.items()}
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_geometry_probe_completed",
        "source_router": "C01TEISP-G1-VIRAL-001",
        "verified_inputs": verified_inputs,
        "pages": PAGES,
        "parked_pages_not_included": PARKED_PAGES,
        "diagnostic_thresholds": {
            "sequence_similarity": DIAGNOSTIC_SEQUENCE_SIMILARITY,
            "token_recall": DIAGNOSTIC_TOKEN_RECALL,
            "acceptance_effect": "none",
        },
        "observed_control_measurement": CONTROL,
        "candidate_generation_reference_text_used": False,
        "reference_text_loaded_after_candidate_hashing": True,
        "candidate_generation_inputs": ["full_page_review_png", "page_space_geometry", "tesseract_ocr"],
        "candidate_count_per_page": {page: len(results) for page, results in page_results.items()},
        "best_by_page": best_by_page,
        "all_pages_diagnostic_threshold_met": all(item["diagnostic_threshold_met"] for item in best_by_page.values()),
        "reference_guided_repair_used": False,
        "independent_ocr_candidate": True,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "pdf_text_layer_extraction_performed": False,
        "render_execution_performed": False,
        "runtime_implementation_created": False,
        "runtime_start_performed": False,
        "page_021_plus_included": False,
        "push_performed": False,
        "recommendation": "Review per-page geometry-probe results before promoting any candidate family.",
    }
    write_json(OUT_ROOT / "geometry_probe_012_013_016_017_018_020_report.json", report)

    lines = [
        "# Core 0.1 Geometry Probe - 012/013/016/017/018/020 - C01TEGP012013016017018020-G1-VIRAL-001",
        "",
        "Status: `candidate_only_geometry_probe_completed`",
        "",
        "Candidate generation uses full-page PNG geometry and Tesseract only; reference text is scorer-only after candidate hashes are sealed.",
        "",
        "| Page | Best candidate | Similarity | Token recall | Diagnostic threshold met | Similarity delta | Token recall delta |",
        "|---|---|---:|---:|---|---:|---:|",
    ]
    for page in PAGES:
        best = best_by_page[page]
        page_metrics = best["metrics"]
        lines.append(
            f"| `{page}` | `{best['candidate_id']}` | "
            f"`{page_metrics['sequence_similarity_ratio']}` | `{page_metrics['token_recall']}` | "
            f"`{best['diagnostic_threshold_met']}` | `{page_metrics['similarity_delta_from_p018_control']}` | "
            f"`{page_metrics['token_recall_delta_from_p018_control']}` |"
        )
    lines.extend(
        [
            "",
            "Parked pages not included: `014`, `019`.",
            "",
            "Boundary: candidate-only OCR probe; no reference-guided repair, no accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "geometry_probe_012_013_016_017_018_020_summary.md", "\n".join(lines))

    manifest_lines = [
        "# Geometry Probe Manifest - C01TEGP012013016017018020-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "geometry_probe_012_013_016_017_018_020_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "geometry_probe_012_013_016_017_018_020_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
