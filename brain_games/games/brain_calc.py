"""Game: Calculator."""
from random import randint

import prompt

count_round = 3
start_random = 1
end_random = 10
description = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def welcome_user():
    """Приветствие."""
    print('Welcome to the Brain Games!')


def get_user_name():
    """Спрашиваем имя у пользователя и говорим ему привет."""
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(user_name))
    return user_name


def get_game_calc():
    welcome_user()
    user_name = get_user_name()
