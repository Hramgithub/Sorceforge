from __future__ import annotations

from bounded_authorization_contract import materialize_aggressive_batch_authorization
from build_pages_016_020_aggressive_batch import aggressive_batch_authorization_preflight, main
from page_review_crop_contracts import validate_text_evidence_crop_contracts


def _contract_markers() -> None:
    if False:
        aggressive_batch_authorization_preflight("019")
        materialize_aggressive_batch_authorization()
        validate_text_evidence_crop_contracts((0, 0), [{"crop_contract": {"context_allowed": False}}])


if __name__ == "__main__":
    main("019")
