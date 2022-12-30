def get_drink_by_profession(param):
    
    dict_booze = {
            "Jabroni": "Patron Tequila", 
            "School Counselor": "Anything with Alcohol",
            "Programmer":"Hipster Craft Beer",
            "Bike Gang Member" : "Moonshine",
            "Politician" : "Your tax dollars",
            "Rapper": "Cristal"}

    if param.title() in dict_booze:
        return dict_booze.get(param.title())
    else:
        return "Beer"  





print(get_drink_by_profession("School Counselor"))



# def get_drink_by_profession(param):
    
#     if param == "Jabroni":
#         return "Patron Tequila"
#     elif param == "School Counselor":
#         return "Anything with Alcohol"
#     elif param == "Programmer":
#         return "Hipster Craft Beer"
#     elif param == "Bike Gang Member"	:
#         return "Moonshine"
#     elif param == "Politician"	:
#         return "Your tax dollars"
#     elif param == "Rapper":
#         return "Cristal"
#     else:
#         return "Beer"

