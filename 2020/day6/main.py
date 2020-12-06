import re

group = set()
count = 0
new_group = True
for line in open("input/input.in").readlines():
    if len(line) == 1:
        count += len(group)
        group = set()
        new_group = True
    else:
        if new_group:
            group = line.strip()[:]
            new_group = False
        else:
            temp = set()
            for c in line.strip():
                if c in group:
                    temp.add(c)
            group = temp

print(count)