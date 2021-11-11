"""Game: GCD."""
from random import randint

START_NUMBER = 1
END_NUMBER = 100
GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers'


def get_game_round():
    """Функция игры."""
    random_num1 = randint(START_NUMBER, END_NUMBER)
    random_num2 = randint(START_NUMBER, END_NUMBER)
    question = '{0} {1}'.format(random_num1, random_num2)
    answer = 0
    while random_num1 != 0 and random_num2 != 0:
        if random_num1 > random_num2:
            random_num1 %= random_num2
        else:
            random_num2 %= random_num1
        answer = random_num1 + random_num2
    return str(question), str(answer)
