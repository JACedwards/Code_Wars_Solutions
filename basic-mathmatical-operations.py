
import operator as op

def basic_op(operator, value1, value2,):
    
    if operator == '+':
        x = op.add

    elif operator == '-':
        x = op.sub

    elif operator == '/':
        x = op.truediv

    elif operator == '*':
        x = op.mul

    output = x(value1, value2)

    return output

print(basic_op('+', 4, 7))


