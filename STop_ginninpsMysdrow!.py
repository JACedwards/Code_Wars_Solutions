def spin_words(sentence):

    output = []
    x = sentence.split()
    length = len(x)
    if length == 1:
        for five in x:
            sl = len(five)
            print(sl)
            if sl >= 5:
                revfive = five[sl::-1]
            return revfive
    else:
        return five

    elif length > 1: 
        for five in x:
            sl = len(five)
            print(sl)
            if sl >= 5:
                revfive = five[sl::-1]
                print(revfive)
                output.append(revfive)
            else:
                output.append(five)

        ' '.join(output)

        return output
        



print(spin_words("Welcome"))

# #works with multiple words
# def spin_words(sentence):
#     x = sentence.split()
#     output = []

#     for five in x:
#         sl = len(five)
#         if sl >= 5:
#             revfive = five[sl::-1]
#             print(revfive)
#             output.append(revfive)
#         else:
#             output.append(five)
#     return output
        



# print(spin_words("Hey fellow warriors"))

