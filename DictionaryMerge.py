# Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.

# The keys in the given dictionaries can overlap. In that case you should combine all source values in an array. Duplicate values should be preserved.

# Here is an example:

# source1 = {"A": 1, "B": 2} 
# source2 = {"A": 3}

# result = merge(source1, source2);
# // result should have this content: {"A": [1, 3]}, "B": [2]}
# You can assume that only valid dictionaries are passed to your function. The number of given dictionaries might be large. So take care about performance.

#psuedo:
# loop through dictionaries

def merge(*dicts):
    lst = [x for x in dicts]
    
    master_d = {}
    holding_lst = []
    for d in dicts:
        for ky in d.keys():
            holding_lst.append(ky)
    values = set(holding_lst)
    values = list(values)
    values.sort()
    #['A', 'B']

    holding_lst2 = []
    for let in values:
        #'A'
        for d in lst:
            #{"A": 1, "B": 2}
            for k, v in d.items():
                if k == let:
                    holding_lst2.append(v)
            print(holding_lst2)
            break








            


print(merge({"A": 1, "B": 2}, {"A": 3}))

# // result should have this content: {"A": [1, 3]}, "B": [2]}