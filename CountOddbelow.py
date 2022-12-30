# def odd_count(n):
#     count = 0

#     rang = range(1,n)
#     for n in rang:
#         if n % 2 == 0:
#             count = count + 1
#         else:
#             continue
#     return(count)

# import math

def odd_count(n):
    
    return len(range(1,n,2))
 



    #tested fine on code wars, but attempt timed out

   








print(odd_count(15))