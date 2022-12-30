def powers_of_two(n):
    powers = 0
    output = []

    while len(output) <= n:
        output.append(2**powers)
        powers +=1

    return output
    



print(powers_of_two(2))
