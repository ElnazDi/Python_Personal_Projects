import random

list_of_choices = ['r', 'p', 's']

choice_dict = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissor'
}
# Get user input
user_choice = input(
    'Please select between Rock, Scissor and Paper: (r, s, p) ')


# Hard coding
# AI_choice = 'r'
AI_choice = random.choice(list_of_choices)


# Check input validation
if user_choice in list_of_choices:
    print(
        f'Your choice is {choice_dict[user_choice]}. AI choice is {choice_dict[AI_choice]}.')
    # print('Valid')
    # p > r, s > p, r > s
    if user_choice == AI_choice:
        print('Tie !')
    # Clean Code, but we can also write in long way with only one if to avoid You Won repeating.
    # elif  (user_choice == 'p' and AI_choice == 'r')  or (user_choice == 'p' and AI_choice == 'r') or (user_choice == 'r' and AI_choice == 's'):
    #     print('You Won!')
    elif user_choice == 'p' and AI_choice == 'r':
        print('You Won !')
    elif user_choice == 's' and AI_choice == 'p':
        print('You Won!')
    elif user_choice == 'r' and AI_choice == 's':
        print('You Won!')
    else:
        print('You Lost!')
else:
    print('Sorry, please enter a correct element!')
