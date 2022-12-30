# A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

# E.g.

# map1 = "abcdefghijklmnopqrstuvwxyz";
# map2 = "etaoinshrdlucmfwypvbgkjqxz";
   
# cipher = Cipher(map1, map2);
# cipher.encode("abc") # => "eta"
# cipher.encode("xyz") # => "qxz"
# cipher.encode("aeiou") # => "eirfg"
   
# cipher.decode("eta") # => "abc"
# cipher.decode("qxz") # => "xyz"
# cipher.decode("eirfg") # => "aeiou"
# If a character provided is not in the opposing alphabet, simply leave it as be.

#Psuedo:
#  make dictionary of two maps
#  loop through input
#  making new string from dictionary values and concatenation
#  (check if letter is missing)


def cipher(map1, map2, input):
    map1 = list(map1)
    map2 = list(map2)
    dict_map = {map1[i] : map2[i] for i in range(len(map1))}
    output = ''
    
    for c in input:
        if c not in map1:
            output = f'{output}{c}' 
        else:
            cipher = dict_map.get(c)
            output = f'{output}{cipher}'

    return output
        


print(cipher("abcdefghijklmnopqrstuvwxyz", "etaoinshrdlucmfwypvbgkjqxz", "aeio?"))