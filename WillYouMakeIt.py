
def zero_fuel(distance_to_pump, mpg, fuel_left):

    # fuel x mpg = distance can drive
    #  compare distance can drive to distance to pump

    can_drive = mpg * fuel_left


    if can_drive >= distance_to_pump:
        return(True)
    else:
        return(False)





print(zero_fuel(100, 50, 1))