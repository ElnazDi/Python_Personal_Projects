import random

list_of_choices = ['s', 'r', 'p']

game_dict = {
    'p': 'Paper',
    'r': 'Rock',
    's': 'Scissor'
}
user_counter = 0
ai_counter = 0
win_number = 5

# while is better option than for to minus the invalid chars
while True:
    user_choice = input(
        f'Which one: 1.Scissors  2.Rock  3.Paper Enter one of: {list_of_choices}\n\n')

    AI_choice = random.choice(list_of_choices)

    if user_choice in list_of_choices:
        # write print here it here to do not get error in invalid
        print(
            f'You chose {game_dict[user_choice]} and AI choice is {game_dict[AI_choice]}')
        if user_choice == AI_choice:
            print(f'Tie !')
        elif user_choice == 'r' and AI_choice == 's':
            user_counter += 1
            print(f'user+1!!!')
        elif user_choice == 'p' and AI_choice == 'r':
            user_counter += 1
            print(f'user+1!!!')
        elif user_choice == 's' and AI_choice == 'p':
            user_counter += 1
            print(f'user+1!!!')
        else:
            ai_counter += 1
            print(f'AI+1!!!')
    else:
        print('Invalid input')
    print(f'Your score = {user_counter} and AI score = {ai_counter}')
    print("\n", "_"*50, "\n")

    if user_counter == win_number or ai_counter == win_number:
        break


if user_counter == win_number:
    print('You Won !')
else:
    print('AI Won !')

# command + D => Select similar items in code
# option + pointer => so many pointers
