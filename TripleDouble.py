# Write a function

# triple_double(num1, num2)
# which takes numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.

# If this isn't the case, return 0

# Examples



def triple_double(num1, num2):

    triple = 0
    num1 = str(num1)

    for n in num1:
        count = num1.count(n)
        if count >= 3:
            triple = int(n)
            print(triple)
            break

    if f'{n}{n}' in str(num2) and f'{n}{n}{n}' in str(num1):
        return 1
    else:
        return 0



print(triple_double(10560002, 100))