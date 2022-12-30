def distinct(seq):


    return list(dict.fromkeys(seq))


print(distinct([1, 1, 1, 2, 3, 4, 5]))