# There are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values. Write a function createDict(keys, values) that returns a dictionary created from keys and values. If there are not enough values, the rest of keys should have a None (JS null)value. If there not enough keys, just ignore the rest of values.

# Example 1:

# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
# Example 2:

# keys = ['a', 'b', 'c']
# values = [1, 2, 3, 4]
# createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}

#Pseudo:
# compare length of lists
#  if keys > values:
#    alter values to add 'None" for missing values

#dictionary comprehension

# def createDict(keys, values):

#     if len(keys) > len(values):
#         l_keys = len(keys)
#         l_values = len(values)
#         while l_values <= l_keys:
#             values.append(None)
#             l_values +=1

#     output = {k:v for (k,v) in zip(keys,values) }
#     return output


# print(createDict(keys = ['a', 'b', 'c', 'd'], values = [1, 2, 3]))

#without dict comprehension

# def createDict(keys, values):

#     if len(keys) > len(values):
#         l_keys = len(keys)
#         l_values = len(values)
#         while l_values <= l_keys:
#             values.append(None)
#             l_values +=1

#     output = {}
#     for i in range(len(keys)):
#         for j in range(len(values)):
#             if i == j:
#                 output[keys[i]] = values[j]

#     return output


# print(createDict(keys = ['a', 'b', 'c', 'd'], values = [1, 2, 3]))


#w/ zip and simplified while:

def createDict(keys, values):

    while len(values) <= len(keys):
            values.append(None)

    output = dict(zip(keys,values))

    return output


print(createDict(keys = ['a', 'b', 'c', 'd'], values = [1, 2, 3]))