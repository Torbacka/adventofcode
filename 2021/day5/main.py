import re

parser = re.compile("-?\d+")
loop = [int(x) for line in open("input/input.in").readlines() for x in parser.findall(line.strip())]
data = [line.strip() for line in open("input/input.in").readlines()]


def main():
    grid = []
    biggest_x = 0
    biggest_y = 0
    for line in data:
        start, end = line.split(" -> ")
        start_split = start.split(",")
        end_split = end.split(",")
        x1 = int(start_split[0])
        y1 = int(start_split[1])
        x2 = int(end_split[0])
        y2 = int(end_split[1])
        if x1 > biggest_x:
            biggest_x = x1
        if x2 > biggest_x:
            biggest_x = x2
        if y1 > biggest_y:
            biggest_y = y1
        if y2 > biggest_y:
            biggest_y = y2
    for x in range(0, biggest_x + 1):
        grid.append([0 for y in range(0, biggest_y + 1)])
    for line in data:
        start, end = line.split(" -> ")
        start_split = start.split(",")
        end_split = end.split(",")
        x1 = min(int(start_split[0]), int(end_split[0]))
        y1 = min(int(start_split[1]), int(end_split[1]))
        x2 = max(int(start_split[0]), int(end_split[0]))
        y2 = max(int(start_split[1]), int(end_split[1]))
        if x1 == x2:
            for i in range(y1, y2 + 1):
                grid[i][x1] += 1
        elif y1 == y2:
            for i in range(x1, x2 + 1):
                grid[y1][i] += 1
        else:
            x1 = int(start_split[0])
            y1 = int(start_split[1])
            x2 = int(end_split[0])
            y2 = int(end_split[1])
            k = int((x1 - x2) / (y1 - y2))
            points = calculcate_points(x1, x2, y1, y2, k)
            for x, y in points:
                grid[y][x] += 1
    sum2 = 0
    for i, y in enumerate(grid):
        for n, x in enumerate(grid[i]):
            if x > 1:
                sum2 += 1
    print(sum2)


def points_on_line(x1, x2, y1, y2, k):
    if x1 < x2:
        return points_on_line(x2, x1, y2, y1, k)
    ret = []
    if k < 0:
        for i in range((x1 - x2), -1, k):
            ret.append((x1 - i, y1 + i))
    else:
        for i in range(0, (x1 - x2) +1, k):
            ret.append((x1 - i, y1 - i))
    return ret


if __name__ == '__main__':
    main()
