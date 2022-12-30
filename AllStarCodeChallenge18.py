def str_count(strng, letter):

    strng = strng.lower()
    letter = letter.lower()
    
    output = strng.count(letter)
    
    return output



print(str_count("", "o"))