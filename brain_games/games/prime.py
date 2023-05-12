from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import PRIME_INSTRUCTION


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def get_problem_number_and_answer():
    problem_number = get_random_number()
    answer = 'yes' if is_prime(problem_number) else 'no'

    return problem_number, answer


def run_game_prime():
    run_game(get_problem_number_and_answer, PRIME_INSTRUCTION)
