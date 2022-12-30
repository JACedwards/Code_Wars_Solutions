# couldn't figure this one out


# Is the string uppercase?
# Task
# Create a method to see whether the string is ALL CAPS.

# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True


def is_uppercase(inp):

    # remove_spaces = inp.replace(" ", "")

    # if remove_spaces.isalpha() == False and inp.upper() == True:
    #     return True
    # else:
    #     return False

    print(inp.isalpha())
    print(inp.isupper())
    # print(inp.islower())



print(is_uppercase("(*H"))