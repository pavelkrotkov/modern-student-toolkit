# Contributing

Этот файл предназначен для автора курса и contributors, **не для ученика, проходящего курс впервые**.

## Локальный просмотр сайта

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Открой <http://127.0.0.1:8000>.

## Публикация

GitHub Pages разворачивается автоматически workflow `.github/workflows/pages.yml` после push в `main`.

## Педагогическая проверка перед merge

Каждый learner-facing урок должен:

1. явно назвать prerequisites;
2. не использовать command/tool до того, как он был установлен и объяснён;
3. не предполагать, что learner уже клонировал этот repository;
4. не использовать фразу «из корня repo» до Git-урока, где понятие root объясняется;
5. использовать стабильную структуру `~/University` из урока 0;
6. давать безопасный способ получить помощь, если шаг не совпадает с текущим UI.

Если меняется порядок уроков, проверь dependency chain целиком.
