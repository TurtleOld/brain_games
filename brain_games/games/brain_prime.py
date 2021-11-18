"""Game: Calculator."""
from random import randint

GAME_DESCRIPTION = 'Answer \"yes\" if given number is prime. ' \
                   'Otherwise answer \"no\"'
START_NUMBER = 2
END_NUMBER = 100


def is_prime(random_number):
    """Проверка на простое число."""
    number = 0
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            number = 1
    if number <= 0:
        return True
    else:
        return False


def get_game_round():
    """Функция игры."""
    random_number = randint(START_NUMBER, END_NUMBER)
    answer = is_prime(random_number)

    return str(random_number), str(answer)
