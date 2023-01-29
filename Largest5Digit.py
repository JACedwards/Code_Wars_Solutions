# In the following 6 digit number:

# 283910
# 91 is the greatest sequence of 2 consecutive digits.

# In the following 10 digit number:

# 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.

# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.

def solution(digits):

    digits = str(digits)
    l=0
    r=5
    longest = 0
    
    while r <= len(digits)-1:
        if r == len(digits)-1:
            if int(digits[l+1:]) > longest:
                longest = int(digits[l+1:])
                return longest
        elif int(digits[l:r]) > longest:
            longest = int(digits[l:r])
            l+=1
            r+=1
        else:
            l+=1
            r+=1

    return longest




print(solution(283790111))
# #91011

