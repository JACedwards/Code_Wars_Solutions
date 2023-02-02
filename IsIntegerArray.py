# Write a function with the signature shown below:

# def is_int_array(arr):
#     return True
# returns true  / True if every element in an array is an integer or a float with no decimals.
# returns true  / True if array is empty.
# returns false / False for every other input.

def is_int_array(arr):

    if arr == []:
        return True 
    
    if arr == [None]:
        return False

    for n in arr:
        if isinstance(n, int) == False and isinstance(n, float) == False:
            return False
        if isinstance(n, float) and int(n) / n != 1:
            return False

    return True



print(is_int_array(['a']))