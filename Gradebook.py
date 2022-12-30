# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

# Examples:

# get_grade(95, 90, 93), "A"
# get_grade(70, 70, 100), "B"

def get_grade(s1, s2, s3):

    ave= (s1+s2+s3) / 3
    print(ave)

    if ave >= 90:
        grade = 'A'
    elif ave >=80:
        grade = 'B'
    elif ave >=70:
        grade = 'C'
    elif ave >=60:
        grade = 'D'
    else:
        grade = 'F'

    return grade
    

print(get_grade(95, 90, 93))
