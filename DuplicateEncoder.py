# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

#pseudo:
    #loop through string
    #check count of char
    #if count == 1:
        #insert "("
    #else:
        #insert ")"

def duplicate_encode(word):

    output = ''
    word = word.lower()
    for c in word:
        if word.count(c) == 1:
            output = f"{output}("
        else:
            output = f"{output})"
    
    return output

print(duplicate_encode('(( @'))