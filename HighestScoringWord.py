# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

#Psuedo:
    #create dictionary of values for each letter of alphabet
    #split string into words(?)
    #loop through each string summing value of each character
    #store in dictionary and list
    #get max list
    #output max value word from dictionary based on max value from list
    #need to figure out if any tie and deal with that (first word of tied is output)


def high(x):
    alpha = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    num = []
    for y in range(1,27):
        num.append(y)
    
    #dictionary of letter keys and number values
    values = {alpha[i]: num[i] for i in range(len(alpha))}
    lst_words = x.split()

    count = 0
    values_list = []
    dct_values = {}
    for w in lst_words:
        for c in w:
            count = count + values.get(c, 0)
        values_list.append(count)
        dct_values[w] = count
        count = 0

    highest = max(values_list)

    output = [k for k,v in dct_values.items() if v == highest][0]
    return output

print(high('zgihpb tipiz zqkp yxagmyrmn qpqzkgrjj cohiuipw iext ghpkqy lcxolzixsw ggrgbu zdvzku etlt owlicrpav tvhgalf evvlljulmi pftjrw gftrcplm'))





