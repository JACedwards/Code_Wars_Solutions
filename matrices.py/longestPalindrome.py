# Longest Palindrome
# Find the length of the longest substring in the given string s that is the same in reverse.

# As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

# If the length of the input string is 0, the return value must be 0.

# Example:
# "a" -> 1 
# "aab" -> 2  
# "abcde" -> 1
# "zzbaabcd" -> 4
# "" -> 0

#Pseudo:
#   left and right pointers
#   find index of next time letter at left pointer occurs
#   do palindrome check between those to letters
#   store running count of longest


# def longest_palindrome (s):

#     l=0
#     r=0
#     output = 0
#     length = 0

#     while l-r !=1 and r != len(s)-1:
          
#         l_value = s[l]
#         s = s[l:]
#         r = s.find(l_value) + 1
#         while r-l >=1:
#             if s[l] == s[r] and r-l == 1:
#                 length = len(s[l:r]) + 1
#                 if output < length:
#                     output = length
#                     print(f'this is output: {output}')
#                     s=s[l+1:]
#                     l_value = s[l]
#                     s = s[l+1:]
#                     r = s.find(l_value) + 1
                    

#             elif s[l] != s[r]:
#                 r+=1
                
#             else:
#                 length = len(s[l:r]) + 1
#                 if output < length:
#                     output = length
#                     print(f'this is output: {output}')
#                     s=s[l+1:]
#                     l_value = s[l]
#                     s = s[l+1:]
#                     r = s.find(l_value) + 1
    
#     return output



# print(longest_palindrome("zzbaabcd"))
















# test.assert_equals(longest_palindrome("a"), 1)
# test.assert_equals(longest_palindrome("aa"), 2)
# test.assert_equals(longest_palindrome("baa"), 2)
# test.assert_equals(longest_palindrome("aab"), 2)
# test.assert_equals(longest_palindrome("abcdefghba"), 1)
# test.assert_equals(longest_palindrome("baablkj12345432133d"), 9)


def longest_palindrome (s):

    length = 0
    output = 0
    l = 0
    r = 2
    while l == len(s) - 2 and r != len(s) - 1:

        l = 0
        r = 1
        left = 0
        right = 1
        slce = s[left:right]
        if len(slce) % 2 != 0:
            while r-l >=1:
                if slce[l] != slce[r]:
                    output = length
                    left += 1
                    right = left + 2
                    slce = s[left:right]
                else:
                    l += 1
                    r -= 1
            if output < length:
                output = length
                left += 1
                right = left + 2
                slce = s[left:right]
        else:
            while r-l >=1:
                if slce[l] != slce[r]:
                    output = length
                    left += 1
                    right = left + 2
                    slce = s[left:right]
                else:
                    l += 1
                    r -= 1
            output = length
            left += 1
            right = left + 2
            slce = s[left:right]
    return output


print(longest_palindrome("zzbaabcd"))
# _______________________________
    # flag = True
    # while flag == True:

        
    #     l_value = s[l]
    #     x = s[l:]
    #     r = x.find(l_value) + 1
    #     print(l_value)
    #     print(r)
    #     flag = False


