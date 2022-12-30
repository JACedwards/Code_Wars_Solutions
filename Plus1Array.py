# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.

# Examples
# Valid arrays

# [4, 3, 2, 5] would return [4, 3, 2, 6]
# [1, 2, 3, 9] would return [1, 2, 4, 0]
# [9, 9, 9, 9] would return [1, 0, 0, 0, 0]
# [0, 1, 3, 7] would return [0, 1, 3, 8]

# Invalid arrays

# [1, -9] is invalid because -9 is not a non-negative integer

# [1, 2, 33] is invalid because 33 is not a single-digit integer

#Pseudo:
# check if input is valid (is a number and is greater than -1)
# if so, join list, which = string I think
# add 1 to int() version of string
# loop through string, appending int versions to output list.

#Note: this worked fine in VS Code.  Timed out in CodeWars Test.  
# Didn't make sense because said taking more than 12,000 ms, 
# but only took VS Code 113 ms.

def up_array(arr):

    for l in arr:
        if len(str(l)) > 1 or l < 0:
            return None
    
    arr_sts = []
    for d in arr:
        arr_sts.append(str(d))

    arr_string = ''.join(arr_sts)
    print(arr_string, type(arr_string))

    output = []

    flag = True
    while flag == True:
        for n in arr_string:
            if n == '0':
                output.append(int(n))
            if n == '0':
                flag = False
    print(output, type(output))
                

    int_str = int(arr_string) + 1
    int_str = str(int_str)

    for c in int_str:
        output.append(int(c))

    return output



print(up_array([1, 2, -3]))
