# Expansion is performed for a given 2x2 matrix.

# [
#   [1,2],
#   [5,3]
# ]
# After expansion:

# [
#   [1,2,a],
#   [5,3,b],
#   [c,d,e]
# ]
# a = 1 + 2 = 3
# b = 5 + 3 = 8
# c = 5 + 1 = 6
# d = 3 + 2 = 5
# e = 1 + 3 = 4
# Final result:

# [
#   [1,2,3],
#   [5,3,8],
#   [6,5,4]
# ]
# TASK
# Let expansion be a function which takes two arguments:

# A: given NxN matrix
# n: number of expansions

#Pseudo:
#  import nympy
#  convert matrix to np array
#    w 0's at end of first two rows
#    and all 0's in final row
#  add rows
# add columns

#-------------------works with known matrix size of 2 x 2-----------------#
# def expansion(matrix, n):

#     output = []
    
#     for r in matrix:
#         r.append(sum(r))
#         output.append(r)
#     #output = [[1, 2, 3], [5, 3, 8]]

#     last_row = []
#     for i in range(len(output[0])):
#         last_row.append(output[0][i]+output[1][i])
    
#     output.append(last_row)
    
#     return output

# print(expansion([[1,2],[5,3]],1))


##---------------this one works with any size of matrix, but can only expand once, not "n" times-----------------##
def expansion(matrix, n):

    output = []
    
    for r in matrix:
        r.append(sum(r))
        output.append(r)
    print(f'output = {output}')

    last_row = []
    ind = 0
    add = 0
    for i in range(len(output[0])):
        while ind <= len(output[0])-2:
            add = add + output[ind][i]
            ind +=1
        last_row.append(add)

        add = 0
        ind = 0
    last_row[-1]= 0
    print(f'lastrow swap 0 = {last_row}')
    output.append(last_row)
    print(f"output = {output}")

    #replacing final vaule with diagonal addition

    
    ind_2 = 0
    add_2 = 0
    for i in range(len(output[0])):
        add_2 = add_2 + output[ind_2][i]
        print(f'output[ind_2][i] = {output[ind_2][i]}')
        ind_2 +=1
    last_row[-1]=add_2
    output[-1]=last_row


    return output

print(expansion([[1,2,3], [1,2,3], [1,2,3]],1))

# [
#   [1,2,3],
#   [5,3,8],
#   [6,5,*4]
# ]

# [
#   [1,2,3],
#   [5,3,8],
#   [6,5,*11]
# ]

# [
#   [1,2,3],
#   [5,3,8],
#   [6,5,*0]
# ]



#numpy start

# import numpy as np

# def expansion(matrix, n):
#     matrix = np.array(matrix)

#     x = np.insert(matrix, 2, 0, axis=1)
#     x = np.append(x, [[0,0,0]], axis=0)
#     # x = #expanded matrix with 0s

#     for r in x:


# print(expansion([[1,2],[5,3]],1))



