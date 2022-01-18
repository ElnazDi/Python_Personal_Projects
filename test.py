# Factorial (Recursive Function)

# 5! = 1 * 2 * 3 * 4 * 5
# 4! = 1 * 2 * 3 * 4 

# 5! = (factorial(3) * 4 )* 5

def factorial(n):
    print(n)
    # this is is very important to finish itself calling
    if n == 1:
        return 1
    # when if is True it will back step by step => 1 * 2 , 2 * 3, 6 * 4, 24 * 5    
    return n * factorial(n - 1)


print(factorial(5))

# Call himself
# 5 -> 4 -> 3 -> 2 -> 1 

# THEN Recursive
# (return 1) * (INMemory 2) => 2 
#  2         * (INMemory 3)  => 6
#  6         * (INMemory 4) => 24
#  24        * (INMemory 5) => 120


