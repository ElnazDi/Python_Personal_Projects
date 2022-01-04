def is_even(num):
    if num % 2 == 0:
        return True
    return False

def even_odd_catcher(list_of_nums):
    even_list = []
    odd_list = []
    for num in list_of_nums:
        if is_even(num):
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list


print(even_odd_catcher([1, 2, 4, 77, 2]))
even_nums, odd_nums = even_odd_catcher([1, 2, 4, 77, 2])
print(even_nums, odd_nums)

# ([2, 4, 2], [1, 77])
# [2, 4, 2] [1, 77]

