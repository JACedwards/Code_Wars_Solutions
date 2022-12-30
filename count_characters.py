# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):

    output = {}

    if string == '':
        return output

    st = set(string)

    for c in st:
        output[c] = string.count(c)

    return output


print(count('aba'))