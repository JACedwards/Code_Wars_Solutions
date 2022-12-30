def no_space(x):
    output = x

    for char in x:
        if char == ' ':
            output = output.replace(char, '')
        else:
            continue

    return output

print(no_space('James Allyn Craig Edwards '))