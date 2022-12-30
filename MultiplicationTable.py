# Your task, is to create NxN multiplication table, of size provided in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

#Psuedo:
# counter_row set to 1
# counter_table set to 0
# output = []
# while loop, appending and resetoing whenever get to "size"
# +=1 counters


#___________misunderstood instructions___thought just supposed to do table with consecutive numbers (works for that)_____________

# def multiplication_table(size):

#     n = 1
#     counter_row = 0
#     counter_table = 1
#     row_collector = []
#     output = []

#     while counter_row <= size and counter_table <= size:
#         if counter_row == size:
#             output.append(row_collector)
#             counter_table +=1
#             counter_row = 0
#             row_collector = []
#         else:
#             row_collector.append(n)
#             counter_row +=1
#             n+=1

#     return output



# print(multiplication_table(3))

#_________multiplication version


# 1 2 3
# 2 4 6
# 3 6 9

#pseudo
# create master list:
#    consecutive numbers from 1 to 'size'
#   # each row loops through master row, multiplying by + 1 per row
#  append each row to output


def multiplication_table(size):

    n = 1
    counter_row = 1
    counter_table = 1
    row_collector = []
    output = []
    base_row = []


    while counter_row <= size:
        base_row.append(n)
        counter_row +=1
        n+=1
    output.append(base_row)

    # start building rest of table based on base row
    i = 0
    base = output[0]
    counter_row = 0
    counter_table = 2
    row_collector = []
    starter = 2

    while counter_row <= size and counter_table <= size:
        if counter_row == size:
            output.append(row_collector)
            counter_table +=1
            counter_row = 0
            row_collector = []

            i=0
            starter +=1
            
        else:
            x = (starter) * base[i]
            row_collector.append(x)
            counter_row +=1
            i+=1


    return output

print(multiplication_table(3))

