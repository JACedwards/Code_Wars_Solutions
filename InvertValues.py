def invert(lst):

    output = []
    for n in lst:
        n = n*-1
        output.append(n)
    return output

print(invert([-1,-2,-3,-4,-5]))