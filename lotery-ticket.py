# Time to win the lottery!

# Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot.

# Example ticket:

# [ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
# To do this, you must first count the 'mini-wins' on your ticket. Each subarray has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini win. Note you can only have one mini win per sub array.

# Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

# All inputs will be in the correct format. Strings on tickets are not always the same length.

# Example = [['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2 == Loser! (no matches, mini wins)

# print(ord(u"$"))   # Unicode code of $ character
# #Output
# #36

#Pseudo:
#  loop through array:
#    loop through 0 index of each sub-array
#    check each character in string against unicode value of index 1
#    if match, add one to mini-win (and break)
#    compare mini-win tally to "win" input.
#    if greater than or equal to return "Winner!"



def bingo(ticket,win):
    
    mini_win = 0
    for arr in ticket:
        for i in range(len(arr[0])):
            print(arr[0][i])
            print(ord(arr[0][i]))
            if arr[1] == ord(arr[0][i]):
                mini_win += 1
    print(f'This is mini_win: {mini_win}')
    if mini_win >= win:
        return 'Winner!'
    
    else:
        return 'Loser!'


print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2))
# print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1))