# Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

# Assume: 0 <= n < 2147483647

# Examples
#        1  ->           "1"
#       10  ->          "10"
#      100  ->         "100"
#     1000  ->       "1,000"
#    10000  ->      "10,000"
#   100000  ->     "100,000"
#  1000000  ->   "1,000,000"
# 35235235  ->  "35,235,235"

#pseudo:
#   convert to string
#   loop backwards through string with counter
#   insert(()) each digit at 0 index
#   when counter gets to 3, insert comma
#   reset counter


def group_by_commas(n):

    n = str(n)
    count = 0
    output = ''

    for d in n[::-1]:
        if count == 3:
            output = f'{d},{output}'
            count = 1
        else:
            output = f'{d}{output}'
            count += 1
    return output


print(group_by_commas(35235235))