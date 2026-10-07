# Шпаргалка: Git

```bash
git status
git diff
git add .
git commit -m "Describe the change"
git log --oneline
git push
git pull
```

Создать repo:

```bash
git init -b main
```

Создать GitHub repo из текущей папки:

```bash
gh repo create NAME --private --source=. --remote=origin --push
```

Вопрос при любой путанице: **какие файлы изменены, какой commit сейчас HEAD, и есть ли незакоммиченные изменения?**
