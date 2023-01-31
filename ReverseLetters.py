# Given a string str, reverse it and omit all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.

# [output] a string

# def reverse_letter(string):

#     sub_ouput = string[::-1]
    
#     output = []
#     for c in sub_ouput:
#         if c.isalpha():
#             output.append(c)
    
#     output = ''.join(output)
#     return output



# print(reverse_letter("ultr53o?n"))

#List comprehension version - one-liner:

# def reverse_letter(string):

    
    
#     # output = ''.join([x for x in string[::-1] if x.isalpha()])

#     return ''.join([x for x in string[::-1] if x.isalpha()])



# print(reverse_letter("ultr53o?n"))


#strings only
def reverse_letter(string):

    output=''
    for c in string:
        if c.isalpha():
            output = f'{c}{output}'

    return output



print(reverse_letter("ultr53o?n"))