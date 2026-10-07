# 3. Chat, Work и Codex

> Проверено: **2026-10-07**. Этот раздел быстро меняется; сверяйся с актуальными страницами OpenAI.

## Простая модель

| Задача | Режим |
|---|---|
| объяснить, перевести, обсудить, проверить понимание | **Chat** |
| выполнить длинную многошаговую работу и выдать законченный результат | **Work** |
| работать с папкой, файлами, Terminal, Git, небольшими техническими проектами | **Codex** |

OpenAI формулирует это почти так же: Chat — conversational help, Work — longer multi-step work and deliverables, Codex — technical/software work.

Источник: <https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex>

## Как не расходовать агентный лимит зря

Если задача решается разговором, переводом или объяснением — оставайся в **Chat**.

Work и Codex используют общую структуру agentic usage/credits на планах, где она применяется. Поэтому нет смысла запускать Codex только чтобы спросить: “что такое Git branch?”.

Для такой задачи Chat лучше:

> Объясни мне по-русски, что такое Git branch. Оставь английские технические термины в скобках и дай один бытовой пример.

## Какую модель выбирать в Work/Codex

Если в твоём account доступен **GPT-6.1 Sol**:

1. **GPT-6.1 Sol — Medium**: обычный default. Хороший баланс качества, скорости и allowance.
2. **GPT-6.1 Sol — XHigh**: сложная задача, где важнее качество, чем расход.
3. **GPT-6 Astra — Low/Medium**: escalation, если задача реально сложная или Sol застрял.

Не повышай reasoning просто “на всякий случай”. OpenAI прямо отмечает, что higher effort расходует больше allowance и не гарантирует лучший результат.

Текущая справка:
<https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex>

Модели в Work/Codex:
<https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex>

## Лимиты и как их смотреть

Не думай о Codex как о “N сообщений в неделю”. Расход зависит от:

- модели;
- reasoning effort;
- длины контекста;
- размера output;
- инструментов и длительности agent task;
- local/cloud execution;
- speed mode.

Проверяй реальный account meter:

- ChatGPT Desktop → **Settings → Usage** (название раздела может меняться);
- в Codex CLI: `/status`;
- CodexBar в menu bar.

OpenAI usage guide:
<https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan>

## CodexBar

Установка уже включена в `Brewfile` или отдельно:

```bash
brew install --cask codexbar
```

Проект: <https://github.com/steipete/CodexBar>

CodexBar показывает usage windows и reset times, если источник/аккаунт предоставляет эти данные. Это удобный индикатор, но при расхождении ориентируйся на официальный usage meter OpenAI.

## Мини-упражнение

Для трёх задач выбери режим до того, как открывать ChatGPT:

1. “Переведи абзац лекции и объясни термин.”
2. “Исследуй пять компаний и сделай таблицу сравнения с источниками.”
3. “В этой папке переименуй файлы по понятной схеме и покажи diff.”

Ответ: Chat → Work → Codex.
