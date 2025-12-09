import math
import re

from shapely import Polygon

parser = re.compile(r"-?\d+")
dots = [tuple(map(int, parser.findall(line))) for line in open("input/input.in").readlines()]
dots_set = set(dots)
print()


def area(dot, dot2):
    return  (math.fabs(dot[1] - dot2[1]) + 1)*(math.fabs(dot[0] - dot2[0]) + 1)


poly = Polygon(dots)
areas = []
for i, dot in enumerate(dots):
    for dot2 in dots[i:]:
        if dot == dot2 or dot[1] == dot2[1] or dot[0] == dot2[0]:
            continue
        square = Polygon([dot, (dot[0], dot2[1]), dot2, (dot2[0], dot[1])])
        if poly.contains(square):
            areas.append((dot, dot2, area(dot, dot2)))


distances = sorted(areas, key=lambda x: x[-1], reverse=True)
print(distances[0][-1])

