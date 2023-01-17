# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8

#This works up to a point if I set the range top end to 1000000.  Need to find a way of generating only x number of odd numbers using range since I don't know what actual highest number needs to be.  For instance, if I need 10 odd numbers, the highest would be 19, but this is based on an input of 4 

def row_sum_odd_numbers(n):
    ind = 0
    dct = {}

    rows = list(range(1,n+1))
    count_odd = sum(rows)
    first_n_odd = list(range(1, count_odd * 2, 2))
    print(first_n_odd)
    print(f'this is count_odd:  {count_odd}')
    print(rows)
    total_odds = list(first_n_odd[0:count_odd])
    print(f'this is total odds {total_odds}')

    a = 1
    y = 0
    z = 1
    for x in rows:
        dct[x] = list(total_odds[y:z])
        a+=1
        y = z
        z = z + a
    print(dct)
    output = dct.get(n)
    output = sum(output)
    return output
    

print(row_sum_odd_numbers(41))