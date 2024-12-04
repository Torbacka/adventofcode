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
        if value == 'X':
            for coord in coords:
                if check_boundary(x + coord[0], y + coord[1]) and check_boundary(x + (coord[0] * 2), y + (coord[1] * 2)) and check_boundary(x + (coord[0] * 3), y + (coord[1] * 3)):
                    if data[y + coord[1]][x + coord[0]] == 'M' and data[y + (coord[1] * 2)][x + (coord[0] * 2)] == 'A' and data[y + (coord[1] * 3)][x + (coord[0] * 3)] == 'S':
                        result +=1
                        output[y][x] = 'X'
                        output[y + coord[1]][x + coord[0]] = 'M'
                        output[y + (coord[1] * 2)][x + (coord[0] * 2)] = 'A'
                        output[y + (coord[1] * 3)][x + (coord[0] * 3)] = 'S'

        if value == 'S':
            for coord in coords:
                if check_boundary(x + coord[0], y + coord[1]) and check_boundary(x + (coord[0] * 2), y + (coord[1] * 2)) and check_boundary(x + (coord[0] * 3), y + (coord[1] * 3)):
                    if data[y + coord[1]][x + coord[0]] == 'A' and data[y + (coord[1] * 2)][x + (coord[0] * 2)] == 'M' and data[y + (coord[1] * 3)][x + (coord[0] * 3)] == 'X':
                        result += 1
                        output[y][x] = 'S'
                        output[y + coord[1]][x + coord[0]] = 'A'
                        output[y + (coord[1] * 2)][x + (coord[0] * 2)] = 'M'
                        output[y + (coord[1] * 3)][x + (coord[0] * 3)] = 'X'

print(result/2)
for y, line in enumerate(output):
    print()
    for x, value in enumerate(line):
        print(value, end="")