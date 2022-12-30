# The objective of this Kata is to write a function that creates a dictionary of factors for a range of numbers.

# The key for each list in the dictionary should be the number. The list associated with each key should possess the factors for the number.

# If a number possesses no factors (only 1 and the number itself), the list for the key should be ['None']

# The function possesses two arguments (n and m). Where n is the starting number and m is the ending number.

# For example: All factors for 2 (n) through to 6 (m) with the number being the key in the dictionary:
#  2, 3, 4, 5, 6
#  2- 

# {2: ['None'], 3: ['None'], 4: [2], 5: ['None'], 6: [2, 3]}

def factorsRange(n, m):

    output = {}
    for i in range(n, m+1):
        #2,3,4,5,6

        check_lst = []
        for j in range(2,i):
            if i % j == 0:
                check_lst.append(j)
        output[i] = check_lst
        check_lst=[]

    for k,v in output.items():
        if v == []:
            output[k] = ['None']

    return output
            


print(factorsRange(2,6))
# {2: ['None'], 3: ['None'], 4: [2], 5: ['None'], 6: [2, 3]}