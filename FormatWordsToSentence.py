# Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string.

# Note:

# Empty string values should be ignored.
# Empty arrays or null/nil/None values being passed into the method should result in an empty string being returned.
# Example: (Input --> output)

# ['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
# ['ninja', '', 'ronin'] --> "ninja and ronin"
# [] -->""

#Psuedo:
#  if empty list, return empty string
# loop through list:
#  removing empty strings
# check lenght of new list:
#    #store next to last index in variable
#    #store last index in variable
# loop through list:
# if element is empty string "continue"
#  if item is -2 index, don't add comma
#  if item is -1 index, add "and <word>"
#  else:  word + comma

def format_words(words):
    if words == None:
        return ''

    no_string = []
    for w in words:
        if w == '':
            continue
        else:
            no_string.append(w)

    if no_string == []:
        return ''
    
    if len(no_string) == 1:
        return no_string[0]

    second_last = len(no_string)-2
    last = len(no_string) -1
    output = ''
    
    for i in range(len(no_string)):
        if i != second_last and i != last:
            output = f"{output}{no_string[i]}, "
        if i == second_last:
            output = f"{output}{no_string[i]} "
        elif i == last:
            output = f"{output}and {no_string[i]}"

        

    return output


print(format_words(['ninja', '', 'ronin']))