# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

#psuedo:
    #check to see if first to indices are the same:
    #if so, that is the non-unique and can loop through
        #comparing each item to non-unique
        #return first that != non-unique

# def find_uniq(arr):

#     non_u = 0
#     if arr[0] == arr[1]:
#         non_u = arr[0]
#         for n in arr:
#             if n != non_u:
#                 return n  
#     else:
#         if arr[0] == arr[2]:
#             n = arr[1]
#             return n
#         else:
#             n = arr[0]
#             return n

# print(find_uniq([ 2,1, 1, 1, 1, 1 ]))

def find_uniq(arr):

    st = set(arr)
    lst = list(st)

    count = arr.count(lst[0])

    if count == 1:
        return lst[0]
    return lst[1]



print(find_uniq([2, 0, 0, 0 ]))