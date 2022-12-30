# sam how to get version at the end to rotate multiple times

# In this kata your mission is to rotate matrix counter - clockwise N-times.

# So, you will have 2 inputs:

# 1)matrix

# 2)a number, how many times to turn it
# And an output is turned matrix.
# Example:

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
      
# times_to_turn = 1
# It should return this:

# [[4, 8, 12, 16],
#  [3, 7, 11, 15],
#  [2, 6, 10, 14],
#  [1, 5, 9, 13]])
# Note: all matrices will be square. Also random tests will have big numbers in input (times to turn)

#           [6, 7],
#           [10, 11]
#output
#           [7, 11],
#           [6, 10]

#second turn [11, 10]
#            [7, 6]

#Psuedo:
# convert to matrix
# import numpy
# rotate, using rot90

#######------------works with np.rot(90)------------------#

# import numpy as np

# def counter(matrix, times, axes):

#     matrix = np.array(matrix)
#     print(matrix)
#     y = np.rot90(matrix, times, axes)
#     print(y)
#     output = y.tolist()
#     return output


# # print(counter([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]],1, (0,1)))
# print(counter([[6,7], [10,11]], 2, (0,1)))

##---------------------------version without using np.rot90 / works only for matrix of size 2x2 / 1 rotation ----------------##


#           [6, 7],
#           [10, 11]
#output
#           [7, 11],
#           [6, 10]

# import numpy as np

# def counter(matrix, times):
#     # matrix.reverse()
#     # print(matrix)
#     length = len(matrix[0]) - 1
#     index_1 = 0
#     index_2 = 0

#     matrix = np.array(matrix)
#     rows = []
#     output = []
#     while index_2 <=length:
#         rows.append(matrix[index_1][index_2])
#         index_1+=1
#         rows.append(matrix[index_1][index_2])
#         output.append(rows)
#         index_1 = 0
#         index_2 +=1
#         rows = []
#     output.reverse()
#     return output

# print(counter([[6, 7],[10, 11]],1))
# print(counter([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]],1))
    
#output
#           [7, 11],
#           [6, 10]


##------------------works with matrix of size any n x n / only 1 rotation / (no rot90)----------#

import numpy as np

# def counter(matrix, times):
#     # matrix.reverse()
#     # print(matrix)
#     length = len(matrix[0]) - 1
#     index_1 = 0
#     index_2 = 0

#     matrix = np.array(matrix)
#     rows = []
#     output = []
#     while index_2 <=length:
#         while index_1 <= length:
#             rows.append(matrix[index_1][index_2])
#             index_1+=1
#         output.append(rows)
#         index_1 = 0
#         index_2 +=1
#         rows = []
#     output.reverse()
#     return output

# # print(counter([[6, 7],[10, 11]],1))
# print(counter([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]],1))

##---------------attempt at any size matrix / any number of times / (no rot90)------------------
#           [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

#           [[4, 8, 12, 16],
#           [3, 7, 11, 15],
#           [2, 6, 10, 14],
#           [1, 5, 9, 13]])
import numpy as np

def counter(matrix, times):
    # matrix.reverse()
    # print(matrix)
    length = len(matrix[0]) - 1
    index_1 = 0
    index_2 = 0

    number = 1

    matrix = np.array(matrix)
    rows = []
    output = []
    while number <= times:
        while index_2 <=length:
            while index_1 <= length:
                rows.append(matrix[index_1][index_2])
                index_1+=1
            output.append(rows)
            index_1 = 0
            index_2 +=1
            rows = []
        output.reverse()
        matrix = output
        print(output)
        number+=1
        index_1=0
        index_2=0
        rows=[]
        output=[]

    return matrix

print(counter([[6, 7],[10, 11]],2))
# print(counter([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]],2))

# 2 times:  
#           [6, 7],
#           [10, 11]
#      (once)
#           [7, 11],
#           [6, 10]

#      (twice)
#           [11, 10],
#           [7, 6]

