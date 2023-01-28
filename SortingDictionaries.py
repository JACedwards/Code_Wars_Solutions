# Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?

# Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

# The list must be sorted by the value and be sorted largest to smallest.

# Examples
# sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
# sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]

# def sort_dict(d):
    
#     lst_to_srt = []
#     for v in d.values():
#         lst_to_srt.append(v)
#     lst_to_srt.sort(reverse=True)
#     print(lst_to_srt)

#     utility = []
#     output = []
#     for value in lst_to_srt:
#         for key, val in d.items():
#             if val == value:
#                 utility.append((key, val))

    
#     return utility




# print(sort_dict({3:1, 2:2, 1:3}))

def sort_dict(d):
    
    sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)
    
    return sorted_d


print(sort_dict({3:1, 2:2, 1:3}))