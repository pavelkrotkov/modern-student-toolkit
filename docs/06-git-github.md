# 6. Git и GitHub: сначала копия готового проекта, потом свой репозиторий

## Перед началом

Установлены `git`, `gh` и GitHub Desktop. Ты умеешь перейти в `~/University/Projects`.

До этого урока курс **не требовал локальной копии самого себя**.

## Что такое Git и GitHub

- **Git** хранит историю изменений в папках.
- **GitHub** хранит репозитории на сервере и позволяет работать с ними через сайт.
- **удалённый репозиторий (remote repository)** — репозиторий на GitHub.
- **локальный репозиторий (local repository)** — копия на твоём Mac.
- **клонирование (clone)** — получение локальной копии существующего удалённого репозитория.

## 1. Первый `git clone`: скачай этот курс

В Terminal:

```bash
cd ~/University/Projects
pwd
```

Убедись, что выведенный путь заканчивается на:

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

Теперь можно объяснить, что такое **корень репозитория (repository root)**: это папка `modern-student-toolkit`, внутри которой находятся `README.md`, `docs/`, `Brewfile` и `.git`.

Посмотри:

```bash
ls
```

Официальная инструкция GitHub:
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>

## 2. Зачем мы начали с клонирования

Раньше ты открывал курс как сайт. Теперь у тебя есть **локальная копия исходных файлов курса**.

Это связывает три идеи:

```text
удалённый репозиторий GitHub → git clone → локальная папка на твоём Mac
```

Пока не редактируй файлы курса и не отправляй изменения на GitHub.

## 3. Проверь Brewfile — теперь файл есть на Mac

Раньше команда была бы непонятной. Теперь можно безопасно проверить:

```bash
brew bundle check --file ~/University/Projects/modern-student-toolkit/Brewfile
```

Она только сообщает, какие программы из образца `Brewfile` уже установлены. Она не нужна для ежедневной работы.

## 4. Учётная запись GitHub и командная строка

Если учётной записи GitHub ещё нет, создай её на <https://github.com/> и включи 2FA.

Затем:

```bash
gh auth login
```

Если программа предлагает варианты, выбери GitHub.com и вход через браузер по HTTPS.

Льготы для студентов:
<https://github.com/education/students>

## 5. Пять понятий

- **репозиторий (repository)** — папка, историю изменений в которой хранит Git;
- **коммит (commit)** — сохранённое состояние файлов с пояснением;
- **разница между версиями (diff)** — какие строки изменились;
- **ветка (branch)** — отдельная линия развития проекта;
- **отправка и получение изменений (push / pull)** — обмен коммитами с удалённым репозиторием.

## 6. Создай свой маленький учебный репозиторий

Не изменяй репозиторий курса. Работай с папкой, созданной в первом уроке:

```bash
cd ~/University/Projects/Codex-Practice
git init -b main
git status
git add .
git commit -m "Initial practice files"
git log --oneline
```

Теперь создай **закрытый** репозиторий на GitHub:

```bash
gh repo create codex-practice --private --source=. --remote=origin --push
```

Открой GitHub.com и найди `codex-practice`.

## 7. Посмотри разницу между версиями

Измени один файл `.txt` в Finder или текстовом редакторе.

```bash
cd ~/University/Projects/Codex-Practice
git status
git diff
```

Посмотри те же изменения в приложении GitHub Desktop.

Затем:

```bash
git add .
git commit -m "Update practice note"
git push
```

## Что пока не нужно

Пока не изучай `rebase`, `cherry-pick`, `bisect`, подмодули и сложные способы объединения веток.

Дополнительная лекция MIT:
<https://missing.csail.mit.edu/2026/version-control/>

## Проверка результата

Ты должен своими словами объяснить цепочку:

**репозиторий GitHub → клонирование → локальная папка → изменение → просмотр разницы → коммит → отправка изменений**.

На Mac должны существовать два отдельных репозитория:

```text
~/University/Projects/modern-student-toolkit   # открытая копия курса
~/University/Projects/Codex-Practice           # твой закрытый учебный репозиторий
```
