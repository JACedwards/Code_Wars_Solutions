# def solution(string):
output = []
string = ['m', 'i', 's', 's', 'i', 's', 's']


if string == []:
    output = []

else:
    for x in string:
        output += string[-1]
        print(output)
        string = string.remove(string[-1])
        print(output)

#     return output

# print(solution(['m', 'i', 's', 's', 'i', 's', 's']))

# def solution(string):
#     output = ''

#     if string == '':
#         output = ''

#     else:
#         for char in string:
#             output += string[-1]
#             string = string.replace(string[-1], '', 1)
#     return output

# print(solution('mississ'))

   

# def solution(string):

#     output = ''

#     if string == '':
#         output = ''

#     else:
#         for char in string:
#             output += string[-1]
#             string = string.replace(string[-1], '')

#     return output

# print(solution('tittle'))




# def solution(string):
#     output = ''
#     c = 0
    
    # if string == '':
    #     output = ''
            
#     else:
#         while c >= len(string):    
#             for char in string:
#                 output += string[-1]
#                 string = string.replace(string[-1], '')
#                 c = c + 1
        
#     return output

# answer = solution('hello')
# print(answer)
