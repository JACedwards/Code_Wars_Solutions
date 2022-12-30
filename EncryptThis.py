#Below works for string where words are 3 or more letters long, but not for 1 or 2 letters.and
# <><>refactor to care for words that are 1 or 2 letters long 
# 
# 
# Description:
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

#Psuedo:  do with single item list, then for multi-items
# create dictionary of ascii characters
#store ascii for first character in a variable
#store last letter of string in a variable
#store second letter of string in a variable
#store index of last letter in a variable
#loop through indices of one-word string:
#  if 0 replace with ascii
#  if 1 replace with final letter
#  if final index replace with second letter
#  else: concatinate letter with no changes
import string

def encrypt_this(text):

    dct =  {c: ord(c) for c in string.ascii_uppercase} | {c: ord(c) for c in string.ascii_lowercase}
    
    text_lst = text.split()

    output = ''
    output_lst = []

    for word in text_lst:
        if len(word) == 1:
            output = f'{dct.get(word[0])}'
            output_lst.append(output)
            output = ''

        elif len(word) == 2:
            output = f'{dct.get(word[0])}{word[1]}'
            output_lst.append(output)
            output = ''
        else:
            first = word[0]
            second = word[1]
            last = word[-1]
            last_ind = len(word) -1 

            for i in range(len(word)):
                if i != 0 and i!= 1 and i != last_ind:
                    output = f'{output}{word[i]}'
                elif i == 0:
                    output = f'{output}{dct.get(first)}'
                elif i == 1:
                    output = f'{output}{last}'
                else:
                    output = f'{output}{second}'
            output_lst.append(output)
            output = ''

    output_final = ' '.join(output_lst)
    return output_final


    



print(encrypt_this("A wise old owl lived in an oak"))    