# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# Based on: http://oj.leetcode.com/problems/two-sum/

# two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]

#Psuedo:  to avoid O(^2) via looping...
# slide through numbers
# checking sum of each pair against target
# return index of first pair that == target

def two_sum(numbers, target):

    l = 0
    r = 1
    output = []


    while r <= len(numbers) - 1:
        if numbers[l] + numbers[r] == target:
            output.append(l)
            output.append(r)
            return output
        if r == len(numbers) - 1:
            l+=1
            r = l + 1
        else:
            r += 1
    
print(two_sum([1234,5678,9012], 14690))