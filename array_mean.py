def find_average(nums):

    if nums == []:
        return 0
    sums = sum(nums)
    length = len(nums)
    return sums / length
    




print(find_average([16, 4]))