data = [[c for c in line.strip()] for line in open("input/input.in").readlines()]
numbers = {}
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c != '.' and not c.isnumeric():
            points = [(y - 1, x), (y - 1, x + 1), (y - 1, x - 1), (y, x - 1), (y, x + 1),
                      (y + 1, x - 1), (y + 1, x + 1), (y, x)]
            for py, px in points:
                if data[py][px].isnumeric():
                    n = ''
                    start = (py, 0)
                    for x1 in range(px, -1, -1):
                        if not data[py][x1].isnumeric():
                            start = (py, x1)
                            break
                        n = data[py][x1] + n
                    for x1 in range(px+1, len(data[0])):
                        if not data[py][x1].isnumeric():
                            break
                        n += data[py][x1]
                    numbers[start] = int(n)

print(sum(numbers.values()))
