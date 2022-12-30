def enough(cap, on, wait):

    if cap - on < wait:
        output = wait - (cap-on)
        return output
    else:
        return 0




print(enough(10,5,5))