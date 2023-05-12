import prompt
from brain_games.cli import welcome_user_and_get_name
from brain_games.const import ROUNDS_NUMBER


def run_game(get_specific_qa, game_instruction):
    name = welcome_user_and_get_name()
    print(game_instruction)

    for _ in range(ROUNDS_NUMBER):
        question, correct_answer = get_specific_qa()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
