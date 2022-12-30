def solution(number):
    
    number = range(number)
    output = 0
    for n in number:
        if n % 3 == 0 or n % 5 == 0:
            output = output + n
        else:
            continue       

    
    return output







print(solution(15))