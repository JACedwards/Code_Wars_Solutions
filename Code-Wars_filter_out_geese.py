
def goose_filter(birds):
    output = []
    a = "African"
    r = "Roman Tufted"
    t = "Toulouse"
    p = "Pilgrim"
    s = "Steinbacher"
    

    for n in birds:
        if n == a or n == r or n == t or n == p or n == s:
            output = output
        # if n.lower() == a or n.lower() == r or n.lower() == t or n.lower() == p or n.lower() == s:
        #     output = output
        else:
            output.append(n)

    return output



print(goose_filter(['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']))