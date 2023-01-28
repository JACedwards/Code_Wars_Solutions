# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

#Psuedo:
#   Dictionary with keys colors and number values
#   loop through list of colors:
#      get value with 0 as alternative if none found
#      store value in variable
#      add key value pair to dictionary adding one to the got value
#   #loop through dictionary  k ,v
#       floor divide values
#       create strings with "1 red pair"  (pay attention to plurals)
#       append strings to list
#       strip last ' +' from end

#this version just returns total number_____________________________

# def number_of_pairs(gloves):
#     dct_color_count = {}

#     for c in gloves:
#         num = dct_color_count.get(c, 0)
#         dct_color_count[c] = num + 1
#     # dct_color_count = {'gray': 2, 'black': 2, 'purple': 2}

#     # 1 red pair + 1 blue pair
#     # '1 gray pair + 1 black pair + 1 purple pair'

#     count = 0
#     for pairs in dct_color_count.values():
#         tot = pairs // 2
#         count = count + tot

#     return count

# print(number_of_pairs(["gray","black","purple","purple","gray","black"]))


#this version returns a string listing number of pairs for each color, which is what I 
# originally thought was the goal________________________

#pseudo for last half:
#   #loop through dictionary  k ,v
#       floor divide values
#       create strings with "1 red pair"  (pay attention to plurals)
#       append strings to list
#       strip last ' +' from end

def number_of_pairs(gloves):
    dct_color_count = {}

    for c in gloves:
        num = dct_color_count.get(c, 0)
        dct_color_count[c] = num + 1
    # dct_color_count = {'gray': 2, 'black': 2, 'purple': 2}

    # 1 red pair + 1 blue pair
    # '1 gray pair + 1 black pair + 1 purple pair'
    print(dct_color_count)
    output = ''
    pairs = 0
    for k, v in dct_color_count.items():
        pairs = int(v/2)
        if pairs == 1:
            output = f'{output} {pairs} {k} pair +'
            pairs = 0
        else:
            output = f'{output} {pairs} {k} pairs +'
            pairs = 0

    return output[:-2]

print(number_of_pairs(["red", "green", "red", "blue", "blue"]))