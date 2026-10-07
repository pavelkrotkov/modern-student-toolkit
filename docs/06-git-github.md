# 6. Git и GitHub: сначала clone, потом свой repo

## Перед началом

Установлены `git`, `gh` и GitHub Desktop. Ты умеешь перейти в `~/University/Projects`.

До этого урока курс **не требовал локальной копии самого себя**.

## Что такое Git и GitHub

- **Git** хранит историю изменений в folders.
- **GitHub** хранит repositories на server и даёт web interface.
- **remote repository** — repo на GitHub.
- **local repository** — его копия на твоём Mac.
- **clone** — создать local copy существующего remote repo.

## 1. Первый `git clone`: скачай этот курс

В Terminal:

```bash
cd ~/University/Projects
pwd
```

Убедись, что output заканчивается на:

```text
/University/Projects
```

Теперь:

```bash
git clone https://github.com/pavelkrotkov/modern-student-toolkit.git
```

Git должен создать:

```text
~/University/Projects/modern-student-toolkit
```

Перейди туда:

```bash
cd ~/University/Projects/modern-student-toolkit
pwd
git status
```

Теперь впервые имеет смысл выражение **root of the repository**: это папка `modern-student-toolkit`, внутри которой находятся `README.md`, `docs/`, `Brewfile` и `.git`.

Посмотри:

```bash
ls
```

Официальный GitHub guide:
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>

## 2. Почему clone был первым Git-упражнением

Ты уже видел этот course как website. Теперь у тебя появилась **local copy его source files**.

Это связывает три идеи:

```text
GitHub remote repo → git clone → local folder on your Mac
```

Пока ничего в course repo не редактируй и не push.

## 3. Проверь Brewfile — теперь path существует

Раньше команда была бы непонятной. Теперь можно безопасно проверить:

```bash
brew bundle check --file ~/University/Projects/modern-student-toolkit/Brewfile
```

Она только сообщает, какие entries из reference `Brewfile` установлены. Она не нужна для ежедневной работы.

## 4. GitHub account и CLI

Если GitHub account ещё нет, создай его на <https://github.com/> и включи 2FA.

Затем:

```bash
gh auth login
```

Выбирай GitHub.com и browser/HTTPS flow, если CLI предлагает варианты.

Student benefits:
<https://github.com/education/students>

## 5. Пять понятий

- **repository** — folder с Git history;
- **commit** — named snapshot;
- **diff** — что изменилось;
- **branch** — отдельная линия history;
- **push / pull** — отправить commits / получить новые commits.

## 6. Создай свой маленький practice repo

Не используй course repo. Работай с созданной раньше папкой:

```bash
cd ~/University/Projects/Codex-Practice
git init -b main
git status
git add .
git commit -m "Initial practice files"
git log --oneline
```

Теперь опубликуй **private** repo:

```bash
gh repo create codex-practice --private --source=. --remote=origin --push
```

Открой GitHub.com и найди `codex-practice`.

## 7. Увидь diff

Измени один `.txt` file в Finder или text editor.

```bash
cd ~/University/Projects/Codex-Practice
git status
git diff
```

Посмотри то же изменение в GitHub Desktop.

Затем:

```bash
git add .
git commit -m "Update practice note"
git push
```

## Что пока не нужно

Не учи `rebase`, `cherry-pick`, `bisect`, submodules или сложные merge strategies.

MIT companion:
<https://missing.csail.mit.edu/2026/version-control/>

## Checkpoint

Ты должен своими словами объяснить цепочку:

**GitHub repo → clone → local folder → change → diff → commit → push**.

И на Mac должны существовать два разных repo:

```text
~/University/Projects/modern-student-toolkit   # public course, cloned
~/University/Projects/Codex-Practice           # твой private practice repo
```
