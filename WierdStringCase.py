# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

#psuedo code:

#split into list
# loop through list:
#    loop through indices of each string in the list:
#        if indice = even, capitalize
#        else lowercase
# join list back into string

# O[n**2] time complexity for first one

# def to_weird_case(words):

#     words = words.split()

#     output = []
#     for word in words:
#         sub_output = ''
#         for i in range(len(word)):
#             if i == 0:
#                 sub_output = f'{sub_output}{word[i].upper()}'
#             elif i % 2 == 0:
#                 sub_output = f'{sub_output}{word[i].upper()}'
#             else:
#                 sub_output = f'{sub_output}{word[i].lower()}'
#         output.append(sub_output)
#         sub_output = ''
    
#     output = ' '.join(output)
#     return output


# print(to_weird_case('Weird string case'))

#attempting O(n) time complexity

def to_weird_case(words):

    ind = 0

    output = ''
    for c in words:
        if c == ' ':
            output = f'{output} '
            ind = 0
        elif ind == 0:
            output = f'{output}{c.upper()}'
            ind += 1
        elif ind % 2 == 0:
            output = f'{output}{c.upper()}'
            ind += 1
        else:
            output = f'{output}{c.lower()}'
            ind += 1
   
    return output


print(to_weird_case('Weird string case'))