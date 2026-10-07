# 9. Python без курса программирования

## Перед началом

Ты уже прошёл Git/Skills и `$teach-me` работает. Python пока мог вообще не быть установлен — это нормально.

Цель — не “выучить Python”. Цель — понимать, что делает маленький script, уметь его запустить и обсуждать изменения с Codex.

## 1. Установи инструменты только сейчас

```bash
brew install uv ripgrep
brew install --cask visual-studio-code
```

Проверка:

```bash
uv --version
rg --version
```

`uv` может сам управлять подходящей Python version и project environment.

Документация:
<https://docs.astral.sh/uv/>

## Что нужно знать

- `.py` — text file с Python code;
- **interpreter** выполняет Python;
- **variable** хранит value;
- **function** — именованный кусок работы;
- **library/package** — готовый внешний code;
- **virtual environment** отделяет dependencies одного project от другого.

## 2. Создай первый project

```bash
cd ~/University/Projects
uv init first-python-project
cd first-python-project
pwd
```

Теперь открой именно эту folder в Codex.

## 3. Попроси `$teach-me`

```text
$teach-me Я не программист.
Покажи мне, какие files создал `uv init`, и объясни их роль.
Потом помоги запустить минимальный Python program.
Не добавляй лишние libraries.
```

Если позже работаешь с реальным CSV, попроси Codex сначала объяснить data и предложить очень маленький analysis.

Например library:

```bash
uv add pandas
```

Запуск script:

```bash
uv run python main.py
```

## Что считать успехом

Ты можешь открыть 20–40 строк простого Python и примерно объяснить:

- откуда приходят data;
- что вызывается;
- что script выдаёт;
- где изменить filename или parameter;
- как запустить его снова.

Этого достаточно для первой версии курса.
