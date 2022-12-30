def find_difference(a, b):

    a = a[0] * a[1] * a[2]

    b = b[0] * b[1] * b[2]

    if b > a:
        return b-a
    else:
        return a-b



print(find_difference([2, 2, 3], [5, 4, 1]))