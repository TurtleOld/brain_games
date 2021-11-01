"""Игра: Проверка на чётность."""
from random import randint
import prompt

count_round = 3
start_random = 1
end_random = 10
description = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def welcome_user():
    print("Welcome to the Brain Games!")


def get_user_name():
    user_name = prompt.string("May I have your name? ")
    print("Hello, {0}".format(user_name))
    return user_name


def is_even(question):
    if question % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return answer


def get_game_even():
    welcome_user()
    user_name = get_user_name()
    print(description)
    for i in range(count_round):
        random_number = randint(start_random, end_random)
        question = random_number
        print("Question: {0}".format(question))
        user_answer = prompt.string("Your answer: ")
        answer = is_even(question)
        if user_answer == answer:
            print("Correct!")
        else:
            print("{0} is wrong answer ;(. Correct answer was {1}.\nLet\'s try again, {2}!".format(user_answer, answer, user_name))
    print("Congratulation, {0}!".format(user_name))