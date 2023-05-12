from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import EVEN_INSTRUCTION


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_number_and_correct_answer():
    number = get_random_number()
    correct_answer = is_even(number)
    return number, correct_answer


def start_even_game():
    run_game(get_number_and_correct_answer, EVEN_INSTRUCTION)
