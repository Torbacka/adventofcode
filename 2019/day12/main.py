import re
from sympy import Point

parser = re.compile("-?\d+")
data = {i: {"pos": list(map(int, parser.findall(line.strip()))), 'velocity': [0, 0, 0]} for i, line in
        enumerate(open("input/input.in").readlines())}


def main():
    print(data)
    for i in range(1000):
        simulate()
    print(calculate_total_energy())


def calculate_total_energy():
    total_energy = 0
    for moon in data.values():
        potential_energy = 0
        kinetic_energy = 0
        for i, pos_cord in enumerate(moon['pos']):
            potential_energy += abs(pos_cord)
            kinetic_energy += abs(moon['velocity'][i])
        total_energy += potential_energy * kinetic_energy
    return total_energy


def simulate():
    for m, moon in enumerate(data.values()):
        for n, compare_moon in enumerate(data.values()):
            if m >= n:
                continue
            for i, coord in enumerate(compare_moon['pos']):
                if moon['pos'][i] < coord:
                    moon['velocity'][i] += 1
                    compare_moon['velocity'][i] -= 1
                if moon['pos'][i] > coord:
                    moon['velocity'][i] -= 1
                    compare_moon['velocity'][i] += 1
        for i, coord in enumerate(moon['velocity']):
            moon['pos'][i] += moon['velocity'][i]


if __name__ == '__main__':
    main()
