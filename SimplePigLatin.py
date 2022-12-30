# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

#Psuedo:
    #split into list
    #loop through strings in list
    #Using slices and f strings:
        #move first letter to end
        #add 'ay'
    #rejoin list into single string

def pig_it(text):
    out_list = []

    lst_text = text.split()
    for w in lst_text:
        if w.isalpha() == False:
            out_list.append(w)
        else:
            pig_w = f"{w[1:]}{w[0]}{'ay'}"
            out_list.append(pig_w)
    output = ' '.join(out_list)
    return output

print(pig_it('Hello world !'))