def two_sort(array):
    build = ''
    output = ''
    array.sort()
    print(array)
    array = array[0]
    for n in array:
        print(n)
        build = n + "***"
        output = output + build
    output = output[0:-3]
    return output




print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))