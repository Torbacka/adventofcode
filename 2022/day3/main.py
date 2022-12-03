import re
from curses.ascii import islower

parser = re.compile("-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]
sum = 0

for i in range(0, len(data), 3):
    lines = data[i:i + 3]
    for c in lines[0]:
        if c in lines[1] and c in lines[2]:
            if islower(c):
                to_add = (bytes(c, 'utf-8')[0] - 70 - 26)
                sum += to_add
            else:
                to_add = (bytes(c, 'utf-8')[0] - 64 + 26)
                sum += to_add
            break

print(sum)
