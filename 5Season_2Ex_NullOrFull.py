import random

cups = int(input('How many cups? '))
chances = int(input('How many chances? '))

ai_goal = random.randint(1, cups)
print('-' * 20)
word = 's'


for i in range(chances):
    if chances - i == 1:
        word = ''
    print(f'{chances - i} chance{word} left.')
    user_guess = int(input(f'Guess [1-{cups}]: '))

    if user_guess == ai_goal:
        print('You guessed right.')
        break
    else:
        print('Wrong guess.')

    print('-' * 20)


if user_guess == ai_goal:
    print('-' * 20)
    print('You Won!')
else:    
    print(f'The right answer is {ai_goal}')
    print('You lost. Sorry!')
