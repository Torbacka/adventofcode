import re
from sympy import Point

parser = re.compile("-?\d+")
data = {i: {"pos": list(map(int, parser.findall(line.strip()))), 'velocity': [0, 0, 0]} for i, line in enumerate(open("input/input.in").readlines())}


def main():
    print(data)
    simulate()
    print(data)


def simulate():
    for moon in data.values():
        acceleration = [0, 0, 0]
        for compare_moon in data.values():
            for i, coord in enumerate(compare_moon['pos']):
                if moon['pos'][i] < coord:
                    acceleration[i] += 1
                if moon['pos'][i] > coord:
                    acceleration[i] -= 1
        for i, coord in enumerate(moon['velocity']):
            moon['velocity'][i] += acceleration[i]
            moon['pos'][i] += moon['velocity'][i]


if __name__ == '__main__':
    main()
