def remove_char(s):
    y = list(s)
    y.remove(y[0])
    y.pop()
    string = ''
    for x in y:
        string += '' + x
    return string

print(remove_char('stupid'))
