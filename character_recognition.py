
def correct(s):

    
    for i in range(len(s)):
        if s[i] == "5":

            s = s.replace(s[i], "S")
        elif s[i] == "0":
            s = s.replace(s[i], "O")
        elif s[i] == "1":

            s = s.replace(s[i], "I")
        else:
            continue
    return s

print(correct("51NGAPORE"))


# def correct(string):

#     print(string.maketrans("501", "SOI"))
#     return string.translate(string.maketrans("501", "SOI"))

# print(correct("51NGAPORE"))
