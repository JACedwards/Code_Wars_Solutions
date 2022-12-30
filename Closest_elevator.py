def elevator(left, right, call):
    print(call - left)
    print(call - right)
    if call - left == call - right:
        return "right"
    elif call == left:
        return "left"
    elif call == right:
        return "right"
    elif call - left > call - right:
    
        return "right"
    else:
        return "left"




print(elevator(0, 1, 0))