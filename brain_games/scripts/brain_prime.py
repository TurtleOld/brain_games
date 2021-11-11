"""Скрипт запуска игры: Проверка на простоту числа."""
from brain_games.game_engine import get_engine_of_games
from brain_games.games import brain_prime


def main():
    """Запускаем игру на проверку простого числа."""
    get_engine_of_games(brain_prime)


if __name__ == '__main__':
    main()
