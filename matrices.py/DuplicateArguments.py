# Complete the solution so that it returns true if it contains any duplicate argument values. Any number of arguments may be passed into the function.

# The array values passed in will only be strings or numbers. The only valid return values are true and false.

# Examples:

# solution(1, 2, 3)             -->  false
# solution(1, 2, 3, 2)          -->  true
# solution('1', '2', '3', '2')  -->  true

# test.assert_equals(solution(1, 2, 3, 1, 2), True)
# test.assert_equals(solution(1, 1), True)
# test.assert_equals(solution(1, 0), False)
# test.assert_equals(solution(1, 0, 2, 3, 4), False)
# test.assert_equals(solution(), False)


def solution(*args):
    checker = []
    for c in args:
        if c not in checker:
            checker.append(c)
        elif c in checker:
            return True

    return False

print(solution(1, 0))