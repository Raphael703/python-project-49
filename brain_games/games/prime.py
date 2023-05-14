from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import PRIME_INSTRUCTION


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_problem_number_and_answer():
    problem_num = get_random_number()
    answer = 'yes' if is_prime(problem_num) else 'no'

    return problem_num, answer


def run_game_prime():
    run_game(get_problem_number_and_answer, PRIME_INSTRUCTION)
