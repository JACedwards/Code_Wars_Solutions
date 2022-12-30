def pipe_fix(nums):

    mi = min(nums)
    mx = max(nums)
    output = []

    for n in range(mi, mx+1):
        output.append(n)

    return output



print(pipe_fix([1, 2, 3, 12]))