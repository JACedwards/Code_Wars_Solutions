# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    output = []

    for char in a1:
        if char not in output:
            output.append(char)
    for char2 in a2:
        if char2 not in output:
            output.append(char2)

    output.sort()
    output_string = ''.join(output)
    return output_string


print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))