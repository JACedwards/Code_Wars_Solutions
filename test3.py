def get_smallest_odd(numlist):
    oddcount = 0
    smallest = float
    for num in numlist:
        if num %2 !=0:
            oddcount +=1
            if num < smallest:

    return oddcount, smallest


print(get_smallest_odd([1,2,3,4,5]))


oddcount = 3
smallest = 1