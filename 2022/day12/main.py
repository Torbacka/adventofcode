import string
from collections import defaultdict

data = [[c for c in line.strip()] for line in open("input.in").readlines()]

dirs = [
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0)
]
graph = defaultdict(lambda: 'Z')

for y, line in enumerate(data):
    for x, value in enumerate(line):
        graph[(x, y)] = value

letters = string.ascii_lowercase + string.ascii_uppercase


def height(c):
    return ord(c.replace('S', 'a').replace('E', 'z'))


def can_move(start, stop):
    return height(graph[stop]) - height(graph[start]) <= 1


def get_adjecent_nodes(node):
    x = node[0]
    y = node[1]
    yield from [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def get_value(lookup_x, lookup_y):
    return ord(data[lookup_y][lookup_x].replace('E', 'z'))


def breadth_first_search(start, end):
    visited = set()
    visited.add(start)

    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if graph[node] == end:
            return path
        for adjacent in get_adjecent_nodes(node):
            if can_move(adjacent, node) and \
                    adjacent not in visited and \
                    adjacent not in queue:
                visited.add(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


start = None
for node, value in graph.items():
    if value == 'E':
        start = node
path = breadth_first_search(start, 'S')
print(len(path) - 1)
path = breadth_first_search(start, 'a')
print(len(path) - 1)
