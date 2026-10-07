# 11. Поддержание Mac в порядке

## Перед началом

К этому моменту Homebrew и основные apps уже используются регулярно. Этот урок — routine, а не ежедневная “оптимизация”.

## Раз в месяц

```bash
brew update
brew outdated
brew upgrade
brew cleanup
```

Если хочешь проверить reference Brewfile курса, используй **полный path**, а не зависимость от current directory:

```bash
brew bundle check --file ~/University/Projects/modern-student-toolkit/Brewfile
```

Если course repo давно не обновлялся, сначала:

```bash
cd ~/University/Projects/modern-student-toolkit
git pull
```

`brew bundle` автоматически устанавливать всё из reference file не обязательно: курс специально устанавливал tools постепенно.

## Если заканчивается место

Сначала:

```bash
mo analyze
```

Перед cleanup:

```bash
mo clean --dry-run
```

И только после просмотра решай, нужен ли:

```bash
mo clean
```

Mole:
<https://github.com/tw93/Mole>

## Периодически

- macOS security updates;
- убедиться, что backup действительно выполняется;
- посмотреть свободное место;
- удалить действительно ненужные apps;
- не устанавливать несколько “Mac cleaner” utilities.

Если есть внешний диск, настрой Time Machine и иногда проверяй дату последнего successful backup.

## Если Homebrew ведёт себя странно

```bash
brew doctor
```

Прочитай output. Если непонятно — пришли весь output Chat, а не запускай случайные forum fixes.

## Codex usage

Перед длинной Work/Codex task посмотри официальный usage meter и CodexBar. Если weekly allowance почти закончился, оставь agent work для задач, которым реально нужны tools/files, а объяснения делай в Chat.

## Итоговая привычка

Хороший Mac обычно требует меньше “чистки”, чем кажется. Нормальная routine:

**updates → backup → free space check → понятные удаления**.
