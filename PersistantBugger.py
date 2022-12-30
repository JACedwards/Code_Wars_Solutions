# Write a function, persistence, that takes in a positive parameter n and returns its multiplicative persistence, which is the nber of times you must multiply the digits in n until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit nber)

# Pseudo code:

    #While length of nber <1:
        #split string version of nber into two digits
        # multiply int's of two digits
        #add to multiplicative persistence count
        #check lenght of string version of product,
            #store in length variable
    #return count

def persistence(n):

    if len(str(n)) == 1:
        return 0

    length = 2
    count = 0

    while length > 1:
        one = 1
        for d in str(n):
            one = one * int(d)
        length=len(str(one))
        count += 1
        n=one

    return count

print(persistence(39))
    