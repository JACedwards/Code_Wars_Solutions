# In this kata you have to write a method that folds a given array of integers by the middle x-times.

# An example says more than thousand words:

# Fold 1-times:
# [1,2,3,4,5] -> [6,6,3]

# A little visualization (NOT for the algorithm but for the idea of folding):

#  Step 1         Step 2        Step 3       Step 4       Step5
#                      5/           5|         5\          
#                     4/            4|          4\      
# 1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
# ----*----      ----*          ----*        ----*        ----*


# Fold 2-times:
# [1,2,3,4,5] -> [9,6]
#  0,1,2,3,4
# As you see, if the count of numbers is odd, the middle number will stay. Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

#Pseudo:

# while loop:
#   left, right pointer
#   check if even or odd, if odd, leave middle alone.


def fold_array(array, runs):
    
    count = 0
    folds = 0
    l = 0
    r = len(array)-1

    sm = 0
    while folds <runs:

        output = []
        if len(array) == 2:
            sm = array[0] + array[1]
            output.append(sm)
            return output
        elif len(array) == 1:
            output.append(array[0])
            return output

        elif len(array) % 2 != 0:
            while r-l >= 2:
                sm = array[l] + array[r]
                output.append(sm)
                sm = 0
                l+=1
                r-=1
                count +=1
            output.append(array[l])
            array = output

            l=0
            r=len(array)-1
            folds +=1
        else:
            while r-l >= 1:
                sm = array[l] + array[r]
                output.append(sm)
                sm = 0
                l+=1
                r-=1
                count +=1
            # output.append(array[l])
            array = output

            l=0
            r=len(array)-1
            folds +=1

    return output

# print(fold_array([1,2,3,4,5], 3))
print(fold_array([-9, 9, -8, 8, 66, 23], 1))


