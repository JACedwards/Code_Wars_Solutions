# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

#Psuedo code:
# return false if length = 1
# remaining = string
# loop through string:
# check for closure of each type of brace
# if not present: return false
# else:
#   find index of closure
#   remove closure bracket from "remaining" list by index
#
#
#
# #------------this version works for many versions except for side-by sides (){}  and embeddeds ({})
# def valid_braces(string):

#     if len(string) == 1:
#         return False
#     if len(string) % 2 != 0:
#         return False

#     #([{}])
#     remaining = string
#     for i in range(len(string)):
#         print(remaining)
#         #()[]
#         if string[i] == '(':
#             if ')' not in remaining:
#                 return False
#             else:
#                 indices = [i for i, x in enumerate(remaining) if x == ")"]
#                 last_index = indices[-1]
#                 #last_index = 1
                
#                 if ((last_index - (i+1)) % 2) <= 0:
#                     #1-3
#                     remaining = f'{remaining[2:]}'
#                 elif ((last_index - (i+1)) % 2) != 0:
#                     return False
                    
#                 else:
#                     if last_index == len(remaining)-1:
#                         remaining = f'{remaining[:last_index]}'
#                     else:
#                         remaining = f'{remaining[:last_index]}{remaining[last_index+1:]}'
                
#         elif string[i] == '[':
#             if ']' not in remaining:
#                 return False
#             else:
#                 indices = [i for i, x in enumerate(remaining) if x == "]"]
#                 last_index = indices[-1]
#                 if ((last_index - (i+1)) % 2) <= 0:
#                     remaining = f'{remaining[2:]}'
#                 elif ((last_index - (i+1)) % 2) != 0:
#                     return False
                    
#                 else:
#                     if last_index == len(remaining)-1:
#                         remaining = f'{remaining[:last_index]}'
#                     else:
#                         remaining = f'{remaining[:last_index]}{remaining[last_index+1:]}'
#         elif string[i] == '{':
#             if '}' not in remaining:
#                 return False
#             else:
#                 indices = [i for i, x in enumerate(remaining) if x == "}"]
#                 #"{}()[]"
#                 #[1]
#                 last_index = indices[-1]
#                 #[0]
#                 #0 - 1
#                 if ((last_index - (i+1)) % 2) <= 0:
#                     remaining = f'{remaining[2:]}'
#                     print(remaining)
#                 elif ((last_index - (i+1)) % 2) != 0:
#                     return False
                    
#                 else:
#                     if last_index == len(remaining)-1:
#                         remaining = f'{remaining[:last_index]}'
#                     else:
#                         remaining = f'{remaining[:last_index]}{remaining[last_index+1:]}'
#         else:
#             remaining = f'{remaining[1:]}'
        
#     return True

# print(valid_braces("([{}])"))



#------------this version works  with a while loop, and is working for (), but not much else, for [{{] seems to be endless while loop ------

# def valid_braces(string):

#     if len(string) == 1:
#         return False
#     if len(string) % 2 != 0:
#         return False

#     #([{}])
#     string = list(string)
#     remaining = string

#     while len(remaining) >= 1:

#         if  remaining[0] == ')' or remaining[0] == '}' or remaining[0] == ']':
#             return False

#         elif remaining[0] == '(':
#             if ')' not in remaining:
#                 return False
#             elif remaining[1] == ')':
#                 if len(remaining) == 2:
#                     return True
#                 else:
#                     remaining = remaining[2:]
#             else:
#                 indices = [i for i, x in enumerate(remaining) if x == ")"]
#                 print(indices)
#                 last_index = indices[-1]
#                 print(last_index)
#                 #last_index = 3
                

#                 if ((last_index - (1)) % 2) != 0:
#                     print('hitting if 1 pf ()')
#                     print(f'there is an odd number: {remaining}')
#                     return False

#                 elif ((last_index - (1)) % 2) == 0:
#                     print('hitting elif 1 of ()')
#                     remaining.pop(last_index)
#                     remaining.pop(0)
#                     print(remaining)

#                 # this would deal with if %2 < 0    
#                 # else:
#                 #     if last_index == len(remaining)-1:
#                 #         remaining = f'{remaining[:last_index]}'
#                 #         print('hitting else-if')
#                 #     else:
#                 #         remaining = f'{remaining[:last_index]}{remaining[last_index+1:]}'
#                 #         print('hitting else-else')                    

                    
#         elif remaining[0] == '[':
#             if ']' not in remaining:
#                 return False
#             elif remaining[1] == ']':
#                 if len(remaining) == 2:
#                     return True
#                 else:
#                     remaining = remaining[2:]
#             else:
#                 indices = [i for i, x in enumerate(remaining) if x == "]"]
#                 print(indices)
#                 last_index = indices[-1]
#                 print(last_index)
#                 #last_index = 3
                

#                 if ((last_index - (1)) % 2) != 0:
#                     print('hitting if 1 of []')
#                     print(f'there is an odd number: {remaining}')
#                     return False

#                 elif ((last_index - (1)) % 2) == 0:
#                     print('hitting elif 1 of []')
#                     remaining.pop(last_index)
#                     remaining.pop(0)
#                     print(remaining)
                    

#         elif remaining[0] == '{':
#             if '}' not in remaining:
#                 return False
#             elif remaining[1] == '}':
#                 if len(remaining) == 2:
#                     return True
#                 else:
#                     remaining = remaining[2:]
#             else:
#                 indices = [i for i, x in enumerate(remaining) if x == "}"]
#                 print(indices)
#                 last_index = indices[-1]
#                 print(last_index)
#                 #last_index = 3
                

#                 if ((last_index - (1)) % 2) != 0:
#                     print('hitting if 1')
#                     print(f'there is an odd number: {remaining}')
#                     return False

#                 elif ((last_index - (1)) % 2) == 0:
#                     print('hitting elif 1 of "curly braces"')
#                     remaining.pop(last_index)
#                     remaining.pop(0)
#                     print(remaining)
       
#     return True

# print(valid_braces("({]})"))


#class version:________________________________________________________

def valid_braces(string):

    if len(string) == 1:
        return False
    if len(string) % 2 != 0:
        return False

    #([{}])
    string = list(string)
    remaining = string

    while len(remaining) >= 1:

        if  remaining[0] == ')' or remaining[0] == '}' or remaining[0] == ']':
            return False

        elif remaining[0] == '(':
            if ')' not in remaining:
                return False
            elif remaining[1] == ')':
                if len(remaining) == 2:
                    return True
                else:
                    remaining = remaining[2:]
            else:
                indices = [i for i, x in enumerate(remaining) if x == ")"]
                print(indices)
                last_index = indices[-1]
                print(last_index)
                #last_index = 3
                

                if ((last_index - (1)) % 2) != 0:
                    print('hitting if 1 pf ()')
                    print(f'there is an odd number: {remaining}')
                    return False

                elif ((last_index - (1)) % 2) == 0:
                    print('hitting elif 1 of ()')
                    remaining.pop(last_index)
                    remaining.pop(0)
                    print(remaining)

                # this would deal with if %2 < 0    
                # else:
                #     if last_index == len(remaining)-1:
                #         remaining = f'{remaining[:last_index]}'
                #         print('hitting else-if')
                #     else:
                #         remaining = f'{remaining[:last_index]}{remaining[last_index+1:]}'
                #         print('hitting else-else')                    

                    
        elif remaining[0] == '[':
            if ']' not in remaining:
                return False
            elif remaining[1] == ']':
                if len(remaining) == 2:
                    return True
                else:
                    remaining = remaining[2:]
            else:
                indices = [i for i, x in enumerate(remaining) if x == "]"]
                print(indices)
                last_index = indices[-1]
                print(last_index)
                #last_index = 3
                

                if ((last_index - (1)) % 2) != 0:
                    print('hitting if 1 of []')
                    print(f'there is an odd number: {remaining}')
                    return False

                elif ((last_index - (1)) % 2) == 0:
                    print('hitting elif 1 of []')
                    remaining.pop(last_index)
                    remaining.pop(0)
                    print(remaining)
                    

        elif remaining[0] == '{':
            if '}' not in remaining:
                return False
            elif remaining[1] == '}':
                if len(remaining) == 2:
                    return True
                else:
                    remaining = remaining[2:]
            else:
                indices = [i for i, x in enumerate(remaining) if x == "}"]
                print(indices)
                last_index = indices[-1]
                print(last_index)
                #last_index = 3
                

                if ((last_index - (1)) % 2) != 0:
                    print('hitting if 1')
                    print(f'there is an odd number: {remaining}')
                    return False

                elif ((last_index - (1)) % 2) == 0:
                    print('hitting elif 1 of "curly braces"')
                    remaining.pop(last_index)
                    remaining.pop(0)
                    print(remaining)
       
    return True

print(valid_braces("({]})"))