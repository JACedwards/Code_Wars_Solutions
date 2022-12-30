def reverse_seq(n):
    seq = []
    for s in range(1,n+1):
        seq.append(s)
    output = seq.reverse()
    return output




print(reverse_seq(5))