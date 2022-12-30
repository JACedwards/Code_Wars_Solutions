# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

#pseudo:
# convert to string,
# split into digits
# square each digit
# concatenating the string version of each product.

#squaring method = x * x

# def square_digits(num):
#     s = str(num)
#     s = list(s)
#     output = ''
#     sq = 0
#     convert_st = ''

#     for d in s:
#         sq = int(d)*int(d)
#         convert_st = str(sq)
#         output = f'{output}{convert_st}'

#     return output 

# print(square_digits('9119'))

#squaring method = x**2

# def square_digits(num):
#     s = str(num)
#     s = list(s)
#     output = ''
#     sq = 0
#     convert_st = ''

#     for d in s:
#         sq = int(d)**2
#         convert_st = str(sq)
#         output = f'{output}{convert_st}'

#     return output 

# print(square_digits('9119'))

#square using math library

import math

def square_digits(num):
    s = str(num)
    s = list(s)
    output = ''
    sq = 0
    convert_st = ''

    for d in s:
        sq = pow(int(d), 2)
        convert_st = str(sq)
        output = f'{output}{convert_st}'

    output = int(output)

    return output 

print(square_digits('91'))