def string_clean(s):
    output_list = []
    list_s = [char for char in s]
    print(list_s)

    for n in list_s:
        if n.isnumeric():
            continue
        else:
            output_list.append(n)
    
    output = "".join(output_list)
    return output



print(string_clean("(E3at m2e2!!)"))