"""Game: Progression."""
from random import randint

LENGTH_PROGRESSION = 10
GAME_DESCRIPTION = 'What number is missing in the progression?'


def get_game_round():
    """Функция игры."""
    start_position = randint(1, 10)
    step = randint(2, 10)
    hidden_index = randint(0, LENGTH_PROGRESSION - 1)
    progression = ''
    answer = start_position + step * hidden_index
    for i in range(LENGTH_PROGRESSION):
        if i == hidden_index:
            progression = '{0} ..'.format(progression)
        else:
            progression = '{0} {1}'.format(progression,
                                           start_position + step * i)
    return str(progression.strip()), str(answer)
