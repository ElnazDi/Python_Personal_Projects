user_name = 'elnaz dehkharghani'


def make_title(my_string):
    return my_string.title()


def split_string(my_string):
    '''str.split() give a list of words seperated by space'''
    return my_string.split()[0]


def make_upper_the_first_words(my_string):
    '''
    (1) This function use the above function
    (2) always put the function into a variable
    (3) always return the value from the functions

    '''
    first_word = split_string(my_string)
    return first_word.upper()


def seperate_and_add(my_string):
    def seperate_stringer(my_string):
        return my_string.split()[0]

    new_word = 'Hello'
    first_word = seperate_stringer(my_string)
    return first_word + ' ' + new_word


# Since we have return, we must print here
print(make_title(user_name))
print(split_string(user_name))
print(make_upper_the_first_words(user_name))
print(seperate_and_add(user_name))
