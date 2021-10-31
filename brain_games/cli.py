"""Модуль CLI."""
import prompt


def welcome_user():
    """Спрашиваем имя пользователя и приветствуем его."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
