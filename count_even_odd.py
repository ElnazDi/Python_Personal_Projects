# (1) How to get the last digit in this number?
# my_num = 123456
#print(my_num % 10)


# (2) How to remove the last digit from my_num?
#print(my_num // 10)


# (3) Now solve a program to count number of even and odd digits...
# count_even = 0
# count_odd = 0
# while my_num != 0:
#     reminder = my_num % 10
#     if reminder % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
#     my_num = my_num // 10
# print(count_even, count_odd)


# (4) Now try again by getting values from the user:
for i in range(5):
    my_num = int(input(f"Enter your number:\n"))

    count_even = 0
    count_odd = 0
    while my_num != 0:
        reminder = my_num % 10
        if reminder % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        my_num = my_num // 10

    print(
        f'Your number has {count_even} even and {count_odd} odd numbers init !')
