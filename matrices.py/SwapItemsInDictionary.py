# In this kata, you will take the keys and values of a dict and swap them around.

# You will be given a dictionary, and then you will want to return a dictionary with the old values as the keys, and list the old keys as values under their original keys.

# For example, given the dictionary: {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'},

# you should return: {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}

# Notes:
# The dictionary given will only contain strings
# The dictionary given will not be empty
# You do not have to sort the items in the lists

#Pseudo:
# extract list of keys
# extract list of values
# make values set, then back to list
#loop through values, creating list of keys for each value
#create final dictionary of former values as keys and lists as values

def switch_dict(dic):

    values = list(set([y for y in dic.values()]))
    # values = set(values)
    # values = list(values)
    output = {}

    lst = []
    for w in values:
        for k,v in dic.items():
            if w == v:
                lst.append(k)
        output[w] = lst
        lst=[]
    return output

print(switch_dict({'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}))
# you should return: {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}