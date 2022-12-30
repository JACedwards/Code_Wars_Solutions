import string


def print_array(arr):

    string_convert = []

    for fl in arr:
        string_convert.append(str(fl))

    print(string_convert)

    return ",".join(string_convert)



print(print_array([2.0,4.2,5.1,2.2]))