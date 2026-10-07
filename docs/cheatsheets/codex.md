# Шпаргалка: Codex

## Выбор режима

- объяснить / перевести / quiz → **Chat**;
- длинный законченный research/deliverable → **Work**;
- files / Terminal / Git / technical task → **Codex**.

## Model baseline

Если доступен GPT-6.1 Sol:

1. Sol Medium — default;
2. Sol XHigh — сложная задача;
3. Astra Low/Medium — escalation.

Проверяй актуальность:
<https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex>

## Usage

Codex CLI:

```text
/status
```

Menu bar: CodexBar.

## Project instructions

```text
/init
```

создаёт scaffold `AGENTS.md` для текущего project (если команда доступна в твоём client/version).

## Tutor

```text
$teach-me <задача>
```

## Доступ

Открывай минимальную нужную папку. Не давай агенту весь home directory без причины.
