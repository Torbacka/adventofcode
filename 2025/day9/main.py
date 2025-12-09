import math

import math
import re

parser = re.compile(r"-?\d+")
dots = [tuple(map(int, parser.findall(line))) for line in open("input/input.in").readlines()]
print()


def distance(dot, dot2):
    return  (math.fabs(dot[1] - dot2[1]) + 1)*(math.fabs(dot[0] - dot2[0]) + 1)


distances = []

for i, dot in enumerate(dots):
    for dot2 in dots[i:]:
        if dot == dot2:
            continue
        distances.append((dot, dot2, distance(dot, dot2)))

distances = sorted(distances, key=lambda x: x[-1], reverse=True)
print(distances[0][-1])
