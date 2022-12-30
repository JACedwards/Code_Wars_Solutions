def sum_array(arr):
    if arr == []:
        return 0
    if len(arr) == 1:
        return 0
    if arr == None:
        return 0
    
    x = max(arr)
    y = min(arr)

    arr.remove(x)
    arr.remove(y)

    output = sum(arr)

    return(output)

    
    
    
    
print(sum_array([None]))