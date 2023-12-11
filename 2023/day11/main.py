import re
from collections import defaultdict


def manhattan(p1, p2, expand_x, expand_y, size):
    size -= 1
    x_sum = sum(1 for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])) if x in expand_x)
    y_sum = sum(1 for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])) if y in expand_y)
    return abs(p1[0] - p2[0]) + (x_sum * size) + abs(p1[1] - p2[1]) + (y_sum * size)


parser = re.compile("-?\d+")
graph = [line.strip() for line in open("input/input.in").readlines()]

rotate = defaultdict(list)

for y, row in enumerate(graph):
    for x, value in enumerate(row):
        rotate[x].append(value)

expand_x = set(i for i, row in rotate.items() if all(map(lambda i: i == '.', row)))
expand_y = set(i for i, row in enumerate(graph) if all(map(lambda i: i == '.', row)))


# expanded_graph = defaultdict(list)
# offset = 0
# for y, row in enumerate(graph):
#    for x, value in enumerate(row):
#        if x in expand_x:
#            expanded_graph[y + offset].append('.')
#        expanded_graph[y + offset].append(value)
#    if y in expand_y:
#        offset += 1
#        expanded_graph[y + offset].extend(['.' for _ in range(0, len(graph) + len(expand_x))])
def calculate_manhattan(coordinates, size):
    sums = 0
    for i, coordinate in enumerate(coordinates):
        for n in range(i + 1, len(coordinates)):
            sums += manhattan(coordinate, coordinates[n], expand_x, expand_y, size)
    return sums

coordinates = []
for y, row in enumerate(graph):
    for x, value in enumerate(row):
        if value == '#':
            coordinates.append((x, y))

print(f"part 1: {calculate_manhattan(coordinates, 2)}")
print(f"part 1: {calculate_manhattan(coordinates, 1000000)}")
