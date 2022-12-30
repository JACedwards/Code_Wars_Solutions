# You're running an online business and a big part of your day is fulfilling orders. As your volume picks up that's been taking more of your time, and unfortunately lately you've been running into situations where you take an order but can't fulfill it.

# You've decided to write a function fillable() that takes three arguments: a dictionary stock representing all the merchandise you have in stock, a string merch representing the thing your customer wants to buy, and an integer n representing the number of units of merch they would like to buy. Your function should return True if you have the merchandise in stock to complete the sale, otherwise it should return False.

# Valid data will always be passed in and n will always be >= 1.

#pseudo:
#get quantity of merch item from stock dictionary
#if quantity is less than n, return False
#else return true

def fillable(stock, merch, n):
    quantity = stock.get(merch)
    if quantity < n:
        return False
    return True



print(fillable(stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }, merch='football', n=3))