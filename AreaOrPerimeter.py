def area_or_perimeter(l , w):

    if l == w:
        output = l*w
    else:
        output = 2*(l+w)
    return output


print(area_or_perimeter(3,3))