# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
# # * 'abcdefg' => ['ab', 'cd', 'ef', 'g_']

#pseudo:
    #check for even/odd length
    #if odd, make slice that doesnt include final character
    #store final character in variable
    #loop through string, creating 2 character substrings and adding to list
    #if odd, add final stored character with "_" at end

#C's original works:

# def solution(s):
    # odd = False

    # if len(s) % 2 != 0:
    #     last = s[-1]
    #     s = s[:len(s)-1]
    #     odd = True
    # output=[]
    
    # for i in range(0, len(s), 2):
    #     output.append(s[i:i+2])
    
    # if odd:
    #     output.append(f"{last}_")
    
    # return output

# print(solution('abcdef'))



def solution(s):
 
    if len(s) % 2 != 0:
        s += '_'

    output = [s[i:i+2] for i in range(0, len(s), 2) ]
    
    return output

print(solution('abcdefg'))