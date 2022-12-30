# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# All numbers will be whole numbers greater than 0.

#Psuedo code:

#store lenght of number in variable
#turn number to string
#split string into list
#loop through list,
#  creating new list
#   by concatenating each item in list with number of 0 in length
#   then subtracting one from length
#   strip out any item in new list that beginns with 0
# create final string by looping through list:
#  concatinating each item to next " + "
# strip final " + " from output string


#_______________works______________

# def expanded_form(num):


#     num = str(num)
#     length = len(num) - 1
#     num = list(num)
#     list_nums = []
#     add_0 = ''

#     for n in num:
#         add_0 = f"{n}{'0' * length}"
#         list_nums.append(add_0)
#         length = length - 1

#     list_no_0 = [x for x in list_nums if x[0] != '0']
    
#     output = ''
#     for p in list_no_0:
#         output = f"{output}{p} + "
    
#     return output[:-3]

# print(expanded_form(70304))
# # '70000 + 300 + 4'

#______________class version_______________

class Expanded():

    def __init__(self, num):
        self.num = num

    def expanded_form(self):

        self.num = str(self.num)
        length = len(self.num) - 1
        self.num = list(self.num)
        list_nums = []
        add_0 = ''

        for n in self.num:
            add_0 = f"{n}{'0' * length}"
            list_nums.append(add_0)
            length = length - 1

        list_no_0 = [x for x in list_nums if x[0] != '0']
        return list_no_0

    def number_form(self):
        list_no_0 = self.expanded_form()
        
        output = ''
        for p in list_no_0:
            output = f"{output}{p} + "
        
        return output[:-3]



test = Expanded(70304)

print(test.number_form())
# '70000 + 300 + 4'
