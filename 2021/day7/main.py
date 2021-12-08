import re
from statistics import median, mean

data = [list(map(int, re.findall("-?\d+", line))) for line in open("input/input.in").readlines()]


def part_1(data):
    m = int(median(data))
    return sum(abs(d - m) for d in data)


def part_2(data):
    m = round(mean(data))
    return sum(abs(d - m) * (abs(d - m) + 1) / 2 for d in data)


if __name__ == '__main__':
    print(part_1(data[0]))
    print(part_2(data[0]))
