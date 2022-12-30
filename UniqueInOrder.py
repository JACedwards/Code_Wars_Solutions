# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

#Psuedo code:
#loop through iterable,
#if letter not in list, add it
#output list

# def unique_in_order(iterable):

#     if iterable == '':
#         return []

#     if len(iterable) == 1:
#         output = [iterable[0]]
#         return output

    
#     first = iterable[0]
#     output = [first]
#     for c in iterable:
#         if c != output[-1]:
#             output.append(c)

#     return output

# print(unique_in_order('AAAABBBCCDAABBB'))


#_____class version______________

class Unique():

    def __init__(self, iterable):
        self.iterable = iterable


    def zeroACheck(self):

        if self.iterable == '':
            return []

    def oneCheck(self):
        if len(self.iterable) == 1:
            output = [self.iterable[0]]
            return output

    def unique_in_order(self):
        self.zeroACheck()
        self.oneCheck()
        
        first = self.iterable[0]
        output = [first]
        for c in self.iterable:
            if c != output[-1]:
                output.append(c)

        return output

test = Unique('')

print(test.unique_in_order())