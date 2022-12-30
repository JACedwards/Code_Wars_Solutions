# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

#Psuedo:
# strip spaces
# split into list
# loop indices of list,
#  if i = odd,
#    reverse by reverse slicing
#  append
# join

# def reverse_alternate(s):

#     s= s.strip()
#     s = s.split()
#     lst_output = []
    
#     for i in range(len(s)):
#         if i % 2 != 0:
#             lst_output.append(s[i][::-1])
#         else:
#             lst_output.append(s[i])
    
#     output = " ".join(lst_output)
#     return output

    #Class version:
class Reverse():

    def __init__(self,s):
        self.s = s

    def strip_split(self):
        s = self.s
        s = s.strip()
        s = s.split()
        return s

    def reverse_alternate(self):    
        s = self.strip_split()

        lst_output = []
        
        for i in range(len(s)):
            if i % 2 != 0:
                lst_output.append(s[i][::-1])
            else:
                lst_output.append(s[i])
        
        output = " ".join(lst_output)
        return output

test1 = Reverse("Did it work?")

print(test1.reverse_alternate())