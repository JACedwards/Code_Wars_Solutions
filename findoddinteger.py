def find_it(seq):

    for n in seq:
        if seq.count(n) % 2 != 0:
            return n
        else: 
            continue



print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))