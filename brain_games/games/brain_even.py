"""Игра: Проверка на чётность."""
from random import randint

START_NUMBER = 1
END_NUMBER = 10
GAME_DESCRIPTION = 'Answer \"yes\" if the number is even, ' \
                   'otherwise answer \"no\".'


def get_game_round():
    """Функция игры."""
    random_num = randint(START_NUMBER, END_NUMBER)
    if random_num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return random_num, answer
