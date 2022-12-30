# Write a function that outputs the transpose of a matrix - a new matrix where the columns and rows of the original are swapped.

# For example, the transpose of:

# | 1 2 3 |
# | 4 5 6 |
# is

# | 1 4 |
# | 2 5 |
# | 3 6 |
# The input to your function will be an array of matrix rows. You can assume that each row has the same length, and that the height and width of the matrix are both positive

   

import numpy as np
def transpose(matrix):
    length = len(matrix[0])-1
    print(length)
    index_1 = 0
    index_2 = 0
    columns = []
    rows = []
    matrix = np.array(matrix)

    while index_2 <= length:
        columns.append(matrix[index_1][index_2])
        index_1 += 1
        columns.append(matrix[index_1][index_2])
        rows.append(columns)
        columns = []
        index_1 = 0
        index_2 +=1
    return rows, type(rows)


print(transpose([[1,2,3],[4,5,6]]))