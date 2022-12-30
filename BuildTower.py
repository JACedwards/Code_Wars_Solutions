# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

# test.assert_equals(tower_builder(1), ['*', ])
# test.assert_equals(tower_builder(2), [' * ', '***'])
# test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****']

#Pseudo:
# stars = 1?
# length = floors * 2 - 1
# middle_index = length // 2 + 1
# spaces = length
# l-index = middle_index - 1
# r_index = middle_index + 2
#output = []
# row = ''
# while stars <= length:
#     row = f'{''* spaces}{'*'* stars}{''* spaces}'
#
#   

def tower_builder(n_floors):
    stars = 1
    length = n_floors * 2 - 1
    spaces = length // 2
    output = []
    row = ''

    while stars <= length:
        row = f"{' '* spaces}{'*'* stars}{' '* spaces}"
        output.append(row)
        spaces -= 1
        stars = stars + 2
 
    return output

print(tower_builder(6))