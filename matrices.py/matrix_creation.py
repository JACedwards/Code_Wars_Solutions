# Create an identity matrix of the specified size( >= 0).

# Some examples:

# (1)  =>  [[1]]

# (2) => [ [1,0],
#          [0,1] ]

#        [ [1,0,0,0,0],
#          [0,1,0,0,0],
# (5) =>   [0,0,1,0,0],
#          [0,0,0,1,0],
#          [0,0,0,0,1] ]   

#Psuedo:
#  if 0 return []
#  if 1 return [1]
#  else:
#   create array the length of n
#   create count variable
#   # loop through indices,
    #  if i = count variable
    #  insert 1
    #  else: continue
    #append list to master
    #  count +=1
    # repeat
#     #return master

# import numpy as np

# def get_matrix(n):
#     if n == 0:
#         return []
#     if n == 1:
#         return [[1]]
#     else:
#         output = []
#         count = 0
#         zero_matrix = np.full((n,n), 0)
#         print(zero_matrix)
#         print(zero_matrix)
#         for l in zero_matrix:  #l = one list in master [0,0]
#             l[count] = 1
#             output.append(l)
#             count +=1
#         #outputs in matrix formatting
#         output2 = np.array(output)
#         return output2
            

# print(get_matrix(5))

#---sam helped me fix the same slot in memory problem in this version using the adjustments in for d loop at 68-69

def get_matrix(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    else:
        output_lst = []
        output = []
        count = 0
        zero_matrix = []
        lst_zero = [0]*n
        for d in range(n):
            zero_matrix.append(lst_zero.copy())
        print(zero_matrix)

        for l in zero_matrix:
            l[count] = 1
            output.append(l)
            count +=1
        return output

print(get_matrix(5))

#version without numpy, but buiding matrix as I go, not empty matrix first

def get_matrix(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    else:
        output_lst = []
        output = []
        count = 0

        while count <= n-1:
            row = [0]*n
            row[count] = 1
            print(row)
            output.append(row)
            count += 1
        return output

print(get_matrix(5))  





