"""Скрипт запуска игры: Наибольший общий делитель."""
from brain_games.game_engine import run_engine_of_games
from brain_games.games import brain_gcd


def main():
    """Запускаем игру по нахождению наибольшего общего делителя."""
    get_engine_of_games(brain_gcd)


if __name__ == '__main__':
    main()
