# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):

    numbers.sort()
    print(numbers)
    for i in range(len(numbers)):
        if numbers[i] > 0:
            x=numbers[i]
            y=numbers[i+1]
            output = x + y
            return output

print(sum_two_smallest_numbers([19, 5, 42, 2, 77, -5, -1, -100]))