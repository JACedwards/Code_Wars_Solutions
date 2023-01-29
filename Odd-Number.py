# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

# def stray(arr):

#     st = set(arr)
#     st = list(st)
#     x = st[0]
#     y = st[1]

#     x_count = arr.count(x)
#     print(x_count)
#     y_count = arr.count(y)
#     print(y_count)

#     if x_count == 1:
#         return x
#     else:
#         return y

# print(stray([17, 17, 3, 17, 17, 17, 17]))

#DICT version
# def stray(arr):
    
#     dct={}
#     count = 0

#     for n in arr:
#         count = dct.get(n, 0)
#         dct[n] = count + 1
    
#     for k, v in dct.items():
#         if v == 1:
#             return k

        

# print(stray([17, 17, 3, 17, 17, 17, 17]))

#Sliding window version

def stray(arr):

    if arr[0] != arr[1]:
        if arr[2] != arr[0]:
            return arr[0]
        else:
            return arr[1]

    l = 0
    r = 1
    while r <= len(arr) - 1:
        if arr[l] == arr[r]:
            repeat = arr[l]
            r+=1
        elif arr[l] != arr[r]:
            l_x = arr[l]
            r_x = arr[r]
            return r_x

print(stray([17, 17, 3, 17, 17, 17, 17]))

