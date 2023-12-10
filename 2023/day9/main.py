import math
import re

parser = re.compile("-?\d+")
data = [[int(x) for x in parser.findall(line.strip())] for line in open("input/input.in").readlines()]
sums = 0
for line in data:
    series = [line.copy()[::-1]]
    while sum(series[-1]) != 0:
        s = series[-1]
        new = []
        for i in range(0, len(series[-1]) -1):
            new.append(s[i + 1] - s[i])
        series.append(new)
    sums += sum([s[-1] for s in series if len(s) > 0])
    print(sums)

print(sums)

