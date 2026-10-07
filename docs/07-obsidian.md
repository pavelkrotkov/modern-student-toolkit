# 7. Obsidian и отдельный закрытый репозиторий GitHub

## Перед началом

Ты уже понимаешь `repo`, `commit`, `diff`, `push` и создал `codex-practice`.

## Важная граница

Вся папка `~/University` **не должна быть одним большим репозиторием Git**.

Мы специально разделили:

```text
~/University/Notes/      # только заметки Obsidian
~/University/Projects/   # отдельные проекты и репозитории
~/University/Sources/    # файлы PDF и данные
~/University/Scratch/    # временные файлы
```

Так мы избегаем вложенных репозиториев и случайного смешивания исходных файлов курса с личными заметками.

## 1. Создай хранилище заметок Obsidian

Открой Obsidian → **Open folder as vault** и выбери:

```text
~/University/Notes
```

Внутри создай:

```text
Notes/
├── Inbox/
├── Courses/
│   ├── Logistics/
│   └── Economics/
├── Projects/
├── Sources/
└── Templates/
```

Папка `~/University/Notes` — это **хранилище заметок (vault)**. На схеме показано его содержимое.

Не пытайся сразу построить идеальную систему знаний. Просто начни писать заметки.

## 2. Создай репозиторий Git только для заметок

В Terminal выполни:

```bash
cd ~/University/Notes
pwd
git init -b main
```

`pwd` должен заканчиваться на `/University/Notes`.

Создай `.gitignore`. Самый простой способ:

```bash
printf ".DS_Store\n.obsidian/workspace.json\n.obsidian/workspaces.json\n" > .gitignore
```

Проверь:

```bash
cat .gitignore
git status
```

Затем:

```bash
git add .
git commit -m "Initial university notes"
gh repo create university-notes --private --source=. --remote=origin --push
```

Репозиторий должен быть **закрытым (private)**.

## 3. Первая настоящая заметка

Создай:

```text
Courses/Logistics/Week-01.md
```

Добавь несколько собственных пунктов.

В Terminal выполни:

```bash
cd ~/University/Notes
git diff
git status
git add .
git commit -m "Add logistics week 1 notes"
git push
```

Посмотри коммит на GitHub.

## 4. Сначала вручную, затем автоматизация

Сделай несколько коммитов вручную. Когда разберёшься с `git diff`, можно будет решить, нужен ли плагин Obsidian Git для автоматической синхронизации:

<https://github.com/Vinzent03/obsidian-git>

GitHub хранит удалённую историю изменений текстовых заметок, но не заменяет полноценное резервное копирование через Time Machine.

## Проверка результата

У тебя должны быть **три отдельные папки с независимыми репозиториями**:

```text
Projects/modern-student-toolkit   # курс
Projects/Codex-Practice           # упражнение
Notes                             # закрытый репозиторий заметок Obsidian
```

Вся папка `~/University` **не является** репозиторием Git.
