import random

list_of_choices = ['s', 'r', 'p']

game_dict = {
    'p': 'Paper',
    'r': 'Rock',
    's': 'Scissor'
}
user_counter = 0
ai_counter = 0

while True:
    user_choice = input(
        f'Which one:\n 1.Scissors  2.Rock  3.Paper  \nEnter one of: {list_of_choices}\n\n')

    AI_choice = random.choice(list_of_choices)

    if user_choice in list_of_choices:
        print(f'You chose {game_dict[user_choice]}')
        print(f'AI choice is {game_dict[AI_choice]}')


        if user_choice == AI_choice:
            print(f'Tie ! AI = {ai_counter} and You = {user_counter}')
        elif user_choice == 'r' and AI_choice == 's':
            user_counter += 1
            print(f'user+1!!! AI = {ai_counter} and You = {user_counter}')
        elif user_choice == 'p' and AI_choice == 'r':
            user_counter += 1
            print(f'user+1!!! AI = {ai_counter} and You = {user_counter}')
        elif user_choice == 's' and AI_choice == 'p':
            user_counter += 1
            print(f'user+1!!! AI = {ai_counter} and You = {user_counter}')
        else:
            ai_counter += 1
            print(f'AI+1!!! AI = {ai_counter} and You = {user_counter}')
    else:
        print('Invalid input')

# command + D => Select similar items in code
# option + pointer => so many pointers
