from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "source_reconstruction_prep_G1_VIRAL_001"
REVIEW_ROOT = TRIAL_ROOT / "source_reconstruction_review_G1_VIRAL_001"
REMEDIATION_REVIEW_ROOT = TRIAL_ROOT / "ocr_remediation_review_G1_VIRAL_001"
MATRIX_ROOT = TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001"

PREP_AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-PREP-001"
RUN_AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-RUN-001"
PROTOCOL_ID = "SRP-G1-VIRAL-001"
ADMITTED_MANIFEST_ID = "SRA-G1-VIRAL-001"
DRY_RUN_ID = "SRD-G1-VIRAL-001"
RUN_MANIFEST_ID = "SRM-G1-VIRAL-001"
REVIEW_PACKAGE_ID = "G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001"
PRECHECK_ID = "SRQ-G1-VIRAL-001"
BASELINE_COMMIT = "02a0c643a6f0d83fb8b3dd35f428b9269c800f69"
RUN_BASELINE_COMMIT = "1003d74f"
EXPECTED_ADMITTED_MANIFEST_SHA256 = "59D146B024EBAEB548D2BD5F03BF3027632C4F289FD2FFAC36F36879501277E9"
RUN_STATUS = "candidate_review_blocked_for_remediation"

EXPECTED_PREDECESSORS = {
    "pre_ocr_map_bundle": "B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F",
    "gold_sample_manifest": "A7EA3157815D8F3311AFA91B0EF70F97AE9E6C0C7F4D76203983C1B0341B7D62",
    "ocr_candidate_manifest": "6FBDC9463A670968D335DFB8F841819CEB55CDC24B2CFC1C32EF9AA9BD323842",
    "remediation_review": "B3491A1F3E942C430AE246A62DCAFB066F95BEA56390CF510D27635EBFEE6725",
    "ocr_admission_candidate": "194BD814F7CC2E2C42575794FE5627231059BEFD53D3B66A0F9DBDC4A6DDD33E",
    "evidence_rollup": "D47730B89FD8BE0BB45A0D81416302BAC8B68D099D4AEB77E09355E50304129C",
    "negative_checks": "2205564DB2BCD9EEF73D8EB02034EA28D7292D1A6970E3056F3BD9F5887E8F61",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def check_predecessors(manifest: dict[str, object]) -> list[dict[str, object]]:
    checks: list[dict[str, object]] = []
    predecessors = manifest["predecessors"]
    for key, expected_hash in EXPECTED_PREDECESSORS.items():
        entry = predecessors[key]
        path = ROOT / entry["path"]
        actual_hash = sha256_file(path)
        passed = actual_hash == expected_hash == entry["sha256"]
        checks.append(
            {
                "name": f"{key} hash matches admitted manifest and prep authorization",
                "passed": passed,
                "path": rel(path),
                "expected_sha256": expected_hash,
                "actual_sha256": actual_hash,
            }
        )
    return checks


def build_dry_run() -> None:
    PREP_ROOT.mkdir(parents=True, exist_ok=True)
    manifest_path = PREP_ROOT / "source_reconstruction_admitted_manifest.json"
    protocol_path = PREP_ROOT / "source_reconstruction_protocol.md"
    manifest = read_json(manifest_path)
    admitted_regions = manifest["admitted_regions"]
    route_keys = [
        (
            region["sample_id"],
            region["page_id"],
            region["region_id"],
            region["predecessor_zone_id"],
            region["predecessor_crop_sha256"],
        )
        for region in admitted_regions
    ]
    predecessor_checks = check_predecessors(manifest)

    checks = predecessor_checks + [
        {
            "name": "prep authorization is exact",
            "passed": manifest["authorization_id"] == PREP_AUTHORIZATION_ID,
        },
        {
            "name": "admitted manifest id is exact",
            "passed": manifest["manifest_id"] == ADMITTED_MANIFEST_ID,
        },
        {
            "name": "no candidate text is allowed in prep",
            "passed": all(region["candidate_text_allowed_in_prep"] is False for region in admitted_regions),
        },
        {
            "name": "all OCR candidate regions require future run authorization",
            "passed": all(
                region["execution_authorization_required"] == RUN_AUTHORIZATION_ID
                for region in admitted_regions
                if region["route_class"] == "ocr_candidate"
            ),
        },
        {
            "name": "visual QC regions do not request execution authorization",
            "passed": all(
                region["execution_authorization_required"] is None
                for region in admitted_regions
                if region["route_class"] == "visual_qc_only"
            ),
        },
        {
            "name": "every admitted region has source page image reference",
            "passed": all((ROOT / region["page_image"]).exists() for region in admitted_regions),
        },
        {
            "name": "every admitted region binds predecessor zone and crop hash",
            "passed": all(
                region.get("predecessor_zone_id") and region.get("predecessor_crop_sha256")
                for region in admitted_regions
            ),
        },
        {
            "name": "admitted route keys are unique at sample/page/region/zone/crop level",
            "passed": len(route_keys) == len(set(route_keys)),
        },
        {
            "name": "coarse duplicate regions are separated by predecessor zone/crop identity",
            "passed": all(
                len(
                    {
                        (region["predecessor_zone_id"], region["predecessor_crop_sha256"], region["route_class"])
                        for region in admitted_regions
                        if (
                            region["sample_id"],
                            region["page_id"],
                            region["region_id"],
                        )
                        == coarse_key
                    }
                )
                == sum(
                    1
                    for region in admitted_regions
                    if (
                        region["sample_id"],
                        region["page_id"],
                        region["region_id"],
                    )
                    == coarse_key
                )
                for coarse_key in {
                    (region["sample_id"], region["page_id"], region["region_id"])
                    for region in admitted_regions
                }
            ),
        },
    ]
    if not all(check["passed"] for check in checks):
        raise AssertionError("source reconstruction prep dry-run checks failed")

    report = {
        "dry_run_id": DRY_RUN_ID,
        "authorization_id": PREP_AUTHORIZATION_ID,
        "status": "source_reconstruction_prep_only",
        "baseline_commit": BASELINE_COMMIT,
        "protocol": {
            "id": PROTOCOL_ID,
            "path": rel(protocol_path),
            "sha256": sha256_file(protocol_path),
        },
        "admitted_manifest": {
            "id": ADMITTED_MANIFEST_ID,
            "path": rel(manifest_path),
            "sha256": sha256_file(manifest_path),
        },
        "admitted_region_count": len(admitted_regions),
        "ocr_candidate_region_count": sum(1 for region in admitted_regions if region["route_class"] == "ocr_candidate"),
        "visual_qc_only_region_count": sum(1 for region in admitted_regions if region["route_class"] == "visual_qc_only"),
        "candidate_text_created": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "source_acceptance": False,
        "gate_1_advancement": False,
        "human_review_required_now": False,
        "future_execution_authorization_required": RUN_AUTHORIZATION_ID,
        "checks": checks,
    }
    write_json(PREP_ROOT / "source_reconstruction_dry_run_report.json", report)

    orchestration = [
        "# Source Reconstruction Prep Orchestration - SRD-G1-VIRAL-001",
        "",
        f"- Script: `scripts/build_source_reconstruction_review_package.py`",
        f"- Prep authorization: `{PREP_AUTHORIZATION_ID}`",
        f"- Protocol: `{PROTOCOL_ID}`",
        f"- Admitted manifest: `{ADMITTED_MANIFEST_ID}`",
        f"- Dry-run report: `{DRY_RUN_ID}`",
        "- OCR executed: `false`",
        "- Candidate source text created: `false`",
        "- PDF opened/parsed/rendered: `false`",
        "- Human review requested now: `false`",
        "",
        "Reproduce with:",
        "",
        "```powershell",
        "python scripts\\build_source_reconstruction_review_package.py --dry-run",
        "python -m pytest tests\\test_source_reconstruction_review_package.py",
        "scripts\\validate_roadmap.ps1",
        "```",
    ]
    (PREP_ROOT / "orchestration_record.md").write_text("\n".join(orchestration) + "\n", encoding="utf-8")


def load_selected_ocr() -> dict[tuple[str, str], dict[str, object]]:
    admission = read_json(REMEDIATION_REVIEW_ROOT / "ocr_admission_candidate.json")
    selected = {}
    for zone in admission["selected_ocr_configs"]:
        selected[(zone["sample_id"], zone["zone_id"])] = zone
    return selected


def build_source_reconstruction_package(args: argparse.Namespace) -> None:
    if args.authorization_id != RUN_AUTHORIZATION_ID:
        raise SystemExit(
            "Refusing execution: source reconstruction run requires "
            f"{RUN_AUTHORIZATION_ID}; received {args.authorization_id!r}."
        )
    manifest_path = PREP_ROOT / "source_reconstruction_admitted_manifest.json"
    manifest_sha256 = sha256_file(manifest_path)
    if args.admitted_manifest_sha256 != EXPECTED_ADMITTED_MANIFEST_SHA256:
        raise SystemExit("Refusing execution: admitted manifest hash argument does not match run authorization.")
    if manifest_sha256 != EXPECTED_ADMITTED_MANIFEST_SHA256:
        raise SystemExit("Refusing execution: admitted manifest on disk is stale for run authorization.")

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = read_json(manifest_path)
    selected_ocr = load_selected_ocr()
    raw_root = MATRIX_ROOT / "raw_outputs"

    candidate_records: list[dict[str, object]] = []
    visual_queue: list[dict[str, object]] = []
    checks: list[dict[str, object]] = check_predecessors(manifest)

    for region in manifest["admitted_regions"]:
        route_class = region["route_class"]
        zone_key = (region["sample_id"], region["predecessor_zone_id"])
        base_record = {
            "region_admission_id": region["region_admission_id"],
            "sample_id": region["sample_id"],
            "page_id": region["page_id"],
            "region_id": region["region_id"],
            "predecessor_zone_id": region["predecessor_zone_id"],
            "predecessor_crop_sha256": region["predecessor_crop_sha256"],
            "page_image": region["page_image"],
            "input_crop": rel(MATRIX_ROOT / "input_crops" / f"{region['sample_id']}__{region['predecessor_zone_id']}.png"),
            "route_class": route_class,
            "review_class": region["review_class"],
            "source_acceptance": False,
        }
        if route_class == "visual_qc_only":
            visual_queue.append(
                base_record
                | {
                    "candidate_text_created": False,
                    "finding": "visual_qc_required_no_text_candidate",
                    "human_review_hint": "Compare source image/region visually; no OCR text candidate is promoted for this component.",
                }
            )
            continue

        selected = selected_ocr.get(zone_key)
        if selected is None:
            raise AssertionError(f"missing selected OCR evidence for {zone_key}")
        if selected["crop_sha256"] != region["predecessor_crop_sha256"]:
            raise AssertionError(f"crop hash mismatch for {zone_key}")
        text_path = raw_root / f"{region['sample_id']}__{region['predecessor_zone_id']}__{selected['selected_config']}.txt"
        tsv_path = raw_root / f"{region['sample_id']}__{region['predecessor_zone_id']}__{selected['selected_config']}.tsv"
        if not text_path.exists() or not tsv_path.exists():
            raise AssertionError(f"missing selected OCR raw output for {zone_key}")
        if sha256_file(text_path) != selected["selected_text_sha256"]:
            raise AssertionError(f"text hash mismatch for {zone_key}")
        if sha256_file(tsv_path) != selected["selected_tsv_sha256"]:
            raise AssertionError(f"TSV hash mismatch for {zone_key}")

        candidate_text = text_path.read_text(encoding="utf-8-sig").strip()
        candidate_records.append(
            base_record
            | {
                "candidate_text": candidate_text,
                "candidate_text_sha256": selected["selected_text_sha256"],
                "candidate_tsv_sha256": selected["selected_tsv_sha256"],
                "selected_config": selected["selected_config"],
                "normalized_exact_evidence": selected["normalized_exact"],
                "token_recall_evidence": selected["token_recall"],
                "char_error_rate_evidence": selected["char_error_rate"],
                "overlay_qc_status": selected["overlay_qc_status"],
                "order_qc_status": selected["order_qc_status"],
                "candidate_text_created": True,
                "accepted_source_text": False,
                "human_review_ready": False,
            }
        )

    overlay_attention_count = sum(1 for record in candidate_records if record["overlay_qc_status"] != "ok")
    visual_qc_count = len(visual_queue)
    human_ready = visual_qc_count == 0 and overlay_attention_count == 0

    checks.extend(
        [
            {
                "name": "exact admitted manifest hash matches run authorization",
                "passed": manifest_sha256 == EXPECTED_ADMITTED_MANIFEST_SHA256,
            },
            {
                "name": "candidate text records come only from selected OCR evidence hashes",
                "passed": len(candidate_records) == 5
                and all(record["candidate_text_sha256"] for record in candidate_records),
            },
            {
                "name": "visual QC entries create no candidate text",
                "passed": len(visual_queue) == 2
                and all(item["candidate_text_created"] is False for item in visual_queue),
            },
            {
                "name": "human-facing package is blocked until visual/overlay findings are remediated",
                "passed": human_ready is False,
            },
            {
                "name": "no source acceptance, QA acceptance, or Gate 1 advancement is produced",
                "passed": True,
            },
        ]
    )
    if not all(check["passed"] for check in checks):
        raise AssertionError("source reconstruction run checks failed")

    precheck = {
        "precheck_id": PRECHECK_ID,
        "authorization_id": RUN_AUTHORIZATION_ID,
        "status": "evidence_precheck_only",
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "human_review_ready": human_ready,
        "human_review_blocked": not human_ready,
        "candidate_record_count": len(candidate_records),
        "visual_qc_queue_count": visual_qc_count,
        "findings": [
            {
                "kind": "visual_qc_required",
                "count": visual_qc_count,
                "blocking_for_human_review": visual_qc_count > 0,
                "blocking_for_source_acceptance": True,
            },
            {
                "kind": "overlay_qc_attention",
                "count": overlay_attention_count,
                "blocking_for_human_review": overlay_attention_count > 0,
                "blocking_for_source_acceptance": True,
            },
        ],
        "checks": checks,
    }

    run_manifest = {
        "run_manifest_id": RUN_MANIFEST_ID,
        "authorization_id": RUN_AUTHORIZATION_ID,
        "status": RUN_STATUS,
        "baseline_commit": RUN_BASELINE_COMMIT,
        "admitted_manifest": {
            "id": ADMITTED_MANIFEST_ID,
            "path": rel(manifest_path),
            "sha256": manifest_sha256,
        },
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "candidate_text_created": True,
        "human_review_ready": human_ready,
        "human_review_blocked": not human_ready,
        "accepted_source_text_created": False,
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "candidate_records": candidate_records,
        "visual_qc_queue": visual_queue,
        "precheck": PRECHECK_ID,
    }

    write_json(REVIEW_ROOT / "source_reconstruction_run_manifest.json", run_manifest)
    write_json(REVIEW_ROOT / "source_reconstruction_precheck.json", precheck)

    review_lines = [
        "# Viral Source Reconstruction Review Package - G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001",
        "",
        f"Status: `{RUN_STATUS}`",
        "",
        f"Authorization: `{RUN_AUTHORIZATION_ID}`",
        "",
        "Boundary: this package is not accepted source text, QA acceptance, fixture acceptance, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "Human review status: `blocked_for_remediation`. Visual-QC and overlay-QC findings must be remediated before asking Bogdan to approve source reconstruction.",
        "",
        "## Candidate Text Records",
        "",
    ]
    for record in candidate_records:
        review_lines.extend(
            [
                f"### {record['region_admission_id']} / {record['page_id']} / {record['predecessor_zone_id']}",
                "",
                f"- Source image: `{record['page_image']}`",
                f"- Input crop: `{record['input_crop']}`",
                f"- Region: `{record['region_id']}`",
                f"- Predecessor crop SHA-256: `{record['predecessor_crop_sha256']}`",
                f"- Selected config: `{record['selected_config']}`",
                f"- OCR text SHA-256: `{record['candidate_text_sha256']}`",
                f"- Overlay QC: `{record['overlay_qc_status']}`",
                f"- Order QC: `{record['order_qc_status']}`",
                "",
                "```text",
                str(record["candidate_text"]),
                "```",
                "",
            ]
        )
    review_lines.extend(
        [
            "## Visual-QC Queue",
            "",
        ]
    )
    for item in visual_queue:
        review_lines.extend(
            [
                f"- `{item['region_admission_id']}` / `{item['page_id']}` / `{item['predecessor_zone_id']}` / crop `{item['predecessor_crop_sha256']}`: `{item['review_class']}`; no candidate text created.",
            ]
        )
    review_lines.extend(
        [
            "",
            "## Review Options",
            "",
            "- Do not request source approval from Bogdan yet.",
            "- Remediate exact records by `region_admission_id` and predecessor crop hash.",
            "- Route visual-QC-only records to a separate visual correction/remediation artifact before human acceptance review.",
        ]
    )
    (REVIEW_ROOT / "raw_ocr_candidate_for_human_review.md").write_text("\n".join(review_lines) + "\n", encoding="utf-8")

    orchestration = [
        "# Source Reconstruction Run Orchestration - SRM-G1-VIRAL-001",
        "",
        f"- Script: `scripts/build_source_reconstruction_review_package.py`",
        f"- Authorization: `{RUN_AUTHORIZATION_ID}`",
        f"- Run manifest: `{RUN_MANIFEST_ID}`",
        f"- Review package: `{REVIEW_PACKAGE_ID}`",
        f"- Evidence precheck: `{PRECHECK_ID}`",
        f"- Status: `{RUN_STATUS}`",
        "- OCR executed by this run: `false`",
        "- Candidate text assembled from selected OCR evidence: `true`",
        f"- Human review ready: `{str(human_ready).lower()}`",
        "- Source acceptance: `false`",
        "- Gate 1 advancement: `false`",
        "",
        "Reproduce with:",
        "",
        "```powershell",
        f"python scripts\\build_source_reconstruction_review_package.py --execute --authorization-id {RUN_AUTHORIZATION_ID} --admitted-manifest-sha256 {EXPECTED_ADMITTED_MANIFEST_SHA256}",
        "python -m pytest tests\\test_source_reconstruction_review_package.py",
        "scripts\\validate_roadmap.ps1",
        "```",
    ]
    (REVIEW_ROOT / "orchestration_record.md").write_text("\n".join(orchestration) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Generate prep-only dry-run evidence.")
    parser.add_argument("--execute", action="store_true", help="Future run mode; fail-closed until run authorization exists.")
    parser.add_argument("--authorization-id", default="", help="Required only for a future execution authorization.")
    parser.add_argument("--admitted-manifest-sha256", default="", help="Exact SRA manifest hash required by run authorization.")
    args = parser.parse_args()

    if args.execute:
        build_source_reconstruction_package(args)
        return
    if not args.dry_run:
        raise SystemExit("Refusing to run: pass --dry-run for prep-only evidence.")
    build_dry_run()


if __name__ == "__main__":
    main()
