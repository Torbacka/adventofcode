from collections import defaultdict
import re
data = [list(map(int, re.findall("-?\d+", line))) for line in open("input/input.in").readlines()]


def main():
    matrix = defaultdict(lambda: 0)
    for x1, y1, x2, y2 in data:
        points = points_on_line(convert_to_int((x1, y1)), convert_to_int((x2, y2)))
        for point in points:
                matrix[point] += 1
    print(sum(1 for v in matrix.values() if v >= 2))


def convert_to_int(string_numbers):
    return tuple(map(int, string_numbers))


def points_on_line(point1, point2):
    yield point2
    # Vertical line
    if point1[0] == point2[0]:
        for y in range(point1[1], point2[1], 1 if point1[1] < point2[1] else -1):
            yield point1[0], y
    # Horizontal line
    elif point1[1] == point2[1]:
        for x in range(point1[0], point2[0], 1 if point1[0] < point2[0] else -1):
            yield x, point1[1]
    else:
        k = int((point1[1] - point2[1]) / (point1[0] - point2[0]))
        step = 1 if point1[0] < point2[0] else -1
        for m in range(0, (point2[0] - point1[0]), step):
            yield (point1[0] + m), (point1[1] + m * k)


if __name__ == '__main__':
    main()
