# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */

#Psuedo:
#create range from 2 to num
#loop through range from 2 to num
# if num % any number in range != 0:
#return false

def is_prime(num):

    if num < 0:
        return False

    if num == 0 or abs(num) == 1:
        return False

    for i in range(2, abs(num)):
        print(i)
        print(abs(num)%i)
        if abs(num) % i == 0:
            return False
        else:
            continue

    return True

print(is_prime(-5))

# for i in range (2,7):
#     print(i)