"""Game: Progression."""
from random import randint

LENGTH_PROGRESSION = 10
GAME_DESCRIPTION = 'What number is missing in the progression?'


def get_progression(initial_element, diff):
    """Получение прогрессии."""
    member, progression = initial_element, [initial_element]
    for i in range(LENGTH_PROGRESSION):
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
    initial_element = randint(1, LENGTH_PROGRESSION)
    diff = randint(2, LENGTH_PROGRESSION)
    hidden_element = randint(0, LENGTH_PROGRESSION - 1)

    answer = get_progression(initial_element, diff)
    question = get_string_from_progression(answer, hidden_element)

    return str(question), str(answer[hidden_element])
