"""Game: Calculator."""
from random import choice, randint

START_NUMBER = 1
END_NUMBER = 100
GAME_DESCRIPTION = 'What is the result of the expression?'


def get_game_round():
    """Функция игры."""
    random_num1 = randint(START_NUMBER, END_NUMBER)
    random_num2 = randint(START_NUMBER, END_NUMBER)
    symbols = ['+', '-', '*']
    random_symbol = choice(symbols)
    question = '{0} {1} {2}'.format(random_num1, random_symbol, random_num2)
    if random_symbol == '+':
        answer = random_num1 + random_num2
    elif random_symbol == '-':
        answer = random_num1 - random_num2
    elif random_symbol == '*':
        answer = random_num1 * random_num2
    return str(question), str(answer)
