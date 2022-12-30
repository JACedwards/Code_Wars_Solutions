#couldn't figure out how to deal with None in list/array
def find_needle(haystack):

    for x in haystack:
        if x == None:
            x = 'junk'
        else:
            if x == 'needle':
                print("found the needle at position " + str(haystack.index("needle")))
                break
                
            else:
                continue

print(find_needle(['hay', None, 'needle', 'guuber']))
