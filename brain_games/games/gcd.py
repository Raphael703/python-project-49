import math
from brain_games.core import run_game
from brain_games.utils import get_random_number
from brain_games.const import GCD_INSTRUCTION


def get_nums_pair_and_gcd():
    first_num, second_num = get_random_number(), get_random_number()
    nums_pair = f'{first_num} {second_num}'
    gcd = math.gcd(first_num, second_num)

    return nums_pair, str(gcd)


def run_gcd_game():
    run_game(get_nums_pair_and_gcd, GCD_INSTRUCTION)
