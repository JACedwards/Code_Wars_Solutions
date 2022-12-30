def string_to_array(s):

    if s == '':
        output = [""]
    else:
        output = s.split()
    return output


print(string_to_array(''))