# Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.

# Legend:
# -Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
# -Function input: String contains only letters, uppercase letters are unique.
# Task:
# Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".

#Psuedo:
#  create list of upper's only
# sort list
# loop through list, 
#    append uppercase version to output
#    checking string as you go for each item in list,
#  append lower case versions of each list item to output list
# 

def find_children(dancing_brigade):

    lst_capitals = []
    output = []

    for c in dancing_brigade:
        if c == c.upper():
            lst_capitals.append(c)
    lst_capitals.sort()
    
    for cap in lst_capitals:
        output.append(cap)
        for l in dancing_brigade:
            if l == cap.lower():
                output.append(l)
    output = ''.join(output)
    return output




print(find_children("aAbaBb"))