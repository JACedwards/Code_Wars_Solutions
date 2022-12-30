def say_hello(name, city, state):
    name_str = " ".join(name)


    return f"Hello, {name_str}! Welcome to {city}, {state}!"




print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))