# An AI has infected a text with a character!!

# This text is now fully mutated to this character.

# If the text or the character are empty, return an empty string.
# There will never be a case when both are empty as nothing is going on!!

# Note: The character is a string of length 1 or an empty string.

# Example
# text before = "abc"
# character   = "z"
# text after  = "zzz"

#pseudo:
# if either input = empty:
#   return empty
# store length of text
# multiply char by length?

def contamination(text, char):

    if text == '' or char == '':
        return ''

    length = len(text)
    output = ''
    output = char * length
    return output


print(contamination("abc", "z"))
