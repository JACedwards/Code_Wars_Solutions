# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

#Psuedo:
#  Set up dictionary of values
#  Set up variables to check for subtraction
#  check if any 6 subtraction strings are in string:
#     if so, need to deal with that
#     if not, can deal with in simpler way, hopefully

def romToStr(s):
    
    value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sub_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400,'CM': 900}
    
    four = 'IV'
    nine = 'IX'
    forty = 'XL'
    ninety = 'XC'
    fr_hun = 'CD'
    ni_hun = 'CM'
    count = 0
    sum = 0

    if four not in s and nine not in s and forty not in s and ninety not in s and fr_hun not in s and ni_hun not in s:
        for c in s:
            count = value_dict.get(c)
            sum = sum + count
            count = 0
        return sum

    else:
        l=0
        r=2
        check_sub = ''
        sum = 0
        count_sub = 0
        #to deal with out of range problem
        s = f"{s}x"

        while r <= len(s):
            slc = s[l:r]
            if four in slc:
                check_sub = 'IV'
                count_sub = sub_dict.get(check_sub)
                sum = sum + count_sub
                count_sub = 0
                check_sub = ''
                l=r
                r += 2
            elif nine in slc:
                check_sub = 'IX'
                count_sub = sub_dict.get(check_sub)
                sum = sum + count_sub
                count_sub = 0
                check_sub = ''
                l=r
                r += 2
            elif forty in slc:
                check_sub = 'XL'
                count_sub = sub_dict.get(check_sub)
                sum = sum + count_sub
                count_sub = 0
                check_sub = ''
                l=r
                r += 2
            elif ninety in slc:
                check_sub = 'XC'
                count_sub = sub_dict.get(check_sub)
                sum = sum + count_sub
                count_sub = 0
                check_sub = ''
                l=r
                r += 2
            elif fr_hun in slc:
                check_sub = 'CD'
                count_sub = sub_dict.get(check_sub)
                sum = sum + count_sub
                count_sub = 0
                check_sub = ''
                l=r
                r += 2
            elif ni_hun in slc:
                check_sub = 'CM'
                count_sub = sub_dict.get(check_sub)
                sum = sum + count_sub
                count_sub = 0
                check_sub = ''
                l=r
                r += 2
            else:
                check_sub = s[l]
                count_sub = value_dict.get(check_sub)
                sum = sum + count_sub
                count_sub = 0
                check_sub = ''
                l += 1
                r += 1
        return sum


print(romToStr("MCMXCIV"))
