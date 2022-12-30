# Given two arrays of strings array1 and array2 return a sorted array r in lexicographical order of the strings of array1 which are substrings of strings of array2.

# Example 1:
# array1 = ["arp", "live", "strong"]

# array2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# array1 = ["tarp", "mice", "bull"]

# array2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash array1 and array2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.

#Quadratic:

# def whichRIn(array1, array2):
#     output = []

#     for st1 in array1:
#         for st2 in array2:
#             if st1 in st2 and st1 not in output:
#                 output.append(st1)
#     output.sort()
#     return output


# print(whichRIn(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]))

#linear version:
# def whichRIn(array1, array2):
    
#     r = 0
#     output = []

#     while r <= len(array2)-1:
#         for st in array1:
#             if st in array2[r] and st not in output:
#                 output.append(st)
#         r+=1
#     output.sort()
#     return output

# print(whichRIn(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]))

#class version:

class AreIn():

    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def whichRIn(self):
        r = 0
        output = []

        while r <= len(self.array2)-1:
            for st in self.array1:
                if st in self.array2[r] and st not in output:
                    output.append(st)
            r+=1
        return output

    def sortOutput(self):
        output = self.whichRIn()
        output.sort()
        return output

test1 = AreIn(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"])
print(test1.sortOutput())