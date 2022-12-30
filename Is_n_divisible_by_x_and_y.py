def is_divisible(n,x,y):

    if n % x == 0 and n % y == 0:
        output = True

    else:
        output = False

    return output

print(is_divisible(100,5,3))