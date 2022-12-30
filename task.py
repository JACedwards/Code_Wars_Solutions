def expression_matter(a, b, c):
    listA = []
    # listB = []
    # listC = []

    arrA1 = a * (b + c)
    listA.append(arrA1)
    arrA2 = a * b * c
    listA.append(arrA2)
    arrA3 = a + b * c
    listA.append(arrA3)
    arrA4 = (a + b) * c
    listA.append(arrA4)
    output = max(listA)
    return output




print(expression_matter(1,1,1))