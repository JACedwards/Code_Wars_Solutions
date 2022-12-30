def simple_multiplication(number):

    if number % 2 == 0:
        output = number * 8
    else:
        output = number * 9

    return output

print(simple_multiplication(3))