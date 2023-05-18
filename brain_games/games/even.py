from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import EVEN_INSTRUCTION


def is_even(num):
    return num % 2 == 0


def get_problem_number_and_answer():
    problem_num = get_random_number()
    answer = 'yes' if is_even(problem_num) else 'no'

    return problem_num, answer


def run_even_game():
    run_game(get_problem_number_and_answer, EVEN_INSTRUCTION)
