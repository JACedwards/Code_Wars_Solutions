def pillars(num_pill, dist, width):
    # centimenters
    if num_pill <= 1:
        return 0
    
    pill_w_minus_2 = (width * num_pill) - (width*2)

    intern_distance = (dist*100) * (num_pill - 1)

    return pill_w_minus_2 + intern_distance



print(pillars(1, 10, 10))