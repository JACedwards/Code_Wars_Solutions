def merge_arrays(arr1, arr2):

    merge = arr1 + arr2
    mergeset = set(merge)
    
    return sorted(mergeset)



print(merge_arrays([1, 3, 5, 7, 9], [10, 8, 6, 4, 2]))