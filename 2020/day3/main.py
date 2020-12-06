import re

data = [list(line.strip()) for line in open("input/input.in")]
score = 1
for y in range(2):
    y += 1
    for n in range(4):
        x = 2 * n + 1
        if y == 2 and x > 1:
            break
        trees = 0
        for i in range(0, len(data)):
            if i * y > len(data):
                break
            if data[i * y][(i * x) % len(data[i * y])] == '#':
                trees += 1
        if x == 3 and y == 1:
            print(trees)
        score *= trees

print(score)
