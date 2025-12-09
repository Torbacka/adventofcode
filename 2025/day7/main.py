import re

parser = re.compile(r"-?\d+")
grid = [[l for l in line.strip()] for line in open("input/input.in").readlines()]
beams = set()
split_count = 0
for line in grid:
    for x, value in enumerate(line):
        if value == 'S':
            beams.add(x)
        elif value == '^' and x in beams:
            beams.remove(x)
            beams.add(x+1)
            beams.add(x-1)
            split_count += 1
print(split_count)