def array_plus_array(arr1,arr2):

    output1 = 0
    output2 = 0
  
    for n in arr1:
        output1 = output1 + n

    for n in arr2:
        output2 = output2 + n

    answer = output1 + output2

    return answer


print(array_plus_array([1,2,3], [4,5,6]))