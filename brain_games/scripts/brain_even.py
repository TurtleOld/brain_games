"""Скрипт запуска игры: Проверка на чётность."""
# !/usr/bin/env python
from brain_games.game_logic import get_logic_of_games
from brain_games.games import brain_even


def main():
    """Запускаем игру."""
    get_logic_of_games(brain_even)


if __name__ == '__main__':
    main()
