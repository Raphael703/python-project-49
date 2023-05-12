import random
from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import CALC_INSTRUCTION, MATH_SIGNS


def get_match_sign():
    return random.choice(MATH_SIGNS)


def get_math_question_and_answer():
    first_num, second_num = get_random_number(), get_random_number()
    sign = get_match_sign()
    question = f'{first_num} {sign} {second_num}'

    if sign == '-':
        result = first_num - second_num
    elif sign == '+':
        result = first_num + second_num
    else:
        result = first_num * second_num

    return question, str(result)


def start_calc_game():
    run_game(get_math_question_and_answer, CALC_INSTRUCTION)
