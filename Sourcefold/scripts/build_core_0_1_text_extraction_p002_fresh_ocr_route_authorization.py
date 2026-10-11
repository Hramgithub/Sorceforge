from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_materialized_surface_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_route_authorization_G1_VIRAL_001"

LANE_ID = "C01TEP002FRESHROUTEAUTH-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-ROUTE-AUTH-001"
INPUT_LANE_ID = "C01TEP002MATREVIEW-G1-VIRAL-001"
PAGE = "002"
CREATION_HEAD = "bb37c3bc"
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)

PINNED_INPUTS = {
    "C01TEP002MATREVIEW-G1-VIRAL-001.report": (
        INPUT_ROOT / "p002_materialized_surface_review_report.json",
        "0B047CF8B9FA2E7B77D3CB73C296F11070198F4C2EEB4B1585882EE91DFFFA1F",
    ),
    "C01TEP002MATREVIEW-G1-VIRAL-001.summary": (
        INPUT_ROOT / "p002_materialized_surface_review_summary.md",
        "8E293FB620CE6503D341FC4EB5F882FF6A98F807C04FEDD51FFE170E8E939AD7",
    ),
    "C01TEP002MATREVIEW-G1-VIRAL-001.manifest": (
        INPUT_ROOT / "p002_materialized_surface_review_manifest.md",
        "CCBFD30FCCCAE5C0659C08817F1524CF3A3740FC87600D6956D6F20555AE6D7B",
    ),
}

FALSE_BOUNDARY_FLAGS = [
    "ocr_execution_performed",
    "tesseract_invoked",
    "fresh_ocr_success",
    "candidate_text_created",
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
    "p002_fresh_ocr_route_authorization_report.json",
    "p002_fresh_ocr_route_authorization_summary.md",
    "p002_fresh_ocr_route_authorization_manifest.md",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


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
    parser = argparse.ArgumentParser(description="Authorize P002 fresh OCR route without executing OCR.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 fresh OCR route authorization is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 fresh OCR route authorization requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 fresh OCR route authorization requires the exact broad orchestration decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}
    review_report = read_json(PINNED_INPUTS["C01TEP002MATREVIEW-G1-VIRAL-001.report"][0])
    if review_report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 materialized surface review lane")
    if review_report["page"] != PAGE:
        raise SystemExit("P002 page drifted")
    if review_report["p002_ready_for_fresh_ocr_route_authorization"] is not True:
        raise SystemExit("P002 is not ready for fresh OCR route authorization")
    if review_report["next_blocker"] != "needs_fresh_ocr_route_authorization":
        raise SystemExit("P002 next blocker drifted")
    if review_report["fresh_ocr_success"] is not False:
        raise SystemExit("P002 unexpectedly already has fresh OCR success")
    return verified, review_report


def materialized_surface_entries(review_report: dict[str, Any]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for item in review_report["reviewed_assets"]:
        path = ROOT / item["materialized_path"]
        actual = sha256_file(path)
        if actual != item["materialized_sha256"]:
            raise SystemExit(f"materialized P002 asset hash drifted: {path.name}")
        entries.append(
            {
                "input_key": item["input_key"],
                "path": item["materialized_path"],
                "sha256": actual,
                "authorized_role": (
                    "full_page_region_candidate_input"
                    if item["input_key"] == "P002.page_image"
                    else "crop_reference_comparison_only_not_ocr_input"
                ),
            }
        )
    return entries


def build_report(
    verified_inputs: dict[str, dict[str, str]],
    review_report: dict[str, Any],
    surface_entries: list[dict[str, str]],
) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_fresh_ocr_route_authorized_no_execution",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_id": INPUT_LANE_ID,
        "page": PAGE,
        "verified_inputs": verified_inputs,
        "materialized_surface_entries": surface_entries,
        "fresh_ocr_route_authorized": True,
        "authorized_future_ocr_page_image": "P002.page_image",
        "authorized_future_ocr_surface_class": "full_page_region",
        "corrected_crop_refs_authorized_as_ocr_input": False,
        "corrected_crop_refs_authorized_for_comparison_only": True,
        "candidate_hash_must_be_sealed_before_reference_scoring": True,
        "bridge_blocker_before_authorization": review_report["next_blocker"],
        "bridge_blocker_cleared": False,
        "allowed_next_action": "separate_bounded_p002_fresh_ocr_candidate_execution",
        "forbidden_next_action_without_separate_gate": [
            "fresh_ocr_success",
            "bridge_removal",
            "production_assembly",
            "acceptance",
            "fixture_admission",
            "source_or_raw_mutation",
            "page_status_mutation",
            "page_021_plus",
            "push",
            "downstream_execution",
        ],
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
            "Authorized a future bounded fresh OCR candidate route for page `002`",
            "from the lane-owned full-page image only.",
            "",
            "- OCR execution performed: `false`.",
            "- Fresh OCR success: `false`.",
            "- Bridge blocker cleared: `false`.",
            "- Corrected crop refs are comparison-only and not OCR input.",
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
        "- Output policy: authorization report, summary, and manifest only; no OCR candidates, raw OCR, acceptance, production, source mutation, or page 021+.",
        f"- Fresh OCR route authorized: `{str(report['fresh_ocr_route_authorized']).lower()}`",
        f"- OCR execution performed: `{str(report['ocr_execution_performed']).lower()}`",
        f"- Fresh OCR success: `{str(report['fresh_ocr_success']).lower()}`",
        f"- Bridge blocker cleared: `{str(report['bridge_blocker_cleared']).lower()}`",
        "",
        "## Output Hashes",
        "",
    ]
    for name in OUTPUT_FILES:
        if name == "p002_fresh_ocr_route_authorization_manifest.md":
            lines.append(f"- `{name}`: sealed by external sync surfaces after manifest write")
        elif name in hashes:
            item = hashes[name]
            lines.append(f"- `{name}`: `{item['sha256']}`")
        else:
            lines.append(f"- `{name}`: pending until post-write sync")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified, review_report = verify_inputs()
    surfaces = materialized_surface_entries(review_report)
    report = build_report(verified, review_report, surfaces)
    write_json(OUT_ROOT / OUTPUT_FILES[0], report)
    write_text(OUT_ROOT / OUTPUT_FILES[1], build_summary(report))
    write_text(OUT_ROOT / OUTPUT_FILES[2], build_manifest(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
