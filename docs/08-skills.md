# 8. Навыки Codex (Skills) и `$teach-me`

## Перед началом

Репозиторий курса уже скопирован сюда:

```text
~/University/Projects/modern-student-toolkit
```

Ты понимаешь, что такое путь и локальный репозиторий.

## Что такое навык Codex

**Навык (skill)** — набор повторно используемых инструкций в папке с файлом `SKILL.md`. Codex может следовать им при выполнении подходящих задач.

OpenAI:
<https://developers.openai.com/plugins/concepts/skills>

## 1. Посмотри исходный файл `$teach-me`

Файл навыка находится в уже скопированном репозитории курса:

```text
~/University/Projects/modern-student-toolkit/skills/teach-me/SKILL.md
```

Посмотри его без изменения:

```bash
cat ~/University/Projects/modern-student-toolkit/skills/teach-me/SKILL.md
```

Это обычный файл в формате Markdown.

## 2. Установи навык для своей учётной записи

Codex поддерживает личные навыки в папке `~/.codex/skills/`.

Создай папку назначения:

```bash
mkdir -p ~/.codex/skills/teach-me
```

Скопируй файл:

```bash
cp ~/University/Projects/modern-student-toolkit/skills/teach-me/SKILL.md \
  ~/.codex/skills/teach-me/SKILL.md
```

Посмотри, что получилось:

```bash
cat ~/.codex/skills/teach-me/SKILL.md
```

Закрой и снова открой приложение ChatGPT, затем перейди в Codex: программа должна обнаружить новый навык.

Пример расположения личного навыка в документации OpenAI:
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

раньше ссылалась бы на файл, которого ещё не было на компьютере.

Теперь ты понимаешь весь путь:

```text
удалённый репозиторий курса на GitHub
→ git clone
→ локальная копия курса
→ SKILL.md
→ ~/.codex/skills/teach-me/
→ $teach-me
```

## 5. Создавай собственные навыки только после знакомства с готовым

Встроенная команда для создания навыков:

```text
$skill-creator
```

OpenAI:
<https://developers.openai.com/plugins/build/skills>

Хорошие идеи позже:

- `$lecture-prep`;
- `$course-review`.

Не создавай десятки навыков без необходимости.

## Проверка результата

`$teach-me` должен работать и в **другой** папке, например `Codex-Practice`, а не только в репозитории курса. Это подтверждает, что навык доступен для разных проектов.
