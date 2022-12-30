# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

#Psuedo:
#Loop through string
#count = 0
#Use f string to:
#  start each section with capital
#  add multiple of count lower case
#  add hyphen
#  increase count by one
# strip last hyphen at end

def accum(s):

    count = 1

    output = f'{s[0].upper()}-'
    
    for c in s[1:]:
        output = f'{output}{c.upper()}{c.lower() * count}-'
        count+=1

    return output[:-1]



print(accum("RqaEzty"))