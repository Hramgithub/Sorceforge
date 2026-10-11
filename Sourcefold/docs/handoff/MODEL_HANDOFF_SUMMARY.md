# Sourcefold — краткая передача проекта другой модели

- Актуальность снимка: 11 октября 2026 года.
- Репозиторий: `https://github.com/Hramgithub/Sorceforge.git`.
- Ветка: `main`.
- Изученная базовая ревизия: `7c880d60320ba11c7a80f62fb804722cfac1548b`.
- Продукт называется **Sourcefold**; `Sorceforge` — только имя репозитория.

Подробная эксплуатационная спецификация:
[MODEL_HANDOFF_SPEC.md](MODEL_HANDOFF_SPEC.md). Готовый стартовый промпт:
[NEW_MODEL_PROMPT.md](NEW_MODEL_PROMPT.md).

## Суть за 60 секунд

Sourcefold — модульный, проверяемый и fail-closed продукт для превращения
неизменяемого исходного материала в принятый русский текстовый мастер. Целевая
цепочка разделена на три обязательных контракта:

```text
immutable source evidence
  -> reconstruct -> accepted source text
  -> translate   -> faithful RU draft
  -> proofread   -> accepted RU master
```

Дополнительные модули `press` и `bridge` могут соответственно создавать
Markdown/HTML/PDF-проекции и явные внешние экспорты, но только из принятого
предшественника. Они не могут исправить или обойти непринятый источник.

Сейчас Sourcefold — не готовый универсальный конвейер новой книги. Это развитая
Phase 0 среда квалификации источника и реконструкции: контракты, схемы,
авторизации, Python-инструменты, тесты и большая база управляемых доказательств
на материале Viral. Перевод, вычитка и production-сборка целой книги ещё не
доказаны как завершённый общий runtime.

## Зачем проект создавался

Sourcefold выделяет общие уроки старых NRI-процессов в новый продукт без
наследования legacy-архитектуры `translator`. Он нужен, чтобы:

- не путать OCR-наблюдение, реконструированный текст и принятый источник;
- сохранять структуру страниц: заголовки, выделения, списки, таблицы, карточки,
  статблоки, иллюстрации и trace anchors;
- привязывать каждый переход к точным входам, хэшам, авторизации и решению;
- останавливать работу при неоднозначности вместо молчаливого угадывания;
- сохранять неудачные и superseded-кандидаты как доказательства, не смешивая их
  с будущим production-output;
- отделять реконструкцию, перевод, вычитку, выпуск и интеграции;
- переносить процесс между моделями и машинами без потери границ полномочий.

## Что уже сделано

1. **Определён продукт.** Зафиксированы границы `reconstruct`, `translate`,
   `proofread`, а также необязательных `press` и `bridge`. KB generation вынесен
   в отдельное будущее направление.
2. **Введено управление работой.** Созданы Phase/Gate hierarchy, vocabulary
   принятия, artifact lineage, bounded authorization, goal governance и
   независимый release-review.
3. **Создана дорожная карта.** YAML-roadmap, интерактивный viewer,
   package-backed validator и documentation checkpoint связаны с планами.
4. **Проведена квалификация Viral.** Сохранены immutable PDF, page/region maps,
   pre-OCR evidence, OCR benchmark, geometry/crop policies и управляемые
   candidate inputs.
5. **Пройдены ограниченные human/QA loops.** Отдельные записи текста и страниц
   реконструировались, проверялись человеком, проходили QA и в некоторых случаях
   принимались строго в названном scope.
6. **Развита OCR-диагностика.** Для страниц 001–020 созданы политики входной
   поверхности, selector replay, method discovery, geometry и remediation
   пробы. Часть результатов использует fresh OCR, часть — выбранных кандидатов,
   часть — bridge к ранее принятой page-complete evidence.
7. **Записано ограниченное Gate-решение.** `G1WGADR-G1-VIRAL-001` принимает
   Gate 1 только для страниц 001–020 и конкретных групп G1FADAR: одной
   положительной и четырёх отрицательных. Это не закрывает глобальный Gate 1 и
   не разрешает страницы 021+, перевод, вычитку или production.
8. **Позднее улучшена страница 002.** `C01TEP002FRESHPASS-G1-VIRAL-001`
   фиксирует fresh OCR success, снятие bridge и promotable status для P002 после
   bounded human-backed remediation. Это не автономный first-pass успех и не
   source/production acceptance.
9. **Проект вынесен из NRI.** В standalone-репозиторий перенесены все
   управляемые исходные файлы и доказательства, добавлены локальные правила,
   проверки и release receipts. Исторические runtime/temp-файлы не переносились.

## На каком этапе проект сейчас

- В дорожной карте **Phase 0** и глобальный **Gate 1 Source Profile** остаются
  `active`.
- Одновременно существуют отдельные принятые записи, page slices, fixture
  groups и bounded whole-Gate decision для страниц 001–020. Эти области нельзя
  ни игнорировать, ни расширять.
- `Core 0.1 RC` остаётся `planned`; более поздние beta/production stages —
  `proposed`.
- Press/Bridge previews и более широкий OCR/KB scope отложены.
- Нет доказанного production-ready whole-book pipeline, завершённого русского
  мастера или разрешения начинать новую книгу.
- Нет текущего действующего разрешения повторять старый OCR-run. Историческая
  авторизация не переносится автоматически на новую модель или машину.

## Текущее проверенное состояние standalone

На базовой ревизии `7c880d6`:

- 3987 отслеживаемых файлов;
- 193 документа, 186 Python/PowerShell scripts, 179 test files;
- 3408 управляемых fixture/evidence files;
- пять module contracts, одна manifest schema и один roadmap-validator;
- roadmap validation: 6 statuses, 7 lanes, 26 nodes, 25 edges,
  254 documentation checkpoints;
- focused Python suite: 37 passed, 1 skipped;
- full collection: 1029 tests — 989 passed, 27 skipped, 13 failed.

Двенадцать падений — старые несовпадения SHA в цепочках evidence и
воспроизводятся в исходном NRI. Ещё один тест требует исторический executable
`D:\NRI\.tools\tesseract\tesseract.exe`. Это известный долг, а не регрессия
standalone-export, но полный набор тестов нельзя называть зелёным.

## Технологии в двух словах

- **Python** — контракты, bounded producers, JSON/файловые манифесты, SHA-256,
  проверки lineage, OCR orchestration и тесты.
- **pytest** — негативные и регрессионные проверки контрактов и evidence.
- **Pillow** — размеры, crops, preprocessing и image-aware проверки.
- **Tesseract** — контролируемые English OCR candidates с TXT/TSV evidence.
- **Node/npm + `yaml@2.9.0`** — воспроизводимая проверка roadmap YAML.
- **PowerShell** — Windows wrappers и documentation checkpoint.
- **HTML/JavaScript** — интерактивный reader дорожной карты; не источник
  истины и не acceptance evidence.
- **Git + SHA-256** — история, точная идентичность и перенос доказательств.

Python dependencies пока не имеют project lockfile. Tesseract привязан к
историческому абсолютному пути. Roadmap viewer использует jsDelivr. Эти пробелы
надо закрывать отдельной задачей, а не скрывать внутри нового запуска.

## Что читать новой модели

В таком порядке:

1. этот summary;
2. [полный handoff spec](MODEL_HANDOFF_SPEC.md);
3. [AGENTS проекта](../../AGENTS.md) и
   [goal governance](../../../docs/governance/nri_goal_governance.md);
4. верхний текущий раздел [PROJECT_STATUS](../../PROJECT_STATUS.md);
5. [product boundary](../architecture/product_boundary.md) и
   [module contracts](../architecture/module_contracts.md);
6. [roadmap YAML](../roadmap/roadmap.yaml) и только затем точный plan/evidence
   выбранной lane.

Не надо начинать с последовательного чтения всего `PROJECT_STATUS.md` и тысяч
исторических receipts. Сначала определить текущую задачу и её exact predecessor.

## Критические предупреждения

- Не говорить ни «Gate 1 полностью завершён», ни «ничего в Gate 1 не принято».
- Не считать `ready`, `coverage`, `promotable` или высокий similarity
  эквивалентом `accepted` или `released`.
- Не утверждать, что все 20 страниц прошли fresh OCR: first-pass surface
  исторически смешивает fresh OCR, selected candidates и bridge records.
- Не переписывать старые reports, manifests, receipts и expected hashes, чтобы
  сделать тесты зелёными.
- Не запускать OCR, render, translation или proofread без новой bounded
  authorization с точными inputs/outputs/limits.
- Не использовать review crops как OCR-safe inputs без policy decision.
- Не считать `translator` текущей зависимостью или канонической спецификацией.
- Не переименовывать продукт в `Sorceforge`.
- Не коммитить runtime, caches, `node_modules`, browser profiles, временные
  логи или credentials.

## Рекомендуемая следующая задача

Сначала провести отдельный **read-only baseline debt and continuation audit**:

1. перечислить 12 падающих lineage assertions и один runtime-dependent test;
2. для каждого указать expected/actual hash, earliest mismatching predecessor и
   источник полномочий;
3. отделить historical supersession, line-ending identity и настоящий defect;
4. сопоставить их с текущими page/lane successor decisions;
5. спроектировать переносимый Tesseract runtime binding и Python dependency
   declaration;
6. предложить одну следующую bounded implementation task без запуска новой
   книги и без изменения evidence.

До отдельного решения пользователя новая модель должна заниматься аудитом и
спецификацией, а не продолжать OCR или объявлять pipeline production-ready.
