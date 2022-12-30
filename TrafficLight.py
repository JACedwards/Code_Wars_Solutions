def update_light(current):


    light = 0

    if current == 'green': 
        light = 'yellow'
        return light
    if current == 'yellow':
        light = 'red'
        return light
    if current == 'red':
        light = 'green'
        return light

print(update_light('yellow'))

