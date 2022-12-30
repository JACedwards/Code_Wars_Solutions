def count_sheep(n):
    output = ''
    x = range(n+1)

    for num in x:
        if num == 0:
            continue
        else: 
            output = output + f"{num} sheep..."
        
    return(output)


print(count_sheep(3))