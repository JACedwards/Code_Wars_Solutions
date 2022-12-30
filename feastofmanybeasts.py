
def feast(beast, dish):
    # beast = ''.join(beast)
    # dish = ''.join(dish)

    if beast[0] == dish[0] and beast[-1] ==  dish[-1]:
        return True
    else:
        return False





print(feast("brown bear", "bear claw"))