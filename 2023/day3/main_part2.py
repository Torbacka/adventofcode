data = [[c for c in line.strip()] for line in open("input/input.in").readlines()]
sum = 0
for y, line in enumerate(data):
    number = set()
    for x, c in enumerate(line):
        if c == '*':
            points = [(y - 1, x), (y - 1, x + 1), (y - 1, x - 1), (y, x - 1), (y, x + 1),
                      (y + 1, x - 1), (y + 1, x + 1), (y, x)]
            for py, px in points:
                if data[py][px].isnumeric():
                    n = ''
                    for x1 in range(px, -1, -1):
                        if not data[py][x1].isnumeric():
                            break
                        n = data[py][x1] + n
                    for x1 in range(px+1, len(data[0])):
                        if not data[py][x1].isnumeric():
                            break
                        n += data[py][x1]
                    number.add(n)
            prod = 1
            if len(number) == 2:
                for n in number:
                    prod *= int(n)
            if prod > 1:
                sum += prod
            number = set()

print(sum)
