def to_alternating_case(string):

    output = ''
    
    for n in string:
        if n == n.lower():
            n = n.upper()
            output = output + n
        elif n == n.upper():
            n = n.lower()
            output = output + n
        else:
            continue

    return output

print(to_alternating_case("hello world"))

