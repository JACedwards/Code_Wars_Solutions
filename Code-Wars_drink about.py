def people_with_age_drink(age):

    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"   
    if age < 21:
        return "drink beer"   
    else:
        return "drink whisky"    



print(people_with_age_drink(13))