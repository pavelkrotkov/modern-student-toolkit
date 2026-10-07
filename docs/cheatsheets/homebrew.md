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

## Reference Brewfile этого курса

Только после урока Git, когда course repo уже клонирован:

```bash
brew bundle check --file ~/University/Projects/modern-student-toolkit/Brewfile
```

`brew bundle` без `--file` ищет Brewfile относительно current directory, поэтому beginner course не должен полагаться на него “из неизвестной папки”.

Справка:
<https://docs.brew.sh/>
