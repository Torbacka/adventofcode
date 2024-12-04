data = [[M for M in line.strip()] for line in open("input/input.in").readlines()]
coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]


def check_boundary(x_1, y_1):
    return 0 <=  x_1 < len(data[0]) and 0 <= y_1 < len(data)


output = []
for y, line in enumerate(data):
    output.append(['.' for v in line])

result = 0
for y, line in enumerate(data):
    for x, value in enumerate(line):
        if value == 'A':
            if check_boundary(x -1, y -1) and check_boundary(x +1, y -1) and check_boundary(x -1, y + 1) and check_boundary(x +1, y + 1):
                if ((data[y -1 ][x -1] == 'M' and  data[y + 1 ][x +1] == 'S') or (data[y -1 ][x -1] == 'S' and  data[y + 1 ][x +1] == 'M')) and ((data[y + 1 ][x -1] == 'M' and  data[y - 1 ][x +1] == 'S') or (data[y +1 ][x -1] == 'S' and  data[y - 1 ][x +1] == 'M')):
                    result +=1

print(result)
for y, line in enumerate(output):
    print()
    for x, value in enumerate(line):
        print(value, end="")