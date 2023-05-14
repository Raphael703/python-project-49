from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import EVEN_INSTRUCTION


def is_even(num):
    return True if num % 2 == 0 else False


def get_problem_number_and_answer():
    num = get_random_number()
    answer = 'yes' if is_even(num) else 'no'

    return num, answer


def run_even_game():
    run_game(get_problem_number_and_answer, EVEN_INSTRUCTION)
