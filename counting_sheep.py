from itertools import count


def count_sheeps(sheep):

    c = 0

    for lamb in sheep:
        if lamb == None:
           c = c
        elif lamb == True:
            c = c + 1
        elif lamb == False:
            c = c
        else:
            c = c
    return c

print(count_sheeps([True, None, True, True, b]))