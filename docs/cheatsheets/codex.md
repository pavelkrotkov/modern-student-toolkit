# Шпаргалка: Codex

## Выбор режима

- объяснить / перевести / quiz → **Chat**;
- длинный finished research/deliverable → **Work**;
- local files / Terminal / Git / technical task → **Codex**.

## Model baseline

Если доступны:

1. GPT-6.1 Sol Medium — default;
2. Sol XHigh — сложная задача;
3. Astra Low/Medium — escalation.

Проверяй актуальность:
<https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex>

## Folder scope

Открывай минимальную нужную folder.

Перед изменениями:

```text
Пока ничего не меняй.
Покажи, какие files видишь, и объясни planned changes.
```

## `$teach-me`

Работает после установки в уроке 8:

```text
$teach-me <задача>
```

Если не установлен, используй обычный tutor prompt:

```text
Я хочу научиться, а не получить готовый ответ.
Сначала объясни цель и дай только первый шаг.
```

## Usage

Официальный account usage meter — главный источник. CodexBar удобен как menu-bar indicator.

Codex CLI `/status` нужен только если ты отдельно используешь CLI; для desktop курса CLI не является prerequisite.
