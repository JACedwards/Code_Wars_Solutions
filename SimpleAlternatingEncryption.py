# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.

#Psuedo code:
#  if s is empty, return s
# n < 0, return s
# loop through indices of S, building two strings
# one for odd / one for even
# concatenate the even onto the end of the odd
# then figure out how to do "n" times

# def encrypt(text, n):
    
#     odds = ''
#     evens = ''
#     output = ''
#     output_list = []
#     count = 0

#     while count <= n:
#         for i in range(len(text)):
#             if int(text[i]) % 2 != 0:
#                 odds = f'{odds}{text[i]}'
#             else:
#                 evens = f'{evens}{text[i]}'
#         output = f'{odds}{evens}'
#         output_list.append(output)
#         odds = ''
#         evens =''
#         count += 1
    
#     return output_list

# print(encrypt("012345", 2))
# "135024"

#decrypt:

# def encrypt(text, n):
    
#     odds = ''
#     evens = ''
#     output = ''
#     output_list = []
#     count = 0

#     while count <= n:
#         for i in range(len(text)):
#             if int(text[i]) % 2 != 0:
#                 odds = f'{odds}{text[i]}'
#             else:
#                 evens = f'{evens}{text[i]}'
#         output = f'{odds}{evens}'
#         output_list.append(output)
#         odds = ''
#         evens =''
#         count += 1
    
#     return output_list

def decrypt(text,n):

    half_length = int(len(text) / 2)
    print(half_length)
    odds = text[0:half_length]
    evens = text[half_length:] 
    # odds = list(odds) #135
    # evens = list(evens) #024

    output = ''
    for i in range(len(odds)):
        output = f"{output}{evens[i]}"
        output = f"{output}{odds[i]}"

    return output

    






print(decrypt("135024", 1))
#"012345"
