# def count_by(x, n):

def count_by(x, n):

    list_1 = []
   

    for i in range(n+2)[1:-1]:
        y = x * i
        list_1.append(y)
    return list_1
        
print(count_by(2,5))
