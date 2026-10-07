# 5. MIT Missing Semester 2026

## Перед началом

Ты умеешь пользоваться Chat для объяснений и умеешь открыть безопасную practice folder в Codex.

Custom `$teach-me` skill появится позже; здесь он **не требуется**.

[The Missing Semester of Your CS Education](https://missing.csail.mit.edu/2026/) — backbone технической части курса. Проходить все девять лекций подряд не нужно.

## Что проходить сейчас

| MIT lecture | Что взять |
|---|---|
| Course Overview + Introduction to the Shell | shell, paths, basic commands, pipes |
| Command-line Environment | выборочно: environment, help, useful shell habits |
| Development Environment and Tools | editors/tools, AI context |
| Version Control and Git | после нашего Git-урока |
| Agentic Coding | после Git и Skills |

Главная страница:
<https://missing.csail.mit.edu/2026/>

## Английский: не переводить всё заранее

Цель — понимать материал **и одновременно узнавать English technical vocabulary**.

Перед лекцией открой Chat:

```text
Я собираюсь смотреть MIT Missing Semester:
<URL>

Я лучше понимаю русский, чем английский.
Дай 5-минутное введение по-русски.
Сохраняй важные English technical terms в скобках.
Дай 10 слов, которые мне важно узнавать на слух.
```

Во время:

```text
Объясни этот абзац по-русски простыми словами.
Commands, filenames и technical terms не переводи; объясни их отдельно.
```

После:

```text
Проверь, понял ли я материал.
Задавай по одному вопросу и не показывай ответ, пока я не попробую.
```

## Codex для упражнения — без custom skill

Если упражнение требует Terminal/files, открой отдельную folder, например:

```text
~/University/Projects/Missing-Semester-Practice
```

Если folder ещё нет:

```bash
mkdir -p ~/University/Projects/Missing-Semester-Practice
```

Открой её в Codex и напиши:

```text
Я делаю упражнение из MIT Missing Semester и хочу научиться, а не получить готовый ответ.
Сначала объясни, чему упражнение должно меня научить.
Потом дай только первый безопасный шаг или одну подсказку.
```

В уроке 8 этот повторяющийся prompt станет `$teach-me`.

## DeepL

DeepL уже установлен и удобен для буквального перевода небольших passages. Для обучения Chat часто полезнее, потому что может объяснить context.

## Checkpoint

После первой MIT shell lecture ты должен узнавать:

`path`, `working directory`, `shell`, `command`, `argument`, `pipe`.

Не обязан помнить все команды из лекции.
