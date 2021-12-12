import re

parser = re.compile("-?\d+")
data = [[int(x) for x in line.strip()] for line in open("input/input.in").readlines()]


def main():
    smallest_cords = []
    for y, line in enumerate(data):
        for x, number in enumerate(line):
            smallest = True
            # check left
            if x > 0:
                if line[x - 1] <= number:
                    smallest = False
            # check right
            if x < len(line) - 1:
                if line[x + 1] <= number:
                    smallest = False
            # check up
            if y > 0:
                if data[y - 1][x] <= number:
                    smallest = False
            if y < len(data) - 1:
                if data[y + 1][x] <= number:
                    smallest = False
            if smallest:
                smallest_cords.append((x, y))
    basins = []
    for cords in smallest_cords:
        checked_cords = set()
        checked_cords.add(cords)
        basins.append(calculate_basin(data, cords, checked_cords, 1))
    ans = 1
    for number in sorted(basins)[-3:]:
        ans *= number
    print(ans)


def calculate_basin(data, dot, checked_cords, basins):
    x, y = dot
    # check left
    if x > 0:
        if data[y][x - 1] != 9:
            if (x -1, y) not in checked_cords:
                checked_cords.add((x -1, y))
                basins += 1
                basins = calculate_basin(data, (x - 1, y), checked_cords, basins)
    # check right
    if x < len(data[y]) - 1:
        if data[y][x + 1] != 9:
            if (x + 1, y) not in checked_cords:
                checked_cords.add((x + 1, y))
                basins += 1
                basins = calculate_basin(data, (x + 1, y), checked_cords, basins)
    # check up
    if y > 0:
        if data[y - 1][x] != 9:
            if (x, y - 1) not in checked_cords:
                checked_cords.add((x, y - 1))
                basins += 1
                basins = calculate_basin(data, (x, y - 1), checked_cords, basins)
    if y < len(data) - 1:
        if data[y + 1][x] != 9:
            if (x, y + 1) not in checked_cords:
                checked_cords.add((x, y + 1))
                basins += 1
                basins = calculate_basin(data, (x, y + 1), checked_cords, basins)

    return basins

if __name__ == '__main__':
    main()
