# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

class Code():

    def __init__(self, st):
        self.st = st

    def encode(self):

        code_d = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
        vowel_l = ['a', 'e', 'i', 'o', 'u']
        output = ''

        for c in self.st:
            if c in vowel_l:
                d = code_d.get(c)
                output = output + d
            else:
                output = output + c
        return output    
        

    def decode(self):
        code_d = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
        code_d_rev = {}
        output_2 = ''
        self.st = self.encode()

        for k,v in code_d.items():
            code_d_rev[v] = k
        
        for n in self.st:
            if n.isnumeric():
                letter = code_d_rev.get(n)
                output_2 = output_2 + letter
            else:
                output_2 = output_2 + n
        return output_2

test1 = Code('hello')

print(test1.decode())


# def encode(st):

#         code_d = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
#         vowel_l = ['a', 'e', 'i', 'o', 'u']
#         output = ''

#         for c in st:
#             if c in vowel_l:
#                 d = code_d.get(c)
#                 output = output + d
#             else:
#                 output = output + c
#         return output    
        
# print(encode('hi there'))


# def decode(st):
#     code_d = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
#     code_d_rev = {}
#     output_2 = ''

#     for k,v in code_d.items():
#         code_d_rev[v] = k
    
#     for n in st:
#         if n.isnumeric():
#             letter = code_d_rev.get(n)
#             output_2 = output_2 + letter
#         else:
#             output_2 = output_2 + n
#     return output_2

# print(decode('h2ll4'))