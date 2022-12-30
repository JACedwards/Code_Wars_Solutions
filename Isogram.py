# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

#Psuedo:  
# return true if empty string
# create empty list
# loop through string asking if letter in empty list:
#    if not, append to list
#    if it is, return false
# return true if false is never hit

def is_isogram(string):
    if string == '':
        return True
    check = []
    for c in string:
        if c.lower() not in check:
            check.append(c.lower())
        else:
            return False
    return True



print(is_isogram("Dermatoglyphics"))