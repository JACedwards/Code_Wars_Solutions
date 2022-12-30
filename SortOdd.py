
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

#Psuedo:
    #loop and extract odd numbers to list
    #sort list
    #loop through source array, replacing each odd with next one in sorted array


# class SortedOdds():

#     def __init__(self, source_array):
#         self.source_array = source_array     


#     def sort_array(self):

#         odds = [n for n in self.source_array if n % 2 != 0]

#         odds.sort(reverse=True)

#         for i in range(len(self.source_array)):
#             if self.source_array[i] % 2 != 0:
#                 self.source_array[i] = odds[-1]
#                 odds.pop()
#         return self.source_array

# array1 = SortedOdds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
# print(array1.sort_array())

####-splitting into two functions, one calling the other

class SortedOdds():

    def __init__(self, source_array):
        self.source_array = source_array     


    def sort_array(self):

        odds = [n for n in self.source_array if n % 2 != 0]

        odds.sort(reverse=True)

        return odds

    def insert_odds(self):

        odds = self.sort_array()
        for i in range(len(self.source_array)):
            if self.source_array[i] % 2 != 0:
                self.source_array[i] = odds[-1]
                odds.pop()
        return self.source_array

array1 = SortedOdds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(array1.insert_odds())
