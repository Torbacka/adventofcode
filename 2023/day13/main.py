import re
from collections import defaultdict

parser = re.compile("-?\d+")
horizontal = [[line for line in graph.strip().split("\n")] for graph in open("input/input.in").read().strip().split("\n\n")]


def compare(i, graph):
    start = graph[:i]
    end = graph[i:(i + len(start))]
    if len(start) > len(end):
        start = start[(len(start) - len(end)):]
    start.reverse()
    return start == end


vertical = []
for i, graph in enumerate(horizontal):
    vertical.append([])
    for y, row in enumerate(graph):
        for x, value in enumerate(row):
            if len(vertical[i]) <= x:
                vertical[i].append('')
            vertical[i][x] += value
sums = 0
for i in range(len(horizontal)):
    h_value = 0
    v_value = 0
    for n in range(1, len(horizontal[i])):
        if compare(n, horizontal[i]):
            h_value = n
            break
        if compare(n, vertical[i]):
            v_value = n
            break
    sums += (100*h_value) + (v_value)

print(sums)