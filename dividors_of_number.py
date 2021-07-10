# Enter your number to get all the divisor of it.
while True:
    your_number = int(input("Please enter your number:\n"))
    divider_list = []
    for i in range(1, your_number):
        if your_number % i == 0:
            divider_list.append(i)
    print(divider_list)
