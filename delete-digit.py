# Task
# Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example
# For n = 152, the output should be 52;

# For n = 1001, the output should be 101.

# Input/Output
# [input] integer n

# Constraints: 10 ≤ n ≤ 1000000.

# [output] an integer


def delete_digit(n):

    n = str(n)
    n_list = list(n)
    mx = 0


    for i in range(len(n_list)):
        n_list[i] = ''
        if int(''.join(n_list)) > mx:
            mx = int(''.join(n_list))
        
        n_list = n
        n_list = list(n_list)

    return mx



print(delete_digit(152))
