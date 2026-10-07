# Шпаргалка: Homebrew

```bash
brew search NAME
brew info NAME
brew install NAME
brew install --cask APP
brew uninstall NAME
brew update
brew outdated
brew upgrade
brew cleanup
brew doctor
```

## Образец Brewfile из курса

Только после урока Git, когда ты уже скачал репозиторий курса:

```bash
brew bundle check --file ~/University/Projects/modern-student-toolkit/Brewfile
```

Без параметра `--file` команда `brew bundle` ищет Brewfile в текущей директории. Поэтому курс не предлагает запускать её из неизвестной папки.

Справка:
<https://docs.brew.sh/>
