# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


#Psuedo:
# 
# count # of capital X and lower case x and add together, store in variable
# same for 'o'
# if both counts = 0, return true
# compare number of combined x n o's
# return true if ==
# return False

def xo(s):
    cap_X = s.count('X')
    low_x = s.count('x')
    cap_O = s.count('O')
    low_o = s.count('o')

    x_combo = cap_X + low_x
    o_combo = cap_O + low_o

    if x_combo + o_combo == 0:
        return True

    else:
        return x_combo == o_combo




print(xo("xooxx"))