"""Скрипт запуска игры: Проверка на чётность."""
from brain_games.game_engine import run_engine_of_games
from brain_games.games import brain_even


def main():
    """Запускаем игру Проверка на чётность."""
    get_engine_of_games(brain_even)


if __name__ == '__main__':
    main()
