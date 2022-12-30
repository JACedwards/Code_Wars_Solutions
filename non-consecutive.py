
def first_non_consecutive(arr):
   
    for n in range(len(arr)-1):
        if arr[n+1] - arr[n] == 1:
            continue
        elif arr[n+1] - arr[n] != 1:
            return arr[n+1] 
        else:
            return None


print(first_non_consecutive([1,2,3,4,6,7,8]))