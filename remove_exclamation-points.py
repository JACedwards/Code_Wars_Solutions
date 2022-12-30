def remove_exclamation_marks(s):

    for n in s:
        if n == '!':
            s = s.replace('!', '')

    return(s)

remove_exclamation_marks('This string! has! lots of! quotation marks')