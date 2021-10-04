import random

cups = int(input('How many cups? '))
chances = int(input('How many chances? '))

ai_goal = random.randint(1, cups)

for i in range(chances):
    print('-' * 20)
    print(f'{chances} chances left.')
    chances -= 1
    user_guess = int(input(f'Guess [1-{cups}]: '))
    if user_guess == ai_goal:
        print('You guessed right.')
        print('-' * 20)
        print('You Won!')
        break
    else:
        print('Wrong guess.')

if chances == 0 and user_guess != ai_goal:
    print('-' * 20)
    print(f'The right answer is {ai_goal}')
    print('You lost. Sorry!')
