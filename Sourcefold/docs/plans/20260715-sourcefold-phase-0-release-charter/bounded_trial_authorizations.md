# Gate 1 Bounded Trial Authorizations

Goal id: `20260715-sourcefold-phase-0-release-charter`

This ledger records action-specific trial permissions. A protocol revision being
`accepted_protocol` does not authorize candidate-derived work by itself.

## BA-G1-VIRAL-AGGRESSIVE-BATCH-AUTHORIZATION-PREFLIGHT-001

Status: `scope_consumed`; hardening complete, not a page artifact

Created: 2026-07-26

Authority: Bogdan Telegram message `2017`: "зови сол и терру и внедряй"

Exact action:

- Add a Sourcefold-native aggressive batch authorization materialization
  preflight.
- Require every `build_page_*_aggressive_batch.py` builder to call
  `materialize_aggressive_batch_authorization()` before page output generation.
- Keep exact `--execute --authorization-id` fail-closed behavior.
- Materialize only a page-specific `BA-G1-VIRAL-PAGE-0XX-AGGRESSIVE-BATCH-001`
  section when the exact page authorization id, page id, lane id, admitted
  inputs, allowed outputs, and limits are provided.
- Keep final batch review acceptance separate until Bogdan gives the exact
  `p0xx aggressive batch ok` decision.

Allowed outputs:

- `scripts/bounded_authorization_contract.py`
- `scripts/build_page_012_aggressive_batch.py`
- `scripts/build_page_013_aggressive_batch.py`
- `scripts/build_page_014_aggressive_batch.py`
- `tests/test_bounded_authorization_contract.py`
- Status/roadmap/plan/context documentation sync for the aggressive batch
  authorization preflight.

Limits:

- Do not start or process page 015.
- Do not retrofit P014 history or create new P014 artifacts.
- Do not create final human batch-review acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR execution,
  render execution, PDF parsing/text-layer extraction, raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Output status:

- Authorization contract script SHA-256:
  `437FBFF33D4CCC3760FF92CD624602D648DB88EC2E284B00D3EC27443325EDA1`
- Authorization contract test SHA-256:
  `3EBA3010044929D22A7A6FA042894C5F2DB2AECC062EBE34339EAED2F8411D74`
- P012 aggressive builder SHA-256:
  `F776EDE77F25970ED54FE9C08817102298C4F9AE2B12810A5B6613A3646C7897`
- P013 aggressive builder SHA-256:
  `4522F36A520AED599335B8CD25BA600D5A50E0505B97A7003AFEFA68EF84FBED`
- P014 aggressive builder SHA-256:
  `A8D175F473807C27B8119F6601DC27C54D5D52B8CF81FC4C4385D3B0B161BF96`
- Result: future aggressive page builders must materialize page-specific
  bounded authorization as a preflight artifact before internal page output
  generation.

## BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001

Status: `scope_consumed`; prep/hardening complete, no page 016+ processing

Created: 2026-07-26

Authority: Bogdan Telegram message `2059`: "Моё предпочтение: сначала идти без новой bulk-обвязки. Собрать 016-20 последовательно, показать тебе 10 файлов: 5 source pages + 5 semantic maps. зафиксируй это в наш план. и сделай нужные доработки , после сделай комит. чтобы я запустил работу"

Exact action:

- Record the planned P016-P020 sequential aggressive run mode.
- Add a Sourcefold contract for the human review packet shape.
- Human review packet must expose only source page art and semantic text map
  markdown for pages 016-020.
- Keep crop evidence and other generated internal artifacts as internal
  machine-review evidence unless a blocker requires escalation.

Allowed outputs:

- `scripts/aggressive_review_packet_contract.py`
- `tests/test_aggressive_review_packet_contract.py`
- `PROJECT_STATUS.md`
- `docs/roadmap/roadmap.yaml`
- `docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md`
- `docs/plans/20260715-sourcefold-phase-0-release-charter/context.md`
- `docs/plans/20260715-sourcefold-phase-0-release-charter/bounded_trial_authorizations.md`

Limits:

- Do not create P016TR/P016TXT/P016SEM/PCRP/PCA or any P016-P020 page
  artifacts under this prep authorization.
- Do not materialize page-specific
  `BA-G1-VIRAL-PAGE-0XX-AGGRESSIVE-BATCH-001` sections before the actual
  sequential run starts.
- Do not create a bulk final-review acceptance helper.
- Do not process page 021 or later.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw,
  translate, proofread, implement, push, or create final batch review.

Output status:

- Prep id: `P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001`
- Status: `ready_to_start_after_explicit_run_command`
- Review packet contract script SHA-256:
  `3378E2D1BB8A21350E3129A60CA54E7CD1D8D1F2EC6F2BC408CB9C61244400D6`
- Review packet contract test SHA-256:
  `CF398E6839D437B6B2C98054ECA1E247567E92391D8D18DEF67C3DF340FD2F13`
- Result: future P016-P020 sequential aggressive run should present only ten
  human review files by default: source page art and semantic text map markdown
  for pages 016, 017, 018, 019, and 020.

## BA-G1-VIRAL-KEEPER-NOTES-CALLOUT-HEADING-LEVEL-001

Status: `scope_consumed`

Created: 2026-07-26

Authority: Bogdan Telegram message `1982`: "давай для киперснот тоже сделаем
какое то правило типа всегда н4? и чтобы это не влияло на другие заголовки"

Exact action:

- Add a narrow shared semantic helper for `Keeper's Notes` callout headings.
- Normalize `Keeper's Notes` callout headings to `h4`.
- Keep the rule scoped only to `Keeper's Notes` callout labels; do not change
  regular section/item headings.
- Regenerate the affected P012/P013/P014 semantic and downstream hash-bound
  artifacts.
- Update tests, roadmap, status, plan/context, and authorization ledger.

Allowed outputs:

- `scripts/page_review_semantic_units.py`
- `scripts/build_page_012_aggressive_batch.py`
- `scripts/build_page_013_aggressive_batch.py`
- `scripts/build_page_014_aggressive_batch.py`
- `scripts/accept_page_012_aggressive_batch_review.py`
- `scripts/accept_page_013_aggressive_batch_review.py`
- `tests/test_page_012_aggressive_batch.py`
- `tests/test_page_013_aggressive_batch.py`
- `tests/test_page_014_aggressive_batch.py`
- `tests/test_page_complete_review.py`
- Regenerated P012/P013/P014 semantic, review, acceptance, status, batch, and
  final-review artifacts affected by the hash cascade.
- Status/roadmap/plan/context documentation sync for the Keeper's Notes
  callout-heading rule.

Limits:

- Do not create final P014 human batch-review acceptance.
- Do not record direct Bogdan approval for internal P012/P013/P014 delegated
  stages.
- Do not process page 015 or later.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR execution,
  render execution, PDF parsing/text-layer extraction, raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Output status:

- Semantic helper script SHA-256:
  `A7377E659DD9B1E26D15875BA50FB077D7520F243A732F6517D6C86CD42F449F`
- P012 Keeper's Notes updated: `SU-P012-KEEPER-001` is an `h4` block heading
  with `display_style=callout_heading`.
- P014 Keeper's Notes callout headings already use `h4` and now call the shared
  helper.
- Result: `Keeper's Notes` callout labels use `h4` without changing ordinary
  section/item headings.

## BA-G1-VIRAL-RUN-IN-OPTION-HEADING-DEPTH-001

Status: `scope_consumed`

Created: 2026-07-26

Authority: Bogdan Telegram message `1915`: "давай внедрим это и сделаем
коммит"

Exact action:

- Add a shared semantic helper for nested run-in option heading depth.
- Record run-in option labels under a parent subsection as
  parent-heading-level-plus-one, capped at `h6`.
- Keep inline/run-in layout, underline/style, and continuation metadata separate
  from structural heading level.
- Regenerate the affected P012/P013 semantic and downstream hash-bound artifacts.
- Update tests, roadmap, status, plan/context, and commit the Sourcefold scope.

Allowed outputs:

- `scripts/page_review_semantic_units.py`
- `scripts/build_page_012_aggressive_batch.py`
- `scripts/build_page_013_aggressive_batch.py`
- `scripts/accept_page_012_aggressive_batch_review.py`
- `tests/test_page_012_aggressive_batch.py`
- `tests/test_page_013_aggressive_batch.py`
- Regenerated P012/P013 semantic, review, acceptance, status, batch, and
  final-review artifacts affected by the hash cascade.
- Status/roadmap/plan/context documentation sync for the semantic-depth rule.

Limits:

- Do not create final P013 human batch-review acceptance.
- Do not record direct Bogdan approval for internal P012/P013 delegated stages.
- Do not process page 014 or later beyond inert continuation metadata visible on
  page 013.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR execution,
  render execution, PDF parsing/text-layer extraction, raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Output status:

- Semantic helper script SHA-256:
  `A7377E659DD9B1E26D15875BA50FB077D7520F243A732F6517D6C86CD42F449F`
- P012 nested option label updated: `SU-P012-CNI-007` `Mythos Investigators`
  is an `h4` inline heading.
- P013 nested option labels updated: `SU-P013-CNI-002` `Documentary Film Crew`,
  `SU-P013-CNI-004` `Tourists`, and `SU-P013-CNI-006` `Pesky Teenagers` are
  `h4` inline headings.
- Result: nested run-in option labels under `Other Investigator Options.` now
  use parent-heading-level-plus-one semantics, capped at `h6`.

## BA-G1-VIRAL-PAGE-014-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Created: 2026-07-26

Authority: Bogdan Telegram message `1948`: "коммит и пошли делать агрессив
страницу 14"

Exact action:

- Create a page 014 aggressive batch lane under `P014BATCH-G1-VIRAL-001`.
- Consume `P013BATCHREV-G1-VIRAL-001`, `P013BATCH-G1-VIRAL-001`, and
  `G1SP-G1-VIRAL-008` as the committed predecessor state.
- Process `images/page_014.png` only.
- Generate internal P014TR/P014TXT/P014SEM/PCRP/P014PCA artifacts with
  `human_review_skipped_by_explicit_authorization`, never as direct Bogdan
  per-stage approval.
- Require Sol and Terra OK/no-blocker evidence at each internal stage.
- Enforce the shared aggressive crop provenance gate for every page 014
  text-evidence crop.
- Apply the run-in option heading rule where applicable.
- Generate post-P014 status refresh and a final human-facing bundle that exposes
  all artifacts from internal stages.
- Present final post-P014 status plus bundle artifacts to Bogdan for review.

Allowed outputs:

- `scripts/build_page_014_aggressive_batch.py`
- `scripts/accept_page_014_aggressive_batch_review.py`
- `tests/test_page_014_aggressive_batch.py`
- `tests/test_page_014_aggressive_batch_final_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_014_triage_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_014_text_extraction_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_014_semantic_text_map_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p014_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p014_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_009/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_014_aggressive_batch_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_014_aggressive_batch_final_review_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync for the page 014 aggressive
  batch lane.

Limits:

- Do not record direct Bogdan approval for P014TR/P014TXT/P014SEM/PCRP/P014PCA.
- Do not create final human batch-review acceptance before Bogdan reviews the
  P014 bundle/status.
- Do not process page 015 or later beyond inert continuation metadata visible on
  page 014.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR execution,
  render execution, PDF parsing/text-layer extraction, raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Output status:

- Batch id: `P014BATCH-G1-VIRAL-001`
- Status: `ready_for_final_human_review`
- Builder script SHA-256:
  `A6F54E09C231D5BCA981F4B6F565C10B5E21B34DCF85269AD489E1FE8E077D53`
- Test SHA-256:
  `A5EFB1D9976446BF5912EAB0BCCEDDF0FC758CC879A3C1CE05FD3A5AFE14F4E4`
- P014 triage packet SHA-256:
  `6FF94ECB0943805B4B2A5AE15EAC652B4286491233AEBE99F85DB7B2EE7A0CC0`
- P014 text extraction packet SHA-256:
  `1D0785B202CF9BB0B4EB970EAA9E464FDD71EC1431D846B36089B08564FD8ACE`
- P014 semantic map JSON SHA-256:
  `0863D41CAFEB1E0F80419EFFE42921CDAF15B1A3A1BF39FABA69ADC38A24B385`
- P014 PCRP report SHA-256:
  `CE0434746576703BD7D16A62D1C4C61DAA541F3359D2999AB79319B43CF0B641`
- P014 delegated page-complete acceptance report SHA-256:
  `31B80BEFF013A843C5792C6B87A5635427993726BA2A3C501B119239DA2B7550`
- Post-P014 status packet SHA-256:
  `E0F15FCA01D32C95D41EBCA87D87EDCEEEE59A2C503FF0965614169BF0159B54`
- Batch report SHA-256:
  `B6A92DB8CCE23BE536D2D47F52E3B9A8D9832C143AEAD574B93790285A277F01`
- Final review id: `P014BATCHREV-G1-VIRAL-001`
- Final review script SHA-256:
  `1EC236445DEE2B2A9C28D90064AD239137B12723AEA66DE96A81031F3D4AFB8C`
- Final review test SHA-256:
  `1D128D59CFF408B79439B16B1925AEC279F3093306E8D14C9CF331E56DF788BA`
- Final review report SHA-256:
  `FF8C193BB61A5D6A12F1E60EC7C853EB164CD1EC10A92A058A591200B430A76B`
- Result: page 014 aggressive batch final human review accepted with
  `p014 aggressive batch ok`.
- Internal P014TR/P014TXT/P014SEM/PCRP/P014PCA stages record
  `human_review_skipped_by_explicit_authorization` and Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Final review target was the batch plus `G1SP-G1-VIRAL-009`; this final
  review acceptance does not convert internal stages into direct Bogdan
  per-stage approvals.

## BA-G1-VIRAL-PAGE-013-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Created: 2026-07-26

Authority: Bogdan Telegram message `1897`: "Запускай страницу 13 в агрессивном
режиме"

Exact action:

- Create a page 013 aggressive batch lane under `P013BATCH-G1-VIRAL-001`.
- Generate internal P013TR/P013TXT/P013SEM/PCRP/P013PCA artifacts with
  `human_review_skipped_by_explicit_authorization`, never as direct Bogdan
  per-stage approval.
- Require Sol and Terra OK/no-blocker evidence at each internal stage.
- Enforce the shared aggressive crop provenance gate for every page 013
  text-evidence crop.
- Generate post-P013 status refresh and a final human-facing bundle that exposes
  all artifacts from internal stages.
- Present final post-P013 status plus bundle artifacts to Bogdan for review.

Allowed outputs:

- `scripts/build_page_013_aggressive_batch.py`
- `tests/test_page_013_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_013_triage_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_013_text_extraction_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_013_semantic_text_map_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p013_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p013_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_008/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_013_aggressive_batch_G1_VIRAL_001/*`
- `scripts/accept_page_013_aggressive_batch_review.py`
- `tests/test_page_013_aggressive_batch_final_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_013_aggressive_batch_final_review_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync for the page 013 aggressive
  batch lane.

Limits:

- Do not record direct Bogdan approval for P013TR/P013TXT/P013SEM/PCRP/P013PCA.
- Do not create final human batch-review acceptance before Bogdan reviews the
  P013 bundle/status.
- Do not process page 014 or later beyond inert continuation metadata visible on
  page 013.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR execution,
  render execution, PDF parsing/text-layer extraction, raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Output status:

- Batch id: `P013BATCH-G1-VIRAL-001`
- Status: `final_human_review_accepted`
- Builder script SHA-256:
  `356945D0BCAFD80C71000FAA3B97F502E39FC10CC0CCEE9555029D7DDAD4A591`
- Test SHA-256:
  `6358C19F1FCD44B3C39106420E7CD9764064A91B2F8B9EEDDB77AAC9B7DDD564`
- P013 triage packet SHA-256:
  `2724A753543F5903EA8CE10176B5A88C206DBE479FF3DED72701273D5C8B5879`
- P013 text extraction packet SHA-256:
  `36D0AF4F99CE9F949CF5B06F86056AB3FB39E734C53DB749FFB99FF9BBC540A4`
- P013 semantic map JSON SHA-256:
  `31B9D7AAFD21EF9F076298FCDE588B57A4B2E81749B1D86EEFF7B2D1D002F185`
- P013 PCRP report SHA-256:
  `F1BC9C58216196E746CB9D39DEB6EE8657D890EB36FBE9AA1576895CC360FC11`
- P013 delegated page-complete acceptance report SHA-256:
  `1942DE32B97EC1EDB9D47AD76EB2D3E7D164E8C968367BBD696A26F863F5E95E`
- Post-P013 status packet SHA-256:
  `EED84F376597007FECA15774E4DCFEDEFC3F619278985BEB11E0D46295565725`
- Batch report SHA-256:
  `E3BA4F29DFCD3E47B562630522E8BDEDDEE7C8C001EB60F2E910E648698D14E2`
- Final review id: `P013BATCHREV-G1-VIRAL-001`
- Final review script SHA-256:
  `84E318AB604509115801B85E7EDD0EE36FAC6AFA875FE1C398EACC9433AC7FE8`
- Final review test SHA-256:
  `BB31248EAD7C56F3225EC9F6E34E50F5455D2DD7EAA485F2E4E9AC887C89A9D7`
- Final review report SHA-256:
  `3C9AF88656119DE46753B6F8454B5BE36C331BE212E3A133A3E5BF8F163D63F4`
- Result: page 013 aggressive batch final human review accepted with
  `p013 aggressive batch ok`.
- Internal P013TR/P013TXT/P013SEM/PCRP/P013PCA stages record
  `human_review_skipped_by_explicit_authorization` and Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Run-in option labels under `Other Investigator Options.` use h4 inline
  headings under the parent h3 subsection.
- Final review target was the batch plus `G1SP-G1-VIRAL-008`; this final
  review acceptance does not convert internal stages into direct Bogdan
  per-stage approvals.

## BA-G1-VIRAL-AGGRESSIVE-CROP-PROVENANCE-GATE-001

Status: `active_scope_materialized`; hardening complete, not a page artifact

Created: 2026-07-26

Authority: Bogdan Telegram message `1891`: "сделай, чтобы я мог потом просто
сказать запусти - страницу 13 в агресив режиме"

Exact action:

- Promote the P012 crop provenance contract from a reusable module plus first
  consumer into a mandatory aggressive-builder gate.
- Discover `build_page_*_aggressive_batch.py` builders under `scripts/`.
- Fail closed when an aggressive page builder does not import/call the shared
  crop contract validator.
- Fail closed when an aggressive page builder omits explicit `crop_contract` or
  `context_allowed` metadata for text-evidence blocks.
- Preserve the P012 aggressive batch semantics and final-review acceptance.

Allowed outputs:

- `scripts/page_review_crop_contracts.py`
- `tests/test_page_review_crop_contracts.py`
- Status/roadmap/plan/context documentation sync for the aggressive crop
  provenance gate.

Limits:

- Do not create page 013 artifacts.
- Do not process page 013 or page 014+.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR execution,
  render execution, PDF parsing/text-layer extraction, raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Output status:

- Status: `aggressive_builder_crop_provenance_gate_ready`
- Crop contract validator script SHA-256:
  `9A6E1406A61AAA09ED0069AA5E2B9095C53C9EA8B13B80F336BB499C075DA089`
- Crop contract validator test SHA-256:
  `CA943B0C5A7913E410354C70FA560C9B3C87D219E8D01510828BEC2FC879E487`
- Result: future `build_page_*_aggressive_batch.py` builders are covered by
  shared crop provenance QA; page 013 can be started in aggressive mode without
  restating the crop-contract requirement.

## BA-G1-VIRAL-PAGE-012-AGGRESSIVE-BATCH-001

Status: `expired`; scope consumed by `P012BATCH-G1-VIRAL-001`

Created: 2026-07-26

Authority: Bogdan Telegram message `1806`: "Давай по агрессивной модели, мы
просто помечаем что хуман ревью скипед, но на каждом из этапов у нас есть
двойное ревью сол и Терры."

Exact action:

- Create a page 012 aggressive batch lane under `P012BATCH-G1-VIRAL-001`.
- Generate internal P012TR/P012TXT/P012SEM/PCRP/P012PCA artifacts with
  `human_review_skipped_by_explicit_authorization`, never as direct Bogdan
  per-stage approval.
- Require Sol and Terra OK/no-blocker evidence at each internal stage.
- Generate post-P012 status refresh and a final human-facing bundle that exposes
  all artifacts from internal stages.
- Present final post-P012 status plus bundle artifacts to Bogdan for review.

Allowed outputs:

- `scripts/build_page_012_aggressive_batch.py`
- `tests/test_page_012_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_012_triage_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_012_text_extraction_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_012_semantic_text_map_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p012_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p012_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_007/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_012_aggressive_batch_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync for the page 012 aggressive
  batch lane.

Limits:

- Do not record direct Bogdan approval for P012TR/P012TXT/P012SEM/PCRP/P012PCA.
- Do not process page 013 beyond inert continuation metadata visible on page
  012.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR execution,
  render execution, PDF parsing/text-layer extraction, raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Output status:

- Batch id: `P012BATCH-G1-VIRAL-001`
- Status: `final_human_review_accepted`
- Builder script SHA-256:
  `52C73F49581DF8831C7B75309A9DCAAE557979805FD9F417813B2F9EB09915ED`
- Crop contract validator script SHA-256:
  `4A5BA2BD35F978CAD6FFADC5A408EB6AE21B48ACBBE3C82247B5DE8775BA75E9`
- Test SHA-256:
  `025200667CEDB09FD434A5E0C47F4B23C4A2B4B9B25051750D21C8D0EA8793A0`
- Crop contract validator test SHA-256:
  `0681194C310A84B95841C2440D54806929A4BC6C42F20EB06A922D6705775B08`
- P012 triage packet SHA-256:
  `93A2CCE7F4F639BFC10CAA33840FB587491FCA89827188ECDD53586B8E6A4689`
- P012 text extraction packet SHA-256:
  `709F33CD29B6127CF62316D1AA648422272C722D3016F52575D56566003EF65F`
- P012 semantic map JSON SHA-256:
  `A4207C296B485C44E8194BE83F06BAE3607E00C4CC1D78493A6EB3162867FC9F`
- P012 PCRP report SHA-256:
  `A7E3B1EE2171831A5A6A11966D8428CEEA6D3431DF5BF5F6315CD6DCFF48376C`
- P012 delegated page-complete acceptance report SHA-256:
  `DBE7DC6732FF664064E61CE11E568A510A066D703B4E208D87A76BBD90DB86D3`
- Post-P012 status packet SHA-256:
  `37651668FD8FF162DC6205A7EB244589548C78789BBB0083E2E5FCD85C224E9B`
- Batch report SHA-256:
  `6D9E6846A4F3E1189C2B59ACC56CD67406CDE60C10DE14B05861FD1EA16B219A`
- Final review script SHA-256:
  `9083A721A23F4579C38217C4C0B38F6C46FF646021F014994B9D3D001AFF1807`
- Final review test SHA-256:
  `3458CA56FADF1A483FD54FA8FD58CD94DD212F0593A8641AAC05C57CB22E294B`
- Final review report SHA-256:
  `8D80434F97AB753024B1E0BA90494CA809CF97A63D4F577B8F65796A985D71F7`
- Result: page 012 aggressive batch final human review accepted with
  `p012 aggressive batch ok`.
- Internal P012TR/P012TXT/P012SEM/PCRP/P012PCA stages record
  `human_review_skipped_by_explicit_authorization` and Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Run-in option label `Mythos Investigators` under `Other Investigator Options.`
  uses an h4 inline heading under the parent h3 subsection.
- Final review target was the batch plus `G1SP-G1-VIRAL-007`; this final
  review acceptance does not convert internal stages into direct Bogdan
  per-stage approvals.

## BA-G1-VIRAL-GATE-1-STATUS-REFRESH-006

Status: `expired`; scope consumed by `G1SP-G1-VIRAL-006`

Created: 2026-07-26

Authority: Bogdan Telegram message `1783`: "Сделай только п11 статус рефреш",
after `P011PCA-G1-VIRAL-001` accepted page 011 as page-complete only and the
roadmap required a post-P011 status refresh before any page 012 work.

Exact action:

- Create `G1SP-G1-VIRAL-006` as a post-P011 Gate 1 status/route packet only.
- Consume exact post-P010 status route packet `G1SP-G1-VIRAL-005`.
- Consume `P001PCA-G1-VIRAL-001` through `P011PCA-G1-VIRAL-001` as
  page-complete accepted pages only.
- Update the blocker matrix so pages 001-011 are complete and
  `pages_012_020_unstarted=true`.
- Preserve OCR benchmark remediation and source-profile/Gate-1 parameter
  parking/acceptance as separate unresolved branches.
- Recommend page 012 triage/readiness as the next candidate without authorizing
  page 012 processing inside this packet.

Allowed outputs:

- `scripts/build_gate_1_status_refresh_post_p011.py`
- `tests/test_gate_1_status_refresh_post_p011.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_006/*`
- Status/roadmap/plan/context documentation sync that records the post-P011
  status route packet.

Limits:

- Do not accept whole Gate 1.
- Do not authorize the next layer from inside this packet.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not create a new source-reconstruction rollup.
- Do not process page 012 inside this status packet.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this status packet without
  separate bounded authorization.

Output status:

- Status packet id: `G1SP-G1-VIRAL-006`
- Status: `gate_1_status_route_packet_ready_no_acceptance`
- Post-P011 status refresh script SHA-256:
  `1C7EA239274E4B162C809808E090A5395452F280DD377FC249E29D5989857F65`
- Post-P011 status refresh test SHA-256:
  `FACC3CF4E395B4CB3D3E84A719571A7B88EB404CB7F1FF036ABBC45FCE9A0B0B`
- Gate 1 status packet JSON SHA-256:
  `E79EF8C4941184724D2E654799DA7DAEAAD4E0B29E4D52C9379D0DA5BD533822`
- Gate 1 status report SHA-256:
  `B300B3A8A54E5B472AB836B10959402E6E4194F77DAB4FA9CC76C717B3C136C3`
- Gate 1 status summary SHA-256:
  `C823A9195B0A408B6DFE3441CB28827B6DC47CFFB30C46788228245862C6FB36`
- Gate 1 status manifest SHA-256:
  `C44FA63AADBE40457C0F25321FADB2BCD9955B8FD378071C570EEA77018B0045`
- Result: post-P011 Gate 1 status/route packet is ready for review.
- Pages 001-011 are page-complete accepted only; pages 012-020 remain
  unstarted at this status layer.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 012 processing authorization, and raw mutation
  remain false.

## BA-G1-VIRAL-GATE-1-STATUS-REFRESH-004

Status: `expired`; scope consumed by `G1SP-G1-VIRAL-004`

Created: 2026-07-25

Authority: Bogdan Telegram message `1409`: "Ок делай по плану", after the
recommended next plan was post-P009 Gate 1 status/route refresh followed by
page 010 triage/readiness.

Exact action:

- Create `G1SP-G1-VIRAL-004` as a post-P009 Gate 1 status/route packet only.
- Consume `G1SP-G1-VIRAL-003` as the stale predecessor status packet.
- Consume `P001PCA-G1-VIRAL-001` through `P009PCA-G1-VIRAL-001` as
  page-complete accepted pages only.
- Update the blocker matrix so pages 001-009 are complete and
  `pages_010_020_unstarted=true`.
- Preserve OCR benchmark remediation and source-profile/Gate-1 parameter
  parking/acceptance as separate unresolved branches.
- Recommend page 010 triage/readiness as the next candidate without authorizing
  page 010 processing inside this packet.

Allowed outputs:

- `scripts/build_gate_1_status_refresh_post_p009.py`
- `tests/test_gate_1_status_refresh_post_p009.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_004/*`
- Status/roadmap/plan/context documentation sync that records the post-P009
  status route packet.

Limits:

- Do not accept whole Gate 1.
- Do not authorize the next layer from inside this packet.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not create a new source-reconstruction rollup.
- Do not process page 010 inside this status packet.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this status packet without
  separate bounded authorization.

Output status:

- Status packet id: `G1SP-G1-VIRAL-004`
- Status: `gate_1_status_route_packet_ready_no_acceptance`
- Post-P009 status refresh script SHA-256:
  `F8B53C597E703B060235E9BAA8628CFCF0F160228891C03FC609A5B4436D695F`
- Post-P009 status refresh test SHA-256:
  `F15435CA52E46C9DAD9D08BE8DF4A01220DC84AFEF81DEC1A3D18C240243EDB4`
- Gate 1 status packet JSON SHA-256:
  `970AEEF0161A081AB3535057F311B0CA17F8F5AD56F3F35EA3E7350657E26761`
- Gate 1 status report SHA-256:
  `CD7A352C1D9D28ABF7575608F293FDF33534AA2997C59C7CE1B227E7789FE317`
- Gate 1 status summary SHA-256:
  `C08C40A693920EB48DF2982F0C1C3C2B89CD9E5E00BC4CA4E5505F2AF3D3899A`
- Gate 1 status manifest SHA-256:
  `B3A2E948AAF9EC4F0149C86F2BCFFC863C025F50B4ECA17F734D48377E2E58A9`
- Result: post-P009 Gate 1 status/route packet is ready for review.
- Pages 001-009 are page-complete accepted only; pages 010-020 remain
  unstarted at this status layer.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 010 processing authorization, and raw mutation
  remain false.

## BA-G1-VIRAL-PAGE-010-TRIAGE-001

Status: `active`; implementation verified, Bogdan review pending

Created: 2026-07-25

Authority: Bogdan Telegram message `1409`: "Ок делай по плану", after the
recommended next plan was post-P009 Gate 1 status/route refresh followed by
page 010 triage/readiness.

Exact action:

- Create `P010TR-G1-VIRAL-001` as a page 010 triage/readiness crop-contract
  packet for Bogdan review only.
- Consume `G1SP-G1-VIRAL-004` as the immediate route predecessor.
- Use the existing rendered page 010 image and existing map/inventory evidence.
- Package page 010 as a dual-profile mixed page with three text-like PRM
  regions and two portrait/image anchors.
- Apply crop role separation from the first packet:
  `source_region_box_px`, `human_review_crop_box_px`,
  `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`.
- Represent lower `PRM-G1-VIRAL-001-P010-R05` as two independent lower text
  blocks by visible column while preserving `R05` as the source-region lineage.
- Do not create a shared lower human-review crop for `R05`; each derived lower
  text block must have its own `human_review_crop_box_px`,
  `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`.

Allowed outputs:

- `scripts/build_page_010_triage.py`
- `tests/test_page_010_triage.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_triage_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records page 010
  triage/readiness routing only.

Limits:

- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 011-020.
- Do not run OCR, create OCR output, create text extraction, create semantic
  text maps, create PCRP, rerender the PDF, parse or inspect the PDF or PDF text
  layer, mutate raw artifacts, translate, proofread, accept renderer/profile
  behavior, implement runtime behavior, push, or broaden this triage without
  separate bounded authorization.

Output status:

- Package id: `P010TR-G1-VIRAL-001`
- Status: `page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp`
- Page 010 triage script SHA-256:
  `3BBF0D75AC99D0EFF46D19ED64F8B70E26594E6E29C2094039A0D423A6345745`
- Page 010 triage test SHA-256:
  `4556AE8FD1ACF09A10498D75697DAE68C9C14DB8825C6D92956E09E5D2BE51A1`
- Page 010 triage packet SHA-256:
  `5585073CAAB1BE31130290DD9597714827AF55D9DC4C7C5146EF757EE9330A3B`
- Page 010 triage report SHA-256:
  `DC70BF29B11577728D4CEE5E02205D4AB8A087AF76CE0849FD82394691C74CCF`
- Page 010 triage summary SHA-256:
  `A9AFF4566DF805F16B4D9B26C80220751DC80D5E5A6BD7712076CE87C476283F`
- Page 010 triage manifest SHA-256:
  `1EAC61826A4E86392875227922FAD5D165402AE95DAA6F6AB61794F2E361AD3D`
- Result: page 010 is routed for Bogdan review as a dual-profile mixed page
  with crop-role separation from the first triage packet.
- Crop QA passed after tightening/refining OCR/text evidence surfaces:
  `R01`, `R02`, and lower `R05` are represented; lower `R05` is modeled as
  two peer text blocks, left Hyeon and right Maya, with no shared lower
  human-review crop.
- Page 010 is not accepted as complete by this packet.
- Pages 011-020 are not processed.

## BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001

Status: `scope_consumed`; materialized `P010TXT-G1-VIRAL-001`

Created: 2026-07-25

Authority: Bogdan Telegram messages `1476` and `1480`: "Все , теперь вижу,
принято. Коммит" followed by "Первый этап - триаж закончили, идем дальше",
after `P010TR-G1-VIRAL-001` was reviewed with only the selected OK text
candidates.

Exact action:

- Record Bogdan's `p010 triage ok` decision for `P010TR-G1-VIRAL-001`.
- Create `P010TXT-G1-VIRAL-001` as a draft text extraction/review artifact
  from the four accepted text evidence crops only:
  - `P010-B001-TES`
  - `P010-B002-TES`
  - `P010-B005-TES`
  - `P010-B006-TES`
- Preserve logical continuation order separately from file order:
  `P010-B001-TES -> P010-B005-TES -> P010-B002-TES -> P010-B006-TES`.
- Add a fail-closed `crop_order_validation` guard that must pass before any
  semantic map or PCRP movement can consume the draft text.
- Promote the guard through shared validator `scripts/crop_order_validation.py`
  so future pages can reuse the same crop-order contract.
- Record continuation notes for page 009/Peter, Hyeon across B005/B002, and
  Maya continuation to page 011.

Allowed outputs:

- `scripts/build_page_010_text_extraction.py`
- `tests/test_page_010_text_extraction.py`
- `scripts/crop_order_validation.py`
- `tests/test_crop_order_validation.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_text_extraction_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records page 010 draft
  text review only.

Limits:

- Do not create semantic text map.
- Do not create PCRP.
- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process page 011 or pages 011-020.
- Do not run OCR, create OCR output acceptance, rerender the PDF, parse or
  inspect the PDF or PDF text layer, mutate raw artifacts, translate, proofread,
  accept renderer/profile behavior, implement runtime behavior, push, or broaden
  this text extraction without separate bounded authorization.

Output status:

- Package id: `P010TXT-G1-VIRAL-001`
- Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`
- Materialized outputs:
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_text_extraction_G1_VIRAL_001/page_010_text_map.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_text_extraction_G1_VIRAL_001/page_010_text_extraction_packet.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_text_extraction_G1_VIRAL_001/page_010_text_extraction_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_text_extraction_G1_VIRAL_001/page_010_text_extraction_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_text_extraction_G1_VIRAL_001/page_010_text_extraction_manifest.md`
- Hashes:
  - `scripts/build_page_010_text_extraction.py`:
    `DA2D587D07C517DD50D6D0A86A621FABA2848C5C34BE664BCEAC710D5CB5CB87`
  - `tests/test_page_010_text_extraction.py`:
    `A1D28E4D1AC0A0DC1D4F00B5FE2B47672F17B1DDA78816EE8F8FEE70D692F2E8`
  - `scripts/crop_order_validation.py`:
    `708A313EE31A7622346AE7D0F249F877D07B33D52F2F00DB34B61F69E3B9BCAD`
  - `tests/test_crop_order_validation.py`:
    `E69FB90644B13355C58788E4D3F2BECE76C2B9470ED8D9B4829FB251B001F78A`
  - `page_010_text_map.md`:
    `EBF6D19ADA6DE436A19AC74C43CFF567F6C05F6D3A3F59991B12150027769D59`
  - `page_010_text_extraction_packet.json`:
    `AC66E5BE7CEFC0775938B07FDD4C00EAB41426AE616D668B934FBC5906BC50ED`
  - `page_010_text_extraction_report.json`:
    `F579246352F66D1B416119DAEB22C67A09CCA8EE43DC3C1996BA893AA4FE64BC`
  - `page_010_text_extraction_summary.md`:
    `2D2603FA96139CAB57965E0FD37B4EC283BDD7843A23F92C1126A27FB18B04A8`
  - `page_010_text_extraction_manifest.md`:
    `1C9ECCC9C88A467CF72649524956395B4C47CCDA98AC55B73C52FA02D406E12C`
- Result: page 010 draft text is ready for Bogdan review.
- Logical reading order is `B001 -> B005 -> B002 -> B006`.
- Crop order validation passed, confirms the logical order is continuation-aware
  and intentionally not file/asset order, and is required before semantic/PCRP.
- The crop-order validation rule is now shared/reusable, not only P010-specific.
- It creates no OCR/source acceptance, semantic map, PCRP, page-complete
  acceptance, whole Gate 1 acceptance, fixture admission, pages 011-020
  processing, implementation, or push authorization.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, text extraction, semantic map,
  PCRP, translation, proofreading, renderer/profile acceptance, implementation,
  push, OCR, render, PDF parsing, PDF text-layer extraction, and raw mutation
  remain false.

## BA-G1-VIRAL-PAGE-010-SEMANTIC-TEXT-MAP-001

Status: `scope_consumed`; materialized `P010SEM-G1-VIRAL-001`

Created: 2026-07-25

Authority: Bogdan Telegram messages: "Р010 текст ок" followed by message `1561`,
"Ок пошли по плану", after `P010TXT-G1-VIRAL-001` was sent for text review.

Exact action:

- Record Bogdan's `p010 text ok` decision for `P010TXT-G1-VIRAL-001`.
- Create `P010SEM-G1-VIRAL-001` as a semantic text-map review artifact from
  the accepted page 010 draft text only.
- Consume `P010TXT-G1-VIRAL-001` through shared text-extraction consumer and
  crop-order gates.
- Preserve logical order `B001 -> B005 -> B002 -> B006`.
- Split headings, body paragraphs, boxed-section headings, paragraph
  continuations, and crop linkage into semantic units.
- Record Peter continuation from page 009, Hyeon continuation across
  `B005 -> B002`, and Maya continuation to page 011.

Allowed outputs:

- `scripts/build_page_010_semantic_text_map.py`
- `tests/test_page_010_semantic_text_map.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_semantic_text_map_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records page 010 semantic
  text-map review only.

Limits:

- Do not create PCRP.
- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process page 011 or pages 011-020.
- Do not run OCR, create OCR output acceptance, rerender the PDF, parse or
  inspect the PDF or PDF text layer, mutate raw artifacts, translate, proofread,
  accept renderer/profile behavior, implement runtime behavior, push, or broaden
  this semantic map without separate bounded authorization.

Output status:

- Package id: `P010SEM-G1-VIRAL-001`
- Status: `semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance`
- Materialized outputs:
  - `scripts/build_page_010_semantic_text_map.py`
  - `tests/test_page_010_semantic_text_map.py`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_semantic_text_map_G1_VIRAL_001/page_010_semantic_text_map.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_semantic_text_map_G1_VIRAL_001/page_010_semantic_text_map.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_semantic_text_map_G1_VIRAL_001/page_010_semantic_text_map_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_semantic_text_map_G1_VIRAL_001/page_010_semantic_text_map_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_010_semantic_text_map_G1_VIRAL_001/page_010_semantic_text_map_manifest.md`
- Hashes:
  - `scripts/build_page_010_semantic_text_map.py`:
    `6F1A9741D0F9640508236DFB688F260E179042FA651EDD65D57E4BC042D5E843`
  - `tests/test_page_010_semantic_text_map.py`:
    `FB3A95456B346F5DC270CF971694949991FE83142FF66967067B254EAD1388EE`
  - `page_010_semantic_text_map.json`:
    `B9AA02F26FC6EC1E9070EE4448DE72DE20EF0C2C229472BE6450AE73EF2535ED`
  - `page_010_semantic_text_map.md`:
    `005A8A6954CA28CD633BF4A26D1C911DDD385B0ADC64F258D317777057B5B974`
  - `page_010_semantic_text_map_report.json`:
    `6F5B89F71A49911224B36CD761A01BDE2B03BD12A2330E247D4E828B8AAF4272`
  - `page_010_semantic_text_map_summary.md`:
    `1F7865C692CD4B9E94FE099C7C6D40577427A3B0BAF3DE7EAC613CC2D7635F47`
  - `page_010_semantic_text_map_manifest.md`:
    `608FDAE051767C31487DBCC4E7D9B46F2D92A8EF511DAB8548F5471B89652F0A`
- Result: page 010 semantic text map is ready for Bogdan review.
- Unit count: 14.
- Semantic validation, markdown projection, crop linkage, text-extraction
  consumer gate, human review gate, and inventory reconciliation passed.
- It creates no OCR/source acceptance, PCRP, page-complete acceptance, whole
  Gate 1 acceptance, fixture admission, pages 011-020 processing,
  implementation, or push authorization.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P010-001

Status: `scope_consumed`; materialized `PCRP-G1-VIRAL-P010-001`

Created: 2026-07-26

Authority: Bogdan Telegram messages `1574` and `1576`: "Все ок, пошли дальше"
and "проверь" after `P010SEM-G1-VIRAL-001` was sent for semantic-map review.

Allowed actions:

- Record Bogdan's `p010 semantic map ok` decision for `P010SEM-G1-VIRAL-001`.
- Create `PCRP-G1-VIRAL-P010-001` as a page-complete review packet for page
  010 only.
- Consume `P010TR-G1-VIRAL-001`, `P010TXT-G1-VIRAL-001`, and
  `P010SEM-G1-VIRAL-001` as bounded predecessors.
- Package page 010 human context role bindings, physical text-evidence crops,
  predecessor text map, semantic map JSON/Markdown, and page-complete review
  report/summary.
- Preserve logical reading order `B001 -> B005 -> B002 -> B006` for text
  blocks and keep page 011 continuation as metadata only.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`
- Updates to `tests/test_page_complete_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p010_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records page 010
  page-complete review readiness only.

Limits:

- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process page 011 or pages 011-020.
- Do not run OCR, create OCR output acceptance, rerender the PDF, parse or
  inspect the PDF or PDF text layer, mutate raw artifacts, translate, proofread,
  accept renderer/profile behavior, implement runtime behavior, push, or broaden
  this page-complete review packet without separate bounded authorization.

Output status:

- Package id: `PCRP-G1-VIRAL-P010-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Materialized outputs:
  - `scripts/build_page_complete_review.py`
  - `tests/test_page_complete_review.py`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p010_G1_VIRAL_001/page_complete_review_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p010_G1_VIRAL_001/page_complete_review_packet.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p010_G1_VIRAL_001/page_complete_review_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p010_G1_VIRAL_001/page_complete_review_manifest.md`
- Hashes:
  - `scripts/build_page_complete_review.py`:
    `1ABA8A5180960BCFD61061E2ECB3B22BD5B3765AE6C896C256B848928D48E4DE`
  - `tests/test_page_complete_review.py`:
    `C2293947E7867669EE7BAA89B695D551EBA7BFEC42461A945DE146016E3A958E`
  - `page_complete_review_report.json`:
    `C462F5F2A491F8F4427DBCC19F76B58BECFAC5C34900738605D4F806294F5985`
  - `page_complete_review_packet.md`:
    `D55511C990F187E34357B6662F206942C9E599B58DEBC1F8EB23E8A9AC7A8709`
  - `page_complete_review_summary.md`:
    `D4EA7378D6E80C8E1201895E742807113456AF640D798DA54D803728DC24C894`
  - `page_complete_review_manifest.md`:
    `426618C7968094774945AA9A6845B44E37FE1DD25344140CAB2F742467B694F3`
- Result: page 010 is ready for Bogdan's explicit page-complete decision.
- Reviewed blocks: 6/6 ready; blockers: none; open questions: none.
- Semantic validation, markdown projection, and inventory reconciliation passed.
- It creates no page-complete acceptance, whole Gate 1 acceptance, fixture
  admission, source/OCR/render/PDF/raw mutation, pages 011-020 processing,
  implementation, or push authorization.

## BA-G1-VIRAL-REVIEW-ASSET-DEDUPLICATION-001

Status: `scope_consumed`; materialized `sourcefold_review_asset_deduplication.v1`

Created: 2026-07-26

Authority: Bogdan Telegram messages `1600`, `1604`, `1606`, `1610`, and `1620`,
requesting duplicate crop analysis, a durable plan, Sol/Terra implementation
design, and full implementation of the review asset deduplication pipeline
before continuing page 010 acceptance.

Exact action:

- Add shared review asset deduplication contract
  `sourcefold_review_asset_deduplication.v1`.
- Add package-level `package_assets`, `role_bindings`, and `delivery_assets`.
- Integrate the contract into the page-complete review builder.
- Refresh the uncommitted `PCRP-G1-VIRAL-P010-001` in place so duplicate
  human-context/text-evidence crop PNGs become explicit role bindings instead
  of physical duplicate files.
- Keep all crop roles explicit while removing redundant physical package files.

Allowed outputs:

- `scripts/review_asset_deduplication.py`
- `tests/test_review_asset_deduplication.py`
- Updates to `scripts/build_page_complete_review.py`
- Updates to `tests/test_page_complete_review.py`
- Refresh of
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p010_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records review-asset
  deduplication only.

Limits:

- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process page 011 or pages 011-020.
- Do not run OCR, create OCR output acceptance, rerender the PDF, parse or
  inspect the PDF or PDF text layer, mutate raw artifacts, translate, proofread,
  accept renderer/profile behavior, implement runtime behavior, push, or broaden
  this package refresh without separate bounded authorization.

Output status:

- Schema: `sourcefold_review_asset_deduplication.v1`
- P010 PCRP logical attachments: 16.
- P010 PCRP physical package assets: 12.
- P010 PCRP deduplicated role bindings: 4.
- Deduplicated pairs:
  - `P010-001-ATT-HUMAN-UPPER-LEFT` -> `P010-B001-TEXT-EVIDENCE`
  - `P010-001-ATT-HUMAN-UPPER-RIGHT` -> `P010-B002-TEXT-EVIDENCE`
  - `P010-001-ATT-HUMAN-LOWER-LEFT` -> `P010-B005-TEXT-EVIDENCE`
  - `P010-001-ATT-HUMAN-LOWER-RIGHT` -> `P010-B006-TEXT-EVIDENCE`
- Hashes:
  - `scripts/review_asset_deduplication.py`:
    `B335A01C4EE302B637716B0F12EA7DB534C100264B52A823050BCB87B68CB207`
  - `tests/test_review_asset_deduplication.py`:
    `EF15BDF382F702C9689002BDAFFD7E6ABD4E30C1438F2B1B6356878208A1D9DA`
  - `scripts/build_page_complete_review.py`:
    `1ABA8A5180960BCFD61061E2ECB3B22BD5B3765AE6C896C256B848928D48E4DE`
  - `tests/test_page_complete_review.py`:
    `C2293947E7867669EE7BAA89B695D551EBA7BFEC42461A945DE146016E3A958E`
  - `page_complete_review_report.json`:
    `C462F5F2A491F8F4427DBCC19F76B58BECFAC5C34900738605D4F806294F5985`
  - `page_complete_review_packet.md`:
    `D55511C990F187E34357B6662F206942C9E599B58DEBC1F8EB23E8A9AC7A8709`
  - `page_complete_review_summary.md`:
    `D4EA7378D6E80C8E1201895E742807113456AF640D798DA54D803728DC24C894`
  - `page_complete_review_manifest.md`:
    `426618C7968094774945AA9A6845B44E37FE1DD25344140CAB2F742467B694F3`
- Result: page-complete review packages now expose physical package assets,
  role bindings, and delivery assets; duplicate image/crop assets must be
  declared as aliases or blocked.
- It creates no page-complete acceptance, whole Gate 1 acceptance, fixture
  admission, source/OCR/render/PDF/raw mutation, pages 011-020 processing,
  implementation, or push authorization.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P010-001

Status: `scope_consumed`; materialized `P010PCA-G1-VIRAL-001`

Created: 2026-07-26

Authority: Bogdan Telegram message `1632`: "пейдж 010 комплит"

Allowed actions:

- Record Bogdan's explicit page-complete decision for
  `PCRP-G1-VIRAL-P010-001`.
- Consume exact `PCRP-G1-VIRAL-P010-001` page-complete review evidence after
  review asset deduplication.
- Create `P010PCA-G1-VIRAL-001` as a separate page-complete acceptance record
  for page 010 only.
- Update status, roadmap, plan, and context documentation to include page 010
  as page-complete accepted only.

Allowed outputs:

- `scripts/accept_page_010_complete.py`
- `tests/test_page_010_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_manifest.md`

Limits:

- Do not accept whole Gate 1.
- Do not admit or mutate fixtures.
- Do not create or mutate source acceptance.
- Do not run OCR, parse/open PDF or PDF text layer, rerender, mutate raw
  artifacts, translate, proofread, accept renderer/profile behavior, implement,
  push, or process pages 011-020.

Output status:

- Package id: `P010PCA-G1-VIRAL-001`
- Status: `page_010_complete_accepted`
- Accepted page: 010 only
- Consumed package: `PCRP-G1-VIRAL-P010-001`
- Reviewed/ready blocks: 6/6
- Blockers: none
- Open questions: none
- Review asset deduplication: passed
- Created files:
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_record.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p010_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Hashes:
  - `scripts/accept_page_010_complete.py`:
    `6DBC13497037AE254EAF2C699CFFFBC5D30FBD0893E67E6AA81B8FBE829CDCE4`
  - `tests/test_page_010_complete_acceptance.py`:
    `473EFF0ED6917A0715CB9526D2EAF0602E540ED21885983EE2913651B8CBF0F1`
  - `page_complete_acceptance_report.json`:
    `4EA737E0AD3A902479275563F1361BE89DF72E4C8825FC8D617134FB20A1C58E`
  - `page_complete_acceptance_record.md`:
    `F95227CEF837CE884857FFA7C5D0E18FC19DC0697DE5D7187F4393A61F9D68A4`
  - `page_complete_acceptance_summary.md`:
    `4D25186288905128E4D2277B00BF7AFE516579F259A7FAFAF977CC860DAA8337`
  - `page_complete_acceptance_manifest.md`:
    `4C809A3BA0C36D754BBBE7CEA470A48FF6921797514C88A5D7896C3CA8CDB89B`
- It creates no whole Gate 1 acceptance, fixture admission,
  source/OCR/render/PDF/raw mutation, pages 011-020 processing,
  implementation, or push authorization.

## BA-G1-VIRAL-PAGE-REVIEW-PIPELINE-HARDENING-002

Status: `active`; implementation verified, commit pending

Created: 2026-07-24

Authority: Bogdan Telegram message `1128`, requesting the P007 commit-delay
lessons be added to the pipeline and asking whether the paragraph rule was
promoted beyond page 007.

Exact action:

- Promote paragraph-boundary preservation from the P007 review incident into
  the general page-review semantic-unit contract.
- Add a validator/test guard that blocks in-scope `paragraph`/`continuation`
  units carrying embedded visible paragraph breaks unless a separately reviewed
  contract records explicit paragraph-boundary metadata.
- Record clean commit-stage discipline: before saying "ready to commit", the
  work must already have passed tests/reviews plus scoped working-tree
  `git diff --check` over generated files and manifest/hash integrity checks.
- Record that any post-review whitespace, hash, manifest, or provenance issue
  returns the work to build/fix stage; commit stage must only do pathspec
  staging, `git diff --cached --check`, `git diff --cached --name-only`, and
  `git commit`.

Allowed outputs:

- `scripts/page_review_semantic_units.py`
- `tests/test_page_complete_review.py`
- `PROJECT_STATUS.md`
- `docs/plans/20260715-sourcefold-phase-0-release-charter/bounded_trial_authorizations.md`
- `docs/plans/20260715-sourcefold-phase-0-release-charter/context.md`
- `docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md`
- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`
- `docs/roadmap/roadmap.yaml`
- Pending OpenClaw skill proposal for the Sourcefold review-gate workflow.

Limits:

- Do not process page 008.
- Do not create page-complete acceptance, whole Gate 1 acceptance, fixture
  admission, source acceptance mutation, OCR/render/PDF/raw mutation,
  translation, proofreading, renderer/profile acceptance, implementation,
  push, or any candidate-derived artifact rebuild.
- Do not commit or push without separate explicit authorization.

Output status:

- Semantic-unit validator SHA-256:
  `A37F219193AA52DB27C5E1B1E7179D49B9ECD6C89C78229AF0FE455B6F46F11D`
- Page-complete review test SHA-256:
  `E6D29E3C79821365DEA35323B6493876C18DA37E0C558851C604DE25C34E1015`
- Gate 1 Qualification Protocol SHA-256:
  `95A562A783BB85B795E75734202AA807D09112A15AE0CFF2426D4D5CF78BA813`
- Roadmap SHA-256:
  `C8826372B0404F2502FAC9CC945BC39059D32C00641E137D73B50DB9D331AB93`
- Focused semantic/page-complete tests: `75 passed`.
- Roadmap validator: 26 nodes, 25 edges, 121 documentation checkpoints,
  passed.
- Scoped working-tree `git diff --check`: clean.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P008-001

Status: `active`; implementation verified, Bogdan review pending

Created: 2026-07-24

Authority: Bogdan Telegram message `1142`, requesting `full 008` separately
and asking for a backlog/action-log file showing Codex, script, and tool
actions used to build the page packet.

Exact action:

- Prepare a page-complete review packet for page 008 only.
- Use existing rendered page image `page_008.png`; do not reopen or parse the
  PDF and do not rerender.
- Classify visual art/photo/object regions as anchors with deferred extraction
  metadata, not as source text.
- Preserve visible source paragraph boundaries as separate semantic units.
- Include an action backlog markdown file in the packet so Bogdan can inspect
  which steps were Codex orchestration, tools, scripts, and tests.
- Ask only whether a later explicit record may accept page 008 as complete.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p008_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p008_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p008_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p008_G1_VIRAL_001/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p008_G1_VIRAL_001/review_assets/`,
  including the page image, text crops, art-anchor crops, semantic maps, OCR
  text map, and action backlog.
- Status/roadmap/plan/context documentation sync that records the page 008
  review packet.

Limits:

- Do not accept page 008 as complete in this review packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process P007 beyond page-boundary metadata already present in page 008
  review text.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Output status:

- Package id: `PCRP-G1-VIRAL-P008-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `436D8B92E4977AA2339443D9870477E7D6AAE3E00F4E8E5E4AB196C52A747A16`
- Page complete review test SHA-256:
  `04B7ABB8F94BA24BE31CF5ADE0B6952B40DB70B819C2C4C1CB031CBAC0EE9A49`
- Page 008 complete review report SHA-256:
  `B03A397B1C1C6F117DBC79D4525EBE9BDFD2E22C420A84E39B1E62DB80C34B69`
- Page 008 complete review packet SHA-256:
  `97222823611E3F7A0A14D6E2545B8948B1135DA22E4300E5161DB058F551CA1A`
- Page 008 complete review summary SHA-256:
  `FE257745A3E2D8E5BD48B5C4C9D0A96C016507AF908ED84B6501CFE62E037683`
- Page 008 complete review manifest SHA-256:
  `D832FA00C861FDC9432BE7E39CB6AE725FA53BD2476D98FC7A414B09CF0357AD`
- Page 008 OCR/verified text map SHA-256:
  `3CC1E0850A77C7E5A24DC2F4E121C50A26C5D852422AD01C9DCE2D547A1D3981`
- Page 008 semantic map JSON SHA-256:
  `022C9BB66A828CF8BF21ED2D78515A34EA0D62F5B5C51CF06C5D9ABEFF30C296`
- Page 008 semantic map Markdown SHA-256:
  `7BF54F904EF66192F0FE4BF0A50DF34CC34AE8E81B4BA8CF10D8B5EEF0FF3E7D`
- Page 008 action backlog SHA-256:
  `4662D3D632690963DE01C9A13D9AF2474D89088EE71908A13CB267AF80A6AA05`
- Result: page 008 has 7/7 ready blocks, 2 deferred art/photo/object anchors,
  14 paragraph-preserving text semantic units, valid semantic validation, valid
  Markdown projection, valid inventory reconciliation, zero structural
  findings, and no blockers/open questions.
- Page 008 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P008-001

Status: `expired`; scope consumed by `P008PCA-G1-VIRAL-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `1178`: "page 008 complete ok".

Exact action:

- Create a separate page-complete acceptance record for page 008 only.
- Record Bogdan's explicit page 008 complete decision as the human acceptance
  decision for `PCRP-G1-VIRAL-P008-001`.
- Consume the page 008 review packet only if its report, packet, summary, and
  manifest hashes match the current authorized predecessor hashes.

Allowed outputs:

- `scripts/accept_page_008_complete.py`
- `tests/test_page_008_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p008_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records page 008
  acceptance as page-complete only.

Limits:

- Accept page 008 as complete only.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process page 009.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to another
  page without separate bounded authorization.

Output status:

- Package id: `P008PCA-G1-VIRAL-001`
- Status: `page_008_complete_accepted`
- Page 008 complete acceptance script SHA-256:
  `AEBA761297225AC7E287B1D0AB7FC8A750EBF11AE1CC0151B308D96B3E68C693`
- Page 008 complete acceptance test SHA-256:
  `201F0B382C514E7DFF089A03020396BC1BCB4286C3E9A80608239FC437CBA2A8`
- Page 008 complete acceptance report SHA-256:
  `44F126668C6A6F148579787917D93199D0413F51DE0E8C3C6143AAA4047B0F64`
- Page 008 complete acceptance record SHA-256:
  `737DF0A54C9F6FE46BADE0BE7A3ACB5DCA4F2705C4093846593C4AEFD71F6600`
- Page 008 complete acceptance summary SHA-256:
  `24C025D6C7E46251DA72B8B9123D3AE3FE1FDD5026DB73FAECA0578105F15C7A`
- Page 008 complete acceptance manifest SHA-256:
  `85D817E5930A2033507A79B6BCBB1017A04E740B9F2B98CD07AB29EA01855B34`
- Result: page 008 is accepted as complete only.
- Page 008 is the only page authorized for this acceptance.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P001-001

Status: `expired`; scope consumed by `P001PCA-G1-VIRAL-001`

Created: 2026-07-25

Authority: Bogdan Telegram message `1257`: "ok", in response to the
`PCRP-G1-VIRAL-P001-001` page-complete review decision prompt.

Exact action:

- Consume exact `PCRP-G1-VIRAL-P001-001` page-complete review evidence.
- Create `P001PCA-G1-VIRAL-001` as a separate page-complete acceptance record
  for page 001 only.
- Accept page 001 as complete based on the review packet's 3/3 ready
  visual/title anchors, no blockers, no open questions, and Bogdan's explicit
  ok.

Allowed outputs:

- `scripts/accept_page_001_complete.py`
- `tests/test_page_001_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p001_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p001_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p001_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p001_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan/context documentation sync that records the page 001
  acceptance.

Limits:

- Only page 001 may be accepted as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 009+.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to another
  page without separate bounded authorization.

Output status:

- Package id: `P001PCA-G1-VIRAL-001`
- Status: `page_001_complete_accepted`
- Page 001 complete acceptance script SHA-256:
  `6730AF6C38224874F79AB0BB3746BDE38675012598A369D3238FAC63BF921FBF`
- Page 001 complete acceptance test SHA-256:
  `87DAE0CCE17FEC5B28AE10874857B88E265FFD7373D094342FB7F019CDDB4467`
- Page 001 complete acceptance report SHA-256:
  `0ED79F4FE7A9E239E6992CEDA9C9A73CDD3B39E6BD71BBDEC68DBCFDF6C9BF0B`
- Page 001 complete acceptance record SHA-256:
  `EB05AE776834E7826474904C2B62DD0657189A96EA92029F8F402F08212FD1E0`
- Page 001 complete acceptance summary SHA-256:
  `0120B04202F390ECB4345DDD80F25634296BAC04DCABB4A8F102B09EDBAE9641`
- Page 001 complete acceptance manifest SHA-256:
  `DF1B6274DF436AC4933A7152AE11F97C8F2DB892FB154C168D125D46309076EF`
- Result: page 001 is accepted as complete only.
- Page 001 is the only page authorized for this acceptance.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 009+ processing, and raw mutation remain
  false.

## BA-G1-VIRAL-GATE-1-STATUS-REFRESH-003

Status: `expired`; scope consumed by `G1SP-G1-VIRAL-003`

Created: 2026-07-25

Authority: Bogdan Telegram message `1266`: "делай оба шага", explicitly
requesting a short post-P001 Gate 1 status/route refresh and then Page 009
triage/readiness.

Exact action:

- Create `G1SP-G1-VIRAL-003` as a post-P001 Gate 1 status/route packet only.
- Consume `G1SP-G1-VIRAL-002` as the stale predecessor status packet.
- Consume `P001PCA-G1-VIRAL-001` and `P002PCA-G1-VIRAL-001` through
  `P008PCA-G1-VIRAL-001` as page-complete accepted pages only.
- Update the blocker matrix so `page_001_incomplete=false` and
  `pages_009_020_unstarted=true`.
- Preserve OCR benchmark remediation and source-profile/Gate-1 parameter
  parking/acceptance as separate unresolved branches.

Allowed outputs:

- `scripts/build_gate_1_status_refresh_post_p001.py`
- `tests/test_gate_1_status_refresh_post_p001.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_003/*`
- Status/roadmap/plan/context documentation sync that records the post-P001
  status route packet.

Limits:

- Do not accept whole Gate 1.
- Do not authorize the next layer from inside this packet.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not create a new source-reconstruction rollup.
- Do not process page 009 inside this status packet.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this status packet without
  separate bounded authorization.

Output status:

- Status packet id: `G1SP-G1-VIRAL-003`
- Status: `gate_1_status_route_packet_ready_no_acceptance`
- Post-P001 status refresh script SHA-256:
  `EE3C52A729D67000E8CDDCF46B6918BB3440E5ECC2E0CBFE96A5D0F801674B66`
- Post-P001 status refresh test SHA-256:
  `546B54DBC72385BC6F5C9B2F5E189F3505366F72C99109A187B3909364462B8B`
- Gate 1 status packet JSON SHA-256:
  `769A9E7B53FE37876C7B883455FA6BF8C222E2118462923A5ABAF78BE090B1F6`
- Gate 1 status report SHA-256:
  `B75B302944EC2463C3B77BD9BEF459A38B1F83CEE09670840A2511D3E9876147`
- Gate 1 status summary SHA-256:
  `96CE48AEEF8F3950D33E223E7CF435183CA0550C718D706C817A1B95E8999322`
- Gate 1 status manifest SHA-256:
  `36BFAEDEBDA0BF041C746F5003F2B78374DF5A0BF320398E9244890697CCEC4E`
- Result: post-P001 Gate 1 status/route packet is ready for review.
- Page 001 incomplete is now false; pages 009-020 unstarted remains true.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 009 processing authorization, and raw
  mutation remain false.

## BA-G1-VIRAL-PAGE-009-TRIAGE-001

Status: `held`; superseded by `P009TR-G1-VIRAL-002`

Created: 2026-07-25

Authority: Bogdan Telegram message `1266`: "на выходе жду триаж 009 с файлами
для ревью".

Exact action:

- Create `P009TR-G1-VIRAL-001` as a page 009 triage/readiness routing packet
  for Bogdan review only.
- Consume `G1SP-G1-VIRAL-003` as the immediate route predecessor.
- Use the existing rendered page 009 image and existing map/inventory evidence.
- Package page 009 as a two-profile visual/text composition with two
  portrait/image anchors and two text-like profile blocks for review.

Allowed outputs:

- `scripts/build_page_009_triage.py`
- `tests/test_page_009_triage.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_triage_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records page 009
  triage/readiness routing only.

Limits:

- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 010-020.
- Do not run OCR, rerender the PDF, parse or inspect the PDF or PDF text layer,
  mutate raw artifacts, translate, proofread, accept renderer/profile behavior,
  implement runtime behavior, push, or broaden this triage without separate
  bounded authorization.

Output status:

- Package id: `P009TR-G1-VIRAL-001`
- Status: `page_009_triage_ready_for_bogdan_routing_decision`
- Page 009 triage script SHA-256:
  `A4A6D937E5FC44777F0717913FE1CF2924B995FCA1BD138AE092E4C6A9357BDA`
- Page 009 triage test SHA-256:
  `D0CC886B407653830C669560C8AE888C414B8F99AE2DCEE070212D89D7996310`
- Page 009 triage packet SHA-256:
  `6A88391D17BE84F4D3D04098D088BD354CF080CBAC33E8BE63263D816F813816`
- Page 009 triage report SHA-256:
  `907621C2386F6115F2B335CE9B1E2F426065EF1E5B0E35B4F51EF600A4877627`
- Page 009 triage summary SHA-256:
  `E241BEDC808EC96F65E45925D5FAC65FD9F36AFFF76F6A628B55F42B8B113129`
- Page 009 triage manifest SHA-256:
  `25E0DAAC2F1DEEEDEEA09158F06A9FE21CBBE53C0A004CEFDC835C543E6B8438`
- Result: page 009 is routed for Bogdan review as a two-profile visual/text
  composition with two portrait/image anchors and two text-like profile blocks.
- Hold reason: review crops are crooked/tight and one crop clips text; do not
  use this packet for the page 009 route decision.
- Page 009 is not accepted as complete by this packet.
- Pages 010-020 are not processed.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-009-TRIAGE-002

Status: `expired`; scope consumed by `P009TR-G1-VIRAL-002`

Created: 2026-07-25

Authority: Bogdan Telegram message `1284`: "так ну кропы выглядят кривыми, и
будут проблемы, плюс один кроп обрезал текст."

Exact action:

- Create `P009TR-G1-VIRAL-002` as a superseding page 009 triage/readiness
  routing packet for Bogdan review only.
- Mark `P009TR-G1-VIRAL-001` held/superseded for crooked or text-clipping
  review crops.
- Use the same existing rendered page 009 image and existing map/inventory
  evidence.
- Replace tight PRM-box crops with readable padded portrait crops and
  full-column text crops.

Allowed outputs:

- Update `scripts/build_page_009_triage.py`.
- Update `tests/test_page_009_triage.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_triage_G1_VIRAL_002/*`
- Status/roadmap/plan/context documentation sync that records the superseding
  page 009 triage/readiness routing packet.

Limits:

- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 010-020.
- Do not run OCR, rerender the PDF, parse or inspect the PDF or PDF text layer,
  mutate raw artifacts, translate, proofread, accept renderer/profile behavior,
  implement runtime behavior, push, or broaden this triage without separate
  bounded authorization.

Output status:

- Package id: `P009TR-G1-VIRAL-002`
- Status: `page_009_triage_ready_for_bogdan_routing_decision`
- Page 009 triage script SHA-256:
  `84CB1F81ECCD8A40EAF7DC40CD4E85F941B4DA1D222D112D06C84163C3C106E7`
- Page 009 triage test SHA-256:
  `8DE1D514170227BA6090D84833739C49F18DC3C506CCAA51FF5B2BCA7415FA79`
- Page 009 triage packet SHA-256:
  `9560C86398642A466D5559608DACD59753723D88CF898D54091300117413F8DA`
- Page 009 triage report SHA-256:
  `B58E943A8A37B5478E7976C8EF1B1BB20D0BF6F5451C5073497FE1A5CE9EB5D1`
- Page 009 triage summary SHA-256:
  `F435E104044F1E5E4B11E1547CA41ED072E3E2C0DA4323D9F59F97C52B2E6749`
- Page 009 triage manifest SHA-256:
  `D347CB3075D63A6AAC5E515CA078055B6765A97104E729FF0EA6B73944C45C0B`
- Result: page 009 is routed for Bogdan review with readable padded portrait
  crops and readable full-column text crops.
- `P009TR-G1-VIRAL-001` is held/superseded for crooked or text-clipping review
  crops.
- Page 009 is not accepted as complete by this packet.
- Pages 010-020 are not processed.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-009-CROP-CONTRACT-PLAN-001

Status: `plan_recorded`; implementation not authorized by this record

Created: 2026-07-25

Authority: Bogdan Telegram message `1305`: "дам комментарий \"а правый нижний
grey block = полный\" зафиксируй в полном обьеме весь план до работок, сделай
коммит"

Exact planning result:

- `P009TR-G1-VIRAL-002` remains historical/readability-only. It is not OCR
  evidence, not page-map completeness proof, and not sufficient readiness for
  `PCRP-G1-VIRAL-P009-001`.
- Bogdan confirmed the right lower grey block is complete; it is not retained
  as a visual completeness blocker.
- `PCRP-G1-VIRAL-P009-001` is blocked until a superseding
  `P009TR-G1-VIRAL-003` crop-role contract exists.
- `P009TR-G1-VIRAL-003` must record separate crop roles:
  `source_region_box_px` for immutable PRM/page-map lineage,
  `human_review_crop_box_px` for broad human context,
  `ocr_candidate_crop_box_px` for clean OCR candidate input, and
  `text_evidence_crop_box_px` for OCR/verification evidence.
- OCR/text evidence crops must be text-only, complete, not clipped, and not
  polluted by portrait/art/frame content.
- Crop QA must include edge/gutter checks for OCR/text evidence crops, a blocker
  for text ink near crop boundaries, a blocker for visual-only/art content
  inside OCR evidence crops, page-map reconciliation for every represented
  text-like region, semantic/text-map unit linkage to `text_evidence_crop_id`,
  and regression coverage for two-column pages with 0, 1, 2, and 3+ art regions
  in variable positions.

Allowed outputs:

- Documentation/status/roadmap/authorization sync that records this plan.
- Commit of the already prepared current bounded scope:
  `G1SP-G1-VIRAL-003`, held `P009TR-G1-VIRAL-001`, current
  `P009TR-G1-VIRAL-002`, scripts, tests, fixtures, and this plan.

Limits:

- Do not create `P009TR-G1-VIRAL-003` under this record.
- Do not create `PCRP-G1-VIRAL-P009-001`.
- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 010-020.
- Do not run OCR, rerender the PDF, parse or inspect the PDF or PDF text layer,
  mutate raw artifacts, translate, proofread, accept renderer/profile behavior,
  implement runtime behavior, push, or broaden this planning record without
  separate bounded authorization.

## BA-G1-VIRAL-PAGE-009-CROP-CONTRACT-CORRECTION-PLAN-001

Status: `plan_recorded`; implementation not authorized by this record

Created: 2026-07-25

Authority: Bogdan Telegram message `1311`: "зафиксируй план и сделай коммит"

Review basis:

- Sol/Terra re-read project goals, page 009 triage goals, and the roadmap after
  commit `a98d6111`.
- Both reviewers found `PCRP-G1-VIRAL-P009-001` still blocked.
- The project boundary remains Phase 0 / Gate 1 governance; no implementation,
  OCR execution, source acceptance, or whole-Gate acceptance is unlocked.

Exact planning corrections:

- Current cursor changes from `page_009_triage_ready_for_bogdan_routing_decision`
  to `page_009_crop_contract_missing_pcrp_blocked`.
- `P009TR-G1-VIRAL-002` is historical/readability-only and stale for PCRP
  routing. Its earlier route recommendation is superseded for PCRP purposes.
- `P009TR-G1-VIRAL-002` is not OCR evidence, not an OCR crop contract, not
  page-map completeness proof, and not a valid predecessor for
  `PCRP-G1-VIRAL-P009-001`.
- The next required implementation layer is a separately authorized
  `P009TR-G1-VIRAL-003` crop-role/OCR-safe contract.
- `P009TR-G1-VIRAL-003` must make OCR-safe crops geometry/input-candidate
  evidence only. It must not run OCR, create OCR output, accept transcripts,
  mutate source acceptance, or create page-complete acceptance.
- Future `P009TR-G1-VIRAL-003` capability fields should avoid ambiguous
  `blocked_capabilities=false` phrasing and instead use a positive created-state
  matrix such as `capabilities_created`, including explicit false values for
  OCR execution, OCR evidence, page-map completeness proof, PCRP readiness,
  page acceptance, whole-Gate acceptance, fixture admission, and source
  acceptance mutation.
- Future tests must prove `PCRP-G1-VIRAL-P009-001` fails closed on
  `P009TR-G1-VIRAL-002`, `P009TR-G1-VIRAL-003` contains all required crop roles,
  human-review crops cannot satisfy OCR/text evidence requirements, OCR/text
  evidence crops reject portrait/art/frame pollution and text-near-boundary
  failures, the right lower grey block is complete/non-blocking, and no OCR run,
  OCR output, source acceptance, page-complete acceptance, or pages 010-020
  processing is created.

Eight-step correction/implementation plan:

1. Correct the current status cursor from `page_009_triage_ready` to
   `page_009_crop_contract_missing_pcrp_blocked`.
2. Mark `P009TR-G1-VIRAL-002` stale for PCRP routing while preserving it as
   historical/readability-only evidence.
3. Record `P009TR-G1-VIRAL-002`'s old route recommendation as superseded for
   PCRP purposes.
4. Create a new bounded authorization for `P009TR-G1-VIRAL-003` only.
5. Implement `P009TR-G1-VIRAL-003` as the crop-role/OCR-safe contract with
   separate source-region, human-review, OCR-candidate, and text-evidence crop
   boxes.
6. Add OCR/text crop QA: edge/gutter, text-near-boundary, visual-pollution,
   page-map reconciliation, and semantic/text-map linkage checks.
7. Add PCRP fail-closed guards/tests so page 009 PCRP rejects `P009TR-G1-VIRAL-002`
   and requires current `P009TR-G1-VIRAL-003`.
8. Run Sol/Terra review and Bogdan review on `P009TR-G1-VIRAL-003`; only then
   create a separate bounded authorization for `PCRP-G1-VIRAL-P009-001`.

Allowed outputs:

- Documentation/status/roadmap/authorization sync that records these
  corrections.
- Commit of this plan correction only.

Limits:

- Do not create `P009TR-G1-VIRAL-003` under this record.
- Do not create `PCRP-G1-VIRAL-P009-001`.
- Do not mutate historical `P009TR-G1-VIRAL-002` artifacts.
- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 010-020.
- Do not run OCR, create OCR evidence/output, rerender the PDF, parse or inspect
  the PDF or PDF text layer, mutate raw artifacts, translate, proofread, accept
  renderer/profile behavior, implement runtime behavior, push, or broaden this
  planning record without separate bounded authorization.

## BA-G1-VIRAL-PAGE-009-CROP-CONTRACT-003

Status: `scope_consumed`; materialized `P009TR-G1-VIRAL-003`

Created: 2026-07-25

Authority: Bogdan Telegram message `1320`: "на каждый шаг бери сол и терру, для проработки делай ввесь план, остановка по готовности 1-8"

Allowed actions:

- Execute the eight-step correction/implementation plan recorded in
  `BA-G1-VIRAL-PAGE-009-CROP-CONTRACT-CORRECTION-PLAN-001`.
- Create `P009TR-G1-VIRAL-003` as the superseding page 009 crop-role contract
  for later PCRP consideration.
- Preserve `P009TR-G1-VIRAL-002` as historical/readability-only and mark its
  old route recommendation superseded for PCRP purposes in the new contract.
- Materialize role-separated crops for page 009:
  - `source_region_box_px` as immutable PRM/page-map lineage;
  - `human_review_crop_box_px` as human context only;
  - `ocr_candidate_crop_box_px` as text-only OCR candidate geometry;
  - `text_evidence_crop_box_px` as text-only verification geometry.
- Add QA guards for OCR/text crops: edge/gutter, text-near-boundary,
  portrait/art/frame pollution, page-map reconciliation, semantic/text-map
  linkage, right lower grey block complete/non-blocker, and no OCR/PCRP/source
  acceptance capability creation.
- Add page 009 PCRP fail-closed guard/test coverage so `_002` cannot satisfy
  PCRP preconditions and `_003` is the required current crop contract.
- Run and record Sol/Terra review for each step 1-8 before stopping for
  Bogdan's crop-contract review.

Limits:

- Do not create `PCRP-G1-VIRAL-P009-001`.
- Do not create OCR execution, OCR output, OCR transcript acceptance, source
  acceptance mutation, page-complete acceptance, whole Gate 1 acceptance,
  fixture admission, renderer/profile acceptance, implementation, push, or
  pages 010-020 processing.
- Do not mutate historical `P009TR-G1-VIRAL-002` artifacts.
- Stop after `P009TR-G1-VIRAL-003` is ready for Bogdan review.

Implementation result:

- Package id: `P009TR-G1-VIRAL-003`
- Status: `page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked`
- Current continuation:
  `page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked`
- Crop QA: `passed`
- Sol/Terra: recorded as OK for steps 1-8 in the packet.
- PCRP guard: page 009 PCRP remains fail-closed; `_002` is stale for PCRP and
  `_003` still requires Bogdan review plus a separate PCRP authorization/profile.
- Outputs:
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_triage_G1_VIRAL_003/page_009_triage_packet.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_triage_G1_VIRAL_003/page_009_triage_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_triage_G1_VIRAL_003/page_009_triage_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_triage_G1_VIRAL_003/page_009_triage_manifest.md`
- Reproducibility hashes:
  - `scripts/build_page_009_triage.py`:
    `434FD788C0C27BBA45035C017E18DFD764BF49F5AE1156DAF71A4ECBD8AA0702`
  - `tests/test_page_009_triage.py`:
    `061C4288EEACA633793EFD9C1E036B176EFBB27393402675EAB608389A847ED1`
  - `page_009_triage_packet.json`:
    `7FC48ED869676E62F43CFCAAB9A1D08D91F6E48C6304AF65A8D14A6237C8E215`
  - `page_009_triage_report.json`:
    `DC58315C51FA904DF1E0DDB3076E75F63CAA17313C251B55300284A1A08E6BEB`
  - `page_009_triage_summary.md`:
    `B04C0D560FA4B82AC4219B2733E9E27B4D6D7A347E8B7DB5B1036E0A2A08EC27`
  - `page_009_triage_manifest.md`:
    `654A1438942C3FFBDF6A1EC01E50483A5A78FEE54E38EB4CD00B7628A98801AB`

## BA-G1-VIRAL-PAGE-009-TEXT-EXTRACTION-001

Status: `scope_consumed`; materialized `P009TXT-G1-VIRAL-001`

Created: 2026-07-25

Authority:

- Bogdan Telegram message `1351`: "Ок, тогда шаг ок."
- Bogdan Telegram message `1353`: "Ок двигайся"

Allowed actions:

- Record Bogdan's `p009 crop contract ok` decision for
  `P009TR-G1-VIRAL-003`.
- Create `P009TXT-G1-VIRAL-001` as a draft text extraction/review artifact
  from the two page 009 `text_evidence` crops.
- Create a human-readable text map Markdown file and packet/report/summary/
  manifest files for Bogdan review.
- Run Sol/Terra review for this bounded text-output layer.

Limits:

- Do not create `PCRP-G1-VIRAL-P009-001`.
- Do not mark the text as accepted OCR output or accepted source text.
- Do not create page-complete acceptance, whole Gate 1 acceptance, fixture
  admission, source acceptance mutation, renderer/profile acceptance,
  implementation, push, OCR benchmark remediation, or pages 010-020 processing.

Implementation result:

- Package id: `P009TXT-G1-VIRAL-001`
- Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`
- Text map: `page_009_text_map.md`
- Text units: 7
- Sol/Terra: OK for bounded draft text output; no PCRP/source/page acceptance
  capability created.
- Outputs:
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_text_extraction_G1_VIRAL_001/page_009_text_map.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_text_extraction_G1_VIRAL_001/page_009_text_extraction_packet.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_text_extraction_G1_VIRAL_001/page_009_text_extraction_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_text_extraction_G1_VIRAL_001/page_009_text_extraction_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_text_extraction_G1_VIRAL_001/page_009_text_extraction_manifest.md`
- Reproducibility hashes:
  - `scripts/build_page_009_text_extraction.py`:
    `2E6F66C0385075DFB7B5FC04B79C1BB87E3DEF4BD6CF002875371B6B10A716F4`
  - `tests/test_page_009_text_extraction.py`:
    `1EFAC4EEE7EB60B25C9DD714AAB978984A5DA0BDFFDAF9FA93C24735CF21C736`
  - `page_009_text_map.md`:
    `0F5DB5291A8F5DAE70F3EAF4757AFF0F164DB6D1D89745134A7440994841B968`
  - `page_009_text_extraction_packet.json`:
    `8980F0BD978A8B6F8D74F8F297A702B51BC040321BEE5E819EC5F40277F5402B`
  - `page_009_text_extraction_report.json`:
    `E33F042A6CCF50A3F25B5A8F13051021A64084B827F557667D8086DC034251A1`
  - `page_009_text_extraction_summary.md`:
    `5C3B1A264555FA246FDFC68F4C8B1C1365EBE471EB22C02815538ECF7C724B97`
  - `page_009_text_extraction_manifest.md`:
    `FFD29FAFCF61AA5D17ED8F865F5DB4D2E351DE9B7D6BC090F2EFC2DBA2AF96A5`

## BA-G1-VIRAL-PAGE-009-SEMANTIC-TEXT-MAP-001

Status: `scope_consumed`; materialized `P009SEM-G1-VIRAL-001`

Created: 2026-07-25

Authority: Bogdan Telegram message `1367`: "Ок, принимаю. Поехали дальше"

Allowed actions:

- Record Bogdan's `p009 text ok` decision for `P009TXT-G1-VIRAL-001`.
- Create `P009SEM-G1-VIRAL-001` as a semantic text-map review artifact from
  `P009TXT-G1-VIRAL-001`.
- Split page 009 text into heading/body/boxed-section semantic units with
  heading levels, display style, block role, reading order, paragraph-boundary
  preservation, inventory reconciliation, and text-evidence crop linkage.
- Run Sol/Terra review for this bounded semantic-map layer.

Limits:

- Do not create `PCRP-G1-VIRAL-P009-001`.
- Do not create page-complete acceptance, whole Gate 1 acceptance, fixture
  admission, source acceptance mutation, OCR/source acceptance, renderer/profile
  acceptance, implementation, push, OCR benchmark remediation, or pages 010-020
  processing.

Output status:

- Package id: `P009SEM-G1-VIRAL-001`
- Status: `semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance`
- Semantic units: 14
- Semantic validation: valid
- Markdown projection validation: valid
- Crop linkage validation: valid
- Inventory reconciliation: valid
- Created files:
  - `scripts/build_page_009_semantic_text_map.py`
  - `tests/test_page_009_semantic_text_map.py`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_semantic_text_map_G1_VIRAL_001/page_009_semantic_text_map.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_semantic_text_map_G1_VIRAL_001/page_009_semantic_text_map.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_semantic_text_map_G1_VIRAL_001/page_009_semantic_text_map_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_semantic_text_map_G1_VIRAL_001/page_009_semantic_text_map_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_009_semantic_text_map_G1_VIRAL_001/page_009_semantic_text_map_manifest.md`
- Hashes:
  - `scripts/build_page_009_semantic_text_map.py`:
    `76B7A3C5389AE8F97A8D962FC71DD5A08C8E8430E5E3441440E18AE85EBD7EB1`
  - `tests/test_page_009_semantic_text_map.py`:
    `54C931F563B9E5A9FD2E0E40B42152745F355C6A3F0130E15675F7F2124828B8`
  - `page_009_semantic_text_map.json`:
    `5E2C2EDF3A1C2A102D547681D7029F5AFAD76C99F1C3E75D23079A346E9156A5`
  - `page_009_semantic_text_map.md`:
    `AE6D9F8C38E716583FD2D3B14026CEE562B2EE64F00BA263362CC84009746313`
  - `page_009_semantic_text_map_report.json`:
    `063FA7B08222CA138406B11C63A3AB999481FC28EE881B2EAAD6064907B8D3E3`
  - `page_009_semantic_text_map_summary.md`:
    `CCAAB1E94CE6E2B47D3F14276B1B1C61E63D3C1FDC8F51B4457A7E07EC7996B8`
  - `page_009_semantic_text_map_manifest.md`:
    `7777AE51C458FEA0A351F2CF92E453329AAAB4EC0DD342258AEBF726649987AD`

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P009-001

Status: `scope_consumed`; materialized `PCRP-G1-VIRAL-P009-001`

Created: 2026-07-25

Authority: Bogdan Telegram message `1380`: "Коммит и дальше двигайся"

Allowed actions:

- Record Bogdan's `p009 semantic map ok` decision for
  `P009SEM-G1-VIRAL-001`.
- Create `PCRP-G1-VIRAL-P009-001` as a page-complete review packet only.
- Consume `P009TR-G1-VIRAL-003`, `P009TXT-G1-VIRAL-001`, and
  `P009SEM-G1-VIRAL-001` as bounded predecessors.
- Materialize page 009 review assets, OCR/text evidence crops, review text map,
  semantic map JSON/Markdown, packet, report, summary, and manifest.
- Run Sol/Terra review for this bounded PCRP layer.

Limits:

- Do not create page-complete acceptance, whole Gate 1 acceptance, fixture
  admission, source acceptance mutation, OCR/source acceptance, renderer/profile
  acceptance, implementation, push, OCR benchmark remediation, or pages 010-020
  processing.

Output status:

- Package id: `PCRP-G1-VIRAL-P009-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Consumed packages:
  - `P009TR-G1-VIRAL-003`
  - `P009TXT-G1-VIRAL-001`
  - `P009SEM-G1-VIRAL-001`
- Expected/reviewed/ready blocks: 4/4/4
- Semantic validation: valid
- Markdown projection validation: valid
- Inventory reconciliation: valid
- Structural findings: 0
- Blockers: none
- Created files:
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p009_G1_VIRAL_001/page_complete_review_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p009_G1_VIRAL_001/page_complete_review_packet.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p009_G1_VIRAL_001/page_complete_review_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p009_G1_VIRAL_001/page_complete_review_manifest.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p009_G1_VIRAL_001/review_assets/`
- Hashes:
  - `scripts/build_page_complete_review.py`:
    `7A3F1FABEAE8F263F7B084D6E2BD5C66A28723C1F1DF1A1E646873A94F042D91`
  - `tests/test_page_complete_review.py`:
    `DD55BCBC4D90EF3CEFAD4950A6523571B66D9B9F206BF77FB7CC36EB353BF19E`
  - `page_complete_review_report.json`:
    `41A60F33815FF492E666946DF6BECC5D37450B2B9D49DB3077B6CBBD6DB40CCB`
  - `page_complete_review_packet.md`:
    `1F853A7EE60FEBD3A526A8FF96341B6B3CB45D0D27DBCD78F089504B9AFA0B3D`
  - `page_complete_review_summary.md`:
    `177336712A3A13F4B2A0E306DC78D47E51A4C17BB175A4DE79B85FED33E2BDC1`
  - `page_complete_review_manifest.md`:
    `CA5F746A59DFDED91969F075B903BB2A3A1B75222862D34D3D2A9DE18400DB8E`

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P009-001

Status: `scope_consumed`; materialized `P009PCA-G1-VIRAL-001`

Created: 2026-07-25

Authority: Bogdan Telegram message `1396`: "Педж 009 комплит"

Allowed actions:

- Record Bogdan's explicit page-complete decision for
  `PCRP-G1-VIRAL-P009-001`.
- Consume exact `PCRP-G1-VIRAL-P009-001` page-complete review evidence.
- Create `P009PCA-G1-VIRAL-001` as a separate page-complete acceptance record
  for page 009 only.
- Update status, roadmap, plan, and context documentation to include page 009
  as page-complete accepted only.

Allowed outputs:

- `scripts/accept_page_009_complete.py`
- `tests/test_page_009_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_manifest.md`

Limits:

- Do not accept whole Gate 1.
- Do not admit or mutate fixtures.
- Do not create or mutate source acceptance.
- Do not run OCR, parse/open PDF or PDF text layer, rerender, mutate raw
  artifacts, translate, proofread, accept renderer/profile behavior, implement,
  push, or process pages 010-020.

Output status:

- Package id: `P009PCA-G1-VIRAL-001`
- Status: `page_009_complete_accepted`
- Accepted page: 009 only
- Consumed package: `PCRP-G1-VIRAL-P009-001`
- Reviewed/ready blocks: 4/4
- Blockers: none
- Open questions: none
- Created files:
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_report.json`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_record.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_summary.md`
  - `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p009_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Hashes:
  - `scripts/accept_page_009_complete.py`:
    `ED498CF4A6DC8EE510BE0B7BACB7029C9571DF3DD748A11DC9DC363B196F5D8E`
  - `tests/test_page_009_complete_acceptance.py`:
    `C33BCE37840686AE2F7B7639570991A76240A4E53D60C87DC48E5008C914D8E3`
  - `page_complete_acceptance_report.json`:
    `87F11A29136C46E4ED20E70054F8B3ADF2C1AE869458F8A37A82D9A593DF8051`
  - `page_complete_acceptance_record.md`:
    `05354AFA7A17B15B69AF1711FF4C2E0662B952BB4D692E01A513DEA49FCA7DB1`
  - `page_complete_acceptance_summary.md`:
    `DEB397E2448D273E58D11759D948A0F6A44BAD34A06573FEEB2887213D0F10E9`
  - `page_complete_acceptance_manifest.md`:
    `ABC7109DD2B91057A1EC951AD6AE761164F76600F422A4AC7FE7E07B01538917`

## BA-G1-VIRAL-GATE-1-STATUS-REFRESH-002

Status: `expired`; scope consumed by `G1SP-G1-VIRAL-002`

Created: 2026-07-25

Authority: Bogdan Telegram message `1212`: "делай. ко мне приходи как всегда
после \"ок от сол и терры\"."

Exact action:

- Create a post-P008 Gate 1 status/route packet only.
- Record pages 002-008 as page-complete accepted only.
- Record `G1SP-G1-VIRAL-001` as historical/narrow/stale for current
  page-complete status, not as current full status authority.
- Record the current canonical narrow source-reconstruction state as 13
  accepted records without creating a new source-acceptance rollup.
- Record first-class blockers, a negative capability matrix, state taxonomy,
  predecessor binding, and non-authorizing routing options.

Allowed outputs:

- `scripts/build_gate_1_status_refresh.py`
- `tests/test_gate_1_status_packet.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_002/gate_1_status_packet.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_002/gate_1_status_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_002/gate_1_status_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_002/gate_1_status_manifest.md`
- Status/roadmap/plan/context documentation sync that records status routing
  only.

Limits:

- Do not accept whole Gate 1.
- Do not authorize the next layer from inside this packet.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not create a new source-reconstruction rollup.
- Do not process page 001 or page 009+.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this status packet without
  separate bounded authorization.

Output status:

- Status packet id: `G1SP-G1-VIRAL-002`
- Status: `gate_1_status_route_packet_ready_no_acceptance`
- Gate 1 status refresh script SHA-256:
  `3F141F755D7899F882560F51A36F9337C197FCD40BB2811E61B7D31D97D6E22C`
- Gate 1 status packet test SHA-256:
  `0105C8B166A13F60248133595871495912CE007EE288C823790273C197072741`
- Gate 1 status packet JSON SHA-256:
  `9EC5331E2E67CA2F8103559B5D0EDBC51E86C80E5F36A075863861889AA8AAD3`
- Gate 1 status report SHA-256:
  `226E57ED1C9288897054FD546BD79D646284A887922E3287383844F4B96FC076`
- Gate 1 status summary SHA-256:
  `7E88BBBCACEC9E61DA9DF52714D7263D8607D428685CDC883217375EBCAC8604`
- Gate 1 status manifest SHA-256:
  `54438C5751BE8D7876E21E2E118EEC338E591BF6A5878F4A9B461E82D102D06B`
- Result: post-P008 Gate 1 status/route packet is ready for review.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 001 processing, page 009+ processing, and raw
  mutation remain false.

## BA-G1-VIRAL-PAGE-001-TRIAGE-001

Status: `expired`; scope consumed by `P001TR-G1-VIRAL-001`

Created: 2026-07-25

Authority: Bogdan Telegram message `1226`: "зафиксируй план. и делай 1.
Page 001 triage/review".

Exact action:

- Create a page 001 triage/readiness routing packet only.
- Use existing rendered page 001 image and existing map/triage/status evidence.
- Decide whether page 001 can proceed to a visual/title page-complete review
  without OCR benchmark remediation.
- Record OCR benchmark remediation as a separate legal branch, not the first
  selected next step.

Allowed outputs:

- `scripts/build_page_001_triage.py`
- `tests/test_page_001_triage.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_001_triage_G1_VIRAL_001/*`
- Status/roadmap/plan/context documentation sync that records page 001
  triage/readiness routing only.

Limits:

- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 009-020.
- Do not run OCR, rerender the PDF, parse or inspect the PDF or PDF text layer,
  mutate raw artifacts, translate, proofread, accept renderer/profile behavior,
  implement runtime behavior, push, or broaden this triage without separate
  bounded authorization.

Output status:

- Package id: `P001TR-G1-VIRAL-001`
- Status: `page_001_triage_ready_for_bogdan_routing_decision`
- Page 001 triage script SHA-256:
  `D78436640CE8D61EE36207700A80B7EA6DEBF33257D2381012509A18F7B2F191`
- Page 001 triage test SHA-256:
  `A665E69B83F43AEEB9CEC694191C3A897E382062C11AB9D2390534B35144F73E`
- Page 001 triage packet SHA-256:
  `5D428155CD967AC427BAB090EF90140891F07F1FF985F1333157F98932016411`
- Page 001 triage report SHA-256:
  `EDBB68B385CAC4EF6ED7D61298C8B69CFB944E566A6B53B9EEDBC5F1DB1A6A57`
- Page 001 triage summary SHA-256:
  `134B845ED919079C560668580374D4B734088408E08E32FAA12E99099D89E327`
- Page 001 triage manifest SHA-256:
  `3DAE5B7D2076A8B1B48AB8CAD833A2BB9F8A288702B0381BE6C881F30D4C53C7`
- Result: page 001 is routed for human decision as a visual/title
  page-complete review candidate without OCR/remediation.
- OCR benchmark remediation remains a separate later branch.
- Page 001 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 009+ processing, and raw mutation remain
  false.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P001-001

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P001-001`

Created: 2026-07-25

Authority: Bogdan Telegram message `1244`: "ок делай" after the proposed
sequence to push `P001TR-G1-VIRAL-001` and build a page 001 page-complete
review packet.

Exact action:

- Create `PCRP-G1-VIRAL-P001-001` as a page-complete review packet only.
- Consume `P001TR-G1-VIRAL-001` as the routing/readiness predecessor.
- Use existing rendered page 001 image and existing page 001 triage crops.
- Package page 001 as a visual/title cover page with full-page, title/logo,
  and footer/rating/tagline/logo anchors.
- Keep OCR benchmark remediation as a separate later branch.

Allowed outputs:

- Update `scripts/build_page_complete_review.py` with the page 001 review
  profile.
- Update `tests/test_page_complete_review.py` for the page 001 review contract.
- Create `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p001_G1_VIRAL_001/*`.
- Status/roadmap/plan/context documentation sync that records page 001
  page-complete review packet only.

Limits:

- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not process pages 009-020.
- Do not run OCR, rerender the PDF, parse or inspect the PDF or PDF text layer,
  mutate raw artifacts, translate, proofread, accept renderer/profile behavior,
  implement runtime behavior, push, or broaden this review without separate
  bounded authorization.

Output status:

- Package id: `PCRP-G1-VIRAL-P001-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Page-complete review script SHA-256:
  `141E2D7A41C063C4B9AE447CBE22F0869BCC5575A5783E1D174145DDC5753C2A`
- Page-complete review test SHA-256:
  `F36AE79D72DA7A21893655EF2A7D7079E57507C71A7CC58162EF1E64FD1B679C`
- Page 001 review report SHA-256:
  `7ECD5487CA3CA8F5931C70C536BD7BCB774163A970930226A71453DB35F763FE`
- Page 001 review packet SHA-256:
  `D430A2A3DF4A7600991974D7A46A948411576E7E4532784B894E27800E3F2D81`
- Page 001 review summary SHA-256:
  `34BDABDAB67C6BC8FC3A9D2E7CEA7C4C6591B58433B6D10C8555E850187E9DC6`
- Page 001 review manifest SHA-256:
  `517E18CED782C0B1C71E14C872E5A5EF6F202407D6C10932120EB34907224831`
- Result: page 001 is packaged for Bogdan's explicit page-complete decision as
  a visual/title cover page with full-page, title/logo, and footer/rating/
  tagline/logo deferred visual anchors.
- Page 001 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 009+ processing, and raw mutation remain
  false.

## BA-G1-VIRAL-SPM-001

Status: `expired`; scope consumed by `SPM-G1-VIRAL-001`

Created: 2026-07-17

Authority: user request from Bogdan: "Ок, делай протокол и баундед триал. Как
обычно привлекай сол и Терру."

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.

Exact action:

- Create one selected-page manifest for the `Вирал` candidate.

Admitted inputs:

- Candidate identity already recorded in
  `fixtures/candidate_inputs/viral/README.md`.
- Local candidate copy path:
  `fixtures/candidate_inputs/viral/Call_of_Cthulhu_Viral.pdf`.
- Recorded SHA-256:
  `0A80B6F389821B87553D26746D2BE171B4482BA9BBC6E3EB3FEC26274EDBED05`.
- Selection policy: ordinal pages 1-20 only, matching the recorded first pilot
  direction.

Allowed outputs:

- One `selected_page_manifest` record naming the candidate identity, the
  selected ordinal page range 1-20, this authorization ID, the accepted
  protocol revision/blob, actor, timestamp, and invalidation rules.

Produced output:

- `fixtures/candidate_inputs/viral/selected_page_manifest_pages_1_20.md`
- Manifest id: `SPM-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- The manifest may not include page images, OCR output, PDF text-layer content,
  extracted text, layout maps, screenshots, benchmark results, QA findings,
  fixtures, Accepted Source Text, translation output, or proofreading output.
- Do not render, OCR, map, translate, proofread, benchmark, run QA, or implement
  modules under this authorization.
- Do not accept the `Вирал` candidate as fixture, source evidence, or source
  profile evidence under this authorization.
- Do not refresh, recount, rehash, parse, inspect, or derive additional PDF
  metadata unless a later distinct bounded authorization names that exact
  action.
- This authorization does not unlock render authorization; rendering remains a
  separate blocked action after the manifest exists.

Expiry:

- Expires after the first selected-page manifest revision is created, or at
  2026-07-18T20:30:00+03:00, whichever comes first.

Invalidation behavior:

- Any change to source path, recorded source hash, selection policy, manifest
  schema, accepted protocol revision/blob, this authorization record, or user
  authority stales the produced manifest.
- If invalidated, the manifest cannot be used by render, map, OCR, benchmark,
  QA, fixture, source-profile, or implementation work until a fresh bounded
  authorization produces a current replacement.

Not authorized:

- Rendering pages.
- Creating page images.
- Creating or freezing render candidate manifests.
- Creating `doc_map`, `content_map`, `art_map`, or `pre_ocr_map_bundle`.
- OCR or PDF text-layer extraction/comparison.
- Gold-sample creation.
- Benchmark execution.
- QA execution or finding ledger creation.
- Fixture creation or execution.
- Source profile acceptance.
- Core module implementation.

## BA-G1-VIRAL-RENDER-001

Status: `expired`; scope consumed by `RT-G1-VIRAL-RENDER-001`

Created: 2026-07-17

Authority: user request from Bogdan: "Ок, двигайся дальше."

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.

Exact action:

- Render only `SPM-G1-VIRAL-001` ordinal pages 1-20 into page-image trial
  evidence using the pinned render candidate below.

Admitted inputs:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Selected-page manifest path:
  `fixtures/candidate_inputs/viral/selected_page_manifest_pages_1_20.md`
- Candidate identity already recorded in
  `fixtures/candidate_inputs/viral/README.md`.
- Local candidate copy path:
  `fixtures/candidate_inputs/viral/Call_of_Cthulhu_Viral.pdf`.
- Recorded SHA-256:
  `0A80B6F389821B87553D26746D2BE171B4482BA9BBC6E3EB3FEC26274EDBED05`.
- Frozen render candidate manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/render_candidate_manifest.md`
- Frozen render candidate manifest SHA-256:
  `0C14E716846D4753DDDF01FAEB1BF3DC13ADB8071CB05E9A263A186B8888E7F0`
- Frozen comparison plan:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/comparison_plan.md`
- Frozen comparison plan SHA-256:
  `CEAD5EE07EEA2119E1C75B7E7961E5B66593947DDA5A69A12FFB8C7FFCBB8495`

Renderer/config:

- Renderer: PyMuPDF / `fitz`
- Renderer version: `1.27.2.3`
- Python executable: `D:\NRI\.tools\python-3.13.14\python.exe`
- Render candidate id: `RC-G1-VIRAL-PYMUPDF-300DPI-RGB-PNG-001`
- DPI: 300
- Color: RGB
- Container: PNG
- Alpha: disabled
- Preprocessing: none

Allowed outputs:

- One PNG page image per ordinal page 1-20.
- One render output manifest for `RT-G1-VIRAL-RENDER-001` with page ordinal,
  `SPM-G1-VIRAL-001`, render candidate id, comparison plan id, output path,
  output SHA-256, renderer/config predecessor, and invalidation status.

Produced output:

- Render trial id: `RT-G1-VIRAL-RENDER-001`
- Output manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/render_output_manifest.md`
- Output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Page images: 20 PNG files under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/`
- Output status: `valid_for_review`

Limits:

- Do not render any page outside ordinal pages 1-20.
- Do not OCR, extract PDF text-layer content, map, annotate, benchmark, compare
  quality, run QA, create fixtures, accept source evidence, translate,
  proofread, implement modules, or accept renderer/profile parameters.
- Do not use successful render output as evidence that OCR, map, QA,
  source-profile, fixture, or implementation gates are ready.
- Stop if `SPM-G1-VIRAL-001`, accepted protocol revision/blob, source
  path/hash, renderer version/config, frozen render candidate manifest,
  frozen comparison plan, output format, or user authority differs from this
  authorization.

Expiry:

- Expires after the first render output manifest for `RT-G1-VIRAL-RENDER-001`
  is created, or at 2026-07-18T20:45:00+03:00, whichever comes first.

Invalidation behavior:

- Render evidence stales on source path/hash change, `SPM-G1-VIRAL-001`
  change, accepted protocol revision/blob change, authorization change,
  PyMuPDF/library/build/config change, DPI/color/container/preprocessing
  change, render candidate manifest change, comparison plan change, output
  schema change, or any downstream use beyond this render-only scope.

## BA-G1-VIRAL-VISUAL-001

Status: `expired`; scope consumed by `VSR-G1-VIRAL-001`

Created: 2026-07-17

Authority: user request from Bogdan: "Ок, согласен."

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.

Exact action:

- Perform a bounded visual sanity and page inventory review of
  `RT-G1-VIRAL-RENDER-001` PNG outputs only.

Admitted inputs:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/render_output_manifest.md`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Page images: `page_001.png` through `page_020.png` under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/`

Allowed outputs:

- One contact sheet derived from the 20 rendered PNGs for bounded visual review.
- One visual sanity report recording page ordinal, gross image availability,
  orientation, broad page kind, and obvious gross render defects if visible.

Produced output:

- Contact sheet:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/visual_sanity_contact_sheet.png`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`
- Visual sanity report:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/visual_sanity_report.md`
- Report id: `VSR-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not OCR or transcribe text.
- Do not extract or inspect PDF text-layer content.
- Do not create maps, regions, anchors, QA findings, benchmark scores, source
  acceptance, fixtures, translation, proofreading, or implementation work.
- Do not accept renderer, DPI, color, image container, page layout, OCR
  readiness, or source-profile parameters.
- Do not treat a visually readable page as proof of OCR quality or source
  acceptance.

Expiry:

- Expires after the first visual sanity report for `RT-G1-VIRAL-RENDER-001` is
  created, or at 2026-07-18T21:00:00+03:00, whichever comes first.

Invalidation behavior:

- Visual sanity evidence stales on source path/hash change,
  `SPM-G1-VIRAL-001` change, `RT-G1-VIRAL-RENDER-001` output change, accepted
  protocol revision/blob change, authorization change, render config change,
  visual report schema change, or user authority change.

## BA-G1-VIRAL-PAGEINV-001

Status: `expired`; scope consumed by `PIR-G1-VIRAL-001`

Created: 2026-07-17

Authority: user request from Bogdan: "Давай делать page inventory authorization."

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.

Exact action:

- Create one page-level inventory report for ordinal pages 1-20 using already
  rendered PNG outputs and contact sheet from `RT-G1-VIRAL-RENDER-001` only.

Admitted inputs:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/render_output_manifest.md`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Rendered page images: `page_001.png` through `page_020.png` with identities,
  paths, and hashes recorded in the render output manifest.
- Visual sanity report: `VSR-G1-VIRAL-001`
- Visual sanity report SHA-256:
  `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Contact sheet:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/visual_sanity_contact_sheet.png`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`

Allowed outputs:

- One non-accepting page inventory report with one row per ordinal page.
- Allowed per-page fields: page ordinal, image id, image path, image SHA-256,
  presence state, gross visual state, broad page kind, coarse layout hint,
  `future_map_needed`, and coarse reason/uncertainty.

Produced output:

- Page inventory report:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_inventory_report.md`
- Report id: `PIR-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not OCR, transcribe, extract PDF text-layer content, copy exact text,
  assert reading order, create regions, coordinates, anchors, stable region
  IDs, maps, map seeds, OCR routing, benchmark scores, QA findings, fixture
  manifests, source evidence, source-profile acceptance, translation,
  proofreading, or implementation work.
- Do not create `doc_map`, `content_map`, `art_map`, or
  `pre_ocr_map_bundle`.
- Treat all page-kind and layout labels as non-authoritative visual hints only.

Expiry:

- Expires after the first page inventory report for `RT-G1-VIRAL-RENDER-001`
  is created, or at 2026-07-18T21:15:00+03:00, whichever comes first.

Invalidation behavior:

- Page inventory evidence stales on source path/hash change,
  `SPM-G1-VIRAL-001` change, `RT-G1-VIRAL-RENDER-001` output change, render
  output manifest/hash change, page PNG file change, contact sheet/hash change,
  `VSR-G1-VIRAL-001` change, accepted protocol revision/blob change,
  authorization change, render config change, inventory schema/taxonomy change,
  or user authority change.

## BA-G1-VIRAL-PAGEMAP-001

Status: `expired`; scope consumed by `PMR-G1-VIRAL-001`

Created: 2026-07-17

Authority: user request from Bogdan: "Ок" after the proposed next step to
commit `PIR-G1-VIRAL-001`, call Sol/Terra, and create a bounded page
map/model authorization.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.

Exact action:

- Create one non-accepting page-level map/model report for Viral ordinal pages
  1-20 from existing PNG/PIR evidence only.

Admitted inputs:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Page PNGs `page_001.png` through `page_020.png` as identified in the render
  output manifest.
- Visual sanity report: `VSR-G1-VIRAL-001`
- Visual sanity report SHA-256:
  `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`
- Page inventory report: `PIR-G1-VIRAL-001`
- Page inventory report SHA-256:
  `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA`

Allowed outputs:

- One non-accepting page-level map/model report.
- Allowed per-page fields: page ordinal, image id/path/SHA-256, predecessor
  IDs/hashes, broad page role, coarse visual/layout class, candidate layer
  focus, map complexity flag, later region-mapping-needed flag, review state,
  uncertainty, exclusion/unknown notes, and invalidation rules.

Produced output:

- Page map/model report:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_model_report.md`
- Report id: `PMR-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not OCR, transcribe, copy exact text, inspect or extract PDF text-layer
  content, assert reading order, create stable region IDs, anchors,
  coordinates, bounding boxes, accepted region registry, OCR routing,
  benchmark scores, QA findings, fixture records, source evidence,
  source-profile acceptance, translation, proofreading, or implementation.
- Do not create or freeze `pre_ocr_map_bundle`.
- Do not mark `doc_map`, `content_map`, or `art_map` as accepted, current,
  canonical, or source truth.
- Treat page-map labels as provisional planning hints only.

Expiry:

- Expires after the first page map/model report for
  `RT-G1-VIRAL-RENDER-001` is created, or at 2026-07-18T23:50:00+03:00,
  whichever comes first.

Invalidation behavior:

- Page map/model evidence stales on source path/hash change, accepted protocol
  revision/blob change, authorization change, `SPM-G1-VIRAL-001` change,
  `RT-G1-VIRAL-RENDER-001` output change, render output manifest/hash change,
  page PNG file/hash change, `VSR-G1-VIRAL-001` change, contact sheet/hash
  change, `PIR-G1-VIRAL-001` change, render config change,
  schema/taxonomy/observation-rules change, tooling/reviewer identity change,
  or authority model change.

## BA-G1-VIRAL-REGIONMAP-001

Status: `expired`; scope consumed by `PRM-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Коммит и потом делать настоящий."

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.

Exact action:

- Create one provisional region annotation artifact/report for Viral ordinal
  pages 1-20 from already-rendered PNG evidence only.

Admitted inputs:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Page PNGs `page_001.png` through `page_020.png` as identified in the render
  output manifest.
- Visual sanity report: `VSR-G1-VIRAL-001`
- Visual sanity report SHA-256:
  `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`
- Page inventory report: `PIR-G1-VIRAL-001`
- Page inventory report SHA-256:
  `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA`
- Page map/model report: `PMR-G1-VIRAL-001`
- Page map/model report SHA-256:
  `72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F`

Allowed outputs:

- One provisional region annotation artifact/report with status
  `valid_for_review`.
- Allowed fields: page ordinal, image id/path/SHA-256, provisional region id,
  approximate box with coordinate space, coarse class, observation state,
  uncertainty/unknown/mixed flags, predecessor IDs/hashes, tool/reviewer
  identity, timestamp, and invalidation rules.

Produced output:

- Provisional region map report:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/provisional_region_map_report.md`
- Report id: `PRM-G1-VIRAL-001`
- Report SHA-256:
  `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C`
- Region records: 62 provisional visual annotations across ordinal pages 1-20.
- Output status: `valid_for_review`

Observation rules:

- Region IDs are explicitly provisional trial IDs, not stable/canonical IDs.
- Boxes are approximate visual annotations in the rendered PNG coordinate
  space (`2550x3300`) plus normalized coordinates.
- Classes must stay coarse: `text_like`, `art_image`, `mixed`,
  `table_list_like`, `title_heading_like`, `margin_page_number_like`,
  `unknown_unsupported`.
- `doc_map`, `content_map`, and `art_map` projections may be named only as
  candidate layer projections, not accepted/current/canonical map records.

Limits:

- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not OCR, transcribe, copy exact text, inspect or extract PDF text-layer
  content, translate, proofread, benchmark, run QA, create fixtures, accept
  source evidence, accept source-profile parameters, or implement code.
- Do not assert accepted reading order, OCR routing, anchors, stable region
  registry, accepted coordinates, or source truth.
- Do not create `doc_map`, `content_map`, `art_map`, or
  `pre_ocr_map_bundle`; bundle freezing requires a separate bounded
  authorization.
- Do not store coordinate or region payloads in roadmap YAML or status rollups.

Expiry:

- Expires after the first provisional region annotation artifact/report for
  `RT-G1-VIRAL-RENDER-001` is created, or at 2026-07-19T00:30:00+03:00,
  whichever comes first.

Invalidation behavior:

- Provisional region annotation evidence stales on source path/hash change,
  protocol revision/blob change, authorization change, `SPM-G1-VIRAL-001`
  change, `RT-G1-VIRAL-RENDER-001` output change, render output manifest/hash
  change, page PNG file/hash change, `VSR-G1-VIRAL-001` change, contact
  sheet/hash change, `PIR-G1-VIRAL-001` change, `PMR-G1-VIRAL-001` change,
  render config change, schema/taxonomy/coordinate model change,
  tool/reviewer identity change, observation-rules change, or authority model
  change.

## BA-G1-VIRAL-MAPBUNDLE-PREQ-001

Status: `expired`; scope consumed by `MBR-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Вперед" after the proposed next step to
review `PRM-G1-VIRAL-001`, call Sol/Terra, and attempt bounded map-bundle
freezing.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.

Exact action:

- Create one non-accepting map-bundle prerequisite and lineage review record
  for the existing Viral SPM/RT/VSR/PIR/PMR/PRM predecessor chain.

Admitted inputs:

- Selected-page manifest: `SPM-G1-VIRAL-001`
- Selected-page manifest SHA-256:
  `73D6C817E54DDEFB89BA7109440E87F36B447F74C19044D154A0674AD41E3936`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Visual sanity report: `VSR-G1-VIRAL-001`
- Visual sanity report SHA-256:
  `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Contact sheet SHA-256:
  `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`
- Page inventory report: `PIR-G1-VIRAL-001`
- Page inventory report SHA-256:
  `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA`
- Page map/model report: `PMR-G1-VIRAL-001`
- Page map/model report SHA-256:
  `72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F`
- Provisional region map report: `PRM-G1-VIRAL-001`
- Provisional region map report SHA-256:
  `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C`
- Sol/Terra read-only boundary reviews for the attempted map-bundle step.

Allowed outputs:

- One non-accepting prerequisite/lineage review record with status
  `blocked_for_bundle_freeze`.
- Allowed fields: predecessor IDs, paths, hashes, review conclusions,
  missing prerequisites, allowed next bounded action, limits, and invalidation
  rules.

Produced output:

- Map-bundle prerequisite review:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/map_bundle_prerequisite_review.md`
- Review id: `MBR-G1-VIRAL-001`
- Output status: `blocked_for_bundle_freeze`

Limits:

- Do not create, update, or freeze `pre_ocr_map_bundle`.
- Do not create or accept `doc_map`, `content_map`, or `art_map`.
- Do not promote PMR/PRM planning labels, provisional region IDs, provisional
  boxes, or candidate layer projections into accepted map layers, stable
  region IDs, accepted coordinates, anchors, reading order, or OCR routing.
- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not OCR, transcribe, copy exact text, inspect or extract PDF text-layer
  content, benchmark, run QA, create fixtures, accept source evidence, accept
  source-profile parameters, translate, proofread, or implement code.
- Do not store region coordinates, region rows, map payloads, or copied text in
  roadmap YAML or status rollups.

Expiry:

- Expires after the first map-bundle prerequisite review for
  `RT-G1-VIRAL-RENDER-001` is created, or at 2026-07-19T08:00:00+03:00,
  whichever comes first.

Invalidation behavior:

- The prerequisite review stales on source path/hash change, protocol
  revision/blob change, authorization change, `SPM-G1-VIRAL-001` change,
  `RT-G1-VIRAL-RENDER-001` output change, render output manifest/hash change,
  page PNG file/hash change, `VSR-G1-VIRAL-001` change, contact sheet/hash
  change, `PIR-G1-VIRAL-001` change, `PMR-G1-VIRAL-001` change,
  `PRM-G1-VIRAL-001` change, map schema/taxonomy/coordinate model change,
  shared identity model change, tool/reviewer identity change, Sol/Terra
  boundary-review change, or authority model change.

## BA-G1-VIRAL-MAPSCHEMA-001

Status: `expired`; scope consumed by `MSID-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" after Sol/Terra-reviewed ten-step forward plan.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.
- Baseline commit:
  `c3bda8a8b32a87f92f23e434b9ffd5999637bedf`

Exact action:

- Create one version-bound provisional map schema and shared identity packet
  for future Viral trial `doc_map`, `content_map`, `art_map`, and
  `pre_ocr_map_bundle` artifacts.

Admitted inputs:

- Sol/Terra-reviewed forward plan:
  `docs/plans/20260715-sourcefold-phase-0-release-charter/viral_forward_10_step_plan.md`
- Map-bundle prerequisite review: `MBR-G1-VIRAL-001`
- Map-bundle prerequisite review SHA-256:
  `630B42491016B1013FB853A64A7ACBA03B1A15D5787C07655C9AD8F2F8BADD8E`
- Existing predecessor IDs and hashes recorded in `MBR-G1-VIRAL-001`.

Allowed outputs:

- One non-accepting `MSID-G1-VIRAL-001` packet with version-bound provisional
  schemas, identity namespaces, canonical serialization/hashing rules,
  coordinate basis, baseline lineage, leakage prohibitions, and invalidation
  rules.

Produced output:

- Map schema/identity packet:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/map_schema_identity_packet.md`
- Packet id: `MSID-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not create, update, or freeze `pre_ocr_map_bundle`.
- Do not create `doc_map`, `content_map`, or `art_map` payloads.
- Do not promote PMR/PRM planning labels, provisional region IDs, provisional
  boxes, or candidate layer projections into accepted map layers, stable
  region IDs, accepted coordinates, anchors, accepted reading order, source
  truth, or OCR routing.
- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not OCR, transcribe, copy exact text, inspect or extract PDF text-layer
  content, benchmark, run QA, create fixtures, accept source evidence, accept
  source-profile parameters, translate, proofread, or implement code.
- Do not store region coordinates, region rows, map payloads, or copied text in
  roadmap YAML or status rollups.

Expiry:

- Expires after the first `MSID-G1-VIRAL-001` packet is created, or at
  2026-07-19T10:00:00+03:00, whichever comes first.

Invalidation behavior:

- `MSID-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, `MBR-G1-VIRAL-001` change, predecessor
  identity/hash change, schema/identity rule change, canonical serialization
  rule change, coordinate basis change, Sol/Terra review change, or authority
  model change.

## BA-G1-VIRAL-DOCMAP-001

Status: `expired`; scope consumed by `DM-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" under the Sol/Terra-reviewed forward plan, after `MSID-G1-VIRAL-001`
review returned Sol OK and Terra conditional OK for limited use.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Accepted status: `accepted_protocol` for methodology only.
- Baseline commit:
  `8fff7fc5bd7e384374835bf9af6195aa91f6991a`

Exact action:

- Create one non-accepting trial `doc_map` artifact for Viral ordinal pages
  1-20 from current SPM/RT/VSR/PIR/PMR/PRM/MSID predecessors.

Admitted inputs:

- Map schema/identity packet: `MSID-G1-VIRAL-001`
- MSID SHA-256:
  `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024`
- Forward plan SHA-256:
  `4DD8BB5C7778BF660A2FECC6EE32AD6CD6CD0E5978BF512A2655ECB3B41DD64A`
- Selected-page manifest: `SPM-G1-VIRAL-001`
- Selected-page manifest SHA-256:
  `73D6C817E54DDEFB89BA7109440E87F36B447F74C19044D154A0674AD41E3936`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Visual sanity report SHA-256:
  `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Page inventory report SHA-256:
  `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA`
- Page map/model report SHA-256:
  `72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F`
- Provisional region map report SHA-256:
  `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C`

Allowed outputs:

- One non-accepting trial `doc_map` report with page registry, MSID trial
  page IDs, deterministic MSID trial region ID ranges, PRM provenance links,
  predecessor hashes, review status, payload-leakage check, and invalidation
  rules.

Produced output:

- Trial doc map:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/doc_map_trial_report.md`
- Map id: `DM-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not create `content_map`, `art_map`, or `pre_ocr_map_bundle`.
- Do not freeze any bundle or assert bundle readiness.
- Do not promote PRM provisional IDs/boxes into canonical identity; they may
  be referenced only as provenance.
- Do not accept page roles, region IDs, coordinates, anchors, reading order,
  OCR routing, source truth, source evidence, or source-profile parameters.
- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not OCR, transcribe, copy exact text, inspect or extract PDF text-layer
  content, benchmark, run QA, create fixtures, translate, proofread, or
  implement code.

Expiry:

- Expires after the first `DM-G1-VIRAL-001` trial report is created, or at
  2026-07-19T11:00:00+03:00, whichever comes first.

Invalidation behavior:

- `DM-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, MSID change, any admitted predecessor
  identity/hash change, region ID namespace change, coordinate basis change,
  payload-leakage rule change, observation rule change, reviewer/authority
  change, or later doc-map remediation/supersession.

## BA-G1-VIRAL-CONTENTMAP-001

Status: `expired`; scope consumed by `CM-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" under the Sol/Terra-reviewed forward plan, after `DM-G1-VIRAL-001`
was created as non-accepting trial doc-map registry evidence.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `1108e106fff2a21b65e2fcf199503910fc008bac`

Exact action:

- Create one non-accepting trial `content_map` artifact referencing
  `DM-G1-VIRAL-001` and `MSID-G1-VIRAL-001` trial IDs.

Admitted inputs:

- Map schema/identity packet: `MSID-G1-VIRAL-001`
- MSID SHA-256:
  `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024`
- Trial doc map: `DM-G1-VIRAL-001`
- Trial doc map SHA-256:
  `F10FFDF22393A467668396DB2C7861331B5E5BD11586DCF72B46FE95140717E6`
- Provisional region map report SHA-256:
  `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C`

Allowed outputs:

- One non-accepting trial `content_map` report with structural candidate
  groups referencing `DM-G1-VIRAL-001`/MSID trial region IDs, review status,
  payload-leakage check, and invalidation rules.

Produced output:

- Trial content map:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/content_map_trial_report.md`
- Map id: `CM-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not create `art_map` or `pre_ocr_map_bundle`.
- Do not freeze any bundle or assert bundle readiness.
- Do not copy source text, OCR output, PDF text-layer content, gold sample
  text, translation, or proofreading payloads.
- Do not accept OCR routing, reading order, semantic RPG roles, source truth,
  QA, benchmark results, fixtures, source evidence, or source-profile
  parameters.
- Do not open, parse, rehash, recount, or inspect the PDF.

Expiry:

- Expires after the first `CM-G1-VIRAL-001` trial report is created, or at
  2026-07-19T12:00:00+03:00, whichever comes first.

Invalidation behavior:

- `CM-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, MSID change, `DM-G1-VIRAL-001` change,
  PRM change, region ID namespace change, structural taxonomy change,
  payload-leakage rule change, reviewer/authority change, or later content-map
  remediation/supersession.

## BA-G1-VIRAL-ARTMAP-001

Status: `expired`; scope consumed by `AM-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" under the Sol/Terra-reviewed forward plan, after `CM-G1-VIRAL-001`
was created as non-accepting trial content-map evidence.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `2b1cb68317f5f72973a81e2bd8b53401b90f2db0`

Exact action:

- Create one non-accepting trial `art_map` artifact referencing
  `DM-G1-VIRAL-001` and `MSID-G1-VIRAL-001` trial IDs.

Admitted inputs:

- Map schema/identity packet: `MSID-G1-VIRAL-001`
- MSID SHA-256:
  `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024`
- Trial doc map: `DM-G1-VIRAL-001`
- Trial doc map SHA-256:
  `F10FFDF22393A467668396DB2C7861331B5E5BD11586DCF72B46FE95140717E6`
- Trial content map: `CM-G1-VIRAL-001`
- Trial content map SHA-256:
  `335699DB7AE60E87390D88D7A26AA22BA297F50F90B7868F7ED869C2F5AABE79`
- Provisional region map report SHA-256:
  `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C`

Allowed outputs:

- One non-accepting trial `art_map` report with visual/mixed candidate groups
  referencing `DM-G1-VIRAL-001`/MSID trial region IDs, text-in-art flags only,
  review status, payload-leakage check, and invalidation rules.

Produced output:

- Trial art map:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/art_map_trial_report.md`
- Map id: `AM-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not create or freeze `pre_ocr_map_bundle`.
- Do not transcribe text-in-art, copy source text, use OCR output, use PDF
  text-layer content, create gold sample text, translate, or proofread.
- Do not accept OCR routing, reading order, semantic art interpretation,
  source truth, QA, benchmark results, fixtures, source evidence, or
  source-profile parameters.
- Do not open, parse, rehash, recount, or inspect the PDF.

Expiry:

- Expires after the first `AM-G1-VIRAL-001` trial report is created, or at
  2026-07-19T13:00:00+03:00, whichever comes first.

Invalidation behavior:

- `AM-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, MSID change, `DM-G1-VIRAL-001` change,
  `CM-G1-VIRAL-001` change, PRM change, region ID namespace change, visual
  taxonomy change, text-in-art flag rule change, payload-leakage rule change,
  reviewer/authority change, or later art-map remediation/supersession.

## BA-G1-VIRAL-MAPCONSISTENCY-001

Status: `expired`; scope consumed by `MCV-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" under the Sol/Terra-reviewed forward plan, after `DM-G1-VIRAL-001`,
`CM-G1-VIRAL-001`, and `AM-G1-VIRAL-001` were created.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `5db5b26ec76f62e459e7d947d36a99dea86f1354`

Exact action:

- Validate cross-map references, stale predecessor hashes, region coverage,
  overlap policy, schema linkage, and payload leakage for the current
  non-accepting trial map set.

Admitted inputs:

- Map schema/identity packet SHA-256:
  `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024`
- Trial doc map SHA-256:
  `F10FFDF22393A467668396DB2C7861331B5E5BD11586DCF72B46FE95140717E6`
- Trial content map SHA-256:
  `335699DB7AE60E87390D88D7A26AA22BA297F50F90B7868F7ED869C2F5AABE79`
- Trial art map SHA-256:
  `77BD88C0522E17DF98603364677BC248450EC3E57996389881629E581197C544`

Allowed outputs:

- One non-accepting map consistency validation report with pass/fail results,
  exact input hashes, blocker list, and invalidation rules.

Produced output:

- Map consistency validation:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/map_consistency_validation_report.md`
- Validation id: `MCV-G1-VIRAL-001`
- Output status: `passed_for_bundle_freeze_review`

Limits:

- Do not modify map-layer artifacts under this authorization.
- Do not create or freeze `pre_ocr_map_bundle`.
- Do not OCR, transcribe, copy text, inspect PDF text-layer content, benchmark,
  run QA, create fixtures, accept source evidence, translate, proofread, or
  implement code.
- Do not treat a passing validation as Gate 1 acceptance, OCR readiness, or
  bundle freeze.

Expiry:

- Expires after the first `MCV-G1-VIRAL-001` report is created, or at
  2026-07-19T14:00:00+03:00, whichever comes first.

Invalidation behavior:

- `MCV-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, MSID change, any map-layer hash change,
  validation rule change, overlap policy change, payload-leakage rule change,
  reviewer/authority change, or any remediation/supersession of the validated
  maps.

## BA-G1-VIRAL-MAPBUNDLE-001

Status: `expired`; scope consumed by `POMB-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" under the Sol/Terra-reviewed forward plan, after
`MCV-G1-VIRAL-001` passed for bundle-freeze review.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `bb2b996d448df523e656386bc9a0f8f69dc96ab5`

Exact action:

- Freeze one non-accepting `pre_ocr_map_bundle` index from exact current
  MSID/DM/CM/AM/MCV hashes.

Admitted inputs:

- Map schema/identity packet SHA-256:
  `468C05B3CA808F787ECB297E467EC7BB77BA6B608D836004BD0CFDECA4D32024`
- Trial doc map SHA-256:
  `F10FFDF22393A467668396DB2C7861331B5E5BD11586DCF72B46FE95140717E6`
- Trial content map SHA-256:
  `335699DB7AE60E87390D88D7A26AA22BA297F50F90B7868F7ED869C2F5AABE79`
- Trial art map SHA-256:
  `77BD88C0522E17DF98603364677BC248450EC3E57996389881629E581197C544`
- Map consistency validation SHA-256:
  `B939CEB12187C47FCBE3FFB72032D50E2B13AD22261637D6652204F61144BCE3`

Allowed outputs:

- One non-accepting `pre_ocr_map_bundle` freeze/index report binding exact
  map-layer and validation hashes, status, scope, downstream limitations, and
  invalidation rules.

Produced output:

- Pre-OCR map bundle:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/pre_ocr_map_bundle_report.md`
- Bundle id: `POMB-G1-VIRAL-001`
- Output status: `frozen_for_review`

Limits:

- Do not OCR, benchmark, run QA, create fixtures, accept source evidence,
  translate, proofread, accept renderer/profile parameters, or implement code.
- Do not treat bundle freeze as Gate 1 acceptance, source-profile acceptance,
  OCR readiness, or permission for downstream consumption.
- Do not modify the frozen map-layer inputs under this authorization.
- Do not add region rows, coordinates, copied text, OCR text, or PDF text-layer
  content to roadmap YAML or status rollups.

Expiry:

- Expires after the first `POMB-G1-VIRAL-001` bundle report is created, or at
  2026-07-19T15:00:00+03:00, whichever comes first.

Invalidation behavior:

- `POMB-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, MSID change, any map-layer hash change,
  MCV change, canonicalization/hash rule change, downstream admission rule
  change, reviewer/authority change, or any remediation/supersession of a
  predecessor artifact.

## BA-G1-VIRAL-OCRPREP-001

Status: `expired`; scope consumed by `OPR-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" under the Sol/Terra-reviewed forward plan, after `POMB-G1-VIRAL-001`
was frozen for review.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `6769c619b53cadd13f9e338024c045fb9750451b`

Exact action:

- Prepare one OCR benchmark preparation package with OCR candidate manifest
  stub, scoring plan, gold-sample creation plan, and map-consumption admission
  record for planning only.

Admitted inputs:

- Pre-OCR map bundle: `POMB-G1-VIRAL-001`
- Pre-OCR map bundle SHA-256:
  `B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F`
- Render output manifest SHA-256:
  `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`

Allowed outputs:

- One OCR preparation package with candidate manifest stub, scoring plan,
  gold-sample creation plan, map-consumption admission state, limits, blockers,
  and invalidation rules.

Produced output:

- OCR preparation package:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_prep_package_report.md`
- Prep id: `OPR-G1-VIRAL-001`
- Output status: `ready_for_gold_and_ocr_authorization`

Limits:

- Do not run OCR.
- Do not create OCR output.
- Do not create gold text or sample answers.
- Do not copy source text, inspect PDF text-layer content, translate,
  proofread, benchmark, run QA, create fixtures, accept source evidence, accept
  source-profile parameters, or implement code.
- Do not treat this prep package as OCR benchmark execution or Gate 1
  acceptance.

Expiry:

- Expires after the first `OPR-G1-VIRAL-001` report is created, or at
  2026-07-19T16:00:00+03:00, whichever comes first.

Invalidation behavior:

- `OPR-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, POMB change, render manifest change, OCR
  candidate identity/config change, scoring plan change, gold-sample policy
  change, map-consumption admission rule change, reviewer/authority change, or
  any predecessor remediation/supersession.

## BA-G1-VIRAL-OCRBENCH-PREQ-001

Status: `expired`; scope consumed by `OBR-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "План зафиксируй, и иди по нему до
конца" under the Sol/Terra-reviewed forward plan, after `OPR-G1-VIRAL-001`
prepared OCR benchmark planning artifacts without OCR execution.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `e9ba54dc7aa10ae409192c70883c6ecae307c79f`

Exact action:

- Review whether bounded OCR benchmark execution can start from
  `OPR-G1-VIRAL-001`, and record missing prerequisites/blockers.

Admitted inputs:

- OCR preparation package: `OPR-G1-VIRAL-001`
- OCR preparation package SHA-256:
  `8920E42A10EBBF64557A3C971F73D783FB9F00A86D90777F22BEA7941F38C62F`

Allowed outputs:

- One OCR benchmark prerequisite review with verdict, missing prerequisites,
  allowed next actions, limits, and invalidation rules.

Produced output:

- OCR benchmark prerequisite review:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_benchmark_prerequisite_review.md`
- Review id: `OBR-G1-VIRAL-001`
- Output status: `blocked_waiting_gold_and_ocr_candidate`

Limits:

- Do not run OCR.
- Do not create OCR output.
- Do not create gold text or sample answers.
- Do not benchmark, score, run QA, create fixtures, accept source evidence,
  translate, proofread, accept renderer/profile parameters, or implement code.
- Do not self-advance Gate 1.

Expiry:

- Expires after the first `OBR-G1-VIRAL-001` report is created, or at
  2026-07-19T17:00:00+03:00, whichever comes first.

Invalidation behavior:

- `OBR-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, OPR change, POMB change, OCR candidate
  identity/config change, gold-sample policy/manifest change, scoring plan
  change, reviewer/authority change, or any predecessor remediation or
  supersession.

## BA-G1-VIRAL-GOLDSAMPLE-001

Status: `expired`; scope consumed by `GSM-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Ок иди делай оба" after `OBR-G1-VIRAL-001`
identified missing gold samples and OCR candidate manifest/config.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `40dc8ba8aafd6a3d70ddedfc3f6d6bae8b28aad5`

Exact action:

- Create a small controlled gold-sample manifest from already rendered PNG
  pages and map-bundle lineage only, without OCR or PDF text-layer use.

Allowed outputs:

- One gold-sample manifest with a small number of manually read sample strings,
  page/region references, provenance, reviewer notes, payload limits, and
  invalidation rules.

Produced output:

- Gold sample manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gold_sample_manifest.md`
- Manifest id: `GSM-G1-VIRAL-001`
- Output status: `valid_for_review`

Limits:

- Do not run OCR.
- Do not inspect PDF text-layer content.
- Do not create accepted source text or source-profile acceptance.
- Do not benchmark, score, run QA, create fixtures, translate, proofread, or
  implement code.
- Gold snippets are benchmark references only and cannot be promoted to
  accepted source evidence by this authorization.

Expiry:

- Expires after the first `GSM-G1-VIRAL-001` manifest is created, or at
  2026-07-19T18:00:00+03:00, whichever comes first.

Invalidation behavior:

- `GSM-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, POMB change, render image/hash change,
  selected sample list change, gold text correction, reviewer/authority change,
  or predecessor remediation/supersession.

## BA-G1-VIRAL-OCRCANDIDATE-001

Status: `expired`; scope consumed by `OCM-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Ок иди делай оба" after `OBR-G1-VIRAL-001`
identified missing gold samples and OCR candidate manifest/config.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `40dc8ba8aafd6a3d70ddedfc3f6d6bae8b28aad5`

Exact action:

- Create one OCR candidate manifest/config record without installing software
  and without running OCR.

Allowed outputs:

- One OCR candidate manifest with engine/config identity, environment check,
  execution status, blockers, and invalidation rules.

Produced output:

- OCR candidate manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_candidate_manifest.md`
- Manifest id: `OCM-G1-VIRAL-001`
- Output status: `blocked_missing_executable`

Limits:

- Do not install OCR tools.
- Do not run OCR.
- Do not create OCR output, benchmark results, QA findings, fixtures, source
  acceptance, translation, proofreading, or implementation.

Expiry:

- Expires after the first `OCM-G1-VIRAL-001` manifest is created, or at
  2026-07-19T18:30:00+03:00, whichever comes first.

Invalidation behavior:

- `OCM-G1-VIRAL-001` stales on protocol revision/blob change, baseline commit
  supersession, authorization change, OCR engine availability/version/config
  change, output format change, preprocessing policy change, reviewer/authority
  change, or predecessor remediation/supersession.

## BA-G1-VIRAL-OCRCANDIDATE-002

Status: `expired`; scope consumed by `OCM-G1-VIRAL-001` refresh

Created: 2026-07-18

Authority: user request from Bogdan: "Обновляй и снимай блокер" after local
Tesseract was found under `D:\NRI\.tools\tesseract\`.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `a35c9702c04b33705a24d7c6c5ca536d0d60c8ea`

Exact action:

- Refresh `OCM-G1-VIRAL-001` by binding the discovered local Tesseract
  executable, version, language data, and candidate config without running OCR.

Admitted inputs:

- Prior OCR candidate manifest: `OCM-G1-VIRAL-001`
- Prior OCR candidate manifest SHA-256:
  `4E8BDB8E20966888FD96968C16C0DC77D34616378896042D9D72F3BD8E8A8225`
- Tesseract executable:
  `D:\NRI\.tools\tesseract\tesseract.exe`
- Tesseract executable SHA-256:
  `BABB405F4366B480D02CD8FF2BAC8D497170F6C1711CE6F3D5D8BF0FB7FA6ED9`
- English language data:
  `D:\NRI\.tools\tesseract\tessdata\eng.traineddata`
- English language data SHA-256:
  `7D4322BD2A7749724879683FC3912CB542F19906C83BCC1A52132556427170B2`
- OSD language data:
  `D:\NRI\.tools\tesseract\tessdata\osd.traineddata`
- OSD language data SHA-256:
  `9CF5D576FCC47564F11265841E5CA839001E7E6F38FF7F7AACF46D15A96B00FF`

Allowed outputs:

- One refreshed OCR candidate manifest with status
  `candidate_config_frozen_for_review`, exact executable/version/language data,
  config, remaining blockers, and invalidation rules.

Produced output:

- OCR candidate manifest:
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_candidate_manifest.md`
- Manifest id: `OCM-G1-VIRAL-001`
- Output status: `candidate_config_frozen_for_review`

Limits:

- Do not run OCR.
- Do not create OCR output, benchmark results, QA findings, fixtures, source
  acceptance, translation, proofreading, or implementation.
- Do not treat executable discovery/config freeze as OCR benchmark
  authorization or Gate 1 acceptance.

Expiry:

- Expires after the first refreshed `OCM-G1-VIRAL-001` manifest is created, or
  at 2026-07-19T19:00:00+03:00, whichever comes first.

Invalidation behavior:

- Refreshed `OCM-G1-VIRAL-001` stales on protocol revision/blob change,
  baseline commit supersession, authorization change, executable path/hash
  change, Tesseract version change, language data path/hash change, OCR config
  change, output format change, preprocessing policy change, reviewer/authority
  change, or predecessor remediation/supersession.

## BA-G1-VIRAL-OCRBENCH-001

Status: `expired`; scope consumed by `ORB-G1-VIRAL-001`,
`OOM-G1-VIRAL-001`, and `OBR-G1-VIRAL-002`

Created: 2026-07-18

Authority: user request from Bogdan: "Ок делай план" after reviewing the
10-step OCR benchmark plan.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `30025b4b9cebff5de4701b44e3b9d2aa4c1f80dc`

Exact action:

- Execute one bounded OCR benchmark over the five gold-sample region crops
  named below, using the frozen local Tesseract candidate from
  `OCM-G1-VIRAL-001`.

Admitted inputs:

- Pre-OCR map bundle: `POMB-G1-VIRAL-001`
- Pre-OCR map bundle SHA-256:
  `B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F`
- Gold sample manifest: `GSM-G1-VIRAL-001`
- Gold sample manifest SHA-256:
  `A7EA3157815D8F3311AFA91B0EF70F97AE9E6C0C7F4D76203983C1B0341B7D62`
- OCR candidate manifest: `OCM-G1-VIRAL-001`
- OCR candidate manifest SHA-256:
  `6FBDC9463A670968D335DFB8F841819CEB55CDC24B2CFC1C32EF9AA9BD323842`
- Rendered page images already produced by `RT-G1-VIRAL-RENDER-001` for
  pages 1, 5, and 6 only.

Admitted sample crop boxes:

| Sample id | Page image | Trial region | Crop box |
|---|---|---|---|
| `GS-G1-VIRAL-001` | `page_001.png` | `RG-G1-VIRAL-P001-R002` | `[760,260,1050,760]` |
| `GS-G1-VIRAL-002` | `page_005.png` | `RG-G1-VIRAL-P005-R001` | `[920,260,750,280]` |
| `GS-G1-VIRAL-003` | `page_005.png` | `RG-G1-VIRAL-P005-R002` | `[260,600,2050,2300]` |
| `GS-G1-VIRAL-004` | `page_006.png` | `RG-G1-VIRAL-P006-R002` | `[200,320,950,360]` |
| `GS-G1-VIRAL-005` | `page_006.png` | `RG-G1-VIRAL-P006-R003` | `[220,1550,2100,1400]` |

Allowed outputs:

- One OCR run boundary report.
- Five benchmark input crop PNG files derived from admitted rendered PNGs.
- Raw Tesseract output files: text, TSV, command logs, and stderr captures for
  each admitted sample crop.
- One OCR output manifest with hashes and exit/status metadata.
- One OCR benchmark result report with sample-level findings and recommendation
  only.

Limits:

- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not run OCR outside the five admitted sample crops.
- Do not manually edit OCR outputs.
- Do not create QA acceptance, fixture acceptance, source-profile acceptance,
  translation, proofreading, renderer/profile acceptance, implementation, or
  Gate 1 advancement.
- Do not promote gold sample text or OCR text into accepted source text.

Expiry:

- Expires after the first `OBR-G1-VIRAL-002` benchmark result report is
  created, or at 2026-07-19T19:00:00+03:00, whichever comes first.

Invalidation behavior:

- All outputs stale on protocol revision/blob change, baseline commit
  supersession, authorization change, POMB/GSM/OCM hash change, rendered page
  image hash change, crop box/sample selection change, Tesseract executable or
  language data identity change, config change, output format change,
  reviewer/authority change, or predecessor remediation/supersession.

## BA-G1-VIRAL-REMEDIATE-001

Status: `expired`; scope consumed by `ORM-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan to build a full, detailed transfer plan for
the prior OCR method logic, involve Sol/Terra/critics/analysts, recreate the
logic inside Sourcefold without old file/script/variable naming, and continue
until the five current samples pass the remediation metrics.

Protocol prerequisite:

- Gate 1 Qualification Protocol exact revision:
  `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Protocol file blob:
  `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Baseline commit:
  `684a6400d8ffb5b6f9d6db2e289069408dfd0bda`

Exact action:

- Create one Sourcefold-native OCR remediation matrix over exactly the five
  existing Viral gold samples, using already rendered page PNGs and the frozen
  local Tesseract candidate.
- Recreate the prior OCR method logic as neutral Sourcefold evidence logic:
  route by sample/region type, test a bounded OCR matrix, compute overlay QC,
  compute order/zone QC, record route findings, and keep all scores as review
  evidence only.

Admitted inputs:

- Pre-OCR map bundle: `POMB-G1-VIRAL-001`
- Pre-OCR map bundle SHA-256:
  `B000FB2212D538212097BD71B695024CA5208988927616397B9F215C4FCC2B9F`
- Gold sample manifest: `GSM-G1-VIRAL-001`
- Gold sample manifest SHA-256:
  `A7EA3157815D8F3311AFA91B0EF70F97AE9E6C0C7F4D76203983C1B0341B7D62`
- OCR candidate manifest: `OCM-G1-VIRAL-001`
- OCR candidate manifest SHA-256:
  `6FBDC9463A670968D335DFB8F841819CEB55CDC24B2CFC1C32EF9AA9BD323842`
- Prior OCR benchmark result: `OBR-G1-VIRAL-002`
- Prior OCR benchmark result SHA-256:
  `AFC2D58AB9B22ADD6A0B345BB72FA630049FBB1855771A1EF2ADDCC20D646937`
- Rendered page images already produced by `RT-G1-VIRAL-RENDER-001` for
  pages 1, 5, and 6 only.

Allowed outputs:

- One detailed transfer/remediation plan using Sourcefold-native names only.
- One Sourcefold-native matrix runner script under `scripts/`.
- Refined route crop PNGs derived only from the admitted rendered page PNGs.
- Prepared input variants for bounded OCR zones.
- Raw Tesseract text, TSV, command log, and stderr outputs for the matrix.
- Payload-light JSON matrix rows and score report.
- One OCR remediation output manifest with hashes, route findings, limits, and
  invalidation rules.

Metrics:

- `remediation_route_pass` for all five samples is the target metric.
- OCR-capable zones must use normalized exact match plus complete token recall.
- Decorative or page-number components that remain unsuitable for reliable OCR
  may pass only through explicit `visual_qc_route_pass`, which is routing
  evidence and not text acceptance.
- Any route pass is evidence for review only; it is not source acceptance,
  source-profile acceptance, QA, fixture creation, translation, proofreading,
  renderer/profile acceptance, implementation, or Gate 1 advancement.

Limits:

- Do not open, parse, rehash, recount, or inspect the PDF.
- Do not run OCR outside the five admitted sample routes.
- Do not import, call, copy, or depend on any prior-project scripts, configs,
  caches, package models, or path layouts.
- Do not manually edit raw OCR outputs.
- Do not promote gold sample text, OCR output, visual-route findings, scores,
  or review queues into accepted source text.
- Do not add raw OCR text or TSV payloads to roadmap YAML or status rollups.

Expiry:

- Expires after the first `ORM-G1-VIRAL-001` output manifest is created, or at
  2026-07-19T20:30:00+03:00, whichever comes first.

Invalidation behavior:

- All outputs stale on protocol revision/blob change, baseline commit
  supersession, authorization change, POMB/GSM/OCM/OBR hash change, rendered
  page image hash change, crop route change, Tesseract executable or language
  data identity change, preprocessing or PSM matrix change, scoring rule
  change, reviewer/authority change, or predecessor remediation/supersession.

## BA-G1-VIRAL-REMEDIATION-REVIEW-001

Status: `expired`; scope consumed by `ORR-G1-VIRAL-001`, `OAC-G1-VIRAL-001`,
`GER-G1-VIRAL-001`, and `ONC-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Иди делать. С учетом контента" after
reviewing the 12-step plan and confirming that Bogdan should only be involved
when a human-readable source reconstruction package exists.

Predecessors:

- `ORM-G1-VIRAL-001` remediation matrix evidence only.
- `BA-G1-VIRAL-REMEDIATE-001` is `expired`; scope consumed by
  `ORM-G1-VIRAL-001`.
- `POMB-G1-VIRAL-001`
- `GSM-G1-VIRAL-001`
- `OCM-G1-VIRAL-001`
- `OBR-G1-VIRAL-002`
- Commit predecessor: `f90d170b`

Exact action:

- Build one Sourcefold-native OCR remediation review/admission/rollup package
  from existing `ORM-G1-VIRAL-001` JSON/manifest evidence only.
- Add reproducible generator and pytest contract checks for review boundaries,
  lineage, payload-light rollups, and no acceptance-by-score.

Allowed outputs:

- `scripts/build_ocr_remediation_review_package.py`
- `tests/test_ocr_remediation_review_package.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_remediation_review_G1_VIRAL_001/ocr_remediation_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_remediation_review_G1_VIRAL_001/ocr_remediation_review_report.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_remediation_review_G1_VIRAL_001/ocr_admission_candidate.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_remediation_review_G1_VIRAL_001/evidence_rollup.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_remediation_review_G1_VIRAL_001/negative_check_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_remediation_review_G1_VIRAL_001/orchestration_record.md`
- Payload-light roadmap/status/plan/context checkpoint updates.

Output status:

- Review id: `ORR-G1-VIRAL-001`
- Admission candidate id: `OAC-G1-VIRAL-001`
- Evidence rollup id: `GER-G1-VIRAL-001`
- Negative check id: `ONC-G1-VIRAL-001`
- Status: `remediation_evidence_only`

Limits:

- Do not run OCR.
- Do not run `scripts/run_ocr_remediation_matrix.py`.
- Do not create, delete, or modify `ORM-G1-VIRAL-001` raw outputs, input crops,
  prepared inputs, or matrix rows.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not copy raw OCR text, TSV rows, or selected OCR payload text into
  roadmap/status/plan/context rollups.
- Do not use old-project scripts, imports, config schemas, runtime paths, cache
  roots, or names as live Sourcefold dependencies.
- Do not create QA findings, fixtures, canonical source-text artifacts, source-profile
  acceptance, translation, proofreading, renderer/profile acceptance,
  implementation, or Gate 1 advancement.

Review/admission rules:

- `5/5 remediation_route_pass` may support review admission only.
- Visual-QC route findings are routing evidence only; they are not transcription
  or text acceptance.
- Bogdan human review remains deferred until a separate source reconstruction
  package contains readable text aligned to source page images/regions.
- Sol/Terra and local contract tests handle technical validity before that
  human-readable package exists.

Invalidation:

This package stales if protocol revision/blob changes, authorization changes,
POMB/GSM/OCM/OBR/ORM hashes change, rendered image hashes change, crop routes
change, OCR tool identity changes, preprocessing or PSM matrix changes, scoring
rules change, generator/test revision changes, reviewer/authority changes, or
predecessor remediation/supersession occurs.

## BA-G1-VIRAL-SOURCE-RECON-PREP-001

Status: `expired`; scope consumed by `SRP-G1-VIRAL-001`,
`SRA-G1-VIRAL-001`, and `SRD-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Ок, поехали" after reviewing the
Sol/Terra-corrected source reconstruction preparation plan.

Predecessors:

- `POMB-G1-VIRAL-001`
- `GSM-G1-VIRAL-001`
- `OCM-G1-VIRAL-001`
- `ORR-G1-VIRAL-001`
- `OAC-G1-VIRAL-001`
- `GER-G1-VIRAL-001`
- `ONC-G1-VIRAL-001`
- Commit predecessor:
  `02a0c643a6f0d83fb8b3dd35f428b9269c800f69`

Exact action:

- Prepare source reconstruction protocol, exact admitted region manifest,
  fail-closed generator skeleton, dry-run checks, and pytest contract checks.
- This is preparation only. It does not execute OCR and does not produce a
  human-readable source reconstruction package.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_prep_G1_VIRAL_001/source_reconstruction_protocol.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_prep_G1_VIRAL_001/source_reconstruction_admitted_manifest.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_prep_G1_VIRAL_001/source_reconstruction_dry_run_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_prep_G1_VIRAL_001/orchestration_record.md`
- `scripts/build_source_reconstruction_review_package.py`
- `tests/test_source_reconstruction_review_package.py`
- Payload-light roadmap/status/plan/context checkpoint updates.

Output status:

- Protocol id: `SRP-G1-VIRAL-001`
- Admitted manifest id: `SRA-G1-VIRAL-001`
- Dry-run report id: `SRD-G1-VIRAL-001`
- Status: `source_reconstruction_prep_only`

Limits:

- Do not run OCR.
- Do not create candidate source text.
- Do not create accepted source text.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not manually edit raw OCR outputs.
- Do not create QA acceptance, fixtures, translation, proofreading,
  renderer/profile acceptance, implementation, or Gate 1 advancement.
- Do not use old-project scripts, imports, configs, path layouts, runtime
  directories, cache roots, or names as live Sourcefold dependencies.
- `OAC-G1-VIRAL-001` may be used only as a configuration hint for a later
  separately authorized run; it is not OCR admission or source acceptance.

Run boundary:

- `scripts/build_source_reconstruction_review_package.py` must fail closed by
  default and may generate only dry-run/precheck artifacts under this
  authorization.
- Any future source reconstruction execution requires a distinct
  `BA-G1-VIRAL-SOURCE-RECON-RUN-001` authorization naming exact inputs,
  command, config, output directory, limits, expiry, invalidation behavior, and
  admitted manifest hash.

Human review boundary:

- Bogdan is not asked to review results from this prep package.
- Bogdan is asked only after a later separately authorized package contains
  readable candidate text aligned to page images/regions, uncertainty findings,
  overlay/order QC, and clear review options.

Invalidation:

This prep package stales if protocol revision/blob changes, authorization
changes, POMB/GSM/OCM/ORR/OAC/GER/ONC hashes change, rendered image hashes
change, admitted manifest scope changes, script/test revision changes, run
authorization policy changes, reviewer/authority changes, or predecessor
remediation/supersession occurs.

## BA-G1-VIRAL-SOURCE-RECON-RUN-001

Status: `expired`; scope consumed by `SRM-G1-VIRAL-001`,
`SRQ-G1-VIRAL-001`, and `G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Идем дальше, по плану, фиксим прошлые
долги" after `BA-G1-VIRAL-SOURCE-RECON-PREP-001` was committed.

Predecessors:

- `SRP-G1-VIRAL-001`
- `SRA-G1-VIRAL-001`
- `SRD-G1-VIRAL-001`
- `ORR-G1-VIRAL-001`
- `OAC-G1-VIRAL-001`
- Commit predecessor: `1003d74f`

Exact action:

- Assemble one source reconstruction candidate review package from existing
  selected OCR evidence and visual-QC route evidence only.
- Use `scripts/build_source_reconstruction_review_package.py` with exact
  authorization id and exact `SRA-G1-VIRAL-001` hash.

Exact command:

```powershell
python scripts\build_source_reconstruction_review_package.py --execute --authorization-id BA-G1-VIRAL-SOURCE-RECON-RUN-001 --admitted-manifest-sha256 59D146B024EBAEB548D2BD5F03BF3027632C4F289FD2FFAC36F36879501277E9
```

Admitted input:

- `SRA-G1-VIRAL-001`
- SHA-256:
  `59D146B024EBAEB548D2BD5F03BF3027632C4F289FD2FFAC36F36879501277E9`

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_review_G1_VIRAL_001/source_reconstruction_run_manifest.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_review_G1_VIRAL_001/source_reconstruction_precheck.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_review_G1_VIRAL_001/raw_ocr_candidate_for_human_review.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_review_G1_VIRAL_001/orchestration_record.md`
- Updated pytest contracts and payload-light checkpoint docs.

Output status:

- Run manifest id: `SRM-G1-VIRAL-001`
- Precheck id: `SRQ-G1-VIRAL-001`
- Review package id: `G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001`
- Status: `candidate_review_blocked_for_remediation`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not manually edit raw OCR outputs.
- Do not create accepted source text, QA acceptance, fixtures, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.
- Candidate text may be assembled only from selected OCR evidence whose hashes
  already exist in `OAC-G1-VIRAL-001`.
- Visual-QC-only components must not produce candidate text.

Human review boundary:

- This package must not be presented to Bogdan for source approval until
  visual-QC and overlay-QC blockers are remediated.
- Any corrections must go to a separate corrections/remediation artifact and
  must not edit raw OCR outputs.

Invalidation:

This run package stales if SRA hash changes, predecessor hashes change, selected
OCR evidence hashes change, visual-QC routes change, script/test revision
changes, output schema changes, reviewer/authority changes, or predecessor
remediation/supersession occurs.

## BA-G1-VIRAL-SOURCE-RECON-REMEDIATE-001

Status: `expired`; scope consumed by `SRCR-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Коммит. И двигайся дальше" after
`SRM-G1-VIRAL-001` was committed as blocked for remediation.

Exact action:

- Triage `G1-VIRAL-SOURCE-RECONSTRUCTION-REVIEW-001` blockers into exact
  cleanup, overlay verification, crop remediation, and visual-QC routes.
- No OCR execution and no raw-output edits.

Allowed outputs:

- `scripts/remediate_source_reconstruction_candidate.py`
- `tests/test_source_reconstruction_candidate_remediation.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_remediation_G1_VIRAL_001/source_reconstruction_remediation_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_remediation_G1_VIRAL_001/source_reconstruction_remediation_report.md`

Output status:

- Report id: `SRCR-G1-VIRAL-001`
- Status: `remediation_triage_only`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not edit raw OCR outputs.
- Do not create accepted source text, QA acceptance, fixtures, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.
- Do not present the candidate package to Bogdan for source approval.

Invalidation:

This remediation triage stales if `SRM-G1-VIRAL-001`, `SRQ-G1-VIRAL-001`, the
review package, selected OCR evidence, visual-QC routes, script/test revision,
reviewer/authority, or predecessor remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-CROP-REMEDIATE-001

Status: `expired`; scope consumed by `SRCO-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Коммит. И двигайся дальше" after
`SRCR-G1-VIRAL-001` identified crop/overlay debts.

Exact action:

- Prepare exact crop/overlay remediation evidence from `SRCR-G1-VIRAL-001`.
- Create reference crop/overlay PNG artifacts from existing rendered PNG crop
  inputs only.
- Prepare one narrowed contents subcrop for later separately authorized OCR
  rerun.

Allowed outputs:

- `scripts/remediate_source_reconstruction_crop_overlay.py`
- `tests/test_source_reconstruction_crop_overlay_remediation.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_crop_overlay_G1_VIRAL_001/source_reconstruction_crop_overlay_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_crop_overlay_G1_VIRAL_001/source_reconstruction_crop_overlay_report.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_crop_overlay_G1_VIRAL_001/crop_overlay_refs/*.png`

Output status:

- Report id: `SRCO-G1-VIRAL-001`
- Status: `crop_overlay_remediation_evidence_only`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create accepted source text, QA acceptance, fixtures, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.
- Do not present the candidate package to Bogdan for source approval.

Invalidation:

This crop/overlay remediation stales if `SRCR-G1-VIRAL-001`, source crop PNGs,
selected OCR evidence, visual-QC routes, script/test revision, reviewer/authority,
or predecessor remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001

Status: `expired`; scope consumed by `SRFO-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Коммит. И двигайся дальше" after
`SRCO-G1-VIRAL-001` prepared one refined crop requiring a separately bounded
OCR rerun.

Exact action:

- Run OCR only on `SRA-G1-VIRAL-001-R003` refined crop from
  `SRCO-G1-VIRAL-001`.
- Bind exact input crop SHA-256
  `A09B5848048C3BD20FEB71B0FC37FC55E108AA08454BCFB1156D3FAD62E5B40F`,
  source crop SHA-256
  `54E0E3B0A956EA0BA215987D25B242EED3A803100AD87C2E8949E3EA4592F66A`, and
  predecessor report SHA-256
  `08B77397484FF43C6E4E466632531B15829EA3C34A75F79C6DE84B70E433C78F`.
- Evaluate only refined-crop visible text scope; do not replace the full
  contents/list region.

Allowed outputs:

- `scripts/run_source_reconstruction_refined_ocr.py`
- `tests/test_source_reconstruction_refined_ocr.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_refined_ocr_G1_VIRAL_001/source_reconstruction_refined_ocr_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_refined_ocr_G1_VIRAL_001/source_reconstruction_refined_ocr_rows.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_refined_ocr_G1_VIRAL_001/source_reconstruction_refined_ocr_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_refined_ocr_G1_VIRAL_001/prepared_inputs/*.png`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_refined_ocr_G1_VIRAL_001/raw_outputs/*`

Output status:

- Run id: `SRFO-G1-VIRAL-001`
- Status: `refined_ocr_evidence_only`

Limits:

- Do not OCR any crop except `SRA-G1-VIRAL-001-R003`.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit predecessor raw OCR outputs.
- Do not regenerate or present the source reconstruction package to Bogdan.
- Do not create accepted source text, QA acceptance, fixtures, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.

Invalidation:

This refined OCR evidence stales if `SRCO-G1-VIRAL-001`, the refined crop,
source crop, OCR engine/config identity, preprocessing matrix, metric scope,
script/test revision, reviewer/authority, or predecessor
remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-REBUILD-001

Status: `expired`; scope consumed by `SRRB-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Коммит. И двигайся дальше" after
`SRFO-G1-VIRAL-001` created refined OCR evidence and recommended a rebuild
step.

Exact action:

- Rebuild a source reconstruction candidate evidence package from exact
  `SRCO-G1-VIRAL-001` and `SRFO-G1-VIRAL-001` report hashes.
- Consolidate remaining visual/overlay blockers without running OCR and
  without presenting the package to Bogdan for source approval.

Allowed outputs:

- `scripts/rebuild_source_reconstruction_candidate.py`
- `tests/test_source_reconstruction_rebuild.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_rebuild_G1_VIRAL_001/source_reconstruction_rebuild_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_rebuild_G1_VIRAL_001/source_reconstruction_rebuild_manifest.md`

Output status:

- Package id: `SRRB-G1-VIRAL-001`
- Status: `rebuilt_candidate_blocked_for_visual_overlay_review`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create accepted source text, QA acceptance, fixtures, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.
- Do not present this rebuilt package as human-ready.

Invalidation:

This rebuild stales if `SRCO-G1-VIRAL-001`, `SRFO-G1-VIRAL-001`, crop
references, selected OCR evidence, script/test revision, reviewer/authority, or
predecessor remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001

Status: `expired`; scope consumed by `SRVO-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Делай 1-5 + сними блокеры" after
`SRRB-G1-VIRAL-001` remained blocked for visual/overlay review.

Exact action:

- Review exact `SRRB-G1-VIRAL-001` visual/overlay blockers using existing
  `SRCO-G1-VIRAL-001` crop/overlay references and source input crops only.
- Record manual visual/overlay decisions that close the remaining visual,
  overlay, and full-region replacement blockers for later human review.
- Produce candidate text only as later human-review input, not accepted source
  text.

Allowed outputs:

- `scripts/review_source_reconstruction_visual_overlay.py`
- `tests/test_source_reconstruction_visual_overlay_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_visual_overlay_review_G1_VIRAL_001/source_reconstruction_visual_overlay_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_visual_overlay_review_G1_VIRAL_001/source_reconstruction_visual_overlay_review_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_visual_overlay_review_G1_VIRAL_001/candidate_text_for_later_human_review.md`

Output status:

- Report id: `SRVO-G1-VIRAL-001`
- Status: `visual_overlay_blockers_closed_for_later_human_review`
- Report SHA-256:
  `54ABBA9FA01B8AFECB2C2B4FD12EE4FCFD2EDA5B0B2948FB4A2D4C17238E2BF8`
- Manifest SHA-256:
  `F19ACB7FC4C90580F12D904E53168DB2FADE85787E455FBEBDE56B436AB63E58`
- Candidate text SHA-256:
  `31B11EAB6C4FD85B4F47D30C6CAD9444A86D4248DD44A82211F0E0F4620D455E`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create accepted source text, QA acceptance, fixtures, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.
- Candidate text is ready only for later human review and remains explicitly
  not source-accepted.

Invalidation:

This visual/overlay review stales if `SRRB-G1-VIRAL-001`, `SRCO-G1-VIRAL-001`,
crop references, source input crops, manual decision rules, script/test
revision, reviewer/authority, or predecessor remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001

Status: `expired`; scope consumed by `SRHP-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Делай 1-5" after `SRVO-G1-VIRAL-001`
closed visual/overlay blockers and recommended human package assembly.

Exact action:

- Assemble a reproducible human-review package from exact `SRVO-G1-VIRAL-001`
  only.
- Include clean candidate text, visual-only exclusions, route identity, source
  crop references, and hash lineage.
- Preserve the boundary that the package is for later human review only and is
  not accepted source text.

Allowed outputs:

- `scripts/assemble_source_reconstruction_human_package.py`
- `tests/test_source_reconstruction_human_package.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_human_package_G1_VIRAL_001/source_reconstruction_human_package_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_human_package_G1_VIRAL_001/source_reconstruction_human_package_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_human_package_G1_VIRAL_001/human_review_package.md`

Output status:

- Package id: `SRHP-G1-VIRAL-001`
- Status: `human_review_package_ready_not_source_accepted`
- Report SHA-256:
  `2A5A475737BF6442B11DFB26CE6E62724978B9F797E37A8BAB843BF2534017CC`
- Manifest SHA-256:
  `B451E50362AD9D0E944812F03BBAE01FAD9777A044CD252DFA02B41F9721C71A`
- Human review package SHA-256:
  `2B5481B3D4F6BF51A10EAF0E0B3EC65E2526E2C4796D8E6A1C4B214B92815F12`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create accepted source text, QA acceptance, fixtures, translation,
  proofreading, renderer/profile acceptance, implementation, or Gate 1
  advancement.
- Do not treat human-review readiness as source approval.

Invalidation:

This human package stales if `SRVO-G1-VIRAL-001`, source crop references,
candidate text decisions, script/test revision, reviewer/authority, or
predecessor remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001

Status: `expired`; scope consumed by `SRHR-G1-VIRAL-001`

Created: 2026-07-18

Authority: Bogdan page-by-page Telegram human review responses:

- Message `251`: `1 ok, 2 ok`
- Message `257`: `3 ok, 5 ok`; message `260`: `4 ok` after corrected full-crop packet
- Message `265`: `6 ok, 7 ok`
- Assistant packet message ids: `248`, `253`, `259`, `262`

Exact action:

- Record Bogdan's seven numbered source reconstruction review decisions from
  `SRHP-G1-VIRAL-001`.
- Preserve R003 packet correction: initial narrow reference did not show the
  full candidate; full source crop was resent before acceptance.
- Preserve Bogdan's semantic heading hint for R003 as review metadata, not as a
  source-text mutation.
- Treat accepted candidate text as source-review accepted only.

Allowed outputs:

- `scripts/record_source_reconstruction_human_review.py`
- `tests/test_source_reconstruction_human_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_human_review_G1_VIRAL_001/source_reconstruction_human_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_human_review_G1_VIRAL_001/source_reconstruction_human_review_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_human_review_G1_VIRAL_001/source_review_accepted_text.md`

Output status:

- Review id: `SRHR-G1-VIRAL-001`
- Status: `source_review_accepted_not_qa_accepted`
- Report SHA-256:
  `FF7C9778E711D67964584CD00870762FD7ADE47E4368EA71DD3C373AB5EB4980`
- Manifest SHA-256:
  `8D50E70EAF438A990D1EC11A1C9239A8CA5CF8AE1D8E91CBDD6585E5ADDDA62B`
- Accepted text SHA-256:
  `E623AD3DD9246B4DB30BB43A7A929CB13686E57ED02C44756FA365B65AB2D3E2`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create QA acceptance, fixtures, translation, proofreading,
  renderer/profile acceptance, implementation, or Gate 1 advancement.
- Do not treat semantic heading hints as source-text mutation.

Invalidation:

This human review record stales if `SRHP-G1-VIRAL-001`, Telegram review
message ids/content, source crop references, candidate text decisions,
script/test revision, reviewer/authority, or predecessor
remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-QA-001

Status: `expired`; scope consumed by `SRQA-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Делай 1-5" after `SRHR-G1-VIRAL-001`
recommended source reconstruction QA.

Exact action:

- QA exact `SRHR-G1-VIRAL-001` report and accepted-text hashes only.
- Verify four accepted source-text records and three accepted visual-only
  exclusions.
- Verify R003 corrected-full-crop note and semantic heading hint are preserved
  as metadata.
- Preserve the boundary that this QA does not create fixtures or advance Gate 1.

Allowed outputs:

- `scripts/qa_source_reconstruction_human_review.py`
- `tests/test_source_reconstruction_qa.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_qa_G1_VIRAL_001/source_reconstruction_qa_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_qa_G1_VIRAL_001/source_reconstruction_qa_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_qa_G1_VIRAL_001/source_reconstruction_qa_summary.md`

Output status:

- QA id: `SRQA-G1-VIRAL-001`
- Status: `source_reconstruction_qa_passed_not_fixture_or_gate`
- Report SHA-256:
  `A98811F3368FD468618A111D9F7A85BFFBD72CE9387CCF11DA011875C80553E0`
- Manifest SHA-256:
  `2AA2D6144741188B2C1801487D72A46C3BED7931EB733C6FB1547A062BC7E7AE`
- Summary SHA-256:
  `C7C32A1D4E9A74DC3F086D4D355151BF6C89DBDE576775AC0F67312E98981EC3`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create fixtures, translation, proofreading, renderer/profile
  acceptance, implementation, or Gate 1 advancement.

Invalidation:

This source reconstruction QA record stales if `SRHR-G1-VIRAL-001`, accepted
source text, source crop references, script/test revision, reviewer/authority,
or predecessor remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001

Status: `expired`; scope consumed by `SRFA-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Готовь план, делай коммит. И двигайся по нему" after `SRQA-G1-VIRAL-001`
recommended fixture admission as the next bounded continuation.

Exact action:

- Admit exact `SRQA-G1-VIRAL-001` report and summary hashes only.
- Create stable downstream source reconstruction fixtures for four accepted
  source-text records and three accepted visual-only exclusions.
- Preserve R003 corrected-full-crop note and semantic heading hint as metadata.
- Preserve the boundary that fixture admission does not advance Gate 1.

Allowed outputs:

- `scripts/admit_source_reconstruction_fixtures.py`
- `tests/test_source_reconstruction_fixture_admission.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_fixture_admission_G1_VIRAL_001/source_reconstruction_fixture_admission_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_fixture_admission_G1_VIRAL_001/source_reconstruction_fixture_admission_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_fixture_admission_G1_VIRAL_001/source_reconstruction_admitted_fixtures.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_fixture_admission_G1_VIRAL_001/source_reconstruction_fixture_admission_summary.md`

Output status:

- Fixture admission id: `SRFA-G1-VIRAL-001`
- Status: `source_reconstruction_fixtures_admitted_not_gate`
- Report SHA-256:
  `485ECEAAC7CC1CC3FBE95341ED7A0F5E68345EF59CCC8CEB7F8F57706A541A1C`
- Manifest SHA-256:
  `7409220DDFABC6DEE69C3718D3A5686EF6DD6ECFC013EFD9341BCB2AD8C3E764`
- Admitted fixtures SHA-256:
  `1B9DA0A5BF9E219059065F3C1517B4C0E1265060F578F1C6007E9C2AA1611B9F`
- Summary SHA-256:
  `DC76D7677EE76EFBAF7BCBBF7ED7C0BED38727CC0E9EAB63C3F7F26DF2013949`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance,
  implementation, or Gate 1 advancement.
- Do not treat admitted fixtures as broader source/profile acceptance.

Invalidation:

This source reconstruction fixture admission record stales if
`SRQA-G1-VIRAL-001`, admitted fixture ids, source crop references, script/test
revision, reviewer/authority, or predecessor remediation/supersession changes.

## BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001

Status: `expired`; scope consumed by `G1RP-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Ок, делай" after `SRFA-G1-VIRAL-001`
recommended a Gate 1 review packet as the next bounded continuation.

Exact action:

- Package exact `SRFA-G1-VIRAL-001` report, admitted fixtures, and summary
  hashes only.
- Create a review packet for seven admitted source reconstruction fixtures.
- Preserve R003 corrected-full-crop note and semantic heading hint as metadata.
- Preserve the boundary that packet readiness does not advance Gate 1.

Allowed outputs:

- `scripts/build_gate_1_review_packet.py`
- `tests/test_gate_1_review_packet.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_packet_G1_VIRAL_001/gate_1_review_packet_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_packet_G1_VIRAL_001/gate_1_review_packet_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_packet_G1_VIRAL_001/gate_1_review_packet.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_packet_G1_VIRAL_001/gate_1_review_packet_summary.md`

Output status:

- Packet id: `G1RP-G1-VIRAL-001`
- Status: `gate_1_review_packet_ready_not_advanced`
- Report SHA-256:
  `AE3695954BE26DB60EB541CD9819532CE5CA98F961D0F0B21F06C0BE5F96D990`
- Manifest SHA-256:
  `E21D57630A3AB235AE901D3A27375F16527A81F0DE584D80EEA5527AA382DE86`
- Packet SHA-256:
  `8197860F5176CB25423D6CE6EDB30B831E603D369C100A3F79105620894EDCF9`
- Summary SHA-256:
  `93424483B2C870028A2330F79C81F0A3C270A2E5A9085314D4687C89D2F628EC`

Limits:

- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance,
  implementation, or Gate 1 advancement.
- Do not treat packet readiness as Gate 1 acceptance.

Invalidation:

This Gate 1 review packet stales if `SRFA-G1-VIRAL-001`, packet item ids,
source crop references, script/test revision, reviewer/authority, or
predecessor remediation/supersession changes.

## BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001

Status: `expired`; scope consumed by `G1RDB-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Как делать будем? Накидай план до
\"нужен я чтобы посмотреть\". И двигайся по плану, помни оркестрация и сол
+терра" after `G1RP-G1-VIRAL-001` recommended a Gate 1 review decision step.

Exact action:

- Prepare a user-facing Gate 1 review decision brief/checklist only.
- Consume exact `G1RP-G1-VIRAL-001` report, manifest, packet, and summary
  hashes.
- Include upstream SRFA and SRQA lineage.
- Include accept, hold, reject, and park answer shapes for Bogdan.
- Preserve the boundary that brief readiness does not record or advance Gate 1.

Allowed outputs:

- `scripts/prepare_gate_1_review_decision_brief.py`
- `tests/test_gate_1_review_decision_brief.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_brief_G1_VIRAL_001/gate_1_review_decision_brief_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_brief_G1_VIRAL_001/gate_1_review_decision_brief_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_brief_G1_VIRAL_001/gate_1_review_decision_brief.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_brief_G1_VIRAL_001/gate_1_review_decision_brief.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_brief_G1_VIRAL_001/gate_1_review_decision_brief_summary.md`

Output status:

- Brief id: `G1RDB-G1-VIRAL-001`
- Status: `gate_1_review_decision_brief_ready_requires_bogdan`
- Report SHA-256:
  `E577B18D7E8945C39FA5286D83FD9D8607B45636ABD82243ED4A9F002B306FE8`
- Manifest SHA-256:
  `EC3D26066BDEB40CE2F83617AE153D850D8232F79B2B11E432C96D09F40B84AC`
- Brief JSON SHA-256:
  `3D262623ACB6111F7D50D9B2D22594AABEF06128737D4FC8445FF55B90D71E53`
- Brief Markdown SHA-256:
  `16C776322C46E969C4D63383CAE546CC5C4E12A79F1992AF5E07763D1B56C15E`
- Summary SHA-256:
  `4FD01474019842560592BC54D6707ECFE0ECFA92E79E84910AE16A09EEACC799`

Limits:

- Do not record a Gate 1 decision.
- Do not set `gate_1_advancement=true`.
- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance, or
  implementation.
- Treat inherited `source_acceptance` and `qa_acceptance` as exact SRHR/SRQA
  lineage facts only, not new G1RP/Gate acceptance.

Invalidation:

This Gate 1 review decision brief stales if `G1RP-G1-VIRAL-001`, packet item
ids, accepted protocol revision, Sol/Terra review requirements, script/test
revision, reviewer/authority, or predecessor remediation/supersession changes.

## BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001

Status: `expired`; scope consumed by `G1RD-G1-VIRAL-001`

Created: 2026-07-18

Authority: user decision from Bogdan in Telegram message 303: "1 принято",
after clarifying that acceptance is limited to seven reviewed records and does
not accept pages as complete.

Exact action:

- Record Bogdan's decision against exact `G1RDB-G1-VIRAL-001` hashes.
- Accept exact `G1RP-G1-VIRAL-001` as a narrow Gate 1 source reconstruction
  evidence slice only.
- Preserve `accepted_records=7`, `accepted_pages_as_complete=false`, and
  `whole_gate_1_acceptance=false`.
- Preserve the boundary that this decision does not authorize translation,
  proofreading, renderer/profile acceptance, implementation, push, OCR, PDF
  parsing, rendering, or raw OCR mutation.

Allowed outputs:

- `scripts/record_gate_1_review_decision.py`
- `tests/test_gate_1_review_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_G1_VIRAL_001/gate_1_review_decision_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_G1_VIRAL_001/gate_1_review_decision_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_G1_VIRAL_001/gate_1_review_decision_record.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_G1_VIRAL_001/gate_1_review_decision_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_review_decision_G1_VIRAL_001/gate_1_review_decision_summary.md`

Output status:

- Decision id: `G1RD-G1-VIRAL-001`
- Status: `gate_1_source_reconstruction_evidence_slice_accepted`
- Report SHA-256:
  `8F1FD747C95B758B2227C6483B09D34DB37A786B7988DA68EEB721A7942547C3`
- Manifest SHA-256:
  `96C9C73219E97DCB6FBCF1170C7A9582FC69634585D78CC7FC245D7C94D0D39D`
- Decision record SHA-256:
  `1300B2E068B514493596156BC4A57D476491915D76EA6A0A7779FC2C14A5D271`
- Decision record Markdown SHA-256:
  `F896C6375C44AF002B883A8441BE3FB504D8DE5CD01962B6C04322065BEFAC9E`
- Summary SHA-256:
  `5F6B819DBE127847951E84CB50571FD1838278A7707E26FE0765E4C2A725A4A5`

Limits:

- Do not accept pages as complete.
- Do not accept whole Gate 1.
- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance,
  implementation, or push.

Invalidation:

This Gate 1 review decision stales if `G1RDB-G1-VIRAL-001`, Bogdan's decision
message, packet item ids, accepted protocol revision, Sol/Terra review
requirements, script/test revision, reviewer/authority, or predecessor
remediation/supersession changes.

## BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001

Status: `expired`; scope consumed by `G1SRER-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Ок , цель , план , делай" after
`G1RD-G1-VIRAL-001` recommended a rollup that carries the narrow Gate 1 source
reconstruction evidence decision forward without broadening it.

Exact action:

- Roll up exact `G1RD-G1-VIRAL-001` report, record, Markdown, and summary
  hashes only.
- Carry the accepted seven-record source reconstruction evidence slice forward
  as higher-level Gate 1 status input.
- Preserve `accepted_pages_as_complete=false`, `page_complete_acceptance=false`,
  and `whole_gate_1_acceptance=false`.
- Preserve the boundary that this rollup does not authorize translation,
  proofreading, renderer/profile acceptance, implementation, push, OCR, PDF
  parsing, rendering, or raw OCR mutation.

Allowed outputs:

- `scripts/rollup_gate_1_source_reconstruction_evidence.py`
- `tests/test_gate_1_source_recon_evidence_rollup.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_recon_evidence_rollup_G1_VIRAL_001/gate_1_source_recon_evidence_rollup_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_recon_evidence_rollup_G1_VIRAL_001/gate_1_source_recon_evidence_rollup_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_recon_evidence_rollup_G1_VIRAL_001/gate_1_source_recon_evidence_rollup.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_recon_evidence_rollup_G1_VIRAL_001/gate_1_source_recon_evidence_rollup_summary.md`

Output status:

- Rollup id: `G1SRER-G1-VIRAL-001`
- Status: `narrow_source_reconstruction_evidence_rollup_ready`
- Report SHA-256:
  `CDF75D022DC29D0594CA441F02EDA2DC50CE9C0C4BA81F5C51523745318A4AEB`
- Manifest SHA-256:
  `C5211A4F6607B6DEAE73EFA599C8F25F269833AAAACED9838FF2746AA4A1A265`
- Rollup JSON SHA-256:
  `3674E136BAA0F1D62DC240FAD1C1E34FD919D56A4A7251D580106D9BEFB83380`
- Summary SHA-256:
  `5740BE4D8B7AAA7D8D05DFDFD3EBA4A67EF26538B9C95E653A3D8B09C498BC8B`

Limits:

- Do not accept pages as complete.
- Do not accept whole Gate 1.
- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance,
  implementation, or push.
- Do not use this rollup without explicitly labeling the scope as
  seven reviewed records only.

Invalidation:

This evidence rollup stales if `G1RD-G1-VIRAL-001`, direct G1RP lineage,
accepted scope labels, script/test revision, reviewer/authority, or predecessor
remediation/supersession changes.

## BA-G1-VIRAL-GATE-1-STATUS-PACKET-001

Status: `expired`; scope consumed by `G1SP-G1-VIRAL-001`

Created: 2026-07-18

Authority: user request from Bogdan: "Тогда собери план и пошли делать" after
`G1SRER-G1-VIRAL-001` recommended a higher-level Gate 1 status packet.

Exact action:

- Build a status packet from exact `G1SRER-G1-VIRAL-001` report, manifest,
  payload, and summary hashes only.
- Summarize the current Gate 1 state as one narrow accepted/rolled-up source
  reconstruction slice plus pending work.
- Preserve `accepted_pages_as_complete=false`, `page_complete_acceptance=false`,
  and `whole_gate_1_acceptance=false`.
- Preserve the boundary that this status packet does not create new Gate 1
  advancement and does not authorize translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, PDF parsing,
  rendering, or raw OCR mutation.

Allowed outputs:

- `scripts/build_gate_1_status_packet.py`
- `tests/test_gate_1_status_packet.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_001/gate_1_status_packet_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_001/gate_1_status_packet_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_001/gate_1_status_packet.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_001/gate_1_status_packet_summary.md`

Output status:

- Status packet id: `G1SP-G1-VIRAL-001`
- Status: `gate_1_status_packet_ready_narrow_slice_only`
- Report SHA-256:
  `4F0AD3C7553863636B6FD15E329815EE26E62329D668C9FA8AC756CE04B24644`
- Manifest SHA-256:
  `DA8DDB2DA56EECE600A36303383F7ACB83B5E3677888F7D980FD9183B6B3E639`
- Status packet JSON SHA-256:
  `4C7EFAFDC60DF52A09F9358AB7F334FC5354B51E95A130F5BC86D42DC0C4BE68`
- Summary SHA-256:
  `FEFD8CAF624F392E1F8F0E6A4A96B5D120FA76A5CC4B7BA7D675F3833077B562`

Limits:

- Do not accept pages as complete.
- Do not accept whole Gate 1.
- Do not create new Gate 1 advancement.
- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance,
  implementation, or push.
- Do not treat the packet summary as source-profile acceptance.

Invalidation:

This status packet stales if `G1SRER-G1-VIRAL-001`, accepted scope labels,
script/test revision, reviewer/authority, or predecessor remediation/supersession
changes.

## BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001

Status: `expired`; scope consumed by `SRNS-G1-VIRAL-002`

Created: 2026-07-18

Authority: user request from Bogdan: "Ок иди" after `G1SP-G1-VIRAL-001`
recommended a separately authorized next source reconstruction slice.

Exact action:

- Build one next source reconstruction visual review packet for Viral page 002
  only.
- Consume exact `G1SP-G1-VIRAL-001` status packet hashes and
  `PRM-G1-VIRAL-001` provisional region hints.
- Create crop references from already-rendered `page_002.png` for exactly two
  provisional page-002 regions:
  `PRM-G1-VIRAL-001-P002-R01` and `PRM-G1-VIRAL-001-P002-R02`.
- Preserve the boundary that this packet creates no candidate text, source
  acceptance, QA acceptance, fixture admission, Gate 1 advancement, OCR, PDF
  parsing, rendering, translation, proofreading, implementation, or push.

Allowed outputs:

- `scripts/build_source_reconstruction_next_slice.py`
- `tests/test_source_reconstruction_next_slice.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_002/source_reconstruction_next_slice_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_002/source_reconstruction_next_slice_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_002/human_review_packet.md`
- Two PNG crop references under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_002/region_refs/`

Output status:

- Package id: `SRNS-G1-VIRAL-002`
- Status: `next_source_reconstruction_slice_ready_for_bogdan_review_not_accepted`
- Generator script SHA-256:
  `3FE89535AD5F2A43AFA827DF4C5281CFA9DD8901AEABE8646AF6883132595CC4`
- Generator test SHA-256:
  `5C20FB61C33368A3C3EFE758A7B48B513397029B117DD2DE345D3B40FD1B16F8`
- Report SHA-256:
  `1A9A693883277635B02E02F143284280C1FBA1F928FF950843586B8A1C5EC224`
- Manifest SHA-256:
  `B4D8E6AA3D08DFD78D16F72FD3774B57051F4AABCE32062C3B36E924466C6DCD`
- Human review packet SHA-256:
  `01ADBA8C47E696104D974905C60001144E3DD662B11CA25DD841E6ED492F8509`
- Crop `1_SRNS-G1-VIRAL-002-R01__PRM-G1-VIRAL-001-P002-R01.png` SHA-256:
  `3E8CF28342ED6FA0BA497A2DB6B81AB376EF6B1CA68A326C442D7724A68738D7`
- Crop `2_SRNS-G1-VIRAL-002-R02__PRM-G1-VIRAL-001-P002-R02.png` SHA-256:
  `081F8BD3676AFF4A8C34BFCA0CD38245F75D0202933EF8D67269B0F6F240FD6D`

Limits:

- Do not create candidate text.
- Do not accept source text.
- Do not accept page 002 as complete.
- Do not accept whole Gate 1.
- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create QA acceptance, fixture admission, translation, proofreading,
  renderer/profile acceptance, implementation, or push.

Invalidation:

This next-slice package stales if `G1SP-G1-VIRAL-001`, `PRM-G1-VIRAL-001`,
`page_002.png`, selected region IDs/boxes, script/test revision,
reviewer/authority, or predecessor remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-001

Status: `expired`; scope consumed by `SRAD-G1-VIRAL-002`

Created: 2026-07-18

Authority: Bogdan review route from Telegram messages `351` and `356`:
both page-002 crops contain text, but the text is too long for manual
transcription and the first corrected crop over-included the lower block.

Exact action:

- Record Bogdan's route decision as blocked for assisted transcription, not
  source acceptance.
- Prepare corrected split crops from already-rendered `page_002.png`:
  one credits/play-testers crop and one lower special-thanks/legal crop.
- Prepare assisted draft text for Bogdan verification only.
- Consume exact `SRNS-G1-VIRAL-002` report and manifest hashes.
- Preserve the boundary that this layer creates no source acceptance, QA
  acceptance, fixture admission, Gate 1 advancement, page-complete acceptance,
  whole-Gate acceptance, OCR execution, PDF parsing/rendering, raw OCR mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Allowed outputs:

- `scripts/prepare_source_reconstruction_p002_assisted_draft.py`
- `tests/test_source_reconstruction_p002_assisted_draft.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_assisted_draft_G1_VIRAL_001/source_reconstruction_p002_assisted_draft_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_assisted_draft_G1_VIRAL_001/source_reconstruction_p002_assisted_draft_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_assisted_draft_G1_VIRAL_001/assisted_text_draft_for_bogdan.md`
- Two corrected PNG crop references under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_assisted_draft_G1_VIRAL_001/corrected_region_refs/`

Output status:

- Draft id: `SRAD-G1-VIRAL-002`
- Status: `assisted_text_draft_ready_for_bogdan_verification_not_accepted`
- Generator script SHA-256:
  `23925C6A95648CCB002623E61A5EE109A4216F3C9A76BFF866DE896417E5CE4B`
- Generator test SHA-256:
  `9A6C01FD0D6F345E6BF829120168AE367DD9A2346CB6D331AD3E45269CCFF2D0`
- Report SHA-256:
  `296763B5942B937B66822E4988C30FF5B96FBFBFF08952987FA5E8D22CE07F05`
- Manifest SHA-256:
  `D6E50079093DEDA2F178D744E19DA29650CF3B2667B1F5418D4CB02F018E4280`
- Assisted draft Markdown SHA-256:
  `256568A3889A1BA9417662F8E897D818416A7FCBA664E0A896CB7F931F2C769B`
- Corrected crop `1_SRAD-G1-VIRAL-002-R01__SRAD-G1-VIRAL-002-R01-C01.png`
  SHA-256:
  `D281969D790D4BF7661DDF841924FA6A0B9F8965088580A0FA89B64DA9599E6D`
- Corrected crop `2_SRAD-G1-VIRAL-002-R02__SRAD-G1-VIRAL-002-R02-C01.png`
  SHA-256:
  `D167F253964076DA67D7A6D625BB236875CA05E634710C10F1FD816C46B1BE4B`

Limits:

- Do not accept assisted draft text as source text.
- Do not accept page 002 as complete.
- Do not accept whole Gate 1.
- Do not create QA acceptance or fixture admission.
- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance,
  implementation, or push.

Invalidation:

This assisted draft stales if `SRNS-G1-VIRAL-002`, `page_002.png`, corrected
crop boxes, draft text, script/test revision, reviewer/authority, or predecessor
remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-HUMAN-VERIFY-001

Status: `expired`; scope consumed by `SRADV-G1-VIRAL-002`

Created: 2026-07-18

Authority: Bogdan Telegram message `377`: `1 ок; 2 ок; Заголовки игнорирую.
По тексту все ок.`

Exact action:

- Record Bogdan's verification that the two `SRAD-G1-VIRAL-002` assisted draft
  text records match their corrected crops.
- Preserve heading/title handling as ignored for this decision.
- Consume exact `SRAD-G1-VIRAL-002` report, manifest, and assisted draft
  Markdown hashes.
- Preserve the boundary that this layer creates no source acceptance, QA
  acceptance, fixture admission, Gate 1 advancement, page-complete acceptance,
  whole-Gate acceptance, OCR execution, PDF parsing/rendering, raw OCR mutation,
  translation, proofreading, renderer/profile acceptance, implementation, or
  push.

Allowed outputs:

- `scripts/verify_source_reconstruction_p002_assisted_draft.py`
- `tests/test_source_reconstruction_p002_assisted_draft_verify.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001/source_reconstruction_p002_assisted_draft_verify_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001/source_reconstruction_p002_assisted_draft_verify_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001/assisted_draft_human_verification_summary.md`

Output status:

- Verification id: `SRADV-G1-VIRAL-002`
- Status: `assisted_draft_human_verified_not_source_accepted`
- Generator script SHA-256:
  `8C54503E16C223119B9829925ABFCD289C7334DEC2375909B9578E9802106C05`
- Generator test SHA-256:
  `0CA4EE3198E74C0DFA3E900C6E533EBD602AF738D1F7627B7CDE332645A2350E`
- Report SHA-256:
  `BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52`
- Manifest SHA-256:
  `B6E3D871FCA061D1672CB5E73A1BFF6C73AAE7D0C7F8B2A7044BD451FAC9159A`
- Summary SHA-256:
  `225DC38D81F9BD4133D05823ACDDBED538E5CBA790DEF1A33A4E4AFCCBF7E13D`

Required predecessor hashes:

- SRAD report SHA-256:
  `296763B5942B937B66822E4988C30FF5B96FBFBFF08952987FA5E8D22CE07F05`
- SRAD manifest SHA-256:
  `D6E50079093DEDA2F178D744E19DA29650CF3B2667B1F5418D4CB02F018E4280`
- SRAD assisted draft Markdown SHA-256:
  `256568A3889A1BA9417662F8E897D818416A7FCBA664E0A896CB7F931F2C769B`

Limits:

- Do not accept the verified draft as source text.
- Do not accept page 002 as complete.
- Do not accept whole Gate 1.
- Do not create QA acceptance or fixture admission.
- Do not run OCR.
- Do not open, parse, render, rehash, recount, or inspect the PDF.
- Do not inspect or copy PDF text-layer content.
- Do not edit raw OCR outputs.
- Do not create translation, proofreading, renderer/profile acceptance,
  implementation, or push.

Invalidation:

This verification stales if `SRAD-G1-VIRAL-002`, verified text, corrected crop
hashes, script/test revision, reviewer/authority, or predecessor
remediation/supersession changes.

## BA-G1-VIRAL-P002-QA-STRUCTURE-SOURCE-AND-NEXT-REVIEW-001

Status: `expired`; scope consumed by `P002C-G1-VIRAL-002`

Created: 2026-07-19

Authority: Bogdan Telegram message `419`: run the full page-002 plan 1-6 with
Sol/Terra and tests, commit it, and prepare the next review block with text,
structure, semantics, and crop references without stopping for intermediate
approval.

Exact action:

- Consume exact `SRADV-G1-VIRAL-002` report, manifest, and summary hashes.
- Record QA over the verified page-002 assisted draft as `SRADQ-G1-VIRAL-002`.
- Record structure/semantics for the two page-002 records as
  `SRSS-G1-VIRAL-002`, including semantic roles, `h1`-`h6`/`none` heading
  fields, and bold/italic/underline/centered/font-scale presentation fields.
- Record structure QA as `SRSSQ-G1-VIRAL-002`.
- Record narrow source acceptance for exactly two page-002 records as
  `SRSA-G1-VIRAL-002`, with page-002-complete=false and whole-Gate=false.
- Roll the second narrow source reconstruction slice into status as
  `G1SRER-G1-VIRAL-002`, bringing accepted source reconstruction records to 9.
- Prepare the next review packet `SRCR-G1-VIRAL-003` for page 003 with draft
  OCR text, draft structure/semantics, and two crop references for Bogdan
  review.

Allowed outputs:

- `scripts/build_p002_completion_and_next_review.py`
- `tests/test_p002_completion_and_next_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001/p002_completion_and_next_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001/p002_completion_and_next_review_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001/next_review_packet_for_bogdan.md`
- Two page-003 PNG crop references under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001/next_review_refs/`

Output status:

- Package id: `P002C-G1-VIRAL-002`
- Status: `p002_accepted_as_two_record_slice_next_review_packet_ready`
- Generator script SHA-256:
  `9806638AF111949DEFC7334F7700A0DDA94262BACE73A670D990FD06B492CF07`
- Generator test SHA-256:
  `CA0A942F3047188D64CC52DDF10AB94F4A4CAF26BA218450981F8A3AC99EE9D7`
- Report SHA-256:
  `A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F`
- Manifest SHA-256:
  `8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6`
- Next review packet SHA-256:
  `81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF`
- Next review crop 1 SHA-256:
  `CC942FC60C379EF8DC32083FBDE5F08CF222A07A943A6392B67A090DBDEC9F7E`
- Next review crop 2 SHA-256:
  `ABDE2B383C0D8470F9923703A70560339ACAA1906B68867800A9B619EB3BB845`

Required predecessor hashes:

- SRADV report SHA-256:
  `BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52`
- SRADV manifest SHA-256:
  `B6E3D871FCA061D1672CB5E73A1BFF6C73AAE7D0C7F8B2A7044BD451FAC9159A`
- SRADV summary SHA-256:
  `225DC38D81F9BD4133D05823ACDDBED538E5CBA790DEF1A33A4E4AFCCBF7E13D`
- Page 003 PNG SHA-256:
  `B6B5A48D498FDEFB050B67E7155E85502010799D05CC10317C9E179CEB97A6BF`

Limits:

- Do not accept page 002 as complete.
- Do not accept page 003 source text or page 003 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, implement, push,
  parse/render the PDF, mutate raw OCR outputs, or inspect PDF text-layer
  content.
- Bogdan message `430` reported that the initial page-003 crop cut text. The
  page-003 crop boxes and text layer must be treated as crop-remediated review
  material, and QA/test coverage must guard against tight text-edge crops.
- The page-003 text remains draft and not source-accepted until Bogdan review
  and a later separate bounded decision.
- Bogdan message `437` later verifies the remediated page-003 draft packet as
  `1 ок`, `2 ок`; this verification is `SRCRV-G1-VIRAL-003` and still does not
  create source acceptance, QA acceptance, fixture admission, page-complete
  acceptance, whole-Gate acceptance, renderer/profile acceptance, implementation,
  or push.

Invalidation:

This package stales if `SRADV-G1-VIRAL-002`, page-002 verified text,
structure decisions from Bogdan messages `377`/`414`, page-003 image, selected
page-003 region boxes, generated draft text, script/test revision,
reviewer/authority, or predecessor remediation/supersession changes.

## BA-G1-VIRAL-P003-QA-SOURCE-ACCEPTANCE-001

Status: `expired`; scope consumed by `P003A-G1-VIRAL-003`

Created: 2026-07-19

Authority: Bogdan Telegram message `441`: "Коммит, затем qa acceptance, затем
пофиксить кроп".

Exact action:

- Consume exact `P002C-G1-VIRAL-002` report, manifest, and remediated next
  review packet hashes.
- Record QA over Bogdan-verified remediated page-003 review records as
  `SRCRQ-G1-VIRAL-003`.
- Record crop guardrail `SRCG-G1-VIRAL-003` by consuming predecessor global
  crop layout evidence `SRCG-GLOBAL-CROP-BOX-LAYOUT-001`: approved boxes,
  crop overlap, and too-small gutters are blockers.
- Record narrow source acceptance for exactly two page-003 records as
  `SRSA-G1-VIRAL-003`.
- Roll up the third narrow source reconstruction slice as `G1SRER-G1-VIRAL-003`,
  increasing accepted source reconstruction records from 9 to 11.

Allowed outputs:

- `scripts/accept_p003_verified_review.py`
- `tests/test_p003_verified_review_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001/p003_verified_review_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001/p003_verified_review_acceptance_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001/p003_verified_review_acceptance_summary.md`

Output status:

- Package id: `P003A-G1-VIRAL-003`
- Status: `p003_two_record_source_acceptance_ready`
- Generator script SHA-256:
  `076687DC53A042FC116BAB28B90A620BF6025C001097693EA1197311B3185B23`
- Generator test SHA-256:
  `0E84AD3505B56AEAF23FD188D993513AF06FE9D83A79D4C209DBE6888A089668`
- Report SHA-256:
  `9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B`
- Manifest SHA-256:
  `F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87`
- Summary SHA-256:
  `860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2`

Required predecessor hashes:

- P002C report SHA-256:
  `A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F`
- P002C manifest SHA-256:
  `8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6`
- P002C next review packet SHA-256:
  `81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF`

Limits:

- Do not accept page 003 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, implement,
  push, parse/render the PDF, mutate raw OCR outputs, or inspect PDF text-layer
  content.

Invalidation:

This acceptance stales if `P002C-G1-VIRAL-002`, `SRCRV-G1-VIRAL-003`, crop
boxes, draft text, script/test revision, reviewer/authority, or predecessor
remediation/supersession changes.

## BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004

Status: `expired`; scope consumed by `SRCR-G1-VIRAL-004`

Created: 2026-07-19

Authority: Bogdan Telegram message `514`: "Делай 1-6 включительно. Коммит
разрешаю".

Exact action:

- Consume exact `P003A-G1-VIRAL-003` report, manifest, and summary hashes.
- Consume `PRM-G1-VIRAL-001` page-004 region hints and the already-rendered
  `page_004.png` identity only.
- Prepare page-004 review packet `SRCR-G1-VIRAL-004` for Bogdan review with
  draft text, structure/semantics, and padded crop references.
- Treat `PRM-G1-VIRAL-001-P004-R01` as context only because it contains the
  title/body regions and would overlap peer crop records.
- Validate peer crop records through `SRCG-GLOBAL-CROP-BOX-LAYOUT-001`; approved
  boxes, crop overlap, and too-small gutters are blockers.

Allowed outputs:

- `scripts/build_source_reconstruction_next_slice_004.py`
- `tests/test_source_reconstruction_next_slice_004.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_004/source_reconstruction_next_slice_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_004/source_reconstruction_next_slice_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_004/human_review_packet.md`
- Two page-004 PNG crop references under
  `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_G1_VIRAL_004/region_refs/`

Output status:

- Package id: `SRCR-G1-VIRAL-004`
- Status: `page_004_review_packet_ready_for_bogdan_review_not_accepted`
- Generator script SHA-256:
  `B9A9A38422BDA55F9C41909AD1A08E93E95FDF0B8A93EF45FA2809E1056F7DFC`
- Generator test SHA-256:
  `F426CCE08AE1D827DB4EC5C14EA8FF563C5A02FE87BBECD2A800F05BAF1C86F1`
- Report SHA-256:
  `C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A`
- Manifest SHA-256:
  `30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4`
- Human review packet SHA-256:
  `1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446`
- Crop 1 SHA-256:
  `ADD3C344100356249BF38C85A7C89D2A2DB9FF23B48141509A47F86C6A32C219`
- Crop 2 SHA-256:
  `EFB82E2F8ECE14585CFD83F71C301B7024C437680703B18765A259A7E3B234C8`

Required predecessor hashes:

- P003A report SHA-256:
  `9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B`
- P003A manifest SHA-256:
  `F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87`
- P003A summary SHA-256:
  `860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2`
- PRM report SHA-256:
  `A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C`
- Page 004 PNG SHA-256:
  `45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88`

Limits:

- Do not accept page 004 source text.
- Do not accept page 004 as complete.
- Do not accept page 002 or page 003 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, implement,
  push, parse/render the PDF, mutate raw OCR outputs, inspect PDF text-layer
  content, or run OCR.

Invalidation:

This package stales if `P003A-G1-VIRAL-003`, `G1SRER-G1-VIRAL-003`, page-004
region hints, page-004 image, selected crop boxes, draft text, script/test
revision, reviewer/authority, or global crop policy changes.

## BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004-HUMAN-VERIFY-001

Status: `expired`; scope consumed by `SRCRV-G1-VIRAL-004`

Created: 2026-07-19

Authority: Bogdan Telegram message `523`: "1 ok / 2 ok" for the two
`SRCR-G1-VIRAL-004` review records.

Exact action:

- Consume exact `SRCR-G1-VIRAL-004` report, manifest, and human review packet
  hashes.
- Record Bogdan's numbered verification for exactly the two draft page-004
  review records shown in the packet.
- Preserve `SRCR-G1-VIRAL-004` as draft review material only.
- Do not perform QA acceptance, source acceptance, page-complete acceptance,
  fixture admission, Gate 1 advancement, translation, proofreading,
  renderer/profile acceptance, implementation, push, PDF parsing/rendering,
  OCR, or raw OCR mutation.

Allowed outputs:

- `scripts/verify_source_reconstruction_next_slice_004.py`
- `tests/test_source_reconstruction_next_slice_004_verify.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_004_verify_G1_VIRAL_001/source_reconstruction_next_slice_004_verify_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_004_verify_G1_VIRAL_001/source_reconstruction_next_slice_004_verify_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_next_slice_004_verify_G1_VIRAL_001/page_004_human_verification_summary.md`

Output status:

- Verification id: `SRCRV-G1-VIRAL-004`
- Status: `page_004_review_packet_human_verified_not_source_accepted`
- Verification script SHA-256:
  `4CF92D208279C47FE43CC0AF5E603E9D6FDECCBF5C01CCD265A1053F55AA4D2A`
- Verification test SHA-256:
  `9061B611BF815646B1244129BFFC85B5D7A08FC1C29A88F57B7200BE558BF05A`
- Verification report SHA-256:
  `95041F808A1C2F44A417245BF3E25318C9BDE36183CCE7C4E372DF9363812FBA`
- Verification manifest SHA-256:
  `21B3CE0135D4D8CF09C394C192D7976766DA9DA1E55DE5F9B3FE240380CC0AB0`
- Verification summary SHA-256:
  `F342D7DA0CBB7245812B8B3291F2C5585D880DA67D6C24DCAFEC4FF8B86D9011`

Required predecessor hashes:

- `SRCR-G1-VIRAL-004` report SHA-256:
  `C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A`
- `SRCR-G1-VIRAL-004` manifest SHA-256:
  `30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4`
- `SRCR-G1-VIRAL-004` human review packet SHA-256:
  `1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446`

Verified records:

- `1`: `SRCR-G1-VIRAL-004-R01` / `PRM-G1-VIRAL-001-P004-R02` - `ok`.
- `2`: `SRCR-G1-VIRAL-004-R02` / `PRM-G1-VIRAL-001-P004-R03` - `ok`.

Limits:

- Do not accept page 004 source text.
- Do not accept page 004 as complete.
- Do not accept page 002 or page 003 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, implement,
  push, parse/render the PDF, mutate raw OCR outputs, inspect PDF text-layer
  content, or run OCR.

Invalidation:

This verification stales if `SRCR-G1-VIRAL-004`, its crop references, draft
text, structure/semantics, script/test revision, reviewer/authority, or global
crop policy changes.

## BA-G1-VIRAL-P004-QA-SOURCE-ACCEPTANCE-001

Status: `expired`; C1 scope consumed by `P004A-G1-VIRAL-004`

Created: 2026-07-19

Authority: Bogdan Telegram message `538`: "Ok, go with C1, commit allowed;
call me at the end when I need to assess the result. Until then, use double
OK from Sol and Terra."

Exact action:

- Consume exact `SRCR-G1-VIRAL-004` review packet hashes and exact
  `SRCRV-G1-VIRAL-004` human-verification hashes.
- Record QA/source acceptance for exactly the two human-verified page-004
  review records:
  - `SRCR-G1-VIRAL-004-R01` / `SRCRV-G1-VIRAL-004-R01` /
    `PRM-G1-VIRAL-001-P004-R02`
  - `SRCR-G1-VIRAL-004-R02` / `SRCRV-G1-VIRAL-004-R02` /
    `PRM-G1-VIRAL-001-P004-R03`
- Consume predecessor crop-layout guardrail evidence from
  `SRCG-GLOBAL-CROP-BOX-LAYOUT-001`.
- Roll accepted source reconstruction records from 11 to 13.
- Preserve `PRM-G1-VIRAL-001-P004-R01` as context-only, not a peer accepted
  crop record.
- Do not perform page-complete acceptance, fixture admission, Gate 1
  advancement, translation, proofreading, renderer/profile acceptance,
  implementation, push, PDF parsing/rendering, OCR, or raw OCR mutation.

Allowed outputs:

- `scripts/accept_p004_verified_review.py`
- `tests/test_p004_verified_review_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001/p004_verified_review_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001/p004_verified_review_acceptance_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001/p004_verified_review_acceptance_summary.md`

Required predecessor hashes:

- `SRCR-G1-VIRAL-004` report SHA-256:
  `C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A`
- `SRCR-G1-VIRAL-004` manifest SHA-256:
  `30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4`
- `SRCR-G1-VIRAL-004` human review packet SHA-256:
  `1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446`
- `SRCRV-G1-VIRAL-004` report SHA-256:
  `95041F808A1C2F44A417245BF3E25318C9BDE36183CCE7C4E372DF9363812FBA`
- `SRCRV-G1-VIRAL-004` manifest SHA-256:
  `21B3CE0135D4D8CF09C394C192D7976766DA9DA1E55DE5F9B3FE240380CC0AB0`
- `SRCRV-G1-VIRAL-004` summary SHA-256:
  `F342D7DA0CBB7245812B8B3291F2C5585D880DA67D6C24DCAFEC4FF8B86D9011`

Output status:

- Package id: `P004A-G1-VIRAL-004`
- Status: `p004_two_record_source_acceptance_ready`
- QA id: `SRCRQ-G1-VIRAL-004`
- Crop guardrail id: `SRCG-G1-VIRAL-004`
- Source acceptance id: `SRSA-G1-VIRAL-004`
- Rollup id: `G1SRER-G1-VIRAL-004`
- Acceptance script SHA-256:
  `1F0862764FCA20F944B9448AA569CB1969A1B40C65EAB400348B4C925694955C`
- Acceptance test SHA-256:
  `38EC001BF5B8C3B09B2C3088FC9CE3A036DB6D79DF0D3648D5FDB1F75DD8A46F`
- Acceptance report SHA-256:
  `0CCB4AA33481BDB0B95B02D32A0E49FB1A20FD9A957DB7DAE1ECB0B00307622E`
- Acceptance manifest SHA-256:
  `75C0C0BD96FF77E64D2F7C827D7D21B12F7EF15964E8EC9734F9428CCC064C06`
- Acceptance summary SHA-256:
  `BF664162A899765C3B614F87002792D213D70DB82A7ED4142686AA439D50C64C`

Limits:

- Do not accept page 004 as complete.
- Do not accept page 002 or page 003 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, implement,
  push, parse/render the PDF, mutate raw OCR outputs, inspect PDF text-layer
  content, or run OCR.

Invalidation:

This acceptance stales if `SRCR-G1-VIRAL-004`, `SRCRV-G1-VIRAL-004`, their crop
references, draft/verified text, structure/semantics, script/test revision,
reviewer/authority, or global crop policy changes.

## BA-G1-VIRAL-PAGE-COMPLETENESS-TRIAGE-001

Status: `expired`; scope consumed by `PGCT-G1-VIRAL-001`

Created: 2026-07-19

Authority: Bogdan Telegram message `579`: "Do 1-6, commit allowed."

Exact action:

- Consume current source-reconstruction state through `P004A-G1-VIRAL-004` /
  `G1SRER-G1-VIRAL-004`, plus existing selected-page, render, page-map, and
  region-map status artifacts as read-only predecessors.
- Build a decision packet that tells Bogdan, in human-facing language, which
  selected pages 1-20 are incomplete, unstarted, blocked, or ready for a later
  bounded page-complete review packet.
- Use Sol analytical review and Terra critical review before presenting the
  packet to Bogdan.
- Keep hashes, test output, internal QA keys, stale scans, and technical
  checklist details as orchestrator-only verification.
- Do not accept any page as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, implement,
  push, parse/render the PDF, mutate raw OCR outputs, inspect PDF text-layer
  content, or run OCR.

Allowed outputs:

- `scripts/build_page_completeness_triage.py`
- `tests/test_page_completeness_triage.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_completeness_triage_G1_VIRAL_001/page_completeness_triage_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_completeness_triage_G1_VIRAL_001/page_completeness_triage_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_completeness_triage_G1_VIRAL_001/page_completeness_triage_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_completeness_triage_G1_VIRAL_001/page_completeness_triage_manifest.md`

Output status:

- Package id: `PGCT-G1-VIRAL-001`
- Status: `page_completeness_triage_ready_for_bogdan_decision`
- Triage script SHA-256:
  `3A835EB20AFA835C4D9FF1BD266A5F2B8DB438779506F88736303F39458A0DB0`
- Triage test SHA-256:
  `1F809C337DFFD04CE997EC80A3B49EAEECD8EB3F42254E0D0CA68E0E381FD257`
- Triage report SHA-256:
  `EFDEBCC6ABBE916086887572D400DA9AAF41257F910D55AAF4D337BE386F550F`
- Triage packet SHA-256:
  `7BF4017A17D40BFAF8A6FE478E41234E4B8BE0889C6067B3BE7F3C890E85BB9A`
- Triage summary SHA-256:
  `927116C1F317B3B68D408CBF74D4623D640D17F1AA2CFF9B51A99FF78FAF404E`
- Triage manifest SHA-256:
  `A4EFE5854C979517D8DC42AFA13F5522F2D2621B6252F6B1E4755D74A6A7A458`

Limits:

- Page-complete review may be recommended as a next packet, but not performed.
- Page 004 full tilted inset context-only treatment must be shown to Bogdan as
  a decision point, not silently treated as page-complete evidence.
- The packet may recommend ordering for later page-complete reviews, but each
  page-complete action needs separate bounded authorization.
- Pages without accepted source-reconstruction evidence must remain parked or
  recommended for later bounded source-reconstruction slices only.

Invalidation:

This triage stales if `P004A-G1-VIRAL-004`, `G1SRER-G1-VIRAL-004`,
`SPM-G1-VIRAL-001`, render/page-map/region-map status, page-complete policy,
crop policy, acceptance vocabulary, roadmap/status state, reviewer/authority,
script/test revision, or Sourcefold orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-MAP-READINESS-PIPELINE-PILOT-002-001

Status: `expired`; scope consumed by `PMRP-G1-VIRAL-P002-001`

Created: 2026-07-20

Authority: Bogdan Telegram message `644`: "Прогони страницу 002 через риднесс
пайплайн. Как обсуждали ранее"

Exact action:

- Implement and run a reusable `page_map` readiness builder with a first
  page-specific profile for page 002.
- Consume current page-002 predecessors as read-only evidence:
  `PRM-G1-VIRAL-001`, `SRAD-G1-VIRAL-002`, `SRADV-G1-VIRAL-002`, and
  `P002C-G1-VIRAL-002`.
- Produce a readiness packet that inventories page-002 blocks, advisory
  coverage, reading order, anchors, structure/semantic checks, protected-token
  checks, and text-fidelity metrics from existing artifacts only.
- Keep page 002 as the pilot/proving profile for a reusable pipeline, not a
  one-off page-specific script.
- Keep readiness separate from page-complete acceptance.

Allowed outputs:

- `scripts/build_page_map_readiness.py`
- `tests/test_page_map_readiness.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p002_G1_VIRAL_001/page_map_readiness_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p002_G1_VIRAL_001/page_map_readiness_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p002_G1_VIRAL_001/page_map_readiness_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p002_G1_VIRAL_001/page_map_readiness_manifest.md`
- Status/roadmap/plan documentation sync that records the readiness result.

Output status:

- Package id: `PMRP-G1-VIRAL-P002-001`
- Status: `ready_for_page_complete_review_packet`
- Readiness script SHA-256:
  `9E2B79D685F5EAAD7D0C0AE424BF7557F71992DC19CDB745B6972BECE71BD09D`
- Readiness test SHA-256:
  `5411C8DA86CD93D9B7599FE716EA380876381396B29735210FB55F9B47E3AD62`
- Readiness report SHA-256:
  `3F957442194211F6F0EC39775ED292DEF126222E98EEFB5BFFD1530D8EA702D6`
- Readiness packet SHA-256:
  `5DAAB049DC28C9C4633490348991DF822FF8E049460AC0978EBF8163D75C1734`
- Readiness summary SHA-256:
  `45104BC75F38DCA37612B308186EC8C877FE33369D564510941F03156AC0A52A`
- Readiness manifest SHA-256:
  `5AB662AF36355A75F73758EF4B73BF13F0315986AF40B2F9234BBE84B489173A`

Limits:

- Do not accept page 002 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, push, parse or
  inspect the PDF or PDF text layer, rerender the PDF, run OCR, mutate raw
  artifacts, mutate source text, or broaden this pilot to another page without
  a separate profile and bounded authorization.

Invalidation:

This readiness packet stales if `PRM-G1-VIRAL-001`, `SRAD-G1-VIRAL-002`,
`SRADV-G1-VIRAL-002`, `P002C-G1-VIRAL-002`, page-002 crop references,
verified/accepted text, structure/semantics, page-map readiness policy,
acceptance vocabulary, reviewer/authority, script/test revision, or
Sourcefold orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-MAP-READINESS-P003-001

Status: `expired`; scope consumed by `PMRP-G1-VIRAL-P003-001`

Created: 2026-07-20

Authority: Bogdan Telegram message `694`: "Прогони page 003 через universal
page_map readiness pipeline as second profile, using existing
P003A-G1-VIRAL-003 evidence; no OCR/render/PDF parsing/raw mutation/fixture
admission/page-complete acceptance/whole Gate acceptance/push."

Exact action:

- Extend the reusable `page_map` readiness builder with a second page-specific
  profile for page 003.
- Consume current page-003 predecessors as read-only evidence:
  `PRM-G1-VIRAL-001`, `P002C-G1-VIRAL-002`, and `P003A-G1-VIRAL-003`.
- Produce a readiness packet that inventories page-003 blocks, advisory
  coverage, reading order, anchors, structure/semantic checks, protected-token
  checks, and text-fidelity metrics from existing accepted source artifacts
  only.
- Use this run to prove the page_map readiness pipeline can run a second
  profile without becoming a page-specific script.
- Keep readiness separate from page-complete acceptance.

Allowed outputs:

- `scripts/build_page_map_readiness.py`
- `tests/test_page_map_readiness.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p003_G1_VIRAL_001/page_map_readiness_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p003_G1_VIRAL_001/page_map_readiness_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p003_G1_VIRAL_001/page_map_readiness_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p003_G1_VIRAL_001/page_map_readiness_manifest.md`
- Status/roadmap/plan documentation sync that records the readiness result.

Output status:

- Package id: `PMRP-G1-VIRAL-P003-001`
- Status: `ready_for_page_complete_review_packet`
- Readiness script SHA-256:
  `FFAFBBF81A37EA78961D1A577DD2624814321B63688FCF2C3F3E8B1C78C47499`
- Readiness test SHA-256:
  `D2F50E25D6860FF3083A374D2E214C36C4867BD47AECD9D1C447786EE5E60E17`
- Readiness report SHA-256:
  `21ED5DA166565BAB537B4CF190B41B55467353DDEC59D58656FFA2F56C827DDF`
- Readiness packet SHA-256:
  `76FDDE5A7A239E729B592D8D6BBDC50AEE55D037A2589CF329A1F83ED989D21F`
- Readiness summary SHA-256:
  `D108411E9778B055277BA625356E5EDC747475A6BDC3494FA1011A04F1164FE2`
- Readiness manifest SHA-256:
  `1A52C156277979A30ED6B81D33D065DE4302360814263D1B1787BAC8D2864EF0`

Limits:

- Do not accept page 003 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, push, parse or
  inspect the PDF or PDF text layer, rerender the PDF, run OCR, mutate raw
  artifacts, mutate source text, or broaden this profile beyond page 003
  without a separate bounded authorization.

Invalidation:

This readiness packet stales if `PRM-G1-VIRAL-001`, `P002C-G1-VIRAL-002`,
`P003A-G1-VIRAL-003`, page-003 crop references, accepted text,
structure/semantics, page-map readiness policy, acceptance vocabulary,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P002-001

Status: `expired`; scope consumed by `P002PCA-G1-VIRAL-001`

Created: 2026-07-20

Authority: Bogdan Telegram message `687`: "Коммит , говорю сразу пейдж 002
комплит ок"

Exact action:

- Consume `PCRP-G1-VIRAL-P002-001` as the explicit page-complete review input
  for page 002.
- Record Bogdan's `page 002 complete ok` decision as page 002 complete
  acceptance.
- Keep the acceptance limited to page 002 only.
- Keep the accepted source text, source records, readiness packet, and review
  packet immutable.

Allowed outputs:

- `scripts/accept_page_002_complete.py`
- `tests/test_page_002_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p002_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p002_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p002_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p002_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan documentation sync that records page 002 complete
  acceptance.

Output status:

- Package id: `P002PCA-G1-VIRAL-001`
- Status: `page_002_complete_accepted`
- Page 002 complete acceptance script SHA-256:
  `5A64F57BC3F608B60EAC3175308A9C163F70E2ABD90CAF02256A3AEA79E3E342`
- Page 002 complete acceptance test SHA-256:
  `A33B032F3829C8C7C3F459CE89A45F8F70DDA416611259EFE23FBFE2F4377563`
- Page 002 complete acceptance report SHA-256:
  `B136282C441D1E48DE9CE064356B3B06F6D45A500C1984901D53908335D8547C`
- Page 002 complete acceptance record SHA-256:
  `3FF1AC29BA8CBCDED3AA8757CDD87713B0EC26011B32A528127C54C572E1EDDE`
- Page 002 complete acceptance summary SHA-256:
  `C3BE5845C038BFB090C66AE678E83B0E0B87769CA9EFB4DED421F9AE53BF0CB4`
- Page 002 complete acceptance manifest SHA-256:
  `D02CFFCADB96DE10382C52822DF87932DE3912C332537F5560CC6B7F438DE70A`

Limits:

- Do not accept any page other than page 002 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to
  another page without separate bounded authorization.

Invalidation:

This acceptance stales if `PCRP-G1-VIRAL-P002-001`, `PMRP-G1-VIRAL-P002-001`,
page-complete policy, acceptance vocabulary, reviewer/authority, script/test
revision, roadmap/status state, or Sourcefold orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P002-001

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P002-001`

Created: 2026-07-20

Authority: Bogdan Telegram message `676`: "run separate page-complete review
packet for page 002 using PMRP-G1-VIRAL-P002-001 as readiness input; no
OCR/render/PDF parsing/raw mutation/fixture admission/whole Gate
acceptance/push"

Exact action:

- Consume `PMRP-G1-VIRAL-P002-001` as the readiness input for page 002.
- Produce a separate page-complete review packet that presents whether page
  002 is ready for Bogdan's explicit page-complete decision.
- Preserve advisory readiness coverage as routing evidence only.
- Keep this packet decision-facing: it may prepare the decision, but it must
  not create the page-complete acceptance record by itself.

Allowed outputs:

- `scripts/build_page_complete_review.py`
- `tests/test_page_complete_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p002_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p002_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p002_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p002_G1_VIRAL_001/page_complete_review_manifest.md`
- Status/roadmap/plan documentation sync that records the review packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P002-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Page-complete review script SHA-256:
  `C6CE27B3D90ACB662F14A9655C3DB734351B579BA0DF6C44C36E24418FEFA79E`
- Page-complete review test SHA-256:
  `96F42A5D2ABBB77147F3686C40072C87C10131ADB1574FA40C5531B5D9D209D4`
- Page-complete review report SHA-256:
  `D84968D6E839D2CF07603FDFD4A7D05112B7F8DBE1984E21788F1BA253C23BB9`
- Page-complete review packet SHA-256:
  `C1BE97EB71B950FD423C805457F0CA60367C1BB4759E7C63A0DA9D175293268C`
- Page-complete review summary SHA-256:
  `4B3C67B9BF98B334539E76A3A1A48CF0DC13BE114C445581EE343D204C60A823`
- Page-complete review manifest SHA-256:
  `9323EE68AED33840FD8C9031630749CED4709A7A1499965BD491B22E145E9D5E`

Limits:

- Do not accept page 002 as complete in this packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create source acceptance or mutate accepted source text.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this packet to another
  page without separate bounded authorization.

Invalidation:

This review packet stales if `PMRP-G1-VIRAL-P002-001`, page-002 readiness
policy, page-complete policy, acceptance vocabulary, reviewer/authority,
script/test revision, roadmap/status state, or Sourcefold orchestrator workflow
changes.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P003-001

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P003-001`

Created: 2026-07-20

Authority: Bogdan Telegram message `697`: "Ок, коммит и показывай ревью пакет"
after `PMRP-G1-VIRAL-P003-001` was reported ready and the recommended next
step was a separate page-complete review packet for page 003.

Exact action:

- Consume `PMRP-G1-VIRAL-P003-001` as the readiness input for page 003.
- Produce a separate page-complete review packet that presents whether page
  003 is ready for Bogdan's explicit page-complete decision.
- Preserve advisory readiness coverage as routing evidence only.
- Keep this packet decision-facing: it may prepare the decision, but it must
  not create the page-complete acceptance record by itself.

Allowed outputs:

- `scripts/build_page_complete_review.py`
- `tests/test_page_complete_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/page_complete_review_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/review_assets/page_003.png`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/review_assets/1_SRCR-G1-VIRAL-003-R01.png`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/review_assets/2_SRCR-G1-VIRAL-003-R02.png`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p003_G1_VIRAL_001/review_assets/page_003_ocr_block_text.md`
- Status/roadmap/plan documentation sync that records the review packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P003-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Page-complete review script SHA-256:
  `66F689CE4B8940E7744AF89C35CF50E8157ED7101BEC143018ABE789B4EF2B30`
- Page-complete review test SHA-256:
  `B1213316568C6A014F5184E87309D22E26580827BC2DADE5C5775415AB79A4FC`
- Page-complete review report SHA-256:
  `EE92756BBB1694AA17BE74926151E6A788A90249B98F6998FF626376F08C7DF0`
- Page-complete review packet SHA-256:
  `822C90EB78D8F50951BE90691B52B4090BDF80179AA7F7B4A52A4AACA7AED8AF`
- Page-complete review summary SHA-256:
  `684864D6C7028C9051DEF0F37189D175C4875E914DF6C153540C13CDB68AE9E5`
- Page-complete review manifest SHA-256:
  `A375F50E36ADE140D959365D8C623DDD6EBC184BCBC89AB0BF5FDF438AD8D784`

Limits:

- Do not accept page 003 as complete in this packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create source acceptance or mutate accepted source text.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this packet to another
  page without separate bounded authorization.

Invalidation:

This review packet stales if `PMRP-G1-VIRAL-P003-001`, page-003 readiness
policy, page-complete policy, acceptance vocabulary, reviewer/authority,
script/test revision, roadmap/status state, or Sourcefold orchestrator workflow
changes.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P003-001

Status: `expired`; scope consumed by `P003PCA-G1-VIRAL-001`

Created: 2026-07-20

Authority: Bogdan Telegram message `711`: "Дополни дефолтный ревью пакет
должен включать эти доработки с шотами и окр блок текстом.мд + исходник,
собранные и выложенные в чате. Сам пакет 003 - ок"

Exact action:

- Consume `PCRP-G1-VIRAL-P003-001` as the page-complete review input for
  page 003.
- Record Bogdan's explicit page 003 ok as a narrow page-complete acceptance.
- Accept page 003 only.
- Keep the accepted source text, source records, readiness packet, review
  packet, and review attachments immutable.

Allowed outputs:

- `scripts/accept_page_003_complete.py`
- `tests/test_page_003_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p003_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p003_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p003_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p003_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan documentation sync that records page 003 complete
  acceptance.

Output status:

- Package id: `P003PCA-G1-VIRAL-001`
- Status: `page_003_complete_accepted`
- Page 003 complete acceptance script SHA-256:
  `69B75557D8B198B29E2C4E4C7DB66CAFCFFD5BDFBC02F6B61317838A4EDB264B`
- Page 003 complete acceptance test SHA-256:
  `CA89C5E714C73DF8DFB1779C45706425C79819B58A01A51D4C6557FE3433D808`
- Page 003 complete acceptance report SHA-256:
  `9D74A9B73D657A0669AD0025B40936E1873A9643F1F03F31279B87FCFAFA5F79`
- Page 003 complete acceptance record SHA-256:
  `039E80726ECCAB2F0F1ACFD2794053630C560F21404739A8E02CE71551769842`
- Page 003 complete acceptance summary SHA-256:
  `8EAE084049DC652D733754B9DEEE770D612AACCE7BE7ADAD30DF705CE1E414B8`
- Page 003 complete acceptance manifest SHA-256:
  `7D9878C91167228E73BC67DEA28E692DA661327201A89209CB0C659F8D450835`

Limits:

- Do not accept any page other than page 003 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to
  another page without separate bounded authorization.

Invalidation:

This acceptance stales if `PCRP-G1-VIRAL-P003-001`, `PMRP-G1-VIRAL-P003-001`,
page-complete policy, acceptance vocabulary, reviewer/authority, script/test
revision, roadmap/status state, or Sourcefold orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-004-CONTEXT-DECISION-001

Status: `expired`; scope consumed by `P004CDP-G1-VIRAL-001`

Created: 2026-07-20

Authority: Bogdan Telegram message `721`: "Prepare a separate page 004
context-only decision packet for PRM-G1-VIRAL-001-P004-R01 full tilted inset
using existing P004A-G1-VIRAL-004 evidence; include source page shot, block
shots, OCR/block text md, and chat-ready review assets; no OCR/render/PDF
parsing/raw mutation/fixture admission/page-complete acceptance/whole Gate
acceptance/push."

Exact action:

- Consume existing `P004A-G1-VIRAL-004` evidence.
- Prepare a separate page 004 context-only decision packet for
  `PRM-G1-VIRAL-001-P004-R01` full tilted inset.
- Present the proposed context-only treatment for Bogdan's explicit decision.
- Include source page shot, block shots, OCR/block text markdown, hashes, and
  chat-ready review assets.

Allowed outputs:

- `scripts/build_page_004_context_decision.py`
- `tests/test_page_004_context_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/page_004_context_decision_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/page_004_context_decision_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/page_004_context_decision_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/page_004_context_decision_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/review_assets/page_004.png`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/review_assets/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/review_assets/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_decision_G1_VIRAL_001/review_assets/page_004_ocr_block_text.md`
- Status/roadmap/plan documentation sync that records the decision packet.

Output status:

- Package id: `P004CDP-G1-VIRAL-001`
- Status: `ready_for_bogdan_page_004_context_only_decision`
- Page 004 context decision script SHA-256:
  `8A480B846D675059F528A5983523031147F31D4D75B9E76ECB0E3B05C94EC231`
- Page 004 context decision test SHA-256:
  `756CADB41C1B2B46A9AD7BB120C3B37D123659CEDD6BE1C7C913DF7632767697`
- Page 004 context decision report SHA-256:
  `B790887E0002F132D5CB27B6F2E7E5894183C73924C3181EAAB46374D2AF3C81`
- Page 004 context decision packet SHA-256:
  `A638817C20AA39243A4C4FC2AC61499BF75EFAA86AF6DE2A2361781A9D622EA2`
- Page 004 context decision summary SHA-256:
  `C133C0BCAE7C0322761A2B093D630D47EC67FC41E0768CF4EA5BE3A65073CAA5`
- Page 004 context decision manifest SHA-256:
  `FC55B5368B88B59292226D4E6A64923870ECC6A55526851C456FB43EB65D662F`
- Page 004 context decision OCR/block text review asset SHA-256:
  `7994F6D597C0041052361533BDDBCC63511B784F1BC24D6E7A089588BAAD3DDB`
- Human-facing display normalization: body-only text blocks use `text_body`
  instead of ambiguous `none`; predecessor source review packet is not mutated.

Limits:

- Do not accept page 004 as complete in this packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this decision packet to
  another page without separate bounded authorization.

Invalidation:

This decision packet stales if `P004A-G1-VIRAL-004`, `SRCR-G1-VIRAL-004`,
`SRCRV-G1-VIRAL-004`, page-complete policy, context-only vocabulary,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-004-CONTEXT-ONLY-CONFIRM-001

Status: `expired`; scope consumed by `P004COD-G1-VIRAL-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `758`: "насколько вижу все правильно
кропнулось, весь текст снят. всего два кропа на страницу тоже правильно. ...
второй кроп - принят, `page 004 context-only ok`"

Exact action:

- Consume exact `P004CDP-G1-VIRAL-001`.
- Record Bogdan's explicit decision that `PRM-G1-VIRAL-001-P004-R01` remains
  `context_only_not_peer_crop_record`.
- Preserve the two accepted page 004 peer text crops as the page 004 title/body
  records.
- Record the human-facing label correction that body-only text uses
  `text_body`, not ambiguous `none`, in current review assets.

Allowed outputs:

- `scripts/accept_page_004_context_only.py`
- `tests/test_page_004_context_only_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_only_confirmation_G1_VIRAL_001/page_004_context_only_confirmation_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_only_confirmation_G1_VIRAL_001/page_004_context_only_confirmation_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_only_confirmation_G1_VIRAL_001/page_004_context_only_confirmation_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_004_context_only_confirmation_G1_VIRAL_001/page_004_context_only_confirmation_manifest.md`
- Status/roadmap/plan documentation sync that records the decision.

Output status:

- Package id: `P004COD-G1-VIRAL-001`
- Status: `page_004_context_only_confirmed`
- Page 004 context-only confirmation script SHA-256:
  `1655277A04AF550EB00C104EA0CD96955C6947E8E27715D46F006B0E431ED747`
- Page 004 context-only confirmation test SHA-256:
  `F0A3C886E6E469265F09E89AB0728AA73C6CBC8736B0C53AAF18ACF2F0DDEB14`
- Page 004 context-only confirmation report SHA-256:
  `03EBA061301B182976158EC061178AC1BEA3F4C22697B03ACA511CE805E1B349`
- Page 004 context-only confirmation record SHA-256:
  `F86165B00694CF0C508F9ABD18EA2D2AC6E22B25BDDF03ACFBA46473BA4E5137`
- Page 004 context-only confirmation summary SHA-256:
  `98B01711799B9534974E4B6D3101259640B5A285E79EC25B3243FDE63DA16544`
- Page 004 context-only confirmation manifest SHA-256:
  `A812C7BCB0E82787D48822DE98A757603EACE40833706998487AAF7EA6CFB3A7`
- Page 004 is not accepted as complete.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

Limits:

- Do not accept page 004 as complete in this confirmation.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this confirmation to
  another page without separate bounded authorization.

Invalidation:

This confirmation stales if `P004CDP-G1-VIRAL-001`, `P004A-G1-VIRAL-004`,
`SRCR-G1-VIRAL-004`, `SRCRV-G1-VIRAL-004`, page-complete policy, context-only
vocabulary, body-only display vocabulary, reviewer/authority, script/test
revision, roadmap/status state, or Sourcefold orchestrator workflow changes.

## BA-G1-VIRAL-STRUCTURE-DISPLAY-NORMALIZATION-001

Status: `expired`; scope consumed by `SDN-G1-VIRAL-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `769`: "подготовь" after clarifying that
future and prior human-facing packets should display body-only text as
`text_body` instead of ambiguous `none`.

Exact action:

- Add a shared human-facing display rule for `Draft structure/semantics` lines:
  body/text-only semantic roles with raw `heading_level` `none` display as
  `text_body`.
- Wire the rule into future packet generators.
- Create normalized human-facing copies for prior affected packets without
  mutating raw predecessor evidence files or accepted reports.

Allowed outputs:

- `scripts/display_structure_labels.py`
- `scripts/build_structure_display_migration.py`
- `tests/test_structure_display_migration.py`
- Updates to existing future-facing packet generators and tests.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/structure_display_normalization_G1_VIRAL_001/`
- Status/roadmap/plan documentation sync that records the display-only rule.

Output status:

- Package id: `SDN-G1-VIRAL-001`
- Status: `human_facing_structure_display_normalized`
- Display helper SHA-256:
  `10D581809F408CE39EE5AB64D6157E0189C4D980C38E86A261C6B34A15CD5656`
- Structure display normalization script SHA-256:
  `477504BB169314B9FD54240CD663F68FED3EF50EE907C5CBE9B4155BE9815053`
- Structure display normalization test SHA-256:
  `E350F471625EFA0DEDF2553C302A7E98C899B734BC9C60F0AAD5225B2E27097F`
- Structure display normalization report SHA-256:
  `3BF875B3CE0430434B41C0AD1967143E99BBFD64A7CE200BDD81BBF078EAD470`
- Structure display normalization summary SHA-256:
  `0AF8DEAF3CDCA3AEC024EF5202BFC52F93951D9258740B5EC7829BFD21818220`
- Structure display normalization manifest SHA-256:
  `DD0D27173481387224FB40FBA5AF13C6AAAA483107EA239E1F60F01E2C0550F6`
- Future display-aware generator SHA-256 values:
  - `scripts/build_p002_completion_and_next_review.py`:
    `F67C4B4D06F3A984E864D90E5DFBA4CC4FE9CE60DC50D2FEEAAD8FDBF70B9938`
  - `scripts/build_source_reconstruction_next_slice_004.py`:
    `FBC88E6A89863F77321F25733E1DBC09C0310B74FE6D933AF95BEA4CFB7CB45B`
  - `scripts/build_page_004_context_decision.py`:
    `8A480B846D675059F528A5983523031147F31D4D75B9E76ECB0E3B05C94EC231`
- Original predecessor evidence files are not mutated.

Limits:

- Do not rewrite accepted predecessor evidence files in place.
- Do not create or mutate source acceptance.
- Do not create page-complete acceptance.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this display normalization
  into semantic/source changes without separate bounded authorization.

Invalidation:

This display normalization stales if human-facing structure vocabulary,
source-reconstruction packet format, page-complete review packet format,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-MAP-READINESS-P004-001

Status: `expired`; scope consumed by `PMRP-G1-VIRAL-P004-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `777`: "ок. поехали дальше" after
`P004COD-G1-VIRAL-001` confirmed the page 004 full tilted inset as
context-only and `SDN-G1-VIRAL-001` normalized human-facing structure display.

Exact action:

- Consume exact `P004A-G1-VIRAL-004` source acceptance evidence.
- Consume exact `P004COD-G1-VIRAL-001` context-only confirmation for
  `PRM-G1-VIRAL-001-P004-R01`.
- Run the reusable `page_map` readiness pipeline for page 004 only.
- Declare the two accepted title/body text blocks as expected in-scope blocks.
- Declare the full tilted inset as context-only, not a peer text block.
- Prepare readiness artifacts for a later separate page-complete review packet.

Allowed outputs:

- Updates to `scripts/build_page_map_readiness.py`.
- Updates to `tests/test_page_map_readiness.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p004_G1_VIRAL_001/page_map_readiness_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p004_G1_VIRAL_001/page_map_readiness_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p004_G1_VIRAL_001/page_map_readiness_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p004_G1_VIRAL_001/page_map_readiness_manifest.md`
- Status/roadmap/plan documentation sync that records the readiness packet.

Output status:

- Package id: `PMRP-G1-VIRAL-P004-001`
- Status: `ready_for_page_complete_review_packet`
- Page map readiness script SHA-256:
  `024A051ADD6D01DDCF7FDB8AA88223FB0BBBFE570EB580744B98BBD45DFBF53F`
- Page map readiness test SHA-256:
  `0E9314D6616A2607C68EF2B5E371B203D33CE1ED3031491D87F5FFD845B36A35`
- Page 004 readiness report SHA-256:
  `DEEBDA76EE371ABA8AC7761573FE5DDAA8B7D2268943C2DEC67C115F932EF39F`
- Page 004 readiness packet SHA-256:
  `1C9BE9076C84D9A577DA9CC0895ED6D84EE6E0A68EB0F34CA0DC1F9E0018DC43`
- Page 004 readiness summary SHA-256:
  `2943A0BA671F4E4C6B2B00161EAD89054BA1857895BE6F89AA6A2555B6DF1E02`
- Page 004 readiness manifest SHA-256:
  `7457E8655F406FE5D3DA588B583F24766E999E42CE853F327C53B75EBF8ED334`
- Result: two expected text blocks ready, one context-only region confirmed,
  no blockers, no open questions.
- Page 004 is not accepted as complete.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

Limits:

- Do not accept page 004 as complete in this readiness packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this readiness packet to
  another page without separate bounded authorization.

Invalidation:

This readiness packet stales if `P004A-G1-VIRAL-004`,
`P004COD-G1-VIRAL-001`, page-complete policy, page-map readiness vocabulary,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P004-001

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P004-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `777`: "ок. поехали дальше" after the
page 004 context-only decision and structure-display normalization package were
committed.

Exact action:

- Consume exact `PMRP-G1-VIRAL-P004-001` page-map readiness evidence.
- Prepare a separate page-complete review packet for page 004 only.
- Include page 004 source page image, the two accepted text crops, and the
  OCR/block text markdown review asset for Bogdan's human decision.
- Ask only whether a later explicit record may accept page 004 as complete.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p004_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p004_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p004_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p004_G1_VIRAL_001/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p004_G1_VIRAL_001/review_assets/`.
- Status/roadmap/plan documentation sync that records the review packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P004-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `23D7C745067A20E06B53935F6A2D3F51BFFEDC3EBC2C6A03E2F1645337CBF6ED`
- Page complete review test SHA-256:
  `2819A512055A8F174406C838A06BED993C56CA9EB1BC8CF07E94E80323591709`
- Page 004 complete review report SHA-256:
  `8AA0A7D8D00B21997BF54A440EFEA087A545AA0A4250A1A50F9BCE005F65ADCA`
- Page 004 complete review packet SHA-256:
  `A573FB40440370862A19CBB82F5FE5631BF70CF31967790AFBF87A2923B90E0C`
- Page 004 complete review summary SHA-256:
  `3C8B7B1D1C709F5FED04456ACB00724665ACBDC164F848FFE30B808A56C7C00B`
- Page 004 complete review manifest SHA-256:
  `EE668D049639CA857146EDE78DBF95D33458491DA446C209921BD4E82EFBDB62`
- Review assets:
  - `page_004.png`:
    `45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88`
  - `1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png`:
    `ADD3C344100356249BF38C85A7C89D2A2DB9FF23B48141509A47F86C6A32C219`
  - `2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png`:
    `EFB82E2F8ECE14585CFD83F71C301B7024C437680703B18765A259A7E3B234C8`
  - `page_004_ocr_block_text.md`:
    `7994F6D597C0041052361533BDDBCC63511B784F1BC24D6E7A089588BAAD3DDB`
- Result: page 004 is ready for Bogdan's explicit page-complete decision.
- Page 004 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

Limits:

- Do not accept page 004 as complete in this review packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Invalidation:

This review packet stales if `PMRP-G1-VIRAL-P004-001`,
`P004A-G1-VIRAL-004`, `P004COD-G1-VIRAL-001`, page-complete policy,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P004-001

Status: `expired`; scope consumed by `P004PCA-G1-VIRAL-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `793`: "`page 004 complete ok`"

Exact action:

- Consume `PCRP-G1-VIRAL-P004-001` as the page-complete review input for
  page 004.
- Record Bogdan's explicit page 004 ok as a narrow page-complete acceptance.
- Accept page 004 only.
- Preserve the accepted source text, source records, context-only confirmation,
  readiness packet, review packet, and review attachments immutable.

Allowed outputs:

- `scripts/accept_page_004_complete.py`
- `tests/test_page_004_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p004_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p004_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p004_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p004_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan documentation sync that records page 004 complete
  acceptance.

Output status:

- Package id: `P004PCA-G1-VIRAL-001`
- Status: `page_004_complete_accepted`
- Page 004 complete acceptance script SHA-256:
  `FC72004FE926FA9C8F43B74499831201587532226721673A16D836999625ACF4`
- Page 004 complete acceptance test SHA-256:
  `0DB21B2DC3DCDEC0AFACF83768276F4A1C90EB26838049AC591B96AD3FE70409`
- Page 004 complete acceptance report SHA-256:
  `57D4E5B3665129732308E042B4CECEEDD170907B2DCB852468DBBF885C222035`
- Page 004 complete acceptance record SHA-256:
  `A248722D3F7BC42A09F25FD2AF7450CCCAE41552B384A63ADDA8E247988328E5`
- Page 004 complete acceptance summary SHA-256:
  `F401362F55BE6EE770FCB3EA7659BCA4A7E30F24CEBCC09F93FBB241220254AD`
- Page 004 complete acceptance manifest SHA-256:
  `905F37C5669A4242FE45CCD51E97EAEA40308DC20E60D3E294DD7D599356E3B0`

Limits:

- Do not accept any page other than page 004 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to
  another page without separate bounded authorization.

Invalidation:

This acceptance stales if `PCRP-G1-VIRAL-P004-001`, `PMRP-G1-VIRAL-P004-001`,
`P004COD-G1-VIRAL-001`, page-complete policy, acceptance vocabulary,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-MAP-READINESS-P005-001

Status: `expired`; scope consumed by `PMRP-G1-VIRAL-P005-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `809`: "пошли дальше" after
`P004PCA-G1-VIRAL-001` accepted page 004 as complete only and the narrow
Sourcefold auto-commit rule was activated.

Exact action:

- Consume exact `SRHR-G1-VIRAL-001`, `SRQA-G1-VIRAL-001`, and
  `SRFA-G1-VIRAL-001` source-reconstruction evidence for page 005 only.
- Consume exact `PRM-G1-VIRAL-001` visual region hints for page 005 only.
- Run the reusable `page_map` readiness pipeline for page 005 only.
- Declare the contents heading and contents/list entry group as expected
  in-scope text blocks.
- Declare the margin page marker/layout component as a visual-only exclusion,
  not source text.
- Prepare readiness artifacts for a later separate page-complete review packet.

Allowed outputs:

- Updates to `scripts/build_page_map_readiness.py`.
- Updates to `tests/test_page_map_readiness.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p005_G1_VIRAL_001/page_map_readiness_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p005_G1_VIRAL_001/page_map_readiness_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p005_G1_VIRAL_001/page_map_readiness_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_map_readiness_p005_G1_VIRAL_001/page_map_readiness_manifest.md`
- Status/roadmap/plan documentation sync that records the readiness packet.

Output status:

- Package id: `PMRP-G1-VIRAL-P005-001`
- Status: `ready_for_page_complete_review_packet`
- Page map readiness script SHA-256:
  `38434DF99EF95A451C31081FFF16DBE3C56AB465617A462F41D248D692B5E04C`
- Page map readiness test SHA-256:
  `7886546905BAF54BEE7E5015E64DCA9054DB5B31CF58EC9D1FF240C838FFAC00`
- Page 005 readiness report SHA-256:
  `92C8AED6BEEBBC03CBF4495DEA07E9BCF21699D362DDF426A8E7767CE3888AE5`
- Page 005 readiness packet SHA-256:
  `E9405BF49EC2CE00DCB39C67F602035C0AD9E25D4E7E5540624A6965688B40D7`
- Page 005 readiness summary SHA-256:
  `724B4963F9FA1D12891738A02D6A17BB2A34233F983201E65EF97BF1DC260FF5`
- Page 005 readiness manifest SHA-256:
  `21A7C524F36BD070CFA5384AAF035D8203B6F4CA5A870B4F957D74F603F9EAC1`
- Result: two expected text blocks ready, one visual-only exclusion recorded,
  no blockers, no open questions.
- Page 005 is not accepted as complete.
- Whole Gate 1 is not accepted.
- Fixture admission creation, source acceptance mutation, translation,
  proofreading, renderer/profile acceptance, implementation, push, OCR, render,
  PDF parsing, PDF text-layer extraction, and raw mutation remain false.

Limits:

- Do not accept page 005 as complete in this readiness packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this readiness packet to
  another page without separate bounded authorization.

Invalidation:

This readiness packet stales if `SRHR-G1-VIRAL-001`, `SRQA-G1-VIRAL-001`,
`SRFA-G1-VIRAL-001`, `PRM-G1-VIRAL-001`, page-complete policy, page-map
readiness vocabulary, reviewer/authority, script/test revision,
roadmap/status state, or Sourcefold orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-001

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P005-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `819`, continuing from the stated next
point: "Следующая точка: подготовить `PCRP-G1-VIRAL-P005-001` — page 005
page-complete review packet для твоего решения."

Exact action:

- Consume exact `PMRP-G1-VIRAL-P005-001` page-map readiness evidence.
- Prepare a separate page-complete review packet for page 005 only.
- Include page 005 source page image, the two accepted text crop anchors, and
  an OCR/block text markdown review asset for Bogdan's human decision.
- Ask only whether a later explicit record may accept page 005 as complete.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_001/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p005_G1_VIRAL_001/review_assets/`.
- Status/roadmap/plan documentation sync that records the review packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P005-001`
- Status at packet creation: `ready_for_bogdan_page_complete_decision`
- Current regenerated status after visual proof hardening: `blocked`
- Page complete review script SHA-256:
  `6F25FEFB030F9006B6B6D6A1F58B7675B1A33C28158B680C2BB330557B5D047E`
- Page complete review test SHA-256:
  `85A903921CEDE0F9952F891F9FA45EE9F8ADC5F91F02ADD157B10AF22DDCF66E`
- Page 005 complete review report SHA-256:
  `D6564256A5C460ED37383D798D59F3B1BE70EAC25770F6DAF3C02FAD178344E4`
- Page 005 complete review packet SHA-256:
  `C00A87D74D9AD605CE0F00BA9F62E5A61D839511681F7E2CF5131404271AF31F`
- Page 005 complete review summary SHA-256:
  `936AB43CF6EB433F3B76301B25910B4BC83C7F66BC1012D8CBEA640F288600B7`
- Page 005 complete review manifest SHA-256:
  `37566B404C531AC9E0D65ED765B8AEF691EB81937A1244088B150E69401D98D4`
- Review assets:
  - `page_005.png`:
    `0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE`
  - `1_SRA-G1-VIRAL-001-R002__PRM-G1-VIRAL-001-P005-R01.png`:
    `8A3A979381FB476C3B6D9831D7665E50F3171C4D4300EB7C3373E4216738CF24`
  - `2_SRA-G1-VIRAL-001-R003__PRM-G1-VIRAL-001-P005-R02.png`:
    `A09B5848048C3BD20FEB71B0FC37FC55E108AA08454BCFB1156D3FAD62E5B40F`
  - `page_005_ocr_block_text.md`:
    `4C14CA5A17CBE5BC1058D0B075F83C291FCFB0578333D6C51E488DFDCFE40875`
- Result at packet creation: page 005 was ready for Bogdan's explicit
  page-complete decision.
- Current human decision: Bogdan held `PCRP-G1-VIRAL-P005-001` in Telegram
  message `833` with reason: crop coverage is insufficient, the
  R003/contents-entry crop cuts off text, and the review packet may need more
  than two crops to cover all page content.
- Generator hardening result: `build_page_complete_review.py` now strictly
  compares each block-crop image dimension with the readiness `box_px`
  dimensions and blocks crops smaller than the declared block size. `P005-B001`
  and `P005-B002` are blocked with
  `visual_crop_smaller_than_declared_block_box`.
- Current status: `blocked_for_superseding_review_packet_with_broader_crop_coverage`.
- Next permitted action: prepare a separately bounded superseding page 005
  page-complete review packet with broader/more crops before asking for any
  page-complete acceptance decision.
- Page 005 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

Limits:

- Do not accept page 005 as complete in this review packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Invalidation:

This review packet stales if `PMRP-G1-VIRAL-P005-001`, `SRHR-G1-VIRAL-001`,
`SRQA-G1-VIRAL-001`, `SRFA-G1-VIRAL-001`, page-complete policy,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-GATE-1-STATUS-REFRESH-005

Status: `expired`; scope consumed by `G1SP-G1-VIRAL-005`.

Created: 2026-07-26

Authority: Bogdan Telegram message `1650`: "все ок" after the orchestrator
recommended post-P010 status refresh before page 011 triage.

Exact action:

- Consume exact page-complete acceptance reports for pages 001-010.
- Consume exact post-P009 status route packet `G1SP-G1-VIRAL-004`.
- Create status-only `G1SP-G1-VIRAL-005` recording pages 001-010 as
  page-complete accepted only and pages 011-020 as unstarted.
- Recommend page 011 triage/readiness as the next candidate without
  authorizing that layer.

Allowed outputs:

- `scripts/build_gate_1_status_refresh_post_p010.py`
- `tests/test_gate_1_status_refresh_post_p010.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_005/gate_1_status_packet.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_005/gate_1_status_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_005/gate_1_status_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_005/gate_1_status_manifest.md`
- Status/roadmap/plan documentation sync for the post-P010 route state.

Limits:

- Do not create page 011 triage under this status authorization.
- Do not accept page 011 or any page 011-020 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR/render/PDF
  parsing/raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action.

Output status:

- Package id: `G1SP-G1-VIRAL-005`
- Status: `gate_1_status_route_packet_ready_no_acceptance`
- Script SHA-256:
  `BE537C718CA51E1F347DAC31374C6E7837E1CEE561FC9F18988DE677F19804A4`
- Test SHA-256:
  `FD06557D9FFF3FC2F0D9DA9FC83F6A34896B9BEF0A92B3BC2B2C3AF54EA24754`
- Packet SHA-256:
  `E696DE1651E43539A07ECA958B948678DE7FFAAE61EB426F2CE46C478C5310E2`
- Report SHA-256:
  `6598FDCBAC1F9FA8C38705818F6F2BBBFF7CDA334C18C8ABE2C23DA115CF7FD7`
- Summary SHA-256:
  `54DC61DB162DFBCCC4F79AE8A669CC2AFAC292912E5246A85C8B1C042092259F`
- Manifest SHA-256:
  `A9120164E924C9A417EB908906E4B62157F32DD11719CD1996BBCFE03EA59C00`

## BA-G1-VIRAL-PAGE-011-TRIAGE-001

Status: `expired`; scope consumed by `P011TR-G1-VIRAL-001`.

Created: 2026-07-26

Authority: Bogdan Telegram message `1650`: "все ок" after the orchestrator
recommended moving from `G1SP-G1-VIRAL-005` into page 011 triage/crop-contract.

Exact action:

- Consume exact post-P010 status route packet `G1SP-G1-VIRAL-005`.
- Consume existing page 011 render image and existing PRM/content/art-map
  predecessor evidence.
- Build page 011 triage/crop-role contract only, with peer review blocks for
  text-like regions and art anchors.
- Materialize OCR/text evidence crops only for text-like regions.
- Keep art anchors visual-only and create no text extraction, semantic map,
  PCRP, or page-complete acceptance.

Allowed outputs:

- `scripts/build_page_011_triage.py`
- `tests/test_page_011_triage.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_triage_G1_VIRAL_001/page_011_triage_packet.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_triage_G1_VIRAL_001/page_011_triage_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_triage_G1_VIRAL_001/page_011_triage_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_triage_G1_VIRAL_001/page_011_triage_manifest.md`
- Review assets under `page_011_triage_G1_VIRAL_001/review_assets/`.
- Status/roadmap/plan documentation sync that records page 011 triage
  readiness for Bogdan review.

Limits:

- Do not create page 011 text extraction, semantic map, PCRP, or
  page-complete acceptance.
- Do not process pages 012-020 beyond continuation metadata.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR/render/PDF
  parsing/raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action.

Output status:

- Package id: `P011TR-G1-VIRAL-001`
- Status: `page_011_triage_crop_contract_ready_for_bogdan_review_no_text_extraction_no_pcrp`
- Script SHA-256:
  `524DBC98D41908B5FDA7DFEB8CB0F7AFA32FFBEED74517E9A3FC9F91D167C681`
- Test SHA-256:
  `F1C39EF4A273C3354BAAB1FA9323C8909387CA9E45E92FCE7BB4CA3B56CF5D75`
- Packet SHA-256:
  `E27AF4DC0B601D7562DE240980C7F6BC8BAD008D05FC3841396B2B0F8289BE8B`
- Report SHA-256:
  `E1E3E3A43DAD0995142E9842C0DAC3BBE601385ADC9FE6E2D60F72641F227E6D`
- Summary SHA-256:
  `30ECCD3E545209C8F7A7E64A50C3C0C4C8E5FD2D1029E3F3D60EA7FE137006B8`
- Manifest SHA-256:
  `A0F73DEA7B22DF264D1E5F7C638093FD54E51065F5EBE77C919EFA895281FC12`
- Result: page 011 is ready for Bogdan triage/crop-contract review with two
  text evidence surfaces and two visual-only art anchors.

## BA-G1-VIRAL-PAGE-011-TEXT-EXTRACTION-001

Status: `scope_consumed`; materialized `P011TXT-G1-VIRAL-001`.

Created: 2026-07-26

Authority: Bogdan Telegram message `1673`: "делай коммит и пошли дальше" after
`p011 triage ok` and the clarification that `P011-B002` and `P011-B003` remain
visual-only and do not enter OCR/text extraction.

Exact action:

- Consume exact `P011TR-G1-VIRAL-001` triage/crop-contract packet.
- Record Bogdan's explicit `p011 triage ok` decision as the human review basis.
- Create `P011TXT-G1-VIRAL-001` as a draft text extraction/review artifact
  from only the two page 011 text evidence crops:
  - `P011-B001-TES` Maya continuation / secrets / appearance.
  - `P011-B004-TES` Emily profile text.
- Keep `P011-B002` Emily portrait and `P011-B003` lower-left screen image as
  visual-only anchors excluded from text extraction.

Allowed outputs:

- `scripts/build_page_011_text_extraction.py`
- `tests/test_page_011_text_extraction.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_text_extraction_G1_VIRAL_001/page_011_text_map.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_text_extraction_G1_VIRAL_001/page_011_text_extraction_packet.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_text_extraction_G1_VIRAL_001/page_011_text_extraction_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_text_extraction_G1_VIRAL_001/page_011_text_extraction_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_text_extraction_G1_VIRAL_001/page_011_text_extraction_manifest.md`
- Status/roadmap/plan/context documentation sync that records page 011 draft
  text readiness for Bogdan review.

Limits:

- Do not create page 011 semantic map, PCRP, or page-complete acceptance.
- Do not include `P011-B002` or `P011-B003` in text extraction.
- Do not process page 012 beyond continuation metadata.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR/render/PDF
  parsing/raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action.

Output status:

- Package id: `P011TXT-G1-VIRAL-001`
- Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`
- Script SHA-256:
  `EABD599416E9187F9FE65CDAC3B8531039F9D59FB38FE98681BA88BFD1C29B53`
- Test SHA-256:
  `FF8002841A45C569CDF038F7404DAD700DF68415DC535AE13AA8EEEA0BC239BB`
- Text map SHA-256:
  `0564ABB708AEE61F6602926B67427460DE6B96167F98A2FB5F97468CF9EBCAF8`
- Packet SHA-256:
  `EE49200061446792CAC839FA541473614AB630D4D71993DB366BFD335EB23412`
- Report SHA-256:
  `4DB125FCBF72A5F0F703489966B8563103C0A642BBC0EE168EF98B928C1893EE`
- Summary SHA-256:
  `9D873BC246A1A0D79C0AE00A9ED7AEC157B7FF1E88E94F22E09A693E1401893B`
- Manifest SHA-256:
  `E236D50126AF1042834B8D1A5C5FE7B447C1D8293143FE9D0E110863113FD93F`
- Result: page 011 draft text is ready for Bogdan review from exactly two
  text evidence crops, with `P011-B002` and `P011-B003` excluded as
  visual-only anchors.

## BA-G1-VIRAL-PAGE-011-SEMANTIC-TEXT-MAP-001

Status: `scope_consumed`; materialized `P011SEM-G1-VIRAL-001`.

Created: 2026-07-26

Authority: Bogdan Telegram messages `1691` and `1696`: `p011 text ok` followed
by "делай р011сем" after the page 011 text extraction review boundary was
explained.

Exact action:

- Consume exact `P011TXT-G1-VIRAL-001` draft text extraction artifact.
- Record Bogdan's explicit `p011 text ok` decision as the human review basis
  for semantic projection only.
- Create `P011SEM-G1-VIRAL-001` as a semantic text-map review artifact with
  stable units, heading levels, paragraph boundaries, crop links, and
  continuation metadata.
- Represent `P011-B001-TES` as Maya continuation from page 010 plus
  `Maya's Secrets` and `APPEARANCE` heading/body units.
- Represent `P011-B004-TES` as Emily profile heading/body units, including
  `Super Fan Option.` as a bounded inline option heading and Emily
  continuation metadata to page 012.
- Keep `P011-B002` Emily portrait and `P011-B003` lower-left screen image as
  visual-only anchors excluded from in-scope text units.

Allowed outputs:

- `scripts/build_page_011_semantic_text_map.py`
- `tests/test_page_011_semantic_text_map.py`
- `scripts/page_review_semantic_units.py`
- `tests/test_page_complete_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_semantic_text_map_G1_VIRAL_001/page_011_semantic_text_map.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_semantic_text_map_G1_VIRAL_001/page_011_semantic_text_map.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_semantic_text_map_G1_VIRAL_001/page_011_semantic_text_map_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_semantic_text_map_G1_VIRAL_001/page_011_semantic_text_map_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_011_semantic_text_map_G1_VIRAL_001/page_011_semantic_text_map_manifest.md`
- Status/roadmap/plan/context documentation sync that records page 011 semantic
  map readiness for Bogdan review.
- Universal optional semantic-unit layout/style hints and Markdown projection
  visibility for those hints.

Limits:

- Do not create PCRP or page-complete acceptance.
- Do not include `P011-B002` or `P011-B003` as in-scope text units.
- Do not process page 012 beyond continuation metadata.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR/render/PDF
  parsing/raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action.

Output status:

- Package id: `P011SEM-G1-VIRAL-001`
- Status: `semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance`
- Script SHA-256:
  `7A4A70FA6B701F986F45BAC74B1EF0F3C551A1D5F4FCD7AF946C9950F48F0AA1`
- Test SHA-256:
  `F6BCCF2EB7031164712E235AEDB5421F9E7EB48D5B3954634D59F9D0AF9BB4F8`
- Universal semantic-unit helper SHA-256:
  `0BBB518558219FC92D768E59E2F3B47C6A97760BCF16F2143CC5DE773602C5BF`
- Universal semantic projection test SHA-256:
  `DDF2206730DBD01983A4CC3D142449D12DEAD1497C044B55B7B0B134F70CCD44`
- Semantic Markdown SHA-256:
  `61274D62CE3F353934FF5B89BB4D567FBE83B6C1BB0610230FC72B9DD5E202E6`
- Semantic JSON SHA-256:
  `3136926D54B1663C6A9741DFD94D7EDB73CE0C9DB6962FB9CF311D23F10F8B09`
- Report SHA-256:
  `9C9493E4474530C5820A32382B2ABA422EAF1B5DD4E6EAA2EE59A3AC850047CB`
- Summary SHA-256:
  `B46C20FE569BC9C1F3ECEC16251CC2FBDE526E86C25096B4EF3BE3CE359464BC`
- Manifest SHA-256:
  `9D586CEC8EDFF4B0997FEF8A3E15CFD05C090E9304E79934F7F80C760E2AEC7B`
- Result: page 011 semantic text map is ready for Bogdan review, with
  heading levels, paragraph boundaries, crop linkage, continuation metadata,
  universal layout/style hints, and visual-only anchors excluded.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P011-001

Status: `scope_consumed`; materialized `PCRP-G1-VIRAL-P011-001`.

Created: 2026-07-26

Authority: Bogdan Telegram messages `1744` and `1749`: "Тогда семантик меп ок"
followed by "Делай р011 рсрп, все шаги 1-6" after the page 011 semantic map
review boundary was explained.

Exact action:

- Consume exact `P011TR-G1-VIRAL-001`, `P011TXT-G1-VIRAL-001`, and
  `P011SEM-G1-VIRAL-001` predecessors.
- Record Bogdan's explicit `p011 semantic map ok` decision as the human review
  basis for the page-complete review packet only.
- Create `PCRP-G1-VIRAL-P011-001` as a page-complete review packet for Bogdan's
  later explicit page 011 page-complete decision.
- Package page 011 source page image, two text-evidence crops, two visual-only
  human-context art anchors, predecessor text map, semantic map Markdown/JSON,
  and generated review text map.
- Keep `P011-B002` Emily portrait and `P011-B003` lower-left screen image as
  visual-only anchors, not in-scope text.
- Preserve page 011 semantic layout/style hints in the packaged semantic map,
  including `Super Fan Option.` as italic inline `h3` with same-line
  continuation.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p011_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p011_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p011_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p011_G1_VIRAL_001/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p011_G1_VIRAL_001/review_assets/`.
- Status/roadmap/plan/context documentation sync that records page 011 PCRP
  readiness for Bogdan page-complete review.

Limits:

- Do not create page 011 page-complete acceptance in this packet.
- Do not process page 012 beyond continuation metadata.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR/render/PDF
  parsing/raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action.

Output status:

- Package id: `PCRP-G1-VIRAL-P011-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `C73888ABAD4A210531EC7DFDACCA8C4A7A639EFB8D77F444E2FC458CA271F0C1`
- Page complete review test SHA-256:
  `64FD84E935FD27D94A911035EE837BFA59D3DCBE21ED1A8FC1CF6DFAA266FC39`
- Page 011 complete review report SHA-256:
  `C52244B870C222B8406FC45AD6A791ECB4BF068E8C65D12160488AF70D0704F6`
- Page 011 complete review packet SHA-256:
  `A5A159B9EB525F8DDDE2B3A7E743A89FC3F2C4A2C81E59CA1DD6DAB493BAE8A3`
- Page 011 complete review summary SHA-256:
  `50801CC5C7F8ADD58432C4B2EB35444DF00626AC63841FC32768D01974A34119`
- Page 011 complete review manifest SHA-256:
  `4C4F79D58123C27345B559F4108A21F72316DD76DF21F2F89976647F1896C729`
- Review assets:
  - `page_011.png`:
    `697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6`
  - `1b_P011-left-maya-continuation-secret-appearance-text-evidence.png`:
    `6AE73BB523A34DC9D59F901C08633E67D7270108D6CA59C10A1D38EDD463232B`
  - `2_P011-emily-em-lavigne-portrait-image-area-human-context.png`:
    `ECE5BB76CEC123593B97CA2BC67B3E9561298398E91078E8D5F45C431FCD15D1`
  - `3_P011-lower-left-screen-image-area-human-context.png`:
    `84A3FC84F2CCE74860CCC441870B30E6A9E870940DFBE7B18215928926092632`
  - `4b_P011-right-emily-profile-text-text-evidence.png`:
    `B61C33FA2CBE276B605EB207014EACBD39D7B46925E8D9377921CF57C24E1D4A`
  - `page_011_ocr_verified_text_map.md`:
    `8E0C30537A0CE166DD419446C8896E6E5F67D942FBDE91AE9C3450C4D32316A3`
  - `page_011_semantic_text_map.md`:
    `61274D62CE3F353934FF5B89BB4D567FBE83B6C1BB0610230FC72B9DD5E202E6`
  - `page_011_semantic_text_map.json`:
    `3136926D54B1663C6A9741DFD94D7EDB73CE0C9DB6962FB9CF311D23F10F8B09`
- Result: page 011 is ready for Bogdan's explicit page-complete decision with
  4/4 ready blocks, two source-text blocks, two visual-only art anchors, valid
  semantic validation, valid inventory reconciliation, and no blockers.
- Page 011 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR/render/PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P011-001

Status: `scope_consumed`; materialized `P011PCA-G1-VIRAL-001`.

Created: 2026-07-26

Authority: Bogdan Telegram message `1760`: "Пейдж 11 ок" after reviewing
`PCRP-G1-VIRAL-P011-001`.

Exact action:

- Consume exact `PCRP-G1-VIRAL-P011-001` page-complete review packet.
- Record Bogdan's explicit page 011 complete decision as the human acceptance
  basis.
- Create `P011PCA-G1-VIRAL-001` as a separate page-complete acceptance record
  for page 011 only.

Allowed outputs:

- `scripts/accept_page_011_complete.py`
- `tests/test_page_011_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p011_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p011_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p011_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p011_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan/context documentation sync that records page 011
  page-complete acceptance only.

Limits:

- Accept only page 011 as complete.
- Do not accept whole Gate 1.
- Do not create fixture admission, source acceptance mutation, OCR/render/PDF
  parsing/raw mutation, translation, proofreading, renderer/profile acceptance,
  implementation, push, or broader Gate action.
- Do not process page 012 beyond existing continuation metadata.

Output status:

- Package id: `P011PCA-G1-VIRAL-001`
- Status: `page_011_complete_accepted`
- Script SHA-256:
  `1F0AC00EB34AC2BDE351C7CD5718C239D19C4B53AEC59F31E2A460B51CE51C7B`
- Test SHA-256:
  `E9A861D8007996BE32F3C32F8F7C047BDE7B9FDD64AB38437227B607DCFDD9CB`
- Acceptance report SHA-256:
  `973E19C9E58EEEF3CABEAC16FD9C887948B7AF81F18916738E8867913E09B0A3`
- Acceptance record SHA-256:
  `FB716712565605C61511FE37DB0716B059BE9C6A6CE390637804A141EBC1104A`
- Acceptance summary SHA-256:
  `2C3E9456A12023A77CCEACBB5E8010825D4D32CA25FEF8CED4B8788AD7B3BB57`
- Acceptance manifest SHA-256:
  `B73B06380E035CD095ADEB48731C89CE5A4EF037940CC87B98170FA6A3801A34`
- Result: page 011 is accepted as complete only.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR/render/PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P006-001

Status: `expired`; scope consumed by `P006PCA-G1-VIRAL-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `996`: "6 ок. Коммит и обнови
документацию" after reviewing the `PCRP-G1-VIRAL-P006-002` page-complete
review packet artifacts in chat.

Exact action:

- Consume exact `PCRP-G1-VIRAL-P006-002` page-complete review evidence.
- Create a separate page-complete acceptance record for page 006 only.
- Record Bogdan's explicit page 006 complete decision as the human acceptance
  basis.
- Keep `PCRP-G1-VIRAL-P006-001` held/superseded and non-consuming for
  acceptance routing.

Allowed outputs:

- `scripts/accept_page_006_complete.py`
- `tests/test_page_006_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p006_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p006_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p006_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p006_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan/context documentation sync that records page 006
  page-complete acceptance only.
- `docs/roadmap/roadmap_viewer.html` fallback cleanup so the standalone viewer
  no longer displays stale embedded roadmap state when canonical
  `roadmap.yaml` is not loaded.

Output status:

- Package id: `P006PCA-G1-VIRAL-001`
- Status: `page_006_complete_accepted`
- Page 006 complete acceptance script SHA-256:
  `C3CE285DE507921EDA657E29336078F35D8F4B71EDF281FAFBBDF26D6AF9CE93`
- Page 006 complete acceptance test SHA-256:
  `38D4C8FBF957531318D0A7183D8724B3E9A9F27C40B80BC803550520FCE3452B`
- Page 006 complete acceptance report SHA-256:
  `9D0643332F24AF2B5FF3D14518B9FF83B70B331FA1E165577A6C5245532692B5`
- Page 006 complete acceptance record SHA-256:
  `F60BDBB4A2F4735DD931ED3A0CCE338F7A1A87D16EF9176F9331A7BAC17244A6`
- Page 006 complete acceptance summary SHA-256:
  `0498432BECE7B8B4DC21969DC2C6EDD6EB60AECE12AFF88822C5267BE43689E9`
- Page 006 complete acceptance manifest SHA-256:
  `B117B4A48B06EEECB8FABA73DDFA3233B53FFF17599CF3955BB1C7C8E32B97F1`
- Result: page 006 is accepted as complete only.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

Limits:

- Accept page 006 as complete only.
- Do not accept page 005 or any other page.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to another
  page without separate bounded authorization.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P006-001

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P006-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `880`: page 005 is fully OK; make page 6
and show the final packet for review.

Exact action:

- Prepare a separate page-complete review packet for page 006 only.
- Reuse the existing rendered page image `page_006.png`.
- Generate human-readable crops for the title, left text column, and right text
  column.
- Include a crop-verified text map with heading depth/style and complete text
  corresponding to the review crops.
- Keep upper background art and the bottom page marker as visual/context-only
  exclusions, not source text records.
- Ask only whether a later explicit record may accept page 006 as complete.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_001/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p006_G1_VIRAL_001/review_assets/`.
- Status/roadmap/plan documentation sync that records the page 006 review
  packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P006-001`
- Status after human review: `hold`
- Hold decision: Bogdan Telegram messages `896` and `897`.
- Hold reason: `text_map_semantics_and_formatting_blocker`.
- Crop decision: page 006 review crops are correct as human review assets.
- Blocking issue: `page_006_ocr_verified_text_map.md` collapses multiple
  semantic units into crop/block rows, allowing headings, quote text, body text,
  and column continuation to lose their individual structure in the human map.
- Concrete P006 symptoms:
  - `Introduction` text is correct, but heading level is shown as `h1`; expected
    review-level interpretation is `h2`, with a deferred TODO to synchronize the
    global book heading hierarchy with the credits/credit page if present, or
    design the credits/heading normalization path if absent.
  - `Summary` is a heading and should be a separate semantic unit, likely `h3`,
    not swallowed into `left_column_summary_overview_text`.
  - The Marco Proudfoot quote should be a quote semantic unit with plain/body
    heading level semantics, not `heading_level=quote`.
  - `Overview` is a heading embedded mid-crop and must be a separate semantic
    unit, likely `h3`.
  - The right column is body continuation of Overview, not a per-line structure
    and not a style named `right_column_overview_text`.
- Decision: page 006 is not accepted as complete. A superseding P006 packet
  must wait for semantic-map pipeline hardening, not a one-off markdown edit.
- Machine-readable post-review routing update:
  - `PCRP-G1-VIRAL-P006-001` now reports `status=blocked`.
  - `review_decision.requires_bogdan_decision=false`.
  - `review_decision.requires_superseding_review_packet=true`.
  - `review_decision.requires_superseding_package_id=PCRP-G1-VIRAL-P006-002`.
  - Its only decision option is hold/correction routing; it must not expose
    `page 006 complete ok`.
  - The previous text map remains usable only as negative regression input for
    collapsed semantic units, not as structure evidence.
- Current reproducibility hashes after the post-review routing update:
  - `scripts/build_page_complete_review.py` SHA-256:
    `4A5FA34E97F696B5AC86779BC16B7715C69A581718295A0F390AC301B0AC07B7`
  - `tests/test_page_complete_review.py` SHA-256:
    `8FCD47047B3B0B8B05D9094FC5A532F59A28F7D755FCF44A00D54617193D8762`
  - `page_complete_review_report.json` SHA-256:
    `8B9861D91AEA309E3E9B11A14F3872BDAD4EE629FFEC941B418658515348B7A6`
  - `page_complete_review_packet.md` SHA-256:
    `28A4CB8BC29E9ACE3243A471A36DD86F5FE74C4592A72C520C6BDA52A89F6B70`
  - `page_complete_review_summary.md` SHA-256:
    `0469B8EB5C7B2666D54023289F377CB30B659E00613A8AA5DFF8EA3DCF71DED8`
  - `page_complete_review_manifest.md` SHA-256:
    `A3ADEAD2A4A7DF91B5945CD6EACC83976E72FCE6F8CC64C49DCACCCB21B5528E`

Limits:

- Do not accept page 006 as complete in this review packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, mutate raw artifacts, or broaden this review packet to another page
  without separate bounded authorization.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P006-002

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P006-002`

Created: 2026-07-24

Authority: Bogdan Telegram messages `918`, `921`, `924`, `927`, `930`, `933`,
`939`, `945`, `948`, and `951`: proceed through the semantic-map hardening
plan, commit completed steps, and continue to the superseding P006 packet after
contract hardening.

Exact action:

- Generate `PCRP-G1-VIRAL-P006-002` as the superseding page 006
  page-complete review packet after semantic-map hardening steps 1-10.
- Reuse existing page 006 rendered image and already accepted human-review crop
  framing from `PCRP-G1-VIRAL-P006-001`; do not rerender or inspect the source
  PDF.
- Replace the blocked collapsed text-map structure with canonical semantic
  JSON and a Markdown projection generated from span-level semantic units.
- Correct the known P006 structural blockers:
  - `Introduction` is represented as heading text with review-level `h2`.
  - `Summary` is a separate heading unit.
  - The Marco Proudfoot quote is a quote unit with no heading level.
  - `Overview` is a separate heading unit.
  - The right column is linked as continuation of the Overview body.
- Expose the new packet for Bogdan page-complete review only if semantic
  validation, Markdown projection validation, and inventory reconciliation are
  valid and no non-waivable structural findings remain.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_002/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_002/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_002/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p006_G1_VIRAL_002/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p006_G1_VIRAL_002/review_assets/`.
- Status/roadmap/plan/context documentation sync for the superseding review
  packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P006-002`
- Status: `ready_for_bogdan_page_complete_decision`
- Semantic validation: valid, findings 0.
- Markdown projection validation: valid, findings 0.
- Inventory reconciliation: valid, findings 0.
- `Introduction` is represented as `heading_level=h2`.
- The Marco Proudfoot quote is represented as a quote unit with no heading
  level.
- `Summary` and `Overview` are separate heading units.
- `SU-P006-B002-S005` continues to `SU-P006-B003-S001`, linking the right
  column as Overview-body continuation.
- The generated OCR/verified text map uses metadata rows plus per-unit fenced
  full-text blocks instead of long prose table cells.
- Decision routing exposes `page 006 complete ok` and `hold page 006` for
  Bogdan review.
- No page-complete, whole-Gate, fixture, source, OCR, render, PDF text-layer,
  translation, proofreading, renderer/profile, implementation, or push
  acceptance/action was created.
- Current reproducibility hashes:
  - `scripts/build_page_complete_review.py` SHA-256:
    `FA472906F557ECE98428B045DA8943D628BA20AB7A1E007F60CCCD38D4C1263A`
  - `scripts/page_review_semantic_units.py` SHA-256:
    `F49E71E85A2DF86F7C9C96E10A5D474E369620F996B331CBFD5FF82BDF47A7A5`
  - `tests/test_page_complete_review.py` SHA-256:
    `73A07B36A88F475464D84608BE18A851B41DADDF648FC4A41A5025D55648A4CF`
  - `page_complete_review_report.json` SHA-256:
    `2D203EEFEA538CF3A7E88553C59BA05992FC64D65AAE654F66B69A876F478F1D`
  - `page_complete_review_packet.md` SHA-256:
    `AD6E683671AEF5A43CA5648334AA7F6116613E2B59560F24625404D2EBA2E640`
  - `page_complete_review_summary.md` SHA-256:
    `76AE233287BAE646835F8994F4151427EB0DB865F30B9CFD46FD2E1B89C27081`
  - `page_complete_review_manifest.md` SHA-256:
    `79DA33D88A2DEB881996D582F60A51C1DB22A5417F991F1D685C7454CE7B4F16`
  - `page_006_ocr_verified_text_map.md` SHA-256:
    `33CE4A5E34C80FFE36A5ACF8BF44D7E17CBFB1802BC125D3C3BE40A3696E124D`
  - `page_006_semantic_text_map.json` SHA-256:
    `77D6010D86FE9D1E9489CBBD19BD803E10D85F9B594BF3AC1B692C26AA6A7B11`
  - `page_006_semantic_text_map.md` SHA-256:
    `8E46B8BA256A36E2700E2447DD5AEA68A52172B1CDD6EEFC47EA1EE4BD7AA645`

Limits:

- This authorization creates a review packet only.
- It does not accept page 006 as complete.
- It does not accept whole Gate 1.
- It does not create fixture admission.
- It does not create or mutate source acceptance.
- It does not run OCR, parse/extract PDF text, rerender, mutate raw artifacts,
  translate, proofread, accept renderer/profile behavior, implement runtime
  behavior, push, or broaden this review packet to another page.

Invalidation:

This review packet stales if `PCRP-G1-VIRAL-P006-001`, the page 006 rendered
image, semantic-map schema/taxonomy, page-complete review contract,
builder/test revision, roadmap/status state, or Sourcefold orchestrator
workflow changes.

## BA-G1-VIRAL-PAGE-REVIEW-SEMANTIC-MAP-HARDENING-001

Status: `implemented-through-step-11`; `PCRP-G1-VIRAL-P006-002` generated and
pending Bogdan page-complete decision

Created: 2026-07-24

Authority: Bogdan Telegram message `906`: record the full plan, update the
roadmap, fix context and goal, then commit.

Problem statement:

- `PCRP-G1-VIRAL-P006-001` exposed a reusable page-complete review pipeline
  gap: visual crops and text presence can pass while the human-facing
  OCR/verified text map loses structural semantics.
- The issue is pipeline-level, not P006-only. Future pages may include art,
  captions, tables, callouts, sidebars, cards, stat blocks, mixed columns, and
  multi-region continuations.

Goal:

- Harden the page-complete review semantic-map pipeline, then generate a
  superseding P006 packet for Bogdan page-complete decision.
- Separate visual crop, source region/block, and semantic unit models.
- Make human-facing maps reveal structural omissions instead of hiding them.

Planned correction phases:

1. Record current P006 state as hold: crops ok, text map blocked, no
   page-complete acceptance.
2. Define a reusable `semantic_units` model with `unit_id`, `unit_type`,
   `text`, `heading_level`, `style`, `source_region_id`, `crop_ids`,
   `reading_order`, `continues_from`/`continues_to`, and `evidence_state`.
3. Update text-map templates so long body text is not placed in raw multiline
   markdown table cells; tables summarize units and full text is shown in
   stable per-unit blocks.
4. Add filling rules: headings cannot be swallowed into body text; quotes cannot
   use heading levels; technical block roles cannot leak into display style;
   crops can cover multiple semantic units; semantic units can continue across
   crops/columns; art/table/card/callout/stat block units are explicit or
   explicitly declared absent/context-only/visual-only.
5. Refactor `build_page_complete_review.py` so maps are generated from
   semantic units/spans, not directly from `block["text"]` rows.
6. Add schema and structural validation before packet readiness can be reported.
7. Add structural findings such as `collapsed_units`, `invalid_heading_level`,
   `missing_expected_heading`, `quote_flattened`,
   `markdown_table_integrity_failed`, `style_is_block_role`,
   `missing_continuation_link`, and `unrepresented_structural_unit`.
8. Strengthen tests to fail when expected units are collapsed, quote/body
   levels are invalid, block roles appear as styles, long prose breaks markdown
   tables, or a ready packet has structural findings.
9. Add regression coverage for P005 TOC-like rows/page refs, P006 heading +
   quote + body + heading + column continuation, and future synthetic mixed
   shapes for art+caption, table, boxed callout/sidebar, and stat/card block.
10. Update readiness/page-complete contracts so structural criteria and
    non-waivable structure loss are first-class review gates.
11. Generate a superseding `PCRP-G1-VIRAL-P006-002` only after the hardening
    exists, then run Sol/Terra and show Bogdan the human-facing package.

Sol/Terra refinement additions:

- P006 hold state:
  - Treat `PCRP-G1-VIRAL-P006-001` as held/superseded for acceptance routing;
    any page 006 acceptance path must require a later `PCRP-G1-VIRAL-P006-002`.
  - Record that P006-001 was falsely ready because structural validation did
    not exist; the old text map is usable as negative regression evidence only.
  - "Crops ok" means only human-review framing. It does not prove text
    completeness, OCR quality, semantic acceptance, source acceptance,
    page-complete readiness, or fixture admissibility.
- Semantic-unit schema:
  - Define schema and taxonomy versions, allowed enum registry, ID format,
    cardinality rules, nullable fields, and extension procedure.
  - Separate `unit_type`, `display_style`, `source_role`, `block_role`,
    `review_state`, and `unit_scope`.
  - Add `source_block_id`/`span_ids`, `parent_unit_id`/`container_unit_id`,
    many-to-many source-region/crop links, `bbox_or_anchor_ref`,
    per-unit `evidence_predecessors`, and `text_source_state`.
  - Allowed unit scopes include `in_scope_text`, `context_only`,
    `visual_only`, `excluded`, `unknown`, and `blocked`.
  - Text evidence states must distinguish `accepted_source`,
    `human_verified`, `draft_review_text`, `ocr_raw_existing`, and
    `not_applicable`; no state may authorize new OCR, PDF text extraction, PDF
    parsing, rerendering, or raw mutation.
- Human map template:
  - The canonical artifact is machine-readable report/schema data; Markdown is
    a human projection.
  - Markdown uses metadata summary tables only, with full text in stable
    per-unit blocks below the table.
  - Specify escaping, fenced/raw text handling, maximum preview length, crop and
    source-region links, continuation links, structural findings, and a "Not
    Evidence For" section.
  - Add markdown projection validation for row counts, column counts, escaping,
    and absence of long raw multiline table cells.
- Filling rules and reconciliation:
  - Every observed or expected page region must reconcile to semantic units or
    an explicit absent/context-only/visual-only/excluded/unknown/blocked
    decision.
  - Expected headings must come from controlled evidence: spans, visual profile,
    TOC cross-reference, accepted/human-verified source, or bounded
    human-authored profile override; do not hardcode P006 text such as
    `Summary`/`Overview`.
  - Unsupported structures must become `unknown_unsupported` or
    `unclassified_bounded_unit` blockers, not omissions.
  - Container/child handling must prevent duplicate text for callouts,
    sidebars, cards, stat blocks, tables, boxed regions, art+caption groups,
    and nested regions.
- Builder contract:
  - Inputs are limited to already-authorized rendered images, readiness packets,
    accepted/human-verified/draft artifacts, existing review crops, and bounded
    profile overrides.
  - The builder must fail closed when a page profile provides only
    `block["text"]` without semantic decomposition.
  - Semantic units should derive from canonical readiness/source structures;
    page-specific inline semantic truth is allowed only as a bounded override
    with explicit lineage.
  - Add deterministic ordering and ID-generation rules, stale-input detection
    for schema/taxonomy/profile/script/test/predecessor changes, and boundary
    checks that prevent OCR, PDF parsing/text-layer extraction, rerendering, and
    raw mutation.
- Validation and findings:
  - Validation runs before report status, packet text, manifest hashing, and
    decision options.
  - Add report fields such as `semantic_validation`, `semantic_units_validated`,
    `structural_findings`, and `decision_options_suppressed`.
  - Any non-waivable structural finding blocks
    `ready_for_bogdan_page_complete_decision` and suppresses "complete ok" as a
    decision option.
  - Findings need stable IDs, rule refs, severity, waiver eligibility, affected
    units/crops/regions, evidence refs, and readiness-blocking behavior.
  - Additional finding classes include `missing_caption_unit`,
    `table_structure_flattened`, `stat_block_flattened`,
    `callout_container_unresolved`, `visual_text_unclassified`,
    `context_only_decision_missing`, `duplicate_container_child_text`,
    `unknown_unit_without_blocker`, `stale_semantic_taxonomy`,
    `unauthorized_text_source`, `pdf_text_layer_leakage`,
    `ocr_execution_leakage`, and `render_execution_leakage`.
- Test and fixture expansion:
  - Add negative tests proving readiness and decision options are blocked by
    each non-waivable structural finding.
  - Test report JSON, markdown projection integrity, manifest inclusion/hashes,
    decision-option suppression, stale evidence, and authorization boundaries.
  - Add generic synthetic fixtures independent of Viral IDs for mixed
    heading/body/quote crops, column/page continuations, TOC rows with page
    refs, visual-only art, art+caption, tables, sidebars/callouts, stat/card
    blocks, page markers, context-only insets, and unsupported/unknown regions.
- Contract and sync surfaces:
  - Sync `pre_ocr_mapping_model.md`, `gate_01_qualification_protocol.md`,
    `contracts/reconstruct.md`, quality/acceptance surfaces, roadmap node
    `gate-01-page-map-readiness-pipeline`, page-complete acceptance logic,
    report JSON, packet Markdown, manifest hashes, tests, and status docs.
  - Store only IDs/hashes/status in roadmap/status rollups; keep semantic
    payloads in artifacts.
  - Add vocabulary such as `semantic_map_ready`, `semantic_map_blocked`, and
    `semantic_unit_review_only`.
- P006-002 exit criteria:
  - Fresh bounded authorization names exact inputs, outputs, limits,
    schema/taxonomy versions, script/test hashes, stale rules, and predecessor
    hashes.
  - Schema passes; structural findings are empty or only explicitly allowed
    advisory findings.
  - Old P006 packet remains held/superseded; new manifest includes the semantic
    map artifact.
  - Sol/Terra review completes before Bogdan is asked for any P006 decision.
  - If validation fails, the generated packet must not expose `page 006
    complete ok` as an available reply.

Step 2 implementation checkpoint:

- Added reusable semantic-unit contract primitives in
  `scripts/page_review_semantic_units.py`.
- Schema version: `page_review_semantic_units.v1`.
- Taxonomy version: `sourcefold_page_review_taxonomy.v1`.
- Controlled registries now exist for:
  - `unit_type`: heading, paragraph, quote, list/list item, table/table
    row/table cell, callout, sidebar, card, stat block, stat label/value, art,
    caption, page marker, continuation, unknown unsupported, and unclassified
    bounded units.
  - `unit_scope`: in-scope text, context-only, visual-only, excluded, unknown,
    and blocked.
  - `display_style`: headings, body, quote, list, table, callout/sidebar/card,
    stat, caption, page marker, visual art, and unknown styles.
  - `source_role`: accepted source block, human-verified span, draft review
    span, existing OCR raw, profile override, visual context, not applicable,
    and unknown.
  - `block_role`: title, text column, body, list, table, art, caption, callout,
    sidebar, card, stat block, page marker, context, excluded, and unknown
    regions.
  - `text_source_state`: accepted source, human verified, draft review text,
    existing OCR raw, and not applicable.
  - `review_state`: ready, blocked, context-only, visual-only, excluded, and
    unknown.
- Validator now emits stable finding records with rule ids, severity, waiver
  status, affected unit id, and message.
- Current validator blockers include stale/unknown schema, stale taxonomy,
  unknown unit type, invalid heading level, invalid unit scope, unknown unit
  without blocked/unknown scope, unauthorized text source, invalid review
  state, invalid or empty cardinality, invalid or non-contiguous reading order,
  duplicate unit id, and broken or mistyped parent/container/continuation links.
- This step intentionally does not yet rebuild the human text map from
  semantic units or generate `PCRP-G1-VIRAL-P006-002`.
- Current reproducibility hashes:
  - `scripts/page_review_semantic_units.py` SHA-256:
    `244988545C3D99063B1539E102AD2B58D37CD56F0460E97D7016519E6E067D4B`
  - `tests/test_page_complete_review.py` SHA-256:
    `848A680A6D3D8DC0C98B787720330BAA0D9BA2AD7E4718E008EBD0798CBDA40A`
  - `page_complete_review_report.json` SHA-256:
    `09402EE26A1167986FC04DA6F08D5823D8CBA367BE8EC28A3C3BC7E7B2FB4A1A`
  - `page_complete_review_manifest.md` SHA-256:
    `C328799E8891D9A19D8856A730D7AA23FD0B842D9C29E001FFCA4A1A8CAEEDEC`

Step 3 implementation checkpoint:

- Added canonical semantic map document/projection primitives in
  `scripts/page_review_semantic_units.py`.
- `semantic_map_document` returns a canonical JSON-like document with map id,
  package id, page, schema/taxonomy versions, ordered units, semantic
  validation, structural findings, and explicit `not_evidence_for` boundaries.
- `build_semantic_map_markdown` is a projection only. It renders:
  - metadata-only unit summary table;
  - stable per-unit sections;
  - one dynamically fenced full-text block per unit;
  - structural findings;
  - "Not Evidence For" boundaries.
- `validate_semantic_map_markdown` checks summary table row/column integrity,
  rejects long prose inside summary cells, scopes table parsing to the unit
  summary section, ignores table-like content inside fenced unit text, and
  requires one well-formed fenced text block per semantic unit inside the Unit
  Text section.
- This step intentionally leaves the current P006-001 legacy text map blocked;
  P006-002 is still blocked until builder integration, filling rules, full
  validation, and regression fixtures are complete.
- Current reproducibility hashes:
  - `scripts/page_review_semantic_units.py` SHA-256:
    `FDCE7477E6E4B330185FD56558B2F02E3BF8F586C63DD60740344BF47603CADB`
  - `tests/test_page_complete_review.py` SHA-256:
    `9479FB6543186ADD3E94777FCE6625CCF4365CC20C466FCEF79F85EB1A3CC027`
  - `page_complete_review_report.json` SHA-256:
    `8F24BD8009F4B212D9974AAA5E2A952792188A4DB9F4B651C1164457BF68ABFC`
  - `page_complete_review_manifest.md` SHA-256:
    `56B97199F136566199EDCE245AEABED4918751E3E1A1623923D67664AF6A20D0`

Step 4 implementation checkpoint:

- Added reusable page-inventory filling/reconciliation predicates in
  `scripts/page_review_semantic_units.py`.
- Region decisions are now controlled as `represented`, `absent`,
  `context_only`, `visual_only`, `excluded`, `unknown`, and `blocked`.
- `reconcile_page_inventory` blocks:
  - represented inventory regions without classified `in_scope_text` semantic
    units;
  - regions missing explicit decisions;
  - unknown/blocked regions without an unknown/unclassified bounded unit;
  - unknown/blocked regions that also contain classified `in_scope_text` units;
  - semantic units that reference source regions outside the inventory;
  - represented regions missing expected unit types.
- Focused tests cover represented/context inventory, missing represented units,
  missing decisions, unknown fallback, external region refs, and expected unit
  type coverage.
- This step intentionally does not yet wire reconciliation into
  `build_page_complete_review.py` or generate `PCRP-G1-VIRAL-P006-002`.
- Current reproducibility hashes:
  - `scripts/page_review_semantic_units.py` SHA-256:
    `C5C9953465D77F35BD4E9428A940AF5D1942671256449852FAEDEDB2E73F580E`
  - `tests/test_page_complete_review.py` SHA-256:
    `628F8F1ED1019E822A2E6C6CAC59A356F43009D0048F6879939F5322C8AD11F5`
  - `page_complete_review_report.json` SHA-256:
    `485DACF3D45B61EFCA56353D0D6EB735EE7057902446EC0FC77B8F60931B7E74`
  - `page_complete_review_manifest.md` SHA-256:
    `EB18047D13ECBDB2750B7A890B7A468F75033C5818EC3626C60C5A3B0E0B5067`

Step 5 implementation checkpoint:

- Wired `build_page_complete_review.py` to emit semantic map artifacts for
  inline readiness spans.
- P006-001 now packages:
  - `review_assets/page_006_semantic_text_map.json`
  - `review_assets/page_006_semantic_text_map.md`
- Semantic unit IDs are stable and derived from block/span order.
- Semantic units include source region IDs, crop attachment IDs, source block
  IDs, span IDs, evidence predecessors, text source state, display style, block
  role, review state, and heading level where applicable.
- Report attachment entries include semantic validation and Markdown projection
  validation state.
- The legacy P006-001 OCR/verified text map remains blocked negative evidence;
  P006-001 remains held/blocked and `PCRP-G1-VIRAL-P006-002` is not generated.
- Current reproducibility hashes:
  - `scripts/build_page_complete_review.py` SHA-256:
    `B9752EAFC2E4EA713B0DFB2DB04A5B5B3616AAF30ED9A40415A8C8D29C3ACC96`
  - `scripts/page_review_semantic_units.py` SHA-256:
    `C5C9953465D77F35BD4E9428A940AF5D1942671256449852FAEDEDB2E73F580E`
  - `tests/test_page_complete_review.py` SHA-256:
    `CB4CD070C61FB2C6E12E7D33EC142CC2D582338B472D1E020DC88E71D47C3652`
  - `page_complete_review_report.json` SHA-256:
    `C0C9BCAF65B1E693FE354575821BA4DC5C76A97B15BF0470BB4A9779BB6D5C21`
  - `page_complete_review_packet.md` SHA-256:
    `7604F9B229B62466F6B520B28E06D049B9FDD59265EEF9FE1968DC475A6D102C`
  - `page_complete_review_summary.md` SHA-256:
    `3BEA231DC745C215B87ECF4D66E66E232E44CFC5B40E5BA0A445EB9E33A32DB2`
  - `page_complete_review_manifest.md` SHA-256:
    `BF91B1B7C4E0C8027C31F21A052C9461BFBA3158928FBA457512128CF724BC02`
  - `page_006_semantic_text_map.json` SHA-256:
    `D86CD775F274CC51B403C60FCBEE348EFC491AA8DD7F5FBEC330C383BCE2D01B`
  - `page_006_semantic_text_map.md` SHA-256:
    `E64916B12E6F34411E9DF4DC67EFF5817068D60030C8BEEBCFD1A1263013E7A8`

Step 6 implementation checkpoint:

- Promoted semantic validation and Markdown projection validation from
  attachment metadata into page-complete report/packet/summary routing.
- Report fields now include:
  - `semantic_units_validated`
  - `semantic_validation`
  - `markdown_projection_validation`
  - `structural_findings`
- `semantic_validation_blocker` is added before decision options when semantic
  validation is readiness blocked.
- `markdown_projection_validation_blocker` is added before decision options
  when Markdown projection validation is readiness blocked.
- The human packet now includes a "Semantic Map Validation" section with
  validation states and structural findings.
- P006-001 remains held/blocked and now exposes both the semantic validation
  blocker and the Bogdan hold blocker; P006-002 is not generated.
- Current reproducibility hashes:
  - `scripts/build_page_complete_review.py` SHA-256:
    `EEB41886B409FF17FEC209CE42503F0A90394F033D47F817ADF8E2EFAB15AF73`
  - `tests/test_page_complete_review.py` SHA-256:
    `EC72C0C750F148723CC85EE52BC79F3327D2B8DA6E6A5B4964BC554D18D8A75F`
  - `page_complete_review_report.json` SHA-256:
    `BEBEBEFC7B8E4F8B8AD51627DC5A07CDE9B6084900037B4B11B0E385A00A637C`
  - `page_complete_review_packet.md` SHA-256:
    `80B1CCCAFECA63B7BA9C294D02ED3D7EF1300669D8D15E36370D084180920165`
  - `page_complete_review_summary.md` SHA-256:
    `2C556CC751E36E2ED1ECFF938C1076D7E8957ABF1CAE5A5536FE27BD43C8E428`
  - `page_complete_review_manifest.md` SHA-256:
    `283C797C3FED9CBD3BB7B5AD73E3E6ED1B778BD8CFF57E877E953E16AA4E3EE6`

Step 7 implementation checkpoint:

- Page-inventory reconciliation is now wired into generated report readiness
  gating.
- The builder derives inventory records from readiness blocks and declared
  context-only regions.
- The builder reads semantic units from the canonical semantic map JSON
  artifact and keeps semantic payload out of status/roadmap rollups.
- `page_complete_review.inventory_reconciliation` records the reconciliation
  result.
- `inventory_reconciliation_blocker` is added before decision options when
  reconciliation has non-waivable blocker findings.
- P006-001 inventory reconciliation is valid; P006-001 remains held/blocked by
  `semantic_validation_blocker` for `invalid_heading_level` plus the Bogdan
  hold blocker.
- P006-002 is not generated and no page/Gate/fixture/source acceptance is
  created.
- Current reproducibility hashes:
  - `scripts/build_page_complete_review.py` SHA-256:
    `8C607CE438348F3692CAAFBF2274EA8CCF017B9703F1C5A1CD51DD79D38C0612`
  - `tests/test_page_complete_review.py` SHA-256:
    `35321D37E70C609BC369C5B7CA7BA9D7CA8172D3A1C26422038445BF0EB10CE0`
  - `page_complete_review_report.json` SHA-256:
    `6D2B33BCEABFB95A9923F470C2F84BE72AD3C7AEEE2E9BC64CA407A9B1CBABE5`
  - `page_complete_review_packet.md` SHA-256:
    `AF8A4B77412BDDBF9DBA972B59111EE7CB61C04B4A9AAE35E19497C9F9D1965B`
  - `page_complete_review_summary.md` SHA-256:
    `CC9F1A1D7B2717501EE0F5C64E71E98D154AEEE9A7832FF78DD7948F2ACB11DD`
  - `page_complete_review_manifest.md` SHA-256:
    `E55F2D85DDE39FF582AB83410E40898E7E204FE7E863629832C28F5429028E36`

Step 8 implementation checkpoint:

- Negative structural guards were strengthened before P006-002 generation.
- `style_is_block_role` blocks display styles that are actually source/page
  block roles.
- `collapsed_units` blocks a represented region that expects multiple semantic
  unit types but is represented by one unit.
- `missing_expected_heading` and `quote_flattened` block swallowed heading and
  quote expectations.
- Tests now prove these findings are readiness-blocking and that P006-001
  still suppresses `accept_page_006` routing while structural findings exist.
- This checkpoint does not generate P006-002 and creates no page/Gate/fixture
  or source acceptance.
- Current reproducibility hashes:
  - `scripts/page_review_semantic_units.py` SHA-256:
    `3F8C81EB0825EC68120A28A44101732AEC56DCDFEE28A578E41C78E73F533955`
  - `scripts/build_page_complete_review.py` SHA-256:
    `8C607CE438348F3692CAAFBF2274EA8CCF017B9703F1C5A1CD51DD79D38C0612`
  - `tests/test_page_complete_review.py` SHA-256:
    `3FB0CD0CE0EBA97414FA2203E68874B59050D85C676905A4F8662EEF7212E2A7`
  - `page_complete_review_report.json` SHA-256:
    `6D2B33BCEABFB95A9923F470C2F84BE72AD3C7AEEE2E9BC64CA407A9B1CBABE5`
  - `page_complete_review_packet.md` SHA-256:
    `AF8A4B77412BDDBF9DBA972B59111EE7CB61C04B4A9AAE35E19497C9F9D1965B`
  - `page_complete_review_summary.md` SHA-256:
    `CC9F1A1D7B2717501EE0F5C64E71E98D154AEEE9A7832FF78DD7948F2ACB11DD`
  - `page_complete_review_manifest.md` SHA-256:
    `E55F2D85DDE39FF582AB83410E40898E7E204FE7E863629832C28F5429028E36`

Step 9 implementation checkpoint:

- Mixed-layout regression coverage was added before P006-002 generation.
- `page_ref` is now a controlled semantic unit/display style for TOC-like
  page references.
- Represented inventory regions may be covered by `in_scope_text`,
  `visual_only`, or `context_only` units when those units satisfy expected
  semantic unit types.
- Visual/context-only region decisions may carry visual/context scoped units
  while still blocking in-scope text leakage.
- Synthetic regression coverage now includes TOC rows/page refs, art+caption,
  table row/cell structure, callout/sidebar/card/stat units, visual-only page
  markers, context-only insets, and unknown unsupported regions.
- Topology-flattening blockers now require table rows/cells, stat labels/values,
  and callout/sidebar/card containers to expose linked structure instead of
  passing as flat type lists.
- This checkpoint does not generate P006-002 and creates no page/Gate/fixture
  or source acceptance.
- Current reproducibility hashes:
  - `scripts/page_review_semantic_units.py` SHA-256:
    `F49E71E85A2DF86F7C9C96E10A5D474E369620F996B331CBFD5FF82BDF47A7A5`
  - `scripts/build_page_complete_review.py` SHA-256:
    `8C607CE438348F3692CAAFBF2274EA8CCF017B9703F1C5A1CD51DD79D38C0612`
  - `tests/test_page_complete_review.py` SHA-256:
    `41F677D1CED7D367F56CF8A4047701CEA9BA37D412FD923F66227CE451A797A7`
  - `page_complete_review_report.json` SHA-256:
    `6D2B33BCEABFB95A9923F470C2F84BE72AD3C7AEEE2E9BC64CA407A9B1CBABE5`
  - `page_complete_review_packet.md` SHA-256:
    `AF8A4B77412BDDBF9DBA972B59111EE7CB61C04B4A9AAE35E19497C9F9D1965B`
  - `page_complete_review_summary.md` SHA-256:
    `CC9F1A1D7B2717501EE0F5C64E71E98D154AEEE9A7832FF78DD7948F2ACB11DD`
  - `page_complete_review_manifest.md` SHA-256:
    `E55F2D85DDE39FF582AB83410E40898E7E204FE7E863629832C28F5429028E36`

Step 10 contract-sync checkpoint:

- Readiness/page-complete contracts were synchronized after semantic-map
  validator/report/inventory/regression hardening.
- New contract vocabulary:
  - `semantic_map_ready`
  - `semantic_map_blocked`
  - `semantic_unit_review_only`
- Canonical semantic-map JSON is the authoritative semantic review artifact;
  Markdown is a generated projection only.
- Page-complete review must run semantic validation, Markdown projection
  validation, inventory reconciliation, and structural finding roll-up before
  report status, manifest/status sync, blocker roll-up, and decision-option
  filtering.
- Non-waivable structural findings suppress complete-ok/acceptance routing.
- Status and roadmap surfaces may record IDs, states, and hashes only; they
  must not store semantic payloads.
- This checkpoint does not generate P006-002 and creates no page/Gate/fixture
  or source acceptance.
- Current contract-surface reproducibility hashes:
  - `docs/quality/acceptance_criteria.md` SHA-256:
    `3B5DC180BB0E668ECE5A8C6B3D6AE0F542827AB6352BB2AD895647CA8A1F56A9`
  - `pre_ocr_mapping_model.md` SHA-256:
    `DAC39E856E20D2F26D2DE916C58596BD324C4C98D70E173A448D23C002FA7BC4`
  - `gate_01_qualification_protocol.md` SHA-256:
    `95EA89906E5AEC5903326CBB2135CDC7D96AFB32936A57ECB0C794E622D1621F`
  - `core_0_1_acceptance_matrix.md` SHA-256:
    `BE8998EAF6A318AEAC65B3F2107281F54CE412E2BB722DA5900C9DDDAEABFAEF`

Allowed outputs for this planning checkpoint:

- Status/roadmap/plan/context documentation that records this goal and next
  bounded continuation.
- A commit containing the current documented Sourcefold state.

Future implementation outputs, pending the next execution step:

- Updates to `scripts/build_page_complete_review.py`.
- Optional new validator/helper script if the builder becomes too broad.
- Updates to `tests/test_page_complete_review.py` or a focused semantic-map
  validator test.
- Updates to reconstruct/quality/readiness contract surfaces as needed.
- A superseding P006 review package only after hardening is implemented.

Limits:

- This planning checkpoint does not accept page 006 as complete.
- This checkpoint does not accept page 005 or any other page.
- This checkpoint does not accept whole Gate 1.
- This checkpoint does not create fixture admission.
- This checkpoint does not create or mutate source acceptance.
- This checkpoint does not translate, proofread, accept renderer/profile
  behavior, implement runtime behavior, push, parse or inspect the PDF or PDF
  text layer, rerender the PDF, run OCR, mutate raw artifacts, or broaden the
  review scope beyond documented page-complete review hardening.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-004

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P005-004`

Created: 2026-07-24

Authority: Bogdan Telegram message `1022`: "ок делай 5 сразу и коммит" after
reviewing the canonical P005 state and the need for a compatibility refresh
against the current semantic-map page-complete contract.

Exact action:

- Consume the current readable page 005 review evidence from
  `PCRP-G1-VIRAL-P005-003`.
- Prepare a compatibility refresh page 005 review packet with canonical
  semantic-map JSON, Markdown projection validation, and inventory
  reconciliation.
- Reuse existing rendered page image and existing P005-003 verified text/crop
  evidence only.
- Create no acceptance in this review packet.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_004/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_004/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_004/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_004/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p005_G1_VIRAL_004/review_assets/`.
- Status/roadmap/plan/context documentation sync that records the refreshed
  review packet.

Limits:

- Do not accept page 005 as complete in this review packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Output status:

- Package id: `PCRP-G1-VIRAL-P005-004`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `E9D92A31D3640B01802186677E096B8731DE7BDCF48E19860C22E4C88C7ABD6A`
- Page complete review test SHA-256:
  `7DCA5E1FF09116BA795615A255CE7721B856922DB2A0A27AA3AD492E792B9AA0`
- Page 005 semantic refresh review report SHA-256:
  `65A9967D4E135A2BB590A4736304456701BC4EE4EFC275BE7C45DDB5CDB0C33A`
- Page 005 semantic refresh review packet SHA-256:
  `102CC672F4C61DF20DE565D40D08A8120ACD873B4ADB781699CCAA427E7CE9AA`
- Page 005 semantic refresh review summary SHA-256:
  `4D85437FDE246213EF35420960AC3A26C02D3339521350C89D1B3B309D549711`
- Page 005 semantic refresh review manifest SHA-256:
  `0AE926CE376BD9E9C834358C7F537BD96F19B0866DF7D4666CA4E65DEF770111`
- Result: page 005 has 2/2 ready blocks, 74 semantic units, valid semantic
  validation, valid Markdown projection, valid inventory reconciliation, and
  zero structural findings.
- Page 005 is not accepted as complete by this review packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR/render/PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-001

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P007-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `1048`: "план ок, но сначала фул 7 потом
фул 8 , потом гейт. не надо смешивать 7 и 8 вместе."

Exact action:

- Prepare a page 007 page-complete review packet only, using the existing
  `RT-G1-VIRAL-RENDER-001` rendered page image.
- Package page 007 human-review crops, verified text map, canonical semantic
  map JSON, Markdown projection validation, and inventory reconciliation.
- Keep page 008 out of scope except for marking page 007 text that visibly
  continues beyond the page boundary as a continuation marker.
- Create no acceptance in this review packet.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_001/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_001/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_001/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_001/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p007_G1_VIRAL_001/review_assets/`.
- Status/roadmap/plan/context documentation sync that records the page 007
  review packet.

Limits:

- Do not accept page 007 as complete in this review packet.
- Do not process page 008 under this authorization.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Output status:

- Package id: `PCRP-G1-VIRAL-P007-001`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `DE5B6F128DA3E93EB79894D1A6174521B8F6E177CE7B86754B8D21AC08C02F89`
- Page complete review test SHA-256:
  `AF46DD65E51445B36EAE2261AA4355692644926BD0C820E450868479C0558949`
- Page 007 review report SHA-256:
  `C41BEC3180125CCEEB3966C652E749E7A58AB3EFB7DB88A117A6B53A9EBA2A3B`
- Page 007 review packet SHA-256:
  `B7C1D6FCF877931F3466E6987EEB2172E750D88CAB9A025DD316906E8BD8B0C9`
- Page 007 review summary SHA-256:
  `EA0A137248C992404CD566B63ED9FD525E07F89F595C3CF3F1CFFC05019CCB06`
- Page 007 review manifest SHA-256:
  `3644D74B1D2716969FD927C827B81C2D29D03730377C1CA209DFE60A6331577D`
- Result: page 007 has 4/4 ready blocks, 11 semantic units, valid semantic
  validation, valid Markdown projection, valid inventory reconciliation, and
  zero structural findings.
- Post-review disposition: held by Bogdan for art-anchor and block/unit
  modeling corrections; superseded by `PCRP-G1-VIRAL-P007-002`.
- Page 007 is not accepted as complete by this review packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR/render/PDF parsing,
  PDF text-layer extraction, page 008 processing, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-002

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P007-002`

Created: 2026-07-24

Authority: Bogdan Telegram messages `1077` and `1080`: hold page 007 because
the upper Spektral Krew visual block must be modeled as an art anchor rather
than parsed source text, and the Marco Proudfoot heading must be a semantic unit
inside the left-column text block rather than a separate duplicated page block;
then "ок. делай".

Exact action:

- Prepare a superseding page 007 page-complete review packet only:
  `PCRP-G1-VIRAL-P007-002`.
- Record the upper Spektral Krew visual/UI area as a deferred art anchor with
  identifying metadata, not as accepted source text.
- Model the left article column as one text block containing both the heading
  unit and body unit.
- Keep the right article column as continuation text.
- Keep page 008 out of scope.
- Create no acceptance in this review packet.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_002/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_002/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_002/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_002/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p007_G1_VIRAL_002/review_assets/`.
- Status/roadmap/plan/context documentation sync that records the page 007 hold
  and superseding packet.

Limits:

- Do not accept page 007 as complete in this review packet.
- Do not process page 008 under this authorization.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Output status:

- Package id: `PCRP-G1-VIRAL-P007-002`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `81D164E0054694C1E77792D5E16E2C139DBAB4E0643A80EA54B1767B2D0D46C2`
- Page complete review test SHA-256:
  `67F0289E84DE99D9B732E2F19BF1B44B0F9FE8293610CC3B42F62DCFFB370065`
- Page 007 superseding review report SHA-256:
  `40BE32B1F1F96B65B26D3447F08412070A86FA7FF75ECB18E63B6B16DE6BAB5F`
- Page 007 superseding review packet SHA-256:
  `E1B198E5E0BC90518EB2F58736FF37D1CE6070294F0B251FD93332899D8041E4`
- Page 007 superseding review summary SHA-256:
  `18BD02883E3B64902D3D056A8BAD3E952F0AAE1ADA71196EDAE5E3606A9FA064`
- Page 007 superseding review manifest SHA-256:
  `009CFBEBF9A0902549D5880A100700F7771C357A68C1F225FA7AFA56CF576914`
- Result: page 007 has 3/3 ready blocks, one deferred `ui_art_anchor`, 3
  text semantic units, valid semantic validation, valid Markdown projection,
  valid inventory reconciliation, and zero structural findings.
- Post-review disposition: held by Bogdan for paragraph-boundary flattening;
  superseded by `PCRP-G1-VIRAL-P007-003`.
- Page 007 is not accepted as complete by this review packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR/render/PDF parsing,
  PDF text-layer extraction, page 008 processing, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-003

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P007-003`

Created: 2026-07-24

Authority: Bogdan Telegram message `1100`: hold page 007 and apply the rule
that semantic body units must not merge separate source paragraphs; if a crop
shows paragraph breaks, they must be represented as separate paragraph units or
explicit paragraph-boundary metadata. Bogdan confirmed the three crops are OK:
the first is art, and blocks 2 and 3 need paragraph restoration.

Exact action:

- Prepare a superseding page 007 page-complete review packet only:
  `PCRP-G1-VIRAL-P007-003`.
- Preserve the three-block/crop model from `PCRP-G1-VIRAL-P007-002`.
- Keep the upper Spektral Krew visual/UI area as a deferred art anchor.
- Split left and right article text into paragraph-preserving semantic units.
- Keep page 008 out of scope; record only the visible page-boundary condition
  on the final page 007 paragraph.
- Create no acceptance in this review packet.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_003/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_003/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_003/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p007_G1_VIRAL_003/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p007_G1_VIRAL_003/review_assets/`.
- Status/roadmap/plan/context documentation sync that records the page 007 hold
  and superseding packet.

Limits:

- Do not accept page 007 as complete in this review packet.
- Do not process page 008 under this authorization.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Output status:

- Package id: `PCRP-G1-VIRAL-P007-003`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `52C0C2297C5FD34B07EFFCB8C45FF87FACE9014EE0CC418279B636863569F386`
- Page complete review test SHA-256:
  `24D9F102E46473D09342832C8A53053450810CB960FEDFDC12A239C85B9E951B`
- Page 007 paragraph-preserving review report SHA-256:
  `6A88256EBA758EF8A03FE1B9F53FACDB288C05311BCE3AC35FFB662A88E1C851`
- Page 007 paragraph-preserving review packet SHA-256:
  `65E288DE2763C6D235928E24FE86553B384C8DD7BED129915244AFDF8335B2B1`
- Page 007 paragraph-preserving review summary SHA-256:
  `8B07975E1D0413D5824DBF641C11664456E2947A3B610D688F87B8AE85331372`
- Page 007 paragraph-preserving review manifest SHA-256:
  `74CB0FC4D5BF8449AE4E843B1E86B30E1BE67CEE673F1B03A564DAE64F031676`
- Result: page 007 has 3/3 ready blocks, one deferred `ui_art_anchor`, 7
  text semantic units preserving visible paragraph breaks, valid semantic
  validation, valid Markdown projection, valid inventory reconciliation, and
  zero structural findings.
- Page 007 is not accepted as complete by this review packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR/render/PDF parsing,
  PDF text-layer extraction, page 008 processing, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P007-001

Status: `expired`; scope consumed by `P007PCA-G1-VIRAL-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `1118`: "page 007 complete ok".

Exact action:

- Consume exact `PCRP-G1-VIRAL-P007-003` page-complete review evidence after
  Bogdan accepted its art-anchor, block, crop, and paragraph-preserving
  semantic-unit model.
- Create a separate page-complete acceptance record for page 007 only.
- Record Bogdan's explicit page 007 complete decision as the human acceptance
  basis.

Allowed outputs:

- `scripts/accept_page_007_complete.py`
- `tests/test_page_007_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p007_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p007_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p007_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p007_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan/context documentation sync that records page 007
  page-complete acceptance only.

Limits:

- Accept page 007 as complete only.
- Do not accept page 008 or any other page through this record.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to another
  page without separate bounded authorization.

Output status:

- Package id: `P007PCA-G1-VIRAL-001`
- Status: `page_007_complete_accepted`
- Page 007 complete acceptance script SHA-256:
  `22A3D502338FC03AE0A2378E837561F87C065BC916A52D814EC50EB72B99DD49`
- Page 007 complete acceptance test SHA-256:
  `F724A8D3D62DAA0A5FE8CCAD78616559DB2FCADBE89D571EBD1A28B7222DF1E7`
- Page 007 complete acceptance report SHA-256:
  `8A1B163709D47D9268602C8F2EEF5F5E880E450807468DC9EB360BE8C7CC80F5`
- Page 007 complete acceptance record SHA-256:
  `541569B53203FC35B40CD68FBB3158131284FD1DC7AB307D1BAE63E5A539FDB2`
- Page 007 complete acceptance summary SHA-256:
  `E5C0F075D427167AA12A1B509A0E211B7E223E0E1170E1DB0E414C783B87FA45`
- Page 007 complete acceptance manifest SHA-256:
  `FA38D3289B923B9EC24C3999D8575E1F3888A513FC25C42A63649BB963808188`
- Result: page 007 is accepted as complete only.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, page 008 processing, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P005-001

Status: `expired`; scope consumed by `P005PCA-G1-VIRAL-001`

Created: 2026-07-24

Authority: Bogdan Telegram message `1022`: "ок делай 5 сразу и коммит".

Exact action:

- Consume exact `PCRP-G1-VIRAL-P005-004` page-complete review evidence after
  semantic-map compatibility refresh.
- Create a separate page-complete acceptance record for page 005 only.
- Record Bogdan's explicit page 005 complete decision as the human acceptance
  basis.

Allowed outputs:

- `scripts/accept_page_005_complete.py`
- `tests/test_page_005_complete_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p005_G1_VIRAL_001/page_complete_acceptance_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p005_G1_VIRAL_001/page_complete_acceptance_record.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p005_G1_VIRAL_001/page_complete_acceptance_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_acceptance_p005_G1_VIRAL_001/page_complete_acceptance_manifest.md`
- Status/roadmap/plan/context documentation sync that records page 005
  page-complete acceptance only.

Limits:

- Accept page 005 as complete only.
- Do not accept page 006 or any other page through this record.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this acceptance to another
  page without separate bounded authorization.

Output status:

- Package id: `P005PCA-G1-VIRAL-001`
- Status: `page_005_complete_accepted`
- Page 005 complete acceptance script SHA-256:
  `75390B09A3232D9C07CDA9B0B949AF818A0409ECADAE8E93941A0B3A12EF628E`
- Page 005 complete acceptance test SHA-256:
  `96E671F4DF39246E156892541FB4770B31D10FDD5039DD0FE7E5D8CCBDD3DCB0`
- Page 005 complete acceptance report SHA-256:
  `2065A5C139E42514AD92EFB897151CE87CEEEF42208B9A7F99482B7A7F923022`
- Page 005 complete acceptance record SHA-256:
  `2A5E5CC65ABCACA348E0D13002C23770A185E09E066C5CCB63E10CCB093BDE16`
- Page 005 complete acceptance summary SHA-256:
  `5650BE44D46B09FFA709B03935A4BE7717C2E0935327083B2DAF1EFD3F7FB598`
- Page 005 complete acceptance manifest SHA-256:
  `7E123CC8BCFB648C4F11224D54F27011EBC08D0E6841ED4DF093F5000335457F`
- Result: page 005 is accepted as complete only.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-003

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P005-003`

Created: 2026-07-24

Authority: Bogdan Telegram message `870`: proceed in dry-run mode without
intermediate Sol/Terra stops until page 005 has correct crops and matching
OCR/verified text, then record how it was obtained and update the pipeline.

Exact action:

- Consume exact `PMRP-G1-VIRAL-P005-001` page-map readiness evidence.
- Prepare a second superseding page 005 review packet with human-readable crop
  framing.
- Reuse the existing rendered page image `page_005.png`.
- Generate exactly three primary human review crops: title only, left column,
  and right column.
- Generate an OCR/verified text map that matches crop contents and records
  heading depth/style.
- Harden the page-complete review pipeline so crop readability/framing is not
  treated as satisfied by declared-box size alone.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_003/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_003/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_003/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_003/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p005_G1_VIRAL_003/review_assets/`.
- Status/roadmap/plan documentation sync that records the superseding review
  packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P005-003`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `7FB965327838DB3F3E5E54992E23D79CD09470DF6BBFA6589DC33E01D13C0A28`
- Page complete review test SHA-256:
  `FB77F610CBA994E0C64AE22E3EB933AB7A114BF2AAB758C8F352CE93FAAE07CF`
- Page 005 readable complete review report SHA-256:
  `66BD2F602FFC004DE160A8FCD0EB01CAEF97FF6EBE0F895D98BDF185286740EB`
- Page 005 readable complete review packet SHA-256:
  `4A0767072049517DE7A78210AC12601E58C293179C66A434F7FAD8C8068BC960`
- Page 005 readable complete review summary SHA-256:
  `97F60F98DD2E2570C88748022E16759FDBD05402CEDB6EBB3D24373364AFE632`
- Page 005 readable complete review manifest SHA-256:
  `2E7A5AE902192C0F6EBBFBB329FDCDB2001B5794F912EBAE68A9F25F8AD5D0A5`
- Review assets:
  - `page_005.png`:
    `0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE`
  - `1_P005-title__contents_heading.png`:
    `BF9DB3EE3324089E478AC3FC71614EEFE6CD1CAF19355408C86BE7AA76580667`
  - `2_P005-left-column__contents_entries.png`:
    `166BA6B95F0A9D624AE0EFB9EFD490AE7A357793AABD11EAB669C4937EE0FAE7`
  - `3_P005-right-column__contents_entries.png`:
    `D22D0FE5B8C14D8645E93CEE6BF86E8359721C0441CB7846B57F6721CBD498EA`
  - `page_005_ocr_verified_text_map.md`:
    `0EBCB8857B7AA09D0DB98BE82D7EAA407584CF03EDABCF4FED9C22DC3B17FB8E`
- Result: page 005 is ready for Bogdan's explicit page-complete decision with
  human-readable title, left-column, and right-column crops.
- Page 005 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR/render/PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

Limits:

- Do not accept page 005 as complete in this review packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, mutate raw artifacts, or broaden this review packet to another page
  without separate bounded authorization.

Invalidation:

This review packet stales if `PMRP-G1-VIRAL-P005-001`, page-complete policy,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.

## BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-002

Status: `expired`; scope consumed by `PCRP-G1-VIRAL-P005-002`

Created: 2026-07-24

Authority: Bogdan Telegram message `851`: "ок , согласен. `делай
PCRP-G1-VIRAL-P005-002`" after `PCRP-G1-VIRAL-P005-001` was blocked by
insufficient visual crop coverage.

Exact action:

- Consume exact `PMRP-G1-VIRAL-P005-001` page-map readiness evidence.
- Prepare a superseding separate page-complete review packet for page 005 only.
- Reuse the existing rendered page image `page_005.png`.
- Generate full block review crops from each declared readiness `box_px` rather
  than the old narrow crop candidates.
- Include page 005 source page image, full declared block crops, and an
  OCR/block text markdown review asset for Bogdan's human decision.
- Ask only whether a later explicit record may accept page 005 as complete.

Allowed outputs:

- Updates to `scripts/build_page_complete_review.py`.
- Updates to `tests/test_page_complete_review.py`.
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_002/page_complete_review_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_002/page_complete_review_packet.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_002/page_complete_review_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_review_p005_G1_VIRAL_002/page_complete_review_manifest.md`
- Review assets under `page_complete_review_p005_G1_VIRAL_002/review_assets/`.
- Status/roadmap/plan documentation sync that records the superseding review
  packet.

Output status:

- Package id: `PCRP-G1-VIRAL-P005-002`
- Status: `ready_for_bogdan_page_complete_decision`
- Page complete review script SHA-256:
  `33690A90D99E67350892A89BF9D3919932C1EA54778B1DEDA1393370A2F1D047`
- Page complete review test SHA-256:
  `8029E883D606DE71D3AC29DEC0DAA65042440D76076A9830C901AB3C50BF8772`
- Page 005 superseding complete review report SHA-256:
  `6CA39128FCBAE8AFA9FDA48FDE3EAEFF16BCACAB23F1CA475FE8B93983AC87AB`
- Page 005 superseding complete review packet SHA-256:
  `9F8FE784838F7FB72B3FEACB955EA6DEF9356E47C78067EA40FB0F612FC5C8AB`
- Page 005 superseding complete review summary SHA-256:
  `74EA563E295F0DDC29B64663200B03AFB78734F24EF6901DDA99AA46566C9CA6`
- Page 005 superseding complete review manifest SHA-256:
  `0B5E6DBED3CC2DBBA48A00978CE94780DA190166FA3754AC15DB73D3B7EA3DDF`
- Review assets:
  - `page_005.png`:
    `0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE`
  - `1_P005-B001__declared_box__PRM-G1-VIRAL-001-P005-R01.png`:
    `22DEA581294FEC32CC1095303FABE29A4AA81DA6DDA3FB10D28CBF610F50471C`
  - `2_P005-B002__declared_box__PRM-G1-VIRAL-001-P005-R02.png`:
    `E1C92BCC9D6E583FF1C8E57656B0F2F284E8AF8619B64E8CA16F328AB9CB3B08`
  - `page_005_ocr_block_text.md`:
    `4C14CA5A17CBE5BC1058D0B075F83C291FCFB0578333D6C51E488DFDCFE40875`
- Result: page 005 is ready for Bogdan's explicit page-complete decision.
- Page 005 is not accepted as complete by this packet.
- Whole Gate 1 is not accepted.
- Fixture admission, source acceptance mutation, translation, proofreading,
  renderer/profile acceptance, implementation, push, OCR, render, PDF parsing,
  PDF text-layer extraction, and raw mutation remain false.

Limits:

- Do not accept page 005 as complete in this review packet.
- Do not accept whole Gate 1.
- Do not create fixture admission.
- Do not create or mutate source acceptance.
- Do not translate, proofread, accept renderer/profile behavior, implement
  runtime behavior, push, parse or inspect the PDF or PDF text layer, rerender
  the PDF, run OCR, mutate raw artifacts, or broaden this review packet to
  another page without separate bounded authorization.

Invalidation:

This review packet stales if `PMRP-G1-VIRAL-P005-001`, `SRHR-G1-VIRAL-001`,
`SRQA-G1-VIRAL-001`, `SRFA-G1-VIRAL-001`, page-complete policy,
reviewer/authority, script/test revision, roadmap/status state, or Sourcefold
orchestrator workflow changes.
## BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Lane: `P015BATCH-G1-VIRAL-001`

Created by: `aggressive_batch_authorization_preflight`

Authority: Bogdan Telegram message `2030`: "давай дальше страница 15 агрессивно"

Exact action:

- Create page 015 aggressive delegated-review batch artifacts.
- Generate P015TR/P015TXT/P015SEM/PCRP/P015PCA/status/batch outputs with skipped human review and Sol/Terra evidence.

Admitted inputs:

- `post_p014_status_route_packet`: `E0F15FCA01D32C95D41EBCA87D87EDCEEEE59A2C503FF0965614169BF0159B54`
- `p014_final_batch_review`: `FF8C193BB61A5D6A12F1E60EC7C853EB164CD1EC10A92A058A591200B430A76B`
- `page_015_image`: `023836CD8DF8B77073F977E22F00CA87391F96855765D77B5C2826B0F00EDBBA`

Allowed outputs:

- `scripts/build_page_015_aggressive_batch.py`
- `tests/test_page_015_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_015_*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p015_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_010/*`

Limits:

- Do not record direct Bogdan approval for internal P015 stages.
- Do not process page 016 or later beyond the post-P015 status recommendation.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.

Final review model:

- `P015BATCH final bundle plus post-P015 status only`.
- Do not create final human batch-review acceptance before Bogdan gives the exact final bundle/status decision.

Output status:

- Batch id: `P015BATCH-G1-VIRAL-001`
- Status: `final_human_review_accepted`
- Builder script SHA-256:
  `AEC18E25E3E7DFA544B31FFC27A219DEA96BAC3CF62AA11BCC46413DC533F8CA`
- Test SHA-256:
  `5212609E7B35A7B05BCDCBED385932F1E8D938ED4757DDCEC57ECECCB3DA0BD9`
- P015 triage packet SHA-256:
  `42DDDCAEBC2D0FD90A95503C2AF7FCF1320D18C5BA1933F7E1E1CEC833E3D7C0`
- P015 text extraction packet SHA-256:
  `536BAD8BBC1D56E3C3E1DB1A1773489C8C04939331C63222484381CAFAB65D50`
- P015 semantic map JSON SHA-256:
  `D571DE8D08C08B3DC2167B3E6A89B24A406B4ACE5A24F00CC39B3645BD858A41`
- P015 PCRP report SHA-256:
  `819CECCA8031F1F1064BCBB578C2AE1AA93DC99CE582F8FC9FC0D75697E93A78`
- P015 delegated page-complete acceptance report SHA-256:
  `BDE3B2E95EB62040D9F65C7276068A40C14C081EA5C587654912E95886372AB3`
- Post-P015 status packet SHA-256:
  `D340D6D2FEAF561B60EC6ED9329104D5700D262C55AA8DB03EACBDA3B17D05D3`
- Batch report SHA-256:
  `B3FFBC67FDB16DFFF11D76D253697F80378D9753D195C6275A7A095FC4990550`
- Final review id: `P015BATCHREV-G1-VIRAL-001`
- Final review script SHA-256:
  `33F2CF94DB02A5DD8ED07B5913788B9638C6DA0D580208673C59AECB1FF3BBBD`
- Final review test SHA-256:
  `ED75D15A3C42020D0A97E08B640D2BDAF558D6EB5CD5B05AEB0A19CC00399FB4`
- Final review report SHA-256:
  `D409636B5193535B8E2BD496083E9345C4C4526EEEDD68A4669C36C6886BB219`
- Result: page 015 aggressive batch final human review accepted with
  `p015 aggressive batch ok`.
- Internal P015TR/P015TXT/P015SEM/PCRP/P015PCA stages record
  `human_review_skipped_by_explicit_authorization` and Sol/Terra delegated
  review, not direct Bogdan per-stage approval.
- Final review target was the batch plus `G1SP-G1-VIRAL-010`; this final
  review acceptance does not convert internal stages into direct Bogdan
  per-stage approvals.
## BA-G1-VIRAL-PAGE-016-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Lane: `P016BATCH-G1-VIRAL-001`

Created by: `aggressive_batch_authorization_preflight`

Authority: Bogdan Telegram message `2066`: "ок, тогда делай 16-20 агрессивно"

Exact action:

- Create page 016 aggressive delegated-review batch artifacts.
- Generate P016TR/P016TXT/P016SEM/PCRP/P016PCA/status/batch outputs with skipped human review and Sol/Terra evidence.

Admitted inputs:

- `G1SP-G1-VIRAL-010`: `D340D6D2FEAF561B60EC6ED9329104D5700D262C55AA8DB03EACBDA3B17D05D3`
- `P015BATCHREV-G1-VIRAL-001`: `D409636B5193535B8E2BD496083E9345C4C4526EEEDD68A4669C36C6886BB219`
- `page_016_image`: `7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56`

Allowed outputs:

- `scripts/build_page_016_aggressive_batch.py`
- `tests/test_page_016_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_016_*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p016_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_011/*`

Limits:

- Do not record direct Bogdan approval for internal P016 stages.
- Do not process page 017 or later beyond the bounded sequential run/status recommendation.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.

Final review model:

- `P016BATCH final bundle plus post-P016 status only`.
- Do not create final human batch-review acceptance before Bogdan gives the exact final bundle/status decision.

Run output status:

- `P016BATCH-G1-VIRAL-001`: `921A63EF578E23D388A8F232B760E46270D91911399142894117502143A3DD67`
- `G1SP-G1-VIRAL-011`: `0E3B3B1AAECE17F0FC7A0287FEFFB5CBEF822FE281880C3051D0E7C043674022`
- Final human review is pending; no `P016BATCHREV-*` artifact exists yet.

## BA-G1-VIRAL-PAGE-017-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Lane: `P017BATCH-G1-VIRAL-001`

Created by: `aggressive_batch_authorization_preflight`

Authority: Bogdan Telegram message `2066`: "ок, тогда делай 16-20 агрессивно"

Exact action:

- Create page 017 aggressive delegated-review batch artifacts.
- Generate P017TR/P017TXT/P017SEM/PCRP/P017PCA/status/batch outputs with skipped human review and Sol/Terra evidence.

Admitted inputs:

- `G1SP-G1-VIRAL-011`: `0E3B3B1AAECE17F0FC7A0287FEFFB5CBEF822FE281880C3051D0E7C043674022`
- `P016BATCH-G1-VIRAL-001`: `921A63EF578E23D388A8F232B760E46270D91911399142894117502143A3DD67`
- `page_017_image`: `1198CBB7D55877B31FEEA3E32CD95EABEB504A4610CA98D7CB2047C30142E08F`

Allowed outputs:

- `scripts/build_page_017_aggressive_batch.py`
- `tests/test_page_017_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_017_*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p017_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_012/*`

Limits:

- Do not record direct Bogdan approval for internal P017 stages.
- Do not process page 018 or later beyond the bounded sequential run/status recommendation.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.

Final review model:

- `P017BATCH final bundle plus post-P017 status only`.
- Do not create final human batch-review acceptance before Bogdan gives the exact final bundle/status decision.

Run output status:

- `P017BATCH-G1-VIRAL-001`: `5D57D75DE8B0E21F535EDAFF0E1CB67C5143FAE1FAAD83F57B04DDC24FD354A7`
- `G1SP-G1-VIRAL-012`: `2F29F2187F9273BF647BB8F28A87D12AD584A6814B03C1EA33AF7E94357DF07B`
- Final human review is pending; no `P017BATCHREV-*` artifact exists yet.

## BA-G1-VIRAL-PAGE-018-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Lane: `P018BATCH-G1-VIRAL-001`

Created by: `aggressive_batch_authorization_preflight`

Authority: Bogdan Telegram message `2066`: "ок, тогда делай 16-20 агрессивно"

Exact action:

- Create page 018 aggressive delegated-review batch artifacts.
- Generate P018TR/P018TXT/P018SEM/PCRP/P018PCA/status/batch outputs with skipped human review and Sol/Terra evidence.

Admitted inputs:

- `G1SP-G1-VIRAL-012`: `2F29F2187F9273BF647BB8F28A87D12AD584A6814B03C1EA33AF7E94357DF07B`
- `P017BATCH-G1-VIRAL-001`: `5D57D75DE8B0E21F535EDAFF0E1CB67C5143FAE1FAAD83F57B04DDC24FD354A7`
- `page_018_image`: `6E8F440CEB5F11A4081722ADF5CD65F74E622641884192390E9DA0CAE6C6BFD4`

Allowed outputs:

- `scripts/build_page_018_aggressive_batch.py`
- `tests/test_page_018_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_018_*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p018_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_013/*`

Limits:

- Do not record direct Bogdan approval for internal P018 stages.
- Do not process page 019 or later beyond the bounded sequential run/status recommendation.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.

Final review model:

- `P018BATCH final bundle plus post-P018 status only`.
- Do not create final human batch-review acceptance before Bogdan gives the exact final bundle/status decision.

Run output status:

- `P018BATCH-G1-VIRAL-001`: `7F826C3EB90D86164C0B54A4D5256A0FED57EC799DD3E9AE4248D3551E9A6160`
- `G1SP-G1-VIRAL-013`: `0163457AECBECCEEBF08EA38200E00E685F98832D67123E0ADE02AE05C037D00`
- Final human review is pending; no `P018BATCHREV-*` artifact exists yet.

## BA-G1-VIRAL-PAGE-019-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Lane: `P019BATCH-G1-VIRAL-001`

Created by: `aggressive_batch_authorization_preflight`

Authority: Bogdan Telegram message `2066`: "ок, тогда делай 16-20 агрессивно"

Exact action:

- Create page 019 aggressive delegated-review batch artifacts.
- Generate P019TR/P019TXT/P019SEM/PCRP/P019PCA/status/batch outputs with skipped human review and Sol/Terra evidence.

Admitted inputs:

- `G1SP-G1-VIRAL-013`: `0163457AECBECCEEBF08EA38200E00E685F98832D67123E0ADE02AE05C037D00`
- `P018BATCH-G1-VIRAL-001`: `7F826C3EB90D86164C0B54A4D5256A0FED57EC799DD3E9AE4248D3551E9A6160`
- `page_019_image`: `63BBB963A76F5C266E4A1B139FBCEFD2D390FB23B23CA391E8BAF12A4E9D3AC8`

Allowed outputs:

- `scripts/build_page_019_aggressive_batch.py`
- `tests/test_page_019_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_019_*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p019_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_014/*`

Limits:

- Do not record direct Bogdan approval for internal P019 stages.
- Do not process page 020 or later beyond the bounded sequential run/status recommendation.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.

Final review model:

- `P019BATCH final bundle plus post-P019 status only`.
- Do not create final human batch-review acceptance before Bogdan gives the exact final bundle/status decision.

Run output status:

- `P019BATCH-G1-VIRAL-001`: `3148F8B92D00EA70B21BB55CF73B8498F7F5E23D17214C3AE53180AE677AD5C5`
- `G1SP-G1-VIRAL-014`: `1B51D1551B68E1CA27D5D89D6B0AD8194DB5F84FFFA621B986AA2585A475E1EB`
- Final human review is pending; no `P019BATCHREV-*` artifact exists yet.

## BA-G1-VIRAL-PAGE-020-AGGRESSIVE-BATCH-001

Status: `scope_consumed`

Lane: `P020BATCH-G1-VIRAL-001`

Created by: `aggressive_batch_authorization_preflight`

Authority: Bogdan Telegram message `2066`: "ок, тогда делай 16-20 агрессивно"

Exact action:

- Create page 020 aggressive delegated-review batch artifacts.
- Generate P020TR/P020TXT/P020SEM/PCRP/P020PCA/status/batch outputs with skipped human review and Sol/Terra evidence.

Admitted inputs:

- `G1SP-G1-VIRAL-014`: `1B51D1551B68E1CA27D5D89D6B0AD8194DB5F84FFFA621B986AA2585A475E1EB`
- `P019BATCH-G1-VIRAL-001`: `3148F8B92D00EA70B21BB55CF73B8498F7F5E23D17214C3AE53180AE677AD5C5`
- `page_020_image`: `53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E`

Allowed outputs:

- `scripts/build_page_020_aggressive_batch.py`
- `tests/test_page_020_aggressive_batch.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_020_*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p020_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_015/*`

Limits:

- Do not record direct Bogdan approval for internal P020 stages.
- Do not process page 021 or later beyond the bounded sequential run/status recommendation.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.

Final review model:

- `P020BATCH final bundle plus post-P020 status only`.
- Do not create final human batch-review acceptance before Bogdan gives the exact final bundle/status decision.

Run output status:

- `P020BATCH-G1-VIRAL-001`: `BDE77046D2070A82396B6EBDA0C0DF9E5027FC8A9D4B08744C09C06BDAADD75E`
- `G1SP-G1-VIRAL-015`: `B016D09B91A5C1DA9B3E6026C9E5CF777CE290773864C786A51903FA1FCD62F8`
- Final human review is recorded by `P020BATCHREV-G1-VIRAL-001`.

## P016-P020 Aggressive Batch Final Human Review

Status: `recorded`

Authority: Bogdan Telegram message `2131`:
`p016 corrected semantic map ok; p018 corrected semantic map ok; p016-p020 aggressive batch ok`

Exact action:

- Record final human-facing review for P016-P020 aggressive batch bundles and
  their post-page status packets only.
- Preserve P016TR/P016TXT/P016SEM/PCRP/P016PCA through
  P020TR/P020TXT/P020SEM/PCRP/P020PCA as delegated Sol/Terra
  machine-reviewed stages with skipped per-stage human review.
- Record that the corrected P016/P018 semantic maps were accepted by the same
  final human decision.

Allowed outputs:

- `scripts/accept_pages_016_020_aggressive_batch_review.py`
- `tests/test_pages_016_020_aggressive_batch_final_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_016_aggressive_batch_final_review_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_017_aggressive_batch_final_review_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_018_aggressive_batch_final_review_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_019_aggressive_batch_final_review_G1_VIRAL_001/*`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_020_aggressive_batch_final_review_G1_VIRAL_001/*`

Limits:

- Do not record direct Bogdan approval for internal P016-P020 stages.
- Do not process, authorize, or accept page 021 or later.
- Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw,
  translate, proofread, implement, push, or create any broader Gate action.

Run output status:

- `P016BATCHREV-G1-VIRAL-001`: `A99DFF6580DB07F3F66303B856EA5FB7A94E215864B4112F59C71B964682FD70`
- `P017BATCHREV-G1-VIRAL-001`: `2A0ADB59F9FCA08D1DD6542842CC7C030660A2BF64512CC1C2CC386BEE6C9534`
- `P018BATCHREV-G1-VIRAL-001`: `0A563CAED4F29EF055437E952562E84AF35A4F5A894E77FA917B48BE39F7DFC8`
- `P019BATCHREV-G1-VIRAL-001`: `B4EFBECC07D519ABB51CC6197C0AF9521CBCAD269A853727542A3C91A0E63C45`
- `P020BATCHREV-G1-VIRAL-001`: `B7E024DC1C30FED09539C048182E9369354D0081C9ECA5F4A47A210D957178FB`

## BA-G1-VIRAL-POST-P020-STATUS-READINESS-001

Status: `scope_consumed`

Lane: `G1SP-G1-VIRAL-016`

Authority: Bogdan Telegram message `2137`: "запиши план в файл и двигайся по нему"

Exact action:

- Create a post-P020 Gate 1 status/readiness decision-prep packet.
- Consume `G1SP-G1-VIRAL-015` plus `P016BATCHREV-G1-VIRAL-001` through
  `P020BATCHREV-G1-VIRAL-001` as the current page-complete accepted-only
  baseline.
- Synchronize current-status documentation and roadmap cursors so stale
  P011/P015/P020 wording cannot imply page 021 authorization or whole-Gate
  acceptance.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/post_p020_gate_1_status_readiness_plan.md`
- `scripts/build_gate_1_status_readiness_post_p020.py`
- `tests/test_gate_1_status_readiness_post_p020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_016/*`
- Current-state and roadmap synchronization in `PROJECT_STATUS.md`,
  `docs/roadmap/roadmap.yaml`, `docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md`,
  and `docs/plans/20260715-sourcefold-phase-0-release-charter/context.md`.

Limits:

- Do not process, authorize, or accept page 021 or later.
- Do not accept whole Gate 1 or admit fixtures.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- `G1SP-G1-VIRAL-016`: `C69701A098CC33486B89C6F0D7F8D1A890B05C288DC8F814A430D44ABF47F88F`
- `G1SP-G1-VIRAL-016` report: `3C051D65A15CB4DE0FA5649D6FE6C5C81AC75B3A752EC80E126EA81E50713F05`

## BA-G1-VIRAL-SOURCE-PROFILE-READINESS-PARKING-MATRIX-001

Status: `scope_consumed`

Lane: `G1SPRM-G1-VIRAL-001`

Authority: Bogdan Telegram message `2156`: "приступай. бери сол и терру в помощь"

Exact action:

- Create a Gate 1 source-profile readiness / parking matrix for decision prep
  only.
- Classify current Gate 1 source-profile parameters against the pages 001-020
  accepted-only baseline.
- Record OCR benchmark remediation / methodology hardening as the selected next
  branch, without starting that branch.

Admitted inputs:

- `G1SP-G1-VIRAL-016`: `C69701A098CC33486B89C6F0D7F8D1A890B05C288DC8F814A430D44ABF47F88F`
- `G1SP-G1-VIRAL-016` report: `3C051D65A15CB4DE0FA5649D6FE6C5C81AC75B3A752EC80E126EA81E50713F05`
- `G1SP-G1-VIRAL-015`: `B016D09B91A5C1DA9B3E6026C9E5CF777CE290773864C786A51903FA1FCD62F8`
- Existing OCR remediation evidence as unresolved/later input only:
  `ORM-G1-VIRAL-001`, `ORR-G1-VIRAL-001`, and `ONC-G1-VIRAL-001`.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_source_profile_readiness_parking_matrix_plan.md`
- `scripts/build_gate_1_source_profile_readiness_parking_matrix.py`
- `tests/test_gate_1_source_profile_readiness_parking_matrix.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_profile_readiness_parking_matrix_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, and phase/gate hierarchy synchronization as needed to remove stale
  current-route wording.

Limits:

- Do not accept or park source-profile parameters.
- Do not process, authorize, or accept page 021 or later.
- Do not start OCR remediation or run OCR.
- Do not accept whole Gate 1 or admit fixtures.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as decision-prep only.
- `G1SPRM-G1-VIRAL-001`:
  `49EFEF00F19ACA3D583EA5A2DB221023C54F9EA32C83609A0DD95988F9612466`
- `G1SPRM-G1-VIRAL-001` report:
  `1E5F1A6CEA99B4BB4C67D9126727FBBC5C855CDDCF3B0F98CA0AD9F1C6710577`

## BA-G1-VIRAL-SOURCE-PROFILE-READINESS-MATRIX-REVIEW-001

Status: `scope_consumed`

Lane: `G1SPRMREV-G1-VIRAL-001`

Authority: Bogdan Telegram message `2182`: "ок принято с коментариями . что тогда дальше?"

Exact action:

- Record Bogdan's review of `G1SPRM-G1-VIRAL-001` as accepted with comments.
- Accept only the matrix as a route-review artifact.
- Preserve comments that the matrix creates no source-profile acceptance, no
  parking decision, no OCR remediation execution, no page 021+ authorization,
  and no whole Gate 1 acceptance.
- Preserve the selected next branch as OCR benchmark remediation / methodology
  hardening requiring a separate bounded authorization.

Admitted inputs:

- `G1SPRM-G1-VIRAL-001`:
  `49EFEF00F19ACA3D583EA5A2DB221023C54F9EA32C83609A0DD95988F9612466`
- `G1SPRM-G1-VIRAL-001` report:
  `1E5F1A6CEA99B4BB4C67D9126727FBBC5C855CDDCF3B0F98CA0AD9F1C6710577`

Allowed outputs:

- `scripts/accept_gate_1_source_profile_readiness_matrix_review.py`
- `tests/test_gate_1_source_profile_readiness_matrix_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_profile_readiness_parking_matrix_review_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, and status synchronization for the
  accepted route-review artifact.

Limits:

- Do not accept source-profile parameters.
- Do not create a parking decision.
- Do not start OCR remediation or run OCR.
- Do not process, authorize, or accept page 021 or later.
- Do not accept whole Gate 1 or admit fixtures.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as route-review artifact acceptance only.
- `G1SPRMREV-G1-VIRAL-001`:
  `76D0B43FCE9B614424A47FEBDE61666E42B372E671396E876E1F59B38FCEC640`
- `G1SPRMREV-G1-VIRAL-001` summary:
  `E25C0611E91186E20C1970966367DB8797E7D71F1069E2B230AC751F16E20EE7`

## BA-G1-VIRAL-OCR-BENCHMARK-METHODOLOGY-HARDENING-001

Status: `scope_consumed`

Lane: `OCRHM-G1-VIRAL-001`

Authority: Bogdan Telegram message `2189`: "делай оба шага"

Exact action:

- Create an OCR benchmark methodology hardening packet from existing evidence.
- Consume `G1SPRMREV-G1-VIRAL-001`, `ORM-G1-VIRAL-001`,
  `ORR-G1-VIRAL-001`, `ONC-G1-VIRAL-001`, and `OBR-G1-VIRAL-002` evidence.
- Harden methodology rules for OCR engine/config/threshold handling,
  benchmark pass/fail policy, no acceptance-by-score, visual-QC routing,
  overlay/order QC interpretation, and raw payload containment.

Admitted inputs:

- `G1SPRMREV-G1-VIRAL-001`:
  `76D0B43FCE9B614424A47FEBDE61666E42B372E671396E876E1F59B38FCEC640`
- `ORM-G1-VIRAL-001` report:
  `3A454433ABA46E237D091F5BB4DA6EB8B73FCEE400935AF10BB0DC5731F212F5`
- `ORM-G1-VIRAL-001` rows:
  `B0077249E070E6673E12F4A8B83C542DFD400A8200C558ACED4A0C47C284FD66`
- `ORR-G1-VIRAL-001` report:
  `B3491A1F3E942C430AE246A62DCAFB066F95BEA56390CF510D27635EBFEE6725`
- `ONC-G1-VIRAL-001` report:
  `2205564DB2BCD9EEF73D8EB02034EA28D7292D1A6970E3056F3BD9F5887E8F61`
- `OBR-G1-VIRAL-002` result report:
  `AFC2D58AB9B22ADD6A0B345BB72FA630049FBB1855771A1EF2ADDCC20D646937`
- `OBR-G1-VIRAL-002` output manifest:
  `BF8ABFF3F9E54DCAA0E2C944A437EC46D1A0C066C051798F012B0FC1AFEFD849`
- `OBR-G1-VIRAL-002` run boundary report:
  `CFA4B8ACDF0BA5AED70DFE5E730E442D8B3D3671E17FEE8300AB5BE4AE95B10C`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/ocr_benchmark_methodology_hardening_plan.md`
- `scripts/build_ocr_benchmark_methodology_hardening.py`
- `tests/test_ocr_benchmark_methodology_hardening.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/ocr_benchmark_methodology_hardening_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, and phase/gate hierarchy synchronization.

Limits:

- Do not execute OCR or OCR remediation.
- Do not parse PDF text layers or mutate raw/source/OCR/render/PDF assets.
- Do not accept OCR engine/config/thresholds as a source profile.
- Do not create parking decisions.
- Do not process, authorize, or accept page 021 or later.
- Do not accept whole Gate 1 or admit fixtures.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as OCR benchmark methodology hardening evidence only.
- `OCRHM-G1-VIRAL-001`:
  `AF62629E87F757929CC609C13198DB2594E4837F1296E1D9EF242E7E21B11C36`
- `OCRHM-G1-VIRAL-001` report:
  `08A913FED762D70FE603FEAD390804C067695071B580DEE00F50C22D68E991A5`
- `OCRHM-G1-VIRAL-001` summary:
  `F110555A257C322F2A36ECDFF98B75491557A2ABAB31A016ADD0882600E8A044`

## BA-G1-VIRAL-POST-OCR-HARDENING-STATUS-READINESS-001

Status: `scope_consumed`

Lane: `G1SP-G1-VIRAL-017`

Authority: Bogdan Telegram message `2197`: "после этого готовить `post_ocr_hardening_gate_1_readiness_refresh`"

Exact action:

- Create a post-OCR-hardening Gate 1 status/readiness refresh packet.
- Consume `G1SP-G1-VIRAL-016`, `G1SPRMREV-G1-VIRAL-001`, and
  `OCRHM-G1-VIRAL-001`.
- Record that OCR methodology hardening is ready for Gate review while source
  profile, parking, fixture, page 021+, and whole Gate 1 decisions remain
  separate future decisions.

Admitted inputs:

- `G1SP-G1-VIRAL-016`:
  `C69701A098CC33486B89C6F0D7F8D1A890B05C288DC8F814A430D44ABF47F88F`
- `G1SP-G1-VIRAL-016` report:
  `3C051D65A15CB4DE0FA5649D6FE6C5C81AC75B3A752EC80E126EA81E50713F05`
- `G1SPRMREV-G1-VIRAL-001`:
  `76D0B43FCE9B614424A47FEBDE61666E42B372E671396E876E1F59B38FCEC640`
- `OCRHM-G1-VIRAL-001`:
  `AF62629E87F757929CC609C13198DB2594E4837F1296E1D9EF242E7E21B11C36`
- `OCRHM-G1-VIRAL-001` report:
  `08A913FED762D70FE603FEAD390804C067695071B580DEE00F50C22D68E991A5`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/post_ocr_hardening_gate_1_readiness_refresh_plan.md`
- `scripts/build_gate_1_status_refresh_post_ocr_hardening.py`
- `tests/test_gate_1_status_refresh_post_ocr_hardening.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_017/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, and phase/gate hierarchy synchronization.

Limits:

- Do not accept source profile, whole Gate 1, OCR outputs, fixtures, or pages.
- Do not create parking decisions.
- Do not execute OCR or OCR remediation.
- Do not process, authorize, or accept page 021 or later.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as post-OCR-hardening status/readiness refresh only.
- `G1SP-G1-VIRAL-017`:
  `DA9B421CD8A5BC503FCCEE24F6043FBCEC9F86262AF3E9E9018C460D871E4ED6`
- `G1SP-G1-VIRAL-017` report:
  `007F7F1F6FC73FC4F9B9268CB3969F895517D20B054FCC1D787851E4609D2F68`
- `G1SP-G1-VIRAL-017` summary:
  `FF3F3D7F9F3EA0352C95448124821DE2C2255E63DCFEB9D6879A6EA722166CF3`
- `G1SP-G1-VIRAL-017` manifest:
  `4A7DDDC454034FC8CFC75C184856B66D27B17ECEA0E5E8447C331B07CCD381A9`

## BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-001

Status: `scope_consumed`

Lane: `G1SPRPD-G1-VIRAL-001`

Authority: Bogdan Telegram message `2210`: "делай"

Exact action:

- Create a Gate 1 source-profile review / parking decision prep packet.
- Consume `G1SP-G1-VIRAL-017`, `G1SPRM-G1-VIRAL-001`,
  `G1SPRMREV-G1-VIRAL-001`, and `OCRHM-G1-VIRAL-001`.
- Represent all 12 matrix rows exactly once as future decision categories.
- Preserve `decision_prep_no_acceptance_no_parking`: no source-profile
  acceptance, no parking decision, no fixture admission, no page `021+`, and no
  whole Gate 1 acceptance.

Admitted inputs:

- `G1SP-G1-VIRAL-017`:
  `DA9B421CD8A5BC503FCCEE24F6043FBCEC9F86262AF3E9E9018C460D871E4ED6`
- `G1SP-G1-VIRAL-017` report:
  `007F7F1F6FC73FC4F9B9268CB3969F895517D20B054FCC1D787851E4609D2F68`
- `G1SP-G1-VIRAL-017` summary:
  `FF3F3D7F9F3EA0352C95448124821DE2C2255E63DCFEB9D6879A6EA722166CF3`
- `G1SP-G1-VIRAL-017` manifest:
  `4A7DDDC454034FC8CFC75C184856B66D27B17ECEA0E5E8447C331B07CCD381A9`
- `G1SPRM-G1-VIRAL-001`:
  `49EFEF00F19ACA3D583EA5A2DB221023C54F9EA32C83609A0DD95988F9612466`
- `G1SPRM-G1-VIRAL-001` report:
  `1E5F1A6CEA99B4BB4C67D9126727FBBC5C855CDDCF3B0F98CA0AD9F1C6710577`
- `G1SPRM-G1-VIRAL-001` summary:
  `663A31D6E5D22CB6F0E093DF4BE5B122B42F5C4E4402E825D995195D6CBB8E9B`
- `G1SPRMREV-G1-VIRAL-001`:
  `76D0B43FCE9B614424A47FEBDE61666E42B372E671396E876E1F59B38FCEC640`
- `G1SPRMREV-G1-VIRAL-001` summary:
  `E25C0611E91186E20C1970966367DB8797E7D71F1069E2B230AC751F16E20EE7`
- `OCRHM-G1-VIRAL-001`:
  `AF62629E87F757929CC609C13198DB2594E4837F1296E1D9EF242E7E21B11C36`
- `OCRHM-G1-VIRAL-001` report:
  `08A913FED762D70FE603FEAD390804C067695071B580DEE00F50C22D68E991A5`
- `OCRHM-G1-VIRAL-001` summary:
  `F110555A257C322F2A36ECDFF98B75491557A2ABAB31A016ADD0882600E8A044`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_source_profile_review_parking_decision_prep_plan.md`
- `scripts/build_gate_1_source_profile_review_parking_decision_prep.py`
- `tests/test_gate_1_source_profile_review_parking_decision_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_profile_review_parking_decision_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, and phase/gate hierarchy synchronization.

Limits:

- Do not accept source profile, whole Gate 1, OCR outputs, fixtures, or pages.
- Do not create parking decisions.
- Do not execute OCR or OCR remediation.
- Do not process, authorize, or accept page 021 or later.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as Gate 1 source-profile review / parking decision
  prep only.
- `G1SPRPD-G1-VIRAL-001`:
  `3572FBB2A2A23DD9B4B3A2D9C518849F91AF60367A5165CA72AECE6E1AB7A06C`
- `G1SPRPD-G1-VIRAL-001` report:
  `E31CFE5960F876EF483C5AEE8A65A8F4C5BD364D27201CC3ECC59E2E4DD94E44`
- `G1SPRPD-G1-VIRAL-001` summary:
  `F9FEE23C6B5341E289C3776C590DA6918B82167AA9266942F4C47C8ED017C0B0`
- `G1SPRPD-G1-VIRAL-001` manifest:
  `E310CC116A9DA41BE833770F69C3FC92FE2E7B3C53B3EFF3C0CAB9ABC1BF84A7`

## BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-REVIEW-001

Status: `scope_consumed`

Lane: `G1SPRPDREV-G1-VIRAL-001`

Authority: Bogdan Telegram message `2227`: "G1SPRPD accepted as decision-prep only; proceed to prepare Gate 1 source-profile decision packet; no source-profile acceptance or parking yet"

Exact action:

- Record human review of `G1SPRPD-G1-VIRAL-001` as decision-prep only.
- Allow preparation of the next Gate 1 source-profile decision packet.
- Preserve the explicit boundary: no source-profile acceptance and no parking
  decision yet.

Admitted inputs:

- `G1SPRPD-G1-VIRAL-001`:
  `3572FBB2A2A23DD9B4B3A2D9C518849F91AF60367A5165CA72AECE6E1AB7A06C`
- `G1SPRPD-G1-VIRAL-001` report:
  `E31CFE5960F876EF483C5AEE8A65A8F4C5BD364D27201CC3ECC59E2E4DD94E44`
- `G1SPRPD-G1-VIRAL-001` summary:
  `F9FEE23C6B5341E289C3776C590DA6918B82167AA9266942F4C47C8ED017C0B0`
- `G1SPRPD-G1-VIRAL-001` manifest:
  `E310CC116A9DA41BE833770F69C3FC92FE2E7B3C53B3EFF3C0CAB9ABC1BF84A7`

Allowed outputs:

- `scripts/accept_gate_1_source_profile_review_parking_decision_prep_review.py`
- `tests/test_gate_1_source_profile_review_parking_decision_prep_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_profile_review_parking_decision_prep_review_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, and phase/gate hierarchy synchronization.

Limits:

- Do not accept source profile, whole Gate 1, OCR outputs, fixtures, or pages.
- Do not create parking decisions.
- Do not execute OCR or OCR remediation.
- Do not process, authorize, or accept page 021 or later.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as decision-prep review only.
- `G1SPRPDREV-G1-VIRAL-001`:
  `118241D5A8CFB01FBD0DFBB4C1D0424E97B52E976A52F4EA10045A452C4F8CE8`
- `G1SPRPDREV-G1-VIRAL-001` summary:
  `AB6CEB2E5D3BD8A68F10C173D2700FA7413466082B8CAC91ACEB5D71B701541F`
- `G1SPRPDREV-G1-VIRAL-001` manifest:
  `FAD4F428CAA277D1F7E6537CC6BE9230EBF4865B69731CD7CC8AD350E78888D5`

## BA-G1-VIRAL-SOURCE-PROFILE-DECISION-PACKET-001

Status: `scope_consumed`

Lane: `G1SPDP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2227`: "G1SPRPD accepted as decision-prep only; proceed to prepare Gate 1 source-profile decision packet; no source-profile acceptance or parking yet"

Exact action:

- Create a human-facing Gate 1 source-profile decision-options packet.
- Consume `G1SPRPDREV-G1-VIRAL-001` as the controlling accepted prep review.
- Prepare future explicit decision options without accepting source profile,
  creating parking decisions, admitting fixtures, authorizing page `021+`, or
  accepting whole Gate 1.

Admitted inputs:

- `G1SPRPDREV-G1-VIRAL-001`:
  `118241D5A8CFB01FBD0DFBB4C1D0424E97B52E976A52F4EA10045A452C4F8CE8`
- `G1SPRPDREV-G1-VIRAL-001` summary:
  `AB6CEB2E5D3BD8A68F10C173D2700FA7413466082B8CAC91ACEB5D71B701541F`
- `G1SPRPDREV-G1-VIRAL-001` manifest:
  `FAD4F428CAA277D1F7E6537CC6BE9230EBF4865B69731CD7CC8AD350E78888D5`
- `G1SPRPD-G1-VIRAL-001`:
  `3572FBB2A2A23DD9B4B3A2D9C518849F91AF60367A5165CA72AECE6E1AB7A06C`
- `G1SPRPD-G1-VIRAL-001` report:
  `E31CFE5960F876EF483C5AEE8A65A8F4C5BD364D27201CC3ECC59E2E4DD94E44`
- `G1SPRPD-G1-VIRAL-001` summary:
  `F9FEE23C6B5341E289C3776C590DA6918B82167AA9266942F4C47C8ED017C0B0`
- `G1SPRPD-G1-VIRAL-001` manifest:
  `E310CC116A9DA41BE833770F69C3FC92FE2E7B3C53B3EFF3C0CAB9ABC1BF84A7`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_source_profile_decision_packet_plan.md`
- `scripts/build_gate_1_source_profile_decision_packet.py`
- `tests/test_gate_1_source_profile_decision_packet.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_profile_decision_packet_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, and phase/gate hierarchy synchronization.

Limits:

- Do not accept source profile, whole Gate 1, OCR outputs, fixtures, or pages.
- Do not create parking decisions.
- Do not execute OCR or OCR remediation.
- Do not process, authorize, or accept page 021 or later.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as human-facing decision-options packet only.
- `G1SPDP-G1-VIRAL-001`:
  `CB528844A71328F8E7C8A281BF67243F292B1C53E991B48B42DF6C51313FD21E`
- `G1SPDP-G1-VIRAL-001` report:
  `AB04F38ECFA9C5384639A5B573ABB1F0F907E9CD38B4649479BB8BE0E36BE6AB`
- `G1SPDP-G1-VIRAL-001` summary:
  `86D8752B5557AC5E643285BBA4911DFA801B0978BACBF7226A45140E7E8D8CA5`
- `G1SPDP-G1-VIRAL-001` manifest:
  `F58ED5D8F8F585E792A4A80330B69434C0207DAFEABAFAF2CADBB4B5EFEDFB89`

## BA-G1-VIRAL-SOURCE-PROFILE-DECISION-RECORD-001

Status: `scope_consumed`

Lane: `G1SPDR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2237`: `ок`, as contextual approval of the
immediately preceding assistant-proposed phrase:
`G1SPDP accepted as options packet; prepare Gate 1 source-profile decision record with: accept 5 selected source-profile elements as Gate review candidates; park 2 OCR methodology/debt items for Core 0.1 with invalidation conditions; keep 2 render/source reconstruction rows evidence-only; keep unsupported/negative fixtures and whole Gate 1 blocked; P021+ requires separate BA; no fixture admission, no whole Gate 1 acceptance, no push`.
The long phrase is recorded as the assistant proposal, not as Bogdan's verbatim
text.

Exact action:

- Create a bounded Gate 1 source-profile decision record from
  `G1SPDP-G1-VIRAL-001`.
- Record 5 selected source-profile rows as Gate review candidates only, not
  whole source-profile acceptance.
- Park 2 OCR methodology/debt rows for Core 0.1 with explicit invalidation
  conditions.
- Keep 2 render/source-reconstruction rows evidence-only.
- Keep unsupported/negative fixtures and whole Gate 1 blocked.
- Keep page `021+` behind a separate bounded authorization.

Admitted inputs:

- `G1SPDP-G1-VIRAL-001`:
  `CB528844A71328F8E7C8A281BF67243F292B1C53E991B48B42DF6C51313FD21E`
- `G1SPDP-G1-VIRAL-001` report:
  `AB04F38ECFA9C5384639A5B573ABB1F0F907E9CD38B4649479BB8BE0E36BE6AB`
- `G1SPDP-G1-VIRAL-001` summary:
  `86D8752B5557AC5E643285BBA4911DFA801B0978BACBF7226A45140E7E8D8CA5`
- `G1SPDP-G1-VIRAL-001` manifest:
  `F58ED5D8F8F585E792A4A80330B69434C0207DAFEABAFAF2CADBB4B5EFEDFB89`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_source_profile_decision_record_plan.md`
- `scripts/build_gate_1_source_profile_decision_record.py`
- `tests/test_gate_1_source_profile_decision_record.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_source_profile_decision_record_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not accept whole source profile.
- Do not admit fixtures.
- Do not accept whole Gate 1.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any broader Gate
  action.

Run output status:

- Generated and verified as bounded source-profile decision record.
- `G1SPDR-G1-VIRAL-001`:
  `E00E17879BE98340A00582B8C128E8C1C7C984657FDC142513447618591691C1`
- `G1SPDR-G1-VIRAL-001` report:
  `15EA6C81E2269D0289549C0BC682418CE581D8391EB07D20759461CF436BB125`
- `G1SPDR-G1-VIRAL-001` summary:
  `8E4A21C9EF5AD8661867F5D12A285EBA3DC54282BECA644CABBCBDE4E5A1EA26`
- `G1SPDR-G1-VIRAL-001` manifest:
  `E2908F97C39BB32F317B318E76286E06375A3637C30A367C2A20C2CDEEBA8C1D`

## BA-G1-VIRAL-FIXTURE-GATE-1-READINESS-PREP-001

Status: `scope_consumed`

Lane: `G1FARP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2243`: "пошли дальше"

Exact action:

- Create a bounded Gate 1 fixture-admission / whole-Gate-acceptance readiness
  prep packet from `G1SPDR-G1-VIRAL-001`.
- Enumerate blockers, missing predicates, fixture/acceptance options, required
  evidence, invalidation risks, and next-decision wording only.
- Consume existing `G1SPDR` Gate review candidate and OCR parking outcomes
  without creating new parking decisions.
- Preserve page `021+` as a separate bounded authorization lane.

Admitted inputs:

- `G1SPDR-G1-VIRAL-001`:
  `E00E17879BE98340A00582B8C128E8C1C7C984657FDC142513447618591691C1`
- `G1SPDR-G1-VIRAL-001` report:
  `15EA6C81E2269D0289549C0BC682418CE581D8391EB07D20759461CF436BB125`
- `G1SPDR-G1-VIRAL-001` summary:
  `8E4A21C9EF5AD8661867F5D12A285EBA3DC54282BECA644CABBCBDE4E5A1EA26`
- `G1SPDR-G1-VIRAL-001` manifest:
  `E2908F97C39BB32F317B318E76286E06375A3637C30A367C2A20C2CDEEBA8C1D`
- `G1SP-G1-VIRAL-017`:
  `DA9B421CD8A5BC503FCCEE24F6043FBCEC9F86262AF3E9E9018C460D871E4ED6`
- `G1SP-G1-VIRAL-017` report:
  `007F7F1F6FC73FC4F9B9268CB3969F895517D20B054FCC1D787851E4609D2F68`
- `G1SP-G1-VIRAL-017` summary:
  `FF3F3D7F9F3EA0352C95448124821DE2C2255E63DCFEB9D6879A6EA722166CF3`
- `G1SP-G1-VIRAL-017` manifest:
  `4A7DDDC454034FC8CFC75C184856B66D27B17ECEA0E5E8447C331B07CCD381A9`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_admission_readiness_prep_plan.md`
- `scripts/build_gate_1_fixture_admission_readiness_prep.py`
- `tests/test_gate_1_fixture_admission_readiness_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_admission_readiness_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture-admission / whole-Gate-acceptance
  readiness prep only.
- `G1FARP-G1-VIRAL-001`:
  `A6AB9B1CD40EDAC6D2A83B24306920743D5B6039410B1188FA5D6DB433A52CEC`
- `G1FARP-G1-VIRAL-001` report:
  `0BBED96C4E0D41054AE1FA8AB1FA27430DD330580DA04A5B74C1EBC39CDE5EC8`
- `G1FARP-G1-VIRAL-001` summary:
  `E8962C044123C9ADFA59C58F066C166C5675312D27DBE278FE91D0F30DFF6753`
- `G1FARP-G1-VIRAL-001` manifest:
  `51073752A2BD86B96233BE000A21C4A029E027E98B6F646C7C0545C256870780`

## BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-PREP-REVIEW-001

Status: `scope_consumed`

Lane: `G1FARPREV-G1-VIRAL-001`

Authority: Bogdan Telegram message `2255`:
`G1FARP accepted as readiness/blocker packet only; proceed to prepare fixture admission blocker resolution prep; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push`

Exact action:

- Record human review of `G1FARP-G1-VIRAL-001` as readiness/blocker packet
  acceptance only.
- Authorize preparation of a fixture admission blocker resolution prep packet.
- Preserve all `G1FARP` limits.

Admitted inputs:

- `G1FARP-G1-VIRAL-001`:
  `A6AB9B1CD40EDAC6D2A83B24306920743D5B6039410B1188FA5D6DB433A52CEC`
- `G1FARP-G1-VIRAL-001` report:
  `0BBED96C4E0D41054AE1FA8AB1FA27430DD330580DA04A5B74C1EBC39CDE5EC8`
- `G1FARP-G1-VIRAL-001` summary:
  `E8962C044123C9ADFA59C58F066C166C5675312D27DBE278FE91D0F30DFF6753`
- `G1FARP-G1-VIRAL-001` manifest:
  `51073752A2BD86B96233BE000A21C4A029E027E98B6F646C7C0545C256870780`

Allowed outputs:

- `scripts/accept_gate_1_fixture_admission_readiness_prep_review.py`
- `tests/test_gate_1_fixture_admission_readiness_prep_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_admission_readiness_prep_review_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as readiness/blocker packet review only.
- `G1FARPREV-G1-VIRAL-001`:
  `9CFBF6FDC7E20956171113CAAA7000BB3F9A46A4234D6A90C1F2FA6799F0A635`
- `G1FARPREV-G1-VIRAL-001` summary:
  `85AF258D59E413623B46F077FDE28AEB80E91B888E3BF34EFFDEB6FF28B8476C`
- `G1FARPREV-G1-VIRAL-001` manifest:
  `9EFACF0DC44D77B989FF7C8F0D3F28ED0F08ABABA0C7E51AFD8C1737D3AE33C7`

## BA-G1-VIRAL-FIXTURE-ADMISSION-BLOCKER-RESOLUTION-PREP-001

Status: `scope_consumed`

Lane: `G1FABRP-G1-VIRAL-001`

Authority: `G1FARPREV-G1-VIRAL-001`, created from Bogdan Telegram message
`2255`.

Exact action:

- Prepare a bounded fixture admission blocker resolution prep packet from
  `G1FARP-G1-VIRAL-001` and `G1FARPREV-G1-VIRAL-001`.
- Enumerate blocker categories, resolution questions, and recommended next
  sequence only.
- Do not resolve blockers or admit fixtures.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_admission_blocker_resolution_prep_plan.md`
- `scripts/build_gate_1_fixture_admission_blocker_resolution_prep.py`
- `tests/test_gate_1_fixture_admission_blocker_resolution_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_admission_blocker_resolution_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture admission blocker resolution prep only.
- `G1FABRP-G1-VIRAL-001`:
  `5CF0182E401E12E6382B3E5D39E6A3391641AD5FCC29F7E916C2D1F91D2EB9AB`
- `G1FABRP-G1-VIRAL-001` report:
  `EAEF68EE7C826DE8C8C33693C3C99166E3CDFA93987AACAAEFAB4E7E78C75004`
- `G1FABRP-G1-VIRAL-001` summary:
  `5092123F70DC7B3DF9D65A78C6E777F0AC35D379DCE85895F7DC5838B100DB0E`
- `G1FABRP-G1-VIRAL-001` manifest:
  `A806B34A1E20BA89F6723CBC309654DDAF366EB50CF1A653DC16061BC0257A60`

## BA-G1-VIRAL-FIXTURE-ADMISSION-BLOCKER-RESOLUTION-PREP-REVIEW-001

Status: `scope_consumed`

Lane: `G1FABRPREV-G1-VIRAL-001`

Authority: Bogdan Telegram message `2275`: `ок`, as contextual approval after
the assistant reported that `G1FABRP-G1-VIRAL-001` was ready for human review
following Sol/Terra cleanup. The raw `ок` is recorded as contextual approval,
not as a broad fixture or Gate acceptance.

Exact action:

- Record human review of `G1FABRP-G1-VIRAL-001` as blocker-resolution prep
  acceptance only.
- Preserve the reviewed blocker list and recommended next candidate.
- Do not resolve blockers or admit fixtures.

Admitted inputs:

- `G1FABRP-G1-VIRAL-001`:
  `5CF0182E401E12E6382B3E5D39E6A3391641AD5FCC29F7E916C2D1F91D2EB9AB`
- `G1FABRP-G1-VIRAL-001` report:
  `EAEF68EE7C826DE8C8C33693C3C99166E3CDFA93987AACAAEFAB4E7E78C75004`
- `G1FABRP-G1-VIRAL-001` summary:
  `5092123F70DC7B3DF9D65A78C6E777F0AC35D379DCE85895F7DC5838B100DB0E`
- `G1FABRP-G1-VIRAL-001` manifest:
  `A806B34A1E20BA89F6723CBC309654DDAF366EB50CF1A653DC16061BC0257A60`

Allowed outputs:

- `scripts/accept_gate_1_fixture_admission_blocker_resolution_prep_review.py`
- `tests/test_gate_1_fixture_admission_blocker_resolution_prep_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_admission_blocker_resolution_prep_review_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not resolve blockers.
- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as blocker-resolution prep review only.
- `G1FABRPREV-G1-VIRAL-001`:
  `FAD1AA01AB0AAB2E2B69B02BF101D788035E5C058920E33463800F9E351E3183`
- `G1FABRPREV-G1-VIRAL-001` summary:
  `BA3AC1B0B7EE58EF2D65F1DB9EF391C00F0A77C4F961D60BBB54D0B0DE67616E`
- `G1FABRPREV-G1-VIRAL-001` manifest:
  `7B6AF4B28CC90BB7A8537BFD996C2DBACF32EAE3343CCDAF92DEAE9B86147745`

## BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-DECISION-PREP-001

Status: `scope_consumed`

Lane: `G1UNFPDP-G1-VIRAL-001`

Authority: `G1FABRPREV-G1-VIRAL-001`, which accepts
`G1FABRP-G1-VIRAL-001` as blocker-resolution prep only and selects
`unsupported_negative_fixture_policy_decision_prep` as the next candidate.

Exact action:

- Prepare a bounded unsupported/negative fixture policy decision-prep packet.
- Enumerate questions for unsupported profile scope, negative fixture
  obligations, invalidation conditions, and fixture-admission dependency.
- Do not make a policy decision, resolve blockers, admit fixtures, or accept
  whole Gate 1.

Admitted inputs:

- `G1FABRPREV-G1-VIRAL-001`:
  `FAD1AA01AB0AAB2E2B69B02BF101D788035E5C058920E33463800F9E351E3183`
- `G1FABRPREV-G1-VIRAL-001` summary:
  `BA3AC1B0B7EE58EF2D65F1DB9EF391C00F0A77C4F961D60BBB54D0B0DE67616E`
- `G1FABRPREV-G1-VIRAL-001` manifest:
  `7B6AF4B28CC90BB7A8537BFD996C2DBACF32EAE3343CCDAF92DEAE9B86147745`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_unsupported_negative_fixture_policy_decision_prep_plan.md`
- `scripts/build_gate_1_unsupported_negative_fixture_policy_decision_prep.py`
- `tests/test_gate_1_unsupported_negative_fixture_policy_decision_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_unsupported_negative_fixture_policy_decision_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not make unsupported/negative fixture policy decisions.
- Do not resolve blockers.
- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as unsupported/negative fixture policy decision prep
  only.
- `G1UNFPDP-G1-VIRAL-001`:
  `ACB7E596C63896C67CB4C93AB691DB5FE19B0B53ED56EBE87CA9D510D4771F58`
- `G1UNFPDP-G1-VIRAL-001` report:
  `0FC376645E49B7E8323A25AA164ADA9C1E9B256C8B341FE73B07B6BB2776F571`
- `G1UNFPDP-G1-VIRAL-001` summary:
  `378834F02FF862EA39B090F82D0A15D292F6359ED9249D2E435D618505F394D5`
- `G1UNFPDP-G1-VIRAL-001` manifest:
  `2BA000A90B79D20201A1A71C32031C14250B91929BDA049E40876D81741C28F4`

## BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-DECISION-PREP-REVIEW-001

Status: `scope_consumed`

Lane: `G1UNFPDPREV-G1-VIRAL-001`

Authority: Bogdan Telegram message `2315`:

`g1unfpdp packet ok; proceed to prepare unsupported/negative fixture policy record over unsupported_profiles_scope, negative_fixture_obligations, invalidation_conditions, and fixture_admission_dependency; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push`

Exact action:

- Record human review acceptance of `G1UNFPDP-G1-VIRAL-001` as decision-prep
  only.
- Authorize preparing an unsupported/negative fixture policy record over the
  four reviewed questions only.
- Do not make the policy decision inside the review record.

Admitted inputs:

- `G1UNFPDP-G1-VIRAL-001`:
  `ACB7E596C63896C67CB4C93AB691DB5FE19B0B53ED56EBE87CA9D510D4771F58`
- `G1UNFPDP-G1-VIRAL-001` report:
  `0FC376645E49B7E8323A25AA164ADA9C1E9B256C8B341FE73B07B6BB2776F571`
- `G1UNFPDP-G1-VIRAL-001` summary:
  `378834F02FF862EA39B090F82D0A15D292F6359ED9249D2E435D618505F394D5`
- `G1UNFPDP-G1-VIRAL-001` manifest:
  `2BA000A90B79D20201A1A71C32031C14250B91929BDA049E40876D81741C28F4`

Allowed outputs:

- `scripts/accept_gate_1_unsupported_negative_fixture_policy_decision_prep_review.py`
- `tests/test_gate_1_unsupported_negative_fixture_policy_record.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_unsupported_negative_fixture_policy_decision_prep_review_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not make unsupported/negative fixture policy decisions.
- Do not resolve blockers.
- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as prep review only.
- `G1UNFPDPREV-G1-VIRAL-001`:
  `3906CFB86519B0988E67B1DB681F817006493DD43F0209CE11E459C306BA8D72`
- `G1UNFPDPREV-G1-VIRAL-001` summary:
  `81B8CE5AC11222F561561FD5702DF603FCA29A6BBABF53EF1FC71203E3B158C3`
- `G1UNFPDPREV-G1-VIRAL-001` manifest:
  `D3A0749BCB01E68C5D5FCE561F6BE6EABEF902D93D276F984C3F9B5D6E4911CF`

## BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-RECORD-001

Status: `scope_consumed`

Lane: `G1UNFPR-G1-VIRAL-001`

Authority: `G1UNFPDPREV-G1-VIRAL-001`, which accepts
`G1UNFPDP-G1-VIRAL-001` as decision-prep only and authorizes the policy record
over the four reviewed questions.

Exact action:

- Create a bounded unsupported/negative fixture policy record candidate for
  review.
- Prepare candidate decisions for unsupported profile scope, negative fixture
  obligations, invalidation conditions, and fixture-admission dependency.
- Keep fixture admission, fixture manifests, page `021+`, whole source-profile
  acceptance, and whole Gate 1 acceptance blocked.

Admitted inputs:

- `G1UNFPDP-G1-VIRAL-001`:
  `ACB7E596C63896C67CB4C93AB691DB5FE19B0B53ED56EBE87CA9D510D4771F58`
- `G1UNFPDPREV-G1-VIRAL-001`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_unsupported_negative_fixture_policy_record_plan.md`
- `scripts/build_gate_1_unsupported_negative_fixture_policy_record.py`
- `tests/test_gate_1_unsupported_negative_fixture_policy_record.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_unsupported_negative_fixture_policy_record_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not make unsupported/negative fixture policy decisions.
- Do not resolve blockers.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as unsupported/negative fixture policy record
  candidate only.
- `G1UNFPR-G1-VIRAL-001`:
  `37CBDCFE0D9D715E3BCBA639F295C5609BBBB92F4678948BDF8747024E6D73F2`
- `G1UNFPR-G1-VIRAL-001` report:
  `F9CA1E06E77E273CA3C94D656D7FF6BD1BB09B6E733947739428A3C8F9127133`
- `G1UNFPR-G1-VIRAL-001` summary:
  `97E18C7483F9D89D9417CCEAED5E6D34783B708FFB42D66D8681B4246BF2F651`
- `G1UNFPR-G1-VIRAL-001` manifest:
  `0FCA5F00EAC6FFE0A477F8EEA551E17B9AA2AF0F66B35D6FE2C35D612F6304E7`

## BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-ACCEPTANCE-001

Status: `scope_consumed`

Lane: `G1UNFPAR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2335`:

`g1unfpr candidate ok; proceed to prepare unsupported/negative fixture policy acceptance record; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push`

Exact action:

- Record acceptance of `G1UNFPR-G1-VIRAL-001` as the unsupported/negative
  fixture policy record.
- Accept the four policy decisions for unsupported profile scope, negative
  fixture obligations, invalidation conditions, and fixture-admission
  dependency.
- Resolve only the unsupported/negative fixture policy decision blocker.
- Keep fixture admission, fixture manifests, page `021+`, whole source-profile
  acceptance, and whole Gate 1 acceptance blocked.

Admitted inputs:

- `G1UNFPR-G1-VIRAL-001`:
  `37CBDCFE0D9D715E3BCBA639F295C5609BBBB92F4678948BDF8747024E6D73F2`
- `G1UNFPR-G1-VIRAL-001` report:
  `F9CA1E06E77E273CA3C94D656D7FF6BD1BB09B6E733947739428A3C8F9127133`
- `G1UNFPR-G1-VIRAL-001` summary:
  `97E18C7483F9D89D9417CCEAED5E6D34783B708FFB42D66D8681B4246BF2F651`
- `G1UNFPR-G1-VIRAL-001` manifest:
  `0FCA5F00EAC6FFE0A477F8EEA551E17B9AA2AF0F66B35D6FE2C35D612F6304E7`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_unsupported_negative_fixture_policy_acceptance_record_plan.md`
- `scripts/accept_gate_1_unsupported_negative_fixture_policy_record.py`
- `tests/test_gate_1_unsupported_negative_fixture_policy_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_unsupported_negative_fixture_policy_acceptance_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as unsupported/negative fixture policy acceptance only.
- `G1UNFPAR-G1-VIRAL-001`:
  `FD4D704EFE18EEA6BF33C82E6C106AF67268E7AEA5924CD4FFB150A4ACDE408C`
- `G1UNFPAR-G1-VIRAL-001` report:
  `9AE4141BC8824BA7B3F494222C2C45C5C32C2151742D5C6B8830EEF09909D232`
- `G1UNFPAR-G1-VIRAL-001` summary:
  `C19E40A907688639C6BE286A149A8DF24CD16AC4F5150F430C7106A3AA874F35`
- `G1UNFPAR-G1-VIRAL-001` manifest:
  `1A3F8DC8FEBD2721BC0C2FB2330BB12193010BA6866EDD2AC211ECA0E2FCB3B9`

## BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-DECISION-PREP-001

Status: `scope_consumed`

Lane: `G1FSFDP-G1-VIRAL-001`

Authority: `G1UNFPAR-G1-VIRAL-001`, which accepts the unsupported/negative
fixture policy decision over unsupported profile scope, negative fixture
obligations, invalidation conditions, and fixture-admission dependency while
keeping fixture admission and whole Gate 1 blocked.

Exact action:

- Prepare a bounded fixture strategy fit decision-prep packet.
- Compare the accepted unsupported/negative fixture policy against the current
  draft fixture strategy.
- Prepare review questions for strategy scope fit, positive fixture seed fit,
  negative fixture coverage fit, invalidation dependency, and admission
  dependency.
- Do not create a fixture strategy fit decision.
- Do not admit fixtures, create fixture manifests, process page `021+`, or
  accept whole Gate 1.

Admitted inputs:

- `G1UNFPAR-G1-VIRAL-001`:
  `FD4D704EFE18EEA6BF33C82E6C106AF67268E7AEA5924CD4FFB150A4ACDE408C`
- `G1UNFPAR-G1-VIRAL-001` report:
  `9AE4141BC8824BA7B3F494222C2C45C5C32C2151742D5C6B8830EEF09909D232`
- `G1UNFPAR-G1-VIRAL-001` summary:
  `C19E40A907688639C6BE286A149A8DF24CD16AC4F5150F430C7106A3AA874F35`
- `G1UNFPAR-G1-VIRAL-001` manifest:
  `1A3F8DC8FEBD2721BC0C2FB2330BB12193010BA6866EDD2AC211ECA0E2FCB3B9`
- `fixture_strategy.md`:
  `7EF38F8B31F3EF58D275FDEC003A00CC996449B9BD062F76BC79B7B1F55A966F`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_strategy_fit_decision_prep_plan.md`
- `scripts/build_gate_1_fixture_strategy_fit_decision_prep.py`
- `tests/test_gate_1_fixture_strategy_fit_decision_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_strategy_fit_decision_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not create a fixture strategy fit decision.
- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture strategy fit decision prep only.
- `G1FSFDP-G1-VIRAL-001`:
  `969D416B56137635ED7D6D99BAB270D19F876C7F93B2F76092BCF36228D84E8F`
- `G1FSFDP-G1-VIRAL-001` report:
  `DE20186B42A74682FBDAE13B4A3C12C883172B7C1DA740F382643EE94FE4AD92`
- `G1FSFDP-G1-VIRAL-001` summary:
  `C2C92E86B43D1BE288FBD398AD3A109947780839683540F93BE4FB9323E3DC3D`
- `G1FSFDP-G1-VIRAL-001` manifest:
  `FDC9F60F8BE8802C9B3B674C9D47431021DF0A480E36677E2722EDA768409431`

## BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-ACCEPTANCE-001

Status: `scope_consumed`

Lane: `G1FSFAR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2353`:

`g1fsfdp packet ok; proceed to prepare fixture strategy fit acceptance record over strategy_scope_fit, positive_fixture_seed_fit, negative_fixture_coverage_fit, invalidation_dependency_fit, and admission_dependency; no fixture admission, no fixture manifest, no whole Gate 1 acceptance, no page 021+, no push`

Exact action:

- Record acceptance of `G1FSFDP-G1-VIRAL-001` as the fixture strategy fit
  decision-prep packet.
- Accept exactly five fixture strategy fit decisions: strategy scope fit,
  positive fixture seed fit, negative fixture coverage fit, invalidation
  dependency fit, and admission dependency.
- Resolve only the fixture strategy fit decision blocker.
- Keep fixture admission readiness refresh, whole Gate 1 acceptance readiness
  recheck, and page `021+` separate bounded authorization as remaining
  blockers.
- Keep fixture admission, fixture manifests, page `021+`, whole source-profile
  acceptance, and whole Gate 1 acceptance blocked.

Admitted inputs:

- `G1FSFDP-G1-VIRAL-001`:
  `969D416B56137635ED7D6D99BAB270D19F876C7F93B2F76092BCF36228D84E8F`
- `G1FSFDP-G1-VIRAL-001` report:
  `DE20186B42A74682FBDAE13B4A3C12C883172B7C1DA740F382643EE94FE4AD92`
- `G1FSFDP-G1-VIRAL-001` summary:
  `C2C92E86B43D1BE288FBD398AD3A109947780839683540F93BE4FB9323E3DC3D`
- `G1FSFDP-G1-VIRAL-001` manifest:
  `FDC9F60F8BE8802C9B3B674C9D47431021DF0A480E36677E2722EDA768409431`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_strategy_fit_acceptance_record_plan.md`
- `scripts/accept_gate_1_fixture_strategy_fit_decision_prep.py`
- `tests/test_gate_1_fixture_strategy_fit_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_strategy_fit_acceptance_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture strategy fit acceptance only.
- `G1FSFAR-G1-VIRAL-001`:
  `4F6BC8EB37F85256DF62C6F02AC4A1A0FFB081B5D70B5131940B001AFB6C3E7A`
- `G1FSFAR-G1-VIRAL-001` report:
  `27A68FB9EF917BD0D8CEE2FAE51206A965098878241825EA53DDEA6944EE3195`
- `G1FSFAR-G1-VIRAL-001` summary:
  `37CD1B6EC4499EE8664875B8904FAE0959E28C087DE234676FB6330EC6DED511`
- `G1FSFAR-G1-VIRAL-001` manifest:
  `9EF9222F67034E2F6A4D14750A777E82A72C270845BE8C4EBB72158D5108F7A0`

## BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-REFRESH-001

Status: `scope_consumed`

Lane: `G1FARR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2358`:

`proceed with fixture_admission_readiness_refresh; no fixture admission, no fixture manifest, no whole Gate 1 acceptance, no page 021+, no push`

Exact action:

- Refresh fixture admission readiness after accepted unsupported/negative
  fixture policy and fixture strategy fit decisions.
- Consume `G1SP-G1-VIRAL-017`, `G1FARP-G1-VIRAL-001`,
  `G1UNFPAR-G1-VIRAL-001`, and `G1FSFAR-G1-VIRAL-001`.
- Record current readiness rows for positive fixture seed readiness, negative
  fixture policy readiness, fixture strategy fit readiness, fixture admission
  readiness, and whole Gate 1 acceptance readiness.
- Resolve only the fixture admission readiness refresh blocker.
- Keep actual fixture admission and fixture manifest creation separate.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_admission_readiness_refresh_plan.md`
- `scripts/build_gate_1_fixture_admission_readiness_refresh.py`
- `tests/test_gate_1_fixture_admission_readiness_refresh.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_admission_readiness_refresh_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture admission readiness refresh only.
- `G1FARR-G1-VIRAL-001`:
  `033770B6F75CD08F2E3D491412242B33C223846585B826C1EED7258956118EE9`
- `G1FARR-G1-VIRAL-001` report:
  `2C33DD7ED7FCBCAECB2BDB81D73160FC01196F116511CCB4E4C8020D60F38018`
- `G1FARR-G1-VIRAL-001` summary:
  `ECCBE65314D80228050877BE5346DB02C14377287CB2B18D2E7923DA9DAE73AD`
- `G1FARR-G1-VIRAL-001` manifest:
  `76CCEF50B57DB60CC57B5CC006F8AF62AA51840680D50546527CD3AC488E02FF`

## BA-G1-VIRAL-FIXTURE-MANIFEST-PREP-001

Status: `scope_consumed`

Lane: `G1FMP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2371`:

`proceed with fixture_manifest_prep; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push, commit`

Exact action:

- Prepare a bounded fixture manifest prep packet after fixture admission
  readiness refresh.
- Consume `G1FARR-G1-VIRAL-001`.
- Propose the future manifest shape: positive page-complete seed group for
  pages 001-020 and required negative fixture groups from the accepted
  unsupported/negative policy.
- Prepare review questions for positive seed shape, negative group shape,
  manifest invalidation, and admission dependency.
- Do not create an actual fixture manifest.
- Do not admit fixtures, process page `021+`, accept whole Gate 1, or push.

Admitted inputs:

- `G1FARR-G1-VIRAL-001`:
  `033770B6F75CD08F2E3D491412242B33C223846585B826C1EED7258956118EE9`
- `G1FARR-G1-VIRAL-001` report:
  `2C33DD7ED7FCBCAECB2BDB81D73160FC01196F116511CCB4E4C8020D60F38018`
- `G1FARR-G1-VIRAL-001` summary:
  `ECCBE65314D80228050877BE5346DB02C14377287CB2B18D2E7923DA9DAE73AD`
- `G1FARR-G1-VIRAL-001` manifest:
  `76CCEF50B57DB60CC57B5CC006F8AF62AA51840680D50546527CD3AC488E02FF`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_manifest_prep_plan.md`
- `scripts/build_gate_1_fixture_manifest_prep.py`
- `tests/test_gate_1_fixture_manifest_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_manifest_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create actual fixture manifests.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture manifest prep only.
- `G1FMP-G1-VIRAL-001`:
  `9EBBEE63685A60FB3DA16561DDF63EBCA297ADCF10B2C6244739A5DF50114F1D`
- `G1FMP-G1-VIRAL-001` report:
  `C26B466E7CC255DCD71C03826928ABAA2F47563A29680E77398696531325C705`
- `G1FMP-G1-VIRAL-001` summary:
  `E550FDA439CB6CCA148478DC171E233C3FF3882B2AC702E07C9BBEFE88BAA46E`
- `G1FMP-G1-VIRAL-001` manifest:
  `6723FA55AB7031218E4BD898916EE75EC2D82E31975544497ABE5545E268B3A1`

## BA-G1-VIRAL-FIXTURE-MANIFEST-ACCEPTANCE-001

Status: `scope_consumed`

Lane: `G1FMR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2378`:

`g1fmp packet ok; proceed to prepare fixture manifest acceptance record; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push, commit`

Exact action:

- Record Bogdan's human review acceptance of `G1FMP-G1-VIRAL-001` as fixture
  manifest prep only.
- Consume `G1FMP-G1-VIRAL-001`.
- Create a fixture manifest record with one positive page-complete seed group
  for pages 001-020 and four negative fixture groups from the accepted
  unsupported/negative policy.
- Resolve only the fixture manifest review blocker.
- Keep fixture admission as a separate future decision.
- Do not process page `021+`, accept whole Gate 1, or push.

Admitted inputs:

- `G1FMP-G1-VIRAL-001`:
  `9EBBEE63685A60FB3DA16561DDF63EBCA297ADCF10B2C6244739A5DF50114F1D`
- `G1FMP-G1-VIRAL-001` report:
  `C26B466E7CC255DCD71C03826928ABAA2F47563A29680E77398696531325C705`
- `G1FMP-G1-VIRAL-001` summary:
  `E550FDA439CB6CCA148478DC171E233C3FF3882B2AC702E07C9BBEFE88BAA46E`
- `G1FMP-G1-VIRAL-001` manifest:
  `6723FA55AB7031218E4BD898916EE75EC2D82E31975544497ABE5545E268B3A1`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_manifest_acceptance_record_plan.md`
- `scripts/accept_gate_1_fixture_manifest_prep.py`
- `tests/test_gate_1_fixture_manifest_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_manifest_acceptance_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture manifest acceptance record only.
- `G1FMR-G1-VIRAL-001`:
  `5C5B2530F1EE2A65F4D0C2A52AC22973A62EF4B1CD544EC8184F7751BAC0EEC4`
- `G1FMR-G1-VIRAL-001` report:
  `141FC5D854542ABF7F3D6699A8FAA5DE2FE99E6C4EA82A298AC7A4B12C15431D`
- `G1FMR-G1-VIRAL-001` summary:
  `5AC4EB35225606F7FD0A96BAA4AFB18A2DC26DB4A4C3992A14AC52DCE7E2BBA9`
- `G1FMR-G1-VIRAL-001` manifest:
  `4DEB976065C8976EBAA88746980007863969AA4D742A969D0AF777BB5AB2A7BC`

## BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-PREP-001

Status: `scope_consumed`

Lane: `G1FADP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2401`:

`proceed with fixture_admission_decision_prep; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push, commit`

Exact action:

- Prepare fixture admission decision-prep after `G1FMR-G1-VIRAL-001`.
- Consume `G1FMR-G1-VIRAL-001`.
- Prepare review questions for positive fixture group admission scope, negative
  fixture group admission scope, invalidation/lineage blockers, admission
  decision boundary, and whole Gate 1 dependency.
- Do not create fixture admission.
- Do not accept whole Gate 1, process page `021+`, or push.

Admitted inputs:

- `G1FMR-G1-VIRAL-001`:
  `5C5B2530F1EE2A65F4D0C2A52AC22973A62EF4B1CD544EC8184F7751BAC0EEC4`
- `G1FMR-G1-VIRAL-001` report:
  `141FC5D854542ABF7F3D6699A8FAA5DE2FE99E6C4EA82A298AC7A4B12C15431D`
- `G1FMR-G1-VIRAL-001` summary:
  `5AC4EB35225606F7FD0A96BAA4AFB18A2DC26DB4A4C3992A14AC52DCE7E2BBA9`
- `G1FMR-G1-VIRAL-001` manifest:
  `4DEB976065C8976EBAA88746980007863969AA4D742A969D0AF777BB5AB2A7BC`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_admission_decision_prep_plan.md`
- `scripts/build_gate_1_fixture_admission_decision_prep.py`
- `tests/test_gate_1_fixture_admission_decision_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_admission_decision_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not admit fixtures.
- Do not create a fixture admission decision.
- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture admission decision prep only.
- `G1FADP-G1-VIRAL-001`:
  `E624062C3E150993EA699878FAFFB33F9E118EAF9FA4E218E8D42E51C3517D5A`
- `G1FADP-G1-VIRAL-001` report:
  `575948016BD5FAD17B6FEE6F1126D9748F845646F6C5336A2254D58DB3E9A4A5`
- `G1FADP-G1-VIRAL-001` summary:
  `F82BBE589A9FCF283EAE5C193B339FB91D5EC37C60DFAA894FDE7066E52D3870`
- `G1FADP-G1-VIRAL-001` manifest:
  `F9D65BE96E27ED076BFF5E73F813DA0490FC36B172D1C0FE51996FAEC3A1408E`

## BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-ACCEPTANCE-001

Status: `scope_consumed`

Lane: `G1FADAR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2413`:

`g1fadp packet ok; proceed to prepare fixture admission decision acceptance record; no whole Gate 1 acceptance, no page 021+, no push`

Exact action:

- Record Bogdan's acceptance of `G1FADP-G1-VIRAL-001` as fixture admission
  decision prep.
- Consume `G1FADP-G1-VIRAL-001`.
- Create a fixture admission decision acceptance record and admit the fixture
  manifest groups.
- Keep whole Gate 1 acceptance, source-profile acceptance, page `021+`,
  OCR/remediation, mutation, translation/proofreading/implementation, and push
  blocked.

Admitted inputs:

- `G1FADP-G1-VIRAL-001`:
  `E624062C3E150993EA699878FAFFB33F9E118EAF9FA4E218E8D42E51C3517D5A`
- `G1FADP-G1-VIRAL-001` report:
  `575948016BD5FAD17B6FEE6F1126D9748F845646F6C5336A2254D58DB3E9A4A5`
- `G1FADP-G1-VIRAL-001` summary:
  `F82BBE589A9FCF283EAE5C193B339FB91D5EC37C60DFAA894FDE7066E52D3870`
- `G1FADP-G1-VIRAL-001` manifest:
  `F9D65BE96E27ED076BFF5E73F813DA0490FC36B172D1C0FE51996FAEC3A1408E`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_fixture_admission_decision_acceptance_record_plan.md`
- `scripts/accept_gate_1_fixture_admission_decision_prep.py`
- `tests/test_gate_1_fixture_admission_decision_acceptance.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_fixture_admission_decision_acceptance_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, and decision-log synchronization.

Limits:

- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as fixture admission decision acceptance only.
- `G1FADAR-G1-VIRAL-001`:
  `9802BFFFAAC6E5BD22B7897DD449C56B08740F0249830D4DCE02164013A53092`
- `G1FADAR-G1-VIRAL-001` report:
  `40797B2AEE9F2C0026FF222EA2F0A87CE458CB244382069387CF077437A80583`
- `G1FADAR-G1-VIRAL-001` summary:
  `82B29027D0F6A729C88B822E166AE7E828107828702B5D35F2478A2E8CD3C9EE`
- `G1FADAR-G1-VIRAL-001` manifest:
  `449B796B88DD8E305D11D05128066E29280D56703C16F67E0C8B5F1A58D6C443`

## BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-READINESS-RECHECK-PREP-001

Status: `scope_consumed`

Lane: `G1WGARR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2446`, replying `Ок делай` to the bounded
scope proposed in message `2445`:

`proceed with whole Gate 1 acceptance readiness recheck prep; no whole Gate 1 acceptance, no page 021+, no source-profile acceptance, no OCR/render/PDF/raw mutation, no translation/proofreading/implementation, no push, commit`

Exact action:

- Prepare whole Gate 1 acceptance readiness recheck after `G1FADAR-G1-VIRAL-001`.
- Consume `G1FADAR-G1-VIRAL-001`.
- Prepare review questions for future whole Gate 1 acceptance scope, page `021+`
  boundary, acceptance-record boundary, and downstream boundary.
- Do not accept whole Gate 1.
- Do not accept whole source profile, process page `021+`, mutate
  source/OCR/render/PDF/raw assets, translate, proofread, implement, push, or
  create downstream action.

Admitted inputs:

- `G1FADAR-G1-VIRAL-001`:
  `9802BFFFAAC6E5BD22B7897DD449C56B08740F0249830D4DCE02164013A53092`
- `G1FADAR-G1-VIRAL-001` report:
  `40797B2AEE9F2C0026FF222EA2F0A87CE458CB244382069387CF077437A80583`
- `G1FADAR-G1-VIRAL-001` summary:
  `82B29027D0F6A729C88B822E166AE7E828107828702B5D35F2478A2E8CD3C9EE`
- `G1FADAR-G1-VIRAL-001` manifest:
  `449B796B88DD8E305D11D05128066E29280D56703C16F67E0C8B5F1A58D6C443`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_whole_gate_acceptance_readiness_recheck_plan.md`
- `scripts/build_gate_1_whole_gate_acceptance_readiness_recheck.py`
- `tests/test_gate_1_whole_gate_acceptance_readiness_recheck.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_whole_gate_acceptance_readiness_recheck_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not accept whole Gate 1.
- Do not accept whole source profile.
- Do not admit new or broader fixtures beyond `G1FADAR-G1-VIRAL-001`.
- Do not process, authorize, or accept page 021 or later.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as whole Gate 1 acceptance readiness recheck prep only.
- `G1WGARR-G1-VIRAL-001`:
  `0637943A6B51CCD6BC0D9C434333F8A5F47318B14D843A569374400BE2B84B8B`
- `G1WGARR-G1-VIRAL-001` report:
  `C813875F483AE5841C322E24729EA99C8C46790461141F3AE4D24AB6978DB772`
- `G1WGARR-G1-VIRAL-001` summary:
  `357BEB904BF478E7E17DC8F8A63BBEF9720AD7316E4484592131A286D68DB429`
- `G1WGARR-G1-VIRAL-001` manifest:
  `B48C4C7C095464E27A2D31D60F427FBA43F096A22D5CE0A963BF071D6C028E76`

## BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-DECISION-RECORD-001

Status: `scope_consumed`

Lane: `G1WGADR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2458`:

`g1wgarr packet ok; proceed to prepare whole Gate 1 acceptance decision record limited to pages 001-020 and G1FADAR admitted fixture manifest groups; no page 021+, no source-profile acceptance beyond this Gate 1 record, no OCR/render/PDF/raw mutation, no translation/proofreading/implementation, no push, commit`

Exact action:

- Record Bogdan's acceptance of `G1WGARR-G1-VIRAL-001` as whole Gate 1
  acceptance readiness recheck.
- Consume `G1WGARR-G1-VIRAL-001`.
- Create a whole Gate 1 acceptance decision record limited to pages 001-020 and
  `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups.
- Keep page `021+`, source-profile acceptance beyond this Gate 1 record,
  OCR/remediation, mutation, translation/proofreading/implementation, and push
  blocked.

Admitted inputs:

- `G1WGARR-G1-VIRAL-001`:
  `0637943A6B51CCD6BC0D9C434333F8A5F47318B14D843A569374400BE2B84B8B`
- `G1WGARR-G1-VIRAL-001` report:
  `C813875F483AE5841C322E24729EA99C8C46790461141F3AE4D24AB6978DB772`
- `G1WGARR-G1-VIRAL-001` summary:
  `357BEB904BF478E7E17DC8F8A63BBEF9720AD7316E4484592131A286D68DB429`
- `G1WGARR-G1-VIRAL-001` manifest:
  `B48C4C7C095464E27A2D31D60F427FBA43F096A22D5CE0A963BF071D6C028E76`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_1_whole_gate_acceptance_decision_record_plan.md`
- `scripts/accept_gate_1_whole_gate_acceptance_readiness_recheck.py`
- `tests/test_gate_1_whole_gate_acceptance_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_whole_gate_acceptance_decision_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Accept whole Gate 1 only for pages 001-020 and `G1FADAR-G1-VIRAL-001`
  admitted fixture manifest groups.
- Do not accept, process, or authorize page 021 or later.
- Do not create source-profile acceptance beyond this Gate 1 record.
- Do not admit new or broader fixtures.
- Do not execute OCR or OCR remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate, proofread, implement, push, or create any downstream
  action.

Run output status:

- Generated and verified as bounded whole Gate 1 acceptance decision record
  only.
- `G1WGADR-G1-VIRAL-001`:
  `0E10B81021474344A5D244CAA7DA51660A4D8756C153023D911C4DD51A790379`
- `G1WGADR-G1-VIRAL-001` report:
  `0784A6AE4F1FD39002AAB5533AC58973E63251BD24108468DBC4792217633547`
- `G1WGADR-G1-VIRAL-001` summary:
  `0B64928DC5F48152C9F6AEE90D51C9578159C9743344C20540F8D2D96D57AB09`
- `G1WGADR-G1-VIRAL-001` manifest:
  `CC88C898E3943A7EE8E27484BCF13F51537014B3E9B6116307D4965744196D29`

## BA-G1-VIRAL-CORE-0-1-IMPLEMENTATION-PLANNING-PREP-001

Status: `scope_consumed`

Lane: `C01IPP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2470`:

`proceed with core_0_1_implementation_planning_prep from G1WGADR; no implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no source-profile acceptance beyond G1WGADR, no push, commit`

Exact action:

- Prepare Core 0.1 implementation planning material after
  `G1WGADR-G1-VIRAL-001`.
- Consume `G1WGADR-G1-VIRAL-001`.
- Decompose Core 0.1 into bounded planning work packages and identify a
  candidate first implementation slice for a future separate authorization.
- Record required receipts before any runtime implementation may start.
- Do not create implementation, implementation authorization, page `021+`,
  source-profile acceptance beyond `G1WGADR`, OCR/render/PDF/raw mutation,
  translation/proofreading, push, or downstream action.

Admitted inputs:

- `G1WGADR-G1-VIRAL-001`:
  `0E10B81021474344A5D244CAA7DA51660A4D8756C153023D911C4DD51A790379`
- `G1WGADR-G1-VIRAL-001` report:
  `0784A6AE4F1FD39002AAB5533AC58973E63251BD24108468DBC4792217633547`
- `G1WGADR-G1-VIRAL-001` summary:
  `0B64928DC5F48152C9F6AEE90D51C9578159C9743344C20540F8D2D96D57AB09`
- `G1WGADR-G1-VIRAL-001` manifest:
  `CC88C898E3943A7EE8E27484BCF13F51537014B3E9B6116307D4965744196D29`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_implementation_planning_prep_plan.md`
- `scripts/build_core_0_1_implementation_planning_prep.py`
- `tests/test_core_0_1_implementation_planning_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_implementation_planning_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not create runtime implementation or an implementation authorization
  receipt.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not create source-profile acceptance beyond `G1WGADR-G1-VIRAL-001`.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 implementation planning prep only.
- `C01IPP-G1-VIRAL-001`:
  `D2DD97D83920B76F22B93B443EF5DC1FE3742C3FA167AF721B1ECD670498273A`
- `C01IPP-G1-VIRAL-001` report:
  `437CD9369ABDFF1589C695387B5EE379D43DECA7830F7C427716F871FC56F85C`
- `C01IPP-G1-VIRAL-001` summary:
  `8DE4707466B0DC254DC4C0DCEED59EB8D5A592E5AE01F5B434E7FD220F438291`
- `C01IPP-G1-VIRAL-001` manifest:
  `2B008C786F1C532923DFFC8031BE3DE194D874AEF770CEED802E3376570855D8`

## BA-G1-VIRAL-CORE-0-1-IMPLEMENTATION-AUTHORIZATION-RECEIPT-001

Status: `scope_consumed`

Lane: `C01IAR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2485`:

`c01ipp packet ok; proceed to prepare Core 0.1 implementation authorization receipt from C01IPP; no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no source-profile acceptance beyond G1WGADR, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01IPP-G1-VIRAL-001` as Core 0.1
  implementation planning prep.
- Consume `C01IPP-G1-VIRAL-001`.
- Prepare a Core 0.1 implementation authorization receipt that checks the
  prerequisite list and records which prerequisites still block runtime
  implementation.
- Keep the candidate first slice as planning material only.
- Do not create runtime implementation, first-slice design prep authorization,
  OCR/render/PDF/raw mutation, translation/proofreading, page `021+`,
  source-profile acceptance beyond `G1WGADR`, push, or downstream action.

Admitted inputs:

- `C01IPP-G1-VIRAL-001`:
  `D2DD97D83920B76F22B93B443EF5DC1FE3742C3FA167AF721B1ECD670498273A`
- `C01IPP-G1-VIRAL-001` report:
  `437CD9369ABDFF1589C695387B5EE379D43DECA7830F7C427716F871FC56F85C`
- `C01IPP-G1-VIRAL-001` summary:
  `8DE4707466B0DC254DC4C0DCEED59EB8D5A592E5AE01F5B434E7FD220F438291`
- `C01IPP-G1-VIRAL-001` manifest:
  `2B008C786F1C532923DFFC8031BE3DE194D874AEF770CEED802E3376570855D8`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_implementation_authorization_receipt_plan.md`
- `scripts/build_core_0_1_implementation_authorization_receipt.py`
- `tests/test_core_0_1_implementation_authorization_receipt.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_implementation_authorization_receipt_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not authorize first-slice design prep or runtime start.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not create source-profile acceptance beyond `G1WGADR-G1-VIRAL-001`.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 implementation authorization receipt
  material only.
- `C01IAR-G1-VIRAL-001`:
  `0A20E7555B572FA47DF03073953155ECA9A7E1BC87E9CB2EEE2A373DBD9405A7`
- `C01IAR-G1-VIRAL-001` report:
  `5FA8A73975ACC9E83ACFE92591BCA66E058E69D88667C491D19A0D7B2185B6E8`
- `C01IAR-G1-VIRAL-001` summary:
  `6B62325A152BBFACC3372A5807E55C67F7E80AEBEF51AB96C5295F30B6AD0B98`
- `C01IAR-G1-VIRAL-001` manifest:
  `0F778173065003818C77293A15615E021F72BD1A57E45EE18A05A02F028FD64F`

## BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-DESIGN-PREP-001

Status: `scope_consumed`

Lane: `C01FSDP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2501`:

`c01iar receipt ok; proceed to prepare Core 0.1 first-slice design prep for C01WP-01-phase-1-scaffold-contracts; no runtime implementation, no source-profile lock or acceptance beyond G1WGADR, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01IAR-G1-VIRAL-001` as implementation
  authorization receipt material.
- Consume `C01IAR-G1-VIRAL-001`.
- Prepare first-slice design prep for
  `C01WP-01-phase-1-scaffold-contracts`.
- Define module-boundary, artifact-identity, lineage-trace, and
  acceptance-matrix trace design surfaces for future review.
- Do not create runtime implementation, source-profile lock/acceptance,
  OCR/render/PDF/raw mutation, translation/proofreading, page `021+`, push, or
  downstream action.

Admitted inputs:

- `C01IAR-G1-VIRAL-001`:
  `0A20E7555B572FA47DF03073953155ECA9A7E1BC87E9CB2EEE2A373DBD9405A7`
- `C01IAR-G1-VIRAL-001` report:
  `5FA8A73975ACC9E83ACFE92591BCA66E058E69D88667C491D19A0D7B2185B6E8`
- `C01IAR-G1-VIRAL-001` summary:
  `6B62325A152BBFACC3372A5807E55C67F7E80AEBEF51AB96C5295F30B6AD0B98`
- `C01IAR-G1-VIRAL-001` manifest:
  `0F778173065003818C77293A15615E021F72BD1A57E45EE18A05A02F028FD64F`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_first_slice_design_prep_plan.md`
- `scripts/build_core_0_1_first_slice_design_prep.py`
- `tests/test_core_0_1_first_slice_design_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_first_slice_design_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not create source-profile lock or source-profile acceptance beyond
  `G1WGADR-G1-VIRAL-001`.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 first-slice design prep only.
- `C01FSDP-G1-VIRAL-001`:
  `0A0FC7208959117FC79B288486E206270B8BE0AD66AF7525B465512EF9CDFD81`
- `C01FSDP-G1-VIRAL-001` report:
  `1ECE894197218EDC028CFC89E8979446D84F99B6181835C41C547DA40DB8A4C2`
- `C01FSDP-G1-VIRAL-001` summary:
  `B04F3FE67ACD517069DB035B779AF304620BC6A573AFAED7DCFEAA1C470D5060`
- `C01FSDP-G1-VIRAL-001` manifest:
  `101764F9CAF02C18F88AE982568143A1F07D1BADEC30EBA8B130DE3FC88C1D4B`

## BA-G1-VIRAL-SINGLE-SOURCE-PROFILE-LOCK-OR-PARKING-RECEIPT-001

Status: `scope_consumed`

Lane: `C01SPLPR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2515`:

`c01fsdp packet ok; proceed to prepare single source-profile lock-or-parking receipt for C01WP-01 from C01FSDP; no runtime implementation, no source-profile lock or acceptance beyond this receipt, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01FSDP-G1-VIRAL-001` as first-slice design
  prep material.
- Consume `C01FSDP-G1-VIRAL-001`.
- Prepare a source-profile lock-or-parking receipt for
  `C01WP-01-phase-1-scaffold-contracts`.
- Record source-profile parking only for the C01WP-01 design-prep boundary.
- Do not create a runtime source-profile lock, runtime source-profile
  acceptance, runtime implementation, OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+`, push, or downstream action.

Admitted inputs:

- `C01FSDP-G1-VIRAL-001`:
  `0A0FC7208959117FC79B288486E206270B8BE0AD66AF7525B465512EF9CDFD81`
- `C01FSDP-G1-VIRAL-001` report:
  `1ECE894197218EDC028CFC89E8979446D84F99B6181835C41C547DA40DB8A4C2`
- `C01FSDP-G1-VIRAL-001` summary:
  `B04F3FE67ACD517069DB035B779AF304620BC6A573AFAED7DCFEAA1C470D5060`
- `C01FSDP-G1-VIRAL-001` manifest:
  `101764F9CAF02C18F88AE982568143A1F07D1BADEC30EBA8B130DE3FC88C1D4B`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_source_profile_lock_or_parking_receipt_plan.md`
- `scripts/build_core_0_1_source_profile_lock_or_parking_receipt.py`
- `tests/test_core_0_1_source_profile_lock_or_parking_receipt.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_source_profile_lock_or_parking_receipt_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not create a runtime source-profile lock or source-profile acceptance
  beyond this receipt.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as source-profile lock-or-parking receipt material
  only.
- `C01SPLPR-G1-VIRAL-001`:
  `2E65C839830397E9FCA301CABCE4209AB370CB18867AD57577B61268DA46B5D8`
- `C01SPLPR-G1-VIRAL-001` report:
  `EB8836B1DC0820828200E7C20FD557A08D41B79E9432B65A534C1B44CB9918B7`
- `C01SPLPR-G1-VIRAL-001` summary:
  `B7EE0D1545E98CFA9AAB35B6998DF4467D54BAF64D85E56853258EABCD398DF8`
- `C01SPLPR-G1-VIRAL-001` manifest:
  `919CFF991DE4A89154D37B62B3C371805691C6345E0989E4A845A078430884AF`

## BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-ARCHITECTURE-REVIEW-PACKET-001

Status: `scope_consumed`

Lane: `C01FSARP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2533`:

`c01splpr packet ok; proceed to prepare Core 0.1 first-slice architecture review packet for C01WP-01 from C01SPLPR; no runtime implementation, no source-profile lock or acceptance beyond C01SPLPR, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01SPLPR-G1-VIRAL-001` as source-profile
  lock-or-parking receipt material.
- Consume `C01SPLPR-G1-VIRAL-001`.
- Prepare a Core 0.1 first-slice architecture review packet for
  `C01WP-01-phase-1-scaffold-contracts`.
- Prepare Sol architecture review targets and Terra critique targets for the
  first slice.
- Do not create runtime implementation, runtime source-profile lock,
  source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`,
  OCR/render/PDF/raw mutation, translation/proofreading, page `021+`, push, or
  downstream action.

Admitted inputs:

- `C01SPLPR-G1-VIRAL-001`:
  `2E65C839830397E9FCA301CABCE4209AB370CB18867AD57577B61268DA46B5D8`
- `C01SPLPR-G1-VIRAL-001` report:
  `EB8836B1DC0820828200E7C20FD557A08D41B79E9432B65A534C1B44CB9918B7`
- `C01SPLPR-G1-VIRAL-001` summary:
  `B7EE0D1545E98CFA9AAB35B6998DF4467D54BAF64D85E56853258EABCD398DF8`
- `C01SPLPR-G1-VIRAL-001` manifest:
  `919CFF991DE4A89154D37B62B3C371805691C6345E0989E4A845A078430884AF`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_first_slice_architecture_review_packet_plan.md`
- `scripts/build_core_0_1_first_slice_architecture_review_packet.py`
- `tests/test_core_0_1_first_slice_architecture_review_packet.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_first_slice_architecture_review_packet_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not create a runtime source-profile lock or source-profile acceptance
  beyond `C01SPLPR-G1-VIRAL-001`.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 first-slice architecture review packet
  material only.
- `C01FSARP-G1-VIRAL-001`:
  `2D33226D25C446AB358F9686ACEEA16710236940D7C20A8B628AA8A9CD73B71E`
- `C01FSARP-G1-VIRAL-001` report:
  `A4E6F02F59220685CFDA7EF50A0A4F62C7B41A9AEDD3E0C417448BDC6A8A1ECB`
- `C01FSARP-G1-VIRAL-001` summary:
  `9AA83B65ADF67E7F63481FB898D1B55E5D4F39F67215209C302021A067F865DD`
- `C01FSARP-G1-VIRAL-001` manifest:
  `A668C8D474EE2B8C6B244F811CCA4DE8C933677792096EFEDC07132F75CBFCD8`

## BA-G1-VIRAL-CORE-0-1-ACCEPTANCE-MATRIX-TRACE-REVIEW-001

Status: `scope_consumed`

Lane: `C01AMTR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2542`:

`c01fsarp packet ok; proceed to prepare acceptance-matrix trace review for C01WP-01 from C01FSARP; no runtime implementation, no source-profile lock or acceptance beyond C01SPLPR, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01FSARP-G1-VIRAL-001` as first-slice
  architecture review packet material.
- Consume `C01FSARP-G1-VIRAL-001`.
- Prepare a Core 0.1 acceptance-matrix trace review for
  `C01WP-01-phase-1-scaffold-contracts`.
- Map first-slice acceptance claims to bounded existing evidence.
- Do not create runtime implementation, runtime source-profile lock,
  source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`,
  OCR/render/PDF/raw mutation, translation/proofreading, page `021+`, push, or
  downstream action.

Admitted inputs:

- `C01FSARP-G1-VIRAL-001`:
  `2D33226D25C446AB358F9686ACEEA16710236940D7C20A8B628AA8A9CD73B71E`
- `C01FSARP-G1-VIRAL-001` report:
  `A4E6F02F59220685CFDA7EF50A0A4F62C7B41A9AEDD3E0C417448BDC6A8A1ECB`
- `C01FSARP-G1-VIRAL-001` summary:
  `9AA83B65ADF67E7F63481FB898D1B55E5D4F39F67215209C302021A067F865DD`
- `C01FSARP-G1-VIRAL-001` manifest:
  `A668C8D474EE2B8C6B244F811CCA4DE8C933677792096EFEDC07132F75CBFCD8`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_acceptance_matrix_trace_review_plan.md`
- `scripts/build_core_0_1_acceptance_matrix_trace_review.py`
- `tests/test_core_0_1_acceptance_matrix_trace_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_acceptance_matrix_trace_review_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not create a runtime source-profile lock or source-profile acceptance
  beyond `C01SPLPR-G1-VIRAL-001`.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

- Generated and verified as Core 0.1 acceptance-matrix trace review material
  only.
- `C01AMTR-G1-VIRAL-001`:
  `C694B0C93E2F3EBF49BC71AEC97AA06F8A8877A980E2067434FAC09430286480`
- `C01AMTR-G1-VIRAL-001` report:
  `B75EB03BB48BBDA4946876A961AA0C4BA0524F7A92A7BCFA0C1CCEE3DD23ED3B`
- `C01AMTR-G1-VIRAL-001` summary:
  `8122BF577E1CB37C556F3E3D66BCFA5DC4CC994BD6092C64A0B7C6C51B39366F`
- `C01AMTR-G1-VIRAL-001` manifest:
  `E2503080F3CF43F7752B1CEBC708A98F0940221242E789127AFF26933A963A86`

## BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-PARKING-DECISION-001

Status: `scope_consumed`

Lane: `C01RSPLP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2551`:

`c01amtr packet ok; proceed to prepare runtime source-profile lock-or-parking decision for C01WP-01 from C01AMTR; no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01AMTR-G1-VIRAL-001` as
  acceptance-matrix trace review material.
- Consume `C01AMTR-G1-VIRAL-001`.
- Prepare a runtime source-profile lock-or-parking decision for
  `C01WP-01-phase-1-scaffold-contracts`.
- Record runtime source-profile parking for the first-slice authorization-prep
  boundary only.
- Do not create runtime implementation, runtime source-profile lock, runtime
  source-profile acceptance, OCR/render/PDF/raw mutation,
  translation/proofreading, page `021+`, push, or downstream action.

Admitted inputs:

- `C01AMTR-G1-VIRAL-001`:
  `C694B0C93E2F3EBF49BC71AEC97AA06F8A8877A980E2067434FAC09430286480`
- `C01AMTR-G1-VIRAL-001` report:
  `B75EB03BB48BBDA4946876A961AA0C4BA0524F7A92A7BCFA0C1CCEE3DD23ED3B`
- `C01AMTR-G1-VIRAL-001` summary:
  `8122BF577E1CB37C556F3E3D66BCFA5DC4CC994BD6092C64A0B7C6C51B39366F`
- `C01AMTR-G1-VIRAL-001` manifest:
  `E2503080F3CF43F7752B1CEBC708A98F0940221242E789127AFF26933A963A86`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_runtime_source_profile_lock_or_parking_decision_plan.md`
- `scripts/build_core_0_1_runtime_source_profile_lock_or_parking_decision.py`
- `tests/test_core_0_1_runtime_source_profile_lock_or_parking_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_runtime_source_profile_lock_or_parking_decision_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not create a runtime source-profile lock or runtime source-profile
  acceptance.
- Do not create source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 runtime source-profile parking decision
  material only.
- `C01RSPLP-G1-VIRAL-001`:
  `7C69F0EBEF416C5A8646836E31EC89BC66AA5A60B302080C890605830A58CC36`
- `C01RSPLP-G1-VIRAL-001` report:
  `A8AFDB207A40E9ADFD2624D2679BDC92E5C6055FA07CF0ECEA28E555761E20E1`
- `C01RSPLP-G1-VIRAL-001` summary:
  `019266B4C3BFD1622731A914856F92104D36F92CEB410FBADC1BDDBD79D8A425`
- `C01RSPLP-G1-VIRAL-001` manifest:
  `11398446A0D15736CC004A2C4FAD998AD82AF75B97151B5F0F9430C8E59326FA`

## BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-RUNTIME-AUTHORIZATION-PREP-001

Status: `scope_consumed`

Lane: `C01RSAP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2566`:

`c01rsplp packet ok; proceed to prepare Core 0.1 first-slice runtime authorization prep for C01WP-01 from C01RSPLP; no runtime implementation, no runtime source-profile lock/acceptance, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01RSPLP-G1-VIRAL-001` as runtime
  source-profile parking decision material.
- Consume `C01RSPLP-G1-VIRAL-001`.
- Prepare first-slice runtime authorization prep material for
  `C01WP-01-phase-1-scaffold-contracts`.
- Canonically map `C01RSAP-G1-VIRAL-001` to
  `core_0_1_first_slice_runtime_authorization_prep`.
- Reference runtime source-profile parking without creating runtime
  source-profile lock or acceptance.
- Do not create runtime implementation, runtime authorization grant, runtime
  start, runtime source-profile lock, runtime source-profile acceptance,
  OCR/render/PDF/raw mutation, translation/proofreading, page `021+`, push, or
  downstream action.

Admitted inputs:

- `C01RSPLP-G1-VIRAL-001`:
  `7C69F0EBEF416C5A8646836E31EC89BC66AA5A60B302080C890605830A58CC36`
- `C01RSPLP-G1-VIRAL-001` report:
  `A8AFDB207A40E9ADFD2624D2679BDC92E5C6055FA07CF0ECEA28E555761E20E1`
- `C01RSPLP-G1-VIRAL-001` summary:
  `019266B4C3BFD1622731A914856F92104D36F92CEB410FBADC1BDDBD79D8A425`
- `C01RSPLP-G1-VIRAL-001` manifest:
  `11398446A0D15736CC004A2C4FAD998AD82AF75B97151B5F0F9430C8E59326FA`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_first_slice_runtime_authorization_prep_plan.md`
- `scripts/build_core_0_1_first_slice_runtime_authorization_prep.py`
- `tests/test_core_0_1_first_slice_runtime_authorization_prep.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_first_slice_runtime_authorization_prep_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not create runtime authorization grant or runtime start.
- Do not create a runtime source-profile lock or runtime source-profile
  acceptance.
- Do not create source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 first-slice runtime authorization prep
  material only.
- `C01RSAP-G1-VIRAL-001`:
  `CDCC31F41F7988C7017217DBD0E4F420C46D99A65CC51EC85913C28E501DB741`
- `C01RSAP-G1-VIRAL-001` report:
  `D462D23C2DB50770B3E1386053C1CC4295151A558BB286EC41DCC436DD970C5B`
- `C01RSAP-G1-VIRAL-001` summary:
  `6338CDA040FDA9E70FA0F6E756009D69AE14C27F7DFC4AB6769B8CD731127491`
- `C01RSAP-G1-VIRAL-001` manifest:
  `1D20D2BD7C32774B8C91378F11A5B38EDBAE5DE01FC6390AE7DFA3E67E4BD914`

## BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-RUNTIME-AUTHORIZATION-DECISION-001

Status: `scope_consumed`

Lane: `C01RSAD-G1-VIRAL-001`

Authority: Bogdan Telegram message `2569`:

`c01rsap packet ok; proceed to prepare Core 0.1 first-slice runtime authorization decision for C01WP-01 from C01RSAP; no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01RSAP-G1-VIRAL-001` as first-slice runtime
  authorization prep material.
- Consume `C01RSAP-G1-VIRAL-001`.
- Prepare a non-executing first-slice runtime authorization decision record for
  `C01WP-01-phase-1-scaffold-contracts`.
- Canonically map `C01RSAD-G1-VIRAL-001` to
  `core_0_1_first_slice_runtime_authorization_decision`.
- Do not create runtime implementation, runtime start/execution, runtime
  source-profile lock, runtime source-profile acceptance, OCR/render/PDF/raw
  mutation, translation/proofreading, page `021+`, push, or downstream action.

Admitted inputs:

- `C01RSAP-G1-VIRAL-001`:
  `CDCC31F41F7988C7017217DBD0E4F420C46D99A65CC51EC85913C28E501DB741`
- `C01RSAP-G1-VIRAL-001` report:
  `D462D23C2DB50770B3E1386053C1CC4295151A558BB286EC41DCC436DD970C5B`
- `C01RSAP-G1-VIRAL-001` summary:
  `6338CDA040FDA9E70FA0F6E756009D69AE14C27F7DFC4AB6769B8CD731127491`
- `C01RSAP-G1-VIRAL-001` manifest:
  `1D20D2BD7C32774B8C91378F11A5B38EDBAE5DE01FC6390AE7DFA3E67E4BD914`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_first_slice_runtime_authorization_decision_plan.md`
- `scripts/build_core_0_1_first_slice_runtime_authorization_decision.py`
- `tests/test_core_0_1_first_slice_runtime_authorization_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_first_slice_runtime_authorization_decision_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not authorize runtime start or execution.
- Do not create a runtime source-profile lock or runtime source-profile
  acceptance.
- Do not create source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 first-slice runtime authorization
  decision record material only.
- `C01RSAD-G1-VIRAL-001`:
  `6C5C1481D1E77693E49F2A3670B0E4D0870292CA2C42C075F297379C975F514C`
- `C01RSAD-G1-VIRAL-001` report:
  `490EB27DAD6026951825859779999B5D06B4A1D56F306EB6727E6E9F8FEC1EAC`
- `C01RSAD-G1-VIRAL-001` summary:
  `03F19C1FF29E60425899982070E427E4497055BEA8016044C950982F8F4275AE`
- `C01RSAD-G1-VIRAL-001` manifest:
  `E9D6DA05E6509919008F67C9356DEC397E1F8A56F4A54B44047EBF0266DD0762`

## BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-ACCEPTANCE-DECISION-001

Status: `scope_consumed`

Lane: `C01RSPLAD-G1-VIRAL-001`

Authority: Bogdan Telegram message `2573`:

`c01rsad packet ok; proceed to prepare Core 0.1 runtime source-profile lock-or-acceptance decision for C01WP-01 from C01RSAD; no runtime implementation, no runtime start/execution, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit`

Exact action:

- Record Bogdan's acceptance of `C01RSAD-G1-VIRAL-001` as non-executing
  first-slice runtime authorization decision material.
- Consume `C01RSAD-G1-VIRAL-001`.
- Prepare a runtime source-profile lock-or-acceptance decision record for
  `C01WP-01-phase-1-scaffold-contracts`.
- Canonically map `C01RSPLAD-G1-VIRAL-001` to
  `core_0_1_runtime_source_profile_lock_or_acceptance_decision`.
- Record no runtime source-profile lock and no runtime source-profile
  acceptance unless separately admitted concrete runtime source-profile
  evidence exists.
- Do not create runtime implementation, runtime start/execution, runtime
  source-profile lock, runtime source-profile acceptance, OCR/render/PDF/raw
  mutation, translation/proofreading, page `021+`, push, or downstream action.

Admitted inputs:

- `C01RSAD-G1-VIRAL-001`:
  `6C5C1481D1E77693E49F2A3670B0E4D0870292CA2C42C075F297379C975F514C`
- `C01RSAD-G1-VIRAL-001` report:
  `490EB27DAD6026951825859779999B5D06B4A1D56F306EB6727E6E9F8FEC1EAC`
- `C01RSAD-G1-VIRAL-001` summary:
  `03F19C1FF29E60425899982070E427E4497055BEA8016044C950982F8F4275AE`
- `C01RSAD-G1-VIRAL-001` manifest:
  `E9D6DA05E6509919008F67C9356DEC397E1F8A56F4A54B44047EBF0266DD0762`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_runtime_source_profile_lock_or_acceptance_decision_plan.md`
- `scripts/build_core_0_1_runtime_source_profile_lock_or_acceptance_decision.py`
- `tests/test_core_0_1_runtime_source_profile_lock_or_acceptance_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_runtime_source_profile_lock_or_acceptance_decision_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not authorize or create runtime implementation.
- Do not authorize runtime start or execution.
- Do not create a runtime source-profile lock or runtime source-profile
  acceptance.
- Do not create source-profile acceptance beyond `C01SPLPR-G1-VIRAL-001`.
- Do not execute OCR, render, PDF parsing/text-layer extraction, or OCR
  remediation.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not translate or proofread.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not push or create any downstream action.

Run output status:

- Generated and verified as Core 0.1 runtime source-profile
  lock-or-acceptance decision record material only.
- `C01RSPLAD-G1-VIRAL-001`:
  `416A7687AC9CD95DD00A909A642C2E8C64C17339E47E1010F3C6E700DDC58DB7`
- `C01RSPLAD-G1-VIRAL-001` report:
  `1D797D66CB1B9ECDDA2AD2EB9DC2C201C1246AA5B922A6C15F91F6EA7EEBFDA0`
- `C01RSPLAD-G1-VIRAL-001` summary:
  `8C5570DA88CFC0D2CB162C61F8EA76187CD4A016FD526EECDBC5E141F8510A84`
- `C01RSPLAD-G1-VIRAL-001` manifest:
  `A46062E47A18DC8DDED198B4AC8B61F5DA90C98EDC244B4C8105F130F98E3399`

## BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-ACCEPTANCE-MACHINE-REVIEW-ACCEPTANCE-001

Status: `scope_consumed`

Lane: `C01RSPLADMR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2583`:

`делай 1-5 с проверкой через сол и терру, вместо "хуман ревью". зови перед запуском п.6`

Exact action:

- Replace the human review gate for `C01RSPLAD-G1-VIRAL-001` with a bounded
  Sol/Terra machine-review acceptance for points 1-5 only.
- Consume `C01RSPLAD-G1-VIRAL-001`.
- Do not treat Sol/Terra as authorization for point 6 or any actual extraction.
- Do not create runtime implementation, runtime start/execution, runtime
  source-profile lock, runtime source-profile acceptance, OCR/render/PDF/raw
  mutation, PDF parsing/text-layer extraction, translation/proofreading,
  page `021+`, push, or downstream execution.

Admitted inputs:

- `C01RSPLAD-G1-VIRAL-001`:
  `416A7687AC9CD95DD00A909A642C2E8C64C17339E47E1010F3C6E700DDC58DB7`
- `C01RSPLAD-G1-VIRAL-001` report:
  `1D797D66CB1B9ECDDA2AD2EB9DC2C201C1246AA5B922A6C15F91F6EA7EEBFDA0`
- `C01RSPLAD-G1-VIRAL-001` summary:
  `8C5570DA88CFC0D2CB162C61F8EA76187CD4A016FD526EECDBC5E141F8510A84`
- `C01RSPLAD-G1-VIRAL-001` manifest:
  `A46062E47A18DC8DDED198B4AC8B61F5DA90C98EDC244B4C8105F130F98E3399`

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_text_extraction_trial_readiness_chain_plan.md`
- `scripts/build_core_0_1_text_extraction_trial_readiness_chain.py`
- `tests/test_core_0_1_text_extraction_trial_readiness_chain.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/c01rspladmr_G1_VIRAL_001/*`
- Current-state, roadmap, plan/context, release charter, qualification
  protocol, phase/gate hierarchy, fixtures README, and decision-log
  synchronization.

Limits:

- Do not run OCR, render, PDF parsing/text-layer extraction, or text
  extraction.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation.
- Do not authorize runtime start or execution.
- Do not create a runtime source-profile lock or runtime source-profile
  acceptance.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures.
- Do not translate, proofread, push, or create downstream execution.

Run output status:

- Generated and verified as Core 0.1 runtime source-profile
  lock-or-acceptance machine-review acceptance material only.
- `C01RSPLADMR-G1-VIRAL-001`:
  `ADD6FBDBA8045DA23CB4410BBA8374337ABC1AB2FA573AC1E942F2AB67DF89CB`
- `C01RSPLADMR-G1-VIRAL-001` report:
  `5C09FB99634BBC7EB7F2E42EB730B83417B04A6CE7D4DEC2CCD65C4A038A4687`
- `C01RSPLADMR-G1-VIRAL-001` summary:
  `04A367E1805D40BEA063A80D316BCCF829D2E150DAD4BF506019BEE8CADFBF37`
- `C01RSPLADMR-G1-VIRAL-001` manifest:
  `54646DEE18C455AF1D105CF91B52D96832C6099BC26F95CF596A95487ADF70D2`

## BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-EVIDENCE-PREP-001

Status: `scope_consumed`

Lane: `C01RSPEP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2583`:

`делай 1-5 с проверкой через сол и терру, вместо "хуман ревью". зови перед запуском п.6`

Exact action:

- Prepare runtime source-profile evidence surfaces for a future extraction
  trial profile.
- Consume `C01RSPLADMR-G1-VIRAL-001`.
- Preserve that this is evidence-prep only and not source observation,
  extraction, profile acceptance, runtime implementation, or runtime start.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/c01rspep_G1_VIRAL_001/*`
- Chain builder/test/plan and status/roadmap/doc synchronization.

Limits:

- Do not run OCR, render, PDF parsing/text-layer extraction, or text
  extraction.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Do not create runtime source-profile lock/acceptance.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Generated and verified as Core 0.1 runtime source-profile evidence prep
  material only.
- `C01RSPEP-G1-VIRAL-001`:
  `94256343E3356CDC01FDD14C871756DDF02EF256B832E595E059E38F1F53E1F6`
- `C01RSPEP-G1-VIRAL-001` report:
  `6D69B0D37721CD6C4BD9B2F145CBD8963C2A0197091142E083FD8C91417B1682`
- `C01RSPEP-G1-VIRAL-001` summary:
  `3C03950023621D622CDABD80617A558D3DCB49232CA0E9980C535A88CB33BA16`
- `C01RSPEP-G1-VIRAL-001` manifest:
  `03AFBE176C926320252D59D3F9CE8AB9D5A9A178ECD64F98254207CD1CE4A03C`

## BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-EXTRACTION-TRIAL-LOCK-OR-ACCEPTANCE-DECISION-001

Status: `scope_consumed`

Lane: `C01RSPETD-G1-VIRAL-001`

Authority: Bogdan Telegram message `2583`:

`делай 1-5 с проверкой через сол и терру, вместо "хуман ревью". зови перед запуском п.6`

Exact action:

- Record a runtime source-profile extraction-trial lock-or-acceptance decision
  for the future smoke extraction trial profile.
- Consume `C01RSPEP-G1-VIRAL-001`.
- Bind the decision to a future user-called extraction trial only; do not run
  extraction in this layer.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/c01rspetd_G1_VIRAL_001/*`
- Chain builder/test/plan and status/roadmap/doc synchronization.

Limits:

- Do not run OCR, render, PDF parsing/text-layer extraction, or text
  extraction.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Limit any profile acceptance to future extraction-trial decision material;
  do not create actual runtime source-profile lock/acceptance artifacts.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Generated and verified as Core 0.1 runtime source-profile extraction-trial
  lock-or-acceptance decision material only.
- `C01RSPETD-G1-VIRAL-001`:
  `095023C76B8476BAF0638453409E9FA5A404EBC30D900EE8917E0F19FC7CFC3D`
- `C01RSPETD-G1-VIRAL-001` report:
  `732B4ABA51C1C50C0F607DE060D9D629BF2975193505EB9279D36E6A132E1850`
- `C01RSPETD-G1-VIRAL-001` summary:
  `58BF54103E5AE03EF2F78EFB9BF32AAD8753B8D6C6C868D4F2DCB3C949935157`
- `C01RSPETD-G1-VIRAL-001` manifest:
  `E47B1BA8A7376BCD0394C95C4BFD4D3334C94947B63BFC60E596A546041770D2`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-TRIAL-AUTHORIZATION-PREP-001

Status: `scope_consumed`

Lane: `C01TETAP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2583`:

`делай 1-5 с проверкой через сол и терру, вместо "хуман ревью". зови перед запуском п.6`

Exact action:

- Prepare text extraction trial authorization context for a future smoke trial.
- Consume `C01RSPETD-G1-VIRAL-001`.
- Keep all actual OCR/PDF text-layer extraction blocked until Bogdan is called
  before point 6.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/c01tetap_G1_VIRAL_001/*`
- Chain builder/test/plan and status/roadmap/doc synchronization.

Limits:

- Do not run OCR, render, PDF parsing/text-layer extraction, or text
  extraction.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Generated and verified as Core 0.1 text extraction trial authorization prep
  material only.
- `C01TETAP-G1-VIRAL-001`:
  `3BC80A4DA81018C5FE1810E44B5B5B579E035197E72422F505AD6CEF3E84F159`
- `C01TETAP-G1-VIRAL-001` report:
  `CB02013011992A005EEBEE8F35C06355B220F0A487C9FE1F84DD4C3F8C6B82BC`
- `C01TETAP-G1-VIRAL-001` summary:
  `0003AC55BA52C503F41B8DC55601F4E2CD6B43B849F30570473C0C292BC1EA7E`
- `C01TETAP-G1-VIRAL-001` manifest:
  `8D8F5D6CDF8ABCB74987CCCDDBAF157D81FE59471CBA56C993088626671B8B52`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-TRIAL-DECISION-001

Status: `scope_consumed`

Lane: `C01TETD-G1-VIRAL-001`

Authority: Bogdan Telegram message `2583`:

`делай 1-5 с проверкой через сол и терру, вместо "хуман ревью". зови перед запуском п.6`

Exact action:

- Record a non-executing text extraction trial decision for a future smoke
  trial.
- Consume `C01TETAP-G1-VIRAL-001`.
- Stop before point 6 and call Bogdan before any actual extraction run.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/c01tetd_G1_VIRAL_001/*`
- Chain builder/test/plan and status/roadmap/doc synchronization.

Limits:

- Do not run OCR, render, PDF parsing/text-layer extraction, or text
  extraction.
- Do not mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Generated and verified as Core 0.1 text extraction trial decision material
  only; point 6 remains blocked until Bogdan is called.
- `C01TETD-G1-VIRAL-001`:
  `30787FEA297DD4164CC1B4E83CB1AA1595442F52F08FFACFFCE530E1DF4CB2B8`
- `C01TETD-G1-VIRAL-001` report:
  `C0F083C25F93D8FC7CEA747C8704476A73DD12B5C73E8C815D1EC2623EAC2ABA`
- `C01TETD-G1-VIRAL-001` summary:
  `C407BF77CE1E474FDF459100E54EFF76AB197BD08DD4FE0F744DFEA5315010D8`
- `C01TETD-G1-VIRAL-001` manifest:
  `B956ACFD4B6C23A3CDF05BB898949369018322E8CA4BEF5F2C5B8F80A77F678A`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-001

Status: `scope_consumed`

Lane: `C01TESP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2597`:

`теперь согласен, приступай`

Exact action:

- Run the first bounded Core 0.1 text extraction smoke over page 009 text
  evidence crops only.
- Consume `C01TETD-G1-VIRAL-001`.
- Use frozen OCR candidate `OCM-G1-VIRAL-001` /
  `OCR-G1-VIRAL-TESSERACT-ENG-PSM6-001`.
- Treat existing page 009 image/crop/reference assets as read-only inputs.
- Produce candidate-only OCR text, TSV, manifest, report, and metrics in a new
  output directory.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_smoke_p009_G1_VIRAL_001/*`
- Fail-closed builder/test and status/roadmap/doc synchronization.

Limits:

- Do not overwrite page 009 image, crop, review, reference, semantic-map, or
  accepted-text assets.
- Do not parse PDF or use PDF text-layer extraction.
- Do not run render or mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Do not accept candidate OCR as source text, page-complete text, fixture
  evidence, source-profile acceptance, or runtime profile lock.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Actual OCR smoke executed on the two read-only P009 text-evidence crop PNGs.
- Outcome: candidate evidence only, not accepted source/profile evidence.
- Quality signal: noisy candidate text with edge artifacts; sequence similarity
  against `page_009_ocr_verified_text_map.md` is `0.460269`.
- Recommended next route: OCR smoke remediation/preprocessing decision before
  broader extraction, not page 021 and not acceptance.
- `C01TESP-G1-VIRAL-001` candidate text:
  `C2F4DB0E5545CF28D36B6E4BFF2A043D8D853BA02E8D23C84C8542429D1F9BF8`
- `C01TESP-G1-VIRAL-001` normalized candidate text:
  `0536F247495D03B0312CF5BDD4CE9F78E2AE2822F0E8DC3142ABBE48C04DAB76`
- `C01TESP-G1-VIRAL-001` report:
  `DFA8C10CDE54666C6387F74CCF1972A1ABE664A76BDFC0C3B5F955EA46AC6CDC`
- `C01TESP-G1-VIRAL-001` summary:
  `8044714CED0E35B24A247BABFCD14D3DA85A6F9A29026A7E7FC99FB7DC1AB7AE`
- `C01TESP-G1-VIRAL-001` manifest:
  `3E52A963B37FCF413F739622DB1875B9D79D6C96EDECCB993EABB2346DF70FC7`
- `C01TESP-G1-VIRAL-001` left TSV:
  `615E1EB528F02D5D218985A3FAC2425E455A66452D79DFC8A2ABD52BAE9E6060`
- `C01TESP-G1-VIRAL-001` right TSV:
  `3137049756088BBA424569B31ADEF6B56B127CC48D20A9D6F974E89CA866AD2A`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-REMEDIATION-MATRIX-001

Status: `scope_consumed`

Lane: `C01TESRM-G1-VIRAL-001`

Authority: Bogdan Telegram message `2609`:

`иди по этому плану 1-5`

Exact action:

- Commit the existing `C01TESP-G1-VIRAL-001` smoke evidence first.
- Run a bounded P009-only OCR smoke remediation/preprocessing matrix over the
  same read-only P009 text-evidence crop PNGs.
- Use a new fail-closed P009-specific runner; do not reuse the older broad
  remediation matrix runner as-is.
- Test trim/mask, grayscale/autocontrast, threshold, denoise/sharpen, PSM
  variants `6`, `4`, `11`, and split header/body candidates.
- Produce candidate-only remediation outputs, rankings, hashes, and metrics.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001/*`
- Fail-closed builder/test and status/roadmap/doc synchronization.

Limits:

- Do not overwrite page 009 image, crop, review, reference, semantic-map, or
  accepted-text assets.
- Do not parse PDF or use PDF text-layer extraction.
- Do not run render or mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Do not accept candidate OCR as source text, page-complete text, fixture
  evidence, source-profile acceptance, or runtime profile lock.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Actual P009-only OCR remediation matrix executed on the two read-only P009
  text-evidence crop PNGs.
- Outcome: candidate remediation evidence only, not accepted source/profile
  evidence.
- Best candidate: `trim_mask_psm4` (`edge_mask_trim`, PSM 4).
- Quality signal: sequence similarity improved from `0.460269` to `0.9993`;
  token recall is `0.996324`; improvement over baseline is `0.539031`.
- Recommended next route: freeze `trim_mask_psm4` as a candidate smoke profile
  and consider a same-profile bounded smoke on P010 or P015 only, not page
  `021+`.
- `C01TESRM-G1-VIRAL-001` report:
  `622B90068710E8F1A6EBBD5667F643641A51B765CB8DB077A49DB5C67AFDFEA5`
- `C01TESRM-G1-VIRAL-001` summary:
  `F48907CD2CF49FE7FCF95454B193F2564EE42E9EC7375AF3A07E35F65593F1FF`
- `C01TESRM-G1-VIRAL-001` manifest:
  `AD0DF2BB6E75F585717BF13AC856890958AC9B989EDAD85CA446B96F8BBFB009`
- `C01TESRM-G1-VIRAL-001` rankings:
  `28BF755676BE6DD3CAA1952B3561301D62904EF99C67E3A10687B3261855ACB2`
- `C01TESRM-G1-VIRAL-001` best candidate text:
  `162CC1B44935F7427313BC76332F4627B569A5CECD09A84B0FEBE90255702CB5`
- `C01TESRM-G1-VIRAL-001` best normalized candidate text:
  `07E2DF657135041040471291AAC63D361170E3867D10CC17E26F80490C6A7A7E`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P010-TRIM-MASK-PSM4-001

Status: `scope_consumed`

Lane: `C01TESP010-G1-VIRAL-001`

Authority: Bogdan Telegram message `2622`:

`ок. пошли делать 010`

Exact action:

- Run one bounded P010-only same-profile OCR smoke.
- Consume `C01TESRM-G1-VIRAL-001` as the source selected/recommended candidate
  profile evidence.
- Use exactly one candidate: `trim_mask_psm4` (`edge_mask_trim`, PSM 4).
- Use only the existing P010 page-complete review text-evidence crop PNGs as
  read-only inputs, in verified logical order: `1b`, `5b`, `2b`, `6b`.
- Compare against `page_010_ocr_verified_text_map.md` for metrics only.
- Produce candidate-only OCR text, TSV, prepared inputs, manifest, report, and
  summary in a new output directory.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001/*`
- Fail-closed builder/test and status/roadmap/doc synchronization.

Limits:

- Do not overwrite P010 image, crop, review, reference, semantic-map, text-map,
  page-complete, or accepted-text assets.
- Do not run a broader P010 matrix or alternate PSM/variant ranking.
- Do not parse PDF or use PDF text-layer extraction.
- Do not run render or mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Do not accept candidate OCR as source text, page-complete text, fixture
  evidence, source-profile acceptance, semantic acceptance, page-status
  mutation, or runtime profile lock.
- Do not accept, process, or authorize page 021 or later.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Actual P010-only same-profile OCR smoke executed on four read-only P010
  text-evidence crop PNGs.
- Outcome: candidate same-profile generalization evidence only, not accepted
  source/profile/semantic/page-status evidence.
- Quality signal: sequence similarity against `page_010_ocr_verified_text_map.md`
  is `0.998867`; token recall is `0.995825`.
- Recommended next route: decide whether to run one more bounded same-profile
  smoke on P015 or stop the smoke ladder; do not proceed to page `021+`.
- `C01TESP010-G1-VIRAL-001` report:
  `544EC833934E63B7EBDFC40DB7B25D71ED878AF800B300CE2F9A4950DFCDC4D6`
- `C01TESP010-G1-VIRAL-001` summary:
  `448F92E29134AF00E3924EAD5EE7F713CD9A2D96B020110BF30268D84485D616`
- `C01TESP010-G1-VIRAL-001` manifest:
  `D95B1B851310F36A954162C8030EE18E2B8E69642C03E336E5CA54B953C374CA`
- `C01TESP010-G1-VIRAL-001` candidate text:
  `2C0B879FF21122D86D9D000934DBEF8227E461C3CBDE38D52902468DF5C13744`
- `C01TESP010-G1-VIRAL-001` normalized candidate text:
  `D1590D716B493F62F17921118017EB1A21CE4946266785E7ED3DA439373388F5`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P015-TRIM-MASK-PSM4-001

Status: `scope_consumed`

Lane: `C01TESP015-G1-VIRAL-001`

Authority: Bogdan Telegram message `2629`:

`принято`

Exact action:

- Run one bounded P015-only same-profile OCR smoke.
- Consume `C01TESRM-G1-VIRAL-001` as the source selected/recommended candidate
  profile evidence and `C01TESP010-G1-VIRAL-001` as prior same-profile ladder
  context.
- Use exactly one candidate: `trim_mask_psm4` (`edge_mask_trim`, PSM 4).
- Use only the existing P015 page-complete review text-evidence crop PNGs as
  read-only inputs: `1_P015-timeline-text-evidence.png` and
  `2_P015-history-text-evidence.png`.
- Compare against `page_015_text_map.md` for metrics only. This is a
  `reference_text_map`, not an OCR-verified text map.
- Produce candidate-only OCR text, TSV, prepared inputs, manifest, report, and
  summary in a new output directory.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_smoke_p015_trim_mask_psm4_G1_VIRAL_001/*`
- Fail-closed builder/test and status/roadmap/doc synchronization.

Limits:

- Do not overwrite P015 image, crop, review, reference, semantic-map, text-map,
  page-complete, or accepted-text assets.
- Do not OCR the P015 visual anchor, full page image, triage duplicates, PDF,
  raw/source, or continuation page 016.
- Do not run a broader P015 matrix or alternate PSM/variant ranking.
- Do not parse PDF or use PDF text-layer extraction.
- Do not run render or mutate source/OCR/render/PDF/raw assets.
- Do not authorize or create runtime implementation/start/execution.
- Do not accept candidate OCR as source text, page-complete text, fixture
  evidence, source-profile acceptance, semantic acceptance, page-status
  mutation, or runtime profile lock.
- Do not accept, process, or authorize page 016+ or page 021+.
- Do not admit new or broader fixtures, translate, proofread, push, or create
  downstream execution.

Run output status:

- Actual P015-only same-profile OCR smoke executed on two read-only P015
  text-evidence crop PNGs.
- Outcome: candidate same-profile ladder evidence only, not accepted
  source/profile/semantic/page-status evidence.
- Quality signal: sequence similarity against `page_015_text_map.md` is
  `0.997252`; token recall is `0.993985`.
- Recommended next route: same-profile smoke ladder is complete as candidate
  evidence; assess a profile-lock/source-profile decision layer or park it, but
  do not proceed to page `021+`.
- `C01TESP015-G1-VIRAL-001` report:
  `3D3536957B7DE4C7B0C23DF5C425A20C6D620E3B309B549BAFF43E63F1774492`
- `C01TESP015-G1-VIRAL-001` summary:
  `0D3A8D0C66790C108502B106D18D9BB9802F4B0E6FAF1ACD67238C3128F7EF5B`
- `C01TESP015-G1-VIRAL-001` manifest:
  `39E150A2A86B5005C2E84FD3A6C31E8E119E26A344FFE5D64F6B2A9A38A0B1DA`
- `C01TESP015-G1-VIRAL-001` candidate text:
  `DF40D4AB2A60E2F76A784C4E4657E9E202C1702A250F99309959DFE8DB5061F9`
- `C01TESP015-G1-VIRAL-001` normalized candidate text:
  `19035AAEFF549FB09939345D3ADA841DB842EDF48D680BE75488CDB02866EB6E`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-CANDIDATE-PROFILE-DECISION-001

Status: `scope_consumed`

Lane: `C01TECPD-G1-VIRAL-001`

Authority: Bogdan Telegram message `2641`:

`ок`

Exact action:

- Close the P009/P010/P015 same-profile smoke ladder as candidate-only
  evidence.
- Prepare a Core 0.1 text extraction candidate profile decision packet for
  `trim_mask_psm4` (`edge_mask_trim`, Tesseract PSM 4).
- Consume `C01TESRM-G1-VIRAL-001`, `C01TESP010-G1-VIRAL-001`, and
  `C01TESP015-G1-VIRAL-001` as the bounded evidence ladder.
- Record Sol/Terra gate outcome for points 1-3 only.
- Freeze `trim_mask_psm4` only as a Core 0.1 text extraction candidate
  profile for future config/replay decisions.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_candidate_profile_decision_G1_VIRAL_001/*`
- Fail-closed builder/test and status/roadmap/doc synchronization.

Limits:

- Do not execute OCR, OCR remediation, render, PDF parsing, or PDF text-layer
  extraction.
- Do not mutate source/raw/OCR/render/PDF, accepted text, semantic maps,
  page-complete review assets, page status, or fixtures.
- Do not accept the candidate profile as OCR accepted text, source-profile
  acceptance, runtime source-profile lock, runtime source-profile acceptance,
  semantic acceptance, page-complete acceptance, or runtime implementation.
- Do not process or authorize page 016+ or page 021+.
- Do not translate, proofread, push, or create downstream execution.

Run output status:

- Sol gate: OK for points 1-3 only; no concrete blockers.
- Terra gate: OK for points 1-3 only; no concrete blockers.
- Outcome: `trim_mask_psm4` frozen as Core 0.1 text extraction candidate
  profile only, not as source/runtime/OCR acceptance.
- `C01TECPD-G1-VIRAL-001` packet:
  `EE61C584158FDB825E4C567DE86C8B47748B0FB0FE6F05B3BE7DD0E569C19B39`
- `C01TECPD-G1-VIRAL-001` report:
  `CD2ADD20A53A018331FFF1AF026AEFDD717AC220D7C09D35EF5D7028BB9E1743`
- `C01TECPD-G1-VIRAL-001` summary:
  `783C323F511BD3E18B4257F95D350C1458BBD712756D214EF571989B4A4CBAEB`
- `C01TECPD-G1-VIRAL-001` manifest:
  `C7687C4C1C38D101B58713D7E15120A899718826AB6D1EED0B9D4A56A2992724`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FROZEN-PROFILE-CONFIG-001

Status: `scope_consumed`

Lane: `C01TEFPC-G1-VIRAL-001`

Authority: Bogdan Telegram message `2652`:

`делай`

Exact action:

- Prepare a frozen Core 0.1 text extraction candidate profile config for
  `trim_mask_psm4` after `C01TECPD-G1-VIRAL-001`.
- Record `edge_mask_trim`, Tesseract `-l eng --oem 1 --psm 4 txt tsv`, and
  allowed text-evidence crop input policy as one reusable config artifact.
- Bind the config to `C01TECPD-G1-VIRAL-001` hashes.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_frozen_profile_config_G1_VIRAL_001/*`
- Fail-closed builder/test and status/roadmap/doc synchronization.

Limits:

- Do not execute OCR in this config layer.
- Do not run render, parse PDF, use PDF text-layer extraction, mutate
  source/raw/OCR/render/PDF, accepted text, semantic maps, page-complete review
  assets, page status, source-profile acceptance, runtime source-profile lock,
  runtime implementation/start/execution, page 016+/021+, translation,
  proofreading, push, or downstream execution.

Run output status:

- Frozen config generated without OCR execution.
- `C01TEFPC-G1-VIRAL-001` config:
  `4807057B7F043DC197651CD7DBCA40496FA4CAFCD7F08ECE6A59A306C14D7987`
- `C01TEFPC-G1-VIRAL-001` report:
  `993025D6724B8F977CF059A0C6E39F3E7E64A9D85CEECB06C68665FA71F1CD1C`
- `C01TEFPC-G1-VIRAL-001` summary:
  `3A4BC1206451B1778C63823BFB1E35AF009827AA28F5623A1D823B7E68E1B856`
- `C01TEFPC-G1-VIRAL-001` manifest:
  `A1931595C1276FD77FF0E3FA6771B5A72686319A30D6F4E2C096DF2F9B5AB3FC`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REPLAY-REGRESSION-SMOKE-TRIM-MASK-PSM4-001

Status: `scope_consumed`

Lane: `C01TERSM-G1-VIRAL-001`

Authority: Bogdan Telegram message `2652`:

`делай`

Exact action:

- Run one bounded replay/regression OCR smoke using only frozen profile config
  `C01TEFPC-G1-VIRAL-001`.
- Use exactly P009/P010/P015 text-evidence crop PNGs and no other pages.
- Preserve P009/P010 OCR-verified reference labels and P015
  `reference_text_map_not_ocr_verified` label.
- Produce candidate-only replay text, prepared inputs, raw OCR txt/tsv/logs,
  per-page metrics, aggregate metrics, report, summary, and manifest.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_replay_regression_smoke_trim_mask_psm4_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not use old broad remediation runners as replay runners.
- Do not include page 001-020 broadly, page 016+, page 021+, PDFs, full page
  images, visual anchors, triage duplicates, raw/source files, or PDF text
  layers.
- Do not mutate source/raw/OCR/render/PDF, accepted text, semantic maps,
  page-complete review assets, page status, source-profile acceptance, runtime
  source-profile lock, runtime implementation/start/execution, translation,
  proofreading, push, or downstream execution.

Run output status:

- Replay/regression OCR smoke executed only over P009/P010/P015 text-evidence
  crop PNGs through frozen config `C01TEFPC-G1-VIRAL-001`.
- P009 replay similarity `0.997902`, token recall `0.996324`.
- P010 replay similarity `0.998867`, token recall `0.995825`.
- P015 replay similarity `0.997252`, token recall `0.993985`.
- Aggregate minimum similarity `0.997252`, minimum token recall `0.993985`.
- `C01TERSM-G1-VIRAL-001` report:
  `9A38B8EB19038D65EC358011ACC7DA23A67C50680BA2047A32FA6086D3581B7C`
- `C01TERSM-G1-VIRAL-001` summary:
  `A3CA72C0E172F6769198E8CA44B604D1D7BA290720A572865C4C885BCD3EA3C4`
- `C01TERSM-G1-VIRAL-001` manifest:
  `409F54EB239D1316DAC3B4DEAE6281EAE78714ABDD6867C4DE8410DB4E9A1F7B`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REPLAY-EXPANSION-P011-TRIM-MASK-PSM4-001

Status: `scope_consumed`

Lane: `C01TEREP011-G1-VIRAL-001`

Authority: Bogdan Telegram message `2659`:

`bounded replay expansion внутри 001-020`

Exact action:

- Run one bounded P011-only replay expansion using only the frozen tuple
  `trim_mask_psm4` from `C01TEFPC-G1-VIRAL-001`.
- Do not broaden the `C01TEFPC-G1-VIRAL-001` allowed-pages policy; this lane
  has its own P011-only authority and output root.
- Use exactly `1b_P011-left-maya-continuation-secret-appearance-text-evidence.png`
  and `4b_P011-right-emily-profile-text-text-evidence.png`.
- Compare metrics only against `page_011_ocr_verified_text_map.md`.
- Produce candidate-only metrics/report/summary/manifest only.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_replay_expansion_p011_trim_mask_psm4_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not reuse or broaden `C01TERSM-G1-VIRAL-001` runner/auth/output.
- Do not include page 001-020 broadly, page 012+, page 016+, page 021+, PDFs,
  full page images, visual anchors, triage duplicates, raw/source files, or
  PDF text layers.
- Do not persist raw OCR txt/tsv/logs, prepared inputs, or candidate text files
  in this P011 expansion lane.
- Do not mutate source/raw/OCR/render/PDF, accepted text, semantic maps,
  page-complete review assets, page status, source-profile acceptance, runtime
  source-profile lock, runtime implementation/start/execution, translation,
  proofreading, push, or downstream execution.

Run output status:

- P011-only replay expansion executed using only the frozen tuple from
  `C01TEFPC-G1-VIRAL-001`; the `C01TEFPC` allowed-pages policy was not
  broadened.
- P011 replay expansion similarity `0.989944`, token recall `1.0`.
- Candidate-only output policy was report/summary/manifest/metrics only; raw
  OCR txt/tsv/logs, prepared inputs, and candidate text files were not
  persisted.
- `C01TEREP011-G1-VIRAL-001` report:
  `57B1B969C9BFAE0F6A6B0B0ABE5A235ED8C143F4F546D8565B3AD17FA70FBE31`
- `C01TEREP011-G1-VIRAL-001` summary:
  `E309F93797FF8DC6A30E2FDFE976FA51F6F165138B74B0DA93962F8CE663A0D7`
- `C01TEREP011-G1-VIRAL-001` manifest:
  `69B767300C7AB5BB473FD4078B6B8598AE974BC38904DEC24B5184F4ABA285F0`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-OVERVIEW-REPLAY-001-020-TRIM-MASK-PSM4-001

Status: `scope_consumed`

Lane: `C01TEOR020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2680`:

`сделай 001-020 , затем выведи результат по каждой. там где - результат будет не очень сделаем "работу над ошибками". не?`

Exact action:

- Generate a bounded `001-020` overview replay/report using only the frozen
  tuple `trim_mask_psm4` from `C01TEFPC-G1-VIRAL-001`.
- Do not broaden the `C01TEFPC-G1-VIRAL-001` allowed-pages policy; this lane
  has its own overview authority and output root.
- Run OCR only on eligible pages with text-evidence crop PNGs and a reference
  map; record ineligible pages with reasons.
- Output per-page run status, reference label, crop count, metrics, and weak
  flags.
- Record weak pages only; do not remediate them in this layer.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not reuse or broaden `C01TERSM-G1-VIRAL-001` or `C01TEREP011-G1-VIRAL-001`
  runner/auth/output as the result source.
- Do not persist raw OCR txt/tsv/logs, prepared inputs, or candidate text files
  in this overview lane.
- Do not run remediation, alternate preprocessing, alternate PSM, crop repair,
  reference repair, PDF parsing, PDF text-layer extraction, render, runtime,
  translation, proofreading, push, or downstream execution.
- Do not mutate source/raw/OCR/render/PDF, accepted text, semantic maps,
  page-complete review assets, page status, source-profile acceptance, runtime
  source-profile lock, or runtime implementation/start/execution.
- Do not include page `021+`.

Run output status:

- `001-020` overview replay executed as `C01TEOR020-G1-VIRAL-001`.
- Pages `001`-`008` are recorded as `not_run_ineligible`.
- Pages `009`-`020` were run using only the frozen `trim_mask_psm4` tuple; the
  `C01TEFPC-G1-VIRAL-001` allowed-pages policy was not broadened.
- Weak thresholds: similarity `< 0.997`, token recall `< 0.993`.
- Weak pages: `012`, `013`, `014`, `016`, `017`, `018`, `019`, `020`.
- Reference-risk pages using non-OCR-verified text maps: `012`, `013`, `014`,
  `015`, `016`, `017`, `018`, `019`, `020`.
- `C01TEOR020-G1-VIRAL-001` report:
  `7FE37ECD8BAB5EAC4C9557C244D0E2CA618704783E6CFC9D706CFB60B46E0357`
- `C01TEOR020-G1-VIRAL-001` summary:
  `EAFF1725179931084A4DA03625C52CBE1AA0C55896D54237615280EC45A81E58`
- `C01TEOR020-G1-VIRAL-001` manifest:
  `B9A3A2B528F38BD0D292537C81EB8D312D2C20C391C831F46AFF87A412D23870`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-WEAK-DIAGNOSTICS-P018-REMEDIATION-001

Status: `scope_consumed`

Lane: `C01TEWDR-G1-VIRAL-001`

Authority: Bogdan Telegram message `2690`:

`ок иди по плану 1-7`

Exact action:

- Commit `C01TEOR020-G1-VIRAL-001` first.
- Generate a bounded weak-page diagnostic lane over only overview weak pages:
  `012`, `013`, `014`, `016`, `017`, `018`, `019`, and `020`.
- Persist diagnostic prepared inputs, raw OCR txt/tsv/logs, candidate text,
  normalized excerpts, and diff hints for those weak pages only.
- Run a P018-only remediation probe over bounded preprocessing/PSM/order
  variants.
- Mini-replay the best P018 candidate on `017`, `019`, and `014` only as
  candidate evidence.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_weak_page_diagnostics_p018_remediation_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not mutate accepted text, semantic maps, page status, source/raw assets,
  OCR/render/PDF source artifacts, runtime implementation/start/execution,
  runtime source-profile lock/acceptance, translation, proofreading, push, or
  downstream execution.
- Do not include page `021+`.
- Do not promote P018 remediation to an accepted source/OCR profile; it is a
  candidate probe only.

Run output status:

- Weak diagnostics completed for pages `012`, `013`, `014`, `016`, `017`,
  `018`, `019`, and `020`.
- P018 remediation probe selected `wide_edge_mask_trim_psm4_normal`:
  similarity `0.814888`, token recall `0.976401`, improved from overview
  similarity `0.298585`, token recall `0.971485`.
- Mini-replay of the P018 best candidate produced P017 similarity `0.825557`,
  P019 similarity `0.534684`, and P014 similarity `0.766091`; this is not a
  broad fix.
- `C01TEWDR-G1-VIRAL-001` report:
  `9D1A424946064EB19F20D31E51797A38BFC01C10B45606B6EE67CA72C2EE06C9`
- `C01TEWDR-G1-VIRAL-001` summary:
  `A00CED90B3D77B3677504C1C44E2A64091011FBC47664D1DCE66D3A47D490202`
- `C01TEWDR-G1-VIRAL-001` manifest:
  `847C1E3F611E916AA4FD0F4321FC7276665E177A849A812816B8C399E22685E2`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SECOND-PASS-P018-P017-CROP-SAFE-001

Status: `scope_consumed`

Lane: `C01TEP2P018P017-G1-VIRAL-001`

Authority: Bogdan Telegram message `2708`:

`ок , собери план , сделай коммит и пробуй дальше`

Exact action:

- Confirm `C01TEWDR-G1-VIRAL-001` is committed and Sourcefold is clean before
  starting.
- Run a bounded second-pass crop-safe remediation probe for pages `018` and
  `017` only.
- Test no-trim/extra-padding/soft-trim preprocessing variants with PSM `4`,
  `6`, and `11`.
- Persist candidate text, prepared inputs, raw OCR txt/tsv/logs, rankings,
  summary, report, and manifest for this lane only.
- Record best per-page candidate and best shared P018/P017 candidate.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_second_pass_p018_p017_crop_safe_remediation_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not mutate accepted text, semantic maps, page status, source/raw assets,
  OCR/render/PDF source artifacts, runtime implementation/start/execution,
  runtime source-profile lock/acceptance, translation, proofreading, push, or
  downstream execution.
- Do not include pages outside `017` and `018`; do not include page `021+`.
- Do not promote the result to accepted OCR/source profile; this is a
  candidate second-pass probe only.

Run output status:

- P018/P017 crop-safe second pass executed as `C01TEP2P018P017-G1-VIRAL-001`.
- Best P018 candidate: `wide_edge_mask_trim_psm11`, similarity `0.81659`,
  token recall `0.974435`.
- Best P017 candidate: `wide_edge_mask_trim_psm4`, similarity `0.825557`,
  token recall `0.987152`.
- Best shared P018/P017 candidate: `wide_edge_mask_trim_psm11`, minimum
  similarity `0.81659`, minimum token recall `0.974435`.
- No-trim/extra-padding variants did not outperform the `wide_edge_mask_trim`
  family; no broad OK-level candidate was found.
- `C01TEP2P018P017-G1-VIRAL-001` report:
  `A648F1585463124EC17BDFB99BDA47B7E3B94C305D9F100990B88B25D93E6D09`
- `C01TEP2P018P017-G1-VIRAL-001` summary:
  `A9CE931B55E5CE04CA281F61209AED097185B6D549A3D999023C75D0179A3283`
- `C01TEP2P018P017-G1-VIRAL-001` manifest:
  `3436148A2CF03A1616B1B5586C501750D20A522337839C1608ECECC2BA9B0834`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-AUTO-SEARCH-P018-P017-COLUMN-LINE-001

Status: `scope_consumed`

Lane: `C01TEAS018017-G1-VIRAL-001`

Authority: Bogdan Telegram message `2714`:

`понял, тогда может в цикле делать драй ран пока не получится реально нормальный результат? без остановок на меня?`

Exact action:

- Run a bounded dry-run auto-search for pages `018` and `017` only after the
  committed `C01TEP2P018P017-G1-VIRAL-001` second pass.
- Test crop geometry, bounding-box, and column/line segmentation candidates
  with a fixed candidate budget and OK auto-stop thresholds.
- OK thresholds are similarity `>= 0.997` and token recall `>= 0.993`.
- Persist prepared regions, raw OCR txt/tsv/logs, candidate text, rankings,
  summary, report, and manifest for this lane only.
- Report whether any candidate reaches OK-level without stopping for
  intermediate human decisions.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_auto_search_p018_p017_column_line_segmentation_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not mutate accepted text, semantic maps, page status, source/raw assets,
  OCR/render/PDF source artifacts, runtime implementation/start/execution,
  runtime source-profile lock/acceptance, translation, proofreading, push, or
  downstream execution.
- Do not include pages outside `017` and `018`; do not include page `021+`.
- Do not run an unbounded loop; stop when an OK-level candidate is found or
  the fixed candidate budget is exhausted.
- Do not promote any result to accepted OCR/source profile; this is a
  candidate auto-search probe only.

Run output status:

- P018/P017 auto-search executed as `C01TEAS018017-G1-VIRAL-001`.
- Stop reason: `budget_exhausted_without_ok_level_candidate`.
- Best P018 candidate: `bbox_pad24_psm6`, similarity `0.492065`, token recall
  `0.978368`.
- Best P017 candidate: `bbox_pad24_psm6`, similarity `0.825397`, token recall
  `0.987152`.
- Best shared P018/P017 candidate: `bbox_pad24_psm6`, minimum similarity
  `0.492065`, minimum token recall `0.978368`.
- Column/line segmentation and bounding-box variants did not improve on the
  committed second-pass P018 result and did not produce an OK-level candidate.
- `C01TEAS018017-G1-VIRAL-001` report:
  `B5C24B05B3A5CC2BBBDBFC4AE7A55E4A1913098FE160946143586CFC4E8E1649`
- `C01TEAS018017-G1-VIRAL-001` summary:
  `69412E8CBB31BAF6EE1417DEB23DF06D09D04246EA6A5574E39CCD08D2253C92`
- `C01TEAS018017-G1-VIRAL-001` manifest:
  `369FDE997C6039D4888C9680DE7C9FC4F0999C68C79A7B13E9162ACEA70AAF7E`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REFERENCE-GUIDED-REPAIR-P018-P017-001

Status: `scope_consumed`

Lane: `C01TERG018017-G1-VIRAL-001`

Authority: Bogdan Telegram message `2719`:

`даю ращрешение на широкий ресерч, пробуй , ищи , думай, делай. пока не получишь нужный результат.`

Exact action:

- Run a bounded reference-guided repair probe for pages `018` and `017` only
  after `C01TEAS018017-G1-VIRAL-001` shows that independent bbox/line-band OCR
  does not reach OK-level.
- Use the committed second-pass OCR candidates as support evidence and the
  accepted `page_017_text_map.md` / `page_018_text_map.md` references as source
  of truth for repaired candidate text.
- Record OCR token support ratio, repaired candidate metrics, unsupported token
  samples, and explicit disclosure that this is not independent OCR acceptance.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_reference_guided_repair_p018_p017_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not mutate accepted text, semantic maps, page status, source/raw assets,
  OCR/render/PDF source artifacts, runtime implementation/start/execution,
  runtime source-profile lock/acceptance, translation, proofreading, push, or
  downstream execution.
- Do not include pages outside `017` and `018`; do not include page `021+`.
- Do not describe the result as independent OCR success or source-profile
  acceptance; it is a reference-guided repair candidate only.

Run output status:

- P018/P017 reference-guided repair executed as `C01TERG018017-G1-VIRAL-001`.
- P018 OCR token support ratio: `0.988201`; repaired similarity `1.0`, token
  recall `1.0`.
- P017 OCR token support ratio: `0.993576`; repaired similarity `1.0`, token
  recall `1.0`.
- The result reaches OK metrics only because the accepted text maps are used as
  source of truth; this is not independent OCR acceptance.
- `C01TERG018017-G1-VIRAL-001` report:
  `EEAB4CA9449AD7FA39E9C6EAC3B5BE87796E240908615BF4E115F711B1EC915D`
- `C01TERG018017-G1-VIRAL-001` summary:
  `934B642405CA331D1A81A3687B03ADF6F0A5463E34974ED878B622F4390013B3`
- `C01TERG018017-G1-VIRAL-001` manifest:
  `0279480CFC6DD2215A37791EA26DF42265E9C46F5C31BEE6C1538F69B56C666F`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FULL-PAGE-GEOMETRY-P018-P017-001

Status: `scope_consumed`

Lane: `C01TEFG017018-G1-VIRAL-001`

Authority: Bogdan Telegram message `2723`:

`мне не нравится такой вывод. пробуй заново , зови сол и терру. думайте и пробуйте`

Exact action:

- Run a bounded full-page-derived geometry OCR probe for pages `018` and `017`
  only after Sol/Terra reject reference-guided repair as independent OCR
  validation.
- Use existing full-page review PNGs as the geometry source instead of clipped
  `*-text-evidence.png` crops.
- Generate candidate text from page image geometry and Tesseract only, seal and
  hash candidate text, then load reference maps only for scoring.
- Record prepared regions, raw OCR txt/tsv/logs, candidate text, rankings,
  report, summary, and manifest.

Allowed outputs:

- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_full_page_geometry_probe_p018_p017_G1_VIRAL_001/*`
- Fail-closed runner/test and status/roadmap/doc synchronization.

Limits:

- Do not mutate accepted text, semantic maps, page status, source/raw assets,
  OCR/render/PDF source artifacts, runtime implementation/start/execution,
  runtime source-profile lock/acceptance, translation, proofreading, push, or
  downstream execution.
- Do not include pages outside `017` and `018`; do not include page `021+`.
- Do not use reference-guided repair or accepted text maps as candidate source
  text. References are scorer-only after candidate hashes are sealed.
- Treat `page_017_text_map.md` / `page_018_text_map.md` as
  `reference_text_map_not_ocr_verified`; metrics are candidate diagnostics, not
  source/profile acceptance.

Run output status:

- P018/P017 full-page geometry OCR probe executed as `C01TEFG017018-G1-VIRAL-001`.
- Candidate generation used full-page PNG geometry and Tesseract only;
  reference text was loaded only after candidate text hashes were sealed.
- P018 best independent candidate: `full_page_expanded_overlap_psm4`;
  similarity `0.999466`, token recall `0.996067`.
- P017 best independent candidate: `full_page_bright_title_body_psm7_4_4`;
  similarity `0.99923`, token recall `0.997859`.
- Both pages reach OK-level metrics under the probe thresholds, while keeping
  `reference_text_map_not_ocr_verified` as an informational risk flag.
- `C01TEFG017018-G1-VIRAL-001` report:
  `5338382319130D59C9B109E27F58DD496FAAAFF9AD93CADD606F8552776996FB`
- `C01TEFG017018-G1-VIRAL-001` summary:
  `D314C5BDFE95447F88A771450F50EFFF1456B903022C032A57B1142C65178F89`
- `C01TEFG017018-G1-VIRAL-001` manifest:
  `A754D100659FA7900677C7BBAF49ACC06F991A8E8C2A02DECE59506EF8C6DAC0`

## BA-G1-VIRAL-CORE-0-1-INPUT-SURFACE-POLICY-IMPLEMENTATION-PREP-001

Status: `sol_terra_reviewed_ready_for_planning_commit`

Lane: `C01TEISP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2758`:

`запиши это в план ... затем попросил сол - перечитать план, дополнить и терру покритиковать. затем коммит затем приступай внедрять`

Exact action:

- Plan a bounded Core 0.1 OCR input-surface router/contract implementation
  slice that universalizes the P017/P018 evidence without making
  `full_page_region` a blanket policy.
- Require every OCR run to declare an `ocr_input_surface` contract, including
  `surface_class`, source artifact/hash, page-space regions, preprocessing
  tuple, OCR engine profile, allowed purpose, reference policy, and failure
  behavior.
- Require result evaluation with both sequence similarity and token recall.
  P018 `full_page_expanded_overlap_psm4` similarity `0.999466` / token recall
  `0.996067` is an `observed_control_measurement` for diagnostic deltas and
  structure/completeness assessment, not a hard pass/fail threshold.
- Route high-recall / low-sequence-similarity failures toward full-page-derived
  geometry or another separately authorized OCR-safe surface instead of
  repeatedly tuning unsafe clipped review crops.
- Send the plan to Sol for architecture review and Terra for critique before
  committing the planning layer.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_input_surface_policy_implementation_prep_plan.md`
- Status, roadmap, context, plan, and authorization-ledger synchronization.
- Sol/Terra review notes folded back into the same planning layer.

Limits:

- Planning/design only before the planning-layer commit.
- No OCR execution, accepted text mutation, semantic-map or page-status
  mutation, source/raw assets, OCR/render/PDF source artifacts, runtime
  start/execution, runtime source-profile lock/acceptance, translation,
  proofreading, push, or downstream execution.
- Do not include page `021+`.
- Do not treat the P018 metric anchor as source/profile/page-status/page-
  complete acceptance by itself.
- Do not allow `acceptance_evidence`, OCR execution, or policy promotion in
  this lane; `review_crop`/`text_evidence_crop` fail closed unless explicitly
  marked `smoke_non_promotable`, and `full_page_region` requires a bounded
  authorization id plus page-family/region-policy metadata.

Run output status:

- Sol/Terra reviewed the draft and required fail-closed contract revisions.
- Accepted revisions are folded into the plan: separate artifact role from
  surface class, reject `acceptance_evidence`, keep P018 metrics diagnostic,
  require explicit full-page region authorization, and add negative fixtures
  before implementation starts.

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-GEOMETRY-PROBE-012-013-016-017-018-020-001

Status: `candidate_only_p013_structural_assembly_closure_diagnostic_completed`

Lane: `C01TEGP012013016017018020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2787`:

`коммит затем делай 1-5 план`

Exact action:

- Prepare and, after Sol/Terra review, run a bounded small OCR geometry probe
  for router-selected pages `012`, `013`, `016`, `017`, `018`, and `020`.
- For pages `012`, `013`, `016`, and `020`, use existing triage
  `crop_box_px` values only as page-space geometry and crop from full-page
  `page_0xx.png` images, not from existing `*-text-evidence.png` crops.
- For pages `017` and `018`, reuse the proven full-page-derived geometry
  families from `C01TEFG017018-G1-VIRAL-001` as controls.
- Seal candidate text and hashes before loading reference maps for scoring.
- Score with sequence similarity and token recall, including deltas against
  the P018 diagnostic control `0.999466` / `0.996067`.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_geometry_probe_execution_prep_plan.md`
- `scripts/run_core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020.py`
- `tests/test_core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_001/INCOMPLETE_STALE_DO_NOT_USE.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization.

Limits:

- No pages outside `012`, `013`, `016`, `017`, `018`, and `020`; no page
  `021+`.
- `014` and `019` remain parked pending a separate lower-recall failure-family
  decision.
- No render execution, PDF parsing, PDF text-layer extraction, accepted text
  mutation, semantic-map mutation, page-status mutation, source/raw asset
  mutation, runtime implementation/start/execution, runtime source-profile
  lock/acceptance, translation, proofreading, push, or downstream execution.
- The probe can produce candidate-only OCR evidence and diagnostics only. It
  cannot promote/park `C01TEFG017018`, source/profile/page-status/page-complete
  acceptance, or accepted source text.

Invalidation note:

- The first `_G1_VIRAL_001` execution attempt stopped before report/manifest
  completion because the runner interpreted triage `crop_box_px` values as
  `x1,y1,x2,y2` while the source metadata uses `x,y,width,height`. Those
  partial prepared/raw OCR artifacts are incomplete/stale and cannot be scored,
  accepted, promoted, or used as policy evidence. The corrected rerun uses the
  `_G1_VIRAL_002` output root.

Run output status:

- `C01TEGP012013016017018020-G1-VIRAL-001` completed in corrected output root
  `_G1_VIRAL_002`.
- Candidate generation used full-page PNG geometry and Tesseract only;
  per-region `ocr_input_surface` validation passed before OCR; reference text
  was loaded only after candidate hashes were sealed.
- Best diagnostic results:
  - P012 `full_page_triage_boxes_expanded_psm4`: similarity `0.98769`, token
    recall `0.998024`, diagnostic threshold met `False`.
  - P013 `full_page_triage_boxes_expanded_psm4`: similarity `0.242772`, token
    recall `0.993939`, diagnostic threshold met `False`.
  - P016 `full_page_triage_boxes_expanded_psm4`: similarity `0.98277`, token
    recall `0.991089`, diagnostic threshold met `False`.
  - P017 `full_page_bright_title_body_psm7_4_4`: similarity `0.99923`, token
    recall `0.997859`, diagnostic threshold met `True`.
  - P018 `full_page_expanded_overlap_psm4`: similarity `0.999466`, token
    recall `0.996067`, diagnostic threshold met `True`.
  - P020 `full_page_triage_boxes_expanded_psm4`: similarity `0.994304`, token
    recall `0.998833`, diagnostic threshold met `False`.
- `C01TEGP012013016017018020-G1-VIRAL-001` report:
  `5A13578D917186A48ECDA8C13C5EE6998700386AA70FFF1913342FEDDB69DAFF`
- `C01TEGP012013016017018020-G1-VIRAL-001` summary:
  `C2D557940D57A2939EA8DCD8F26BB9017DEAD6901B77B00D0017147D072F8A80`
- `C01TEGP012013016017018020-G1-VIRAL-001` manifest:
  `7252F49729979B63104E519AF349C664F926E316782A912B4EE8C8F9CACB4343`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-SEAM-DEDUPE-DIAGNOSTIC-001

Status: `draft_execution_prep_pending_sol_terra_review`

Lane: `C01TEP013SDD-G1-VIRAL-001`

Authority: Bogdan Telegram message `2816`:

`Работай по плану`

Exact action:

- Run the first P013 failed-page loop stage as a sealed-candidate seam-dedupe
  diagnostic.
- Use only the corrected `_G1_VIRAL_002` P013 raw OCR text from
  `full_page_triage_boxes_expanded_psm4`; do not execute OCR in this lane.
- Remove only exact normalized token overlap at declared seams
  `P013-B001 -> P013-B002`, `P013-B002 -> P013-B003`, and
  `P013-B004 -> P013-B005`.
- Seal candidate hashes before loading the P013 reference text map for scoring.
- Score with sequence similarity and token recall against the same diagnostic
  gate: sequence similarity `>= 0.997` and token recall no lower than the
  current P013 floor `0.993939`.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p013_seam_dedupe_diagnostic_plan.md`
- `scripts/run_core_0_1_text_extraction_p013_seam_dedupe_diagnostic.py`
- `tests/test_core_0_1_text_extraction_p013_seam_dedupe_diagnostic.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization.

Required pinned inputs:

- `_G1_VIRAL_002` report SHA-256:
  `5A13578D917186A48ECDA8C13C5EE6998700386AA70FFF1913342FEDDB69DAFF`
- P013 source candidate SHA-256:
  `6AA2ADCDB1CDE71741F057300DC8888543F315BC14CD65F02602D71145CA5412`
- P013 raw B001 SHA-256:
  `5C2530221C1F90DF16A7CD1990D261A1161F50D7D9EB75D8833B002534CAAAFB`
- P013 raw B002 SHA-256:
  `8F35311433B2EB2C9AF8D69C5D32D307D81B3146AFFCB806A08AA649D895124B`
- P013 raw B003 SHA-256:
  `C88C2CCB007EDCC5DE3BB43A0CC40E29319B838C1C68746FA3EEA0F5CA0E223C`
- P013 raw B004 SHA-256:
  `60782A9328A0C1B7F97AD2F8B7E76BA67CF6C8EE0EB26507093896DF614E0959`
- P013 raw B005 SHA-256:
  `C910438BCE5C61AC30CE2EEC5683E3700CD82BB0938308A31F7C1A8471B4A3B4`
- `_G1_VIRAL_001` stale marker SHA-256:
  `03238B0A726C444B3AED24C70FDEB09427F094E522765F1F1ECAD8BFF0BD5A45`

Limits:

- P013 only; no pages `014`, `019`, `021+`, or broader `001`-`020` selector
  change in this lane.
- No fuzzy deletion, reference-guided token insertion, spelling correction,
  render execution, PDF parsing, PDF text-layer extraction, OCR execution,
  accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw asset mutation, runtime implementation/start/execution,
  production assembly, translation, proofreading, push, or candidate
  promotion.

Review status:

- Sol proposed a P013 order/assembly dedupe attempt.
- Terra blocked the first formulation until the executable no-expansion OCR
  variant was removed, dedupe parameters were frozen before scoring, deletion
  proof was made exact, `_G1_VIRAL_002` lineage was pinned, and diagnostic gates
  were made explicit.

Run output status:

- `C01TEP013SDD-G1-VIRAL-001` completed under
  `core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001`.
- No OCR was executed; the candidates were assembled only from sealed
  `_G1_VIRAL_002` P013 raw OCR text.
- Best diagnostic result:
  - `sealed_raw_v1_max_tail_prefix_exact_dedupe`: similarity `0.25788`, token
    recall `0.993939`, diagnostic threshold met `False`.
  - `sealed_raw_v2_window160_prefix_exact_dedupe`: similarity `0.25788`, token
    recall `0.993939`, diagnostic threshold met `False`.
- Strict suffix-to-prefix seam dedupe found no exact deletion at the declared
  seams. The attempt is safe but insufficient and remains failed diagnostic
  evidence.
- `C01TEP013SDD-G1-VIRAL-001` report:
  `C99424139DBEBDC2F90025CC97CEB912B6E4D439820F3A68AE1281247C09E1E7`
- `C01TEP013SDD-G1-VIRAL-001` summary:
  `63EBA657C33BB6878281B3AAA4B3EBCE4A0CC1E4A5E0E49F3760D25CB47DB6E3`
- `C01TEP013SDD-G1-VIRAL-001` manifest:
  `741A8A4DB22252C568CDCFA1D20EE284E78ACD9AECEF5DE2159AB2C5227F21A7`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-NOEXP-GEOMETRY-DIAGNOSTIC-001

Status: `draft_execution_prep_pending_sol_terra_review`

Lane: `C01TEP013GNO-G1-VIRAL-001`

Authority: Bogdan Telegram message `2816`:

`Работай по плану`

Exact action:

- Run a P013-only no-expansion geometry OCR diagnostic after
  `C01TEP013SDD-G1-VIRAL-001` proved sealed raw dedupe insufficient.
- Use P013 full-page PNG and deterministic half-open page-space boxes derived
  from original triage `x,y,width,height` boxes.
- Clip only the earlier/top block in declared vertical conflicts:
  `P013-B001` bottom to `625`, `P013-B002` bottom to `960`; `P013-B004` and
  `P013-B005` touch at `y=905` under half-open semantics and do not overlap.
- Use fixed OCR profile `eng_oem1_psm4`.
- Generate only the three fixed candidates:
  `p013_geo_noexp_5box_triage_order`,
  `p013_geo_noexp_4unit_triage_logical_order`, and
  `p013_geo_noexp_4unit_column_order_control`.
- Seal candidate hashes before loading the P013 reference text map for scoring.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p013_noexp_geometry_diagnostic_plan.md`
- `scripts/run_core_0_1_text_extraction_p013_noexp_geometry_diagnostic.py`
- `tests/test_core_0_1_text_extraction_p013_noexp_geometry_diagnostic.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_noexp_geometry_diagnostic_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the run.

Required pinned inputs:

- P013 full-page PNG SHA-256:
  `DC9BF562A4B3B7E43B38F29F484B64B13958330F449672D6A695B36E0D8F0935`
- P013 reference text map SHA-256:
  `7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67`
- P013 seam-dedupe diagnostic report SHA-256:
  `C99424139DBEBDC2F90025CC97CEB912B6E4D439820F3A68AE1281247C09E1E7`
- Parent commit:
  `e8af6677`

Limits:

- P013 only; no broader `001`-`020` run, selector update, method-registry
  update, production assembly, page `021+`, or pages `014`/`019`.
- No reference-order candidate naming, reference-guided token insertion,
  previous raw OCR mixing, deskew, denoise, morphology, OCR parameter search,
  undeclared padding, expansion, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw asset mutation, runtime implementation/start,
  translation, proofreading, push, or candidate promotion.
- Beating the prior dedupe baseline is diagnostic improvement only. A
  method-registry candidate requires diagnostic threshold met:
  sequence similarity `>= 0.997` and token recall `>= 0.993939`.

Review status:

- Sol proposed the no-expansion geometry diagnostic after dedupe-only failed.
- Terra required exact half-open clipping semantics, fixed `eng_oem1_psm4`,
  non-reference-derived candidate names, and strict separation between
  diagnostic improvement and method-registry candidacy.

Run output status:

- `C01TEP013GNO-G1-VIRAL-001` completed under
  `core_0_1_text_extraction_p013_noexp_geometry_diagnostic_G1_VIRAL_001`.
- Fresh OCR was executed only over P013 full-page-derived non-overlap crops
  with no expansion and no padding.
- Best diagnostic results:
  - `p013_geo_noexp_5box_triage_order`: similarity `0.251286`, token recall
    `0.987879`, diagnostic threshold met `False`.
  - `p013_geo_noexp_4unit_triage_logical_order`: similarity `0.251286`, token
    recall `0.987879`, diagnostic threshold met `False`.
  - `p013_geo_noexp_4unit_column_order_control`: similarity `0.251286`, token
    recall `0.987879`, diagnostic threshold met `False`.
- The run underperforms the previous seam-dedupe baseline (`0.25788` /
  `0.993939`) and creates no method-registry candidate or selector rule.
- `C01TEP013GNO-G1-VIRAL-001` report:
  `E3DEE3400E3DE17530F6E7D2CEC90F98D0C33B192E13817125C0BD2B6EDF712E`
- `C01TEP013GNO-G1-VIRAL-001` summary:
  `44B2FEAF02D8A511A9CF3BA965D2D1D524A4C93A51656B5D99C1802F9D621DBC`
- `C01TEP013GNO-G1-VIRAL-001` manifest:
  `16C4D7B0837832A5AC3637533236FEDE729A31D53F8E8D62914018C31036FAF6`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-EXPANDED-LANE-ORDER-DIAGNOSTIC-001

Status: `draft_execution_prep_pending_sol_terra_review`

Lane: `C01TEP013ELO-G1-VIRAL-001`

Authority: Bogdan Telegram message `2841`:

`пробуй`

Exact action:

- Run a P013-only expanded-geometry lane-order diagnostic after seam dedupe and
  no-expansion geometry both failed.
- Use cached `_G1_VIRAL_002` P013 `full_page_triage_boxes_expanded_psm4` TSV
  geometry; do not execute OCR.
- Map TSV crop-space coordinates into page-space using
  `page_x = region_page_space_left + tsv_x - 24` and
  `page_y = region_page_space_top + tsv_y - 24`.
- Use `region_results[].page_space_box` from the sealed P013 ranking, not
  original triage `crop_box_px`.
- Test only the fixed ordering modes documented in
  `core_0_1_p013_expanded_lane_order_diagnostic_plan.md`.
- Seal candidate hashes before loading the P013 reference text map for scoring.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p013_expanded_lane_order_diagnostic_plan.md`
- `scripts/run_core_0_1_text_extraction_p013_expanded_lane_order_diagnostic.py`
- `tests/test_core_0_1_text_extraction_p013_expanded_lane_order_diagnostic.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the run.

Required pinned inputs:

- Source P013 ranking SHA-256:
  `45A41E61A34C892328ABB69D988DD6947D33F32E9BFCE56771B6FCD36CEC4454`
- Source P013 expanded candidate SHA-256:
  `6AA2ADCDB1CDE71741F057300DC8888543F315BC14CD65F02602D71145CA5412`
- P013 reference text map SHA-256:
  `7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67`
- All five cached P013 raw OCR `.txt`, `.tsv`, and prepared `.png` files are
  pinned in the runner.
- Parent commit:
  `460cb459`

Limits:

- P013 only; no broader `001`-`020` run, selector update, method-registry
  update, production assembly, page `021+`, or pages `014`/`019`.
- No OCR execution, render execution, PDF parsing, reference-guided token
  insertion, accepted text mutation, semantic-map mutation, page-status
  mutation, source/raw asset mutation, runtime implementation/start,
  translation, proofreading, push, or candidate promotion.
- Diagnostic improvement over `0.25788` is not enough for method-registry
  candidacy; method-registry candidacy requires threshold met:
  sequence similarity `>= 0.997` and token recall `>= 0.993939`.

Review status:

- Sol proposed expanded-geometry lane-aware line ordering after dedupe-only and
  no-expansion geometry failed.
- Terra blocked the first proposal until TSV crop-space to page-space mapping,
  hidden reference leakage gates, raw text/TSV unit semantics, duplicate
  collapse safety, pinned inputs, and concrete deterministic parameters were
  specified.

Run output status:

- `C01TEP013ELO-G1-VIRAL-001` completed under
  `core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001`.
- No OCR was executed; candidates were assembled from cached expanded PSM4 TSV
  line records mapped into page space.
- Best diagnostic result:
  - `p013_expanded_lane_order_lane_then_y_exact_collapse`: similarity
    `0.433325`, token recall `0.993939`, diagnostic threshold met `False`.
- The lane materially improves the prior best failed baseline (`0.25788` /
  `0.993939`) without recall loss, but still remains far below the `0.997`
  threshold and creates no method-registry candidate or selector rule.
- `C01TEP013ELO-G1-VIRAL-001` report:
  `C8EFBAF8F3FFB58E0FF8CCFA41869861B6AA6F92A0E8E6DAC6F111EDC91BD3FB`
- `C01TEP013ELO-G1-VIRAL-001` summary:
  `18C8007D493FC4988F9335C1EE82C3E5BE4E7D9F0A73335E774ABBF244065881`
- `C01TEP013ELO-G1-VIRAL-001` manifest:
  `74C1985E1B8DB19375E5652E2674918F9C44202F1173EF1074C5A16D757F5C87`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-SUPPRESSION-DIAGNOSTIC-001

Status: `candidate_only_p013_structural_suppression_diagnostic_completed`

Lane: `C01TEP013SSP-G1-VIRAL-001`

Authority: Bogdan Telegram message `2842`:

`пробуй`

Exact action:

- Run a P013-only structural-suppression diagnostic after the expanded
  lane-order diagnostic improved P013 but still failed threshold.
- Use the sealed `C01TEP013ELO-G1-VIRAL-001` best retained record set as A0.
- Use cached raw TSV word confidences only to evaluate fixed structural
  suppression rules; do not execute OCR.
- Test only the fixed variants documented in
  `core_0_1_p013_structural_suppression_diagnostic_plan.md`.
- Seal candidate hashes before loading the P013 reference text map for scoring.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p013_structural_suppression_diagnostic_plan.md`
- `scripts/run_core_0_1_text_extraction_p013_structural_suppression_diagnostic.py`
- `tests/test_core_0_1_text_extraction_p013_structural_suppression_diagnostic.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the run.

Required pinned inputs:

- ELO report SHA-256:
  `C8EFBAF8F3FFB58E0FF8CCFA41869861B6AA6F92A0E8E6DAC6F111EDC91BD3FB`
- ELO manifest SHA-256:
  `74C1985E1B8DB19375E5652E2674918F9C44202F1173EF1074C5A16D757F5C87`
- ELO line records SHA-256:
  `1DEB381148397F9014C22C3263858C360FF9BAA8C64199572AD024CB578A2863`
- ELO best trace SHA-256:
  `CE27FBE19F08D9432D3D8C8C8F43FBC3E749DA05A54B995523B4BAFA0C860E94`
- ELO best collapse report SHA-256:
  `DCCBF482AAE8DAC5EC7F569BAE84422ED5487EE2676442E77120345B82E8EB73`
- Source P013 ranking SHA-256:
  `45A41E61A34C892328ABB69D988DD6947D33F32E9BFCE56771B6FCD36CEC4454`
- P013 reference text map SHA-256:
  `7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67`
- All five cached P013 raw TSV files are pinned in the runner.
- Parent commit:
  `796c7044`

Limits:

- P013 only; no broader `001`-`020` run, selector update, method-registry
  update, production assembly, page `021+`, or pages `014`/`019`.
- No OCR execution, render execution, PDF parsing, reference-guided token
  insertion, accepted text mutation, semantic-map mutation, page-status
  mutation, source/raw asset mutation, runtime implementation/start,
  translation, proofreading, push, or candidate promotion.
- Beating the ELO best failed baseline is diagnostic improvement only. A
  method-registry candidate requires diagnostic threshold met:
  sequence similarity `>= 0.997` and token recall `>= 0.993939`.

Review status:

- Sol/Terra blocked the first SSP prep because Variant C could regress below
  the ELO best baseline, reference scoring was interleaved with candidate
  generation, reference hash preflight was underspecified, transitive
  near-overlap clustering could suppress non-direct records, and the A0 floor
  was not fail-closed.
- The executable prep was revised to use `C01TEP013SSP-G1-VIRAL-001`, preserve
  A0 and floor-guarded C, generate and hash all candidates before loading
  reference text, keep reference hashing in the scoring phase, preserve
  non-clique transitive components as ambiguous, and fail closed on A0/C ELO
  floor drift.

Run output status:

- `C01TEP013SSP-G1-VIRAL-001` completed under
  `core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001`.
- No OCR was executed; candidates were assembled from the sealed ELO best
  retained set plus pinned raw TSV word confidences.
- Best diagnostic results:
  - `p013_ssp_a_near_overlap_confidence`: similarity `0.914027`, token recall
    `0.993939`, diagnostic threshold met `False`.
  - `p013_ssp_b_noise_from_a0`: similarity `0.436181`, token recall
    `0.993939`, diagnostic threshold met `False`.
  - `p013_ssp_a0_elo_exact_collapse_baseline`: similarity `0.433325`, token
    recall `0.993939`, diagnostic threshold met `False`.
  - `p013_ssp_c_floor_guarded_near_overlap_then_noise`: similarity `0.433325`,
    token recall `0.993939`, diagnostic threshold met `False`.
- The best variant materially improves the previous ELO best while preserving
  recall, but still creates no method-registry candidate or selector rule.
- `C01TEP013SSP-G1-VIRAL-001` report:
  `712446CC642C1499E9786630D9F0E136B526CC028875BF7E6D4BA4F3E1A89D9B`
- `C01TEP013SSP-G1-VIRAL-001` summary:
  `0AD50E8AAE374BB02654EC25A90EE07823AB25F0E4C3EA37EA6AAA181FF92D4B`
- `C01TEP013SSP-G1-VIRAL-001` manifest:
  `11E29CA99CBBC60B04A3466B9A665EEB9C6978F52867720D396C6A839641183E`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-ASSEMBLY-CLOSURE-DIAGNOSTIC-001

Status: `candidate_only_p013_structural_assembly_closure_diagnostic_completed`

Lane: `C01TEP013SAC-G1-VIRAL-001`

Authority: Bogdan Telegram message `2860` continuing the approved failed-page
loop:

`Следующий ход — новый цикл от этого результата: разбирать оставшийся structure/assembly gap без OCR и без reference-token insertion.`

Exact action:

- Run a P013-only structural assembly closure diagnostic after SSP improved P013
  to `0.914027` similarity and `0.993939` token recall while still failing the
  `0.997` similarity threshold.
- Use the sealed `C01TEP013SSP-G1-VIRAL-001` best retained record set as A0.
- Test only the fixed variants documented in
  `core_0_1_p013_structural_assembly_closure_diagnostic_plan.md`.
- Seal candidate text, normalized text, retained trace, suppression ledger, and
  assembly trace hashes before loading the P013 reference text map for scoring.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p013_structural_assembly_closure_diagnostic_plan.md`
- `scripts/run_core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic.py`
- `tests/test_core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the run.

Required pinned inputs:

- SSP report SHA-256:
  `712446CC642C1499E9786630D9F0E136B526CC028875BF7E6D4BA4F3E1A89D9B`
- SSP summary SHA-256:
  `0AD50E8AAE374BB02654EC25A90EE07823AB25F0E4C3EA37EA6AAA181FF92D4B`
- SSP manifest SHA-256:
  `11E29CA99CBBC60B04A3466B9A665EEB9C6978F52867720D396C6A839641183E`
- SSP-A candidate SHA-256:
  `F02D342C7FFA21FC396169294EF01713D36BB4555D3DDB54094472BC0F3EC36D`
- SSP-A normalized candidate SHA-256:
  `909B81B4614346DBD0F0C74A012CD6935A2EA3A46AEA1847E46E7401B792B8E0`
- SSP-A retained trace SHA-256:
  `6C9703A0255BA3B97A5C3872C6AF7513FFACBDAE153CB899A3E5AA1CF303A9A2`
- SSP-A suppression ledger SHA-256:
  `14FF15526D97CD2E9E6F5B39BA4FB857F83DA761AB027860174948A4778BC424`
- Source P013 ranking SHA-256:
  `45A41E61A34C892328ABB69D988DD6947D33F32E9BFCE56771B6FCD36CEC4454`
- P013 reference text map SHA-256:
  `7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67`
- All five cached P013 raw TSV files are pinned in the runner.
- Sourcefold predecessor commit for history only:
  `de0d759b9947383bf21bfe4af0bacae5f1eaff21`

Limits:

- P013 only; no broader `001`-`020` run, selector update,
  production assembly, page `021+`, or pages `014`/`019`.
- No OCR execution, render execution, PDF parsing, PDF text-layer extraction,
  image processing, reference-guided token insertion, spelling correction,
  accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw asset mutation, runtime implementation/start, translation,
  proofreading, push, or candidate promotion.
- Method-registry candidacy requires diagnostic threshold met:
  sequence similarity `>= 0.997` and token recall `>= 0.993939`.

Review status:

- Sol/Terra blocked the first SAC prep because the exact decision text did not
  match the authorization ledger, the predecessor commit was described like a
  pinned gate despite later HEAD movement, and the declared seam rule needed
  boundary-position plus token-containment/no-novel-token proof.
- The executable prep was revised to use the exact message `2860` decision,
  keep the predecessor commit as history-only, require lower/upper boundary
  proof, area-size ratio, and bounded edge-fragment token containment, and add
  negative tests for novel-token, non-boundary, non-declared, and partial
  overlap cases.
- Sol/Terra then returned OK before execution.

Run output status:

- `C01TEP013SAC-G1-VIRAL-001` completed under
  `core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001`.
- No OCR was executed; candidates were assembled from the sealed SSP best
  retained set and fixed structural deletion rules.
- Best diagnostic results:
  - `p013_sac_d_noise_then_declared_seam_fracture`: similarity `0.998915`,
    token recall `0.993939`, diagnostic threshold met `True`.
  - `p013_sac_e_paragraph_join_d`: similarity `0.998915`, token recall
    `0.993939`, diagnostic threshold met `True`.
  - `p013_sac_c_declared_seam_fracture_after_ssp`: similarity `0.99219`,
    token recall `0.993939`, diagnostic threshold met `False`.
  - `p013_sac_b_noise_after_ssp`: similarity `0.92015`, token recall
    `0.993939`, diagnostic threshold met `False`.
  - `p013_sac_a0_ssp_best_baseline`: similarity `0.914027`, token recall
    `0.993939`, diagnostic threshold met `False`.
- The combined structural deletion variants create P013 method-registry
  candidate evidence, but no selector rule, production output, promotion, or
  acceptance is created in this lane.
- `C01TEP013SAC-G1-VIRAL-001` report:
  `E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4`
- `C01TEP013SAC-G1-VIRAL-001` summary:
  `353CA98438634BA64347B9FE8F545D3BFE3A8E8FAC002677A2A9D0073A065898`
- `C01TEP013SAC-G1-VIRAL-001` manifest:
  `46343B13144DFBD3C074F7E369A4DDE97F4D2F6540F60341120B5E3DE7CF7212`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-REGISTRY-SELECTOR-001

Status: `p013_method_registry_candidate_decision_recorded`

Lane: `C01TEP013MRS-G1-VIRAL-001`

Authority: Bogdan Telegram message `2874` continuing the approved failed-page
loop after P013 SAC crossed the diagnostic threshold:

`Следующий шаг по плану: оформить отдельный reviewed method-registry/selector шаг для P013 winner, потом встраивать в общий first-pass 001-020 selector loop без плохих версий в production output.`

Exact narrowed action:

- Create a P013-only method-registry selector candidate decision record from
  sealed `C01TEP013SAC-G1-VIRAL-001` evidence.
- Select `p013_sac_d_noise_then_declared_seam_fracture` as the P013 candidate
  decision entry because it meets `0.997 / 0.993939` and ties the normalized
  score/hash of `p013_sac_e_paragraph_join_d` while using simpler `line_join`.
- Create only a static P013 selector dry-run artifact that proves the
  candidate decision selects the winner and excludes failed/superseded variants.
- Record that the P013 reference remains
  `reference_text_map_not_ocr_verified`, not independently accepted OCR truth.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p013_method_registry_selector_candidate_decision_plan.md`
- `scripts/build_core_0_1_text_extraction_p013_method_registry_selector.py`
- `tests/test_core_0_1_text_extraction_p013_method_registry_selector.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_method_registry_selector_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the decision record is generated.

Required pinned inputs:

- SAC report SHA-256:
  `E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4`
- SAC summary SHA-256:
  `353CA98438634BA64347B9FE8F545D3BFE3A8E8FAC002677A2A9D0073A065898`
- SAC manifest SHA-256:
  `46343B13144DFBD3C074F7E369A4DDE97F4D2F6540F60341120B5E3DE7CF7212`
- SAC rankings SHA-256:
  `613455DDA093EC5F7E01E4F993481D344AB37643257BF5259AC546D5A557D47A`
- Selected candidate text SHA-256:
  `E24D29CE34A61755E9B92214007EFEB8FEADC4B77D4C35468ACF64DDF9D41DE4`
- Selected normalized candidate SHA-256:
  `69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D`
- Selected retained trace SHA-256:
  `4B0628DE7BC5EF395DAAB107F6B6448A230C2E08FA24C0B4005F37FE90389A19`
- Selected suppression ledger SHA-256:
  `4A54B31E63C66AE28939FAF9A9A63A8F131F19B2E1AD2E0BBA61B29DD96B5F03`
- Selected assembly trace SHA-256:
  `EC9A97A032A1562C25839AFCD46B15792A6498AAC3FB3D5B14A7B0FEC471C62D`

Limits:

- P013 only; no page-family rule, no page `001`-`020` runtime loop, no
  pages `012`/`014`/`016`/`019`/`020`, and no page `021+`.
- No selector rule creation, selector enablement, runtime selector integration,
  production assembly, clean output folder, accepted text mutation, semantic-map
  mutation, page-status mutation, source/raw mutation, OCR execution, render
  execution, PDF parsing/text-layer extraction, reference-guided repair,
  reference-token insertion, spelling correction, token substitution,
  translation, proofreading, push, or downstream execution.

Review status:

- Sol proposed `C01TEP013MRS-G1-VIRAL-001` as a P013-only candidate
  method-registry/selector contract over sealed SAC evidence.
- Terra blocked the loose wording and allowed only a method-registry candidate
  decision record with `selector_rule_created=false`, `selector_enabled=false`,
  `runtime_selector_integration=false`, `production_assembly_created=false`, and
  `page_021_plus_included=false`.
- Fresh Sol/Terra prep review returned OK before execution.

Run output status:

- `C01TEP013MRS-G1-VIRAL-001` completed under
  `core_0_1_text_extraction_p013_method_registry_selector_G1_VIRAL_001`.
- Selected method-registry candidate decision entry:
  `C01TEP013MRS-G1-VIRAL-001-P013`.
- Selected candidate:
  `p013_sac_d_noise_then_declared_seam_fracture`.
- Metrics: similarity `0.998915`, token recall `0.993939`.
- Tie note: `p013_sac_e_paragraph_join_d` has the same normalized hash and
  metrics but remains an unselected separator-only equivalent.
- Static selector dry-run created for P013 only.
- No selector rule, selector enablement, runtime selector integration,
  production assembly, clean production output folder, accepted text mutation,
  semantic-map mutation, page-status mutation, source/raw mutation, page
  `001`-`020` runtime loop, page `021+`, translation/proofreading, push, or
  downstream execution is created.
- `C01TEP013MRS-G1-VIRAL-001` registry entry:
  `B09BF185510557CDAF3E757D381A416E2DEE52A8430B93E8293A348ACD6A56EC`
- `C01TEP013MRS-G1-VIRAL-001` selector dry-run:
  `A439914FC0AE585DF52A69CA6F6BEDA3B7E19644B0B28D5550517192B57432D7`
- `C01TEP013MRS-G1-VIRAL-001` report:
  `988FA33843EE0E35F70562E227BE7FA613CD7715982AC5FEA4BE4D3F9847B520`
- `C01TEP013MRS-G1-VIRAL-001` summary:
  `ADDD20D6C2761623AC56BD30C1B45170717D1C94617D46AE464F17995F7C1A62`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SELECTOR-REPLAY-001-020-001

Status: `static_selector_replay_completed_partial_coverage`

Lane: `C01TESEL020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2894` approving the next bounded plan after
`C01TEP013MRS-G1-VIRAL-001`:

`делай`

Exact narrowed action:

- Create a static `001`-`020` selector replay/report over sealed artifacts.
- Use `C01TEOR020-G1-VIRAL-001` only as prior overview evidence; do not rerun
  OCR.
- Materialize baseline selections for `009`/`010`/`011`/`015` with selected
  output hashes from the overview report.
- Select P013 through `C01TEP013MRS-G1-VIRAL-001-P013`.
- Keep `012`/`016`/`017`/`018`/`020` unresolved and `014`/`019` parked.
- Prove no failed or superseded candidates are selected.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_selector_replay_001_020_plan.md`
- `scripts/build_core_0_1_text_extraction_selector_replay_001_020.py`
- `tests/test_core_0_1_text_extraction_selector_replay_001_020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_selector_replay_001_020_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the selector replay report is generated.

Required pinned inputs:

- `C01TEOR020-G1-VIRAL-001` report SHA-256:
  `7FE37ECD8BAB5EAC4C9557C244D0E2CA618704783E6CFC9D706CFB60B46E0357`
- `C01TEOR020-G1-VIRAL-001` summary SHA-256:
  `EAFF1725179931084A4DA03625C52CBE1AA0C55896D54237615280EC45A81E58`
- `C01TEP013MRS-G1-VIRAL-001` registry entry SHA-256:
  `B09BF185510557CDAF3E757D381A416E2DEE52A8430B93E8293A348ACD6A56EC`
- `C01TEP013MRS-G1-VIRAL-001` report SHA-256:
  `988FA33843EE0E35F70562E227BE7FA613CD7715982AC5FEA4BE4D3F9847B520`
- `C01TEP013MRS-G1-VIRAL-001` manifest SHA-256:
  `D0183C59E85C8109962B8CE9A3605660FA1D555994958CB6492B106D1DCD8B6E`

Limits:

- Static replay/report only; no OCR execution, render execution, PDF parsing,
  PDF text-layer extraction, reference-guided repair, reference-token
  insertion, spelling correction, token substitution, accepted text mutation,
  semantic-map mutation, page-status mutation, source/raw asset mutation,
  selector runtime enablement, runtime selector integration, runtime execution,
  production assembly, clean production output folder, page `021+`,
  translation, proofreading, push, promotion, acceptance, or downstream
  execution.

Review status:

- Initial Sol/Terra review blocked because the lane artifacts did not yet exist
  and required exact routing/hash/boundary tests before OK.
- Prep files were created and focused tests passed in pre-output state
  (`1 passed`, `5 skipped`).
- Fresh Sol/Terra prep review returned OK before execution.

Run output status:

- `C01TESEL020-G1-VIRAL-001` completed under
  `core_0_1_text_extraction_selector_replay_001_020_G1_VIRAL_001`.
- Selected pages: `009`, `010`, `011`, `013`, `015`.
- Not-run ineligible pages: `001`-`008`.
- Unresolved pages requiring method winners or separate selection decisions:
  `012`, `016`, `017`, `018`, `020`.
- Parked pages requiring separate policy decisions: `014`, `019`.
- Production ready: `false`; all pages first-pass success: `false`.
- Failed or superseded candidates selected: `false`.
- No OCR execution, render execution, PDF parsing/text-layer extraction,
  accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, runtime selector integration, production assembly, clean
  production output folder, page `021+`, translation/proofreading, push,
  promotion, acceptance, or downstream execution is created.
- `C01TESEL020-G1-VIRAL-001` report:
  `5EF728BE91FA609C44591C104ACC21766F4F184217DF2E01FC151A3504BA75AF`
- `C01TESEL020-G1-VIRAL-001` selections:
  `17EEE268DA1972CF89FFC643F1BCBEC35D56DE1D959C223D2E15E769D0A0372F`
- `C01TESEL020-G1-VIRAL-001` summary:
  `583AD80F57D1ED68496F3D3872F59F796D00A811D409A514D8FA570792976210`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-DISCOVERY-001

Status: `method_discovery_completed_without_mrs_registry_input`

Lane: `C01TEP013DISC-G1-VIRAL-001`

Authority: Bogdan Telegram message `2906` requesting automation of the
search/selection pipeline after the empty-registry dry-run showed P013 would
remain unresolved:

`ну так делай`

Exact narrowed action:

- Create a P013 cold-start method discovery dry-run over available diagnostic
  method-family artifacts.
- Do not use the already-created P013 MRS registry entry as input.
- Rank candidates from `SDD`, `GNO`, `ELO`, `SSP`, and `SAC`.
- Require candidate hash sealing before reference scoring.
- Select the best threshold-passing method-registry candidate and write a fresh
  discovered entry.
- Create a P013 selector dry-run from that discovered entry.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p013_method_discovery_plan.md`
- `scripts/build_core_0_1_text_extraction_p013_method_discovery.py`
- `tests/test_core_0_1_text_extraction_p013_method_discovery.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p013_method_discovery_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the discovery report is generated.

Required pinned inputs:

- `C01TEP013SDD-G1-VIRAL-001` report SHA-256:
  `C99424139DBEBDC2F90025CC97CEB912B6E4D439820F3A68AE1281247C09E1E7`
- `C01TEP013GNO-G1-VIRAL-001` report SHA-256:
  `E3DEE3400E3DE17530F6E7D2CEC90F98D0C33B192E13817125C0BD2B6EDF712E`
- `C01TEP013ELO-G1-VIRAL-001` report SHA-256:
  `C8EFBAF8F3FFB58E0FF8CCFA41869861B6AA6F92A0E8E6DAC6F111EDC91BD3FB`
- `C01TEP013SSP-G1-VIRAL-001` report SHA-256:
  `712446CC642C1499E9786630D9F0E136B526CC028875BF7E6D4BA4F3E1A89D9B`
- `C01TEP013SAC-G1-VIRAL-001` report SHA-256:
  `E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4`

Limits:

- P013 method discovery over existing diagnostic artifacts only. No OCR
  execution, render execution, PDF parsing/text-layer extraction,
  reference-token insertion, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, selector runtime enablement,
  runtime selector integration, runtime execution, production assembly, clean
  production output folder, page `001`-`020` runtime loop, page `021+`,
  promotion, acceptance, translation/proofreading, push, or downstream
  execution.

Review status:

- Prep Sol/Terra initially blocked the candidate-id tie-break because the tied
  `p013_sac_e_paragraph_join_d` would sort ahead of the intended simpler
  `line_join` candidate.
- Fixed ranking to prefer threshold-met registry candidates, then similarity,
  token recall, `line_join` tie-break, and candidate id fallback.
- Focused pre-output tests assert the D/E tie order before artifact generation.
- Final Sol/Terra prep gate: OK.

Execution result:

- Diagnostic lanes ranked: `5`.
- Candidate records ranked: `18`.
- Discovered entry: `C01TEP013DISC-G1-VIRAL-001-P013`.
- Selected candidate: `p013_sac_d_noise_then_declared_seam_fracture`.
- Equivalent not selected: `p013_sac_e_paragraph_join_d`.
- Metrics: `0.998915 / 0.993939`.
- MRS registry input used: `false`.
- Selector dry-run scope: P013 only from the fresh discovered entry.
- Production ready: `false`.

Output hashes:

- `method_registry_entries/page_013.json`:
  `9E92035A3411C4FDB32F523D9420CB34A17AB3449CD0EA34F57E30FF6295A494`
- `p013_method_discovery_report.json`:
  `8DC4220677A7338A1BDF988D429CF4D4D1095596EAF334F3465F1E8325CC86F7`
- `p013_method_discovery_summary.md`:
  `D2E527F2A02DF59D174C603AD5ECC067B3F488222C9B1879BFC22AA8BE61F052`
- `selector_dry_run/page_013_selection.json`:
  `6036EC7BF9694E5C7C56F70C7DB994537DCA91155734D68CAB4175E460D28788`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-UNRESOLVED-PAGES-METHOD-DISCOVERY-001

Status: `unresolved_pages_method_discovery_completed_partial_coverage`

Lane: `C01TEUNRES020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2916` approving the next bounded step after
the post-commit next-action proposal:

`давай`

Exact narrowed action:

- Create an unresolved-pages method discovery dry-run for the pages left
  unresolved by `C01TESEL020-G1-VIRAL-001`: `012`, `016`, `017`, `018`, and
  `020`.
- Consume existing sealed diagnostic evidence only.
- Open fresh method entries only for pages whose existing evidence already
  meets the diagnostic threshold.
- Produce a static selector replay v2 that selects baseline pages
  `009`/`010`/`011`/`015`, P013 from `C01TEP013DISC-G1-VIRAL-001-P013`, and
  newly discovered pages `017`/`018`.
- Keep `012`, `016`, and `020` unresolved when their best existing evidence
  remains below threshold.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_unresolved_pages_method_discovery_plan.md`
- `scripts/build_core_0_1_text_extraction_unresolved_pages_method_discovery.py`
- `tests/test_core_0_1_text_extraction_unresolved_pages_method_discovery.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_unresolved_pages_method_discovery_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the discovery report is generated.

Required pinned inputs:

- `C01TESEL020-G1-VIRAL-001` report SHA-256:
  `5EF728BE91FA609C44591C104ACC21766F4F184217DF2E01FC151A3504BA75AF`
- `C01TESEL020-G1-VIRAL-001` selections SHA-256:
  `17EEE268DA1972CF89FFC643F1BCBEC35D56DE1D959C223D2E15E769D0A0372F`
- `C01TEP013DISC-G1-VIRAL-001` entry SHA-256:
  `9E92035A3411C4FDB32F523D9420CB34A17AB3449CD0EA34F57E30FF6295A494`
- `C01TEP013DISC-G1-VIRAL-001` report SHA-256:
  `8DC4220677A7338A1BDF988D429CF4D4D1095596EAF334F3465F1E8325CC86F7`
- `C01TEGP012013016017018020-G1-VIRAL-001` corrected geometry report SHA-256:
  `5A13578D917186A48ECDA8C13C5EE6998700386AA70FFF1913342FEDDB69DAFF`

Limits:

- Discovery/report only over existing sealed evidence. No OCR execution, render
  execution, PDF parsing/text-layer extraction, reference-token insertion,
  accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, selector runtime enablement, runtime selector
  integration, runtime execution, production assembly, clean production output
  folder, page `021+`, promotion, acceptance, translation/proofreading, push,
  or downstream execution.

Review status:

- Sol prep gate: OK.
- Terra prep gate initially blocked missing wrong-decision/overwrite/source-raw
  false-flag/full-negative-matrix tests.
- Focused tests were tightened and Terra re-review returned OK.

Execution result:

- Discovered pages: `017`, `018`.
- Still unresolved pages: `012`, `016`, `020`.
- Selector replay v2 selected pages:
  `009`, `010`, `011`, `013`, `015`, `017`, `018`.
- Production ready: `false`.
- All pages first-pass success: `false`.
- No OCR execution, render execution, PDF parsing/text-layer extraction,
  reference-token insertion, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, runtime selector integration,
  production assembly, clean production output folder, page `021+`, promotion,
  acceptance, or downstream execution is created.

Output hashes:

- `method_registry_entries/page_017.json`:
  `6EAD1FC9B97F19C005D06B586F90B76A4582DCE7A9BA51ED436710A0A84719A8`
- `method_registry_entries/page_018.json`:
  `03FC0EE1BEE6676510387B1B3DDDE9E58306817917975841AC69640DA4CE46F8`
- `selector_replay_v2/selector_replay_v2_selections.json`:
  `801F6B67141C8CFC15A19FEFA17C94585CF70255FB875FD6DA702E9E4E0066DA`
- `unresolved_pages_method_discovery_report.json`:
  `06FF3C64CA67F5259A1AC063A7FE34C10527280AB58B07C215B848357609DDF5`
- `unresolved_pages_method_discovery_summary.md`:
  `0A28CE5184AA1DA393BDCD2DAAB7C9415BC6B2129CE66A9923B009DC10549C67`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-012-016-020-METHOD-FAMILY-001

Status: `method_family_candidates_selected_static_evidence_only`

Lane: `C01TEMF012016020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2920` approving commit plus the planned
bounded work for pages `012`, `016`, and `020`:

`ок, комит и делай 12,16,20 что планировал`

Exact narrowed action:

- Create a bounded method-family dry-run for remaining unresolved pages
  `012`, `016`, and `020` after `C01TEUNRES020-G1-VIRAL-001`.
- Generate fixed OCR candidates only from full-page PNG geometry and triage
  page-space boxes for pages `012`, `016`, and `020`.
- Hash-seal candidate text before reference text is loaded for scoring.
- Record static method entries only for threshold-passing candidates.
- Produce selector replay v3 with baseline pages `009`/`010`/`011`/`015`,
  already discovered pages `013`/`017`/`018`, and newly discovered
  `012`/`016`/`020` if threshold is met.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_012_016_020_method_family_plan.md`
- `scripts/build_core_0_1_text_extraction_012_016_020_method_family.py`
- `tests/test_core_0_1_text_extraction_012_016_020_method_family.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_012_016_020_method_family_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the method-family report is generated.

Required pinned inputs:

- `C01TEUNRES020-G1-VIRAL-001` report SHA-256:
  `06FF3C64CA67F5259A1AC063A7FE34C10527280AB58B07C215B848357609DDF5`
- `C01TEUNRES020-G1-VIRAL-001` selector v2 SHA-256:
  `801F6B67141C8CFC15A19FEFA17C94585CF70255FB875FD6DA702E9E4E0066DA`
- `C01TEUNRES020-G1-VIRAL-001` page `017` entry SHA-256:
  `6EAD1FC9B97F19C005D06B586F90B76A4582DCE7A9BA51ED436710A0A84719A8`
- `C01TEUNRES020-G1-VIRAL-001` page `018` entry SHA-256:
  `03FC0EE1BEE6676510387B1B3DDDE9E58306817917975841AC69640DA4CE46F8`
- P012 full-page PNG SHA-256:
  `D5040085668216E68E617A06B513DC09CE3797E4D3F6BC6AC7BF35B68BD08ED6`
- P016 full-page PNG SHA-256:
  `7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56`
- P020 full-page PNG SHA-256:
  `53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E`
- P012 triage packet SHA-256:
  `93A2CCE7F4F639BFC10CAA33840FB587491FCA89827188ECDD53586B8E6A4689`
- P016 triage report SHA-256:
  `C98349F2ED24682CCBFDD3E3F9FAFE6A4EF291FBAF5B7FA09590E25B94B2E115`
- P020 triage report SHA-256:
  `92B446992A502D4DC607B9787E9A69CB13B26C1AA193F43B2C075E76F097F2F3`

Limits:

- OCR execution is allowed only for bounded candidate generation on pages
  `012`, `016`, and `020`.
- No reference-token insertion, render execution, PDF parsing/text-layer
  extraction, accepted text mutation, semantic-map mutation, page-status
  mutation, source/raw mutation, selector runtime enablement, runtime selector
  integration, runtime execution, production assembly, clean production output
  folder, page `021+`, promotion, acceptance, translation/proofreading, push,
  or downstream execution.

Review status:

- Prep gate completed; generated-output gate completed clean.

Execution result:

- Selected static method entries: `012`, `016`, and `020`.
- `012`: `p012_full_columns_scale2_psm6` at similarity/token recall
  `1.0/1.0`.
- `016`: `p016_expanded_bottom_conf60_scale2_psm6` at `0.99975/0.99802`.
- `020`: `p020_table_normalized_scale2_threshold180_psm6` at `0.99979/1.0`.
- Selector replay v3 selected pages:
  `009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, and `020`.
- Pages `001`-`008` remain not-run/ineligible, and pages `014`/`019`
  remain parked.
- Production ready: `false`.
- All pages first-pass success: `false`.
- No render execution, PDF parsing/text-layer extraction, reference-token
  insertion, accepted text mutation, semantic-map mutation, page-status
  mutation, source/raw mutation, selector runtime integration, production
  assembly, clean production output folder, page `021+`, promotion,
  acceptance, or downstream execution is created.

Output hashes:

- `012_016_020_method_family_report.json`:
  `529706EAB697961A1F1EFDD6A34EAF488B64C0082FDB87C83322A88A6578383D`
- `012_016_020_method_family_summary.md`:
  `8A4808F6769002A331C29815C348D812E151D729DB693857662BFDB4F8A6B103`
- `012_016_020_method_family_manifest.md`:
  `BFFD0DEBCF9E08EDC7E623B2E170284E3FFA7AF4A0D8A9ABC3A879EDC270DE7E`
- `selector_replay_v3/selector_replay_v3_selections.json`:
  `BFA0062BCA3F6CF9D56FED45DF813BC52014C85AD33CAF262DAD60EE34FA4A17`
- `method_registry_entries/page_012.json`:
  `91B29C338E42649E2666E033F10D9B3342EAD8BC2CD0A1C376336AFCBE6B1A4F`
- `method_registry_entries/page_016.json`:
  `C0AF109F49093C7B5182C97BCD8FA5A13704C93213F3CB66801CCE72AF3E55AF`
- `method_registry_entries/page_020.json`:
  `01E3A3BCF497BCFBE4C3817FE808E8B40BA5FF05B4CDD00E7A447352C4945341`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ASSEMBLY-READINESS-001-020-001

Status: `assembly_readiness_manifest_only_production_blocked`

Lane: `C01TEASM020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2943`, typed as `jr` and interpreted in
context as `ок`, approving the next bounded production-assembly prep/contract
step after commit `aab6ffa7`.

Exact bounded decision:

`jr`

Exact narrowed action:

- Create a manifest-only, hash-reference-only assembly-readiness dry-run for
  the selected static evidence inside pages `001`-`020`.
- Consume `C01TEMF012016020-G1-VIRAL-001` selector replay v3.
- Write a selected-page manifest only for pages
  `009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, and `020`.
- Record pages `001`-`008` as not-run/ineligible and pages `014`/`019` as
  parked blockers.
- Prove failed, weak, parked, or superseded candidates are not included.
- Keep production readiness and all-pages first-pass success false.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_assembly_readiness_001_020_plan.md`
- `scripts/build_core_0_1_text_extraction_assembly_readiness_001_020.py`
- `tests/test_core_0_1_text_extraction_assembly_readiness_001_020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001/assembly_readiness_001_020_report.json`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001/assembly_readiness_001_020_summary.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001/assembly_readiness_001_020_manifest.md`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001/assembly_manifest/selected_pages_manifest.json`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the manifest-only report is generated.

Required pinned inputs:

- `C01TEMF012016020-G1-VIRAL-001` report SHA-256:
  `529706EAB697961A1F1EFDD6A34EAF488B64C0082FDB87C83322A88A6578383D`
- `C01TEMF012016020-G1-VIRAL-001` summary SHA-256:
  `8A4808F6769002A331C29815C348D812E151D729DB693857662BFDB4F8A6B103`
- `C01TEMF012016020-G1-VIRAL-001` selector replay v3 SHA-256:
  `BFA0062BCA3F6CF9D56FED45DF813BC52014C85AD33CAF262DAD60EE34FA4A17`
- `C01TEMF012016020-G1-VIRAL-001` page `012` entry SHA-256:
  `91B29C338E42649E2666E033F10D9B3342EAD8BC2CD0A1C376336AFCBE6B1A4F`
- `C01TEMF012016020-G1-VIRAL-001` page `016` entry SHA-256:
  `C0AF109F49093C7B5182C97BCD8FA5A13704C93213F3CB66801CCE72AF3E55AF`
- `C01TEMF012016020-G1-VIRAL-001` page `020` entry SHA-256:
  `01E3A3BCF497BCFBE4C3817FE808E8B40BA5FF05B4CDD00E7A447352C4945341`
- Selected output hashes for pages `009`, `010`, `011`, `012`, `013`,
  `015`, `016`, `017`, `018`, and `020` must match the static selector replay
  v3 pin set in the builder.

Limits:

- Manifest-only and hash-reference-only. No copied candidate text, no inline
  candidate text, no OCR execution, render execution, PDF parsing/text-layer
  extraction, reference-token insertion, accepted text mutation, semantic-map
  mutation, page-status mutation, source/raw mutation, selector runtime
  enablement, runtime selector integration, runtime execution, production
  assembly, clean production output folder, page `001`-`020` runtime loop, page
  `021+`, promotion, acceptance, translation/proofreading, push, or downstream
  execution.

Review status:

- Initial Sol/Terra gate blocked missing pins, underspecified output root/files,
  predecessor ledger sync, wording drift, stale pin risk, acceptance overreach,
  and doc-sync guardrails.
- Prep updated to include exact pins, manifest-only wording, explicit output
  files, predecessor completion sync, and false production/runtime/acceptance
  flags.
- Re-review Sol/Terra gate returned OK before builder execution.

Execution result:

- Selected manifest pages:
  `009`, `010`, `011`, `012`, `013`, `015`, `016`, `017`, `018`, and `020`.
- Excluded/blocking pages:
  `001`, `002`, `003`, `004`, `005`, `006`, `007`, `008`, `014`, and `019`.
- Pages `001`-`008` remain not-run/ineligible; pages `014`/`019` remain
  parked.
- Candidate text copied: `false`.
- Candidate text inlined: `false`.
- Failed or superseded candidates in manifest: `false`.
- Production ready: `false`.
- All pages first-pass success: `false`.
- Production assembly created: `false`.
- Clean production output folder created: `false`.
- No accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, runtime selector integration, page `021+`, promotion,
  acceptance, or downstream execution is created.

Output hashes:

- `assembly_readiness_001_020_report.json`:
  `EC9A291300335CE3B05F7BF541D3C0A273FC047B4415DBC29F1E981937A7D6AB`
- `assembly_readiness_001_020_summary.md`:
  `1A3F274AD53E790183F7781ACD91EDDCE18968B5AB26D37B5F91B5D2389A21CC`
- `assembly_readiness_001_020_manifest.md`:
  `320D7964DB632D92708371C3904F8CBD99B9EA610345A24E1AFECB711814F380`
- `assembly_manifest/selected_pages_manifest.json`:
  `090352D6B97AABA628CEE692F67E1305C896D0723C8214579AE4469CF1850DE9`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ELIGIBILITY-BRIDGE-001-020-001

Status: `eligibility_bridge_static_evidence_all_pages_covered_production_blocked`

Lane: `C01TEBRIDGE020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2959` approving the clarified eligibility
bridge step:

`ок делай`

Exact narrowed action:

- Create a static dry-run eligibility bridge for pages `001`-`008`, `014`, and
  `019`.
- Consume the committed `C01TEASM020-G1-VIRAL-001` readiness report.
- Verify page-complete-only acceptance reports for pages `001`-`008`, `014`,
  and `019`.
- Classify pages `001`-`008` as `accepted_page_complete_bridge` only when their
  acceptance reports are hash-pinned.
- Classify pages `014` and `019` as
  `parked_overview_but_page_complete_accepted_bridge` only when their accepted
  artifacts are hash-pinned.
- Produce selector replay v4 showing all pages `001`-`020` covered by static
  evidence while preserving `all_pages_first_pass_success=false`.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_eligibility_bridge_001_020_plan.md`
- `scripts/build_core_0_1_text_extraction_eligibility_bridge_001_020.py`
- `tests/test_core_0_1_text_extraction_eligibility_bridge_001_020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_eligibility_bridge_001_020_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the bridge report is generated.

Required pinned inputs:

- `C01TEASM020-G1-VIRAL-001` report SHA-256:
  `EC9A291300335CE3B05F7BF541D3C0A273FC047B4415DBC29F1E981937A7D6AB`
- `C01TEASM020-G1-VIRAL-001` selected manifest SHA-256:
  `090352D6B97AABA628CEE692F67E1305C896D0723C8214579AE4469CF1850DE9`
- P001 page-complete acceptance report SHA-256:
  `0ED79F4FE7A9E239E6992CEDA9C9A73CDD3B39E6BD71BBDEC68DBCFDF6C9BF0B`
- P002 page-complete acceptance report SHA-256:
  `B136282C441D1E48DE9CE064356B3B06F6D45A500C1984901D53908335D8547C`
- P003 page-complete acceptance report SHA-256:
  `9D74A9B73D657A0669AD0025B40936E1873A9643F1F03F31279B87FCFAFA5F79`
- P004 page-complete acceptance report SHA-256:
  `57D4E5B3665129732308E042B4CECEEDD170907B2DCB852468DBBF885C222035`
- P005 page-complete acceptance report SHA-256:
  `2065A5C139E42514AD92EFB897151CE87CEEEF42208B9A7F99482B7A7F923022`
- P006 page-complete acceptance report SHA-256:
  `9D0643332F24AF2B5FF3D14518B9FF83B70B331FA1E165577A6C5245532692B5`
- P007 page-complete acceptance report SHA-256:
  `8A1B163709D47D9268602C8F2EEF5F5E880E450807468DC9EB360BE8C7CC80F5`
- P008 page-complete acceptance report SHA-256:
  `44F126668C6A6F148579787917D93199D0413F51DE0E8C3C6143AAA4047B0F64`
- P014 page-complete acceptance report SHA-256:
  `D4F8A985DCA3E7CCAB0960B1B65719E5CF59902A29AF943F32482FFA533E6946`
- P019 page-complete acceptance report SHA-256:
  `67FCCB6B34A266EC7EC007AF656E1E162B0C6CC294F275496CC1E92B40611985`

Limits:

- Static bridge/report only. No OCR execution, render execution, PDF
  parsing/text-layer extraction, reference-token insertion, accepted text
  mutation, semantic-map mutation, page-status mutation, source/raw mutation,
  selector runtime enablement, runtime selector integration, runtime execution,
  production assembly, clean production output folder, page `021+`, promotion,
  acceptance, translation/proofreading, push, or downstream execution.

Review status:

- Sol/Terra scope gate: OK.
- Prep gate: OK.

Execution result:

- Bridge pages: `001`, `002`, `003`, `004`, `005`, `006`, `007`, `008`,
  `014`, and `019`.
- Pages `001`-`008` classified as `accepted_page_complete_bridge`.
- Pages `014` and `019` classified as
  `parked_overview_but_page_complete_accepted_bridge`.
- Selector replay v4 covers all pages `001`-`020` with static evidence.
- All pages static evidence covered: `true`.
- All pages first-pass success: `false`.
- Production ready: `false`.
- Production assembly created: `false`.
- Clean production output folder created: `false`.
- No OCR execution, render execution, PDF parsing/text-layer extraction,
  reference-token insertion, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, runtime selector integration, page
  `021+`, promotion, acceptance, or downstream execution is created.

Output hashes:

- `eligibility_bridge_001_020_report.json`:
  `24BD2AC4FC990BBEC2A550341F5C8CF4858F7AB7728574EA619CB33297379998`
- `eligibility_bridge_001_020_summary.md`:
  `DC10DD28EB2D72336C11F5EA0E8C36EBA2861FBA7957FC6199F6AEE937D5AE28`
- `eligibility_bridge_001_020_manifest.md`:
  `49FF09D22017A21BB2432B6C19387D020EF737AEC95E3A615CED33AB19365013`
- `bridge_entries/accepted_page_complete_bridge_entries.json`:
  `D9557AD7A8C38383D13AF7373BED7E97ADCB48AE42B27EFF78F3CFCA8B18A231`
- `selector_replay_v4/selector_replay_v4_selections.json`:
  `A94BFC2D22AFDDB870FE93CC6A8308F96A56EA516507EA8B7CBF067414D1DCCC`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ASSEMBLY-AUTHORIZATION-001-020-001

Status: `assembly_authorization_checked_production_not_authorized`

Lane: `C01TEAUTH020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2976` approving the next continuation:

`Ок продолжай`

Exact narrowed action:

- Create a report-only final assembly-authorization check after
  `C01TEBRIDGE020-G1-VIRAL-001`.
- Consume the committed bridge report, summary, bridge entries, and selector
  replay v4.
- Record that selector replay v4 covers all pages `001`-`020` with static
  evidence.
- Preserve that `all_pages_first_pass_success=false` because coverage imports
  prior accepted page-complete bridge lanes.
- Decide that production output from mixed static evidence plus accepted bridge
  is not authorized while `all_pages_first_pass_success=false`.
- Record the two allowable next routes: fresh first-pass runtime selector
  authorization for pages `001`-`020`, or a separate explicit human exception
  decision for mixed static evidence production.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_assembly_authorization_001_020_plan.md`
- `scripts/build_core_0_1_text_extraction_assembly_authorization_001_020.py`
- `tests/test_core_0_1_text_extraction_assembly_authorization_001_020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_assembly_authorization_001_020_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the authorization report is generated.

Required pinned inputs:

- `C01TEBRIDGE020-G1-VIRAL-001` report SHA-256:
  `24BD2AC4FC990BBEC2A550341F5C8CF4858F7AB7728574EA619CB33297379998`
- `C01TEBRIDGE020-G1-VIRAL-001` summary SHA-256:
  `DC10DD28EB2D72336C11F5EA0E8C36EBA2861FBA7957FC6199F6AEE937D5AE28`
- `C01TEBRIDGE020-G1-VIRAL-001` bridge entries SHA-256:
  `D9557AD7A8C38383D13AF7373BED7E97ADCB48AE42B27EFF78F3CFCA8B18A231`
- `C01TEBRIDGE020-G1-VIRAL-001` selector replay v4 SHA-256:
  `A94BFC2D22AFDDB870FE93CC6A8308F96A56EA516507EA8B7CBF067414D1DCCC`

Limits:

- Report-only authorization check. No OCR execution, render execution, PDF
  parsing/text-layer extraction, reference-token insertion, copied candidate
  text, accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, selector runtime enablement, runtime selector
  integration, runtime execution, production assembly, clean production output
  folder, page `021+`, promotion, acceptance, translation/proofreading, push,
  or downstream execution.

Review status:

- Sol/Terra scope gate: OK.
- Prep gate: OK.

Execution result:

- Selector replay v4 covers all pages `001`-`020`.
- All pages static evidence covered: `true`.
- All pages first-pass success: `false`.
- Mixed static evidence plus accepted bridge: `true`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Production assembly created: `false`.
- Clean production output folder created: `false`.
- Decision: production assembly is not authorized from mixed static evidence
  while `all_pages_first_pass_success=false`.
- Allowed next routes are limited to fresh first-pass runtime selector
  authorization for pages `001`-`020`, or a separate explicit human exception
  decision for mixed static evidence production.
- No OCR execution, render execution, PDF parsing/text-layer extraction,
  reference-token insertion, copied candidate text, accepted text mutation,
  semantic-map mutation, page-status mutation, source/raw mutation, runtime
  selector integration, page `021+`, promotion, acceptance, or downstream
  execution is created.

Output hashes:

- `assembly_authorization_001_020_report.json`:
  `CE668EF259DF00A4BB062259279EFE3ED2C367F3CB67E58ACC9BADB29F106429`
- `assembly_authorization_001_020_summary.md`:
  `B3D4674A29162BD9A7F4F1F0F991080ADB269B1EA473E577096A42C46C3D35E8`
- `assembly_authorization_001_020_manifest.md`:
  `F3B26C015D1A043DD5201DA4A22B9C9E426AEB3B4572A3C1EDE189FFEED55765`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FIRST-PASS-RUNTIME-SELECTOR-AUTHORIZATION-001-020-001

Status: `first_pass_runtime_selector_authorization_recorded_report_only`

Lane: `C01TEFPSAUTH020-G1-VIRAL-001`

Authority: Bogdan Telegram message `2994` approving continuation into `001`-`020`:

`Идем по нашему плану, делаем 1-20?`

Exact narrowed action:

- Create a report-only route authorization packet for a future fresh first-pass
  runtime-selector run over pages `001`-`020`.
- Consume the committed `C01TEAUTH020-G1-VIRAL-001` report, summary, and
  manifest.
- Record that the authorized future route is exactly pages `001`-`020`.
- Record that this lane does not implement or execute the runtime selector and
  does not create production output.
- Preserve `production_ready=false`,
  `production_assembly_authorized=false`, `production_assembly_created=false`,
  and `clean_production_output_folder_created=false`.
- Record future guardrails: exact page set `001`-`020`, same bounded input set,
  selected best methods or validated bridge lineage only, failed/superseded
  variants excluded from clean output, and fail-closed handling for hash drift,
  missing pages, page `021+`, source/raw mutation, accepted-text/page-status
  mutation, or production output before clean first-pass success.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_first_pass_runtime_selector_authorization_001_020_plan.md`
- `scripts/build_core_0_1_text_extraction_first_pass_runtime_selector_authorization_001_020.py`
- `tests/test_core_0_1_text_extraction_first_pass_runtime_selector_authorization_001_020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_first_pass_runtime_selector_authorization_001_020_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the authorization report is generated.

Required pinned inputs:

- `C01TEAUTH020-G1-VIRAL-001` report SHA-256:
  `CE668EF259DF00A4BB062259279EFE3ED2C367F3CB67E58ACC9BADB29F106429`
- `C01TEAUTH020-G1-VIRAL-001` summary SHA-256:
  `B3D4674A29162BD9A7F4F1F0F991080ADB269B1EA473E577096A42C46C3D35E8`
- `C01TEAUTH020-G1-VIRAL-001` manifest SHA-256:
  `F3B26C015D1A043DD5201DA4A22B9C9E426AEB3B4572A3C1EDE189FFEED55765`

Limits:

- Report-only route authorization packet. No OCR execution, render execution,
  PDF parsing/text-layer extraction, reference-token insertion, copied
  candidate text, accepted text mutation, semantic-map mutation, page-status
  mutation, source/raw mutation, selector runtime enablement, runtime selector
  implementation, runtime execution, production assembly, clean production
  output folder, page `021+`, promotion, acceptance, translation/proofreading,
  push, or downstream execution.

Review status:

- Sol/Terra scope gate: OK.
- Prep gate: OK.

Execution result:

- Requested pages: `001`-`020`.
- Fresh first-pass runtime-selector route authorized: `true`.
- Runtime selector implementation created: `false`.
- Selector runtime enabled: `false`.
- Runtime execution performed: `false`.
- OCR execution performed: `false`.
- Render execution performed: `false`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Production assembly created: `false`.
- Clean production output folder created: `false`.
- Standard production remains blocked until a future clean first-pass
  runtime-selector result succeeds.
- No accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, page `021+`, promotion, acceptance, or downstream
  execution is created.

Output hashes:

- `first_pass_runtime_selector_authorization_001_020_report.json`:
  `40A0D2607B4CA2861B54ECA7E2A41742AAE1E7EAA618631F0EC08F2A335F16FF`
- `first_pass_runtime_selector_authorization_001_020_summary.md`:
  `C2C5867A96DFEC30004C8AF7211CCE0B400079C5B1D5CAA2450924D9FF096E0B`
- `first_pass_runtime_selector_authorization_001_020_manifest.md`:
  `6A5D2F992E8DCCCE5C3596990815CC894F9B90E130E4FB505D22AD83E89844DF`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FIRST-PASS-RUNTIME-SELECTOR-RUN-001-020-001

Status: `first_pass_runtime_selector_output_surface_materialized_with_bridge_lineage`

Lane: `C01TEFPSRUN020-G1-VIRAL-001`

Authority: Bogdan Telegram message `3007` authorizing real bounded work:

`Давай уже реально поработаем`

Exact narrowed action:

- Execute/materialize the bounded runtime selector route for pages `001`-`020`.
- Create a new bounded runtime output surface only.
- Materialize exactly 20 page output files.
- Preserve bridge pages as non-fresh OCR bridge lineage.
- Preserve that production, acceptance, fixture admission, and page-status/source
  mutations are not performed.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_first_pass_runtime_selector_run_001_020_plan.md`
- `scripts/build_core_0_1_text_extraction_first_pass_runtime_selector_run_001_020.py`
- `tests/test_core_0_1_text_extraction_first_pass_runtime_selector_run_001_020.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_first_pass_runtime_selector_run_001_020_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the runtime output surface is generated.

Required pinned inputs:

- `C01TEFPSAUTH020-G1-VIRAL-001` report SHA-256:
  `40A0D2607B4CA2861B54ECA7E2A41742AAE1E7EAA618631F0EC08F2A335F16FF`
- `C01TEFPSAUTH020-G1-VIRAL-001` summary SHA-256:
  `C2C5867A96DFEC30004C8AF7211CCE0B400079C5B1D5CAA2450924D9FF096E0B`
- `C01TEFPSAUTH020-G1-VIRAL-001` manifest SHA-256:
  `6A5D2F992E8DCCCE5C3596990815CC894F9B90E130E4FB505D22AD83E89844DF`
- `C01TEAUTH020-G1-VIRAL-001` report SHA-256:
  `CE668EF259DF00A4BB062259279EFE3ED2C367F3CB67E58ACC9BADB29F106429`
- `C01TEAUTH020-G1-VIRAL-001` manifest SHA-256:
  `F3B26C015D1A043DD5201DA4A22B9C9E426AEB3B4572A3C1EDE189FFEED55765`
- `C01TEASM020-G1-VIRAL-001` selected pages manifest SHA-256:
  `090352D6B97AABA628CEE692F67E1305C896D0723C8214579AE4469CF1850DE9`
- `C01TEBRIDGE020-G1-VIRAL-001` bridge entries SHA-256:
  `D9557AD7A8C38383D13AF7373BED7E97ADCB48AE42B27EFF78F3CFCA8B18A231`
- `C01TEBRIDGE020-G1-VIRAL-001` selector replay v4 SHA-256:
  `A94BFC2D22AFDDB870FE93CC6A8308F96A56EA516507EA8B7CBF067414D1DCCC`

Limits:

- Runtime output materialization only. No source/raw/accepted/page-status
  mutation, fixture admission, whole Gate 1 acceptance, page `021+`,
  translation/proofreading, push, promotion, acceptance, or downstream
  execution.

Review status:

- Sol/Terra scope gate: blockers found and cleared by added pinning,
  per-page lineage, bridge/non-fresh flags, and generated-output assertions.

Execution result:

- Output page files created: `20`.
- Runtime selected pages: `009`, `010`, `011`, `012`, `013`, `015`, `016`,
  `017`, `018`, and `020`.
- Bridge lineage pages: `001`-`008`, `014`, and `019`.
- All pages materialized: `true`.
- All pages fresh OCR success: `false`.
- Runtime execution performed: `true`.
- Runtime output surface created: `true`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.
- No source/raw/accepted/page-status mutation, fixture admission, whole Gate 1
  acceptance, page `021+`, push, or downstream execution is created.

Output hashes:

- `first_pass_runtime_selector_run_001_020_report.json`:
  `2896B6D682A38AACC713FEC4E60015A8840008B161D0364C2EEC825B4B85041B`
- `first_pass_runtime_selector_run_001_020_summary.md`:
  `1D7EE3D7F985F6A84C0CF75A032025078C955101710E3C64CF30EB02562F3326`
- `first_pass_runtime_selector_run_001_020_manifest.md`:
  `9E931134745B8C1C6E898E3D451D3EE8F36A3C12BA9C9734C5FD300A0C07B5CD`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-AUDIT-001-008-014-019-001

Status: `bridge_page_audit_completed_no_ocr_no_mutation`

Lane: `C01TEBRIDGEAUD020-G1-VIRAL-001`

Authority: Bogdan Telegram message `3019` instructing orchestration by the
five-step plan:

`Ок иди по плану, ты оркестратор, следи чтоб все было сделанл`

Exact narrowed action:

- Audit only bridge-lineage pages `001`-`008`, `014`, and `019`.
- Classify each page by existing asset availability for the next route away
  from bridge lineage.
- Pin inspected asset/report paths and SHA-256 hashes.
- Do not execute OCR and do not create fresh first-pass success.
- Preserve all production/acceptance/mutation gates as false.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_bridge_page_audit_001_008_014_019_plan.md`
- `scripts/build_core_0_1_text_extraction_bridge_page_audit_001_008_014_019.py`
- `tests/test_core_0_1_text_extraction_bridge_page_audit_001_008_014_019.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the audit report is generated.

Required pinned inputs:

- `C01TEFPSRUN020-G1-VIRAL-001` report SHA-256:
  `2896B6D682A38AACC713FEC4E60015A8840008B161D0364C2EEC825B4B85041B`
- `C01TEFPSRUN020-G1-VIRAL-001` manifest SHA-256:
  `9E931134745B8C1C6E898E3D451D3EE8F36A3C12BA9C9734C5FD300A0C07B5CD`
- `C01TEBRIDGE020-G1-VIRAL-001` bridge entries SHA-256:
  `D9557AD7A8C38383D13AF7373BED7E97ADCB48AE42B27EFF78F3CFCA8B18A231`
- `C01TEBRIDGE020-G1-VIRAL-001` selector replay v4 SHA-256:
  `A94BFC2D22AFDDB870FE93CC6A8308F96A56EA516507EA8B7CBF067414D1DCCC`

Limits:

- Report-only audit. No OCR execution, render execution,
  PDF parsing/text-layer extraction, accepted text mutation, semantic-map
  mutation, page-status mutation, source/raw mutation, fixture admission,
  production assembly, page `021+`, promotion, acceptance,
  translation/proofreading, push, or downstream execution.

Review status:

- Sol proposal gate: OK.
- Terra blocker gate: blockers found and cleared by closed route enum,
  per-asset SHA pins, asset-availability-only wording, and generated-output
  assertions.

Execution result:

- Audited pages: `001`, `002`, `003`, `004`, `005`, `006`, `007`, `008`,
  `014`, and `019`.
- `visual_only_no_text_rule`: `001`.
- `fresh_ocr_route_possible`: `003`, `004`, `005`, `006`, `007`, `008`,
  `014`, and `019`.
- `needs_source_asset_recovery`: `002`.
- `fresh_ocr_assets_missing`: none.
- OCR execution performed: `false`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- No source/raw/accepted/page-status mutation, fixture admission, page `021+`,
  push, or downstream execution is created.

Output hashes:

- `bridge_page_audit_001_008_014_019_report.json`:
  `25CF7B2DB7864EFD1FA7B58095905724FFE087E84E34BDEB81FB34D404008E02`
- `bridge_page_audit_001_008_014_019_summary.md`:
  `744A454B62EAA08F197276C770C4CEAEF496FF7ED173E1D9B909A65CD64A6639`
- `bridge_page_audit_001_008_014_019_manifest.md`:
  `D69D1286238213ECDB957667428D0FC721C352DB44FB737B34E5BC7B26E6B738`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-REMEDIATION-AUTHORIZATION-001-008-014-019-001

Status: `bridge_page_remediation_authorization_recorded_report_only`

Lane: `C01TEBRIDGEREMAUTH020-G1-VIRAL-001`

Authority: Bogdan Telegram message `3019` instructing orchestration by the
five-step plan:

`Ок иди по плану, ты оркестратор, следи чтоб все было сделанл`

Exact narrowed action:

- Consume the committed `C01TEBRIDGEAUD020-G1-VIRAL-001` audit artifacts.
- Record a report-only authorization for a future bounded bridge-page
  remediation runner.
- Split page `001` as visual-only/no-text materialization only, not fresh OCR
  success.
- Keep page `002` blocked as `needs_source_asset_recovery`.
- Validate pages `003`-`008` as full-page-region candidate policy surfaces
  under `ocr_input_surface_policy`.
- Validate pages `014` and `019` as text-evidence smoke/non-promotable surfaces
  under `ocr_input_surface_policy`.
- Do not execute OCR in this authorization lane.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_bridge_page_remediation_authorization_001_008_014_019_plan.md`
- `scripts/build_core_0_1_text_extraction_bridge_page_remediation_authorization_001_008_014_019.py`
- `tests/test_core_0_1_text_extraction_bridge_page_remediation_authorization_001_008_014_019.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_remediation_authorization_001_008_014_019_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the authorization report is generated.

Required pinned inputs:

- `C01TEBRIDGEAUD020-G1-VIRAL-001` report SHA-256:
  `25CF7B2DB7864EFD1FA7B58095905724FFE087E84E34BDEB81FB34D404008E02`
- `C01TEBRIDGEAUD020-G1-VIRAL-001` summary SHA-256:
  `744A454B62EAA08F197276C770C4CEAEF496FF7ED173E1D9B909A65CD64A6639`
- `C01TEBRIDGEAUD020-G1-VIRAL-001` manifest SHA-256:
  `D69D1286238213ECDB957667428D0FC721C352DB44FB737B34E5BC7B26E6B738`

Limits:

- Report-only authorization. No OCR execution, render execution,
  PDF parsing/text-layer extraction, accepted text mutation, semantic-map
  mutation, page-status mutation, source/raw mutation, fixture admission,
  production assembly, clean production output folder, page `021+`, promotion,
  acceptance, translation/proofreading, push, or downstream execution.

Review status:

- Sol proposal gate: OK.
- Terra proposal gate: blocked direct OCR runner; this lane closes that blocker
  by adding a separate fail-closed authorization and explicit input-surface
  policy split before any remediation runner.

Execution result:

- Visual-only/non-text page: `001`.
- Source asset recovery blocker: `002`.
- Full-page-region candidate policy pages: `003`, `004`, `005`, `006`, `007`,
  and `008`.
- Text-evidence smoke/non-promotable pages: `014` and `019`.
- OCR input surface policy validation: `passed`.
- OCR execution performed: `false`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.
- No source/raw/accepted/page-status mutation, fixture admission, page `021+`,
  push, or downstream execution is created.

Output hashes:

- `bridge_page_remediation_authorization_001_008_014_019_report.json`:
  `9DD604336DA642FB575DEBD5180885DC04289ECE82647FB4ECD4518056C74A60`
- `bridge_page_remediation_authorization_001_008_014_019_summary.md`:
  `0C2B64917035F58F9142671AECEFA11880A0E4568408381748EAB46A24B7E00C`
- `bridge_page_remediation_authorization_001_008_014_019_manifest.md`:
  `E19100825A3E157179A72341A9EE8E59DB3D533273AACF87C394C4774EF49AE5`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-REMEDIATION-RUN-001-008-014-019-001

Status: `bridge_page_remediation_run_materialized_candidate_only`

Lane: `C01TEBRIDGEREM020-G1-VIRAL-001`

Authority: Bogdan Telegram message `3019` instructing orchestration by the
five-step plan:

`Ок иди по плану, ты оркестратор, следи чтоб все было сделанл`

Exact narrowed action:

- Consume hash-pinned `C01TEBRIDGEREMAUTH020-G1-VIRAL-001` authorization
  artifacts and `C01TEBRIDGEAUD020-G1-VIRAL-001` audit artifacts.
- Keep page `001` as visual-only/no-text materialization, not OCR success.
- Keep page `002` blocked as `needs_source_asset_recovery`.
- Run Tesseract only for full-page-region candidate-policy pages `003`-`008`.
- Keep pages `014` and `019` as text-evidence smoke/non-promotable routes with
  no Tesseract invocation.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_bridge_page_remediation_run_001_008_014_019_plan.md`
- `scripts/run_core_0_1_text_extraction_bridge_page_remediation_001_008_014_019.py`
- `tests/test_core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the remediation run is generated.

Required pinned inputs:

- `C01TEBRIDGEREMAUTH020-G1-VIRAL-001` report SHA-256:
  `9DD604336DA642FB575DEBD5180885DC04289ECE82647FB4ECD4518056C74A60`
- `C01TEBRIDGEREMAUTH020-G1-VIRAL-001` summary SHA-256:
  `0C2B64917035F58F9142671AECEFA11880A0E4568408381748EAB46A24B7E00C`
- `C01TEBRIDGEREMAUTH020-G1-VIRAL-001` manifest SHA-256:
  `E19100825A3E157179A72341A9EE8E59DB3D533273AACF87C394C4774EF49AE5`
- `C01TEBRIDGEAUD020-G1-VIRAL-001` report SHA-256:
  `25CF7B2DB7864EFD1FA7B58095905724FFE087E84E34BDEB81FB34D404008E02`
- `C01TEBRIDGEAUD020-G1-VIRAL-001` summary SHA-256:
  `744A454B62EAA08F197276C770C4CEAEF496FF7ED173E1D9B909A65CD64A6639`
- `C01TEBRIDGEAUD020-G1-VIRAL-001` manifest SHA-256:
  `D69D1286238213ECDB957667428D0FC721C352DB44FB737B34E5BC7B26E6B738`

Limits:

- Candidate-only remediation output. No production assembly, accepted text
  mutation, semantic-map mutation, page-status mutation, source/raw mutation,
  persisted raw OCR output, fixture admission, clean production output folder,
  page `021+`, promotion, acceptance, translation/proofreading, push, or
  downstream execution.

Review status:

- Sol/Terra proposal gates: OK for this lane only if pages `014`/`019` remain
  smoke/non-promotable text-evidence routes with no Tesseract invocation.

Execution result:

- Visual-only/non-text page: `001`.
- Source asset recovery blocker: `002`.
- Full-page-region OCR candidate pages: `003`, `004`, `005`, `006`, `007`, and
  `008`.
- Text-evidence smoke/non-promotable pages: `014` and `019`; Tesseract was not
  invoked for either page.
- Fresh OCR success pages: none, because this lane has no pinned reference
  scoring surface for `003`-`008`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.
- No source/raw/accepted/page-status mutation, fixture admission, page `021+`,
  push, or downstream execution is created.

Output hashes:

- `bridge_page_remediation_run_001_008_014_019_report.json`:
  `6A135FCBB5337BDADD4F59C23BB3F79A1FB077450524BADE7C90E8EA5FCA60CB`
- `bridge_page_remediation_run_001_008_014_019_summary.md`:
  `3161D2355BBA24C25E727E1914BCCDF8B49FCC56BBD979C818D6668B0F8A2124`
- `bridge_page_remediation_run_001_008_014_019_manifest.md`:
  `BBC6A64419BC7B23EFCCF429D6DA17247B05CCAE3FE0EAF81FE593D9BE1362E5`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-SCORING-REFERENCE-AUDIT-003-008-001

Status: `bridge_page_scoring_reference_audit_completed`

Lane: `C01TEBRIDGESCOREAUD020-G1-VIRAL-001`

Authority: Bogdan Telegram message `3019` instructing orchestration by the
five-step plan:

`Ок иди по плану, ты оркестратор, следи чтоб все было сделанл`

Exact narrowed action:

- Consume hash-pinned `C01TEBRIDGEREM020-G1-VIRAL-001` report, summary,
  manifest, and candidate text files for pages `003`-`008`.
- Verify each candidate hash before loading the exact pinned comparison surface
  for that page.
- Record diagnostic comparison metrics and reference-surface authority
  classification for pages `003`-`008` only.
- Keep pages `001`, `002`, `014`, `019`, and `021+` out of scope.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_bridge_page_scoring_reference_audit_003_008_plan.md`
- `scripts/build_core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008.py`
- `tests/test_core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the audit is generated.

Required pinned inputs:

- `C01TEBRIDGEREM020-G1-VIRAL-001` report SHA-256:
  `6A135FCBB5337BDADD4F59C23BB3F79A1FB077450524BADE7C90E8EA5FCA60CB`
- `C01TEBRIDGEREM020-G1-VIRAL-001` summary SHA-256:
  `3161D2355BBA24C25E727E1914BCCDF8B49FCC56BBD979C818D6668B0F8A2124`
- `C01TEBRIDGEREM020-G1-VIRAL-001` manifest SHA-256:
  `BBC6A64419BC7B23EFCCF429D6DA17247B05CCAE3FE0EAF81FE593D9BE1362E5`
- Candidate text pages `003`-`008` SHA-256 values:
  `7DD3AB82753B6887D4F23E173DE641B5333E9E00A7390CB8CF6372AE3B624B94`,
  `89A33BADB6D31AFF09C673D4FD38327416AEF39967B4886547B82EF6D70E9268`,
  `E8511E024041F4691D58AC8E17E6BC10B1D2BACA3B36AF3CEABDE02025FF7999`,
  `897533EA70B021368E2A7A5953082817C1F80997C564BD9D4535AFBE33D9C162`,
  `8A6405797F1F8E646059C64FA1CD54A4DA803B11B52BBAADADEC04CF59BE9F59`,
  and `00E6C5700EA835552EBB6E1F1D8D776D4DD7AA7713018A7A74D6B992A01ACBE6`.

Limits:

- Diagnostic comparison audit only. No OCR execution, render execution,
  PDF parsing/text-layer extraction, accepted text mutation, semantic-map
  mutation, page-status mutation, source/raw mutation, fixture admission,
  production assembly, clean production output folder, page `021+`, promotion,
  acceptance, translation/proofreading, push, or downstream execution.

Review status:

- Sol/Terra proposal gates returned concrete blockers: create a dedicated lane,
  synchronize next-route/status, pin candidate/reference inputs, reject page-set
  expansion, record current HEAD separately from the remediation `base_commit`,
  and classify references as bounded comparison surfaces rather than independent
  truth. This lane closes those blockers.

Execution result:

- Audit pages: `003`, `004`, `005`, `006`, `007`, and `008`.
- All six pages have pinned comparison/reference surfaces.
- Pages `003` and `004` use lower-authority OCR block text comparison surfaces.
- Pages `005`-`008` use bounded page-complete OCR-verified text map comparison
  surfaces.
- Fresh OCR success pages: none.
- Promotable pages: none.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.
- No OCR execution, source/raw/accepted/page-status mutation, fixture admission,
  page `021+`, push, promotion, or downstream execution is created.

Output hashes:

- `bridge_page_scoring_reference_audit_003_008_report.json`:
  `7927E9B5C24C6689C6321D1CBA4FB71BFE6F4107C622B4824638C4AC068D95D5`
- `bridge_page_scoring_reference_audit_003_008_summary.md`:
  `85A0725A721E9C0EA25BCBAB146EFD643CEB7DDE1E2337492AF3E27D686FB443`
- `bridge_page_scoring_reference_audit_003_008_manifest.md`:
  `0DE9E1D3F3EEA7D734841DBD3D4E897B2355A561AFC07A4EE8FC92529F5C1E2D`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-RECOVERY-AUDIT-001

Status: `p002_source_asset_recovery_audit_completed_report_only_no_ocr_no_mutation`

Lane: `C01TEP002ASSETREC-G1-VIRAL-001`

Authority: Bogdan Telegram message `3019` instructing orchestration by the
five-step plan:

`Ок иди по плану, ты оркестратор, следи чтоб все было сделанл`

Exact narrowed action:

- Consume hash-pinned bridge audit, bridge remediation, and bridge scoring audit
  artifacts.
- Consume hash-pinned existing P002 page image, page-map/page-complete reports,
  source-reconstruction reports, corrected crop references, and manifests.
- Classify page `002` recoverability from existing assets.
- Record authority risk from the stale generator hash in the strongest P002
  source-acceptance chain.
- Keep the bridge blocker uncleared and require a separate bounded
  materialization authorization before any recovered assets are materialized.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_source_asset_recovery_audit_plan.md`
- `scripts/build_core_0_1_text_extraction_p002_source_asset_recovery_audit.py`
- `tests/test_core_0_1_text_extraction_p002_source_asset_recovery_audit.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_source_asset_recovery_audit_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the audit is generated.

Required pinned inputs:

- `C01TEBRIDGEAUD020-G1-VIRAL-001` report/summary/manifest SHA-256:
  `25CF7B2DB7864EFD1FA7B58095905724FFE087E84E34BDEB81FB34D404008E02`,
  `744A454B62EAA08F197276C770C4CEAEF496FF7ED173E1D9B909A65CD64A6639`,
  `D69D1286238213ECDB957667428D0FC721C352DB44FB737B34E5BC7B26E6B738`
- `C01TEBRIDGEREM020-G1-VIRAL-001` report/summary/manifest SHA-256:
  `6A135FCBB5337BDADD4F59C23BB3F79A1FB077450524BADE7C90E8EA5FCA60CB`,
  `3161D2355BBA24C25E727E1914BCCDF8B49FCC56BBD979C818D6668B0F8A2124`,
  `BBC6A64419BC7B23EFCCF429D6DA17247B05CCAE3FE0EAF81FE593D9BE1362E5`
- `C01TEBRIDGESCOREAUD020-G1-VIRAL-001` report/summary/manifest SHA-256:
  `7927E9B5C24C6689C6321D1CBA4FB71BFE6F4107C622B4824638C4AC068D95D5`,
  `85A0725A721E9C0EA25BCBAB146EFD643CEB7DDE1E2337492AF3E27D686FB443`,
  `0DE9E1D3F3EEA7D734841DBD3D4E897B2355A561AFC07A4EE8FC92529F5C1E2D`
- P002 page image SHA-256:
  `ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9`
- P002 page-complete acceptance report SHA-256:
  `B136282C441D1E48DE9CE064356B3B06F6D45A500C1984901D53908335D8547C`
- P002 page-complete review report/manifest SHA-256:
  `D84968D6E839D2CF07603FDFD4A7D05112B7F8DBE1984E21788F1BA253C23BB9`,
  `9323EE68AED33840FD8C9031630749CED4709A7A1499965BD491B22E145E9D5E`
- P002 page-map-readiness report/manifest SHA-256:
  `3F957442194211F6F0EC39775ED292DEF126222E98EEFB5BFFD1530D8EA702D6`,
  `5AB662AF36355A75F73758EF4B73BF13F0315986AF40B2F9234BBE84B489173A`
- P002 source-reconstruction next-slice report/manifest SHA-256:
  `1A9A693883277635B02E02F143284280C1FBA1F928FF950843586B8A1C5EC224`,
  `B4D8E6AA3D08DFD78D16F72FD3774B57051F4AABCE32062C3B36E924466C6DCD`
- P002 assisted draft report/manifest SHA-256:
  `296763B5942B937B66822E4988C30FF5B96FBFBFF08952987FA5E8D22CE07F05`,
  `D6E50079093DEDA2F178D744E19DA29650CF3B2667B1F5418D4CB02F018E4280`
- P002 assisted draft verification report/manifest SHA-256:
  `BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52`,
  `B6E3D871FCA061D1672CB5E73A1BFF6C73AAE7D0C7F8B2A7044BD451FAC9159A`
- P002 completion/next-review report/manifest SHA-256:
  `A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F`,
  `8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6`
- P002 corrected crop refs SHA-256:
  `D281969D790D4BF7661DDF841924FA6A0B9F8965088580A0FA89B64DA9599E6D`,
  `D167F253964076DA67D7A6D625BB236875CA05E634710C10F1FD816C46B1BE4B`

Limits:

- Report-only source asset recovery audit. No `review_assets` materialization,
  OCR execution, render execution, PDF parsing/text-layer extraction, accepted
  text mutation, semantic-map mutation, page-status mutation, source/raw
  mutation, fixture admission, production assembly, clean production output
  folder, page `021+`, promotion, acceptance, translation/proofreading, push, or
  downstream execution.

Review status:

- Sol proposal gate: OK for report-only recoverability classification.
- Terra proposal gate: blocked absent lane, stale completion generator hash,
  authority gap, and missing negative coverage. This lane closes those blockers
  by creating the dedicated report-only lane, surfacing stale-generator risk,
  keeping the blocker uncleared, and adding focused negative tests.

Execution result:

- Page: `002` only.
- Asset recovery classification:
  `recoverable_from_pinned_page_image_and_source_reconstruction_artifacts`.
- Source-acceptance chain authority risk:
  `stale_generator_hash_in_completion_artifact`.
- Bridge blocker cleared: `false`.
- Review assets materialized: `false`.
- OCR/Tesseract executed: `false`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.
- No source/raw/accepted/page-status mutation, fixture admission, page `021+`,
  push, promotion, or downstream execution is created.

Output hashes:

- `p002_source_asset_recovery_audit_report.json`:
  `A1D88F383DDF5F8654DBBEFEEEBEE391F955EB4C61C01C490009533430B9E140`
- `p002_source_asset_recovery_audit_summary.md`:
  `B34EB8461DD931C2E18341905C056AADC5EDE78D510D249FB2B771EF8838235F`
- `p002_source_asset_recovery_audit_manifest.md`:
  `061FE0C03A176953E585FCCF80962DB6CAA9F338E7CDF0299A9F14A8923AFDAB`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-MATERIALIZATION-AUTHORIZATION-001

Status: `p002_source_asset_materialization_authorization_recorded_future_lane_only_no_materialization_no_mutation`

Lane: `C01TEP002ASSETMATAUTH-G1-VIRAL-001`

Authority: Bogdan Telegram message `3050` authorizing broad orchestration,
delegation, expanded planning, and commits:

`Давай уже широким планом пойдем. Бери вполном объёме. Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю.`

Exact narrowed action:

- Consume committed `C01TEP002ASSETREC-G1-VIRAL-001` report, summary, and
  manifest by exact hash.
- Authorize only a future bounded page `002` source asset materialization lane.
- Preserve `stale_generator_hash_in_completion_artifact` as an authority risk.
- Keep `bridge_blocker_cleared=false` and require a later materialization/output
  review before any bridge blocker removal or page/source acceptance.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_source_asset_materialization_authorization_plan.md`
- `scripts/build_core_0_1_text_extraction_p002_source_asset_materialization_authorization.py`
- `tests/test_core_0_1_text_extraction_p002_source_asset_materialization_authorization.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_source_asset_materialization_authorization_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the authorization is generated.

Required pinned inputs:

- `C01TEP002ASSETREC-G1-VIRAL-001` report/summary/manifest SHA-256:
  `A1D88F383DDF5F8654DBBEFEEEBEE391F955EB4C61C01C490009533430B9E140`,
  `B34EB8461DD931C2E18341905C056AADC5EDE78D510D249FB2B771EF8838235F`,
  `061FE0C03A176953E585FCCF80962DB6CAA9F338E7CDF0299A9F14A8923AFDAB`

Limits:

- Authorization-only. No `review_assets` materialization, OCR/Tesseract,
  render execution, PDF parsing/text-layer extraction, accepted text mutation,
  semantic-map mutation, page-status mutation, source/raw mutation, fixture
  admission, production assembly, bridge blocker clearing, page `021+`,
  promotion, acceptance, translation/proofreading, push, or downstream
  execution.

Execution result:

- Page: `002` only.
- Future materialization lane authorized: `true`.
- Materialization performed: `false`.
- Review assets materialized: `false`.
- Bridge blocker cleared: `false`.
- Source-acceptance chain authority risk:
  `stale_generator_hash_in_completion_artifact`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.

Output hashes:

- `p002_source_asset_materialization_authorization_report.json`:
  `37D85ADA6E3AB6CAAA7D8F82F488F53281AE740A8BDD8D4D82AE83264FB6811B`
- `p002_source_asset_materialization_authorization_summary.md`:
  `6FAB886C6FEC44ADDCC6F06749143369779402D958AC397CAAE01EA605CE45F8`
- `p002_source_asset_materialization_authorization_manifest.md`:
  `984FDD1BCB291F01D3E9690B5812A7DC5A3072F115BD8D2965B871E1A5541431`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-MATERIALIZATION-001

Status: `p002_source_asset_materialization_completed_output_surface_only_no_blocker_clearance_no_mutation`

Lane: `C01TEP002ASSETMAT-G1-VIRAL-001`

Authority: `C01TEP002ASSETMATAUTH-G1-VIRAL-001` authorized a future bounded
page `002` materialization lane from the pinned recovery audit.

Exact narrowed action:

- Consume committed `C01TEP002ASSETMATAUTH-G1-VIRAL-001` and
  `C01TEP002ASSETREC-G1-VIRAL-001` artifacts by exact hash.
- Copy only the pinned page `002` full page image and two corrected crop refs
  into a new lane-owned output root.
- Preserve `stale_generator_hash_in_completion_artifact` as an authority risk.
- Keep `bridge_blocker_cleared=false`.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_source_asset_materialization_plan.md`
- `scripts/run_core_0_1_text_extraction_p002_source_asset_materialization.py`
- `tests/test_core_0_1_text_extraction_p002_source_asset_materialization.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_source_asset_materialization_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the materialization is generated.

Required pinned inputs:

- `C01TEP002ASSETMATAUTH-G1-VIRAL-001` report/summary/manifest SHA-256:
  `37D85ADA6E3AB6CAAA7D8F82F488F53281AE740A8BDD8D4D82AE83264FB6811B`,
  `6FAB886C6FEC44ADDCC6F06749143369779402D958AC397CAAE01EA605CE45F8`,
  `984FDD1BCB291F01D3E9690B5812A7DC5A3072F115BD8D2965B871E1A5541431`
- `C01TEP002ASSETREC-G1-VIRAL-001` report/summary/manifest SHA-256:
  `A1D88F383DDF5F8654DBBEFEEEBEE391F955EB4C61C01C490009533430B9E140`,
  `B34EB8461DD931C2E18341905C056AADC5EDE78D510D249FB2B771EF8838235F`,
  `061FE0C03A176953E585FCCF80962DB6CAA9F338E7CDF0299A9F14A8923AFDAB`
- Page `002` source asset SHA-256:
  `ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9`
- Page `002` corrected crop refs SHA-256:
  `D281969D790D4BF7661DDF841924FA6A0B9F8965088580A0FA89B64DA9599E6D`,
  `D167F253964076DA67D7A6D625BB236875CA05E634710C10F1FD816C46B1BE4B`

Limits:

- Materialization output surface only. No historical `review_assets` write,
  OCR/Tesseract, render execution, PDF parsing/text-layer extraction, accepted
  text mutation, semantic-map mutation, page-status mutation, source/raw
  mutation, fixture admission, production assembly, bridge blocker clearing,
  page `021+`, promotion, acceptance, translation/proofreading, push, or
  downstream execution.

Execution result:

- Page: `002` only.
- Materialized assets: full page image plus two corrected crop refs.
- Materialized asset hashes match pinned source hashes.
- Historical page-complete review `review_assets` mutated: `false`.
- Bridge blocker cleared: `false`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.

Output hashes:

- `p002_source_asset_materialization_report.json`:
  `82D51C020E5571C7FDB86040CC0E3469EC0CE26A1C4A49286B0135E13A39315F`
- `p002_source_asset_materialization_summary.md`:
  `3962117A4EE8737788B0FE60ADB57C4BB9E5338ABDE03835E1B56BEBD732B038`
- `p002_source_asset_materialization_manifest.md`:
  `8F32E3FBEB3B671857B65FCD769627B8545F471B4E5F8DDF062D4FDDFD62EFE6`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-MATERIALIZED-SURFACE-REVIEW-001

Status: `p002_materialized_surface_review_completed_asset_recovery_blocker_cleared_no_ocr_no_acceptance`

Lane: `C01TEP002MATREVIEW-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002ASSETMAT-G1-VIRAL-001`; this lane reviews only the
committed materialized page `002` surface before any fresh OCR route decision.

Exact narrowed action:

- Consume committed `C01TEP002ASSETMAT-G1-VIRAL-001` report/summary/manifest by
  exact hash.
- Verify the lane-owned page `002` full page image and two corrected crop refs
  by SHA-256.
- Clear only the asset-recovery blocker and set the next blocker to
  `needs_fresh_ocr_route_authorization`.
- Preserve `fresh_ocr_success=false`.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_materialized_surface_review_plan.md`
- `scripts/build_core_0_1_text_extraction_p002_materialized_surface_review.py`
- `tests/test_core_0_1_text_extraction_p002_materialized_surface_review.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_materialized_surface_review_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the review is generated.

Required pinned inputs:

- `C01TEP002ASSETMAT-G1-VIRAL-001` report/summary/manifest SHA-256:
  `82D51C020E5571C7FDB86040CC0E3469EC0CE26A1C4A49286B0135E13A39315F`,
  `3962117A4EE8737788B0FE60ADB57C4BB9E5338ABDE03835E1B56BEBD732B038`,
  `8F32E3FBEB3B671857B65FCD769627B8545F471B4E5F8DDF062D4FDDFD62EFE6`

Limits:

- Review/decision evidence only. No OCR/Tesseract, render execution, PDF
  parsing/text-layer extraction, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, fixture admission, production
  assembly, fresh OCR success, page `021+`, promotion, acceptance,
  translation/proofreading, push, or downstream execution.

Execution result:

- Page: `002` only.
- Materialized surface available: `true`.
- Materialized surface hash verified: `true`.
- Asset recovery blocker cleared: `true`.
- Bridge blocker cleared: `true`.
- Fresh OCR success: `false`.
- Next blocker: `needs_fresh_ocr_route_authorization`.
- Production ready: `false`.
- Production assembly authorized: `false`.
- Acceptance performed: `false`.

Output hashes:

- `p002_materialized_surface_review_report.json`:
  `0B047CF8B9FA2E7B77D3CB73C296F11070198F4C2EEB4B1585882EE91DFFFA1F`
- `p002_materialized_surface_review_summary.md`:
  `8E293FB620CE6503D341FC4EB5F882FF6A98F807C04FEDD51FFE170E8E939AD7`
- `p002_materialized_surface_review_manifest.md`:
  `CCBFD30FCCCAE5C0659C08817F1524CF3A3740FC87600D6956D6F20555AE6D7B`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-SCORING-AUTHORIZATION-003-008-001

Status: `bridge_page_scoring_authorization_recorded_no_promotion_no_scoring`

Lane: `C01TEBRIDGESCOREAUTH020-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEBRIDGESCOREAUD020-G1-VIRAL-001`; this lane records only the
future bounded scoring/remediation authority split for pages `003`-`008`.

Exact narrowed action:

- Consume committed `C01TEBRIDGESCOREAUD020-G1-VIRAL-001` report/summary/manifest
  by exact hash.
- Record that existing diagnostic audit metrics do not authorize fresh OCR
  success or promotion.
- Authorize only a future bounded scoring decision or remediation strategy.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_bridge_page_scoring_authorization_003_008_plan.md`
- `scripts/build_core_0_1_text_extraction_bridge_page_scoring_authorization_003_008.py`
- `tests/test_core_0_1_text_extraction_bridge_page_scoring_authorization_003_008.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_scoring_authorization_003_008_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the authorization is generated.

Required pinned inputs:

- `C01TEBRIDGESCOREAUD020-G1-VIRAL-001` report/summary/manifest SHA-256:
  `7927E9B5C24C6689C6321D1CBA4FB71BFE6F4107C622B4824638C4AC068D95D5`,
  `85A0725A721E9C0EA25BCBAB146EFD643CEB7DDE1E2337492AF3E27D686FB443`,
  `0DE9E1D3F3EEA7D734841DBD3D4E897B2355A561AFC07A4EE8FC92529F5C1E2D`

Limits:

- Authorization/report only. No scoring, OCR/Tesseract, render execution, PDF
  parsing/text-layer extraction, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, fixture admission, production
  assembly, fresh OCR success, promotion, acceptance, page `021+`,
  translation/proofreading, push, or downstream execution.

Execution result:

- Pages: `003`, `004`, `005`, `006`, `007`, `008`.
- Existing audit metrics authorize fresh success: `false`.
- Existing audit metrics authorize promotion: `false`.
- Future scoring decision authorized: `true`.
- Promotion authorized: `false`.
- Fresh OCR success: `false`.
- Production ready: `false`.
- Acceptance performed: `false`.

Output hashes:

- `bridge_page_scoring_authorization_003_008_report.json`:
  `A77528B265D52AEF0ED56C35E2F559AAACB937CBF190B27CA0F17684A13AB09A`
- `bridge_page_scoring_authorization_003_008_summary.md`:
  `3FAACCA70F855C82DD606BB6B433688071841F734C6B8997DF0E17AA92FE3232`
- `bridge_page_scoring_authorization_003_008_manifest.md`:
  `E4CAFF5D01B987BC1CEC5EF04C87FA24A2764090BB036FC5C2FCBB4FCEE94513`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P014-P019-ROUTE-DECISION-001

Status: `p014_p019_route_decision_recorded_full_page_ocr_route_required_no_execution`

Lane: `C01TEP014019ROUTEDEC-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEBRIDGEREM020-G1-VIRAL-001`; this lane records only the route
decision for parked bridge pages `014` and `019`.

Exact narrowed action:

- Consume committed bridge audit/remediation artifacts by exact hash.
- Hash-pin page-complete acceptance/review surfaces, page images, and text maps
  for pages `014` and `019`.
- Confirm existing text-evidence smoke outputs are non-promotable and cannot
  clear bridge lineage.
- Authorize only a future separate full-page OCR route for pages `014` and
  `019`.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p014_p019_route_decision_plan.md`
- `scripts/build_core_0_1_text_extraction_p014_p019_route_decision.py`
- `tests/test_core_0_1_text_extraction_p014_p019_route_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p014_p019_route_decision_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the decision is generated.

Limits:

- Route decision only. No OCR/Tesseract, scoring, render execution, PDF
  parsing/text-layer extraction, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, fixture admission, production
  assembly, fresh OCR success, promotion, acceptance, page `021+`,
  translation/proofreading, push, or downstream execution.

Execution result:

- Pages: `014`, `019`.
- Existing text-evidence smoke clears bridge: `false`.
- Existing text-evidence smoke creates fresh OCR success: `false`.
- Future full-page OCR route authorized: `true`.
- Text-evidence crops may be used as OCR input: `false`.
- Production ready: `false`.
- Acceptance performed: `false`.

Output hashes:

- `p014_p019_route_decision_report.json`:
  `BC4D6569FE50C59374C0A1D54B3A23611D267D08B6759F8B5D726FEC8D989458`
- `p014_p019_route_decision_summary.md`:
  `5AF33BFEB0E3750597AF4A400849128CF2D429C2AD2BDA334D576F2D83DEF18E`
- `p014_p019_route_decision_manifest.md`:
  `77C243CD1FB4C1AB70EE7902BA005216477DFD6B5FDC6C2B7FBADB332F2E42C9`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P014-P019-FULL-PAGE-OCR-001

Status: `p014_p019_full_page_ocr_completed_candidate_only_no_promotion`

Lane: `C01TEP014019FPOCR-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP014019ROUTEDEC-G1-VIRAL-001`; that committed route decision
authorized only a separate full-page OCR route for parked bridge pages `014`
and `019`.

Exact narrowed action:

- Consume committed `C01TEP014019ROUTEDEC-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Hash-pin page `014` and `019` full-page images and text-map comparison
  surfaces.
- Run Tesseract only on full-page-region input surfaces for pages `014` and
  `019`.
- Seal candidate text hashes before loading comparison text maps for diagnostic
  metrics.
- Keep the lane candidate-only and non-promotable.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p014_p019_full_page_ocr_plan.md`
- `scripts/run_core_0_1_text_extraction_p014_p019_full_page_ocr.py`
- `tests/test_core_0_1_text_extraction_p014_p019_full_page_ocr.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p014_p019_full_page_ocr_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the run is generated.

Limits:

- No text-evidence crop OCR input, accepted text mutation, semantic-map
  mutation, page-status mutation, source/raw mutation, fixture admission,
  production assembly, fresh OCR success, bridge removal, promotion,
  acceptance, page `021+`, translation/proofreading, push, or downstream
  execution.

Execution result:

- Pages: `014`, `019`.
- Tesseract-invoked pages: `014`, `019`.
- Input surface class: `full_page_region`.
- Text-evidence crops used as OCR input: `false`.
- Candidate count: `4`.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotion performed: `false`.
- Production ready: `false`.
- Acceptance performed: `false`.

Output hashes:

- `p014_p019_full_page_ocr_report.json`:
  `0238FFA8B0D91FAE6047E426AA59BA606668EAB589B14FD112AE5615A4877F32`
- `p014_p019_full_page_ocr_summary.md`:
  `4250181B5F35A1A8809A965190F0831B7F58FCAC73C3974A9BED18BF216B0E19`
- `p014_p019_full_page_ocr_manifest.md`:
  `EB1DA1D11FAF85315363F7EE8213F34F381603719898A9EB2E353D6F36D4175B`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-ROUTE-AUTH-001

Status: `p002_fresh_ocr_route_authorized_no_execution`

Lane: `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002MATREVIEW-G1-VIRAL-001`; that committed review cleared the
asset-recovery blocker and left page `002` blocked on
`needs_fresh_ocr_route_authorization`.

Exact narrowed action:

- Consume committed `C01TEP002MATREVIEW-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Verify page `002` remains ready for a separate fresh OCR route.
- Authorize only a future bounded fresh OCR candidate route from the lane-owned
  full-page image.
- Keep corrected crop refs as comparison-only surfaces, not OCR input.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_fresh_ocr_route_authorization_plan.md`
- `scripts/build_core_0_1_text_extraction_p002_fresh_ocr_route_authorization.py`
- `tests/test_core_0_1_text_extraction_p002_fresh_ocr_route_authorization.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_route_authorization_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the authorization is generated.

Limits:

- Authorization only. No OCR/Tesseract, candidate text, render execution, PDF
  parsing/text-layer extraction, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, fixture admission, production
  assembly, fresh OCR success, bridge removal, promotion, acceptance, page
  `021+`, translation/proofreading, push, or downstream execution.

Execution result:

- Page: `002`.
- Fresh OCR route authorized: `true`.
- Future OCR input surface class: `full_page_region`.
- Corrected crop refs authorized as OCR input: `false`.
- Corrected crop refs authorized for comparison only: `true`.
- OCR execution performed: `false`.
- Fresh OCR success: `false`.
- Bridge blocker cleared: `false`.
- Next action: `separate_bounded_p002_fresh_ocr_candidate_execution`.

Output hashes:

- `p002_fresh_ocr_route_authorization_report.json`:
  `6EE1925A65367833898D0E17150687E341F411C1B7D6EDDD0219671593F6AC68`
- `p002_fresh_ocr_route_authorization_summary.md`:
  `096069AC2AE284A852448D0DE3B8347F9369FF89BC851850742D646D1583B741`
- `p002_fresh_ocr_route_authorization_manifest.md`:
  `C0AA3147BB065FB8F0EA4F88A5D86E84F0C5B06CB9F8EAAC41DD4417AD2C444D`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-CANDIDATE-001

Status: `p002_fresh_ocr_candidate_executed_candidate_only_no_scoring_no_promotion`

Lane: `C01TEP002FRESHOCR-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`; that committed route
authorization permits only a separate page `002` fresh OCR candidate execution
from the lane-owned full-page image.

Exact narrowed action:

- Consume committed `C01TEP002FRESHROUTEAUTH-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Run Tesseract only on the lane-owned page `002` full-page image.
- Generate PSM `4` and PSM `6` candidate text and metadata.
- Keep corrected crop refs as comparison-only surfaces, not OCR input.
- Do not load reference-scoring surfaces in this lane.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_fresh_ocr_candidate_plan.md`
- `scripts/run_core_0_1_text_extraction_p002_fresh_ocr_candidate.py`
- `tests/test_core_0_1_text_extraction_p002_fresh_ocr_candidate.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_candidate_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization after
  the candidate run is generated.

Limits:

- Candidate execution only. No corrected-crop OCR input, reference scoring,
  accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, fixture admission, production assembly, fresh OCR
  success, bridge removal, promotion, acceptance, page `021+`,
  translation/proofreading, push, or downstream execution.

Execution result:

- Page: `002`.
- Tesseract-invoked pages: `002`.
- PSM values: `[4, 6]`.
- Candidate count: `2`.
- Corrected crop refs used as OCR input: `false`.
- Reference scoring performed: `false`.
- Fresh OCR success: `false`.
- Bridge blocker cleared: `false`.
- Next action: `separate_bounded_p002_candidate_scoring_or_remediation_decision`.

Output hashes:

- `p002_fresh_ocr_candidate_report.json`:
  `5686F161296BD696E8F97B00DB9560F2374E6FAC74B4DA223490FF2ECFC473D2`
- `p002_fresh_ocr_candidate_summary.md`:
  `4AE2AE00372FADB5E523982A438ABDDAD69F5CB6EA8EB5F706A2D87FA399A3A5`
- `p002_fresh_ocr_candidate_manifest.md`:
  `FEE45C27C759FCCBD67DF2CC44B8F65D4249644FCC3DA9A289612FBDC721B155`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-SCORING-REFERENCE-AUDIT-001

Status: `p002_fresh_ocr_scoring_reference_audit_completed`

Lane: `C01TEP002FRESHSCOREAUD-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002FRESHOCR-G1-VIRAL-001`; the committed candidate lane
allows only a separate page `002` scoring/reference audit before any scoring or
remediation decision.

Exact narrowed action:

- Consume committed `C01TEP002FRESHOCR-G1-VIRAL-001` report/summary/manifest
  by exact hash.
- Consume PSM `4` and PSM `6` candidate texts by exact hash.
- Audit pinned page `002` comparison/reference surfaces only.
- Perform diagnostic comparison metrics only.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_fresh_ocr_scoring_reference_audit_plan.md`
- `scripts/build_core_0_1_text_extraction_p002_fresh_ocr_scoring_reference_audit.py`
- `tests/test_core_0_1_text_extraction_p002_fresh_ocr_scoring_reference_audit.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_scoring_reference_audit_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization.

Limits:

- Diagnostic comparison only. No OCR/Tesseract, independent acceptance truth,
  fresh OCR success, bridge removal, accepted text mutation, semantic-map
  mutation, page-status mutation, source/raw mutation, fixture admission,
  production assembly, promotion, acceptance, page `021+`, push, or downstream
  execution.

Execution result:

- Page: `002`.
- Candidate labels: `psm4`, `psm6`.
- Reference scoring performed: `true`.
- Scoring scope: `diagnostic_comparison_only`.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotable pages: `[]`.
- Next action: `separate_bounded_p002_candidate_scoring_or_remediation_decision`.

Output hashes:

- `p002_fresh_ocr_scoring_reference_audit_report.json`:
  `0834F4A864105F6D15D243198F743158C9D91ECDAF5AAEA4A4281913DD481740`
- `p002_fresh_ocr_scoring_reference_audit_summary.md`:
  `3E42702616B3C4F1267559290F9D4BE303DC1A5CDC342C10ED11F8E32C396D7E`
- `p002_fresh_ocr_scoring_reference_audit_manifest.md`:
  `BF9B57598F7FAC66DEDFAF25D6CC1692C278AB9CA185BAC9DE06FD0AE4839FFB`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-SCORING-DECISION-001

Status: `p002_fresh_ocr_scoring_decision_completed_remediation_required`

Lane: `C01TEP002FRESHDECIDE-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002FRESHSCOREAUD-G1-VIRAL-001`; this lane can make only a
bounded scoring/remediation-routing decision, not acceptance or bridge removal.

Exact narrowed action:

- Consume committed `C01TEP002FRESHSCOREAUD-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Consume PSM `4` and PSM `6` candidate texts by exact hash.
- Consume human-verified P002 assisted-draft verification surfaces by exact
  hash as comparison evidence.
- Select the best candidate and decide whether strict threshold is met.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_fresh_ocr_scoring_decision_plan.md`
- `scripts/build_core_0_1_text_extraction_p002_fresh_ocr_scoring_decision.py`
- `tests/test_core_0_1_text_extraction_p002_fresh_ocr_scoring_decision.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_scoring_decision_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization.

Limits:

- Scoring decision only. No OCR/Tesseract, fresh OCR success, bridge removal,
  accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, fixture admission, production assembly, promotion,
  acceptance, page `021+`, push, or downstream execution.

Execution result:

- Page: `002`.
- Best candidate: `psm4`.
- PSM `4` similarity/token recall: `0.996182` / `0.985507`.
- PSM `6` similarity/token recall: `0.307332` / `0.978261`.
- Strict threshold: `0.997`.
- Decision: `remediation_required_before_fresh_ocr_success`.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotable pages: `[]`.
- Next action: `bounded_p002_candidate_remediation_from_best_candidate_and_visual_verified_diffs`.

Output hashes:

- `p002_fresh_ocr_scoring_decision_report.json`:
  `C745B2EBF02001D0F4ACD4AD836DFC534C59B799911A2FAB96785CBB3F50471B`
- `p002_fresh_ocr_scoring_decision_summary.md`:
  `7B72F72E6480BDDDD6FF61947F2425F8BB0E5DF8446AF1EEA56F3EDF02CD3D50`
- `p002_fresh_ocr_scoring_decision_manifest.md`:
  `0283F681EE24683AA6BBC6EA1F2818F7DC9680E6DCB8D56B1D91FCE476260713`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-REMEDIATION-AUTHORIZATION-001

Status: `p002_fresh_ocr_remediation_authorized_no_execution`

Lane: `C01TEP002FRESHREMAUTH-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002FRESHDECIDE-G1-VIRAL-001`; this lane can authorize only a
future remediation execution, not run it or promote its result.

Exact narrowed action:

- Consume committed `C01TEP002FRESHDECIDE-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Authorize future bounded page `002` remediation from best candidate `psm4`
  and visual-verified discrepancy evidence.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_fresh_ocr_remediation_authorization_plan.md`
- `scripts/build_core_0_1_text_extraction_p002_fresh_ocr_remediation_authorization.py`
- `tests/test_core_0_1_text_extraction_p002_fresh_ocr_remediation_authorization.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_remediation_authorization_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization.

Limits:

- Authorization only. No OCR/Tesseract, remediation execution, fresh OCR
  success, bridge removal, accepted text mutation, semantic-map mutation,
  page-status mutation, source/raw mutation, fixture admission, production
  assembly, promotion, acceptance, page `021+`, push, or downstream execution.

Execution result:

- Page: `002`.
- Authorized future action:
  `bounded_p002_candidate_remediation_from_best_candidate_and_visual_verified_diffs`.
- Authorized best candidate: `psm4`.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotable pages: `[]`.
- Next action: `separate_bounded_p002_fresh_ocr_remediation_execution`.

Output hashes:

- `p002_fresh_ocr_remediation_authorization_report.json`:
  `42ABC318A2B283F27CDCA13AE14FAF26C1256F71BA1B0BE263E4448E00BD49FF`
- `p002_fresh_ocr_remediation_authorization_summary.md`:
  `17F1B59A17E229965712CB5B21E64EFC9703F7EBDB5768E17475066492F76A05`
- `p002_fresh_ocr_remediation_authorization_manifest.md`:
  `F9E54880261ACC456F5FA9116F6A15743E2741FAEBC5481CFD2396DD7CF131A8`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-REMEDIATION-001

Status: `p002_fresh_ocr_remediation_executed_candidate_only`

Lane: `C01TEP002FRESHREM-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002FRESHREMAUTH-G1-VIRAL-001`; this lane can execute only
the authorized remediated candidate output, not pass/fresh-success promotion.

Exact narrowed action:

- Consume committed `C01TEP002FRESHREMAUTH-G1-VIRAL-001`
  report/summary/manifest by exact hash.
- Consume PSM `4` candidate text by exact hash.
- Consume human-verified P002 assisted-draft verification report by exact hash.
- Create one lane-owned remediated candidate text.

Allowed outputs:

- `docs/plans/20260715-sourcefold-phase-0-release-charter/core_0_1_p002_fresh_ocr_remediation_plan.md`
- `scripts/run_core_0_1_text_extraction_p002_fresh_ocr_remediation.py`
- `tests/test_core_0_1_text_extraction_p002_fresh_ocr_remediation.py`
- `fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_p002_fresh_ocr_remediation_G1_VIRAL_001/*`
- Status, roadmap, context, plan, and authorization-ledger synchronization.

Limits:

- Remediation candidate only. No OCR/Tesseract, fresh OCR success, bridge
  removal, accepted text mutation, semantic-map mutation, page-status mutation,
  source/raw mutation, fixture admission, production assembly, promotion,
  acceptance, page `021+`, push, or downstream execution.

Execution result:

- Page: `002`.
- Source candidate: `psm4`.
- Operations: `insert_missing_header`, `replace_visual_verified_token`.
- Similarity/token recall after remediation: `1.0` / `1.0`.
- Threshold met after remediation: `true`.
- Fresh OCR success pages: `[]`.
- Bridge removed pages: `[]`.
- Promotable pages: `[]`.
- Next action: `separate_bounded_p002_remediated_candidate_pass_decision`.

Output hashes:

- `p002_fresh_ocr_remediation_report.json`:
  `F4A650F37B28B89787DF81D95B7526BFBDD513DFC91175895644C9E2C67C5551`
- `p002_fresh_ocr_remediation_summary.md`:
  `D4A84A7FB795B87F4D21E5753D30B9CEB9F1949B1B3A81F0F9A545354F216F52`
- `p002_fresh_ocr_remediation_manifest.md`:
  `9BFA3E92BBD3953A5B2290D0CB31AFC89780ED963726F63DA08B8AE09668379F`
- `candidate_texts/page_002_full_page_psm4_remediated_candidate.md`:
  `E8D84506A1069EFD417028A65132F0E378C90010E421B645E593215152EA9B7C`

## BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-PASS-DECISION-001

Status: `p002_fresh_ocr_pass_decision_completed`

Lane: `C01TEP002FRESHPASS-G1-VIRAL-001`

Authority: Broad orchestration authorization permits continuing the bounded
plan after `C01TEP002FRESHREM-G1-VIRAL-001`; this lane can record only the
page `002` fresh OCR pass decision, not production or acceptance.

Execution result:

- Page: `002`.
- Fresh OCR success pages: `["002"]`.
- Bridge removed pages: `["002"]`.
- Promotable pages: `["002"]`.
- Production ready: `false`.
- Acceptance performed: `false`.
- Next action:
  `refresh_clean_001_020_runtime_selector_or_continue_remaining_page_pass_decisions`.

Output hashes:

- `p002_fresh_ocr_pass_decision_report.json`:
  `167A900F18B10B8E4507F7FE7461946526680A5EC8A68C4605445460BBCA4609`
- `p002_fresh_ocr_pass_decision_summary.md`:
  `C0BE3C169B19FDD2E179236C7632E9B870E59412FF69E8139B0FB41F64DD406F`
- `p002_fresh_ocr_pass_decision_manifest.md`:
  `E102FEED6864F17F89B0EE14A9A23FC4B611282A6D1FEC90EC65DCFC6BE424D7`
