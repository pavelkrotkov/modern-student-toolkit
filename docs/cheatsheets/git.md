# Шпаргалка: Git

## Скопировать существующий удалённый репозиторий

```bash
cd ~/University/Projects
git clone https://github.com/OWNER/REPO.git
cd REPO
git status
```

## Работа в существующем репозитории

```bash
git status
git diff
git add .
git commit -m "Describe the change"
git log --oneline
git push
git pull
```

## Создать новый локальный репозиторий

```bash
cd /path/to/project
git init -b main
```

## Создать закрытый репозиторий GitHub из текущей папки

```bash
gh repo create NAME --private --source=. --remote=origin --push
```

Если потерялся:

```bash
pwd
git status
```

Сначала разберись, **в какой папке ты находишься**, и только потом выполняй команды Git.
