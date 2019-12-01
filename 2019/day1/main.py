import math

pairs = [int(line.strip()) for line in open("input/input.txt").readlines()]


def main():
    fuel = 0
    for pair in pairs:
        fuel += math.floor(pair/3) - 2
    print(fuel)


if __name__ == '__main__':
    main()
