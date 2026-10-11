# Sourcefold Product Boundary

Sourcefold is one modular product for text truth and accepted Russian masters.
Its core promise is that source meaning, structure, and data survive
reconstruction, translation, and proofreading before any downstream rendering.

## Core Lane

| Module | Product question | Accepted output |
|---|---|---|
| `reconstruct` | Do we have reliable structured source text? | Accepted Source Text |
| `translate` | Does RU preserve source meaning, structure, and data? | Faithful RU Draft |
| `proofread` | Is Russian reader-ready without meaning or data drift? | Proofread RU Master |

## Optional Lanes

`press` may render Markdown, HTML, or PDF from an accepted RU master. It must not
repair, mask, or reinterpret unresolved core findings.

`bridge` may export accepted artifacts to explicit external systems. It must
record the source artifact, export contract, and destination assumptions.

## Out Of Scope

Knowledge base generation, cross-book rule integration, and unified reference
systems are future directions. They may consume accepted Sourcefold artifacts
later, but they are not part of ordinary book processing.

## Legacy Boundary

`translator` remains legacy implementation evidence. Sourcefold can learn from
its concepts, failures, and reviews, but does not inherit its runtime namespace,
status, package history, prompts, or file structure.
