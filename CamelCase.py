# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

# For instance:

# camelcase("hello case") => HelloCase

#Peudo:
#  Split string into list
#  Loop through list
#  Concatenate using title case for each element


def camel_case(string):
    lst = string.split()
    output = ''

    for s in lst:
        output = output + s.title()

    return output

print(camel_case("hello case"))
