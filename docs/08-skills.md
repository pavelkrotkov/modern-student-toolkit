# 8. Skills и `$teach-me`

Skill — reusable workflow: набор инструкций и ресурсов, которые агент может применять повторно.

OpenAI описывает skill как папку с обязательным `SKILL.md`, где есть `name`, `description` и инструкции:
<https://developers.openai.com/plugins/concepts/skills>

## `$teach-me`

В этом repo уже есть:

```text
skills/teach-me/SKILL.md
```

Его задача — заставить Codex **обучать**, а не просто мгновенно выполнять упражнение.

Ключевые правила:

- объяснять по-русски;
- сохранять English technical terms;
- команды и код никогда не переводить;
- давать минимум теории перед действием;
- позволять ученику выполнить простой шаг самому;
- сначала hint, потом полный ответ;
- destructive actions сначала preview;
- завершать коротким recap и самостоятельным заданием.

## Как вызывать

Когда skill установлен/доступен в Codex:

```text
$teach-me Помоги мне понять git status и git diff на этой папке.
```

В Codex built-in skill creator вызывается как:

```text
$skill-creator
```

OpenAI example: <https://developers.openai.com/blog/eval-skills>

## Хорошие первые собственные skills

Не делай десятки. Достаточно одного-двух реальных повторяемых процессов.

Например:

- `$lecture-prep` — подготовить bilingual vocabulary и вопросы перед лекцией;
- `$course-review` — по заметкам недели сделать quiz и список непонятных мест.

## Плохой skill

Огромный универсальный prompt на десять страниц, который пытается управлять всем Codex сразу.

Skills полезны именно для **конкретного повторяемого workflow**.

Дополнительный актуальный материал OpenAI:
<https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra>
