data = [line.strip() for line in open("input/input.in").readlines()]


def main():
    grid = {}

    for line in data:
        start, end = line.split(" -> ")
        points = points_on_line(convert_to_int(start.split(",")), convert_to_int(end.split(",")))
        for point in points:
            if point not in grid:
                grid[point] = 1
            else:
                grid[point] += 1
    sum = 0
    for point, hits in grid.items():
        if hits > 1:
            sum += 1
    print(sum)


def convert_to_int(string_numbers):
    return tuple(map(int, string_numbers))


def points_on_line(point1, point2):
    points = []
    # Check vertical line
    if point1[0] == point2[0]:
        for y in range(point1[1], point2[1], 1 if point1[1] < point2[1] else -1):
            points.append((point1[0], y))

    # check horizontal line
    elif point1[1] == point2[1]:
        for x in range(point1[0], point2[0], 1 if point1[0] < point2[0] else -1):
            points.append((x, point1[1]))

    else:
        k = int((point1[1]-point2[1])/(point1[0] - point2[0]))
        m = point1[1] - (k * point1[0])
        step = k
        if k < 0 and point1[0] < point2[0]:
            step *= -1
        elif k > 0 and point1[0] > point2[0]:
            step *= -1
        for x in range(point1[0], point2[0], step):
                y = k * x + m
                points.append((x, y))
    points.append(point2)
    return points


if __name__ == '__main__':
    main()
