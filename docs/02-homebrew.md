# 2. Homebrew и программы

Homebrew — **package manager**: один проверяемый способ устанавливать, обновлять и удалять большое количество программ.

Официальная документация: <https://docs.brew.sh/Installation>

## Установка

Используй команду с официальной страницы <https://brew.sh/>. После установки Terminal может попросить добавить Homebrew в `PATH`; выполни именно команды, которые он показывает.

Проверка:

```bash
brew --version
brew doctor
```

## Установить набор курса

Из корня этого репозитория:

```bash
brew bundle
```

`Brewfile` устанавливает:

### Основное

- `git` — история изменений;
- `gh` — GitHub из Terminal;
- `mole` — анализ/обслуживание Mac;
- ChatGPT;
- Codex CLI;
- CodexBar;
- ONLYOFFICE;
- Obsidian;
- Zotero;
- DeepL.

### Инструменты, которые пригодятся позже

- `uv` — Python и его зависимости;
- `ripgrep` (`rg`) — быстрый поиск по текстовым файлам;
- GitHub Desktop — визуальные commits/diffs;
- VS Code — удобный текстовый/кодовый редактор.

Проверенные Homebrew entries на 2026-10-07:

- <https://formulae.brew.sh/cask/chatgpt>
- <https://formulae.brew.sh/cask/codex>
- <https://formulae.brew.sh/cask/codexbar>
- <https://formulae.brew.sh/formula/mole>
- <https://formulae.brew.sh/formula/gh>
- <https://formulae.brew.sh/formula/uv>

## Как обновлять

Раз в несколько недель или перед важной работой:

```bash
brew update
brew outdated
brew upgrade
brew cleanup
```

Если Homebrew ведёт себя странно:

```bash
brew doctor
```

Homebrew сам периодически обновляет метаданные при командах установки/upgrade; не нужно ежедневно запускать `brew update` вручную.

## Brewfile = воспроизводимый Mac

Проверить, соответствует ли компьютер `Brewfile`:

```bash
brew bundle check
```

Установить всё недостающее:

```bash
brew bundle
```

Это первая встреча с полезной идеей **configuration as code**: список программ хранится в обычном текстовом файле и отслеживается Git.

Источник: <https://docs.brew.sh/Brew-Bundle-and-Brewfile>
