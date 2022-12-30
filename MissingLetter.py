# Write a method that takes an charsay of consecutive (increasing) letters as input and that returns the missing letter in the charsay.

# You will always get an valid charsay. And it will be always exactly one letter be missing. The length of the charsay will always be at least 2.
# The charsay will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

#pseudo:
    # find index of chars[0] in abc
    # slide through abc
    # checking for equality
    # if not equality
    # return chars at that index

def find_missing_letter(chars):
    
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if chars[0] in abc:
        case = 'lower'
    else:
        case = 'upper'
        

    l = abc.index(chars[0].lower())
    for c in chars:
        if c.lower() != abc[l]:
            if case == 'lower':
                return abc[l]
            else:
                return abc[l].upper()
        else:
            l+=1

print(find_missing_letter(['O','Q','R','S']))
