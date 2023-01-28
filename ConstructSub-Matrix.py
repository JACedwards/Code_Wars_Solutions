# Simple Fun #235: Construct Submatrix

# Task
# Given a matrix, find its submatrix obtained by deleting the specified rows and columns.

# Example
# For

# matrix = [
# [1, 0, 0, 2], 
# [0, 5, 0, 1], 
# [0, 0, 3, 5]
# ]
# rowsToDelete = [1] and columnsToDelete = [0, 2]
# the output should be

#  [ [0, 2], [0, 5] ]

# conditions 1 -10

# Pseudo:
# import numpy
# convert list to array
#  loop through rows to delete, deleting from matrix at appropriate index
#  loop through cols to delete, deleting from matrix

import numpy as np

#https://note.nkmk.me/en/python-numpy-delete/

def construct_submatrix(matrix, rows_to_delete, cols_to_delete):

    #convert list of lists to numpy array
    matrix = np.array(matrix)
    
    # remove specified rows (by index), using numbers in rows_to_delete input list as indices
    matrix = np.delete(matrix, rows_to_delete, 0)      #0 = horizontal access (i.e. rows)
    
    # remove specified columns (by index), using numbers in columns_to_delete input list as indices
    matrix = np.delete(matrix, cols_to_delete, 1)      #1 = vertical access (i.e., columns)
    
    #convert from <numpy array> back to list of lists
    output = matrix.tolist()

    return output


print(construct_submatrix([[1, 0, 0, 2], [0, 5, 0, 1],[0, 0, 3, 5]], [1], [0,2]))




#_----------------Works with 2 test cases in code wars (+ cols and rows to delete at [] and len 2 each) not with some edge cases-----------------#

# def construct_submatrix(matrix, rows_to_delete, cols_to_delete):

#     if len(matrix) == 1:
#         return []
    
#     #Removing rows
#     if len(rows_to_delete) == 1:
#         matrix.pop(rows_to_delete[0])
#     elif len(rows_to_delete) > 1:
#         if len(rows_to_delete) == len(matrix):
#             matrix.clear()

#         else:
#             rows_to_delete.sort()
#             matrix.pop(rows_to_delete[0])
#             rows_to_delete.pop(0)
#             for rows in rows_to_delete:
#                 matrix.pop(rows - 1) 
#     print(matrix)
#     #Removing columns
#     if len(cols_to_delete) == 1:
#         for c in matrix:
#             c.pop(cols_to_delete[0]) #works
        
#     elif len(cols_to_delete) > 1:
#         if len(cols_to_delete) == len(matrix[0]):
#             matrix.clear() #works
        
#         else:
#             cols_to_delete.sort()

#             for r in matrix:
#                 r.pop(cols_to_delete[0])
#             cols_to_delete.pop(0)  #works
#             print(f'matrix = {matrix}')
#             print(f'cols to delete = {cols_to_delete}')
#             for ind in cols_to_delete:            
#                 for r in matrix:
#                     r.pop(ind-1) 
    
#     return matrix
    
    
# # print(construct_submatrix([[8, 9, 7, 3, 4], [7, 5, 0, 6, 1]], [], [2,3,4]))
# print(construct_submatrix([[1, 0, 0, 2], [0, 5, 0, 1],[0, 0, 3, 5]], [1], [0,2]))


#------------------works with all code wars test, with exception that some of my [] should have single populated row-----------------------#
#--------------Example, my [] should equal [[2,1,7,5,0]] or my [] should equal [[9,5]] ------------------------------------------------#

def construct_submatrix(matrix, rows_to_delete, cols_to_delete):

    # if len(matrix) == 1:
    #     return []
    
    #Removing rows
    if len(rows_to_delete) == 1:
        matrix.pop(rows_to_delete[0])
    elif len(rows_to_delete) > 1:
        if len(rows_to_delete) == len(matrix):
            matrix.clear()

        else:
            minus = 1
            rows_to_delete.sort()
            matrix.pop(rows_to_delete[0])
            rows_to_delete.pop(0)
            for rows in rows_to_delete:
                matrix.pop(rows - minus)
                minus +=1 
    print(matrix)
    #Removing columns
    if len(cols_to_delete) == 1:
        for c in matrix:
            c.pop(cols_to_delete[0]) #works
        
    elif len(cols_to_delete) > 1:
        if len(cols_to_delete) == len(matrix[0]):
            matrix.clear() #works
        
        else:
            sub = 1
            cols_to_delete.sort()

            for r in matrix:
                r.pop(cols_to_delete[0])
            cols_to_delete.pop(0)  #works
            # print(f'matrix = {matrix}')
            # print(f'cols to delete = {cols_to_delete}')
            for ind in cols_to_delete:            
                for r in matrix:
                    r.pop(ind-sub)  #still get some out of range errors here
                sub +=1
            sub = 1
    
    return matrix
    
    
print(construct_submatrix([[8, 9, 7, 3, 4], [7, 5, 0, 6, 1]], [], [2,3,4]))
# print(construct_submatrix([[1, 0, 0, 2], [0, 5, 0, 1],[0, 0, 3, 5]], [1], [0,2]))

