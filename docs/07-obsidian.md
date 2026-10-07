# 7. Obsidian + private GitHub repo

Obsidian хранит заметки как обычные Markdown (`.md`) файлы. Это делает его особенно хорошим учебным проектом для Git.

Документация Obsidian: <https://help.obsidian.md/>

## Не строй “идеальную систему знаний”

Начни просто:

```text
University/
├── Inbox/
├── Courses/
│   ├── Logistics/
│   ├── Economics/
│   └── ...
├── Projects/
├── Sources/
└── Templates/
```

Папки можно изменить позже. Важно начать писать заметки.

## Первый private repo

Перейди в папку vault:

```bash
cd ~/University
```

Создай `.gitignore`:

```text
.DS_Store
.obsidian/workspace.json
.obsidian/workspaces.json
```

Затем:

```bash
git init -b main
git add .
git commit -m "Initial university vault"
gh repo create university-notes --private --source=. --remote=origin --push
```

**Repo должен быть private**, если в заметках есть личные данные, coursework, материалы с ограничениями или что-либо, что ты не хотел бы публиковать.

## Сначала manual, потом automation

Сделай несколько commits вручную. Научись видеть `git diff`.

Только потом решай, нужен ли Obsidian Git plugin для автоматических commits/push/pull:
<https://github.com/Vinzent03/obsidian-git>

## Это sync или backup?

GitHub даёт историю и удалённую копию текстовых файлов, но не заменяет полноценный backup всего Mac. Time Machine решает другую задачу.

## Практика

1. Создай заметку `Courses/Logistics/Week-01.md`.
2. Добавь три пункта.
3. Посмотри `git diff`.
4. Commit.
5. Push.
6. Открой GitHub и посмотри историю файла.

Теперь Git — не абстракция: ты только что сохранил историю своей реальной заметки.
