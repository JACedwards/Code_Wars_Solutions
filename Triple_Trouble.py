def triple_trouble(one, two, three):
    output_short = ""
    output_final = ""
    p=1
    while p <= len(one):

        for i in range(len(one)):
            output_short = one[i] + two[i] + three[i]
            output_final = output_final + output_short
            p+=1
            output_short = ""
    return output_final
            




print(triple_trouble("aaa","bbb","ccc"))