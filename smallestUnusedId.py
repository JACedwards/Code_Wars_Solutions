def next_id(arr):
    if arr == []:
        return 0
    if 0 not in arr:
        return 0
    arr.sort()
    arr = set(arr)
    arr = list(arr)

    

    if len(arr) == arr[-1] + 1:
        return arr[-1] + 1

    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]>1:
            return arr[i] +1




print(next_id([1,2,3]))