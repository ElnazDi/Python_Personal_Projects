# (With For)
number_of_inputs = int(input('How many scores do you have? '))

scores = []
for _ in range(number_of_inputs):
    score = int(input('please enter scores: '))
    scores.append(score)
print(scores)


# (With While)
print('Enter your student scores, when you are finish write exit.')
scores = []
while True:
    user_input = input('Enter score:')
    if user_input == 'exit':
        break
    scores.append(int(user_input))
print(f'Entered scores are: {scores}')
print(f'The max grade is: {max(scores)}')
print(f'The min grade is: {min(scores)}')
print(f'The average is: {sum(scores)/len(scores)}')
