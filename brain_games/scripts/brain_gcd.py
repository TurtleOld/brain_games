"""Скрипт запуска игры: Наибольший общий делитель."""
from brain_games.game_logic import get_logic_of_games
from brain_games.games import brain_gcd


def main():
    """Запускаем игру."""
    get_logic_of_games(brain_gcd)


if __name__ == '__main__':
    main()
