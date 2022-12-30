def abbrev_name(name):

    print(name.title())
    output = ''

    for n in name.title():
        if n == n.upper():

            output = f"{output}.{n}"
        else:
            continue

    x = output.replace(' ', '')

    x = x.replace('.', '')

    x = x[0] + "." + x[1]

    return x

print(abbrev_name('patrick feenan'))