# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def calcFunctions(input):
    goober = input.split('(')
    print(goober)
    
    nums_let = ['1','2','3','4','5','6','7','8','9']
    nums_int = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    nums_dct = {nums_int[i]: nums_let[i] for i in range(len(nums_let))}
    print(nums_dct)

    oper_sym = ['+', '-', '/', '*']
    oper_let = ['plus', 'minus', 'divided_by', 'times']
    oper_dct = {oper_let[i]:oper_sym[i] for i in range(len(oper_sym))}
    print(oper_dct)

    one = nums_dct[goober[0]]
    two = oper_dct[goober[1]]
    three = nums_dct[goober[2]]
    concat = f'{one}{two}{three}'
    output = eval(concat)
    output = int(output)
    return output, type(output)






print(calcFunctions('six(divided_by(two()))'))