# Given a list of rows of a square matrix, find the product of the main diagonal.

# Examples:

# main_diagonal_product([[1,0],[0,1]]) => 1

# main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]) => 45

#Psuedo:
#import numpy
#change to array
#while loop:
#index = 0
#lenght = len(array)-1
#sum = 0
#loop through lists
#add number at appropriate index
#index+=1
#return sum
import numpy as np

def main_diagonal_product(mat):
    length = len(mat)-1
    index = 0
    sum = 1
    mat = np.array(mat)
    print(mat)

    for n in mat:
        sum = sum * n[index]
        index +=1
    return sum


print(main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]))
