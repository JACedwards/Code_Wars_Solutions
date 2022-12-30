def divisible_by(numbers, divisor):

    build = []

    for n in numbers:
        if n % divisor == 0:
            build.append(n)
        else:
            continue

    return build



print(divisible_by([1, 2, 3, 4, 5, 6], 2))