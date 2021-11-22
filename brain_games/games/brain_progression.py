"""Game: Progression."""
from random import randint

LENGTH_PROGRESSION = 10
FIRST_DIFF_PROGRESSION = 2
MIN_NUMBER_RANDOM = 1
MIN_HIDDEN_NUMBER = 0
GAME_DESCRIPTION = 'What number is missing in the progression?'


def get_progression(initial_element, diff, length_progression):
    """Получение прогрессии."""
    member, progression = initial_element, [initial_element]
    for i in range(length_progression):
        member += diff
        progression.append(member)
    return progression


def get_string_from_progression(progression, hidden_element):
    """Получение строкового представления прогрессии."""
    string_progression = []
    for element in progression:
        string_progression.append(str(element))
    string_progression[hidden_element] = '..'
    return " ".join(string_progression)


def get_game_round():
    """Функция игры."""
    initial_element = randint(MIN_NUMBER_RANDOM, LENGTH_PROGRESSION)
    diff = randint(FIRST_DIFF_PROGRESSION, LENGTH_PROGRESSION)
    hidden_element = randint(MIN_HIDDEN_NUMBER, LENGTH_PROGRESSION - MIN_NUMBER_RANDOM)

    answer = get_progression(initial_element, diff, LENGTH_PROGRESSION)
    question = get_string_from_progression(answer, hidden_element)

    return str(question), str(answer[hidden_element])
