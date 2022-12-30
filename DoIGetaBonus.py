def bonus_time(salary, bonus):

    if bonus == True:
        comp = salary*10
    else:
        comp = salary

    comp = f"${str(comp)}"
    return comp



print(bonus_time(10000, True))