# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).

# Examples:
#     1 = $40
#     4 = $140
#     8 = $270
#     7 = $230

# <3 = d * 40
# 3-6 = (d * 40)-20
# >7


def rental_car_cost(d):
    if d < 3:
        cost = 40 * d
    elif d < 7:
        cost = (40*d) - 20
    else:
        cost = (d*40)-50

    return cost



print(rental_car_cost(8))
