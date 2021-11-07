"""Игра: Проверка на чётность."""
from random import randint

start_number = 1
end_number = 10
game_description = 'Answer \"yes\" if the number is even, ' \
                   'otherwise answer \"no\".'


def get_game_round():
    """Функция игры."""
    random_num = randint(start_number, end_number)
    if random_num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return random_num, answer
