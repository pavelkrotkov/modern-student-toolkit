# 8. Skills и `$teach-me`

## Перед началом

Course repo уже клонирован сюда:

```text
~/University/Projects/modern-student-toolkit
```

Ты понимаешь, что такое path и local repo.

## Что такое skill

Skill — reusable workflow: небольшая папка с `SKILL.md`, которую Codex может использовать как повторяемую инструкцию.

OpenAI:
<https://developers.openai.com/plugins/concepts/skills>

## 1. Посмотри source `$teach-me`

Source skill лежит в уже клонированном course repo:

```text
~/University/Projects/modern-student-toolkit/skills/teach-me/SKILL.md
```

Посмотри его без изменения:

```bash
cat ~/University/Projects/modern-student-toolkit/skills/teach-me/SKILL.md
```

Это обычный Markdown file.

## 2. Установи skill для своего user account

Codex поддерживает user-scoped skills в `~/.codex/skills/`.

Создай destination:

```bash
mkdir -p ~/.codex/skills/teach-me
```

Скопируй один file:

```bash
cp ~/University/Projects/modern-student-toolkit/skills/teach-me/SKILL.md \
  ~/.codex/skills/teach-me/SKILL.md
```

Посмотри, что получилось:

```bash
cat ~/.codex/skills/teach-me/SKILL.md
```

Закрой и снова открой ChatGPT Desktop/Codex, чтобы новый skill точно обнаружился.

OpenAI example user-scoped path:
<https://developers.openai.com/blog/eval-skills>

## 3. Первый вызов

Открой в Codex `~/University/Projects/Codex-Practice` и напиши:

```text
$teach-me Помоги мне понять git status и git diff в этой папке.
```

Если Codex не узнаёт `$teach-me`, открой [«Если застрял»](help.md) и приложи:

```bash
ls -la ~/.codex/skills/teach-me
cat ~/.codex/skills/teach-me/SKILL.md
```

## 4. Зачем мы ждали до урока 8

До Git-урока локального `modern-student-toolkit` не существовало. Поэтому ссылка вида:

```text
skills/teach-me/SKILL.md
```

раньше была бы скрытым prerequisite.

Теперь ты понимаешь весь путь:

```text
GitHub remote course
→ git clone
→ local course repo
→ SKILL.md
→ ~/.codex/skills/teach-me/
→ $teach-me
```

## 5. Создание собственных skills — только после использования готового

Built-in creator:

```text
$skill-creator
```

OpenAI:
<https://developers.openai.com/plugins/build/skills>

Хорошие идеи позже:

- `$lecture-prep`;
- `$course-review`.

Не создавай десятки skills заранее.

## Checkpoint

`$teach-me` должен сработать в **другой** folder, например `Codex-Practice`, а не только в course repo. Это подтверждает, что skill установлен user-scoped.
