import prompt


def welcome_user_and_get_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
