"""Logic games."""
# !/usr/bin/env python
import prompt

ROUNDS_COUNT = 3


def welcome_user():
    """Приветствие."""
    print('Welcome to the Brain Games!')


def get_user_name():
    """Спрашиваем имя у пользователя и говорим ему привет."""
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(user_name))
    return user_name


def get_engine_of_games(game):
    """Движок игры."""
    welcome_user()
    user_name = get_user_name()
    print(game.GAME_DESCRIPTION)
    for i in range(count_round):
        question, answer = game.get_game_round()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print("{0} is wrong answer ;(. "
                  "Correct answer was {1}.\nLet\'s try again, {2}!".format
                  (user_answer, answer, user_name))
            return
    print('Congratulations, {0}!'.format(user_name))
