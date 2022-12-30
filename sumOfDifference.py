def sum_of_differences(arr):
    ordered = sorted(arr, reverse=True)
    print(ordered)
    pointer=0
    diff=0

    sum=0

    # while pointer < len(ordered)-1:
    for i in range(len(ordered)-1):
        print(i)
        if i <= len(ordered)-1:
            print(i)
            if i+1 > len(ordered):
                break
            else:
                diff=ordered[i]-ordered[i+1]
                sum=sum+diff
                pointer+=1
        
    return(diff)
    


    



sum_of_differences([1,2,10])  