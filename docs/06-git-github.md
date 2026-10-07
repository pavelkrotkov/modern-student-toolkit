# 6. Git и GitHub — только нужное

Git — не GitHub.

- **Git** хранит историю изменений в папке.
- **GitHub** хранит удалённую копию repository и даёт веб-интерфейс, sharing и collaboration.

## Пять понятий

**repository (repo)** — папка, историю которой отслеживает Git.

**commit** — именованный snapshot изменений.

**diff** — что именно изменилось.

**branch** — отдельная линия изменений.

**push/pull** — отправить изменения на GitHub / получить их обратно.

Для начала этого достаточно.

## Первая локальная история

```bash
cd ~/University/Codex-Practice
git init -b main
git status
git add .
git commit -m "Initial practice files"
git log --oneline
```

Не заучивай команды. После каждой спроси себя: **какой snapshot или состояние я сейчас изменил?**

## GitHub CLI

Войти:

```bash
gh auth login
```

Создать private repo из текущей папки:

```bash
gh repo create codex-practice --private --source=. --remote=origin --push
```

## GitHub Desktop

Используй его как визуальный способ увидеть:

- changed files;
- diff;
- commit history;
- branch.

Terminal всё ещё нужен, но GUI помогает сформировать правильную картину.

## Что не нужно пока

Не надо учить:

- rebase;
- cherry-pick;
- bisect;
- submodules;
- сложные merge strategies.

## MIT companion

<https://missing.csail.mit.edu/2026/version-control/>

MIT объясняет модель Git глубже, чем нужно для этого курса. Пойми snapshots/commits/references; advanced exercises оставь на потом.

## GitHub Education

Если университет подходит под eligibility, оформи student benefits:
<https://github.com/education/students>

## Мини-упражнение

Измени один `.txt` файл и выполни:

```bash
git status
git diff
git add .
git commit -m "Update practice note"
git push
```

Посмотри тот же commit на GitHub.com и в GitHub Desktop.
