def rps(p1, p2):

    r = 'rock'
    p = 'paper'
    s = 'scissors'

    if p1 == r and p2 == p:
        return "Player 2 won!"
    elif p1 == r and p2 == s:
        return "Player 1 won!"
    elif p1 == r and p2 == r:
        return "Draw!"

    if p1 == s and p2 == p:
        return "Player 1 won!"
    elif p1 == s and p2 == r:
        return "Player 2 won!"
    elif p1 == s and p2 == s:
        return "Draw!"

    if p1 == p and p2 == s:
        return "Player 2 won!"
    elif p1 == p and p2 == r:
        return "Player 1 won!"
    elif p1 == p and p2 == p:
        return "Draw!"
        
print(rps('scissors','paper'))