# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

#psuedo:
#split into list
# loop through appending to another list in int form
# min()
# max()
# concat

#version using min()/max()

# def high_and_low(numbers):

#     lst_strs = numbers.split(' ')
    
#     lst_int = []
#     for s in lst_strs:
#         lst_int.append(int(s))

#     minimum = min(lst_int)
#     maximum = max(lst_int)

#     output = ''
#     output = f'{str(maximum)} {str(minimum)}'

#     return output, type(output)    
    

# print(high_and_low("1"))

#sliding window version:

def high_and_low(numbers):

    lst_int = [int(s) for s in numbers.split(' ')]
    # print(lst_int)

    minimum = 0
    maximum = 0

    for i in range(len(lst_int)):
        if i == 0:
            minimum = lst_int[i]
            maximum = lst_int[i]
        else:
            # print(f'this is lst_int[i]: {lst_int[i]}')
            if lst_int[i] < minimum:
                minimum = lst_int[i]
                # print(f'this is min: {minimum}')
            elif lst_int[i] > maximum:
                maximum = lst_int[i]
                # print(f'this is max: {maximum}')

    output = ''
    output = f'{maximum} {minimum}'

    return output, type(output)    
    

# print(high_and_low("1 9 3 4 -5"))
print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"

