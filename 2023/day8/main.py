import math
import re

parser = re.compile("-?\w+")
path, graph_line = open("input/input.in").read().split("\n\n")
graph = {parser.findall(line)[0]: (parser.findall(line)[1], parser.findall(line)[2]) for line in graph_line.split("\n")}

starts = [key for key, _ in graph.items() if key[-1] == 'A']
index = 0

indexes = []
while len(indexes) < 6:
    print(starts)
    for i, s in enumerate(starts):
        direction = path[index % len(path)]
        if 'R' == direction:
            starts[i] = graph[s][1]
        else:
            starts[i] = graph[s][0]
        if starts[i][-1] == 'Z':
            indexes.append(index+1)
    index += 1

print(math.lcm(*indexes))
