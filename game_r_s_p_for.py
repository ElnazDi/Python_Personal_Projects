import random

list_of_choices = ['s', 'r', 'p']

game_dict = {
    'p': 'Paper',
    'r': 'Rock',
    's': 'Scissor'
}
user_counter = 0
ai_counter = 0

for i in range(5):
    user_choice = input(
        f'Which one: 1.Scissors  2.Rock  3.Paper Enter one of: {list_of_choices}\n\n')

    AI_choice = random.choice(list_of_choices)

    if user_choice in list_of_choices:
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


if user_counter > ai_counter:
    print(f'User = {user_counter} | AI = {ai_counter} \n You Won!!!')
elif user_counter < ai_counter:
    print(f'User = {user_counter} | AI = {ai_counter} \n AI Won!!!')
else:
    print(f'User = {user_counter} | AI = {ai_counter} \n Tie !!!')

# command + D => Select similar items in code
# option + pointer => so many pointers
