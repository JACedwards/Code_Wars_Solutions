# In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

# >>> d = Dictionary()

# >>> d.newentry('Apple', 'A fruit that grows on trees')

# >>> print(d.look('Apple'))
# A fruit that grows on trees

# >>> print(d.look('Banana'))
# Can't find entry for Banana

#Pseudo:
# function first, then class
# create empty dictionary
# accept key, accept value
# add key, value pair to dict

class Dictionary():
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        
    def newentry(self):
        dct = {}
        dct[self.word] = self.definition
        return dct
        
    def look(self, key):
        dct = self.newentry()
        check = dct.get(key)
        if check == None:
            return f"Can't find entry for {key}"
        else:
            return check

test1 = Dictionary('Apple', 'A fruit that grows on trees')

print(test1.look('Banana'))