# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

def parse(data):

    output = []
    count = 0
    
    for c in data:
        if c == 'i':
            count += 1
        elif c == 'd':
            count -= 1        
        elif c == 's':
            count = count**2
        elif c == 'o':
            output.append(count)
    return output


print(parse("codewars"))