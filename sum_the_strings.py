# Example: (Input1, Input2 -->Output)

# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"
# Notes:

# If either input is an empty string, consider it as zero.

# Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)

def sum_str(a, b):

    if a == '':
        a = '0'
    if b == '':
        b = '0'


    int_sum = int(a) + int(b)
    return str(int_sum)


print(sum_str("34", ""))