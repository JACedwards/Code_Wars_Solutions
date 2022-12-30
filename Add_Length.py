# Problem to Solve:  What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Examples:
# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"] 

#  1. Determine length of each string
#  2. Add lenth immediately after each string

# Split single string into list of individuals
# Loop through list counting each individual string's length.
# concatenate string with its length Inter 


str_1 = "you will win"
str_2 = ""

def add_length(str_):
    
    lslist = []
    split_string = str_.split()
    for x in split_string:
        l = len(x)
        lslist.append(x + ' ' + str(l))
        
    return lslist





print(add_length(str_1))