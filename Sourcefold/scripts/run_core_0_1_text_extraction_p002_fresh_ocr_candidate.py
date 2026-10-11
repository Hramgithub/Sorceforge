from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from ocr_input_surface_policy import route_ocr_input_surface, validate_ocr_input_surface


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_route_authorization_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_candidate_G1_VIRAL_001"
CANDIDATE_ROOT = OUT_ROOT / "candidate_texts"
METADATA_ROOT = OUT_ROOT / "ocr_metadata"

LANE_ID = "C01TEP002FRESHOCR-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-CANDIDATE-001"
INPUT_LANE_ID = "C01TEP002FRESHROUTEAUTH-G1-VIRAL-001"
CREATION_HEAD = "cc0fe001"
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)
PAGE = "002"
PSM_VALUES = [4, 6]
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

PINNED_INPUTS = {
    "C01TEP002FRESHROUTEAUTH-G1-VIRAL-001.report": (
        INPUT_ROOT / "p002_fresh_ocr_route_authorization_report.json",
        "6EE1925A65367833898D0E17150687E341F411C1B7D6EDDD0219671593F6AC68",
    ),
    "C01TEP002FRESHROUTEAUTH-G1-VIRAL-001.summary": (
        INPUT_ROOT / "p002_fresh_ocr_route_authorization_summary.md",
        "096069AC2AE284A852448D0DE3B8347F9369FF89BC851850742D646D1583B741",
    ),
    "C01TEP002FRESHROUTEAUTH-G1-VIRAL-001.manifest": (
        INPUT_ROOT / "p002_fresh_ocr_route_authorization_manifest.md",
        "C0AA3147BB065FB8F0EA4F88A5D86E84F0C5B06CB9F8EAAC41DD4417AD2C444D",
    ),
}

FALSE_BOUNDARY_FLAGS = [
    "fresh_ocr_success",
    "bridge_blocker_cleared",
    "reference_scoring_performed",
    "render_execution_performed",
    "pdf_parsing_or_text_layer_extraction_performed",
    "accepted_text_mutation_performed",
    "semantic_text_mutation_performed",
    "page_status_mutation_performed",
    "source_or_raw_mutation_performed",
    "fixture_admission_performed",
    "production_ready",
    "production_assembly_authorized",
    "production_assembly_created",
    "acceptance_performed",
    "page_021_plus_included",
    "push_performed",
    "promotion_performed",
    "downstream_execution_performed",
]

OUTPUT_FILES = [
    "candidate_texts/page_002_full_page_psm4_candidate.md",
    "candidate_texts/page_002_full_page_psm6_candidate.md",
    "ocr_metadata/page_002_full_page_psm4_ocr_metadata.json",
    "ocr_metadata/page_002_full_page_psm6_ocr_metadata.json",
    "p002_fresh_ocr_candidate_report.json",
    "p002_fresh_ocr_candidate_summary.md",
    "p002_fresh_ocr_candidate_manifest.md",
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


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run bounded P002 fresh OCR candidate execution.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 fresh OCR candidate execution is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 fresh OCR candidate execution requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 fresh OCR candidate execution requires the exact broad orchestration decision")


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
    route = read_json(PINNED_INPUTS["C01TEP002FRESHROUTEAUTH-G1-VIRAL-001.report"][0])
    if route["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 fresh OCR route authorization lane")
    if route["page"] != PAGE:
        raise SystemExit("P002 page drifted")
    if route["fresh_ocr_route_authorized"] is not True:
        raise SystemExit("P002 fresh OCR route is not authorized")
    if route["authorized_future_ocr_surface_class"] != "full_page_region":
        raise SystemExit("P002 OCR surface class drifted")
    if route["corrected_crop_refs_authorized_as_ocr_input"] is not False:
        raise SystemExit("P002 crop refs unexpectedly authorized as OCR input")
    return verified, route


def authorized_page_image(route: dict[str, Any]) -> dict[str, str]:
    entries = {item["input_key"]: item for item in route["materialized_surface_entries"]}
    page_image = entries["P002.page_image"]
    if page_image["authorized_role"] != "full_page_region_candidate_input":
        raise SystemExit("P002 page image role drifted")
    for key in ["P002.corrected_crop_ref.1", "P002.corrected_crop_ref.2"]:
        if entries[key]["authorized_role"] != "crop_reference_comparison_only_not_ocr_input":
            raise SystemExit(f"{key} role drifted")
    path = ROOT / page_image["path"]
    actual = sha256_file(path)
    if actual != page_image["sha256"]:
        raise SystemExit("P002 page image hash drifted")
    return {"path": page_image["path"], "sha256": actual}


def run_tesseract(image_path: Path, psm: int) -> tuple[str, dict[str, Any]]:
    with tempfile.TemporaryDirectory(prefix=f"sf_p{PAGE}_psm{psm}_") as tmp:
        output_base = Path(tmp) / f"page_{PAGE}_full_page_psm{psm}"
        command = [str(TESSERACT), str(image_path), str(output_base), "-l", "eng", "--oem", "1", "--psm", str(psm), "txt", "tsv"]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(f"tesseract failed for page {PAGE} psm {psm}: {result.stderr}")
        txt_path = output_base.with_suffix(".txt")
        tsv_path = output_base.with_suffix(".tsv")
        text = txt_path.read_text(encoding="utf-8-sig") if txt_path.exists() else ""
        return text, {
            "engine": "tesseract",
            "executable": str(TESSERACT),
            "command_profile": f"tesseract -l eng --oem 1 --psm {psm} txt tsv",
            "transient_ocr_output_persisted": False,
            "transient_tsv_sha256": sha256_file(tsv_path) if tsv_path.exists() else None,
            "stdout_sha256": sha256_text(result.stdout),
            "stderr_sha256": sha256_text(result.stderr),
            "returncode": result.returncode,
        }


def run_candidate(route: dict[str, Any], psm: int) -> dict[str, Any]:
    page_image = authorized_page_image(route)
    image_path = ROOT / page_image["path"]
    surface = {
        "page_id": "P002",
        "surface_class": "full_page_region",
        "allowed_purpose": "candidate_policy",
        "source_artifact": {"path": page_image["path"], "sha256": page_image["sha256"], "hash_status": "matched"},
        "authorization": {
            "full_page_region_authorization_id": AUTHORIZATION_ID,
            "page_family": "p002_fresh_ocr_route",
            "region_policy": "lane_owned_full_page_image_only_no_crop_ref_ocr_input",
            "negative_reason_not_baseline": "page_002_bridge_lineage_needs_fresh_ocr_candidate_execution",
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
        raise SystemExit(f"P002 surface validation failed: {validation['findings']}")
    text, ocr_run = run_tesseract(image_path, psm)
    candidate_path = CANDIDATE_ROOT / f"page_002_full_page_psm{psm}_candidate.md"
    write_text(candidate_path, text)
    candidate_hash = sha256_file(candidate_path)
    route_decision = route_ocr_input_surface(surface=surface, metrics=None, candidate_text_hash_sealed=True, scoring_report_complete=False)
    metadata = {
        "page": PAGE,
        "psm": psm,
        "surface": surface,
        "surface_validation": validation,
        "ocr_run": ocr_run,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": candidate_hash,
        "candidate_hash_sealed": True,
        "reference_scoring_performed": False,
        "policy_route": route_decision,
        "fresh_ocr_success": False,
        "bridge_removal_effect": "none",
        "acceptance_effect": "none",
        "promotion_effect": "none",
    }
    metadata_path = METADATA_ROOT / f"page_002_full_page_psm{psm}_ocr_metadata.json"
    write_json(metadata_path, metadata)
    metadata["ocr_metadata_path"] = metadata_path.relative_to(ROOT).as_posix()
    metadata["ocr_metadata_sha256"] = sha256_file(metadata_path)
    return metadata


def build_report(verified_inputs: dict[str, dict[str, str]], route: dict[str, Any], candidates: list[dict[str, Any]]) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_fresh_ocr_candidate_executed_candidate_only_no_scoring_no_promotion",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_id": INPUT_LANE_ID,
        "page": PAGE,
        "verified_inputs": verified_inputs,
        "route_authorization_status": route["status"],
        "ocr_execution_performed": True,
        "tesseract_invoked": True,
        "tesseract_invoked_pages": [PAGE],
        "psm_values": PSM_VALUES,
        "ocr_input_surface_class": "full_page_region",
        "ocr_input_path": route["materialized_surface_entries"][0]["path"],
        "corrected_crop_refs_used_as_ocr_input": False,
        "candidate_hash_sealed_before_reference_scoring": True,
        "candidate_count": len(candidates),
        "candidate_entries": candidates,
        "fresh_ocr_success_pages": [],
        "bridge_removed_for_pages": [],
        "allowed_next_action": "separate_bounded_p002_candidate_scoring_or_remediation_decision",
    }
    for flag in FALSE_BOUNDARY_FLAGS:
        report[flag] = False
    return report


def build_summary(report: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# {LANE_ID}",
            "",
            f"Status: `{report['status']}`",
            "",
            "Ran bounded fresh OCR candidates for page `002` from the lane-owned",
            "full-page image only. Corrected crop refs were not used as OCR input.",
            "",
            "- Candidate count: `2`.",
            "- Fresh OCR success: `false`.",
            "- Bridge blocker cleared: `false`.",
            "- Reference scoring performed: `false`.",
            "",
        ]
    )


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for name in OUTPUT_FILES:
        path = OUT_ROOT / name
        if path.exists():
            hashes[name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
    return hashes


def build_manifest(report: dict[str, Any]) -> str:
    hashes = output_hashes()
    lines = [
        f"# {LANE_ID} Manifest",
        "",
        f"- Authorization: `{AUTHORIZATION_ID}`",
        f"- Status: `{report['status']}`",
        "- Output policy: candidate texts, metadata, report, summary, and manifest only; no raw OCR, acceptance, production, source mutation, or page 021+.",
        f"- OCR execution performed: `{str(report['ocr_execution_performed']).lower()}`",
        f"- Fresh OCR success: `{str(report['fresh_ocr_success']).lower()}`",
        f"- Bridge blocker cleared: `{str(report['bridge_blocker_cleared']).lower()}`",
        "",
        "## Inputs",
        "",
    ]
    for key, item in report["verified_inputs"].items():
        lines.append(f"- `{key}`: `{item['sha256']}`")
    lines.extend(["", "## Outputs", ""])
    for name in OUTPUT_FILES:
        if name == "p002_fresh_ocr_candidate_manifest.md":
            lines.append(f"- `{name}`: sealed by external sync surfaces after manifest write")
        elif name in hashes:
            lines.append(f"- `{name}`: `{hashes[name]['sha256']}`")
        else:
            lines.append(f"- `{name}`: pending until post-write sync")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified_inputs, route = verify_inputs()
    candidates = [run_candidate(route, psm) for psm in PSM_VALUES]
    report = build_report(verified_inputs, route, candidates)
    write_json(OUT_ROOT / "p002_fresh_ocr_candidate_report.json", report)
    write_text(OUT_ROOT / "p002_fresh_ocr_candidate_summary.md", build_summary(report))
    write_text(OUT_ROOT / "p002_fresh_ocr_candidate_manifest.md", build_manifest(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
