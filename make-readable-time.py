# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

#Psuedo:
#  floor divide seconds by number of seconds in an hour
#  concatinate that number onto output, adding 0 to beginning to anything less than 10
#  multiply number of hours by seconds in an hour
#  subtract that from running total
#  repeat for minutes and seconds

#seconds per hour = 3600
#seconds per minute = 60


def make_readable(seconds):

    output = ''

    hour_check = seconds // 3600

    if hour_check > 9:
        output = f'{hour_check}:'
    elif hour_check < 10 and hour_check >= 0:
        output = f'0{hour_check}:'
    else:
        output = '00:'

    seconds = seconds - (hour_check * 3600)

    minute_check = seconds // 60

    if minute_check > 9:
        output = f'{output}{minute_check}:'
    elif minute_check < 10 and minute_check >= 0:
        output = f'{output}0{minute_check}:'
    else:
        output = f'{output}00:'

    seconds = seconds - (minute_check * 60)

    if seconds > 9:
        output = f'{output}{seconds}'
    else:
        output = f'{output}0{seconds}'

    return output

print(make_readable(5))


# test.assert_equals(make_readable(0), "00:00:00")
# test.assert_equals(make_readable(5), "00:00:05")
# test.assert_equals(make_readable(60), "00:01:00")
# test.assert_equals(make_readable(86399), "23:59:59")
# test.assert_equals(make_readable(359999), "99:59:59")
