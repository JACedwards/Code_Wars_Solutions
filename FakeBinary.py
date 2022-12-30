def fake_bin(x):
    y = ''
    x = list(x)
    for n in x:
        if int(n) < 5:
            n = 0
            n= str(n)
            y=f'{y}{n}'

        elif int(n) >= 5:
            n = 1
            n= str(n)
            y=f'{y}{n}'

    return y



print(fake_bin("16"))