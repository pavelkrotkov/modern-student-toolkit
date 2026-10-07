# Шпаргалка: Git

## Скопировать существующий remote repo

```bash
cd ~/University/Projects
git clone https://github.com/OWNER/REPO.git
cd REPO
git status
```

## Обычная работа в уже существующем repo

```bash
git status
git diff
git add .
git commit -m "Describe the change"
git log --oneline
git push
git pull
```

## Создать новый local repo

```bash
cd /path/to/project
git init -b main
```

## Создать private GitHub repo из current folder

```bash
gh repo create NAME --private --source=. --remote=origin --push
```

Если потерялся:

```bash
pwd
git status
```

Сначала пойми **в какой folder ты находишься**, затем уже думай про Git.
