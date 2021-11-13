"""Game: GCD."""
from random import randint

START_NUMBER = 1
END_NUMBER = 100
GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers'


def is_gcd(random_number1, random_number2):
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 %= random_number2
        else:
            random_number2 %= random_number1
    return random_number1 + random_number2


def get_game_round():
    """Функция игры."""
    random_num1 = randint(START_NUMBER, END_NUMBER)
    random_num2 = randint(START_NUMBER, END_NUMBER)

    question = '{0} {1}'.format(random_num1, random_num2)
    answer = is_gcd(random_num1, random_num2)

    return str(question), str(answer)
