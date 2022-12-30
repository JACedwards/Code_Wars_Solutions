def disemvowel(string_):
    output_list = []
    vowels = ["a","e","i","o","u"]

    for i in range(len(string_)):
        if string_[i].lower() in vowels:
            continue
        else:
            output_list.append(string_[i])

    

    return "".join(output_list), type("".join(output_list))

print(disemvowel("This website is for losers LOL!"))