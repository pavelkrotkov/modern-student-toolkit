# 4. Codex: folders, browser и Computer Use

## Перед началом

- ChatGPT Desktop установлен;
- папка `~/University/Projects/Codex-Practice` создана в уроке 1;
- ты понимаешь `pwd`, `ls`, `cd`.

`$teach-me` пока не нужен.

## Главная идея

**Открыть папку в Codex** и **дать Computer Use** — разные вещи.

## 1. Открой practice folder в Codex

1. Открой ChatGPT Desktop.
2. Выбери **Codex**.
3. Начни новый chat.
4. Выбери действие **Open folder / Open local folder** и укажи:

```text
University → Projects → Codex-Practice
```

Текущий OpenAI guide подтверждает, что Codex desktop работает с local folders, repositories и terminals:
<https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex>

Если название кнопки изменилось, не угадывай: спроси обычный Chat и приложи screenshot.

## 2. Сначала inspection без изменений

Отправь Codex:

```text
Я учусь работать с folders.
Пока ничего не меняй.
Покажи, какие файлы видишь в открытой папке,
и объясни, что означает working directory.
```

Сравни список с Finder.

## 3. Одно контролируемое изменение

```text
Предложи создать внутри этой папки directory `archive`.
Сначала объясни, что именно изменится.
Не перемещай другие файлы без моего подтверждения.
```

После создания проверь изменение в Finder.

## 4. Почему scope важен

Для упражнения Codex нужна только `Codex-Practice`.

Не открывай `~` или весь диск “на всякий случай”. Smaller scope:

- проще понять;
- проще проверить;
- уменьшает случайные изменения;
- лучше объясняет агенту, с каким project он работает.

## 5. Direct files/Terminal обычно лучше GUI

Если задачу можно выполнить напрямую с files или command, обычно это прозрачнее, чем визуально кликать по окнам.

Позже, после установки `ripgrep`, поиск по Markdown может выглядеть так:

```bash
rg "economics" ~/University/Notes
```

Пока эту command запускать не нужно.

## 6. Built-in browser

Browser нужен, когда работа действительно живёт на website.

В Work или Codex открой встроенный browser через toolbar или:

```text
Command+Shift+B
```

OpenAI guide:
<https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app>

## 7. Computer Use

Computer Use нужен, когда агент должен **видеть и управлять GUI application**: нажимать кнопки, вводить текст, открывать settings.

Пример:

```text
Помоги мне найти в Obsidian settings раздел Community plugins.
Ничего не устанавливай без моего подтверждения.
```

Предпочтительный порядок:

1. direct file/API;
2. Terminal/command;
3. browser;
4. Computer Use.

## 8. Record & Replay — позже

На eligible macOS accounts Codex может записать показанный GUI workflow и превратить его в reusable skill. Пока просто знай, что такая возможность существует.

Справка:
<https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan>

## Checkpoint

Ты должен уметь:

- открыть только `Codex-Practice`;
- попросить Codex сначала inspect, а не edit;
- объяснить разницу между folder access и Computer Use.
