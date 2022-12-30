# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    
    #loop through s, using a counter for positives 
    # multiplying negatives
    #ignoring 0
    output = []
    p_count = 0
    n_sum = 0

    if arr == []:
        return []

    for c in arr:
        if c > 0:
            p_count += 1
        elif c < 0:
            n_sum = n_sum + c
        else:
            continue

    output.append(p_count)
    output.append(n_sum)
    return output




print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))