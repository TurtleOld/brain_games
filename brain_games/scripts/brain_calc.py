"""Скрипт запуска игры: Калькулятор."""
from brain_games.game_logic import get_logic_of_games
from brain_games.games import brain_calc


def main():
    """Запускаем игру."""
    get_logic_of_games(brain_calc)


if __name__ == '__main':
    main()
