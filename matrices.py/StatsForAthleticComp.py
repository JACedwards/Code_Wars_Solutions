# You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:

# "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

# Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by ,  or ,.

# To compare the results of the teams you are asked for giving three statistics; range, average and median.

# Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

# Mean or Average : To calculate mean, add together all of the numbers and then divide the sum by the total count of numbers.

# Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

# Your task is to return a string giving these 3 values. For the example given above, the string result will be

# "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

# of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`

# where hh, mm, ss are integers (represented by strings) with each 2 digits.

# Remarks:
# if a result in seconds is ab.xy... it will be given truncated as ab.
# if the given string is "" you will return ""

# Pseudo:
# Split string
#strip 0 of beginning
#transform substrings into integers through slicing, multiplying by 3600 and 60 as you go....

def stat(strg):
    if strg == '':
        return ''

    lst_strg = strg.split()
    # print(lst_strg)

    t_lst_split = []
    running = 0
    for t in lst_strg:
        t = t.lstrip('0')
        t =  t.rstrip(',')
        t_lst = t.split('|')
        t_lst_split.append(t_lst) 

    conv_to_sec = []
    for n in t_lst_split:
        running = running + (int(n[0]) * 3600)
        running = running + (int(n[1]) * 60)
        running = running + int(n[2])
        conv_to_sec.append(running)
        running = 0
    
    #conv_to_sec = [4559, 6426, 4640, 5554, 7397]

    print(conv_to_sec)
    conv_to_sec.sort()
    #conv_to_sec - sorted:  [4559, 4640, 5554, 6426, 7397]

    #____________find RANGE________#
    output = ''
    rng_str = ''
    hour = 0
    minute = 0
    second = 0
    minute_in_sec = 0

    rng = conv_to_sec[-1] - conv_to_sec[0]
    # print(rng)
    if rng >= 3600:
        hour = rng // 3600
        if hour < 9:
            rng_str = f'0{str(hour)}|'

        else:
            rng_str = f'{str(hour)}|'

        #'48|
        minute_in_sec = rng - (hour * 3600)
    else:
        rng_str = f'00|'
        minute_in_sec = rng
    # print(rng_str)
    # print(minute_in_sec)
    #2838
    #figure minute string

    if minute_in_sec >= 60:
        minute = minute_in_sec // 60
        if minute < 9:
            rng_str = f'{rng_str}0{str(minute)}|'
        else:
            rng_str = f'{rng_str}{str(minute)}|'
        #'48|
        second = minute_in_sec - (minute * 60)
    else:
        rng_str = f'{rng_str}00|'
        second = minute_in_sec
    
    rng_str=f'{rng_str}{second}'
    # print(rng_str)

    output = f'Range: {rng_str}'
    # print(output)



    #____________find ARVERAGE________#
    ave_in_sec = int(sum(conv_to_sec) / len(conv_to_sec))
    # print(ave_in_sec)

    if ave_in_sec >= 3600:
        hour = ave_in_sec // 3600
        if hour < 9:
            ave_str = f'0{str(hour)}|'

        else:
            ave_str = f'{str(hour)}|'
        #'48|
        minute_in_sec = ave_in_sec - (hour * 3600)
    else:
        ave_str = f'00|'
        minute_in_sec = ave_in_sec
    # print(rng_str)
    # print(minute_in_sec)
    #2838
    #figure minute string

    if minute_in_sec >= 60:
        minute = minute_in_sec // 60
        if minute < 9:
            ave_str = f'{ave_str}0{str(minute)}|'
        else:
            ave_str = f'{ave_str}{str(minute)}|'
        #'48|
        second = minute_in_sec - (minute * 60)
    else:
        ave_str = f'{ave_str}00|'
        second = minute_in_sec
    if second < 9:
        ave_str=f'{ave_str}0{second}'
    else:
        ave_str=f'{ave_str}{second}'
    # print(rng_str)

    output = f'{output} Average: {ave_str}'
    # print(output)



    # <><><>Median output messed up see Code Wars test

    #____________find MEDIAN________________#
    print(conv_to_sec)
    if len(conv_to_sec) % 2 != 0:
        goober = (int(len(conv_to_sec) / 2))
        print(f'this is goober:  {goober}')
        mean_in_sec = conv_to_sec[(int(len(conv_to_sec) / 2))]
        print(f'this is mean_in_sec for odd:  {mean_in_sec}')

    else:
        mean_in_sec = int(((conv_to_sec[(int(len(conv_to_sec) / 2))]) +  (conv_to_sec[(int(len(conv_to_sec) / 2))-1]))  / 2 ) 
        
        print(f'mean in seconds: {mean_in_sec}')
        
    

    if mean_in_sec >= 3600:
        hour = mean_in_sec // 3600
        if hour < 9:
            mean_str = f'0{str(hour)}|'

        else:
            mean_str = f'{str(hour)}|'
        #'48|
        minute_in_sec = mean_in_sec - (hour * 3600)
    else:
        mean_str = f'00|'
        minute_in_sec = mean_in_sec
    # print(rng_str)
    # print(minute_in_sec)
    #2838
    #figure minute string

    if minute_in_sec >= 60:
        minute = minute_in_sec // 60
        if minute < 9:
            mean_str = f'{mean_str}0{str(minute)}|'
        else:
            mean_str = f'{mean_str}{str(minute)}|'
        #'48|
        second = minute_in_sec - (minute * 60)
    else:
        mean_str = f'{mean_str}00|'
        second = minute_in_sec
    if second < 9:
        mean_str=f'{mean_str}0{second}'
    else:
        mean_str=f'{mean_str}{second}'
    # print(rng_str)

    output = f'{output} Median: {mean_str}'
    return output



# print(stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"))
# print(stat("50|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"))
print(stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17, 2|3|17"))
# print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))

#              'Range: 01|01|18 Average: 01|38|05 Median: 01|17|20' 
# should equal 'Range: 01|01|18 Average: 01|38|05 Median: 01|32|34'