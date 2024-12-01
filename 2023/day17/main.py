import functools
import re
import sys
from collections import defaultdict

parser = re.compile("-?\d+")
graph = [[int(i) for i in line.strip()] for line in open("input/input.in").readlines()]


def direction(node1, node2):
    dx = 0 if node1[0] == node2[0] else 1
    dy = 0 if node1[1] == node2[1] else 1
    return dx, dy


def boundry(graph, coordinate):
    x, y = coordinate
    x = 0 if x < 0 else x
    x = len(graph[0]) - 1 if x == len(graph[0]) else x
    y = 0 if y < 0 else y
    y = len(graph) - 1 if y == len(graph) else y
    return x, y


def get_directions(path):
    last_dirs = set()
    last_dirs.add(direction(path[-1], path[-2]))
    last_dirs.add(direction(path[-2], path[-3]))
    last_dirs.add(direction(path[-3], path[-4]))
    last_dirs.add(direction(path[-4], path[-5]))
    return last_dirs


def find_neighbours(graph, node, path):
    x, y = node
    neighbours = set()
    if len(path) < 5 or len(get_directions(path)) > 1:
        neighbours = {boundry(graph, (x, y + 1)),
                      boundry(graph, (x, y - 1)),
                      boundry(graph, (x + 1, y)),
                      boundry(graph, (x - 1, y))}
        if len(path) > 1 and path[-2] in neighbours:
            neighbours.remove(path[-2])
        if node in neighbours:
            neighbours.remove(node)
    else:
        dx, dy = direction(path[-1], path[-2])
        if dy != 0:
            neighbours = {boundry(graph, (x + 1, y)),
                          boundry(graph, (x - 1, y))}
        if dx != 0:
            neighbours = {boundry(graph, (x, y + 1)),
                          boundry(graph, (x, y - 1))}
    r = set()
    paths = set(path)
    for n in neighbours:
        if n not in paths:
            r.add(n)
    return r

def print_graph(graph, path):
    for y, row in enumerate(graph):
        for x, value in enumerate(row):
            if (x, y) in path:
                print("*", end="")
            else:
                print(".", end="")
        print()


def compare(node1, node2):
    return node1[1] - node2[1]


def bfs(graph, start, end):
    queue = [(start, 0, [start])]
    visited = []
    while queue:
        node = queue.pop(0)
        for neighbour in find_neighbours(graph, node[0], node[2]):
            cost = node[1] + graph[neighbour[1]][neighbour[0]]
            path = node[2].copy()
            path.append(neighbour)
            queue.append((neighbour, cost, path))
            if neighbour == end:
                visited.append({
                    "path": path,
                    "cost": cost
                })
        if len(queue) > 200000:
            queue = sorted(queue, key=functools.cmp_to_key(compare))[:100000]
    return visited


end_x, end_y = (len(graph[0]) - 1, len(graph) - 1)
visited = d = bfs(graph, (0, 0), (end_x, end_y))
cost, end_path = next((value["cost"], value["path"]) for node, value in visited.items() if (0, 0) == node)
print_graph(graph, set(end_path))
print(cost)
