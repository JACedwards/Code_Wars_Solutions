# Given a name, turn that name into a perfect square matrix (nested array with the amount of arrays equivalent to the length of each array).

# You will need to add periods (.) to the end of the name if necessary, to turn it into a matrix.

# If the name has a length of 0, return "name must be at least one letter"

# Examples
# "Bill" ==> [ ["B", "i"],
#              ["l", "l"] ]

# "Frank" ==> [ ["F", "r", "a"],
#               ["n", "k", "."],
#               [".", ".", "."] ]

#Psuedo:
#  divide length of string by 2
#  round up math.ceil(2.0) (store in variable "up")
#  split string into list
#    ["B", "i", "l", "l"]
#   while loop, each letters*up into separate list

# ####-----------------------works for 0, 1, 2, 3, 4, 5, 6 letter words (only) -----------------------#
# import math

# def matrixfy(st):

#     count_1 = 1
#     count_2 = 0
#     index = 0
#     row = []
#     output = []

#     if len(st) == 0:
#         return "name must be at least one letter"

#     if len(st) == 1:
#         row.append(st)
#         output.append(row)
#         return output

#     if len(st) == 2:
#         st = list(st)
#         output.append(st)
#         output.append(['.','.'])
#         return output


#     length = len(st) / 2
#     length = math.ceil(length)
#     st = list(st)
#     #add appropriate number of periods to finish out matrix
#     len_st_n_pers = length * length
#     num_pers = len_st_n_pers - len(st)
#     x_pers = ['.'] * num_pers
#     st = st +  x_pers
#     # print(st)


#     while count_1 <= length:
#         while count_2 <= length -1:
#             row.append(st[index])
#             # print(f'row = {row}')
#             index += 1
#             count_2 += 1
#         output.append(row)
#         # print(f'output = {output}')
#         count_1 +=1
#         row = []
#         count_2 = 0
    
#     return output


# print(matrixfy("franklin"))

####-----------------------works for letters of any "n" -----------------------#
import math

def matrixfy(st):

    count_1 = 1
    count_2 = 0
    index = 0
    row = []
    output = []

    if len(st) == 0:
        return "name must be at least one letter"

    if len(st) == 1:
        row.append(st)
        output.append(row)
        return output

    if len(st) == 2:
        st = list(st)
        output.append(st)
        output.append(['.','.'])
        return output


    length = math.sqrt(len(st))  #key is using square root here
    length = math.ceil(length)
    st = list(st)
    #add appropriate number of periods to finish out matrix
    len_st_n_pers = length * length
    num_pers = len_st_n_pers - len(st)
    x_pers = ['.'] * num_pers
    st = st +  x_pers
    # print(st)


    while count_1 <= length:
        while count_2 <= length -1:
            row.append(st[index])
            # print(f'row = {row}')
            index += 1
            count_2 += 1
        output.append(row)
        # print(f'output = {output}')
        count_1 +=1
        row = []
        count_2 = 0
    
    return output


print(matrixfy("franklin"))


