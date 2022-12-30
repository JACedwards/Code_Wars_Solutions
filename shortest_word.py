# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):

    count = 0
    for i in range(len(s)):
        if s[i] != ' ':
            count += 1
        if s[i] == ' ':

            break

    count_2 = 0
    running_count = count
    count += 1 
    for i in range(count, len(s)):
        if s[i] != ' ':
            count_2 += 1
        elif s[i] == ' ':
            if count_2 < running_count:
                running_count = count_2
                count_2 = 0
            else:
                count_2 = 0

    return running_count



print(find_short("Lets all go on holiday somewhere very cold"))