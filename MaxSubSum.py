# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

#Psuedo:
    #if [], return 0
    #loop through, if every number < 0, return 0
    #loop through array, if evrery number is > 0, return sum of entire array

    #while l <= r:
        #slide through arr
        #l = 0
        #r=1
        #count_max = 0
        #check each sub_array's sum
        #increase max if greater than max
        #return max count

        
#Passed 27 tests on code wars, and then reached "Max buffer size" and "failed" 

def max_sequence(arr):
    
    if arr == []:
        return 0

    count_neg = 0
    for n in arr:
        if n < 0:
            count_neg += 1
    if count_neg == len(arr):
        return 0

    count_pos = 0
    for p in arr:
        if p > 0:
            count_pos += 1
    if count_pos == len(arr):
        return sum(arr)

    count_max = 0
    check_sum = 0
    l = 0
    r = 1
    arr.append(0)

    while r <= len(arr)-1:
        print(arr[l:r])
        check_sum = sum(arr[l:r])
        print(check_sum)
        if check_sum > count_max:
            count_max = check_sum
        r += 1
        if r == len(arr):
            l+=1
            r = l + 1
    return count_max
 

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))