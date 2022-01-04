# 1000 + 0.2 = 1000 + (1000 * 0.2) = 1000 (1 + (1 + 0.2)) = current_money * (1 + rate))


def calc_bank_investment(intial_money, num_of_years, rate = 0.2):
    current_money = intial_money

    for i in range(num_of_years):
        current_money *= 1 + rate
    return current_money
# rate is default, if we add it in the below then it will substitude with the defualt one
print(calc_bank_investment(1000, 3))

