# DESCRIPTION:
# Write a small function that returns the values of an array that are not odd.

# All values in the array will be integers. Return the good values in the order they are given.

def no_odds(values):

    # output = []

    # for n in values:
    #     if n % 2 == 0:
    #         output.append(n)

    # output = [x for x in values if x % 2 ==0]

    return [x for x in values if x % 2 ==0]

    # return output

print(no_odds([0, 1, 2, 3]))