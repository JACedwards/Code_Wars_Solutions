# You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.

# Examples
# []                   -->  0
# [1, 2, 3]            -->  3
# ["x", "y", ["z"]]    -->  4
# [1, 2, [3, 4, [5]]]  -->  7
# The input will always be an array.

#<><> Current version works only if all lists are nested inside each other, this one does not work, for instance:
#   [[28, 43, 4, 28], [29, 26, 66, -7, 36], 14, 15, 47]
#   Returns 8 when should return 13 because it stops when reaches FIRST instance of embedded list.



def deep_count(a):
    total = 0
    
    flag = True
    while flag == True:
        cnt = len(a)
        total = total + cnt
        #total = 3 (first time)
        
        #[5]
        lst = [None]
        for tp in a:
            if isinstance(tp, list):
                lst = tp
        if lst != [None]:
            a = lst
        else:
            flag = False


    return total



print(deep_count(["x", "y", ["z"]]))