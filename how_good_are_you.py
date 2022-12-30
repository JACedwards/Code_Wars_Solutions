import statistics

def better_than_average(class_points, your_points):

    class_points.append(your_points)
    output = statistics.mean(class_points)
    if output < your_points:
        return True
    else:
        return False

    

print(better_than_average([2, 2], 2))