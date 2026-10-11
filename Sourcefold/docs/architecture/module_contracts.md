# Module Contracts

Sourcefold modules exchange accepted artifacts with explicit provenance. A
module may run independently only when its required upstream artifact and
acceptance evidence already exist.

## Shared Contract Rules

- Inputs are immutable within a run.
- Outputs record their producing module, source artifact, tool/model versions,
  QA state, and acceptance state.
- Findings stay open until resolved or explicitly waived with rationale.
- Downstream modules consume accepted upstream artifacts, not ad hoc work files.
- Optional lanes cannot satisfy missing core acceptance.

## Core Flow

```text
Source Evidence
  -> reconstruct
Accepted Source Text
  -> translate
Faithful RU Draft
  -> proofread
Proofread RU Master
```

QA can send work back to an earlier module. The process is a governed DAG, not a
one-way wizard.

## Contract Files

- `contracts/reconstruct.md`
- `contracts/translate.md`
- `contracts/proofread.md`
- `contracts/press.md`
- `contracts/bridge.md`
