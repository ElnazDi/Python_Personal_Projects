# Elnaz Solution
def find_biggest_string(*strings):
    '''  *strings == *args this in tuple'''
    length = 0 # we do not have lesser length than 0
    my_list = []

    for string in strings:
        big_string = strings[0]
        length = len(string)
        my_list.append(length)
        big_string = string

    return max(my_list), big_string


max_length, big_string = find_biggest_string('This', 'Elnaz Dehkharghani', 'Ich bin verheiratet und Ich wohne in Mannheim')
print(f' The maximum length is: {max_length} \n The string is: {big_string}')


# Second solution = M.Hadi Hosseini
def calc_max_string(*args):

    max_string = args[0]

    for string in args:
        if len(string) > len(max_string):
            max_string = string


    return len(max_string), max_string


print(calc_max_string('This', 'Elnaz Dehkharghani', 'Ich bin verheiratet und Ich wohne in Mannheim'))





