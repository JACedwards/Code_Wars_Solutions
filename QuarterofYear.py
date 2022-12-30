def quarter_of(month):

    if month < 4:
        return 1
    elif month < 7:
        return 2
    elif month < 10:
        return 3
    else:
        return 4

print(quarter_of(12))