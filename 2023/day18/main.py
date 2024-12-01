from shapely import Polygon, affinity

data = [line.strip().split() for line in open("input/input.in").readlines()]

start = (0, 0)
direction = (0, 0)
edges = [start]

for line in data:
    distance = int(line[2][2:-1][:-1], 16)
    dir = int(line[2][2:-1][-1])
    if dir == 0:
        direction = (1, 0)
    elif dir == 3:
        direction = (0, -1)
    elif dir == 2:
        direction = (-1, 0)
    elif dir == 1:
        direction = (0, 1)
    edge = (edges[-1][0] + direction[0] * distance, edges[-1][1] + direction[1] * distance)
    edges.append(edge)

polygon = Polygon(edges)
buffered = polygon.buffer(0.5, join_style=2)
print(buffered.area)
