# DESCRIPTION:
# Write a function that accepts a string, and returns true if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)

# Examples:

# "(123) 456-7890"  => true
# "(1111)555 2345"  => false
# "(098) 123 4567"  => false
# REGULAR EXPRESSIONSALGORITHMS

def valid_phone_number(phone_number):

    print

    if phone_number[1:4].isnumeric() == False or phone_number[6:9].isnumeric() == False or phone_number[10:].isnumeric() == False:
        return False
    
    elif phone_number[0] != '(' or phone_number[4] != ')':
        return False

    elif phone_number[9] != '-':
        return False
    
    elif phone_number[5] != ' ':
        return False

    else:
        return True

print(valid_phone_number("(085) 125-923:"))
        