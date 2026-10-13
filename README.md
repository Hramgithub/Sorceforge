# Sorceforge

Репозиторий проекта **Sourcefold** (название продукта; `Sorceforge` — только
имя репозитория).

## Состояние (2026-10-13)

Ветка `main` очищена по решению владельца. Здесь остались только материалы
аудита и handoff-документы. Код, скрипты, тесты, фикстуры и evidence
Sourcefold Phase 0 удалены из рабочей ветки.

## Где старый код

| Что | Где |
|---|---|
| Sourcefold (весь Phase 0: скрипты, тесты, фикстуры, evidence, роадмап) | `https://github.com/Hramgithub/NRI`, каталог `Sourcefold/` (коммит `22fafc14`); локально `C:\_Hobby\_work\NRI\Sourcefold` |
| kb_creator | `https://github.com/Hramgithub/NRI`, каталог `kb_creator/`; локально `C:\_Hobby\_work\NRI\kb_creator` |
| Полный standalone-снимок до очистки | история этого репозитория, коммит `72ea9be` |

## Что здесь

- `docs/project-goal.md` — **цель проекта**, место в экосистеме (kb_creator,
  git_coc, Foundry, словарь CoC), критерии достижения и открытые вопросы.
- `Sourcefold/docs/audit/20261013-idea-vs-implementation.md` — аудит идеи и
  реализации; выводы и варианты дальнейшего пути.
- `Sourcefold/docs/plans/20261012-sourcefold-baseline-debt-audit/` —
  технический аудит 13 падающих тестов и целостности хэшей (приостановлен;
  пути в нём относятся к снимку `72ea9be`).
- `Sourcefold/docs/handoff/` — handoff-описание проекта для новой модели
  (описывает состояние до очистки).
- `AGENTS.md` — правила работы в репозитории.
