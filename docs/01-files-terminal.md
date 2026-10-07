# 1. Finder, файлы, папки и Terminal

## Перед началом

Должен быть пройден урок 0. В `~/University` уже существуют:

`Notes`, `Projects`, `Sources`, `Scratch`.

Git и Homebrew всё ещё не нужны.

## Finder и Terminal показывают одну систему

Finder — графический способ видеть файлы. Terminal — текстовый способ работать с теми же файлами.

Ключевые термины:

- **folder / directory** — папка;
- **path** — адрес файла или папки;
- **working directory** — папка, относительно которой Terminal сейчас выполняет команды;
- `~` — твоя home folder;
- `..` — parent directory.

## 1. Открой Terminal

Нажми **Command+Space**, введи `Terminal`, нажми Enter.

Появится окно с приглашением командной строки. Ничего опасного от самого открытия Terminal не происходит.

## 2. Узнай, где ты находишься

Введи:

```bash
pwd
```

На Mac ответ обычно заканчивается именем твоего user account. `pwd` означает **print working directory**.

Теперь:

```bash
ls
```

В списке должна быть папка `University`.

## 3. Перейди в University

```bash
cd ~/University
pwd
ls
```

После `pwd` path должен заканчиваться на `/University`.

После `ls` должны быть видны:

```text
Notes
Projects
Scratch
Sources
```

`cd` означает **change directory**.

## 4. Убедись, что Finder и Terminal видят одно и то же

```bash
open .
```

Точка `.` означает **current directory**. Finder должен открыть именно `University`.

## 5. Создай безопасную practice folder

```bash
cd ~/University/Projects
mkdir Codex-Practice
cd Codex-Practice
pwd
open .
```

В Finder создай внутри `Codex-Practice` три обычных text files, например:

```text
one.txt
two.txt
old.txt
```

Вернись в Terminal:

```bash
ls
```

Ты должен увидеть те же три файла.

## Пока достаточно шести команд

```bash
pwd
ls
cd
mkdir
open .
cat
```

`cat FILE` позже позволит показать содержимое простого text file.

## MIT companion — только после практики выше

2026 Course Overview + Introduction to the Shell:

<https://missing.csail.mit.edu/2026/course-shell/>

Не пытайся освоить лекцию целиком. Пока нужны paths, `pwd`, `ls`, `cd` и идея working directory.

## Checkpoint

Без подсказки ответь:

1. Что показывает `pwd`?
2. Что означает `~`?
3. Чем Finder отличается от Terminal в этом упражнении?
4. Как открыть текущую Terminal-папку в Finder?

Если ответы неясны, попроси Chat объяснить их по-русски и повтори шаги 2–4.
