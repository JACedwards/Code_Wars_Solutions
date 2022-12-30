def create_phone_number(n):
    
    area_code = n[0:3]
    area_code_string = [str(x) for x in area_code]
    area_code_smash = ''.join(area_code_string)

    city_code = n[3:6]
    city_code_string = [str(x) for x in city_code]
    city_code_smash = ''.join(city_code_string)

    home_code = n[6:]
    home_code_string = [str(x) for x in home_code]
    home_code_smash = ''.join(home_code_string)

    return f"({area_code_smash}) {city_code_smash}-{home_code_smash}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))



