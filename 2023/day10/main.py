import re
from collections import defaultdict

from shapely import Point, Polygon
from termcolor import colored

parser = re.compile("-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]

x, y = [(x, y) for y, row in enumerate(data) for x, value in enumerate(data[y]) if value == 'S'][0]
distance = 1
nest_graph = [(x, y)]
dx = 1
dy = 0

for dx, dy in [(0, 1)]:
    x += dx
    y += dy
    value = data[y][x]
    while value != 'S':
        if value == '|':
            pass
        elif value == '-':
            pass
        elif value == 'L':
            dy = -1 if dy == 0 else 0
            dx = 1 if dx == 0 else 0
        elif value == 'J':
            dy = -1 if dy == 0 else 0
            dx = -1 if dx == 0 else 0
        elif value == '7':
            dy = 1 if dy == 0 else 0
            dx = -1 if dx == 0 else 0
        elif value == 'F':
            dy = 1 if dy == 0 else 0
            dx = 1 if dx == 0 else 0
        nest_graph.append((x, y))
        x += dx
        y += dy
        distance += 1
        value = data[y][x]
    print(distance / 2)

polygon = Polygon(nest_graph)
path = set(nest_graph)
sums = 0
for y, row in enumerate(data):
    for x, value in enumerate(data[y]):
        if (x,y) in path:
            print(colored(value, 'green', attrs=['bold']), end="")
        elif value == '.':
            print(colored(value, 'yellow', attrs=['bold']), end="")
        else:
            print(value, end="")
        if value not in path and polygon.contains(Point(x, y)):
            sums += 1
    print()

print(sums)

