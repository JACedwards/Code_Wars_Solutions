
# couldn't figure out how to make it work about 12-14
def how_much_i_love_you(nb_petals):
    a1 = 'I love you'
    a2 = 'a little' 
    a3 = 'a lot' 
    a4 = 'passionately' 
    a5 = 'madly' 
    a6 = 'not at all'

    b1 = 1
    b2 = 2 
    b3 = 3 
    b4 = 4 
    b5 = 5 
    b6 = 6

    if nb_petals < 7:
        output = nb_petals
        if output == 1:
            return a1
        elif output == 2:
            return a2
        elif output == 3:
            return a3
        elif output == 4:
            return a4
        elif output == 5:
            return a1
        elif output == 6:
            return a6

    else:
        output = nb_petals - 6
        if output == 1:
            return a1
        elif output == 2:
            return a2
        elif output == 3:
            return a3
        elif output == 4:
            return a4
        elif output == 5:
            return a1
        elif output == 6:
            return a6

how_much_i_love_you(269)
sdlkfj