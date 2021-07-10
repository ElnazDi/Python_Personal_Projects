list_of_names = ['Elnaz', 'Sanaz', 'Farnaz',
                 'Hamid', 'Fariba', 'Hassan', 'Elyas', 'Setia']
correct_guess = list_of_names[3]
print(list_of_names)
your_geuss = input('Please enter your guess word:\n')
for i in range(5):
    if your_geuss == correct_guess:
        print('You Won!')
        break
    elif i == 4:
        print('You are loser!')
    else:
        print(f'No, It is not correct ! you can try {4-i} times more')
        your_geuss = input('Try again:\n')
print(f'Correct word was {correct_guess}!')
