"""Скрипт запуска игры: Арифметическая прогрессия."""
from brain_games.game_logic import get_logic_of_games
from brain_games.games import brain_progression


def main():
    """Запускаем игру Арифметическая прогрессия."""
    get_logic_of_games(brain_progression)


if __name__ == '__main__':
    main()
