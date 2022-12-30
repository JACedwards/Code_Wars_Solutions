def reverse_words(s):

    x = s.split()
    x.reverse()
    y = ' '.join(x)
    return(y)

print(reverse_words("The greatest victory"))