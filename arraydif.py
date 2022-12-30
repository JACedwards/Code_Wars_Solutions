

def array_diff(a, b):

    if a == []:
        return []
    if b == []:
        return a

    for x in b:
        a = [i for i in a if i != x]
                    
    return a

print(array_diff([1,2,2],[1]))    

# def array_diff(a, b):

#     if a == []:
#         return []
#     if b == []:
#         return a

#     a = set(a)

#     for n in b:
#         if n in a:
#             a.remove(n)
                
#     return list(a)



# print(array_diff([1,2,2],[1]))

# a = [1,2,2,2,3] 
# b = [2]
# check = 

# if b in a:
#     print(b)
    
# #     for x in a:
# #         if x != b:
# #             print(x)

# #     return a



# array_diff([1,2,2,2,3],[2])