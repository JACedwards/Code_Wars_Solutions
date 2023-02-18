#still some errors on this one:  run test to keep working (missing 123):  https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python 

#Pandas, 2-key sort: https://stackoverflow.com/questions/17141558/how-to-sort-a-dataframe-in-python-pandas-by-two-or-more-columns


# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

# 180 is before 90 since, having the same "weight" (9), it comes before as a string.

# All numbers in the list are positive numbers and the list can be empty.

# Notes
# it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
# For C: The result is freed.

#Pseudo:
# split string by spaces (may be more than one)
# loop through list of strings:
#    splitting each
#    appending int version of each digit to list
#    sum list
#    add string version of original as key to integer version of the summed version.
# (going to have to deal with the "same" weight alphabetical thing eventually)

#____________________First one works unless original string has duplicates_______________

# def order_weight(strng):

#     strng = strng.split()
#     #['56', '65', '74', '100', '99', '68', '86', '180', '90']
#     dct = {strng[i] : [0, ''] for i in range(len(strng))}
#     dct_lst = {}
#     # {'56': [0, ''], '65': [0, ''], '74': [0, ''], '100': [0, ''], '99': [0, ''], '68': [0, ''], '86': [0, ''], '180': [0, ''], '90': [0, '']}
#     convert = []
#     nums = {1:'one', 10:'ten', 11: 'eleven', 12: 'tw', 13: 'th', 14:'fo', 15:'fi', 16: 'si', 17:'se', 18:'ei', 19:'ni', 2: 'tw', 3: 'th', 4 : 'fo', 5 : 'fi', 6 : 'si', 7:'se', 8:'ei', 9:'ni'}

#     for w in strng:
#         for d in w:
#             convert.append(int(d))
#         sm = sum(convert)
#         print(sm)
#         if w == '10':
#             alpha = nums.get(10)
#             dct_lst[w] = [sm, alpha]
#         elif w == '11':
#             alpha = nums.get(11)
#             dct_lst[w] = [sm, alpha]
#         elif w == '12':
#             alpha = nums.get(12)
#             dct_lst[w] = [sm, alpha]
#         elif sm == '13':
#             alpha = nums.get(13)
#             dct_lst[w] = [sm, alpha]
#         elif w == '14':
#             alpha = nums.get(14)
#             dct_lst[w] = [sm, alpha]
#         elif w == '15':
#             alpha = nums.get(15)
#             dct_lst[w] = [sm, alpha]
#         elif w == '16':
#             alpha = nums.get(16)
#             dct_lst[w] = [sm, alpha]
#         elif w == '17':
#             alpha = nums.get(17)
#             dct_lst[w] = [sm, alpha]
#         elif w == '18':
#             alpha = nums.get(18)
#             dct_lst[w] = [sm, alpha]
#         elif w == '19':
#             alpha = nums.get(19)
#             dct_lst[w] = [sm, alpha]
#         else:
#             n = w[0]
#             alpha = nums.get(int(n))
#             dct_lst[w] = [sm, alpha]

#         alpha = ''
#         convert = []
#     print(dct_lst)
#     sorted_dct_lst = sorted(dct_lst.items(), key = lambda x:x[1][0])
#     print(sorted_dct_lst)
#     output = []
#     for srt in sorted_dct_lst:
#         output.append(srt[0])
#     output_str = ' '.join(output)
#     return output_str

    

# print(order_weight("56 65 74 100 99 68 86 180 90"))

# "100 180 90 56 65 74 68 86 99"

# 11
# 11
# 11
# 1
# 18
# 14
# 14
# 9
# 9

#_______________This second one is attempt to deal with original string having duplicates using pandas___________

import pandas as pd

def order_weight(strng):
    #strng = "2000 10003 1234000 44444444 9999 11 11 22 123"
    strng = strng.split()
    # = ['2000', '10003', '1234000', '44444444', '9999', '11', '11', '22', '123']
    ints = []

    for s in strng:
        ints.append(int(s))
    # ints = [2000, 10003, 1234000, 44444444, 9999, 11, 11, 22, 123]

    #sum + alpha:
    nums = {1:'one', 10:'ten', 11: 'eleven', 12: 'tw', 13: 'th', 14:'fo', 15:'fi', 16: 'si', 17:'se', 18:'ei', 19:'ni', 2: 'tw', 3: 'th', 4 : 'fo', 5 : 'fi', 6 : 'si', 7:'se', 8:'ei', 9:'ni'}

    sums = []
    alphas = []
    convert = []

    for w in strng:
        for d in w:
            convert.append(int(d))
        sm = sum(convert)
        sums.append(sm)
        if w == '10':
            alpha = nums.get(10)

        elif w == '11':
            alpha = nums.get(11)

        elif w == '12':
            alpha = nums.get(12)

        elif sm == '13':
            alpha = nums.get(13)

        elif w == '14':
            alpha = nums.get(14)
           
        elif w == '15':
            alpha = nums.get(15)

        elif w == '16':
            alpha = nums.get(16)
   
        elif w == '17':
            alpha = nums.get(17)
 
        elif w == '18':
            alpha = nums.get(18)
 
        elif w == '19':
            alpha = nums.get(19)
 
        else:
            n = w[0]
            alpha = nums.get(int(n))
        alphas.append(alpha)
        convert = []

    # ints = [2000, 10003, 1234000, 44444444, 9999, 11, 11, 22, 123]
    #['tw', 'one', 'one', 'fo', 'ni', 'eleven', 'eleven', 'tw', 'one']
    #[2, 4, 10, 32, 36, 2, 2, 4, 6]


    lst_o_lsts = []

    for i in range(len(ints)):
        sub_lst = []
        sub_lst.append(strng[i])
        sub_lst.append(ints[i])
        sub_lst.append(alphas[i])
        sub_lst.append(sums[i])
        lst_o_lsts.append(sub_lst)
        sub_lst = []

    print(lst_o_lsts)

    #lst_o_lsts:
    #[['2000', 2000, 'tw', 2], ['10003', 10003, 'one', 4], ['1234000', 1234000, 'one', 10], ['44444444', 44444444, 'fo', 32], ['9999', 9999, 'ni', 36], ['11', 11, 'eleven', 2], ['11', 11, 'eleven', 2], ['22', 22, 'tw', 4]]

    df = pd.DataFrame(lst_o_lsts, columns = ['str', 'ints', 'alphas', 'sums'])
    
    df_srt = df.sort_values(by=['sums', 'alphas'])
 

    col_list = df_srt["str"].values.tolist()

    output = ' '.join(col_list)

    return output



    
  

print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
#"11 11 2000 10003 22 ***123*** 1234000 44444444 9999"
# print(order_weight("56 65 74 100 99 68 86 180 90"))
# "100 180 90 56 65 74 68 86 99"

        # test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
