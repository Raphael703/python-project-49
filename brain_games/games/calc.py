import random
from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import CALC_INSTRUCTION


def get_random_math_sign_and_result(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])


def get_math_question_and_result():
    first_num, second_num = get_random_number(), get_random_number()
    sign, result = get_random_math_sign_and_result(first_num, second_num)
    question = f'{first_num} {sign} {second_num}'

    return question, str(result)


def run_calc_game():
    run_game(get_math_question_and_result, CALC_INSTRUCTION)
