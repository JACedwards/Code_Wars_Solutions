def solution(a, b):
    counta = 0
    countb = 0

    for i in range(0, len(a)-1):
        if(a[1] != ''):
            counta = counta +1
    for i in range(len(b)-1):
        if(b[1] != ''):
            countb = countb +1  

    if countb > counta:
        return f"{a}{b}{a}"

    else:
        return f"{b}{a}{b}"

print(solution("1", "22"))

        