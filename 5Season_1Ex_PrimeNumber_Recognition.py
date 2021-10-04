# PRIME
# Prime Number can be divided only by (1 , itself) => % == 0 


# This fact is True for all other numbers (1, itself) => % == 0


# NOT PRIME
# If a number can be divided by other numbers as well between (2, *until* itself) => % == 0



###################################################################
# If a number % between (2, one before itself) == 0 then NOT PRIME
###################################################################


is_prime = True
user_input = int(input('Enter number: '))
for i in range(2, user_input):
    if user_input % i == 0:
        print(f'{user_input} % {i} is Zero!')
        is_prime = False
        break

if is_prime == True:
    print(f'{user_input} is Prime')
else:
    print(f'{user_input} is not Prime.')

