# Given a variable n,

# If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

# If n is not an integer, return the string "None".

# Ex:

# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'

#Psuedo:
# turn n into string
# for loop through n:
#     if n = odd
#        replace n with -n-
#     else:  replace n with itself
# when finished, strip any leading or end "-"

def dashatize(n):
    n = str(n)
    output = ''

    for c in n:
        if int(c) % 2 == 0:
            output = f"{output}{str(c)}"
        else:
            output = f"{output}-{str(c)}-"
    if output[0] == '-':
        output = output.replace('-', '', 1)
    
    length = len(output)-1
    if output[length] == '-':
        output = output[:length]
    
    return output


print(dashatize(92747))