def double_char(s):
    output = []
    split = [char for char in s]
    print(split)
    for c in split:
        output.append(c)
        output.append(c)


    return ''.join(output)



print(double_char("String"))