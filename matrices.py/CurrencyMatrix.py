# On the Forex Market the currency symbols for exchange between two currencies are put together in regards to their strength and weakness. The order of the currency strength is as follows:

# "EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"

# So for AUD the currency matrix would be as follows EURAUD, GBPAUD, AUDNZD, AUDUSD, AUDCAD, AUDCHF, AUDJPY

# Your goal is to generate this currency matrix for a given currency. You can assume that the passed in currency is a valid one.
# tests = (
#     ('EUR', ['EURGBP', 'EURAUD', 'EURNZD', 'EURUSD', 'EURCAD', 'EURCHF', 'EURJPY']),
#     ('GBP', ['EURGBP', 'GBPAUD', 'GBPNZD', 'GBPUSD', 'GBPCAD', 'GBPCHF', 'GBPJPY']),
#     ('AUD', ['EURAUD', 'GBPAUD', 'AUDNZD', 'AUDUSD', 'AUDCAD', 'AUDCHF', 'AUDJPY']),
# )

#Psuedo:
#  create list of currency symbols
#  loop through list of symbols, comparing to currency input:
#    if currency != symbol:
#      concatinate currency to the back of symbol (and append to output list)
#    if currency == symbol:
#        skip, then
#        start concatenating currency on front of symbol

def generate_currency_matrix(currency):

    symbols = ["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
    concat = ''
    output = []

    for s in symbols:
        if s != currency:
            concat = f'{s}{currency}'
            output.append(concat)

        elif s == currency:
            index = symbols.index(s)
            symbols = symbols[index+1:]
            for s in symbols:
                concat = f'{currency}{s}'
                output.append(concat)
            break
    return output





print(generate_currency_matrix('AUD'))

#     ('GBP', ['EURGBP', 'GBPAUD', 'GBPNZD', 'GBPUSD', 'GBPCAD', 'GBPCHF', 'GBPJPY']),


