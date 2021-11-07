"""Game: Calculator."""
from random import randint

start_number = 1
end_number = 100
game_description = 'Find the greatest common divisor of given numbers'


def get_game_round():
    """Функция игры."""
    random_num1 = randint(start_number, end_number)
    random_num2 = randint(start_number, end_number)
    question = '{0} {1}'.format(random_num1, random_num2)
    answer = ''
    while random_num1 != 0 and random_num2 != 0:
        if random_num1 > random_num2:
            random_num1 %= random_num2
        else:
            random_num2 %= random_num1
        answer = random_num1 + random_num2
    return str(question), str(answer)
