from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

RUN_AUTHORIZATION_ID = "BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001"
HUMAN_DECISION = "p016 corrected semantic map ok; p018 corrected semantic map ok; p016-p020 aggressive batch ok"
PAGES = ("016", "017", "018", "019", "020")
CORRECTED_SEMANTIC_MAP_DECISIONS = {
    "016": "p016 corrected semantic map ok",
    "018": "p018 corrected semantic map ok",
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


def page_authorization_id(page: str) -> str:
    return f"BA-G1-VIRAL-PAGE-{page}-AGGRESSIVE-BATCH-001"


def batch_report_path(page: str) -> Path:
    return TRIAL_ROOT / f"page_{page}_aggressive_batch_G1_VIRAL_001" / f"page_{page}_aggressive_batch_report.json"


def status_packet_path(page: str) -> Path:
    status_index = int(page) - 5
    return TRIAL_ROOT / f"gate_1_status_packet_G1_VIRAL_{status_index:03d}" / "gate_1_status_packet.json"


def output_root(page: str) -> Path:
    return TRIAL_ROOT / f"page_{page}_aggressive_batch_final_review_G1_VIRAL_001"


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Accept pages 016-020 aggressive batch final human review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--run-authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("pages 016-020 aggressive batch final review is fail-closed; pass --execute")
    if args.run_authorization_id != RUN_AUTHORIZATION_ID:
        raise SystemExit(f"pages 016-020 aggressive batch final review requires {RUN_AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit(f"pages 016-020 aggressive batch final review requires decision: {HUMAN_DECISION}")


def verify_predecessors(page: str) -> tuple[dict, dict, str, str]:
    batch_path = batch_report_path(page)
    status_path = status_packet_path(page)
    batch_sha = sha256_file(batch_path)
    status_sha = sha256_file(status_path)
    batch = read_json(batch_path)
    status = read_json(status_path)

    if batch["package_id"] != f"P{page}BATCH-G1-VIRAL-001":
        raise SystemExit(f"P{page} aggressive batch package id mismatch")
    if batch["authorization_id"] != page_authorization_id(page):
        raise SystemExit(f"P{page} aggressive batch authorization mismatch")
    if batch["status"] != "ready_for_bogdan_final_batch_review":
        raise SystemExit(f"P{page} aggressive batch is not ready for final review")
    if status["status_packet_id"] != f"G1SP-G1-VIRAL-{int(page) - 5:03d}":
        raise SystemExit(f"P{page} status packet id mismatch")
    if status["status"] != "gate_1_status_route_packet_ready_for_final_human_batch_review":
        raise SystemExit(f"P{page} status packet is not ready for final batch review")
    return batch, status, batch_sha, status_sha


def guardrails() -> dict[str, bool]:
    return {
        "whole_gate_1_acceptance": False,
        "fixture_admission": False,
        "source_acceptance_mutation": False,
        "ocr_execution": False,
        "render_execution": False,
        "pdf_parsing_or_text_layer_extraction": False,
        "raw_mutation": False,
        "translation": False,
        "proofreading": False,
        "renderer_profile_acceptance": False,
        "implementation": False,
        "push": False,
        "page_021_plus_processing": False,
    }


def write_manifest(page: str) -> None:
    out = output_root(page)
    lines = [f"# Page {page} Aggressive Batch Final Review Manifest", "", "| Output | SHA-256 |", "|---|---|"]
    manifest_name = f"page_{page}_aggressive_batch_final_review_manifest.md"
    for path in sorted(out.rglob("*")):
        if path.is_file() and path.name != manifest_name:
            lines.append(f"| `{path.relative_to(out).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(out / manifest_name, "\n".join(lines))


def build_page_review(page: str) -> None:
    batch, status, batch_sha, status_sha = verify_predecessors(page)
    out = output_root(page)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    record = {
        "review_id": f"P{page}BATCHREV-G1-VIRAL-001",
        "run_authorization_id": RUN_AUTHORIZATION_ID,
        "authorization_id": page_authorization_id(page),
        "human_decision": HUMAN_DECISION,
        "batch_decision": "p016-p020 aggressive batch ok",
        "corrected_semantic_map_decisions": CORRECTED_SEMANTIC_MAP_DECISIONS,
        "status": f"page_{page}_aggressive_batch_final_human_review_accepted",
        "human_review_scope": f"final_bundle_and_post_p{page}_status_only",
        "internal_stage_human_review_state": "human_review_skipped_by_explicit_authorization",
        "predecessors": [
            {"package_id": batch["package_id"], "sha256": batch_sha},
            {"status_packet_id": status["status_packet_id"], "sha256": status_sha},
        ],
        "accepted_page_complete_pages_current": status["page_complete_accepted_pages"],
        "remaining_page_complete_pages_unstarted": status["remaining_page_complete_pages_unstarted"],
        "recommended_next_candidate": status["recommended_next_candidate"],
        "continuation": status.get("continuation", batch.get("continuation")),
        "guardrails": guardrails(),
    }
    write_json(out / f"page_{page}_aggressive_batch_final_review_report.json", record)
    write_text(
        out / f"page_{page}_aggressive_batch_final_review_summary.md",
        f"# Page {page} Aggressive Batch Final Review - P{page}BATCHREV-G1-VIRAL-001\n\n"
        f"Bogdan accepted the page {page} final aggressive batch review target as part of "
        f"`{HUMAN_DECISION}`.\n\n"
        f"This accepts the final page {page} bundle plus `G1SP-G1-VIRAL-{int(page) - 5:03d}` only. "
        f"It does not rewrite internal P{page}TR/P{page}TXT/P{page}SEM/PCRP/P{page}PCA stages as direct "
        "human-approved stages.\n\n"
        "Pages `001-020` are page-complete accepted only after this P016-P020 final-review set. "
        "Page 021+ remains unprocessed and unauthorized by this record.\n",
    )
    write_manifest(page)


def build() -> None:
    for page in PAGES:
        build_page_review(page)


if __name__ == "__main__":
    check_authorization()
    build()
