import random
import prompt

from brain_games.cli import welcome_user


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0

    while counter < 3:
        given_number = random.randint(1, 99)
        print(f'Question: {given_number}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = is_even(given_number)
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"Oops, that's not quite right. "
                  f"Correct answer was {correct_answer}. "
                  f"Keep trying, you'll get it next time!")
            counter = 0


if __name__ == '__main__':
    main()
