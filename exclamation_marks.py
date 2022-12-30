def replace_exclamation(string):
    output = set(string)

    output.discard('a')
    output.discard('e')
    output.discard('i')
    output.discard('o')
    output.discard('u')
    output.discard('a'.upper())
    output.discard('e'.upper())
    output.discard('i'.upper())
    output.discard('o'.upper())
    output.discard('u'.upper())
    

    return output

print(replace_exclamation("ABCDE"))

# string = "geeks for geeks geeks geeks geeks" 
   
# # Prints the string by replacing all
# # geeks by Geeks 
# print(string.replace("geeks", "Geeks")) 