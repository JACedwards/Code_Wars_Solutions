# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
# #Input

# A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

# #Output

# The middle character(s) of the word represented as a string.

#Pseudo:
# if only one letter,
#     return that letter
# if only two letters,
#     return both letters
# else:  check length for odd/even
# store length in variable
# if length odd divide and round up:
#     return index of that value
# if length even divide by 2:
#     return that index + next one

def get_middle(s):
    if len(s) == 1 or len(s) == 2:
        return s

    length = len(s)
    print(length)
    print(length//2)

    if length % 2 == 0:
        mid = length // 2
        return f'{s[mid-1]}{s[mid]}'
    else:
        mid = length // 2
        return f'{s[mid]}'




print(get_middle('testing'))
#'t'