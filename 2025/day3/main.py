import re

parser = re.compile(r"-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]

sum = 0
for line in data:
    biggest = 0
    for i, first in enumerate(line):
        if i == len(line) - 1:
            break
        for second in line[i+1:]:
            number = int(first + second)
            if biggest < number:
                biggest = number

    sum += biggest

print(sum)