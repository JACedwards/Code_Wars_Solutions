def get_planet_name(id):
    
    if id == 1: 
        name = "Mercury"
    if id == 2: 
        name = "Venus"
    if id == 3: 
        name = "Earth"
    if id == 4: 
        name = "Mars"
    if id == 5: 
        name = "Jupiter"
    if id == 6: 
        name = "Saturn"
    if id == 7: 
        name = "Uranus"  
    if id == 8: 
        name = "Neptune"
    return name 


print(get_planet_name(2))