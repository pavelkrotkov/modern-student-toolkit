# Modern Student Toolkit

Практический курс для студента, который **не собирается становиться программистом**, но хочет уверенно пользоваться современным Mac, ChatGPT, Codex, Git/GitHub, Obsidian и небольшими автоматизациями.

Курс написан по-русски, но сохраняет английские технические термины. Это намеренно: команды, ошибки, документация и интерфейсы почти всегда встречаются на английском.

## Что внутри

- базовая работа с файлами, папками и Terminal;
- установка и обновление программ через Homebrew;
- Chat vs Work vs Codex: какой режим выбирать и как не тратить лимиты впустую;
- работа Codex с локальными папками, browser use и Computer Use;
- MIT Missing Semester 2026 с русскоязычным AI-сопровождением;
- Git/GitHub на уровне грамотного пользователя, а не разработчика;
- Obsidian + private GitHub repo;
- персональный Codex skill `$teach-me`;
- Python как грамотность и средство автоматизации, а не как отдельная профессия;
- ONLYOFFICE, Zotero и перевод;
- минимальное обслуживание Mac.

Сайт собирается из Markdown через [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) и разворачивается на GitHub Pages.

## Локальный просмотр сайта

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Откройте <http://127.0.0.1:8000>.

## Публикация в новый public GitHub repo

На Mac с Homebrew:

```bash
brew install gh
./scripts/publish.sh
```

Скрипт создаёт public repo `pavelkrotkov/modern-student-toolkit`, включает GitHub Pages в режиме GitHub Actions и запускает deployment workflow. Перед публикацией можно передать другое имя:

```bash
./scripts/publish.sh USER/REPO
```

## Лицензия

MIT. Внешние материалы и ссылки принадлежат своим авторам и сохраняют их лицензии.
