# 2. Homebrew и установка программ

## Перед началом

Ты уже умеешь:

- открыть Terminal;
- выполнить `pwd`, `ls`, `cd`;
- перейти в `~/University`.

Локальная копия репозитория курса **ещё не нужна**.

## Что такое Homebrew

Homebrew — **менеджер пакетов (package manager)**: программа, с помощью которой можно устанавливать и обновлять другие программы из Terminal.

Официальный сайт: <https://brew.sh/>

## 1. Установи Homebrew

Открой <https://brew.sh/> в браузере.

На главной странице есть команда установки. **Скопируй её именно с официального сайта**, вставь в Terminal и нажми Enter.

Во время установки macOS может:

- попросить пароль для входа на Mac;
- предложить установить Apple Command Line Tools;
- попросить нажать Enter для продолжения.

Это нормально.

В конце установщик Homebrew может показать раздел **Next steps** с командами для настройки переменной `PATH`. Выполни эти команды **точно так, как их показал установщик**.

Проверка:

```bash
brew --version
```

Если появилась строка с номером версии, Homebrew работает.

## 2. Установи основные инструменты командной строки

```bash
brew install git gh mole
```

Проверка:

```bash
git --version
gh --version
mo --version
```

Если одна из проверок не удалась, открой [«Если застрял»](help.md) и отправь точный вывод Terminal.

## 3. Установи основные приложения

```bash
brew install --cask chatgpt codexbar onlyoffice obsidian zotero deepl github
```

Здесь:

- `chatgpt` — приложение ChatGPT для Mac с режимами Chat, Work и Codex;
- `codexbar` — индикатор расхода лимита в строке меню;
- `onlyoffice` — документы/таблицы/презентации;
- `obsidian` — заметки в формате Markdown;
- `zotero` — источники и библиографические ссылки;
- `deepl` — быстрый перевод;
- `github` — GitHub Desktop.

Официальная страница загрузки ChatGPT:
<https://chatgpt.com/download/>

## 4. Открой ChatGPT для Mac

Через Finder → Applications открой **ChatGPT** и войди в ту же учётную запись.

В текущей версии приложения для Mac режимы Chat, Work и Codex доступны в одной программе:
<https://help.openai.com/en/articles/9275200-downloading-the-chatgpt-macos-app>

## 5. Mole: сначала только анализ

```bash
mo analyze
```

Не удаляй ничего только потому, что Mole обнаружил временные файлы.

Если позднее понадобится очистка:

```bash
mo clean --dry-run
```

`--dry-run` сначала показывает план без удаления.

Mole: <https://github.com/tw93/Mole>

## Что пока НЕ делать

Не запускай `brew bundle`. `Brewfile` находится в репозитории курса, который мы сознательно **пока не клонировали**. К Brewfile вернёмся после Git-урока.

Не устанавливай Python и VS Code только потому, что они упомянуты в программе курса. Они появятся тогда, когда будут нужны.

## Как обновлять установленное

Раз в несколько недель:

```bash
brew update
brew outdated
brew upgrade
brew cleanup
```

При проблемах:

```bash
brew doctor
```

## Проверка результата

Перед уроком 3:

- [ ] `brew --version` работает;
- [ ] `git --version` работает;
- [ ] `gh --version` работает;
- [ ] `mo analyze` запускается;
- [ ] приложение ChatGPT открывается;
- [ ] в ChatGPT ты можешь выбрать Chat, Work и Codex.
