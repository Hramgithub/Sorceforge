from __future__ import annotations

from pathlib import Path
from typing import Any


BOUNDED_AUTHORIZATION_SCHEMA_VERSION = "sourcefold_bounded_authorization.v1"
AGGRESSIVE_BATCH_AUTHORIZATION_SCHEMA_VERSION = "sourcefold_aggressive_batch_authorization.v1"
AUTHORITY_LEAKAGE_FLAGS = [
    "page_complete_acceptance_created",
    "whole_gate_1_acceptance_created",
    "fixture_admission_created",
    "source_acceptance_created",
    "pcrp_created",
]


def validate_bounded_authorization(
    *,
    artifact: dict[str, Any],
    expected_authorization_id: str,
    ledger_text: str,
    allowed_scope_markers: list[str],
    created_capabilities: dict[str, bool],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    actual_authorization_id = artifact.get("authorization_id")
    if actual_authorization_id != expected_authorization_id:
        findings.append(
            {
                "finding_id": "bounded_authorization_id_mismatch",
                "expected": expected_authorization_id,
                "actual": actual_authorization_id,
            }
        )
    if f"## {expected_authorization_id}" not in ledger_text:
        findings.append({"finding_id": "bounded_authorization_missing_from_ledger", "authorization_id": expected_authorization_id})
    scope = str(artifact.get("scope", ""))
    if allowed_scope_markers and not any(marker in scope for marker in allowed_scope_markers):
        findings.append({"finding_id": "bounded_authorization_scope_not_allowed", "scope": scope, "allowed_scope_markers": allowed_scope_markers})
    leaked = [flag for flag in AUTHORITY_LEAKAGE_FLAGS if created_capabilities.get(flag) is True]
    if leaked:
        findings.append({"finding_id": "bounded_authorization_leaked_authority", "flags": leaked})
    return {
        "schema_version": BOUNDED_AUTHORIZATION_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "authorization_id": expected_authorization_id,
        "allowed_scope_markers": allowed_scope_markers,
        "findings": findings,
    }


def _assert_nonblank(value: str, field: str) -> None:
    if not value:
        raise ValueError(f"{field} must be non-empty")


def aggressive_batch_authorization_artifact(
    *,
    authorization_id: str,
    page: str,
    lane_id: str,
    authority: str,
    exact_action: list[str],
    admitted_inputs: list[dict[str, str]],
    allowed_outputs: list[str],
    limits: list[str],
) -> dict[str, Any]:
    _assert_nonblank(authorization_id, "authorization_id")
    _assert_nonblank(page, "page")
    _assert_nonblank(lane_id, "lane_id")
    _assert_nonblank(authority, "authority")
    expected_page_token = f"PAGE-{page}"
    expected_batch_token = f"P{page}BATCH"
    if expected_page_token not in authorization_id:
        raise ValueError(f"authorization_id must include {expected_page_token}")
    if expected_batch_token not in lane_id:
        raise ValueError(f"lane_id must include {expected_batch_token}")
    if not exact_action:
        raise ValueError("exact_action must list at least one action")
    if not admitted_inputs:
        raise ValueError("admitted_inputs must list at least one input")
    if not allowed_outputs:
        raise ValueError("allowed_outputs must list at least one output")
    if not limits:
        raise ValueError("limits must list at least one limit")

    return {
        "schema_version": AGGRESSIVE_BATCH_AUTHORIZATION_SCHEMA_VERSION,
        "authorization_id": authorization_id,
        "page": page,
        "lane_id": lane_id,
        "status": "active_scope_materialized",
        "authority": authority,
        "exact_action": exact_action,
        "admitted_inputs": admitted_inputs,
        "allowed_outputs": allowed_outputs,
        "limits": limits,
        "final_review_model": f"P{page}BATCH final bundle plus post-P{page} status only",
        "guardrails": {
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
            f"page_{int(page) + 1:03d}_plus_processing": False,
        },
    }


def aggressive_batch_authorization_markdown(artifact: dict[str, Any]) -> str:
    lines = [
        f"## {artifact['authorization_id']}",
        "",
        "Status: `active_scope_materialized`",
        "",
        f"Lane: `{artifact['lane_id']}`",
        "",
        "Created by: `aggressive_batch_authorization_preflight`",
        "",
        f"Authority: {artifact['authority']}",
        "",
        "Exact action:",
        "",
    ]
    lines.extend(f"- {item}" for item in artifact["exact_action"])
    lines.extend(["", "Admitted inputs:", ""])
    lines.extend(f"- `{item['name']}`: `{item['sha256']}`" for item in artifact["admitted_inputs"])
    lines.extend(["", "Allowed outputs:", ""])
    lines.extend(f"- `{item}`" for item in artifact["allowed_outputs"])
    lines.extend(["", "Limits:", ""])
    lines.extend(f"- {item}" for item in artifact["limits"])
    lines.extend(
        [
            "",
            "Final review model:",
            "",
            f"- `{artifact['final_review_model']}`.",
            "- Do not create final human batch-review acceptance before Bogdan gives the exact final bundle/status decision.",
            "",
        ]
    )
    return "\n".join(lines)


def materialize_aggressive_batch_authorization(
    *,
    ledger_path: Path,
    authorization_id: str,
    page: str,
    lane_id: str,
    authority: str,
    exact_action: list[str],
    admitted_inputs: list[dict[str, str]],
    allowed_outputs: list[str],
    limits: list[str],
) -> dict[str, Any]:
    artifact = aggressive_batch_authorization_artifact(
        authorization_id=authorization_id,
        page=page,
        lane_id=lane_id,
        authority=authority,
        exact_action=exact_action,
        admitted_inputs=admitted_inputs,
        allowed_outputs=allowed_outputs,
        limits=limits,
    )
    ledger_text = ledger_path.read_text(encoding="utf-8-sig") if ledger_path.exists() else ""
    if f"## {authorization_id}" not in ledger_text:
        prefix = "" if ledger_text.endswith("\n") or not ledger_text else "\n"
        ledger_path.parent.mkdir(parents=True, exist_ok=True)
        ledger_path.write_text(
            ledger_text + prefix + aggressive_batch_authorization_markdown(artifact) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    return artifact


def assert_aggressive_page_builder_uses_authorization_preflight(script_path: Path) -> None:
    source = script_path.read_text(encoding="utf-8")
    script_name = script_path.name
    if "bounded_authorization_contract" not in source:
        raise ValueError(f"{script_name} must import the aggressive authorization preflight contract")
    if "materialize_aggressive_batch_authorization(" not in source:
        raise ValueError(f"{script_name} must call materialize_aggressive_batch_authorization")
    if "aggressive_batch_authorization_preflight" not in source:
        raise ValueError(f"{script_name} must name aggressive_batch_authorization_preflight in authority/materialization metadata")
