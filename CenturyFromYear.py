def century(year):

    begin = 1
    end = 101
    output = 1

    while True:
        if year in range(begin, end):
            output = output
            return output
             
        else:
            begin = begin +100
            end = end + 100