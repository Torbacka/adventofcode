import re

diff = [0, 1, -1]


def update_max(coord, max):
    temp_max = max
    if abs(coord[0]) + offset > temp_max:
        temp_max = abs(coord[0]) + offset
    if abs(coord[1]) + offset > temp_max:
        temp_max = abs(coord[1]) + offset
    if abs(coord[2]) + offset > temp_max:
        temp_max = abs(coord[2]) + offset
    return temp_max


def generate_neighbours(coord):
    neighbours = set()
    for x in diff:
        for y in diff:
            for z in diff:
                for w in diff:
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    neighbours.add((coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + w))

    return neighbours


def print_cube(active_coords):
    for z in range(-max+1, max):
        print()
        print(f"z={z}")
        for y in range(max, -max, -1):
            for x in range(-max+1, max+1):
                if x == 0 and y == 0 and z == 0:
                    print("@", end="")
                elif (x, y, z) in active_coords:
                    print("#", end="")
                else:
                    print(".", end="")
            print()


parser = re.compile("-?\d+")
data = [list(line.strip()) for line in open("input/input.in")]
active_coords = set()
offset = int(len(data) / 2)
max = 0
for y, row in enumerate(data):
    for x, value in enumerate(row):
        if value == '#':
            active_coord = (x-offset, offset - y, 0, 0)
            active_coords.add(active_coord)
            max = update_max(active_coord, max)


for i in range(6):
    new_active_coords = set()
    new_max = max
    for y in range(-max, max+1):
        for x in range(-max, max +1):
            for z in range(-max, max+1):
                for w in range(-max, max+1):
                    current_coord = (x, y, z, w)
                    neighbours = generate_neighbours(current_coord)
                    active_neighbours = set()
                    for neighbour in neighbours:
                        if neighbour in active_coords:
                            active_neighbours.add(neighbour)
                            if len(active_neighbours) > 3:
                                break
                    if current_coord in active_coords and (len(active_neighbours) == 2 or len(active_neighbours) == 3):
                        new_active_coords.add(current_coord)
                        new_max = update_max(current_coord, new_max)
                    elif len(active_neighbours) == 3:
                        new_active_coords.add(current_coord)
                        new_max = update_max(current_coord, new_max)
    max = new_max
    active_coords = new_active_coords

print(len(active_coords))