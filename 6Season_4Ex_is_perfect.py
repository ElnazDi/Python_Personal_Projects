# Perfect => divisors of 6 = [1, 2, 3, 6] if 1 + 2 + 3 = 6 => it is perfect
# First solution
# def is_perfect(num):
#     divisors = []
#     for i in range(1, num):
#         if num % i == 0:
#             divisors.append(i)
#     if sum(divisors) == num:
#         return True
#     return False


# print(is_perfect(6))


# Second Solution
def divisors(num):
    '''Find all the divisors of num
       Ex: 6 = [1, 2, 3, 6]
    '''
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def is_perfect(num):
    sum_divisors = sum(divisors(num)) - num

    return sum_divisors == num, sum_divisors


bool_value, sum_divisors = is_perfect(100)
print(
    f' The result is: {bool_value}, \n because sum of the divisors of your number is {sum_divisors} !')
