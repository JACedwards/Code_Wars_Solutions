def square_sum(numbers):
    output = 0
    for n in numbers:
        output += n**2
    return output 

print(square_sum([1,2,2]))