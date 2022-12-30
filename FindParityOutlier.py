# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

#psuedo:
    #check first 3 digits to see if at least 2 even or odd
    #for at least 2 even, loop through and return first odd
    #for at least 2 odd, loop through and return first even

def find_outlier(integers):
    ev_odd = ''
    count = 0
    
    for n in integers[:3]:
        if n % 2 == 0:
            count +=1
    if count >=2:
        ev_odd = 'even'

    count = 0
    
    for n in integers[:3]:
        if n % 2 != 0:
            count +=1
    if count >=2:
        ev_odd = 'odd'

    if ev_odd == 'odd':
        for n in integers:
            if n % 2 == 0:
                return n

    if ev_odd == 'even':
        for n in integers:
            if n % 2 != 0:
                return n

print(find_outlier([2, 4, 1]))