import random


def get_input():
    while True:
        user_input = input('Enter your guess: ')
        if user_input.isalpha():
            return user_input
        print('Please enter a valid alphabet words')


def get_input_from_list(words):
    user_input = get_input()
    while user_input.lower() not in words:
        print('You should guess a word from the given words list!')
        print('Please enter a correct word.')
        user_input = get_input()

    return user_input.lower()


def print_game_intro():
    print('-' * 10)
    print('Hi, Welcome to the Guess Game.')
    print('All words', list_of_words)
    print('Please start guessing.')
    print('-' * 10)


def run_game(number_of_rounds, words):
    print_game_intro()
    print(f'Number of guesses: {number_of_rounds}')
    correct_word = random.choice(words)

    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)

        if user_input == correct_word:
            print('You Won!')
            return
        else:
            print('You guessed wrong!')
            print(
                f'Please try again, number of rounds left: {number_of_rounds - 1 - i}')

    print('You Lost!')


# list_of_words = ['elnaz', 'sanaz', 'farnaz', 'hassan', 'hamid', 'fariba', 'setia', 'elyas']
# Or like string -> split on the string will put them in the list

list_of_words = 'salam iran chetori khoobi'.split()
run_game(3, list_of_words)
