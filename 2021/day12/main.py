import re
from collections import Counter
parser = re.compile("-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]


def main():
    print()
    print(len(visit_all(get_graph())))


def visit_all(graph):
    start = 'start->start'
    paths = set()
    paths.add(start)
    final_path = []
    while paths:
        path = paths.pop()
        visited = path.split('->')
        if visited[-1] not in graph:
            continue
        if visited[-1] == 'end':
            continue
        for i, con in enumerate(graph[visited[-1]]):
            if con == 'end':
                final_path.append(f"{path}->{con}")
            elif con == 'start':
                continue
            elif con.islower():
                small_caves = [cave for cave in path.split('->') if cave.islower() and cave != 'start' and cave != 'end']
                already_visted_small_twice = False
                counter = Counter(small_caves)
                for cave, number in counter.items():
                    if number >1:
                        already_visted_small_twice = True
                if not already_visted_small_twice or (con not in counter.keys() and already_visted_small_twice):
                    paths.add(f"{path}->{con}")
                continue
            paths.add(f"{path}->{con}")
    return final_path

def get_graph():
    graph = {
    }
    for line in data:
        start, dest = line.split("-")
        if start not in graph:
            graph[start] = [dest]
        else:
            graph[start].append(dest)
        if dest not in graph:
            graph[dest] = [start]
        else:
            graph[dest].append(start)
    return graph


if __name__ == '__main__':
    main()

