"""Игра: Проверка на чётность."""
from random import randint

START_NUMBER = 1
END_NUMBER = 10
GAME_DESCRIPTION = 'Answer \"yes\" if the number is even, ' \
                   'otherwise answer \"no\".'


def is_even(random_number):
    """Проверка на чётность."""
    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def get_game_round():
    """Функция игры."""
    random_number = randint(START_NUMBER, END_NUMBER)
    answer = is_even(random_number)

    return random_number, answer
