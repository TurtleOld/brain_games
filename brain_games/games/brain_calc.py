"""Game: Calculator."""
from random import choice, randint

start_number = 1
end_number = 100
GAME_DESCRIPTION = 'What is the result of the expression?'


def get_game_round():
    """Функция игры."""
    random_num1 = randint(start_number, end_number)
    random_num2 = randint(start_number, end_number)
    symbols = ['+', '-', '*']
    random_symbols = choice(symbols)
    question = '{0} {1} {2}'.format(random_num1, random_symbols, random_num2)
    answer = ''
    if random_symbols == '+':
        answer = random_num1 + random_num2
    elif random_symbols == '-':
        answer = random_num1 - random_num2
    elif random_symbols == '*':
        answer = random_num1 * random_num2
    return str(question), str(answer)
