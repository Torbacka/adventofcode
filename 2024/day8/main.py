import re
from collections import defaultdict

parser = re.compile(r"-?\d+")

data = [[i for i in line.strip()] for line in open("input/input.in").readlines()]
antennas = defaultdict(list)
for y, line in enumerate(data):
    for x, value in enumerate(line):
        if value != '.':
            antennas[value].append((x, y))


def check_boundary(x_1, y_1):
    return 0 <= x_1 < len(data[0]) and 0 <= y_1 < len(data)


def draw_grid():
    for y, line in enumerate(data):
        print()
        for x, value in enumerate(line):
            print(value, end='')


result = set()
for antenna, locations in antennas.items():
    for l1 in locations:
        for l2 in locations:
            if l1 != l2:
                y_diff = (l2[1] - l1[1])
                x_diff = (l2[0] - l1[0])
                result.add((l2[0], l2[1]))
                data[l2[1]][l2[0]] = '#'
                x,y = (l2[0] + x_diff, l2[1] + y_diff)
                while check_boundary(x, y):
                    data[y][x] = '#'
                    result.add((x ,y))
                    x, y = (x + x_diff, y + y_diff)


print(len(result))
draw_grid()