# 11. Поддержание Mac в порядке

Mac не требует постоянной “оптимизации”. Полезнее редкие понятные действия.

## Раз в месяц

```bash
brew update
brew outdated
brew upgrade
brew cleanup
```

Проверить Brewfile:

```bash
brew bundle check
```

Если чего-то не хватает:

```bash
brew bundle
```

## Если заканчивается место

Сначала диагностика:

```bash
mo analyze
```

Или machine-readable report для Codex:

```bash
mo analyze --json ~/Documents
```

Перед cleanup:

```bash
mo clean --dry-run
```

Только после просмотра списка решай, запускать ли:

```bash
mo clean
```

Mole safety guidance:
<https://github.com/tw93/Mole>

## Периодически

- установить macOS security updates;
- проверить, что backup действительно работает;
- посмотреть свободное место;
- удалить приложения, которые больше не нужны, нормальным uninstaller или `mo uninstall` с preview;
- не устанавливать пять “Mac cleaner” приложений одновременно.

## Если что-то сломалось после обновления Brew

```bash
brew doctor
```

Затем прочитай вывод. Не копируй случайные команды из форума, не понимая их.

## Проверка Codex usage

Перед длинной agent task посмотри официальный usage meter и CodexBar. Если weekly allowance низкий, используй Chat для объяснений и оставь Codex для задач, которым действительно нужны files/tools.
