def positive_sum(arr):
    positive = 0
    
    for num in arr:
        if num >= 0:
            positive = positive + num
        else:
            continue
            
    return positive

print(positive_sum([2,0,4,-5]))
