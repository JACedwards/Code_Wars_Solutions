
# def difference_in_ages(ages):
#     mn = ages[0]
#     mx = ages[0]

#     for n in ages:
#         if n <= mn:
#             mn = n
#         if n > mx:
#             mx = n

#     d = mx - mn

#     return (mn, mx, d)




# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))


# Brute force:

# def difference_in_ages(ages):
#     ages.sort()
#     x = min(ages)
#     y = max(ages)
#     z = y - x
#     return ((x,y,z))



# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))

# Slighly improved, avoids min() and max() funcitons:

def difference_in_ages(ages):
    ages.sort()
    d = ages[-1] - ages[0]
    return ((ages[0], ages[-1], d))



print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))