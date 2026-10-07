# 2. Homebrew и установка программ

## Перед началом

Ты уже умеешь:

- открыть Terminal;
- выполнить `pwd`, `ls`, `cd`;
- перейти в `~/University`.

Локальная копия этого course repo **ещё не нужна**.

## Что такое Homebrew

Homebrew — **package manager**: единый способ устанавливать и обновлять много Mac-программ из Terminal.

Официальный сайт: <https://brew.sh/>

## 1. Установи Homebrew

Открой <https://brew.sh/> в browser.

На главной странице есть одна install command. **Копируй её именно с официального сайта**, вставь в Terminal и нажми Enter.

Во время установки macOS может:

- попросить твой Mac password;
- предложить установить Apple Command Line Tools;
- попросить нажать Enter для продолжения.

Это нормально.

В конце Homebrew может показать блок **Next steps** и команды для добавления Homebrew в `PATH`. Выполни эти команды **точно такими, как их показал installer**.

Проверка:

```bash
brew --version
```

Если видишь version number — Homebrew работает.

## 2. Установи базовые command-line tools

```bash
brew install git gh mole
```

Проверка:

```bash
git --version
gh --version
mo --version
```

Если одна команда ведёт себя иначе, открой [«Если застрял»](help.md) и пришли точный output.

## 3. Установи основные приложения

```bash
brew install --cask chatgpt codexbar onlyoffice obsidian zotero deepl github
```

Здесь:

- `chatgpt` — новый ChatGPT desktop app, который включает Chat, Work и Codex;
- `codexbar` — menu-bar индикатор usage;
- `onlyoffice` — документы/таблицы/презентации;
- `obsidian` — Markdown notes;
- `zotero` — sources/citations;
- `deepl` — быстрый перевод;
- `github` — GitHub Desktop.

Официальный ChatGPT download также доступен здесь:
<https://chatgpt.com/download/>

## 4. Открой ChatGPT Desktop

Через Finder → Applications открой **ChatGPT** и войди в тот же account.

По текущей версии приложения Chat, Work и Codex находятся в одном desktop app:
<https://help.openai.com/en/articles/9275200-downloading-the-chatgpt-macos-app>

## 5. Mole: сначала только анализ

```bash
mo analyze
```

Ничего не удаляй только потому, что tool показывает caches.

Если позже понадобится cleanup:

```bash
mo clean --dry-run
```

`--dry-run` сначала показывает план без удаления.

Mole: <https://github.com/tw93/Mole>

## Что пока НЕ делать

Не запускай `brew bundle`. `Brewfile` находится в course repository, а мы сознательно **ещё не клонировали repository**. К Brewfile вернёмся после Git-урока.

Не устанавливай Python/VS Code только потому, что они упомянуты в curriculum. Они появятся тогда, когда будут нужны.

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

## Checkpoint

Перед уроком 3:

- [ ] `brew --version` работает;
- [ ] `git --version` работает;
- [ ] `gh --version` работает;
- [ ] `mo analyze` запускается;
- [ ] ChatGPT Desktop открывается;
- [ ] в ChatGPT ты видишь Chat/Work и отдельный Codex view.
