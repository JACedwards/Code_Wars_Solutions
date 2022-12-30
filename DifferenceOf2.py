# The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

# The result array should be sorted in ascending order of values.

# Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

# Examples
# [1, 2, 3, 4]  should return [(1, 3), (2, 4)]

# [4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

# [1, 23, 3, 4, 7] should return [(1, 3)]

# [4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]

#Psuedo:
# sort list in ascending order (to help with output being in ascending order)
# #add random character to end of list to avoid index out of range 
# While loop:
#  Slide through list until left pointer = length of list -1
#  Check if each pair has difference of abs(2):
#     If so, append to a list:
#         turn list into tuple
#         append tuple to output list
#         set check list to = []



def twos_difference(lst):

    lst.sort()
    lst.append(100)

    l=0
    r=1
    sum = 0
    check = []
    output = []
    print(f"length of list for 'l' target is {len(lst)-3}")
    while l <= len(lst)-3:
        
        sum = lst[l] - lst[r]
        if abs(sum) == 2:
            check.append(lst[l])
            check.append(lst[r])
            check = tuple(check)
            output.append(check)
            check=[]
            if r > len(lst) - 2:
                print(f"length of list for 'r' target is {len(lst)-1}")
                l+=1
                r = l+1
            else:
                r+=1
        if abs(sum) != 2:
            if r > len(lst) - 2:
                l+=1
                r = l+1
            else:
                r+=1
    return output

print(twos_difference([4, 3, 1, 5, 6]))