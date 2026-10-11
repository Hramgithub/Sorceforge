# Translator Evidence Index

`translator` is legacy evidence. Sourcefold may mine principles and lessons from
specific reviewed documents, but must not inherit old structure, commands,
package prompts, current status, runtime artifacts, or governance.

| Legacy path | Useful evidence | Must not inherit |
|---|---|---|
| `translator/docs/architecture/translator_charter_20260713.md` | Mission around accepted source text, faithful RU draft, proofread RU master, hard quality invariants, downstream publishing boundary, stop rule. | `Translator` naming, old deliverable framing, implementation assumptions, command surface. |
| `translator/docs/architecture/translator_concept_review_20260713.md` | Three core stages, publishing as downstream, KB as future separate product, failure lesson that damaged reconstruction invalidates downstream polish. | Incident-specific plan state, historical hardening backlog, Viral package context. |
| `translator/docs/architecture/product_naming_review_20260714.md` | `Sourcefold` working name, one modular product, core module names, optional `press` and `bridge`, future `RuleAtlas` boundary. | Naming confidence beyond working proposal, package/domain assumptions, old namespace migration plan. |
| `Sourcefold/docs/architecture/bootstrap_document_set_20260714.md` | First scaffold file list and extraction rules. | Any implication that legacy implementation has been migrated. |
| `docs/governance/nri_goal_governance.md` | Current NRI goal bundle, handoff, watchdog, and review standard. | None; this is current governance, not legacy Translator evidence. |

Future entries must record path, revision or commit when available, what is
useful, and what remains legacy-only.
