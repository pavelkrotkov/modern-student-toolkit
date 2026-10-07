# 7. Obsidian + отдельный private GitHub repo

## Перед началом

Ты уже понимаешь `repo`, `commit`, `diff`, `push` и создал `codex-practice`.

## Важная граница

`~/University` **не должен быть одним большим Git repo**.

Мы специально разделили:

```text
~/University/Notes/      # только Obsidian notes
~/University/Projects/   # отдельные projects/repos
~/University/Sources/    # PDFs/data
~/University/Scratch/    # временные файлы
```

Это предотвращает nested repositories и случайное смешивание course source с личными notes.

## 1. Создай Obsidian vault

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

Здесь внешний `Notes/` — это path `~/University/Notes`; показанная структура — содержимое vault.

Не строй сложную “идеальную knowledge system”. Начни писать notes.

## 2. Сделай Git repo только из vault

Terminal:

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

Repo должен быть **private**.

## 3. Первый реальный note

Создай:

```text
Courses/Logistics/Week-01.md
```

Добавь несколько собственных пунктов.

Terminal:

```bash
cd ~/University/Notes
git diff
git status
git add .
git commit -m "Add logistics week 1 notes"
git push
```

Посмотри commit на GitHub.

## 4. Manual сначала, automation потом

Сделай несколько commits руками. Только после того, как `git diff` стал понятным, решай, нужен ли Obsidian Git plugin:

<https://github.com/Vinzent03/obsidian-git>

GitHub — полезная remote history для text notes, но не полноценная замена Time Machine.

## Checkpoint

У тебя должны быть **три независимых repo/folder contexts**:

```text
Projects/modern-student-toolkit   # course
Projects/Codex-Practice           # practice
Notes                             # private Obsidian notes
```

`~/University` целиком Git repo **не является**.
