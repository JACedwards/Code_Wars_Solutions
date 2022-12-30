def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0

    if arr == None:
        output = []
        return output
        
    if arr == []:
        output = []
        return output
    else:
        for n in arr:
            if n > 0:
                pos = pos + 1
            elif n < 0:
                neg = neg + n

        output = [pos, neg]
        return output

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))