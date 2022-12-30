# Complete the solution so that it takes the object (JavaScript/CoffeeScript) or hash (ruby) passed in and generates a human readable string from its key/value pairs.

# The format should be "KEY = VALUE". Each key/value pair should be separated by a comma except for the last pair.

# Example:

# solution({"a": 1, "b": '2'}) # should return "a = 1,b = 2"

#Psuedo:
# loop through dictionary
# concatinate key + = value + comma
# strip final comma

def solution(pairs):

    concat = ''
    lst = []

    for k, v in pairs.items():
        concat = f"{k} = {v},"
        lst.append(concat)

    lst.sort()
    string = ''

    for w in lst:
        string = f'{string}{w}'
    print(string)

    output = string[:-1]

    return output



print(solution({'b': 8, 2: -5, 'y': 2}))

#should be:
#           '2 = -5,b = 8,y = 2'
#got:       'b = 8,2 = -5,y = 2'

