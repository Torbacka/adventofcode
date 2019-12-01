import math

pairs = [int(line.strip()) for line in open("input/input.txt").readlines()]


def main():
    fuel_total = 0
    for pair in pairs:
        fuel = math.floor(pair/3) - 2
        while fuel > 0:
            fuel_total += fuel
            fuel = math.floor(fuel / 3) - 2
    print(fuel_total)


if __name__ == '__main__':
    main()
