# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# Psuedo:
# loop through
# check if int
# if int append to knew list

def filter_list(l):

    nums = []
    for n in l:
            if isinstance(n, int):
                print(f'Is integer')
                nums.append(n)
    output=[]
    for dup in nums:
        if dup not in output:
            output.append(dup)
    
    return output

print(filter_list(["a", "b", "1"]))

# def filter_list(l):

#     nums = []
#     for n in l:
#         try:
#             if n.integer() == True:
#                 print(f'Is integer')
#                 nums.append(n)
#             elif n.is_numeric() == True:
#                 nums.append(int(n))
#                 print("is string integer")
#         except:
#             print("continue")
#             continue
#     return nums



# print(filter_list([1,2,'a','b']))