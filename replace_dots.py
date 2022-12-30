def replace_dots(str):

    list_a = [y for y in str.replace(".", "-") ]
    output = ''

    for x in list_a:
        output += ''+ x
    
    return output







print(replace_dots("one.two.three"))