# An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

# You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

# Example
# find_missing([1, 3, 5, 9, 11]) == 7
# PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!

#Pseudo:
# loop through subtracting each number from one before it
#  collect in list
#  get count of first to items in output list
#  whichever is greater than 1, store in variable
#  loop through original list again:
#     when arrive at difference != variable
#     insert variable amount + previous index amount
# return output

#___________works only with positive numbers__________

# def find_missing(sequence):
#     dif_collector = []
#     for i in range(1, len(sequence)):
#         dif = sequence[i] - sequence[i-1]
#         dif_collector.append(dif)

#     dif_collector.sort()
#     key = dif_collector[0]

#     output = 0
#     for i in range(1, len(sequence)):
#         if sequence[i] - sequence[i-1] != key:
#             output = sequence[i-1] + key

#     return output

# print(find_missing([1,3,5,9,11]))

#---This should work with almost all inputs that are all positive and inputs that are all negative or mixture of negative/positive___________


def find_missing(sequence):
    if sequence[-1] < 0:
        sequence = [abs(x) for x in sequence]
        sequence.sort()
        print(sequence)
        
        dif_collector = []
        for i in range(1, len(sequence)):
            dif = sequence[i] - sequence[i-1]
            dif_collector.append(dif)

        dif_collector.sort()
        key = dif_collector[0]

        output = 0
        for i in range(1, len(sequence)):
            if sequence[i] - sequence[i-1] != key:
                output = sequence[i-1] + key
        # output = output * -1
        return -output

    else:
        dif_collector = []
        for i in range(1, len(sequence)):
            dif = sequence[i] - sequence[i-1]
            dif_collector.append(dif)

        dif_collector.sort()
        key = dif_collector[0]

        output = 0
        for i in range(1, len(sequence)):
            if sequence[i] - sequence[i-1] != key:
                output = sequence[i-1] + key

        return output

print(find_missing([-3, -1, 1, 3, 7]))