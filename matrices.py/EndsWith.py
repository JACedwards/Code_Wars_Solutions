# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

#psuedo:
#  check length of ending
#  check if negative slice of -length:end = same as ending


def solution(text, ending):
    length = len(ending)
    print(text[-length:])
    return text[-length:] == ending


print(solution("samurai", "ai"))