import math
from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import GCD_INSTRUCTION


def get_gcd_question_and_correct_answer():
    first_number, second_number = get_random_number(), get_random_number()
    question = f'{first_number} {second_number}'

    correct_answer = math.gcd(first_number, second_number)
    return question, str(correct_answer)


def start_gcd_game():
    run_game(get_gcd_question_and_correct_answer, GCD_INSTRUCTION)
