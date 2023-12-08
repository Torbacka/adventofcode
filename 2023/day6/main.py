import math
import re
from functools import reduce

parser = re.compile("-?\d+")
data = [[int(x) for x in parser.findall(line.strip())] for line in open("input/input.in").readlines()]
time_difference = []
for i in range(len(data[0])):
    total_time = data[0][i]
    total_distant = data[1][i]
    min_time = (total_time / 2) - math.sqrt(math.pow(total_time / 2, 2) - total_distant)
    max_time = (total_time / 2) + math.sqrt(math.pow(total_time / 2, 2) - total_distant)
    time_difference.append(round(max_time - min_time))
print(f"part1: {reduce(lambda a, b: a*b, time_difference)}")
print(f"part2: {time_difference}")