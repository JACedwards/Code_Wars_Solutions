x = [1, 2, [3, 4, [5]]]

for y in x:
    if isinstance(y, list):
        print(y)
