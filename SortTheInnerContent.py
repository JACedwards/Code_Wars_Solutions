# You have to sort the inner content of every word of a string in descending order.

# The inner content is the content of a word without first and the last char.

# Some examples:

# "sort the inner content in descending order"  -->  "srot the inner ctonnet in dsnnieedcg oredr"
# "wait for me"        -->  "wiat for me"
# "this kata is easy"  -->  "tihs ktaa is esay"
# Words are made up of lowercase letters.

# The string will never be null and will never be empty. In C/C++ the string is always nul-terminated.

#Psuedo code:

#split string into list of strings
#split each string in the list into its own list
# if a given string is length of 1, 2, or 3, 
#   nothing needs to be done to it
# else:
#   put middle letters of each word into separate list
#      sort them in descending order
#   add them back to original word
#   will need to do some joining...

def sort_the_inner_content(words):

    sent_lst = []
    words = words.split()
    all_joined = ''

    for w in words:
        w = list(w)
        
        if len(w) == 1 or len(w) == 2 or len(w) == 3:
            joined = ''.join(w)
            sent_lst.append(joined)
            print(sent_lst)

        else:
            middle = w[1:-1]
            middle.sort(reverse=True)
            middle_join = ''.join(middle)
            all_joined = f'{w[0]}{middle_join}{w[-1]}'
            sent_lst.append(all_joined)
    
    output = ' '.join(sent_lst)
    return output


        
        


        #[['w', 'a', 'i', 't'], ['f', 'o', 'r'], ['m', 'e']] = sent_lst
    


    # split = "wait"
    # split = list(split)
    # print(split)
    # middle = split[1:-1]
    # middle.sort(reverse=True)
    # print(middle)




print(sort_the_inner_content("this kata is easy"))