# For a given string s find the character c (or C) with longest consecutive repetition and return:

# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

# For empty string return:

# ('', 0)
# In JavaScript: If you use Array.sort in your solution, you might experience issues with the random tests as Array.sort is not stable in the Node.js version used by CodeWars. This is not a kata issue.

# Happy coding! :)


def longest_repetition(chars):

    letter = ''
    final_letter = ''
    running = 1
    total_num = 0
    left = 0
    right = 1

    while right <= len(chars) - 1:
        
        if chars[left] == chars[right] and right == len(chars) - 1:
            print(chars[left], chars[right] )
            running += 1
            if running > total_num:
                total_num = running
                final_letter = letter
                return (final_letter, total_num)
            else:
                return (final_letter, total_num)

        
        elif chars[left] == chars[right]:
            print(chars[left], chars[right] )
            running += 1
            letter = chars[left]
            left += 1
            right += 1
        else:
            letter = chars[right]
            print(chars[right] )
            if running > total_num:
                total_num = running
                final_letter = chars[left]

            running = 1
            letter = chars[right]
            left += 1
            right +=1

    return (final_letter, total_num)


print(longest_repetition("aaaabb"))