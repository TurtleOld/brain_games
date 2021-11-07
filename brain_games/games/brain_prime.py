"""Game: Calculator."""
from random import randint

game_description = 'Answer "yes" if given number is prime. Otherwise answer "no"'
start_number = 2
end_number = 100


def get_game_round():
    """Функция игры."""
    number = 0
    random_number = randint(start_number, end_number)
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            number += 1
    if number <= 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(random_number), str(answer)
