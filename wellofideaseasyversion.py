def well(x):

    good = x.count("good")

    if good > 2:
        return "I smell a series!"
    if good == 1 or good ==2:
        return "Publish!"
    else:
        return "Fail!"


print(well(['good', 'bad', 'bad', 'bad', 'bad']))
