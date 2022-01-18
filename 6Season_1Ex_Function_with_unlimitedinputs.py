# First Solution Easy Way:

# def min_max_sum_len(*args):
#     '''Type of the args is Tuple'''
#     # print(type(args))
#     return min(args), max(args), sum(args), len(args)

# # print(min_max_sum_len(1, 2, 3, 4, 5, 6))


# min_result, max_result, sum_result, len_result = min_max_sum_len(1, 2, 3, 4, 5, 6) # Tuple Unpacking
# print(min_result, max_result, sum_result, len_result)


# Second Solution Reviw everythin:

def min_max_sum_len(*args, input_list):
    '''Type of the args is tuple'''

    # for (2)
    input_list.clear()

    # never use another numbers, only use the first value in list or tuple
    result_min = args[0]
    result_max = args[0]
    sum_result = 0
    len_result = 0

    for i in args:

        # input_list_copied = input_list.copy()
        # input_list_copied.append(i)

        input_list.append(i)

        len_result += 1

        if i < result_min:
            result_min = i

        if i > result_max:
            result_max = i

        sum_result += i

    return result_min, result_max, sum_result, len_result

# (1) my_list = list()
# or my_list = []


# (2)if the list was not empty, in the function you can use: my_list.clear()
my_list = [1, 1, 1]


print(my_list)  # first list is empty
print(min_max_sum_len(1, 2, 3, 4, 5, 6, input_list=my_list))
print(my_list)  # here list is full: we know list will change in the functions because they are indicating to same pictures

# if you want to get the empty list again, use this instead or do copy in the function:
# print(min_max_sum_len(1, 2, 3, 4, 5, 6, input_list = my_list.copy()))
