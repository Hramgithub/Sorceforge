from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from ocr_input_surface_policy import route_ocr_input_surface, validate_ocr_input_surface


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p014_p019_route_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p014_p019_full_page_ocr_G1_VIRAL_001"
CANDIDATE_ROOT = OUT_ROOT / "candidate_texts"
METADATA_ROOT = OUT_ROOT / "ocr_metadata"

LANE_ID = "C01TEP014019FPOCR-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P014-P019-FULL-PAGE-OCR-001"
INPUT_LANE_ID = "C01TEP014019ROUTEDEC-G1-VIRAL-001"
CREATION_HEAD = "a33aa0db"
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)
PAGES = ["014", "019"]
PSM_VALUES = [4, 6]
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

PINNED_INPUTS = {
    "C01TEP014019ROUTEDEC-G1-VIRAL-001.report": (
        INPUT_ROOT / "p014_p019_route_decision_report.json",
        "BC4D6569FE50C59374C0A1D54B3A23611D267D08B6759F8B5D726FEC8D989458",
    ),
    "C01TEP014019ROUTEDEC-G1-VIRAL-001.summary": (
        INPUT_ROOT / "p014_p019_route_decision_summary.md",
        "5AF33BFEB0E3750597AF4A400849128CF2D429C2AD2BDA334D576F2D83DEF18E",
    ),
    "C01TEP014019ROUTEDEC-G1-VIRAL-001.manifest": (
        INPUT_ROOT / "p014_p019_route_decision_manifest.md",
        "77C243CD1FB4C1AB70EE7902BA005216477DFD6B5FDC6C2B7FBADB332F2E42C9",
    ),
    "P014.page_image": (
        TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001" / "review_assets" / "page_014.png",
        "24271ACED987DDF04850975ABE27D3B9BD4D48C74D81226E381D98D5E82948EA",
    ),
    "P014.text_map": (
        TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001" / "review_assets" / "page_014_text_map.md",
        "F454329B57FC3AD31455B77378D4E5642C20B8E86B6B33922077B2382C08EC66",
    ),
    "P019.page_image": (
        TRIAL_ROOT / "page_complete_review_p019_G1_VIRAL_001" / "review_assets" / "page_019.png",
        "63BBB963A76F5C266E4A1B139FBCEFD2D390FB23B23CA391E8BAF12A4E9D3AC8",
    ),
    "P019.text_map": (
        TRIAL_ROOT / "page_complete_review_p019_G1_VIRAL_001" / "review_assets" / "page_019_text_map.md",
        "A808376F3B6BA8DAE947847394FB69172E8E0E0646287B0C0AF3370CAE635E24",
    ),
}

FALSE_BOUNDARY_FLAGS = [
    "production_ready",
    "production_assembly_authorized",
    "production_assembly_created",
    "acceptance_performed",
    "accepted_text_mutation_performed",
    "semantic_text_mutation_performed",
    "page_status_mutation_performed",
    "source_or_raw_mutation_performed",
    "fixture_admission_performed",
    "page_021_plus_included",
    "push_performed",
    "promotion_performed",
    "downstream_execution_performed",
]

OUTPUT_FILES = [
    "candidate_texts/page_014_full_page_psm4_candidate.md",
    "candidate_texts/page_014_full_page_psm6_candidate.md",
    "candidate_texts/page_019_full_page_psm4_candidate.md",
    "candidate_texts/page_019_full_page_psm6_candidate.md",
    "ocr_metadata/page_014_full_page_psm4_ocr_metadata.json",
    "ocr_metadata/page_014_full_page_psm6_ocr_metadata.json",
    "ocr_metadata/page_019_full_page_psm4_ocr_metadata.json",
    "ocr_metadata/page_019_full_page_psm6_ocr_metadata.json",
    "p014_p019_full_page_ocr_report.json",
    "p014_p019_full_page_ocr_summary.md",
    "p014_p019_full_page_ocr_manifest.md",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def git_head() -> str:
    result = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def token_recall(candidate: str, reference: str) -> float:
    cand_tokens = set(re.findall(r"[A-Za-z0-9']+", candidate.lower()))
    ref_tokens = set(re.findall(r"[A-Za-z0-9']+", reference.lower()))
    return len(cand_tokens & ref_tokens) / len(ref_tokens) if ref_tokens else 0.0


def metrics(candidate: str, reference: str) -> dict[str, float]:
    candidate_norm = normalize(candidate)
    reference_norm = normalize(reference)
    return {
        "sequence_similarity_ratio": round(difflib.SequenceMatcher(None, candidate_norm, reference_norm).ratio(), 6),
        "token_recall": round(token_recall(candidate_norm, reference_norm), 6),
    }


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run bounded full-page OCR for P014/P019.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P014/P019 full-page OCR is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P014/P019 full-page OCR requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P014/P019 full-page OCR requires the exact broad orchestration decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}
    decision = read_json(PINNED_INPUTS["C01TEP014019ROUTEDEC-G1-VIRAL-001.report"][0])
    if decision["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P014/P019 route decision input lane")
    if decision["pages"] != PAGES:
        raise SystemExit("P014/P019 route decision page set drifted")
    if decision["future_full_page_ocr_route_authorized"] is not True:
        raise SystemExit("P014/P019 full-page OCR route is not authorized")
    if decision["future_full_page_ocr_route_may_use_text_evidence_crops_as_ocr_input"] is not False:
        raise SystemExit("P014/P019 route decision unexpectedly allows text-evidence OCR input")
    return verified, decision


def page_image(page: str) -> Path:
    return PINNED_INPUTS[f"P{page}.page_image"][0]


def page_reference(page: str) -> str:
    return PINNED_INPUTS[f"P{page}.text_map"][0].read_text(encoding="utf-8-sig")


def run_tesseract(image_path: Path, page: str, psm: int) -> tuple[str, dict[str, Any]]:
    with tempfile.TemporaryDirectory(prefix=f"sf_p{page}_psm{psm}_") as tmp:
        output_base = Path(tmp) / f"page_{page}_full_page_psm{psm}"
        command = [str(TESSERACT), str(image_path), str(output_base), "-l", "eng", "--oem", "1", "--psm", str(psm), "txt", "tsv"]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(f"tesseract failed for page {page} psm {psm}: {result.stderr}")
        txt_path = output_base.with_suffix(".txt")
        tsv_path = output_base.with_suffix(".tsv")
        text = txt_path.read_text(encoding="utf-8-sig") if txt_path.exists() else ""
        tsv_hash = sha256_file(tsv_path) if tsv_path.exists() else None
        return text, {
            "engine": "tesseract",
            "executable": str(TESSERACT),
            "command_profile": f"tesseract -l eng --oem 1 --psm {psm} txt tsv",
            "input_path": image_path.relative_to(ROOT).as_posix(),
            "input_sha256": sha256_file(image_path),
            "transient_ocr_output_persisted": False,
            "transient_tsv_sha256": tsv_hash,
            "stdout_sha256": sha256_text(result.stdout),
            "stderr_sha256": sha256_text(result.stderr),
            "returncode": result.returncode,
        }


def run_page_candidate(page: str, psm: int) -> dict[str, Any]:
    image = page_image(page)
    surface = {
        "page_id": f"P{page}",
        "surface_class": "full_page_region",
        "allowed_purpose": "candidate_policy",
        "source_artifact": {
            "path": image.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(image),
            "hash_status": "matched",
        },
        "authorization": {
            "full_page_region_authorization_id": AUTHORIZATION_ID,
            "page_family": "parked_bridge_page_014_019",
            "region_policy": "full_page_image_only_no_text_evidence_crop_input",
            "negative_reason_not_baseline": "prior_route_was_text_evidence_smoke_non_promotable",
        },
        "ocr_allowed": True,
        "tesseract_invoked": False,
        "render_invoked": False,
        "pdf_parsed": False,
        "pdf_text_layer_read": False,
        "non_temp_artifact_write": False,
        "reference_loaded_before_candidate_hash": False,
    }
    validation = validate_ocr_input_surface(surface)
    if validation["status"] != "passed":
        raise SystemExit(f"P{page} surface validation failed: {validation['findings']}")
    text, run_meta = run_tesseract(image, page, psm)
    candidate_path = CANDIDATE_ROOT / f"page_{page}_full_page_psm{psm}_candidate.md"
    write_text(candidate_path, text)
    candidate_hash = sha256_file(candidate_path)
    reference_text = page_reference(page)
    candidate_metrics = metrics(text, reference_text)
    route = route_ocr_input_surface(surface=surface, candidate_text_hash_sealed=True, scoring_report_complete=True, metrics=candidate_metrics)
    metadata = {
        "page": page,
        "psm": psm,
        "surface": surface,
        "surface_validation": validation,
        "ocr_run": run_meta,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": candidate_hash,
        "candidate_hash_sealed_before_reference_scoring": True,
        "reference_text_map_path": PINNED_INPUTS[f"P{page}.text_map"][0].relative_to(ROOT).as_posix(),
        "reference_text_map_sha256": PINNED_INPUTS[f"P{page}.text_map"][1],
        "reference_authority": "page_complete_text_map_comparison_only_not_acceptance_truth",
        "diagnostic_metrics": candidate_metrics,
        "policy_route": route,
        "fresh_ocr_success": False,
        "acceptance_effect": "none",
        "promotion_effect": "none",
    }
    metadata_path = METADATA_ROOT / f"page_{page}_full_page_psm{psm}_ocr_metadata.json"
    write_json(metadata_path, metadata)
    metadata["ocr_metadata_path"] = metadata_path.relative_to(ROOT).as_posix()
    metadata["ocr_metadata_sha256"] = sha256_file(metadata_path)
    return metadata


def build_report(verified_inputs: dict[str, dict[str, str]], decision: dict[str, Any], candidates: list[dict[str, Any]]) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    by_page: dict[str, list[dict[str, Any]]] = {page: [] for page in PAGES}
    for item in candidates:
        by_page[item["page"]].append(item)
    selected = []
    for page, items in by_page.items():
        best = sorted(items, key=lambda item: (item["diagnostic_metrics"]["sequence_similarity_ratio"], item["diagnostic_metrics"]["token_recall"]), reverse=True)[0]
        selected.append(
            {
                "page": page,
                "selected_candidate_text_path": best["candidate_text_path"],
                "selected_candidate_text_sha256": best["candidate_text_sha256"],
                "selected_psm": best["psm"],
                "diagnostic_metrics": best["diagnostic_metrics"],
                "fresh_ocr_success": False,
                "selection_basis": "highest_diagnostic_similarity_then_token_recall_comparison_only",
            }
        )
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p014_p019_full_page_ocr_completed_candidate_only_no_promotion",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_id": INPUT_LANE_ID,
        "pages": PAGES,
        "verified_inputs": verified_inputs,
        "route_decision_status": decision["status"],
        "ocr_execution_performed": True,
        "tesseract_invoked": True,
        "tesseract_invoked_pages": PAGES,
        "ocr_input_surface_class": "full_page_region",
        "text_evidence_crops_used_as_ocr_input": False,
        "candidate_hash_sealed_before_reference_scoring": True,
        "candidate_count": len(candidates),
        "candidate_entries": candidates,
        "selected_candidates": selected,
        "fresh_ocr_success_pages": [],
        "bridge_removed_for_pages": [],
        "comparison_reference_authority": "page_complete_text_map_comparison_only_not_acceptance_truth",
        "allowed_next_action": "separate_bounded_014_019_scoring_or_remediation_decision",
    }
    for flag in FALSE_BOUNDARY_FLAGS:
        report[flag] = False
    return report


def build_summary(report: dict[str, Any]) -> str:
    lines = [
        f"# {LANE_ID}",
        "",
        f"Status: `{report['status']}`",
        "",
        "Ran bounded full-page OCR candidates for pages `014/019` from full-page",
        "image surfaces only. Text-evidence crops were not used as OCR input.",
        "",
        "Candidates are comparison-only and do not promote, accept, or clear bridge",
        "lineage in this lane.",
        "",
    ]
    for item in report["selected_candidates"]:
        lines.append(
            f"- Page `{item['page']}` selected PSM `{item['selected_psm']}` with similarity "
            f"`{item['diagnostic_metrics']['sequence_similarity_ratio']}` and token recall "
            f"`{item['diagnostic_metrics']['token_recall']}`."
        )
    lines.append("")
    return "\n".join(lines)


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for name in OUTPUT_FILES:
        path = OUT_ROOT / name
        if path.exists():
            hashes[name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
    return hashes


def build_manifest(report: dict[str, Any], hashes: dict[str, dict[str, str]]) -> str:
    lines = [
        f"# {LANE_ID} Manifest",
        "",
        f"- Authorization: `{AUTHORIZATION_ID}`",
        f"- Status: `{report['status']}`",
        "- Output policy: candidate texts, metadata, report, summary, and manifest only; no raw OCR, acceptance, production, source mutation, or page 021+.",
        "",
        "## Inputs",
        "",
    ]
    for key, item in report["verified_inputs"].items():
        lines.append(f"- `{key}`: `{item['sha256']}`")
    lines.extend(["", "## Outputs", ""])
    for name, item in hashes.items():
        lines.append(f"- `{name}`: `{item['sha256']}`")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified_inputs, decision = verify_inputs()
    candidates = [run_page_candidate(page, psm) for page in PAGES for psm in PSM_VALUES]
    report = build_report(verified_inputs, decision, candidates)
    write_json(OUT_ROOT / "p014_p019_full_page_ocr_report.json", report)
    write_text(OUT_ROOT / "p014_p019_full_page_ocr_summary.md", build_summary(report))
    write_text(OUT_ROOT / "p014_p019_full_page_ocr_manifest.md", build_manifest(report, output_hashes()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
