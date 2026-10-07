# 3. Chat, Work и Codex

> Проверено: **2026-10-07**. Названия и limits могут меняться; первичные ссылки даны ниже.

## Перед началом

Установлен новый ChatGPT Desktop и выполнен вход в account.

## Сначала научись выбирать режим

| Задача | Режим |
|---|---|
| объяснить, перевести, обсудить, проверить понимание | **Chat** |
| выполнить длинную многошаговую работу и выдать finished deliverable | **Work** |
| работать с локальными folders, files, Terminal, Git или technical project | **Codex** |

В desktop app выбери **ChatGPT** или **Codex** сверху слева. В ChatGPT переключай **Chat / Work**.

Текущая справка:
<https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex>

## Простое правило расхода allowance

Если задачу можно решить разговором — используй **Chat**.

Не открывай Codex только чтобы спросить “что означает `git clone`?”. Для объяснения Chat проще и обычно экономнее.

## Models в Work/Codex

Если в твоём account доступны эти варианты, baseline курса:

1. **GPT-6.1 Sol — Medium**: обычный default.
2. **GPT-6.1 Sol — XHigh**: сложная задача, где качество важнее расхода.
3. **GPT-6 Astra — Low/Medium**: escalation, если задача действительно сложна или Sol застрял.

Не повышай reasoning effort автоматически.

Актуальная справка:
<https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex>

## Usage limits

Не представляй allowance как фиксированное “N prompts”. Расход зависит от model, reasoning, context и длительности agent work.

Проверяй:

- официальный usage meter в ChatGPT;
- CodexBar в macOS menu bar;
- если позже начнёшь использовать Codex CLI — `/status`.

Codex/plan guide:
<https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan>

## CodexBar

Ты установил его в уроке 2. Открой CodexBar из Applications, разреши запуск, если macOS спросит, и оставь иконку в menu bar.

CodexBar — удобный индикатор; если цифры расходятся с официальным OpenAI usage meter, ориентируйся на OpenAI.

Проект:
<https://github.com/steipete/CodexBar>

## Первый tutor prompt

`$teach-me` пока **не установлен**. Используй обычный prompt:

```text
Я не программист. Объясняй по-русски, но сохраняй важные English technical terms.
Не делай практическое упражнение полностью за меня.
Сначала объясни цель, затем дай один следующий шаг.
```

Мы превратим этот pattern в настоящий reusable skill в уроке 8.

## Мини-упражнение

Определи режим:

1. “Переведи и объясни абзац лекции.”
2. “Исследуй пять shipping companies и сделай sourced comparison.”
3. “Работай с файлами в моей practice folder и покажи, что изменилось.”

Ответ: **Chat → Work → Codex**.

## Checkpoint

Ты должен уметь открыть каждый из трёх режимов и своими словами объяснить, зачем нужен каждый.
